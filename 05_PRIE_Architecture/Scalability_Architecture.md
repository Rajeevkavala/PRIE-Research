# Scalability Architecture: Stateless Microservices, Workload Isolation & Sharding Strategies

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Scalability_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Scalability Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & Scalability Principles

The Scalability Architecture defines the structural mechanisms through which PRIE handles varying institutional cohort sizes and concurrent user loads.

**Anti-Hallucination & Rigor Rule (Section 32)**:
Arbitrary, unverified capacity claims (e.g., *"PRIE infinitely scales to 10 million concurrent users"*) are strictly prohibited. Scalability is analyzed logically through:
1. **Stateless Service Decoupling**: Application and intelligence workers maintain zero local in-memory session state; all persistent states reside in managed data layers.
2. **Asynchronous Workload Partitioning**: Computationally heavy batch tasks (LayoutLMv3 resume parsing, TFT sequence training, DiCE optimization) are isolated from interactive user-facing request paths.
3. **Multi-Tiered Caching Hierarchy**: Repeated analytical queries, static concept DAG traversals, and pre-computed archetype counterfactuals are served from high-speed in-memory caches.
4. **Heterogeneous Compute Isolation**: High-throughput CPU tasks (XGBoost, TreeSHAP, SBERT) are separated onto dedicated node pools, preventing resource contention with GPU-bound workers (vLLM, LayoutLMv3).

---

## 2. Global Scalability Topology

```
                         [Incoming HTTPS / WSS Traffic]
                                       │
                                       ▼
                       ┌──────────────────────────────┐
                       │ High-Availability L7 Balancer│
                       │ (Nginx / Cloud Load Balancer)│
                       └───────────────┬──────────────┘
                                       │ Round-Robin / Least-Connections
                                       ▼
                       ┌──────────────────────────────┐
                       │ Stateless Gateway Containers │
                       │ (CMP-GW-ROUT: Autoscaled)    │
                       └───────────────┬──────────────┘
                                       │
        ┌──────────────────────────────┴──────────────────────────────┐
        │ SYNCHRONOUS INFERENCE PATH                                  │ ASYNCHRONOUS TASK QUEUE
        ▼ (< 200ms Latency SLA)                                       ▼ (Background Worker Pool)
┌──────────────────────────────┐                              ┌──────────────────────────────┐
│ Stateless Reasoning Workers  │                              │ Redis Task Broker (Cluster)  │
│ • M01: SPV Aggregator        │                              │ (CMP-INF-BUS)                │
│ • M06: XGBoost ONNX Worker   │                              └───────────────┬──────────────┘
│ • M07: TreeSHAP Worker       │                                              │
│ • M09: RAG Query Gateway     │                                              ▼
└───────────────┬──────────────┘                              ┌──────────────────────────────┐
                │                                             │ Dedicated GPU / Heavy Workers│
                ▼                                             │ • M02: LayoutLMv3 Workers    │
┌──────────────────────────────┐                              │ • M06: TFT PyTorch Sequence  │
│ In-Memory Distributed Cache  │                              │ • M07: DiCE Solver Workers   │
│ (Redis Cluster: SPV & DAG)   │                              │ • M05: Ephemeral Sandboxes   │
└───────────────┬──────────────┘                              └───────────────┬──────────────┘
                │                                                             │
                └──────────────────────────────┬──────────────────────────────┘
                                               │ Persist Verified State
                                               ▼
                               ┌──────────────────────────────┐
                               │ Scalable Storage Tier        │
                               │ • PostgreSQL (Master-Replica)│
                               │ • TimescaleDB (Hyper-Tables) │
                               │ • ChromaDB (Partitioned HNSW)│
                               └──────────────────────────────┘
```

---

## 3. Workload Isolation & Worker Provisioning

To prevent long-running tasks from degrading interactive student experiences, PRIE partitions workloads into three isolated compute pools:

