# PRIE Architecture Overview: High-Level Scientific Vision & Operational Lifecycle

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/PRIE_Architecture_Overview.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative High-Level Overview  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Executive Summary & Core Scientific Mission

The **Placement Readiness Intelligence Engine (PRIE)** is the central artificial intelligence and analytical core of ScholarCamp. While traditional higher education placement tools operate as fragmented, static, unexplainable, and open-loop point solutions, PRIE is formulated as an end-to-end, scientifically defensible, and closed-loop intelligence engine.

PRIE solves the **Core Research Problem (PRO)** formulated in Phase 03:
> *"How can heterogeneous multimodal student data (academic transcripts, coding test metrics, multi-column resume layouts, and conversational interview dynamics) be unified into an explainable, longitudinal, and privacy-compliant intelligence engine that accurately predicts placement outcomes and autonomously generates distance-constrained prescriptive career remediation pathways?"*

PRIE directly resolves the eight validated research gaps (`RG1`–`RG8`) through an unbroken deductive chain:
$$\text{Literature Evidence} \longrightarrow \text{Research Gaps} \longrightarrow \text{Design Decisions} \longrightarrow \text{Architectural Subsystems} \longrightarrow \text{Empirical Experiments}$$

---

## 2. The Four Pillars of PRIE Intelligence

PRIE organizes its twelve functional modules (`M01`–`M12`) across four foundational scientific pillars:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PRIE INTELLIGENCE PILLARS                       │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 1. MULTIMODAL     │ 2. DUAL-TRACK     │ 3. PRESCRIPTIVE                │
│    PERCEPTION     │    ANALYTICAL     │    ACTIONABLE                  │
│                   │    REASONING      │    REMEDIATION                 │
│ • M01: SPV        │ • M04: Skill Gap  │ • M07: DiCE Recourse           │
│ • M02: ATS Parser │ • M06: Predictor  │ • M08: Dynamic Roadmap         │
│ • M03: Quizzing   │ • M11: Telemetry  │ • M09: Curriculum RAG          │
│ • M05: Mock Coach │                   │ • M10: Causal Concept AQG      │
├───────────────────┴───────────────────┴────────────────────────────────┤
│ 4. CLOSED-LOOP TRIANGULAR GOVERNANCE & PRIVACY COMPLIANCE              │
│ • M12: Closed-Loop Digital Twin Synchronizer                           │
│ • Zero-Trust Differential Privacy Architecture (ε ≤ 1.0)               │
└────────────────────────────────────────────────────────────────────────┘
```

### Pillar 1: Multimodal Perception
- **The Challenge**: Traditional placement models rely strictly on isolated academic transcripts or flat-text resume scans, completely ignoring practical coding ability, conversational speech delivery, and non-verbal composure.
- **PRIE Countermeasure**: Unifies heterogeneous signals across transcripts, live Docker coding sandboxes (`M05`), 2D spatial layout document intelligence (`M02`), and client-side streaming speech and paralinguistics (`M05`) into a standardized 22-dimensional feature tensor (`M01`).

### Pillar 2: Dual-Track Analytical Reasoning
- **The Challenge**: Educational prediction systems evaluate candidate employability as a single, static snapshot in time, failing to capture student learning momentum, habit persistence, or early-intervention windows.
- **PRIE Countermeasure**: Deploys a **Dual-Track Predictive Architecture** (`DD-002`, `M06`):
  - *Track 1 (Cross-Sectional)*: Extreme Gradient Boosting (XGBoost) for immediate static placement tier screening ($P \in [0.0, 1.0]$).
  - *Track 2 (Longitudinal)*: Temporal Fusion Transformers (TFT) with multi-head self-attention modeling student telemetry sequences across multiple semesters (Sem 4 $\to$ Sem 7) to provide multi-horizon quantile early warnings.

### Pillar 3: Prescriptive Actionable Remediation
- **The Challenge**: The "Descriptive-to-Prescriptive Chasm" (`RG3`). Existing explainable AI in higher education stops at post-hoc attribution (e.g., standard SHAP beeswarms) telling students *why* they are unready without offering actionable, feasible steps to fix it.
- **PRIE Countermeasure**: Couples TreeSHAP with **DiCE constraint-optimized counterfactual generation** (`DD-003`, `M07`). By locking immutable features (branch, past grades) and traversing a Computer Science Causal Concept DAG (`DD-008`, `M08`), PRIE computes the exact minimum-effort path required to transition an at-risk candidate into placement readiness.

### Pillar 4: Closed-Loop Governance & Zero-Trust Privacy
- **The Challenge**: Open-loop architecture (`RG8`) where recommendations are never dynamically re-ingested into model updates, while faculty and recruiters operate in disconnected administrative silos under severe privacy liabilities.
- **PRIE Countermeasure**: Implements a **Closed-Loop Triangular Digital Twin** (`DD-010`, `M12`) synchronizing student readiness state across Student, Faculty Mentor, and Placement Cell dashboards. Student telemetry continuously recalibrates model weights, while differential privacy ($\epsilon \le 1.0$) and local on-premise execution protect sensitive candidate data (`DD-011`).

---

## 3. The End-to-End PRIE Operational Lifecycle

The PRIE runtime executes an unbroken 13-stage perception, reasoning, remediation, and feedback loop:

```
[Raw Candidate Inputs: PDF Resume, Audio/Video, Transcripts, Code]
                           │
                           ▼
                  [Stage 1: Ingestion]
                           │
                           ▼
                [Stage 2: Preprocessing]
                           │
                           ▼
           [Stage 3: 22-Dimensional SPV Tensor]
                           │
                           ▼
             [Stage 4: Prediction Engine (M06)]
             ├── Static Track 1: XGBoost (Tier)
             └── Temporal Track 2: TFT (Multi-Horizon)
                           │
                           ▼
             [Stage 5: Explainability Engine (M07)]
             ├── Descriptive: TreeSHAP Attribution
             └── Prescriptive: DiCE Feasible Recourse
                           │
                           ▼
              [Stage 6: Skill Gap Engine (M04)]
              (Weighted Euclidean / Cosine Deficit)
                           │
                           ▼
          [Stage 7: Recommendation Engine (M08/M09)]
             ├── Topological A* Search on CS Concept DAG
             └── Two-Stage Curriculum RAG Assistance
                           │
                           ▼
          [Stage 8: Dynamic Personalized Roadmap (M08)]
              (Sequenced Milestones & Prerequisites)
                           │
                           ▼
         [Stage 9: Formative Practice & Assessment]
             ├── Causal Concept AQG Diagnostic Tests (M10)
             └── Sub-1.5s Streaming Mock Interviews (M05)
                           │
                           ▼
        [Stage 10: Telemetry & Event Streaming (M11)]
          (Login Cadence, Attempt Velocity, Habit Decay)
                           │
                           ▼
           [Stage 11: Real-Time SPV Tensor Update]
                           │
                           ▼
      [Stage 12: Triangular Digital Twin Synchronization (M12)]
        (Student, Faculty Advisor, Placement Cell Dashboards)
                           │
                           ▼
               [Stage 13: Closed-Loop Feedback]
          (Adaptive Retraining & Intervention Calibration)
