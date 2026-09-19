# PRIE System Architecture: 6-Layer Hierarchical Design & System Boundaries

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/System_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative System Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. System Vision & Architectural Philosophy

The Placement Readiness Intelligence Engine (PRIE) is designed to overcome the structural fragmentation of higher education career preparation systems. As demonstrated across Phases 01–04, existing systems fail because they operate as isolated, static, unexplainable, and non-actionable point solutions.

PRIE is architected around the fundamental principle of **Research-Driven Cohesion**:
$$\text{Evidence (P01–P44)} \longrightarrow \text{Gaps (RG1–RG8)} \longrightarrow \text{Decisions (DD-001–DD-012)} \longrightarrow \text{Architecture (M01–M12)}$$

The architecture strictly segregates:
1. **The Scientific Research System**: The mathematical formulations, representations (SPV), predictive models, explainability engines, and experimental validation boundaries designed to test Hypotheses **`H1`–`H6`**.
2. **The Engineering Substrate**: The distributed runtime, API gateways, ephemeral sandboxes, vector databases, and asynchronous event buses that make the scientific system deployable, robust, and privacy-compliant.

---

## 2. Global 6-Layer Architectural Hierarchy

PRIE is organized into six explicitly decoupled architectural layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: USER & INTERACTION LAYER                                      │
│ Student Hub | Faculty Mentorship | Placement Portal | Mock Interview UI│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ HTTPS / WSS / Client Wasm
┌───────────────────────────────────▼────────────────────────────────────┐
│ LAYER 2: APPLICATION & API GATEWAY LAYER                               │
│ API Gateway | JWT Auth & RBAC | Request Router | DP Anonymizer         │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Validated Requests / Event Messages
┌───────────────────────────────────▼────────────────────────────────────┐
│ LAYER 3: PRIE INTELLIGENCE & REASONING LAYER                           │
│ M01 (SPV) | M02 (ATS) | M03 (Quiz) | M04 (Gap) | M05 (Coach)          │
│ M06 (Predict) | M07 (XAI) | M08 (Roadmap) | M09 (RAG) | M10 (AQG)      │
│ M11 (Telemetry) | M12 (Digital Twin Synchronizer)                      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Feature Tensors / Context Vectors
┌───────────────────────────────────▼────────────────────────────────────┐
│ LAYER 4: AI & ML MODEL EXECUTION LAYER                                 │
│ XGBoost | TFT | LayoutLMv3 | SBERT | Whisper | TreeSHAP | DiCE | vLLM   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ State Persist / Read / Embeddings
┌───────────────────────────────────▼────────────────────────────────────┐
│ LAYER 5: DATA & KNOWLEDGE LAYER                                        │
│ SPV Store | ChromaDB Vector Store | CS Concept DAG | Privacy Audit Log │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Virtualization / Container Execution
┌───────────────────────────────────▼────────────────────────────────────┐
│ LAYER 6: INFRASTRUCTURE & EXECUTION LAYER                              │
│ Docker Sandboxes | Model Registry | Redis Bus | Telemetry Observer    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Layer Specifications & Operational Boundaries

### 3.1 Layer 1: User & Interaction Layer
- **Purpose**: Provides role-specific, responsive, and secure presentation interfaces for all primary stakeholders.
- **Components**:
  - `UI-STU`: Student Preparation & Remediation Dashboard. Surfaces the 22-dimensional readiness status, prescriptive counterfactual roadmaps, and adaptive quizzes.
  - `UI-FAC`: Faculty Advisor Mentorship Workspace. Displays aggregated cohort distributions, at-risk early warnings (Week 3–4), and intervention logs.
  - `UI-TPO`: Training & Placement Cell Portal. Provides corporate job-description alignment analytics, candidate shortlisting, and institutional conversion forecasting.
  - `UI-INT`: Multimodal Mock Interview Interface. Captures streaming microphone audio and executes client-side computer vision via WebAssembly without video uplink.
  - `UI-DOC`: Multi-Column Resume Dropzone. Supports drag-and-drop ingestion of complex PDF/DOCX resumes.
