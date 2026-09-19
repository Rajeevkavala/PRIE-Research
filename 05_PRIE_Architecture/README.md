# Phase 05 — PRIE Architecture: Master Repository Index

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core System**: Placement Readiness Intelligence Engine (PRIE)  
**Research Phase**: Phase 05 — Architecture  
**Status**: **COMPLETE (Quality Gates G01–G17: 17/17 PASS)**  

---

## 1. Executive Directory Architecture

The `05_PRIE_Architecture` repository translates verified empirical literature findings (`Paper01`–`Paper44`), cross-paper analyses, validated research gaps (`RG1`–`RG8`), research objectives (`RO1`–`RO6`), research questions (`RQ1`–`RQ6`), testable hypotheses (`H1`–`H6`), and formal design decisions (`DD-001`–`DD-012`) into a publication-grade, mathematically grounded architecture.

All files are structured into 7 logical architectural layers and an exhaustive visual asset hub:

```
05_PRIE_Architecture/
│
├── README.md                                  <-- Master Repository Index (This File)
├── PHASE_05_IMPLEMENTATION_PLAN.md            <-- Master Execution & Planning Blueprint
├── PHASE_05_ARCHITECTURE_LEDGER.md            <-- Formal Architectural Decision Ledger
├── PHASE_05_COMPLETION_REPORT.md              <-- Authoritative Quality Gate Audit & Sign-off
│
├── [1. System Foundation & Overview]
│   ├── System_Architecture.md                 <-- 6-Layer Architecture & Operational Boundaries
│   ├── PRIE_Architecture_Overview.md          <-- 4 Intelligence Pillars & 13-Stage Lifecycle
│   └── Component_Architecture.md              <-- Structural Specs for CMP-01 through CMP-06
│
├── [2. Authoritative Profile & Feature Space]
│   └── Student_Profile_Vector_Architecture.md <-- Invariant 22-Dimensional SPV Tensor (F01-F22)
│
├── [3. Functional Modules Architecture (M01-M12)]
│   ├── Module_Architecture.md                 <-- Complete Unified Specs for All 12 Modules
│   ├── Prediction_Engine_Architecture.md      <-- M03: Dual-Track XGBoost & TFT Engine
│   ├── XAI_Architecture.md                    <-- M04: Two-Tiered TreeSHAP & DiCE Recourse
│   ├── ATS_Architecture.md                    <-- M06: 2D Spatial LayoutLMv3 + S-BERT Matcher
│   ├── Mock_Interview_Architecture.md         <-- M05: Streaming Whisper, vLLM & Wasm Vision
│   ├── Recommendation_Engine_Architecture.md  <-- M07: Constrained Topological A* DAG Traversal
│   ├── Learning_Roadmap_Architecture.md       <-- M08: Dynamic Sprints & Verification Gates
│   ├── RAG_Architecture.md                    <-- M09: ChromaDB Retrieval & Cross-Encoder
│   ├── Learning_Analytics_Architecture.md     <-- M10: Behavioral Clickstream Telemetry
│   ├── Digital_Twin_Architecture.md           <-- M11: Triangular Multi-Stakeholder Sync
│   └── Question_Generation_Architecture.md    <-- M12: Causal Concept DAG AQG with Distractors
│
├── [4. Orchestration, Communication & APIs]
│   ├── Multi_Agent_Orchestration.md           <-- AGT-00 Supervisor & Governance Mutation Gate
│   ├── Data_Flow_Architecture.md              <-- Sync (<150ms), Streaming (<1.5s), Async Flows
│   └── API_Architecture.md                    <-- OpenAPI REST Contracts & WebSocket Protocols
│
├── [5. Data & Model Serving Infrastructure]
│   ├── Data_Architecture.md                   <-- 20 Logical Entities, Relational & Hybrid ERD
│   ├── Model_Serving_Architecture.md          <-- ONNX CPU Runtime vs GPU Transformer Pools
│   ├── Technology_Stack_Architecture.md       <-- Research Demands vs Engineering Choices
│   └── Scalability_Architecture.md            <-- Stateless Services, Caching & Time Chunking
│
├── [6. Governance, Security & Failure Resilience]
│   ├── Security_Privacy_Architecture.md       <-- Zero-Trust, DP Laplace (eps <= 1.0), Cgroups
│   └── Failure_Recovery_Architecture.md       <-- 10 Failure Modes, Circuit Breakers, Fallbacks
│
├── [7. Traceability, Decisions & Validation]
│   ├── Architecture_Traceability.md           <-- 100% Trace Matrix to DD, RG, RO, RQ, H
│   ├── Architecture_Decision_Records.md       <-- Formal ADR-001 through ADR-012 Records
│   ├── Architecture_Assumptions.md            <-- 8 Formal Assumptions with Risk Protocols
│   ├── Architecture_Constraints.md            <-- Research, Compute, Latency & Privacy Limits
│   └── Architecture_Validation_Plan.md        <-- 11 Verification Dimensions mapped to EXP-1-6
│
└── diagrams/                                  <-- Complete Visual Assets Hub (14 Diagrams)
    ├── README.md                              <-- Diagram Catalog across 7 Export Formats
    ├── *.md                                   <-- 14 Markdown Documentation Diagrams
    ├── mermaid/                               <-- 14 Standalone Normal Mermaid (.mmd) Files
    ├── svg/                                   <-- 14 Infinite-Resolution Vector (.svg) Files
    ├── png/                                   <-- 14 High-Resolution Raster (.png) Files
    ├── pdf/                                   <-- 14 Publication-Ready Documents (.pdf)
    ├── excalidraw/                            <-- 14 Native Whiteboard Files (.excalidraw)
    └── drawio/                                <-- 14 Diagrams.net Project Files (.drawio)
```