| Workload Pool | Allocated Components | Scaling Trigger | Target Resources | Operational Priority |
|:---|:---|:---|:---|:---:|
| **Interactive User Pool** | `CMP-GW-ROUT`, `CMP-INT-SPV`, `CMP-INT-PRD` (XGBoost), `CMP-INT-QZ` | CPU utilization $>70\%$ or request latency $>100$ms | CPU-optimized nodes (2–4 vCPU, 4GB RAM) | **Tier 1 (Highest)** |
| **Conversational Voice Pool** | `CMP-MDL-ASR` (Whisper), `CMP-MDL-LLM` (vLLM Llama-3-8B), WebSocket Gateway | Active concurrent interview sessions | GPU nodes (NVIDIA A10G / T4) | **Tier 1 (Real-Time)** |
| **Asynchronous Batch Pool** | `CMP-INT-ATS` (LayoutLMv3), `CMP-MDL-TFT` (Longitudinal sequence), `CMP-MDL-CF` (DiCE) | Redis queue depth $>20$ tasks | Mixed CPU/GPU batch nodes | **Tier 2 (Deferred)** |
| **Sandbox Execution Pool** | `CMP-INF-BOX` (Ephemeral Docker Sandboxes) | Concurrent code test runs | Isolated bare-metal host with cgroup CPU/RAM limits | **Tier 3 (Isolated)** |

---

## 4. Multi-Tiered Caching Architecture

To minimize redundant database reads and expensive machine learning re-computations:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        MULTI-TIERED CACHING ENGINE                     │
├───────────────────┬───────────────────┬───────────────┬────────────────┤
│ CACHE TIER        │ DATA STORED       │ TTL (LIFETIME)│ INVALIDATION   │
├───────────────────┼───────────────────┼───────────────┼────────────────┤
│ Tier 1: Client    │ Static curriculum │ 24 Hours      │ Hard refresh / │
│ (Browser Cache)   │ assets, UI radar  │               │ ETag mismatch  │
├───────────────────┼───────────────────┼───────────────┼────────────────┤
│ Tier 2: Gateway   │ Verified JWT auth │ 15 Minutes    │ Session logout │
│ (Redis In-Memory) │ session tokens    │               │ or role revoke │
├───────────────────┼───────────────────┼───────────────┼────────────────┤
│ Tier 3: Profile   │ Compiled 22-dim   │ 4 Hours       │ Invalidated on │
│ (Redis In-Memory) │ SPV feature vector│               │ new test/event │
├───────────────────┼───────────────────┼───────────────┼────────────────┤
│ Tier 4: Knowledge │ Serialized CS     │ 7 Days        │ Updated when   │
│ (Redis In-Memory) │ Concept DAG       │               │ syllabus edits │
├───────────────────┼───────────────────┼───────────────┼────────────────┤
│ Tier 5: Recourse  │ Pre-computed DiCE │ Permanent     │ Updated on     │
│ (PostgreSQL Cache)│ cohort archetypes │               │ model retrain  │
└───────────────────┴───────────────────┴───────────────┴────────────────┘
```

---

## 5. Database Partitioning & Sharding Strategy

### 5.1 Relational Store (PostgreSQL)
- **Read-Write Splitting**: Implements single-primary with multiple read-replicas. All transactional student updates target the primary database; faculty cohort dashboards and recruiter analytics query read-replicas.
- **Departmental Multi-Tenancy**: Logical partitioning by `institution_id` and `department_code` ensures queries for one department never scan cross-institutional tables.

### 5.2 Time-Series Store (TimescaleDB)
- **Hyper-Table Chunking**: Telemetry event tables (`LearningEvent`) are partitioned into automatic **7-day temporal chunks**. Queries filtering by rolling weekly windows touch only active chunks, eliminating massive table scans.
- **Continuous Aggregates**: Automatically down-samples raw clickstream events into hourly and weekly summary views, reducing query latency on historical telemetry by $>90\%$.

### 5.3 Vector Database (ChromaDB)
- **Collection Partitioning**: ChromaDB indexes are segregated into isolated collections (`collection_curriculum_syllabi`, `collection_job_descriptions`, `collection_question_bank`).
- Vector search scans are bounded strictly to the relevant collection, preventing quadratic nearest-neighbor search degradation.