```

---

## 4. Methodological Grounding & Traceability Summary

Every subsystem within PRIE maps directly to the verified research corpus:

| PRIE Module | Core Scientific Function | Literature Grounding | Research Gap | Research Objective | Evaluation Protocol |
|:---|:---|:---|:---:|:---:|:---|
| **M01: SPV Aggregator** | Multimodal feature harmonization (22 dims) | **P01, P04, P06, P08, P22** | `RG1` | `RO1` | Feature ablation & collinearity benchmarks |
| **M02: ATS Matcher** | 2D Spatial OCR & dense semantic matching | **P11, P12, P17, P35, P42** | `RG4` | `RO1` | Boundary Token F1 on multi-column resumes |
| **M03: Adaptive Quiz** | Conceptual prerequisite diagnostic testing | **P02, P04, P25, P26, P39** | `RG6` | `RO5` | Item Difficulty ($p$) & Discrimination ($DI$) |
| **M04: Skill Gap Engine** | Weighted mathematical skill distance | **P04, P13, P16, P35, P41** | `RG1, RG7` | `RO4` | Correlation with interview failure rates |
| **M05: Interview Coach** | Streaming audio, client vision, Docker code sandbox | **P03, P15, P28, P29, P38** | `RG5` | `RO2` | Voice turnaround $<1.5$s; Pearson $r \ge 0.70$ |
| **M06: Prediction Engine** | Dual-track XGBoost + Temporal Fusion Transformer | **P01, P04, P18, P22, P44** | `RG2` | `RO3` | Macro-$F_1$ (static); Quantile Loss (TFT) |
| **M07: Prescriptive XAI** | TreeSHAP attribution + DiCE counterfactuals | **P18, P19, P22, P32, P34** | `RG3` | `RO4` | Actionability score $\ge 80\%$; Proximity $L_1$ |
| **M08: Roadmap Generator**| $A^*$ shortest path on CS Concept DAG | **P13, P16, P35, P41, P43** | `RG7` | `RO4` | Milestone completion rate & Catalog Coverage |
| **M09: RAG Assistant** | Curriculum vector store with Triad verification | **P20, P21, P23, P27, P40** | `RG8` | `RO5, RO6` | RAG Triad (Relevance $\ge 0.85$, Grounding $\ge 0.90$) |
| **M10: Causal AQG** | Causal Concept DAG-guided distractor generation | **P25, P26, P39** | `RG6` | `RO5` | Distractor Plausibility Index ($DPI \ge 0.70$) |
| **M11: Telemetry Engine** | Behavioral cadence & habit decay tracking | **P02, P05, P33, P44** | `RG2` | `RO3` | Early-warning sensitivity ($>85\%$) at Week 4 |
| **M12: Digital Twin** | Closed-loop multi-stakeholder synchronization | **P02, P41, P44** | `RG8` | `RO6` | Difference-in-Differences conversion uplift |

---

## 5. Architectural Quality Standard

PRIE's architecture is defined under strict non-fabrication and scientific integrity rules:
1. **Zero Fictional Modules**: No components exist simply because an architectural pattern is popular; each component exists solely to resolve a validated research void.
2. **Explicit Epistemological Status**: All components maintain formal classifications (`ESTABLISHED BY RESEARCH`, `PROPOSED ARCHITECTURE`, `EXISTING IMPLEMENTATION`, `VALIDATION REQUIRED`).
3. **Reproducibility Guarantee**: Every algorithmic and architectural parameter is mathematically defined to support experimental validation in Phase 08.