- **Architectural Constraints**:
  - Zero raw audio/video persistent storage (enforces `DD-005` and `DD-011`).
  - Client-side execution of computer vision models (`MediaPipe FaceMesh`) in browser WebAssembly to guarantee zero-trust candidate biometric privacy.

### 3.2 Layer 2: Application & API Gateway Layer
- **Purpose**: Acts as the single perimeter security boundary, managing authentication, rate limiting, request routing, and differential privacy noise injection.
- **Components**:
  - `GW-AUTH`: Authentication & Authorization Manager enforcing Role-Based Access Control (`RBAC`) via cryptographically signed JWTs.
  - `GW-ROUTE`: Reverse Proxy & Dynamic Request Router dispatching requests to synchronous intelligence services or asynchronous message brokers.
  - `GW-PRIV`: Zero-Trust Differential Privacy Proxy. Injects Laplacian noise ($\epsilon \le 1.0$) into aggregated analytical outputs surfaced to corporate recruiters and faculty dashboards (`DD-011`).
  - `GW-RATE`: Rate Limiter & Abuse Detector preventing denial-of-service and brute-force query attacks on heavy ML inference endpoints.
- **API Protocol Support**: REST (OpenAPI 3.1) for transactional requests; WebSocket (WSS) for streaming conversational audio in mock interviews.

### 3.3 Layer 3: PRIE Intelligence & Reasoning Layer
- **Purpose**: The central scientific core of the ecosystem. Implements all twelve PRIE functional modules (`M01` through `M12`).
- **Subsystem Organization**:
  - *Perceptual Ingestion*: `M01` (Student Profile Vector Aggregator), `M02` (Resume Intelligence & Multi-Column ATS Matcher), `M03` (Adaptive Assessment & Quizzing), `M05` (Multimodal Mock Interview Coach).
  - *Analytical Reasoning*: `M04` (Skill Gap Analysis & Distance Engine), `M06` (Placement Readiness Prediction Engine — Dual Track), `M11` (Behavioral Telemetry & Longitudinal Analytics).
  - *Actionable Remediation & Closed-Loop*: `M07` (Prescriptive Explainability & Counterfactual Engine), `M08` (Dynamic Personalized Roadmap Generator), `M09` (Curriculum RAG Assistant), `M10` (Causal Concept-Guided AQG), `M12` (Triangular Digital Twin Orchestrator).
- **Communication Pattern**: Decoupled, stateless microservices communicating internally via high-performance gRPC or internal REST with shared data stores.

### 3.4 Layer 4: AI & ML Model Execution Layer
- **Purpose**: Encapsulates model inference, feature tensor formatting, and explainability calculations across heterogeneous machine learning architectures.
- **Model Portfolio & Roles**:
  - `XGBoost`: Primary static cross-sectional placement readiness classifier (`DD-002`, `M06`).
  - `Temporal Fusion Transformer (TFT)`: Multi-horizon sequence forecaster modeling multi-semester academic and telemetry trajectories (`DD-002`, `M06`).
  - `LayoutLMv3`: Vision-language document intelligence transformer preserving 2D spatial bounding boxes for multi-column resumes (`DD-004`, `M02`).
  - `Sentence-BERT (all-MiniLM-L6-v2)`: Dense 384-dimensional bi-encoder generating semantic embeddings for resumes and job descriptions (`M02`).
  - `Whisper ASR`: Streaming chunked speech-to-text transcription engine (`DD-005`, `M05`).
  - `TreeSHAP`: Exact cooperative game-theoretic feature attribution for tree models (`DD-003`, `M07`).
  - `DiCE (Diverse Counterfactual Explanations)`: Constraint-optimized loss minimization over SPV input space to generate feasible prescriptive recourse (`DD-003`, `M07`).
  - `Quantized Llama-3-8B-Instruct (via vLLM)`: Lightweight local conversational SLM for interview follow-ups and RAG synthesis (`DD-005`, `M05`, `M09`).

