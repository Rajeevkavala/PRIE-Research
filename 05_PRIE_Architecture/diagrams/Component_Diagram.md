# PRIE Component Diagram: Structural Wiring & Subsystem Interconnects

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/diagrams/Component_Diagram.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Component Wiring Diagram  

---

## 1. Description & Structural Purpose

The Component Diagram visualizes the structural decoupling, interfaces, ports, and data bindings between the physical components specified in `Component_Architecture.md`.

---

## 2. Mermaid Structural Component Diagram

```mermaid
graph LR
    %% Client Tier
    subgraph TIER_CLIENT["Presentation & Client Components (Layer 1)"]
        UI_STU["CMP-UI-STU<br/>Student Hub"]
        UI_INT["CMP-UI-INT<br/>Wasm Perceiver"]
        UI_FAC["CMP-UI-FAC<br/>Mentor Hub"]
        UI_TPO["CMP-UI-TPO<br/>Recruiter Hub"]
    end

    %% Gateway Tier
    subgraph TIER_GATEWAY["Security & Gateway Components (Layer 2)"]
        GW_ROUT["CMP-GW-ROUT<br/>Request Router"]
        GW_AUTH["CMP-GW-AUTH<br/>JWT/RBAC Guard"]
        GW_PRIV["CMP-GW-PRIV<br/>DP Laplace Proxy"]
    end

    %% Intelligence Subsystems (Layer 3)
    subgraph TIER_INTEL["PRIE Intelligence Subsystems (Layer 3)"]
        INT_SPV["CMP-INT-SPV<br/>M01: SPV Aggregator"]
        INT_ATS["CMP-INT-ATS<br/>M02: ATS Matcher"]
        INT_QZ["CMP-INT-QZ<br/>M03: Adaptive Quiz"]
        INT_GAP["CMP-INT-GAP<br/>M04: Skill Gap Engine"]
        INT_INT["CMP-INT-INT<br/>M05: Interview Coach"]
        INT_PRD["CMP-INT-PRD<br/>M06: Predictor Engine"]
        INT_XAI["CMP-INT-XAI<br/>M07: Prescriptive XAI"]
        INT_REC["CMP-INT-REC<br/>M08: Roadmap Generator"]
        INT_RAG["CMP-INT-RAG<br/>M09: Curriculum RAG"]
        INT_AQG["CMP-INT-AQG<br/>M10: Causal AQG"]
        INT_TEL["CMP-INT-TEL<br/>M11: Telemetry Engine"]
        INT_DTW["CMP-INT-DTW<br/>M12: Digital Twin Sync"]
    end

    %% Model Execution Workers (Layer 4)
    subgraph TIER_MODELS["AI & ML Execution Workers (Layer 4)"]
        MDL_XGB["CMP-MDL-XGB<br/>XGBoost ONNX"]
        MDL_TFT["CMP-MDL-TFT<br/>PyTorch TFT"]
        MDL_DOC["CMP-MDL-DOC<br/>LayoutLMv3 FP16"]
        MDL_SEM["CMP-MDL-SEM<br/>SBERT Bi-Encoder"]
        MDL_ASR["CMP-MDL-ASR<br/>Whisper ASR"]
        MDL_LLM["CMP-MDL-LLM<br/>vLLM Llama-3-8B"]
        MDL_SHP["CMP-MDL-SHP<br/>TreeSHAP Lib"]
        MDL_CF["CMP-MDL-CF<br/>DiCE Solver"]
    end

    %% Data Stores (Layer 5)
    subgraph TIER_DATA["Data & Knowledge Stores (Layer 5)"]
        DAT_SPV["CMP-DAT-SPV<br/>PostgreSQL SPV DB"]
        DAT_VEC["CMP-DAT-VEC<br/>ChromaDB Vector Store"]
        DAT_DAG["CMP-DAT-DAG<br/>CS Concept DAG"]
        DAT_LOG["CMP-DAT-LOG<br/>TimescaleDB Telemetry"]
    end

    %% Infrastructure (Layer 6)
    subgraph TIER_INFRA["Infrastructure Components (Layer 6)"]
        INF_BOX["CMP-INF-BOX<br/>Docker Sandbox Manager"]
        INF_BUS["CMP-INF-BUS<br/>Redis Broker"]
    end

    %% Client -> Gateway
    UI_STU --> GW_ROUT
    UI_INT -->|WSS Audio/Telemetry| GW_ROUT
    UI_FAC --> GW_ROUT
    UI_TPO --> GW_PRIV
    GW_PRIV --> GW_ROUT
    GW_ROUT <--> GW_AUTH

    %% Gateway -> Intelligence
    GW_ROUT --> INT_SPV
    GW_ROUT --> INT_ATS
    GW_ROUT --> INT_QZ
    GW_ROUT --> INT_INT
    GW_ROUT --> INT_PRD
    GW_ROUT --> INT_RAG
    GW_ROUT --> INT_DTW

    %% Internal Subsystem Wirings
    INT_ATS -->|F13, F14| INT_SPV
    INT_TEL -->|F16, F19, F21| INT_SPV
    INT_SPV -->|SPV_Tensor| INT_PRD
    INT_SPV -->|SPV_Tensor| INT_GAP
    INT_GAP -->|Missing Skills| INT_REC
    INT_PRD -->|Tier / Prob| INT_XAI
    INT_XAI -->|Counterfactual Delta| INT_REC
    INT_REC -->|Active Sprints| INT_DTW
    INT_AQG -->|Assessment Items| INT_QZ

    %% Intelligence -> Model Workers
    INT_PRD --> MDL_XGB
    INT_PRD --> MDL_TFT
    INT_ATS --> MDL_DOC
    INT_ATS --> MDL_SEM
    INT_INT --> MDL_ASR
    INT_INT --> MDL_LLM
    INT_XAI --> MDL_SHP
    INT_XAI --> MDL_CF
    INT_RAG --> MDL_SEM
    INT_RAG --> MDL_LLM
    INT_AQG --> MDL_LLM

    %% Intelligence -> Data Stores
    INT_SPV <--> DAT_SPV
    INT_ATS <--> DAT_VEC
    INT_RAG <--> DAT_VEC
    INT_REC <--> DAT_DAG
    INT_AQG <--> DAT_DAG
    INT_TEL <--> DAT_LOG

    %% Sandboxes & Bus
    INT_INT <--> INF_BOX
    INT_TEL <--> INF_BUS

    %% Styling
    classDef clientStyle fill:#1e293b,stroke:#0ea5e9,stroke-width:2px,color:#fff;
    classDef gwStyle fill:#1e293b,stroke:#6366f1,stroke-width:2px,color:#fff;
    classDef intStyle fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff;
    classDef mdlStyle fill:#1e293b,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef datStyle fill:#1e293b,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef infStyle fill:#1e293b,stroke:#f59e0b,stroke-width:2px,color:#fff;

    class UI_STU,UI_INT,UI_FAC,UI_TPO clientStyle;
    class GW_ROUT,GW_AUTH,GW_PRIV gwStyle;
    class INT_SPV,INT_ATS,INT_QZ,INT_GAP,INT_INT,INT_PRD,INT_XAI,INT_REC,INT_RAG,INT_AQG,INT_TEL,INT_DTW intStyle;
    class MDL_XGB,MDL_TFT,MDL_DOC,MDL_SEM,MDL_ASR,MDL_LLM,MDL_SHP,MDL_CF mdlStyle;
    class DAT_SPV,DAT_VEC,DAT_DAG,DAT_LOG datStyle;
    class INF_BOX,INF_BUS infStyle;
```

---

## 3. Consistency Verification

- **Component Naming Match**: 100% congruent with the `CMP-*` naming schema defined in `Component_Architecture.md`.
- **Interface Traceability**: Every port and arrow represents an established gRPC, REST, or database communication protocol.
