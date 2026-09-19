# Multi-Agent Methodology: Specialized Supervisory Hierarchy, Tool Interfaces & Governance

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Multi_Agent_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Multi-Agent Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Anti-Proliferation Principle & Supervisory Hierarchy

PRIE strictly adheres to an **Anti-Proliferation Principle**: agents are not spawned indiscriminately. LLMs are strictly segregated from core mathematical decision logic. Mathematical computations (XGBoost, TreeSHAP, DiCE, $A^*$ search) run in deterministic code; agents serve strictly as specialized natural language interface orchestrators:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       SUPERVISORY AGENT ORCHESTRATION                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│                     ┌──────────────────────────────────┐                        │
│                     │ SUPERVISORY ORCHESTRATOR AGENT   │                        │
│                     │ (Routing, State Machine, Safety) │                        │
│                     └────────────────┬─────────────────┘                        │
│                                      │                                          │
│        ┌─────────────────────────────┼─────────────────────────────┐            │
│        ▼                             ▼                             ▼            │
│ ┌──────────────┐             ┌──────────────┐             ┌──────────────┐      │
│ │ DIAGNOSTIC   │             │ INTERVIEW    │             │ REMEDIATION  │      │
│ │ AGENT        │             │ COACH AGENT  │             │ ROADMAP AGENT│      │
│ └──────────────┘             └──────────────┘             └──────────────┘      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Specialized Agent Inventory & Tool Bindings

### Agent 1: Diagnostic Assessment Agent
- **Task**: Guides students through initial technical competency evaluations.
- **Tools**: `db_query_quiz`, `docker_sandbox_exec`, `record_score`.
- **Governing Model**: Quantized local `Llama-3-8B-Instruct`.

### Agent 2: Conversational Interview Coach Agent
- **Task**: Executes low-latency mock technical and behavioral interviews (`M05`).
- **Tools**: `whisper_stream_transcribe`, `mediapipe_kinematic_fetch`, `evaluate_response_rubric`.
- **Latency Budget**: Must yield first token within $450\text{ms}$.

### Agent 3: Remediation & Roadmap Agent
- **Task**: Translates DiCE counterfactuals into empathetic, structured weekly milestones (`M08`).
- **Tools**: `astar_dag_search`, `curriculum_rag_query`, `calendar_sync`.
- **Validation**: Every recommended milestone must pass through the deterministic Prerequisite Safety Filter.
