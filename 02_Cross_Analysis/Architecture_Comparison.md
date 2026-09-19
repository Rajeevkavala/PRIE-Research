# System Architecture Comparison & Engineering Synthesis

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/Architecture_Comparison.md`  
**Status**: Authoritative Architecture Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. Architectural Paradigms in Educational & Recruitment AI

Deploying intelligent systems across universities and enterprise recruitment demands robust, scalable, and secure software architectures. Across the 44 verified papers, system architectures span four (4) distinct architectural paradigms:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            ARCHITECTURAL PARADIGMS                               │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Paradigm                      │ Representative Studies & Systems                 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Monolithic Web Portals     │ P30 (Verma et al., 2025 MERN interview portal),  │
│                               │ P38 (Kulkarni et al., 2026 PrepWise portal).     │
│ 2. Microservice & API-Driven  │ P04 (Kazi, 2025), P17 (Solanki, 2026 ResuMatch), │
│                               │ P28 (Vachkal, 2026 IndusAI FastAPI + Docker).    │
│ 3. Multi-Agent Knowledge Graph│ P13 (Ashrafi, 2023 Career-gAIde Neo4j),          │
│                               │ P25 (Wang, 2025), P41 (Babureddy Digital Twin).  │
│ 4. Real-Time Streaming WebRTC │ P29 (Wahid et al., 2026 Gemini WebRTC Stream).   │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master System Architecture Benchmark Matrix

The table below compiles a comprehensive engineering audit across the primary software architectures documented in the corpus:

| Paper ID & System | Architectural Pattern | Frontend Technology | Backend / API Framework | Database & State Storage | Sandboxing & Isolation | Throughput / Turn Latency | Deployment Readiness Tier |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **P04** (Kazi et al., 2025) | Modular Microservices | React.js SPA | Python Flask REST API | MySQL Relational DB | None (Local Execution) | ~1.5s per resume | Campus Pilot Prototype |
| **P13** (Ashrafi et al., 2023) | Graph-Augmented Agent | React + Cytoscape.js| Python FastAPI + LangChain| **Neo4j Graph Database** | None | ~2.2s per path plan | Academic Prototype |
| **P17** (Solanki et al., 2026) | High-Throughput Search | Next.js Dashboard | FastAPI + OnnxRuntime | In-Memory Faiss + BM25 | None | **~40ms per query (Fast)**| Production-Ready Engine |
| **P21** (Nisanth et al., 2025) | Local Offline RAG Node | Streamlit UI | Python FastAPI (Local) | **ChromaDB Local Vector DB**| Local GPU Isolation | ~1.8s per answer | On-Premise Campus Node |
| **P23** (Venkatesh et al., 2025)| Cloud Serverless RAG | Angular SPA | Google Cloud Run + FastAPI| Google Cloud Firestore + FAISS| Cloud VPC Isolation | ~2.2s per answer | Enterprise Cloud Pilot |
| **P25** (Wang et al., 2025) | Dual-Agent Graph Pipeline| Web Dashboard | Python Asynchronous Core | GraphML + SQLite | Dual-Agent Verification | ~4.2s per MCQ item | Laboratory Research Pipeline|
| **P28** (Vachkal et al., 2026) | Secure Microservice | React + Monaco Editor| **FastAPI Asynchronous Gateway**| PostgreSQL + Redis Cache | **Docker Container Sandbox**| ~3.5s (Code compilation) | Enterprise Alpha Stage |
| **P29** (Wahid et al., 2026) | **Real-Time WebRTC Stream**| React + WebRTC API | Python FastAPI WebRTC Server | Redis In-Memory State | None (Audio Stream) | **<1.2s (Sub-second lag)** | Production-Ready Core |
| **P30** (Verma et al., 2025) | Full-Stack MERN Monolith| React.js SPA | Express.js / Node.js Monolith| MongoDB Document Store | None | ~2.2s per turn | Campus Production Portal |
| **P36** (Suryawanshi, 2025) | Lightweight Dashboard | Streamlit Web App | Streamlit Server (Python) | Local File System | None | ~0.85s per parse | Educational Sandbox |
| **P38** (Kulkarni et al., 2026)| Full-Stack Web Portal | React.js SPA | Node.js / Express | MongoDB | None | ~1.8s per module | Student Prototype |
| **P41** (Babureddy & Mathew, 2026)| **Triangular Digital Twin**| Next.js / Tailwind UI| Multi-Agent Orchestrator | **Neo4j Graph (1,150 nodes)**| Institutional ERP Link | Real-Time State Sync | **Advanced Institutional Twin**|
| **P42** (Kapula, 2025) | Cognitive IDP Pipeline | Enterprise Web Portal| Python FastAPI + PyTorch GPU| Enterprise Document Vault | GPU Process Isolation | ~1.5s per page | Enterprise Production |
| **P43** (Rajeevan & Mini Devi)| Graph Convolution Engine| Library Web OPAC | Python Flask + PyTorch Geom | Neo4j + MARC21 Bibliographic| Read-Only Query Sandbox| ~65ms per rec | Operational Library Core |
| **P44** (Azeez & Sajjad, 2026) | Streaming Closed-Loop RL| Angular Dashboard | FastAPI + Ray RLlib | TimescaleDB Time-Series DB | Policy Action Constraints| Multi-Horizon Forecast | Operational LMS Integration |

---

## 3. Critical Architectural Bottlenecks & Solutions

### 3.1 Code Sandboxing and Security Isolation (P28 IndusAI)
- `[CROSS-PAPER OBSERVATION]` Automated technical interview systems (such as P28) must compile and execute untrusted candidate source code in real time. Executing candidate code directly on the host operating system presents catastrophic security vulnerabilities (e.g., fork bombs, file system tampering, network exfiltration).
- `[AUTHOR-STATED FACT]` Vachkal et al. (P28) solved this by provisioning ephemeral **Docker container sandboxes** with strict CPU/memory limits, read-only root filesystems, and zero network egress, returning Abstract Syntax Tree (AST) analysis and test results within 3.5 seconds.

### 3.2 Graph State vs Flat Relational Storage
- `[CROSS-PAPER OBSERVATION]` Flat relational databases (MySQL, PostgreSQL in P04, P28) degrade when modeling student competency trees, course prerequisite hierarchies, and multi-stakeholder interactions. Traversal across 5-hop prerequisite chains requires complex, computationally expensive recursive SQL joins.
- `[AUTHOR-STATED FACT]` Studies adopting **Neo4j Graph Databases** (P13, P41, P43) represent concepts, students, and recruiters as native nodes and edges, reducing multi-hop path query latency to under 15 milliseconds.

### 3.3 Audio Streaming: WebRTC vs HTTP REST Polling
- `[AUTHOR-STATED FACT]` Wahid et al. (P29) demonstrated that traditional HTTP REST request-response cycles introduce unacceptable latency in mock interview bots. Establishing a **bidirectional WebRTC streaming connection** allows continuous audio streaming and sub-1.2s conversational turns.

---

## 4. ScholarCamp / PRIE Target Enterprise Architecture

ScholarCamp / PRIE adopts an asynchronous, event-driven microservices architecture integrating Docker sandboxing, WebRTC streaming, and Neo4j graph storage:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           PRIE ENTERPRISE ARCHITECTURE                           │
├──────────────────────────────────────────────────────────────────────────────────┤
│                               CLIENT TIER (Next.js SPA)                          │
│     • Student Portal   • Faculty Mentor Dashboard   • Corporate Recruiter Console│
│     • WebAssembly Video Tracker (MediaPipe)         • Monaco Code Editor         │
├──────────────────────────────────────┬───────────────────────────────────────────┤
│                                      │                                           │
│  HTTP / REST / GraphQL               │  Bidirectional Audio / Video Stream       │
│  ▼                                   │  ▼                                        │
│  FastAPI API Gateway & Auth          │  WebRTC Streaming Gateway (P29)           │
│  ▼                                   │  ▼                                        │
│  MICROSERVICES LAYER:                │  FAST-PATH AI ENGINES:                    │
│  • Employability Service (CatBoost)  │  • openSMILE Prosody Engine (C++)         │
│  • ATS Parser (LayoutLMv3 + SBERT)   │  • Gemini 1.5 Flash Real-Time Interview   │
│  • Dynamic Analytics (TFT-RL Agent)  │  • faster-whisper ASR Transcription       │
│  • Secure Sandbox (Docker Containers)│                                           │
├──────────────────────────────────────┴───────────────────────────────────────────┤
│                                 DATA PERSISTENCE TIER                            │
│  • Neo4j Graph DB: Competency DAG, Course Trees, Triangular Digital Twin (P41)   │
│  • ChromaDB / FAISS: Dense Curriculum Vector Embeddings for Local RAG (P21, P23) │
│  • PostgreSQL / TimescaleDB: Temporal Clickstream Logs & Grade Records (P44)     │
│  • Redis: Session Caching, Asynchronous Task Queues & WebRTC State Storage       │
└──────────────────────────────────────────────────────────────────────────────────┘
```
