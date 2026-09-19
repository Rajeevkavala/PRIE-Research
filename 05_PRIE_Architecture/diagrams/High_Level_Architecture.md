# PRIE High-Level Architecture Diagram: 6-Layer Hierarchical System Design

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/diagrams/High_Level_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative High-Level Architecture Diagram  

---

## 1. Description & Structural Overview

This diagram formalizes the 6-layer decoupled architecture of PRIE, depicting the downward flow of user requests and data ingestion, horizontal interactions between intelligence components, and persistent interactions with models, data, and infrastructure.

---

## 2. Mermaid 6-Layer Architecture Blueprint

```mermaid
graph TD
    %% Layer 1: User & Interaction Layer
    subgraph L1["LAYER 1: USER & INTERACTION LAYER"]
        UI_STU["Student Hub UI<br/>(Readiness Radar, Roadmaps)"]
        UI_FAC["Faculty Mentor Workspace<br/>(At-Risk Alerts, Cohort View)"]
        UI_TPO["Placement Cell Analytics<br/>(Job Alignment, DP Views)"]
        UI_INT["Mock Interview Client<br/>(Wasm MediaPipe, Audio Worklet)"]
        UI_DOC["Resume Dropzone UI<br/>(PDF/DOCX Drag & Drop)"]
    end

    %% Layer 2: Application & API Gateway Layer
    subgraph L2["LAYER 2: APPLICATION & API GATEWAY LAYER"]
        APIGW["Secure API Gateway (Reverse Proxy / Nginx)"]
        AUTH["JWT Authentication & RBAC Engine"]
        DP_PROXY["Differential Privacy Proxy (CMP-GW-PRIV)<br/>• Injects Laplace Noise (eps <= 1.0)"]
        ROUTER["Dynamic Request Router & Rate Limiter"]
    end

    %% Layer 3: PRIE Intelligence Layer
    subgraph L3["LAYER 3: PRIE INTELLIGENCE & REASONING LAYER"]
        subgraph L3_PERCEPT["Perception & Ingestion"]
            M01["M01: SPV Aggregator & Harmonizer"]
            M02["M02: ATS Document Matcher"]
            M03["M03: Adaptive Diagnostic Quizzing"]
            M05["M05: Multimodal Mock Interview Coach"]
        end
        
        subgraph L3_REASON["Analytical Reasoning"]
            M04["M04: Skill Gap & Distance Engine"]
            M06["M06: Placement Predictor (Dual-Track)"]
            M11["M11: Behavioral Telemetry Analytics"]
        end
        
        subgraph L3_ACTION["Actionable Remediation & Closed-Loop"]
            M07["M07: Prescriptive XAI (TreeSHAP + DiCE)"]
            M08["M08: Dynamic Roadmap Generator"]
            M09["M09: Two-Stage Curriculum RAG"]
            M10["M10: Causal Concept AQG Engine"]
            M12["M12: Triangular Digital Twin Sync"]
        end
    end

    %% Layer 4: AI & ML Model Layer
    subgraph L4["LAYER 4: AI & ML MODEL EXECUTION LAYER"]
        MDL_XGB["XGBoost GBDT<br/>(ONNX Runtime CPU, <5ms)"]
        MDL_TFT["Temporal Fusion Transformer<br/>(PyTorch GPU, Quantiles)"]
        MDL_DOC["LayoutLMv3 Spatial Transformer<br/>(ONNX FP16, Bounding Boxes)"]
        MDL_SEM["Sentence-BERT Bi-Encoder<br/>(all-MiniLM-L6-v2, 384d)"]
        MDL_ASR["Whisper ASR Streaming Engine<br/>(whisper.cpp, Sub-250ms chunks)"]
        MDL_LLM["Local Quantized Llama-3-8B<br/>(vLLM AWQ 4-bit, TTFT <350ms)"]
        MDL_SHP["TreeSHAP Attribution Worker<br/>(Exact polynomial O(T L D^2))"]
        MDL_CF["DiCE Counterfactual Optimizer<br/>(Constrained Loss Minimizer)"]
    end

    %% Layer 5: Data & Knowledge Layer
    subgraph L5["LAYER 5: DATA & KNOWLEDGE LAYER"]
        DB_SPV["SPV Store & History<br/>(PostgreSQL / TimescaleDB)"]
        DB_VEC["Vector Store<br/>(ChromaDB HNSW: Syllabi, JDs)"]
        DB_DAG["CS Concept Prerequisite DAG<br/>(Graph Ontology Store)"]
        DB_AUDIT["Immutable Audit Ledger<br/>(Tamper-Evident Access Logs)"]
    end

    %% Layer 6: Infrastructure Layer
    subgraph L6["LAYER 6: INFRASTRUCTURE & EXECUTION LAYER"]
        BOX["Ephemeral Docker Sandbox Manager<br/>(--net=none, 128MB RAM, 5s timeout)"]
        BROKER["Redis Message Broker & Task Queue<br/>(Asynchronous Celery Workers)"]
        REGISTRY["Model Artifact Registry (REG-MDL)<br/>(Versioned ONNX & PyTorch Models)"]
        OBS["Observability & Drift Monitor<br/>(Prometheus, Grafana, PSI/KS)"]
    end

    %% Cross-Layer Connections
    L1 -->|HTTPS / WSS| L2
    L2 -->|Authenticated Requests| L3
    L3 <-->|Inference Calls / Predictions| L4
    L3 <-->|CRUD & State Snapshots| L5
    L4 <-->|Load Versioned Artifacts| REGISTRY
    L3 <-->|Dispatch Heavy Tasks| BROKER
    M05 <-->|Spin Up Secure Containers| BOX
    L3 -->|Emit Performance Metrics| OBS

    %% Styling
    classDef l1Style fill:#1e293b,stroke:#0ea5e9,stroke-width:2px,color:#fff;
    classDef l2Style fill:#1e293b,stroke:#6366f1,stroke-width:2px,color:#fff;
    classDef l3Style fill:#0f172a,stroke:#38bdf8,stroke-width:3px,color:#fff;
    classDef l4Style fill:#1e293b,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef l5Style fill:#1e293b,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef l6Style fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;

    class UI_STU,UI_FAC,UI_TPO,UI_INT,UI_DOC l1Style;
    class APIGW,AUTH,DP_PROXY,ROUTER l2Style;
    class M01,M02,M03,M04,M05,M06,M07,M08,M09,M10,M11,M12 l3Style;
    class MDL_XGB,MDL_TFT,MDL_DOC,MDL_SEM,MDL_ASR,MDL_LLM,MDL_SHP,MDL_CF l4Style;
    class DB_SPV,DB_VEC,DB_DAG,DB_AUDIT l5Style;
    class BOX,BROKER,REGISTRY,OBS l6Style;
```

---

## 3. Consistency Verification

- **Layer Completeness**: All 6 architectural layers codified in `System_Architecture.md` are represented.
- **Module Coverage**: All twelve modules (`M01` through `M12`) are positioned within Layer 3.
- **Model Isolation**: Layer 4 explicitly isolates all 8 model execution workers.
- **Infrastructure Alignment**: Layer 6 models the ephemeral Docker sandboxes (`DD-006`), Redis broker, model registry, and observability stack.