---

## 2. Functional Modules Master Cross-Reference

| Module ID | Module Title | Primary Architectural Document | Primary Pipeline Diagram | Key Technologies |
| :---: | :--- | :--- | :--- | :--- |
| **M01** | **SPV Aggregation & Ingestion** | [Student_Profile_Vector_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Student_Profile_Vector_Architecture.md) | [SPV_Pipeline.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/SPV_Pipeline.md) | MICE, RobustScaler, Pydantic |
| **M02** | **Skill Gap Quantification** | [Component_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Component_Architecture.md) | [Recommendation_Pipeline.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Recommendation_Pipeline.md) | Euclidean & Cosine Subspace Distance |
| **M03** | **Placement Prediction Engine** | [Prediction_Engine_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Prediction_Engine_Architecture.md) | [Prediction_Pipeline.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Prediction_Pipeline.md) | XGBoost (ONNX Runtime CPU), TFT (LibTorch) |
| **M04** | **Explainable AI & Diagnostics** | [XAI_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/XAI_Architecture.md) | [Data_Flow_Diagram.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Data_Flow_Diagram.md) | TreeSHAP, DiCE Counterfactuals |
| **M05** | **Interactive Mock Interview** | [Mock_Interview_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Mock_Interview_Architecture.md) | [Interview_Pipeline.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Interview_Pipeline.md) | Silero VAD, Whisper, vLLM Qwen2.5, FastTTS |
| **M06** | **ATS Resume Intelligence** | [ATS_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/ATS_Architecture.md) | [ATS_Pipeline.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/ATS_Pipeline.md) | LayoutLMv3, Sentence-BERT (`all-mpnet`) |
| **M07** | **Prescriptive Recommendation** | [Recommendation_Engine_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Recommendation_Engine_Architecture.md) | [Recommendation_Pipeline.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Recommendation_Pipeline.md) | Constrained Topological $A^*$ Traversal |
| **M08** | **Personalized Learning Roadmap**| [Learning_Roadmap_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Learning_Roadmap_Architecture.md) | [PRIE_Pipeline.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/PRIE_Pipeline.md) | Dynamic Sprint Scheduling, Gate Checkers |
| **M09** | **Curriculum RAG Service** | [RAG_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/RAG_Architecture.md) | [Component_Diagram.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Component_Diagram.md) | ChromaDB, Cross-Encoder, TruLens Triad |
| **M10** | **Behavioral Telemetry Analytics**| [Learning_Analytics_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Learning_Analytics_Architecture.md) | [Learning_Feedback_Loop.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Learning_Feedback_Loop.md) | TimescaleDB Hypertables, Rolling Aggregators |
| **M11** | **Digital Twin Synchronization** | [Digital_Twin_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Digital_Twin_Architecture.md) | [Learning_Feedback_Loop.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Learning_Feedback_Loop.md) | Triangular Multi-Stakeholder Sync Daemon |
| **M12** | **Adaptive Question Generation** | [Question_Generation_Architecture.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Question_Generation_Architecture.md) | [Component_Diagram.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/Component_Diagram.md) | Causal Concept DAG Distractor Formulator |

---

## 3. Visual Assets Hub

The [`diagrams/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams) directory contains all 14 architectural diagrams in:
- **Mermaid (`.mmd`)**: Raw code for Mermaid CLI or live renderers
- **SVG (`.svg`)**: Scalable vectors for papers, presentations, and websites
- **PNG (`.png`)**: High-res bitmap renderings for quick previewing
- **PDF (`.pdf`)**: Formatted document pages
- **Excalidraw (`.excalidraw`)**: Native whiteboard canvas files for interactive editing
- **Draw.io (`.drawio`)**: Diagrams.net project files for visual engineering

Consult the [Diagrams Catalog](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/README.md) for direct download links and software instructions.