### 3.5 Layer 5: Data & Knowledge Layer
- **Purpose**: Provides persistent, specialized storage engines tailored to relational, vector, graph, and temporal data geometries.
- **Data Stores**:
  - `SPV-DB`: High-performance relational and document store maintaining authoritative student profiles, academic histories, and 22-dimensional feature tensors.
  - `VEC-DB (ChromaDB)`: Vector database indexing dense embeddings of college course syllabi, university placement archives, and corporate Job Descriptions.
  - `DAG-DB`: Graph store managing the Computer Science Causal Concept Directed Acyclic Graph (DAG) for prerequisite roadmap traversal and distractor generation.
  - `LOG-DB`: Time-series telemetry database capturing granular interaction timestamps, session durations, quiz attempts, and habit decay markers.
  - `AUDIT-DB`: Append-only tamper-evident audit ledger tracking data access, model inferences, and differential privacy accounting.

### 3.6 Layer 6: Infrastructure & Execution Layer
- **Purpose**: Provides isolated execution environments, asynchronous messaging, model lifecycle management, and end-to-end system observability.
- **Components**:
  - `BOX-EXEC`: Ephemeral Docker Container Sandboxes for secure, unprivileged execution of live student coding submissions during interviews and tests (`DD-006`).
  - `REG-MDL`: Centralized Model Registry tracking versioned ONNX and PyTorch model artifacts, hyperparameter manifests, and training provenance.
  - `BUS-MSG`: Redis / Celery asynchronous message broker managing decoupled background tasks (e.g., heavy LayoutLMv3 resume parsing, longitudinal TFT forecasting).
  - `OBS-MON`: Prometheus & Grafana observability pipeline tracking system latency, API throughput, model prediction drift, and data quality degradation.

---

## 4. System Boundaries & Cross-Cutting Constraints

### 4.1 Synchronous vs Asynchronous Execution Boundary
To maintain interactive system responsiveness under bounded compute budgets:
- **Synchronous Boundary ($<1.5$s Latency)**: User authentication, static placement tier inference (`XGBoost`), TreeSHAP local attribution, streaming conversational interview dialogue (`Whisper` + local SLM), and interactive quiz generation.
- **Asynchronous Boundary (Deferred / Queue-Driven)**: 2D spatial layout resume parsing (`LayoutLMv3`), longitudinal TFT multi-semester forecasting, DiCE counterfactual optimization searches, batch model retraining, and differential privacy noise calibration.

### 4.2 Research vs Engineering Separation
| Aspect | Research Architecture Standard | Engineering Architecture Standard |
|:---|:---|:---|
| **Primary Metric** | Scientific defensibility, statistical validity, $F_1$, Quantile Loss, Item Discrimination. | Latency, throughput, availability, memory footprint, CPU utilization. |
| **Model Justification** | Grounded in empirical literature benchmarks (`P01`–`P44`) and formal inductive biases. | Evaluated for containerizability, cold-start latency, and hardware constraints. |
| **Data Integrity** | Strict prevention of look-ahead bias and feature target leakage. | ACID compliance, idempotent writes, zero-trust cryptographic hashing. |
| **Explainability** | Theoretical consistency (Shapley axioms) and causal feasibility (DiCE). | Render speed, JSON schema standardization, and visualization payload size. |

---

## 5. Architectural Invariance Verification

This architecture guarantees strict invariance to the foundational research decisions:
1. **The 22 Dimensions of the SPV** are the invariant interface across Layers 3, 4, and 5.
2. **The 12 Functional Modules (`M01`–`M12`)** map one-to-one to the validated research gaps (`RG1`–`RG8`).
3. **Zero Untraceable Technologies**: Every runtime component directly supports an established research requirement or operational constraint.
