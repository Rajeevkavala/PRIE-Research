# PHASE 07 — COMPLETE CODEBASE RESEARCH-READINESS AUDIT
## ScholarCamp Core System: PRIE (Placement Readiness Intelligence Engine)
**Document Status:** Complete Deep-Readiness & Architectural Conformance Audit  
**Authoritative Context:** Phases 01–06 (Research Foundation, Cross-Analysis, Problem Statement, Evidence Ledgers, Architecture, Methodology)  
**Target Directory:** `07_Implementation/`  
**Execution Date:** September 2026 (Audit Baseline)  
**Implementation Modification Policy:** Strict Read-Only Analysis — Zero Code Modified  

---

## 1. Executive Summary

### 1.1 Audit Context & Objectives
This audit provides a comprehensive, evidence-grounded research-readiness evaluation of the existing implementation artifacts within `07_Implementation/` for the **Placement Readiness Intelligence Engine (PRIE)** of ScholarCamp. 

In strict adherence to the research hierarchy, **Phases 01 through 06 are authoritative**. The existing implementation in `07_Implementation/` represents a combination of legacy prototype scripts, exploratory notebooks, and an initial clean refactoring attempt (`PRIE_v1/`). Under no circumstances is the existing code assumed to be correct, complete, or research-valid where it diverges from or falls short of the theoretical, architectural, and methodological standards established in Phases 01–06.

### 1.2 Dual-Codebase Discovery
Investigation of `07_Implementation/` revealed the coexistence of **two separate, unmerged, and conflicting implementation branches**:
1. **Legacy Prototype (`07_Implementation/src/`, `configs/`, `models/`, `notebooks/`)**:
   - Monolithic Streamlit application intended to run via `src/app.py`.
   - SQLite database (`src/database/`).
   - 13 ad-hoc functional modules (`src/modules/`).
   - Serialized machine learning artifacts (`models/xgb_model.pkl`, `scaler.pkl`, `feature_names.json`, `jd_embeddings.npy`, `jd_metadata.json`).
   - Exploratory Jupyter notebooks (`notebooks/ScholarCamp_PRIE_Google_Colab.ipynb`, `notebooks/ScholarCamp_PRIE_Research_From_Scratch.ipynb`).
2. **Clean v1 Implementation (`07_Implementation/PRIE_v1/`)**:
   - Modern decoupled architecture featuring a FastAPI REST backend (`backend/main.py`).
   - Vanilla HTML5/CSS3/ES6 JavaScript frontend (`frontend/`).
   - Sub-package modularization structured around architecture modules (`backend/modules/m01` through `m12`, with `m05` completely missing).
   - Dedicated database abstraction (`backend/database/`).
   - Model artifact directory (`backend/models/`) which is **completely empty** (0 model files).

### 1.3 Key Audit Findings
| Audit Dimension | Status | Primary Finding | Research Impact |
| :--- | :--- | :--- | :--- |
| **SPV Schema Conformance** | **CRITICAL FAILURE** | Legacy code uses divergent 22D schema (`backlogs`, `internship_months`, `skill_count`) omitting core canonical features (`os_score`, `soft_skills_score`, `project_quality_score`). `PRIE_v1` adopts canonical F01–F22 schema but lacks trained models. | Models trained on legacy schema cannot test Hypotheses H1–H6 or validate canonical SPV. |
| **Model Artifact Provenance** | **INVALID** | `models/xgb_model.pkl` is verified to originate from Colab Cell 29, trained on 1,200 *synthetic* pseudo-random rows using legacy schema. Zero empirical datasets used. | Ineligible for research paper submission or empirical benchmark claims. |
| **Application Executability** | **BROKEN** | Legacy Streamlit entry point (`src/app.py`) crashes on launch due to missing `pages/` directory. Path resolution bug in `src/config.py` forces fallback dummy model generation on every request. | Prototype cannot be demonstrated or evaluated end-to-end without immediate fixes. |
| **Architectural Completeness** | **PARTIAL** | M05 (Mock Interview Coach) is completely missing from `PRIE_v1`; legacy M05 is offline audio-only. M02 (ATS) lacks LayoutLMv3 spatial NER. M07 (XAI) stubs out DiCE counterfactuals. M09 (RAG), M10 (AQG), and M12 (Digital Twin) are empty stubs. | Experiments EXP-2, EXP-3, EXP-4, and EXP-6 cannot be executed with current codebase. |
| **Data Leakage & Integrity** | **HIGH RISK** | Telemetry features in legacy SPV are hardcoded constants (`gap_score=0.35`, `behavior_score=0.65`, etc.). Synthetic generator lacks temporal masking and student group isolation. | Risk of invalid inflated experimental results and baseline contamination. |
| **Security & Production Readiness**| **VULNERABLE** | Hardcoded JWT secrets (`SECRET_KEY`), missing rate limiting, unsanitized file paths in resume processing, unauthenticated API routers. | Unsafe for live student trials or campus deployment. |

### 1.4 Final Audit Verdict
**REQUIRES IMPLEMENTATION WORK** — The codebase contains valuable algorithmic building blocks (specifically within `PRIE_v1/backend/spv_version.py`, `backend/ml/`, and `src/modules/explainability.py`), but suffers from severe schema divergence, missing core modules, invalid synthetic model weights, and broken UI entry points. A disciplined, research-aligned consolidation into a unified research architecture is mandatory before empirical experimentation can proceed.

---

## 2. Reading Audit

To ensure absolute fidelity to the established research, an exhaustive read of all upstream documentation and design artifacts across Phases 01 through 06 was executed prior to auditing code.

### 2.1 Inventory of Discovered and Read Files
```
==================================================================================================
PRIE PHASE 01–06 COMPREHENSIVE READING LEDGER
==================================================================================================
PHASE 01: RESEARCH FOUNDATION (01_Research_Foundation/)
├── 44 Verified Primary Research Papers (PDFs & BibTeX records cataloged)
│   ├── Paper 01–10: Predictive Modeling, Feature Selection, and Academic Early Warning
│   ├── Paper 11–20: Explainable AI in Education (SHAP, LIME, Counterfactual Recourse)
│   ├── Paper 21–30: Resume Intelligence, LayoutLM Spatial NER, and Skill Extraction
│   ├── Paper 31–40: Multimodal Interview Assessment (Librosa Prosody, MediaPipe Vision, Whisper)
│   └── Paper 41–44: Benchmark Studies (Paper41 Babureddy, Paper44 Azeez, Paper42 Kapula, Paper15 Inamdar)
├── Literature Review Syntheses & Taxonomy Ledgers
└── Primary Gap Ledgers (Identifying CG1–CG8)

PHASE 02: CROSS ANALYSIS (02_Cross_Analysis/)
├── Comparative Algorithmic Trade-off Matrices (Tree Ensembles vs. Deep Neural Networks)
├── Feature Importance & Redundancy Cross-Evaluations
└── Multimodal Fusion Paradigms (Early vs. Late vs. Hybrid Attention)

PHASE 03: RESEARCH PROBLEM (03_Research_Problem/)
├── Formal Problem Formulation Document
├── Research Questions Specification: RQ1 through RQ6
├── Hypotheses Specification: H1 through H6
├── Research Objectives Specification: RO1 through RO6
└── Core Research Gaps Specification: CG1 through CG8

PHASE 04: RESEARCH EVIDENCE (04_Research_Evidence/)
├── Design Decisions Ledger: DD-001 through DD-012
├── Feature Traceability Ledger: Canonical 22-Dimensional SPV Mapping (F01–F22)
└── Empirical Baseline Ledgers (Babureddy 2024, Azeez 2024, Kapula 2024 benchmarks)

PHASE 05: PRIE ARCHITECTURE (05_PRIE_Architecture/)
├── System_Architecture.md & Component_Architecture.md
├── Module_Architecture.md (Authoritative M01 through M12 definitions)
├── Student_Profile_Vector_Architecture.md (Canonical SPV Mathematical & Structural Spec)
├── Data_Architecture.md & API_Architecture.md
├── Diagrams (Mermaid, Excalidraw, SVG, PNG, PDF):
│   ├── System_Architecture.mmd, Component_Architecture.mmd, Data_Flow.mmd
│   ├── SPV_Pipeline.mmd, Prediction_Pipeline.mmd, Recommendation_Pipeline.mmd
│   ├── ATS_Pipeline.mmd, Interview_Pipeline.mmd, Agent_Orchestration.mmd
│   └── Model_Serving.mmd, RAG_Architecture.mmd, System_Context.mmd

PHASE 06: METHODOLOGY (06_Methodology/)
├── Research_Design.md & Methodology_Overview.md & Research_Workflow.md
├── Experimental_Framework.md (Authoritative EXP-1 through EXP-6 definitions)
├── Dataset Methodology (DS-BENCH-01, DS-BENCH-02, DS-CORPUS-01, DS-SYNTH-01, DS-REAL-01)
├── Preprocessing, Feature Engineering & Selection (SPV normalization, SMOTE rules)
├── Model Selection, Hyperparameter Optimization, Validation & Calibration Protocols
├── Explainability (SHAP TreeExplainer & DiCE Feasibility Constraints)
├── Multimodal Interview Processing (Librosa acoustic, Whisper text, MediaPipe action units)
├── Dynamic Remediation (Prerequisite DAG, Kahn's Topological Sort)
├── Evaluation Metrics, Statistical Significance Protocols (Wilcoxon, McNemar, Friedman)
└── Reproducibility, Randomness, Seed Management, and Ethical Safeguards

PHASE 07: IMPLEMENTATION (07_Implementation/)
├── Legacy Prototype: configs/config.json, models/*, notebooks/*, src/*, src/modules/*
└── Clean v1 Prototype: PRIE_v1/backend/*, PRIE_v1/frontend/*, PRIE_v1/data/*
==================================================================================================
```

### 2.2 Phase 05 Architectural Diagram Conformance & Inconsistencies
A critical cross-comparison between the text specifications in Phase 05 and the architectural diagrams (`05_PRIE_Architecture/diagrams/mermaid/`) revealed a major schema discrepancy:

```
+--------------------------------------------------------------------------------------------------+
| DIAGRAM DISCREPANCY: SPV_Pipeline.mmd vs. Student_Profile_Vector_Architecture.md                 |
+--------------------------------------------------------------------------------------------------+
| File: 05_PRIE_Architecture/diagrams/mermaid/SPV_Pipeline.mmd (Lines 39–72)                       |
| Diagram Content:                                                                                 |
|   F01: cgpa                   F09: hackathons_won             F17: github_contributions          |
|   F02: backlogs_history       F10: certifications_count       F18: branch_tier                   |
|   F03: dsa_score              F11: leetcode_problems_solved   F19: college_tier                  |
|   F04: dbms_score             F12: resume_ats_score           F20: assessment_velocity           |
|   F05: system_design_score    F13: technical_interview_score  F21: behavior_consistency          |
|   F06: aptitude_score         F14: hr_interview_score         F22: mock_interview_count          |
|   F07: soft_skills_score      F15: skill_gap_index                                               |
|   F08: project_count          F16: tech_stack_breadth                                            |
+--------------------------------------------------------------------------------------------------+
| VS.                                                                                              |
| Authoritative Text: Student_Profile_Vector_Architecture.md & Feature_Traceability.md             |
|   F01: cgpa                   F09: project_count              F17: branch_encoded                |
|   F02: dsa_score              F10: project_quality_score      F18: target_role_encoded           |
|   F03: dbms_score             F11: has_internship             F19: assessment_attempts           |
|   F04: os_score               F12: certifications_count       F20: behavior_score                |
|   F05: cn_score               F13: resume_ats_score           F21: engagement_score              |
|   F06: programming_score      F14: cosine_similarity          F22: roadmap_completion_rate       |
|   F07: aptitude_score         F15: gap_score                                                     |
|   F08: soft_skills_score      F16: consistency_score                                             |
+--------------------------------------------------------------------------------------------------+
```
**Resolution & Ruling**: The text specification in `Student_Profile_Vector_Architecture.md` and the evidence ledgers in `04_Research_Evidence/Feature_Traceability.md` are authoritative. The diagram `SPV_Pipeline.mmd` represents an un-synchronized exploratory drafting state that must be updated to match the canonical F01–F22 ledger.

---

## 3. Research Context Summary

### 3.1 ScholarCamp PRIE Mission & Architecture
PRIE (Placement Readiness Intelligence Engine) is an AI-driven, multi-component diagnostic and remediation platform designed to overcome the structural failures of traditional Higher Education placement cells: opaque scoring, uncalibrated binary placement predictions, lack of actionable student guidance, and generic course recommendations.

PRIE solves this through an integrated pipeline:
1. Multi-dimensional diagnostic ingestion across academic records, technical assessments, ATS-compliant resume evaluation, and multimodal mock interviews.
2. Canonical 22-Dimensional Student Profile Vector (SPV) synthesis.
3. Well-calibrated, explainable placement probability prediction via cost-sensitive, Platt-scaled XGBoost.
4. Prescriptive counterfactual recourse (DiCE) providing actionable, cost-minimized developmental targets.
5. Dynamic, prerequisite-constrained learning roadmaps formulated via Directed Acyclic Graphs (DAGs) and Kahn's topological sort.
6. Contextual placement intelligence via Domain-Specific RAG and Bloom's Automated Question Generation (AQG).

### 3.2 Authoritative Research Framework Summary
* **Research Questions**:
  * **RQ1 (Predictive Calibration)**: Can an ensemble ML pipeline calibrated with Platt Scaling achieve high calibration fidelity (Brier Score $\le 0.08$) and discrimination (AUC-ROC $\ge 0.88$) on heterogeneous student data?
  * **RQ2 (Prescriptive Explainability)**: Does providing counterfactual recourse (DiCE) alongside local feature attributions (SHAP) significantly improve student placement readiness and user agency over feature attributions alone?
  * **RQ3 (Multimodal Behavioral Fusion)**: Does late fusion of acoustic prosody, facial Action Units, and NLP semantic coherence reliably assess behavioral readiness and correlate with HR placement evaluations ($F1 \ge 0.82$)?
  * **RQ4 (Spatial-Semantic Document Parsing)**: Does 2D spatial multimodal document modeling (LayoutLMv3) outperform 1D sequential token classification for dense, multi-column technical resume parsing ($F1 \ge 0.89$)?
  * **RQ5 (Prerequisite-Constrained Remediation)**: Does dynamic DAG-based topological curriculum sequencing accelerate student skill gap remediation velocity ($\ge 25\%$) compared to unconstrained greedy recommendation?
  * **RQ6 (Contextual Intelligence & Self-Efficacy)**: Does fine-grained domain-specific RAG coupled with automated Bloom's question generation improve interview self-efficacy while maintaining low factual hallucination ($\le 5\%$)?
* **Core Hypotheses**: $H1$ through $H6$ corresponding directly to $RQ1$–$RQ6$.
* **Primary Research Gaps**:
  * `CG1`: Lack of multi-dimensional feature synthesis (isolated academic scoring).
  * `CG2`: Pervasive uncalibrated model overconfidence in educational predictive modeling.
  * `CG3`: Descriptive "black-box" predictions lacking actionable recourse or developmental paths.
  * `CG4`: Superficial keyword-matching ATS tools lacking 2D spatial layout comprehension.
  * `CG5`: Absence of objective, multimodal behavioral interview coaching.
  * `CG6`: Unstructured, unranked course lists lacking prerequisite-dependency enforcement.
  * `CG7`: Generic, ungrounded conversational agents prone to domain hallucination.
  * `CG8`: Static assessments lacking item response calibration or adaptive difficulty.

---

## 4. Current Codebase Architecture

### 4.1 Comparative Architectural Topology
The filesystem within `07_Implementation/` hosts two radically different structural organizations:

```
==================================================================================================
07_Implementation/ CODEBASE TOPOLOGY
==================================================================================================
LEGACY PROTOTYPE (Streamlit Monolith)         CLEAN V1 PROTOTYPE (FastAPI + Vanilla Web)
├── configs/config.json                       ├── backend/
├── models/                                   │   ├── api/ (v1 REST endpoints)
│   ├── xgb_model.pkl (Synthetic 1200 rows)   │   ├── config.py
│   ├── scaler.pkl                            │   ├── database/ (db_manager.py, schema.sql)
│   ├── feature_names.json (Legacy 22D)       │   ├── main.py (FastAPI application factory)
│   ├── jd_embeddings.npy                     │   ├── ml/ (predictor, explainer, data generator)
│   └── jd_metadata.json                      │   ├── modules/ (m01, m02, m03, m04, m06, m07,
├── notebooks/                                │   │            m08, m09, m10, m11, m12; NO M05)
│   ├── ScholarCamp_PRIE_Google_Colab.ipynb   │   ├── spv_version.py (Canonical 22D SPV schema)
│   └── ScholarCamp_PRIE_Research_From_...    │   └── tests/ (test_api.py, test_spv.py)
├── src/                                      ├── data/ (prie_v1.db SQLite)
│   ├── app.py (Broken Streamlit entry)       └── frontend/
│   ├── config.py (Broken paths)                  ├── index.html, dashboard.html, etc.
│   ├── database/ (schema.sql, db_manager)        ├── css/style.css
│   ├── modules/ (13 unaligned modules)           └── js/ (api.js, dashboard.js, etc.)
│   └── utils/
==================================================================================================
```

### 4.2 Structural and Semantic Divergence Analysis
1. **Frontend / Application Paradigm**:
   - The legacy prototype relies on Streamlit (`src/app.py`). While fast for one-off prototyping, Streamlit enforces a single-threaded server-side state model that cannot support WebRTC media streaming for mock interviews, sub-millisecond DOM manipulation, or complex custom dashboard layouts.
   - `PRIE_v1` adopts a decoupled architecture: an asynchronous FastAPI backend serving static HTML/CSS/JavaScript. This directly satisfies the ScholarCamp clean UI mandate.
2. **Module Decomposition**:
   - Legacy modules are named functionally without architectural mapping (`placement_predictor.py`, `student_profiling.py`, `resume_intelligence.py`).
   - `PRIE_v1` organizes modules by architectural identifier (`m01_profiling`, `m02_ats`, `m03_quiz`, `m04_gap`, `m06_predictor`, `m07_xai`, `m08_roadmap`, `m09_rag`, `m10_aqg`, `m11_company`, `m12_twin`). However, **M05 (Mock Interview) was completely omitted from `PRIE_v1`**.
3. **Configuration & Environment**:
   - Legacy configuration in `configs/config.json` hardcodes divergent SPV feature lists and weights.
   - `src/config.py` incorrectly computes its base path relative to `src/`, causing model resolution failures.
   - `PRIE_v1/backend/config.py` relies on `pydantic-settings` with `.env` overrides, representing a significantly cleaner foundation.

---

## 5. Actual Execution Flow

### 5.1 Legacy Execution Flow (`07_Implementation/src/`)
Tracing the execution of the legacy prototype reveals immediate critical runtime blockers:

```
[User invokes: streamlit run src/app.py]
  │
  ├──> Imports streamlit, config.py, db_manager.py, student_profiling.py, etc.
  │
  ├──> src/config.py executes:
  │      BASE_DIR = Path(__file__).resolve().parent  --> Resolves to: 07_Implementation/src
  │      MODELS_DIR = BASE_DIR / "models"            --> Resolves to: 07_Implementation/src/models [DOES NOT EXIST]
  │
  ├──> src/app.py executes navigation setup (Lines 112–125):
  │      pages = [
  │          st.Page("pages/01_login.py", title="Login"),
  │          st.Page("pages/02_dashboard.py", title="Dashboard"),
  │          ...
  │          st.Page("pages/10_admin.py", title="Admin Portal")
  │      ]
  │      CRITICAL ERROR: Directory "07_Implementation/pages" DOES NOT EXIST!
  │      CRITICAL ERROR: Directory "07_Implementation/src/pages" DOES NOT EXIST!
  │      --> Streamlit raises FileNotFoundError and aborts execution immediately.
```

If individual modules are executed in isolation or via test harnesses:
```
[Profile Ingestion & Inference Path]
  │
  ├──> student_profiling.py receives raw student inputs (CGPA, assessment scores)
  │      Telemetry features are hardcoded:
  │        gap_score = 0.35, consistency_score = 0.60, behavior_score = 0.65,
  │        engagement_score = 0.70, roadmap_completion_rate = 0.30
  │      Arbitrary overrides applied:
  │        if certifications == 0: certifications = 1
  │        if projects == 0: projects = 2
  │
  ├──> SPV assembled: [cgpa, dsa_score, dbms_score, cn_score, aptitude_score, backlogs, ...]
  │      (22 features, but 3 features conflict with canonical schema)
  │
  ├──> placement_predictor.py attempts to load model:
  │      Looks in: 07_Implementation/src/models/xgb_model.pkl (Not found)
  │      Catches exception silently!
  │      Executes fallback: trains a 10-tree dummy XGBoost model on 10 random samples on the fly!
  │
  ├──> Predicts placement probability using uncalibrated dummy model.
  │
  └──> explainability.py attempts TreeExplainer:
         Computes SHAP values on dummy model.
         DiCE counterfactual generation is stubbed: returns fixed rule-based text hints.
```

### 5.2 Clean v1 Execution Flow (`07_Implementation/PRIE_v1/`)
Tracing the execution flow in `PRIE_v1`:

```
[User invokes: uvicorn backend.main:app --reload]
  │
  ├──> backend/main.py initializes FastAPI application.
  │      Registers CORS middleware (configured with wildcard origins).
  │      Mounts API routers: /api/v1/auth, /api/v1/students, /api/v1/predictions,
  │                          /api/v1/roadmaps, /api/v1/assessments.
  │      Mounts static frontend: / -> frontend/
  │
  ├──> Database initialization:
  │      db_manager.py initializes SQLite database at data/prie_v1.db.
  │      Executes schema.sql (14 well-structured tables).
  │
  ├──> Client accesses http://localhost:8000:
  │      Serves frontend/index.html.
  │      User logs in -> POST /api/v1/auth/login -> returns mock JWT token.
  │      Redirects to frontend/dashboard.html.
  │
  ├──> Dashboard triggers API calls:
  │      GET /api/v1/students/STU001/profile -> returns profile data.
  │      POST /api/v1/predictions/predict:
  │        m06_predictor calls ml/placement_predictor.py.
  │        Predictor looks in backend/models/xgb_model.pkl -> DIRECTORY EMPTY!
  │        Falls back to dummy model trained on 60 random normal samples!
  │        Returns synthetic probability and mock SHAP attributions.
  │
  └──> Assessment & Roadmap triggers:
         POST /api/v1/assessments/quiz/submit -> records score in SQLite.
         POST /api/v1/roadmaps/generate -> m08_roadmap runs Kahn's topological
         sort on a hardcoded 20-node DAG. Returns sequenced milestones.
```

---

## 6. Module-by-Module Audit

Every module across both codebases was audited against its code, functionality, and upstream research requirements.

### 6.1 Audit Matrix: Legacy Implementation (`07_Implementation/src/modules/`)

```
====================================================================================================
MODULE AUDIT TABLE: LEGACY PROTOTYPE (07_Implementation/src/modules/)
====================================================================================================
Module File                  Actual Status          Research Mapping   Primary Code Flaw
----------------------------------------------------------------------------------------------------
student_profiling.py         PARTIALLY IMPLEMENTED  M01 (SPV)          Divergent features; hardcoded telemetry
resume_intelligence.py       DEMO ONLY              M02 (ATS)          Regex only; no LayoutLMv3 spatial NER
assessment_engine.py         PARTIALLY IMPLEMENTED  M03 (Quiz)         Heuristic ladder; no IRT Rasch ability
skill_gap_engine.py          IMPLEMENTED            M04 (Gap)          Cosine similarity functional on mock JDs
mock_interview.py            DEMO ONLY              M05 (Interview)    Offline audio-only; no video or late fusion
placement_predictor.py       PARTIALLY IMPLEMENTED  M06 (Predictor)    Path bug forces dummy model; uncalibrated
explainability.py            PARTIALLY IMPLEMENTED  M07 (XAI)          SHAP works; DiCE counterfactuals stubbed
roadmap_generator.py         DEMO ONLY              M08 (Roadmap)      Greedy list slicing; no DAG constraints
behavior_analyzer.py         STUB / PLACEHOLDER     Auxiliary / M01    Rule-based mock telemetry scoring
company_predictor.py         PARTIALLY IMPLEMENTED  M11 (Company)      Euclidean distance to mock company benchmarks
prie_orchestrator.py         DEMO ONLY              System Pipeline    Chains modules in-memory; no async queue
recommendation_engine.py     DUPLICATED / DEMO      M04 / M08          Overlaps roadmap_generator and skill_gap
sus_evaluator.py             RESEARCH-SUPPORTING    Evaluation (H2)    Calculates System Usability Scale scores
====================================================================================================
```

### 6.2 Audit Matrix: Clean v1 Implementation (`07_Implementation/PRIE_v1/backend/modules/`)

```
====================================================================================================
MODULE AUDIT TABLE: CLEAN V1 PROTOTYPE (07_Implementation/PRIE_v1/backend/modules/)
====================================================================================================
Module Sub-Package           Actual Status          Research Mapping   Primary Code Flaw
----------------------------------------------------------------------------------------------------
m01_profiling/               RESEARCH-READY (CODE)  M01 (SPV)          Canonical F01–F22 schema implemented
m02_ats/                     STUB / DEMO            M02 (ATS)          Pure regex fallback; no LayoutLMv3
m03_quiz/                    PARTIALLY IMPLEMENTED  M03 (Quiz)         3-tier difficulty; lacks IRT estimation
m04_gap/                     IMPLEMENTED            M04 (Gap)          Embedding cosine gap calculation functional
m05 (MOCK INTERVIEW)         NOT IMPLEMENTED        M05 (Interview)    ENTIRE MODULE MISSING FROM PRIE_v1
m06_predictor/               PARTIALLY IMPLEMENTED  M06 (Predictor)    No model files in models/; dummy fallback
m07_xai/                     PARTIALLY IMPLEMENTED  M07 (XAI)          SHAP functional; DiCE is mock rule-based
m08_roadmap/                 RESEARCH-READY (LOGIC) M08 (Roadmap)      Kahn's DAG topological sort implemented
m09_rag/                     STUB / PLACEHOLDER     M09 (RAG)          Mock responses; no ChromaDB / FAISS
m10_aqg/                     STUB / PLACEHOLDER     M10 (AQG)          Mock template generation; no LLM call
m11_company/                 IMPLEMENTED            M11 (Company)      Weighted composite benchmark matcher
m12_twin/                    STUB / PLACEHOLDER     M12 (Digital Twin) Perturbation math stub; not connected
====================================================================================================
```

### 6.3 Detailed Evidence Ledger for Critical Modules

#### Module M01: Student Profiling & SPV Assembly
```
FILE:
07_Implementation/src/modules/student_profiling.py

FINDING:
Divergent SPV feature schema, hardcoded telemetry, and arbitrary data manipulation.

EVIDENCE:
Lines 54–68:
    profile_vector = [
        data.get("cgpa", 0.0),
        data.get("dsa_score", 0.0),
        data.get("dbms_score", 0.0),
        data.get("cn_score", 0.0),
        data.get("aptitude_score", 0.0),
        data.get("backlogs", 0),               # <-- NOT IN CANONICAL 22D SPV
        data.get("internship_months", 0),      # <-- NOT IN CANONICAL 22D SPV
        data.get("skill_count", 0),            # <-- NOT IN CANONICAL 22D SPV
        ...
    ]
Lines 78–82:
    # Telemetry defaults hardcoded to arbitrary constants
    gap_score = 0.35
    consistency_score = 0.60
    behavior_score = 0.65
    engagement_score = 0.70
    roadmap_completion_rate = 0.30
Lines 89–93:
    if certifications == 0: certifications = 1  # Arbitrary silent data falsification
    if projects == 0: projects = 2              # Arbitrary silent data falsification

RESEARCH IMPACT:
Violates Phase 04 Feature Traceability (DD-001, DD-002) and Phase 05 SPV Architecture.
Omission of os_score, soft_skills_score, and project_quality_score prevents valid evaluation
of technical curriculum breadth. Silent data inflation destroys empirical data integrity.

RECOMMENDATION:
Deprecate src/modules/student_profiling.py. Adopt PRIE_v1/backend/spv_version.py which strictly
enforces the canonical F01–F22 vector structure and authentic telemetry derivation.

PRIORITY:
CRITICAL
```

#### Module M02: Resume Intelligence & ATS Parsing
```
FILE:
07_Implementation/src/modules/resume_intelligence.py & PRIE_v1/backend/modules/m02_ats/

FINDING:
Absence of 2D spatial document parsing (LayoutLMv3); reliance on brittle 1D regex heuristics.

EVIDENCE:
07_Implementation/src/modules/resume_intelligence.py, Lines 42–58:
    def extract_text_from_pdf(pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() # Flat unstructured text dump
        return text

    def extract_skills_regex(text, skill_dict):
        # Brittle keyword matching against flat text string
        found = [s for s in skill_dict if re.search(r'\b' + re.escape(s) + r'\b', text, re.I)]
        return found

RESEARCH IMPACT:
Directly invalidates Hypothesis H4 and Experiment EXP-4. Research Foundation Paper 21–30
and Phase 06 Methodology mandate LayoutLMv3 fine-tuning on multi-column resumes with bounding-box
spatial coordinates (x0, y0, x1, y1). Current code cannot parse complex 2-column templates.

RECOMMENDATION:
Implement LayoutLMv3 token classification pipeline with bounding-box feature extraction using
PyMuPDF visual words dictionary, preserving regex as an explicit ablation baseline only.

PRIORITY:
HIGH
```

#### Module M05: Multimodal Mock Interview Coach
```
FILE:
07_Implementation/src/modules/mock_interview.py (and absence in PRIE_v1)

FINDING:
Module M05 is completely missing from PRIE_v1. Legacy prototype is an offline audio-only script
lacking visual processing, multimodal fusion, and real-time streaming interfaces.

EVIDENCE:
07_Implementation/src/modules/mock_interview.py:
    - Analyzes pre-recorded .wav files using Librosa (pitch, jitter, shimmer, tempo) and Whisper.
    - Zero facial action unit extraction (MediaPipe / OpenCV).
    - Zero Late Fusion architecture (no weighted tensor combination of prosody, vision, semantics).
    - Zero WebRTC streaming interface for browser-based interaction.
    - PRIE_v1/backend/modules/ has NO m05 directory whatsoever.

RESEARCH IMPACT:
Blocks Hypothesis H3 and Experiment EXP-3 completely. PRIE cannot demonstrate its core
behavioral competency assessment or evaluate multimodal fusion gains over unimodal baselines.

RECOMMENDATION:
Create PRIE_v1/backend/modules/m05_interview/ implementing:
1. WebRTC / WebSocket audio-video chunk ingestion.
2. OpenCV/MediaPipe facial landmark & emotion action unit extractor.
3. Librosa prosodic feature extractor + Whisper transcription.
4. Late Multimodal Fusion network combining acoustic, visual, and semantic embeddings.

PRIORITY:
CRITICAL
```

#### Module M06: Placement Predictor & Model Calibration
```
FILE:
07_Implementation/src/modules/placement_predictor.py & PRIE_v1/backend/ml/placement_predictor.py

FINDING:
Model loading fails silently, falling back to dynamic uncalibrated dummy models; absence of
runtime Platt/Isotonic calibration enforcement.

EVIDENCE:
07_Implementation/src/modules/placement_predictor.py, Lines 35–48:
    try:
        with open(self.model_path, "rb") as f:
            self.model = pickle.load(f)
    except Exception as e:
        logger.warning(f"Failed to load model from {self.model_path}: {e}. Training fallback.")
        self.model = self._train_fallback_model() # Trains 10-tree XGBoost on 10 random samples!

07_Implementation/PRIE_v1/backend/ml/placement_predictor.py, Lines 42–56:
    if not self.model_path.exists():
        # Directory backend/models/ is empty
        self.model = self._create_dummy_model() # Trains on 60 synthetic normal samples

RESEARCH IMPACT:
Directly invalidates Hypothesis H1 and Experiment EXP-1. Predictions served to the API and UI
are generated by 10-row or 60-row random noise models. Probability outputs are uncalibrated,
violating Brier score calibration requirements ($Brier \le 0.08$).

RECOMMENDATION:
1. Establish automated training pipeline script (`scripts/train_canonical_spv.py`).
2. Train XGBoost on canonical 22D SPV dataset with CalibratedClassifierCV (Platt scaling).
3. Serialize calibrated model and scaler to `backend/models/` with sha256 checksums.
4. Replace silent dummy training with explicit fatal initialization errors in production mode.

PRIORITY:
CRITICAL
```

#### Module M07: Prescriptive Explainability & Counterfactual Recourse
```
FILE:
07_Implementation/src/modules/explainability.py & PRIE_v1/backend/modules/m07_xai/

FINDING:
DiCE counterfactual recourse optimization is completely un-implemented; uses static rule-based hints.

EVIDENCE:
07_Implementation/src/modules/explainability.py, Lines 88–104:
    def get_counterfactual_plan(self, student_vector, target_class=1):
        # Stubbed out: does NOT call dice_ml.Dice
        # Uses hardcoded directional logic:
        plan = []
        if student_vector[1] < 70: # dsa_score
            plan.append({"feature": "dsa_score", "current": student_vector[1], "target": 75})
        return plan

RESEARCH IMPACT:
Blocks Hypothesis H2 and Experiment EXP-2. Phase 06 Methodology explicitly defines DiCE
optimization under feasibility constraints (fixing non-actionable features like `branch_encoded`
and bounding actionable features like `dsa_score` within realistic semester deltas $\Delta \le 15\%$).
Heuristic rules cannot validate the mathematical optimization of counterfactual loss functions.

RECOMMENDATION:
Integrate `dice_ml` Explainer with `ModelInterface` wrapping the calibrated XGBoost pipeline.
Enforce feature immutability masks (`features_to_vary=['dsa_score', 'certifications_count', ...]`)
and sparsity loss constraints ($k=3$ actionable levers).

PRIORITY:
HIGH
```

#### Module M08: Dynamic Learning Roadmap Generator
```
FILE:
07_Implementation/src/modules/roadmap_generator.py vs. PRIE_v1/backend/modules/m08_roadmap/

FINDING:
Legacy module uses unconstrained greedy list slicing. PRIE_v1 successfully implements Kahn's
topological DAG sorting, representing a major positive migration asset.

EVIDENCE:
07_Implementation/src/modules/roadmap_generator.py, Lines 35–45:
    # Greedy slicing without prerequisite awareness:
    missing_skills = skill_gap_result.get("missing_skills", [])
    roadmap = [{"week": i+1, "skill": skill} for i, skill in enumerate(missing_skills)]

VS.

07_Implementation/PRIE_v1/backend/modules/m08_roadmap/dag_scheduler.py, Lines 48–78:
    def kahns_topological_sort(graph, in_degree):
        queue = [n for n, deg in in_degree.items() if deg == 0]
        ordered = []
        while queue:
            curr = queue.pop(0)
            ordered.append(curr)
            for neighbor in graph.get(curr, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return ordered

RESEARCH IMPACT:
Validates the viability of Hypothesis H5 and Experiment EXP-5 in `PRIE_v1`. However, the
current DAG graph is a hardcoded 20-node mock dictionary rather than an extensible curricular
knowledge base.

RECOMMENDATION:
Retain and promote `PRIE_v1/backend/modules/m08_roadmap/`. Connect the DAG scheduler to a
persistent database of domain skills and prerequisite constraints loaded from SQLite.

PRIORITY:
MEDIUM (Refinement of existing good code)
```

---

## 7. M01–M12 Implementation Mapping

This section maps the authoritative Phase 05 Module Architecture (M01 through M12) against both implementation branches, identifying missing components and unjustified code.

```
========================================================================================================================
AUTHORITATIVE ARCHITECTURE MAPPING TABLE (M01–M12)
========================================================================================================================
Arch ID  Module Name                     Legacy Prototype File          PRIE_v1 Package            Implementation Status
------------------------------------------------------------------------------------------------------------------------
M01      Student Profiling & SPV         src/modules/student_profil...  backend/modules/m01_pro... PARTIALLY IMPLEMENTED
M02      Resume Intelligence & ATS       src/modules/resume_intelli...  backend/modules/m02_ats/   DEMO / STUB (Regex only)
M03      Adaptive Quiz & Assessment      src/modules/assessment_eng...  backend/modules/m03_quiz/  PARTIALLY IMPLEMENTED
M04      Skill Gap & Benchmark Engine    src/modules/skill_gap_engi...  backend/modules/m04_gap/   IMPLEMENTED (Mock JDs)
M05      Mock Interview Coach            src/modules/mock_interview.py  [MISSING ENTIRELY]         BROKEN / UNIMPLEMENTED
M06      Placement Predictor & Calib.    src/modules/placement_pred...  backend/modules/m06_pre... PARTIALLY IMPLEMENTED
M07      Prescriptive XAI & Counterfact. src/modules/explainability.py  backend/modules/m07_xai/   PARTIALLY IMPLEMENTED
M08      Dynamic Roadmap Generator       src/modules/roadmap_genera...  backend/modules/m08_roa... RESEARCH-READY (v1 DAG)
M09      RAG Placement Assistant         [NOT IMPLEMENTED]              backend/modules/m09_rag/   STUB / PLACEHOLDER
M10      Automated Question Gen (AQG)    [NOT IMPLEMENTED]              backend/modules/m10_aqg/   STUB / PLACEHOLDER
M11      Company Readiness Matcher       src/modules/company_predic...  backend/modules/m11_com... IMPLEMENTED
M12      Student Digital Twin Simulator  [NOT IMPLEMENTED]              backend/modules/m12_twin/  STUB / PLACEHOLDER
========================================================================================================================
```

### 7.1 Architecture Components with Zero Implementation
1. **M05 Multimodal Streaming & Visual Tracking Pipeline**:
   - `CMP-INT-001` (MediaPipe Face & Pose Action Unit Estimator): **ZERO CODE**.
   - `CMP-INT-002` (Late Multimodal Fusion Layer): **ZERO CODE**.
   - `CMP-INT-003` (WebRTC / Secure Audio-Video Ingestion Buffer): **ZERO CODE**.
2. **M09 Vector Knowledge Retrieval & RAG Store**:
   - `CMP-RAG-001` (ChromaDB / FAISS Persistent Placement Knowledge Vector Index): **ZERO CODE** (Both branches use in-memory strings or stubs).
   - `CMP-RAG-002` (Contextual Guardrail & Hallucination Filter): **ZERO CODE**.
3. **M10 Bloom's Taxonomy Automated Question Generation**:
   - `CMP-AQG-001` (Few-Shot Question Prompt Generator with Difficulty Calibration): **ZERO CODE**.
4. **M12 Digital Twin State Perturbation Engine**:
   - `CMP-TWN-001` (What-If SPV Forward Simulation & Milestone Sensitivity Matrix): **ZERO CODE**.

### 7.2 Implementations with Zero Architecture Justification
1. **`src/modules/behavior_analyzer.py`**:
   - Implements arbitrary pseudo-psychological scoring rules (`behavior_score = (login_count * 0.2) + (time_spent * 0.8)`) with zero basis in research literature.
   - *Status*: Unjustified heuristic. Must be replaced by authentic telemetry tracking.
2. **`src/modules/sus_evaluator.py`**:
   - Streamlit UI questionnaire calculating 10-item System Usability Scale scores. While valuable for human user studies, placing it as a core backend module conflates study data collection with system operational logic.
   - *Status*: Misplaced. Move to experimental study runner.

---

## 8. Research Question Traceability (RQ1–RQ6)

```
========================================================================================================================
RESEARCH QUESTION TRACEABILITY MATRIX
========================================================================================================================
RQ ID  Core Research Question                    Mapped Module(s)  Current Code Pathway?  Can Generate Research Data?
------------------------------------------------------------------------------------------------------------------------
RQ1    Calibrated Ensemble Placement Prediction   M01, M06          NO (Schema & Model Bug) NO (Requires 22D Retraining)
RQ2    Prescriptive XAI vs Feature Attribution   M06, M07          NO (DiCE is Stubbed)    NO (Requires DiCE Optimization)
RQ3    Multimodal Behavioral Interview Fusion    M05               NO (M05 Missing in v1)  NO (Requires Vision/Fusion)
RQ4    2D Spatial-Semantic Resume Intelligence   M02               NO (Regex Only)         NO (Requires LayoutLMv3)
RQ5    Dynamic Prerequisite DAG Roadmap Velocity M04, M08          PARTIAL (v1 DAG Exists) PARTIAL (Needs Longitudinal Sim)
RQ6    RAG Grounding & AQG Bloom Calibration     M09, M10          NO (Stubs Only)         NO (Requires Vector Store/LLM)
========================================================================================================================
```

### 8.1 Detailed RQ Pathway Gap Analysis
* **RQ1 (Predictive Calibration)**:
  - *Pathway Requirement*: $Raw Data \to Canonical SPV (F01–F22) \to Preprocessing/Scaling \to Cost-Sensitive XGBoost \to Platt Scaling (CalibratedClassifierCV) \to Brier Score & ECE Evaluation$.
  - *Current Status*: The path breaks at step 2 (SPV divergence) and step 4 (models fail to load, falling back to 10-row dummy models). No Brier Score, Expected Calibration Error (ECE), or Reliability Curve calculation exists in the codebase.
* **RQ2 (Prescriptive Counterfactual Recourse)**:
  - *Pathway Requirement*: $Calibrated Model \to TreeExplainer(SHAP) \to DiCE Optimization(Continuous/Categorical Feasibility Constraints) \to Sparsity/Proximity Losses \to User Agency Metrics$.
  - *Current Status*: SHAP values are computed in `src/modules/explainability.py` and `PRIE_v1/backend/modules/m07_xai/`. However, DiCE is completely replaced by static `if-else` rules. No optimization loss or user agency data can be exported.
* **RQ3 (Multimodal Behavioral Interview Assessment)**:
  - *Pathway Requirement*: $Audio-Video Input \to [Librosa Prosody \parallel MediaPipe Action Units \parallel Whisper Semantics] \to Late Multimodal Fusion \to Behavioral Trait F1 / MAE$.
  - *Current Status*: Broken. Only legacy audio extraction exists. No video processing, no fusion layer, no API endpoints.
* **RQ4 (Spatial-Semantic Resume Intelligence)**:
  - *Pathway Requirement*: $PDF Resume \to PyMuPDF Spatial Extraction \to LayoutLMv3 Token Classification \to Multi-Class NER Extraction (Skills, Experience, Education) \to ATS Match Scoring$.
  - *Current Status*: Broken. Both codebases use `re.search()` keyword matching on unstructured text dumps.
* **RQ5 (Prerequisite-Constrained Remediation)**:
  - *Pathway Requirement*: $Identified Skill Gaps \to Prerequisite DAG Knowledge Graph \to Kahn's Topological Sequencing \to Weekly Milestone Schedule \to Mastery Velocity Tracking$.
  - *Current Status*: The topological sort algorithm exists in `PRIE_v1/backend/modules/m08_roadmap/dag_scheduler.py`. Missing an authentic curricular skill graph and velocity evaluation harness.
* **RQ6 (Contextual Placement Knowledge & Bloom's AQG)**:
  - *Pathway Requirement*: $Placement Corpus \to Chunking/Embedding \to Vector DB (ChromaDB) \to Hybrid Dense/Sparse Retrieval \to RAG Response \to RAGAS Evaluation (Faithfulness \ge 0.90)$.
  - *Current Status*: Broken. Stubs return canned strings.

---

## 9. Hypothesis Traceability (H1–H6)

```
========================================================================================================================
HYPOTHESIS TRACEABILITY & EXPERIMENTAL READINESS MATRIX
========================================================================================================================
Hypoth. Formal Statement & Benchmark Target                 Required Modules  Required Baseline        Current Status
------------------------------------------------------------------------------------------------------------------------
H1      Calibrated XGBoost achieves Brier <= 0.08,           M01, M06          Uncalibrated XGB,        PARTIALLY IMPL.
        AUC-ROC >= 0.88, outperforming baselines.                             Logistic Reg, RF         (No Calib Script)
H2      Prescriptive DiCE recourse yields >= 20% higher     M06, M07          SHAP-only explanations,  MISSING
        actionability and user agency over SHAP alone.                        Feature importance       (DiCE is Stub)
H3      Late multimodal fusion achieves F1 >= 0.82 in       M05               Unimodal audio,          MISSING
        behavioral trait assessment, beating unimodal >=12%.                  Unimodal text            (No Vision/Fusion)
H4      LayoutLMv3 achieves F1 >= 0.89 on resume NER,       M02               spaCy 1D NER,            MISSING
        outperforming 1D regex/token models by >= 14%.                        Regex matching           (Regex Only)
H5      Kahn's DAG topological sequencing reduces prereq     M04, M08          Greedy unconstrained     PARTIALLY IMPL.
        violations to 0% and boosts mastery velocity >=25%.                   recommendation           (Algorithm Ready)
H6      Domain-specific RAG achieves factual faithfulness   M09, M10          Zero-shot LLM,           MISSING
        >= 92% with hallucination rate <= 5%.                                 Ungrounded Prompting     (Stubs Only)
========================================================================================================================
```

---

## 10. EXP-1–EXP-6 Experiment Readiness

To support peer-reviewed academic publication, the codebase must provide automated experimental harnesses capable of executing the empirical protocols specified in Phase 06.

```
========================================================================================================================
EXPERIMENT EXECUTION READINESS MATRIX (EXP-1 THROUGH EXP-6)
========================================================================================================================
Dimension                       EXP-1        EXP-2        EXP-3        EXP-4        EXP-5        EXP-6
------------------------------------------------------------------------------------------------------------------------
Target RQ / Hypothesis          RQ1 / H1     RQ2 / H2     RQ3 / H3     RQ4 / H4     RQ5 / H5     RQ6 / H6
Dataset Pipeline Available?     PARTIAL (Syn) NO (No Study) NO (No AV)   NO (No PDFs) PARTIAL      NO (No Corpus)
Feature Extractor Available?    PARTIAL (v1) PARTIAL (SHAP) NO (Audio)   NO (Regex)   YES (DAG)    NO (No Embed)
Trained Model Available?        NO (Dummy)   NO (Dummy)   NO           NO           YES (Logic)  NO
Baseline Code Available?        PARTIAL (NB) NO           NO           YES (Regex)  YES (Greedy) NO
Validation Protocol (CV)?       PARTIAL (NB) NO           NO           NO           NO           NO
Metrics Calculation Engine?     PARTIAL (NB) NO           NO           NO           NO           NO
Statistical Significance Test?  NO           NO           NO           NO           NO           NO
Automated Experiment Runner?    NO           NO           NO           NO           NO           NO
Result Export (JSON/LaTeX)?     NO           NO           NO           NO           NO           NO
------------------------------------------------------------------------------------------------------------------------
OVERALL READINESS VERDICT:      NOT READY    NOT READY    NOT READY    NOT READY    NOT READY    NOT READY
========================================================================================================================
```

### 10.1 Gap Ledger: Missing Experimental Infrastructure
1. **No Centralized Experiment Runner**: There is no `scripts/run_experiments.py` or equivalent CLI tool to execute reproducible benchmark trials across seeds 42, 123, 456, 789, 1011.
2. **Missing Statistical Testing Suite**: Phase 06 mandates Wilcoxon signed-rank tests for paired algorithmic comparisons and 5x2 cross-validated paired $t$-tests. Zero statistical testing routines exist in the codebase.
3. **No Automated Metric Exporters**: Neither codebase outputs structured JSON/CSV metrics or LaTeX table strings for direct paper compilation.

---

## 11. 22-Dimensional Student Profile Vector (SPV) Audit

The Student Profile Vector (SPV) is the central data contract of PRIE. The research defines a mathematically rigorous 22-dimensional tensor ($SPV \in \mathbb{R}^{22}$).

### 11.1 Authoritative Specification vs. Code Implementations

```
========================================================================================================================
22-DIMENSIONAL SPV SCHEMA AUDIT TABLE
========================================================================================================================
ID   Canonical Name          Type    Range     Legacy Implementation      PRIE_v1 Implementation    Status / Alignment
------------------------------------------------------------------------------------------------------------------------
F01  cgpa                    Float   [0.0, 10] Found: cgpa                Found: cgpa               MATCH
F02  dsa_score               Float   [0.0, 100]Found: dsa_score           Found: dsa_score          MATCH
F03  dbms_score              Float   [0.0, 100]Found: dbms_score          Found: dbms_score         MATCH
F04  os_score                Float   [0.0, 100]MISSING (Omitted!)         Found: os_score           CRITICAL MISMATCH IN LEGACY
F05  cn_score                Float   [0.0, 100]Found: cn_score            Found: cn_score           MATCH
F06  programming_score       Float   [0.0, 100]Found: programming_score   Found: programming_score  MATCH
F07  aptitude_score          Float   [0.0, 100]Found: aptitude_score      Found: aptitude_score     MATCH
F08  soft_skills_score       Float   [0.0, 100]MISSING (Omitted!)         Found: soft_skills_score  CRITICAL MISMATCH IN LEGACY
F09  project_count           Int     [0, 15]   Found: project_count       Found: project_count      MATCH
F10  project_quality_score   Float   [0.0, 100]MISSING (Omitted!)         Found: project_quality_s. CRITICAL MISMATCH IN LEGACY
F11  has_internship          Binary  {0, 1}    MISSING (Used months!)     Found: has_internship     SCHEMA MISMATCH IN LEGACY
F12  certifications_count    Int     [0, 20]   Found: certifications_cou. Found: certifications_co. MATCH
F13  resume_ats_score        Float   [0.0, 100]Found: resume_ats_score    Found: resume_ats_score   MATCH
F14  cosine_similarity       Float   [0.0, 1.0]Found: cosine_similarity   Found: cosine_similarity  MATCH
F15  gap_score               Float   [0.0, 1.0]Found: gap_score           Found: gap_score          MATCH
F16  consistency_score       Float   [0.0, 1.0]Found: consistency_score   Found: consistency_score  MATCH
F17  branch_encoded          Int     {0..5}    Found: branch_encoded      Found: branch_encoded     MATCH
F18  target_role_encoded     Int     {0..7}    Found: target_role_encoded Found: target_role_enc.   MATCH
F19  assessment_attempts     Int     [0, 50]   Found: assessment_attempts Found: assessment_attem.  MATCH
F20  behavior_score          Float   [0.0, 1.0]Found: behavior_score      Found: behavior_score     MATCH
F21  engagement_score        Float   [0.0, 1.0]Found: engagement_score    Found: engagement_score   MATCH
F22  roadmap_completion_rate Float   [0.0, 1.0]Found: roadmap_completion_ Found: roadmap_completion MATCH
------------------------------------------------------------------------------------------------------------------------
[EXTRA IN LEGACY]: backlogs (Int), internship_months (Int), skill_count (Int) -> UNJUSTIFIED DIVERGENCE!
========================================================================================================================
```

### 11.2 Mathematical Derivations and Normalization Audit
1. **Normalization Inconsistency**:
   - Phase 06 Methodology specifies **Min-Max scaling to $[0.0, 1.0]$** for all continuous score features and standard $z$-score standardization for Tree Ensembles where applicable.
   - In legacy `src/modules/student_profiling.py`, scores are left in raw $[0, 100]$ or $[0, 10]$ ranges, while telemetry scores are $[0.0, 1.0]$. The saved `models/scaler.pkl` was fitted on these inconsistent scales.
2. **Missing Feature Derivations**:
   - `F16 (consistency_score)` is defined in Phase 04 as the rolling inverse standard deviation of weekly assessment scores over a 6-week window:
     $$\text{consistency\_score} = 1.0 - \min\left(1.0, \frac{\sigma_{\text{weekly}}}{\mu_{\text{weekly}}}\right)$$
   - In both codebases, this value is passed as a static raw input or defaulted to `0.60`. Zero windowed variance calculations exist.

---

## 12. Model Artifact Audit

A comprehensive forensic audit of all serialized artifacts in `07_Implementation/models/` and `07_Implementation/PRIE_v1/backend/models/` was executed.

```
========================================================================================================================
MODEL ARTIFACT FORENSIC AUDIT TABLE
========================================================================================================================
Artifact Path                        Size     Format   Inspected Provenance              Research Validity Status
------------------------------------------------------------------------------------------------------------------------
models/xgb_model.pkl                 142 KB   Pickle   Colab Notebook Cell 29            INVALID (Synthetic Data & Schema)
models/scaler.pkl                    1.8 KB   Pickle   Colab Notebook Cell 29            INVALID (Fitted on Legacy Schema)
models/feature_names.json            624 B    JSON     Colab Notebook Cell 29            INVALID (Lists Legacy Features)
models/jd_embeddings.npy             15.3 KB  NumPy    Generated from mock JDs           USABLE FOR MOCK DEMOS ONLY
models/jd_metadata.json              3.2 KB   JSON     Generated from mock JDs           USABLE FOR MOCK DEMOS ONLY
PRIE_v1/backend/models/*             0 B      EMPTY    NO ARTIFACTS EXIST                MISSING (Forces Dummy Model)
========================================================================================================================
```

### 12.1 Detailed Provenance Investigation
1. **Forensic Verification of `models/xgb_model.pkl`**:
   - The model was unpickled and inspected in scratch memory.
   - It is an `xgboost.XGBClassifier` with `n_estimators=100`, `max_depth=4`, `learning_rate=0.05`.
   - The feature names embedded in the model header correspond **exactly** to the 22 features in `models/feature_names.json` (including `backlogs`, `internship_months`, and `skill_count`).
   - Cross-referencing with `notebooks/ScholarCamp_PRIE_Google_Colab.ipynb` reveals that this artifact was generated in **Cell 29** using `pickle.dump(best_xgb, f)` after fitting on synthetic rows generated by `np.random.normal()` in Cell 4.
   - **Verdict**: Provenance is fully verified, but the model is **scientifically invalid for research** because it was trained on synthetic random numbers with an incorrect feature schema.
2. **Investigation of `PRIE_v1/backend/models/`**:
   - The directory contains **zero files**.
   - As a direct consequence, every API call to `/api/v1/predictions/predict` invokes the fallback routine in `backend/ml/placement_predictor.py`, training an ephemeral 60-row synthetic model on every server process launch.

---

## 13. Notebook Audit

### 13.1 Audit of `ScholarCamp_PRIE_Google_Colab.ipynb`
The repository contains `ScholarCamp_PRIE_Google_Colab.ipynb` comprising 31 execution cells.

```
========================================================================================================================
COLAB NOTEBOOK CELL-BY-CELL MAPPING & RESEARCH AUDIT
========================================================================================================================
Cell Range   Executed Logic                     Methodology Mapping    Research Quality / Flaws
------------------------------------------------------------------------------------------------------------------------
Cells 01–03  Environment setup & imports        Setup                  Standard imports; unpinned package versions
Cells 04–06  Synthetic dataset generation       Methodology (DS-SYNTH) Generates 1,200 synthetic rows; uses LEGACY schema
Cells 07–10  Exploratory Data Analysis (EDA)    Data Understanding     Visualizes distributions; confirms target balance
Cells 11–14  Train/Val/Test Split (70/15/15)    Research Protocol      Splits data; applies SMOTE to train set correctly
Cells 15–18  StandardScaler fitting             Preprocessing          Fits scaler on X_train only; good leakage isolation
Cells 19–23  Baseline Model Benchmarking        Methodology (Baselines)Trains LogReg, Random Forest, LightGBM, XGBoost
Cells 24–26  GridSearchCV Hyperparameter Tuning Methodology (Tuning)   Tunes max_depth, n_estimators on XGBoost
Cells 27–28  CalibratedClassifierCV & SHAP      Methodology (Calib/XAI)Fits Platt scaling; initializes TreeExplainer
Cell 29      Artifact Serialization             Deployment             Dumps xgb_model.pkl, scaler.pkl, feature_names
Cells 30–31  Mock Inference Test Pipeline       Inference              Validates prediction on single sample
========================================================================================================================
```

### 13.2 Key Findings & Logic Migration Opportunities
1. **Strengths in Notebook**:
   - Cells 11–15 demonstrate proper experimental hygiene: splitting into train, validation, and test sets **before** applying `StandardScaler` and `SMOTE`. This prevents scaler and synthetic target leakage.
   - Cell 27 correctly employs `CalibratedClassifierCV(estimator=best_xgb, method='sigmoid', cv='prefit')`.
2. **Critical Flaws**:
   - The data generator in Cell 4 defines features according to the legacy prototype schema rather than the canonical F01–F22 specification.
   - The dataset is 100% synthetic, generated by uncorrelated normal distributions. No empirical benchmark datasets (`DS-BENCH-01`, `DS-BENCH-02`) are ingested.
3. **Migration Plan**:
   - The model training, calibration, and SHAP initialization routines in Cells 19–28 should be extracted and formalized into a dedicated, parameterized training script (`scripts/train_model.py`).
   - The notebook should be retained purely as a reproducible experimental record.

---

## 14. Data Pipeline Audit

```
[RAW DATA INGESTION]
  │   - Academic Records (CGPA, Branch, Backlogs)
  │   - Assessment Engine Logs (DSA, DBMS, OS, CN, Aptitude Scores)
  │   - Resume PDF Documents
  │   - Mock Interview Audio/Video Streams
  ▼
[VALIDATION & INTEGRITY GATEWAY]
  │   - Legacy: Zero validation; accepts arbitrary dicts; silently fills missing keys.
  │   - PRIE_v1: Pydantic schemas (StudentProfileCreate, SPVVectorRequest) validate types and ranges.
  ▼
[PREPROCESSING & FEATURE DERIVATION]
  │   - Normalization: Inconsistent scales in legacy; Min-Max scaling in PRIE_v1.
  │   - Text Parsing: Unstructured regex keyword matching.
  │   - Telemetry Derivation: Hardcoded constants (gap_score=0.35, behavior_score=0.65).
  ▼
[CANONICAL 22D SPV SYNTHESIS]
  │   - Legacy: Assembles 22 features, but diverges by 3 features from canonical specification.
  │   - PRIE_v1: Strictly assembles canonical F01–F22 vector tensor.
  ▼
[INFERENCE / EXPERIMENTAL EVALUATION]
  │   - Model Loading: Fails in both branches -> falls back to random dummy models.
  │   - Explainability: SHAP values computed; DiCE counterfactuals bypassed with rule-based text.
  ▼
[DATABASE PERSISTENCE]
  │   - Legacy: Direct un-indexed SQLite writes via db_manager.py.
  │   - PRIE_v1: Relational SQLite storage across 14 tables in prie_v1.db.
```

---

## 15. Data Leakage Audit

A rigorous audit across all 11 potential data leakage vectors was conducted:

```
========================================================================================================================
COMPREHENSIVE DATA LEAKAGE AUDIT TABLE
========================================================================================================================
Leakage Vector        Risk Level  Observed Evidence & Location                                  Recommended Remediation
------------------------------------------------------------------------------------------------------------------------
Target Leakage        LOW         Target 'placed' excluded from feature matrices.               Maintain exclusion check
Train/Test Leakage    MEDIUM      Colab splits properly; however, synthetic generator uses       Enforce fixed seed across
                                  global seed before splitting.                                 train/test partitions
Scaler Leakage        MEDIUM      Colab fits scaler on train only; however, runtime dummy       Strictly isolate fit() to
                                  fallback in placement_predictor.py fits on all dummy data.    train partition only
SMOTE Leakage         LOW         Colab Cell 14 correctly fits SMOTE on X_train only.           Maintain pipeline isolation
Feature Leakage       HIGH        Telemetry features (gap_score, consistency_score) are        Derive telemetry strictly
                                  hardcoded constants across all students.                      from historic student events
Duplicate Student     MEDIUM      Cross-validation in Colab uses standard KFold; does not       Use GroupKFold grouped on
Leakage                           enforce GroupKFold on student IDs.                            unique student_id
Resume Leakage        HIGH        Embedding vectorizer (MiniLM) computes embeddings on raw JDs  Precompute static corpus
                                  without train/test corpus separation.                         embeddings independently
JD Leakage            MEDIUM      Mock JDs used in training skill gaps overlap test JDs.        Partition JD test split
Temporal Leakage      HIGH        No temporal masking (e.g. past semester predicting future);   Implement temporal split
                                  all features assumed concurrently available.                  by academic semester
Embedding Leakage     LOW         SentenceTransformer used for cosine similarity inference.     Acceptable (pre-trained)
Label Leakage         MEDIUM      Assessment scores generated from placement-correlated noise   Replace with authentic
                                  in synthetic generator, creating artificial collinearity.     IRT assessment traces
========================================================================================================================
```

---

## 16. Database Audit

### 16.1 Comparative Schema Evaluation

```
========================================================================================================================
DATABASE SCHEMA ARCHITECTURAL COMPARISON
========================================================================================================================
Dimension               Legacy Prototype (src/database/schema.sql)    PRIE_v1 Prototype (backend/database/schema.sql)
------------------------------------------------------------------------------------------------------------------------
Database Engine         SQLite (file-based)                           SQLite (prie_v1.db)
Total Tables            6 tables                                      14 tables
Table Coverage          students, assessments, resumes,               students, academic_profiles, skill_assessments,
                        interviews, placements, roadmaps              resumes, interviews, placement_predictions,
                                                                      counterfactual_plans, roadmaps, milestones,
                                                                      mock_questions, student_responses, audit_logs
Foreign Key Cascades    NOT ENFORCED (Missing ON DELETE CASCADE)      ENFORCED (Proper cascading deletes)
Indexes                 Primitive index on student_id only            Composite indexes on (student_id, created_at)
Connection Management   Ad-hoc sqlite3.connect() in functions         Thread-safe SQLite connection pool abstraction
ORM / Migrations        None (raw SQL string execution)               None (raw SQL; Alembic migrations missing)
========================================================================================================================
```

### 16.2 Critical Findings
1. `PRIE_v1` represents a substantial architectural upgrade over the legacy schema, supporting rich relational integrity across placement predictions, counterfactual recourse plans, and roadmap milestones.
2. **Missing Schema Elements**:
   - Neither database schema includes tables for storing **audio/video interview metrics** (pitch, jitter, action units).
   - Neither schema includes tables for tracking **experimental runs, hyperparameter logs, or model benchmark artifacts**.
   - Lack of an automated database migration tool (e.g., Alembic) creates high risk of data corruption during schema iteration.

---

## 17. API Audit

### 17.1 REST API Endpoint Conformance (`PRIE_v1/backend/`)

```
========================================================================================================================
FASTAPI ENDPOINT AUDIT TABLE (PRIE_v1)
========================================================================================================================
Method Path                                Input Schema           Output Schema          Auth? Error Handling  Status
------------------------------------------------------------------------------------------------------------------------
POST   /api/v1/auth/login                  LoginRequest           TokenResponse          NO    Basic 401       FUNCTIONAL
POST   /api/v1/auth/register               RegisterRequest        UserResponse           NO    Basic 400       FUNCTIONAL
GET    /api/v1/students/{id}/profile       None                   StudentProfileResponse YES   Basic 404       FUNCTIONAL
POST   /api/v1/students/{id}/profile       StudentProfileCreate   StudentProfileResponse YES   Basic 400       FUNCTIONAL
POST   /api/v1/predictions/predict         SPVVectorRequest       PredictionResponse     YES   Fallback dummy  DEGRADED
POST   /api/v1/predictions/counterfactual  CounterfactualRequest  CounterfactualResponse YES   Mock rule-based DEGRADED
POST   /api/v1/roadmaps/generate           RoadmapRequest         RoadmapResponse        YES   Basic 500       FUNCTIONAL
POST   /api/v1/assessments/quiz/submit     QuizSubmitRequest      QuizResultResponse     YES   Basic 400       FUNCTIONAL
GET    /api/v1/assessments/quiz/next       None                   QuizQuestionResponse   YES   Basic 404       FUNCTIONAL
POST   /api/v1/resumes/upload              [MISSING ENDPOINT]     [MISSING ENDPOINT]     --    --              NOT IMPLEMENTED
POST   /api/v1/interviews/session          [MISSING ENDPOINT]     [MISSING ENDPOINT]     --    --              NOT IMPLEMENTED
POST   /api/v1/rag/query                   [MISSING ENDPOINT]     [MISSING ENDPOINT]     --    --              NOT IMPLEMENTED
POST   /api/v1/aqg/generate                [MISSING ENDPOINT]     [MISSING ENDPOINT]     --    --              NOT IMPLEMENTED
========================================================================================================================
```

### 17.2 Critical API Findings
1. **Missing Core Architectural Endpoints**: There are no API endpoints for uploading resumes, initiating mock interview sessions, querying the RAG knowledge assistant, or triggering digital twin simulations.
2. **Degraded Prediction Endpoints**: `/api/v1/predictions/predict` succeeds with HTTP 200, but the data returned is generated by an uncalibrated 60-sample dummy model due to the empty `backend/models/` directory.

---

## 18. Frontend / UI Audit

```
========================================================================================================================
FRONTEND IMPLEMENTATION AUDIT TABLE
========================================================================================================================
Page / Interface          Legacy Streamlit Implementation        PRIE_v1 Web Implementation             UI Readiness
------------------------------------------------------------------------------------------------------------------------
Landing / Login           pages/01_login.py (MISSING / CRASH)    frontend/index.html                    FUNCTIONAL (Clean)
Student Dashboard         pages/02_dashboard.py (MISSING)        frontend/dashboard.html                PARTIALLY IMPL.
SPV Profile Explorer      pages/03_profile.py (MISSING)          Embedded in dashboard.html             PARTIALLY IMPL.
Placement Probability     pages/04_prediction.py (MISSING)       Embedded in dashboard.html             PARTIALLY IMPL.
Prescriptive Recourse     pages/05_xai.py (MISSING)              Stubbed card in dashboard.html         NOT IMPLEMENTED
Skill Gap Radar           pages/06_skill_gap.py (MISSING)        Chart.js canvas in dashboard.html      FUNCTIONAL
Resume ATS Intelligence   pages/07_resume.py (MISSING)           [MISSING ENTIRELY]                     NOT IMPLEMENTED
Mock Interview Studio     pages/08_interview.py (MISSING)        [MISSING ENTIRELY]                     NOT IMPLEMENTED
Adaptive Assessment Quiz  pages/09_assessment.py (MISSING)       frontend/assessment.html               FUNCTIONAL
Dynamic Roadmap Gantt     pages/10_roadmap.py (MISSING)          frontend/roadmap.html                  FUNCTIONAL
Coordinator Analytics     pages/11_admin.py (MISSING)            frontend/admin.html                    PARTIALLY IMPL.
========================================================================================================================
```

### 18.1 Clean UI Compliance Evaluation
1. **Technology Stack**: `PRIE_v1/frontend/` uses standard HTML5, vanilla CSS3, and ES6 JavaScript. It avoids heavy framework overhead while providing responsive layouts, satisfying the web design mandate.
2. **Critical Functional Gaps**:
   - **No Resume Upload / ATS Interface**: There is no UI page where a student can drop a PDF resume to view entity extraction or ATS match scoring.
   - **No Mock Interview Studio**: There is no UI page with camera/microphone capture, real-time audio waveforms, or interview question prompts.
   - **No Interactive Counterfactual Simulator**: Students cannot dynamically drag feature sliders to view real-time placement probability changes (What-If recourse).

---

## 19. Security Audit

```
========================================================================================================================
SECURITY AUDIT & VULNERABILITY LEDGER
========================================================================================================================
Vulnerability Class  Location                                Evidence / Vulnerability Detail            Severity
------------------------------------------------------------------------------------------------------------------------
Hardcoded Secrets    src/config.py & backend/config.py        SECRET DETECTED — LOCATION REDACTED        CRITICAL
                                                              Default JWT secret hardcoded in codebase.
Insecure File Path   src/modules/resume_intelligence.py       os.path.join(UPLOAD_DIR, file.name) lacks  HIGH
                                                              filename sanitization (Path Traversal).
CORS Misconfiguration PRIE_v1/backend/main.py                 allow_origins=["*"] with                   MEDIUM
                                                              allow_credentials=True (Insecure wildcard)
Missing Rate Limit   FastAPI auth routers                     No rate-limiting middleware on /login or   MEDIUM
                                                              /register (Vulnerable to brute force).
Unauthenticated APIs Legacy Streamlit modules                 No authentication required for direct      HIGH
                                                              module execution or database queries.
Plaintext Passwords  Legacy SQLite database                   Passwords stored in plaintext without      CRITICAL
                                                              bcrypt hashing in legacy prototype.
========================================================================================================================
```

---

## 20. Code Quality & Technical Debt Audit

1. **Coupling & Cohesion**:
   - Legacy prototype suffers from extreme coupling: `src/app.py` directly instantiates database managers, feature scalers, and module classes in the UI thread.
   - `PRIE_v1` achieves clean separation of concerns, decoupling REST routing (`backend/api/`), business logic (`backend/modules/`), and data access (`backend/database/`).
2. **Duplication**:
   - Substantial logic duplication exists between `notebooks/ScholarCamp_PRIE_Google_Colab.ipynb`, `07_Implementation/src/modules/placement_predictor.py`, and `PRIE_v1/backend/ml/placement_predictor.py`.
3. **Type Safety & Documentation**:
   - Legacy Python modules contain almost zero type hints and minimal docstrings.
   - `PRIE_v1` enforces Pydantic models for API request/response validation, representing significantly higher code quality.

---

## 21. Dependency Audit

```
========================================================================================================================
DEPENDENCY AUDIT TABLE
========================================================================================================================
Package Name            Legacy Version     PRIE_v1 Version    Status / Conflicts
------------------------------------------------------------------------------------------------------------------------
fastapi                 MISSING            0.110.0            Required for REST backend
uvicorn                 MISSING            0.28.0             Required for ASGI serving
pydantic                MISSING            2.6.4              Required for data contracts
streamlit               1.32.0             MISSING            Legacy only; deprecate
xgboost                 2.0.3              2.0.3              Core predictive model
scikit-learn            1.4.1              1.4.1              Preprocessing and calibration
shap                    0.44.1             0.44.1             Feature explainability
dice-ml                 MISSING            MISSING            CRITICAL: Missing required dependency for H2!
torch / torchvision     MISSING            MISSING            CRITICAL: Required for LayoutLMv3 and Fusion!
transformers            MISSING            MISSING            CRITICAL: Required for LayoutLMv3 and Whisper!
librosa                 0.10.1             MISSING            Required for acoustic prosody extraction
mediapipe               MISSING            MISSING            CRITICAL: Required for facial action units!
chromadb                MISSING            MISSING            CRITICAL: Required for RAG vector storage!
PyMuPDF (fitz)          1.23.26            MISSING            Required for resume spatial extraction
========================================================================================================================
```

---

## 22. Reproducibility Audit

A researcher attempting to reproduce PRIE from the current codebase encounters immediate failures:
1. **Unpinned Random Seeds**: While the Colab notebook sets `random_state=42` in certain cells, the runtime dummy models generated in `placement_predictor.py` use unseeded `np.random.normal()` and `np.random.rand()`.
2. **Missing Dataset Ingestion Scripts**: No automated scripts exist to download or ingest the benchmark datasets specified in Phase 06 (`DS-BENCH-01 Babureddy`, `DS-BENCH-02 Azeez`).
3. **Missing Environment Specification**: Neither `requirements.txt` locks dependency hashes, creating high vulnerability to breaking changes in `transformers`, `torch`, or `pydantic`.

---

## 23. Error Handling Audit

```
FILE:
07_Implementation/src/modules/placement_predictor.py

FINDING:
Silent exception swallowing and invisible degradation to dummy model.

EVIDENCE:
Lines 42–46:
    except Exception as e:
        logger.warning(f"Error: {e}")
        return self._dummy_prediction()

RESEARCH IMPACT:
Critical experimental failures during batch evaluation are silently masked as valid probability
predictions (e.g. returning 0.72 for all failed rows), corrupting empirical benchmark metrics.

RECOMMENDATION:
Remove silent fallbacks in production and experimental modes. Raise explicit typed exceptions
(ModelArtifactNotFoundError, PredictionInferenceError).

PRIORITY:
HIGH
```

---

## 24. Performance & Scalability Bottlenecks

1. **Synchronous On-the-Fly Dummy Model Training**:
   - In `PRIE_v1/backend/ml/placement_predictor.py`, missing models trigger synchronous fitting of an XGBoost classifier on the ASGI event loop, blocking all concurrent API requests.
2. **Sequential PDF Parsing**:
   - Resume processing in `src/modules/resume_intelligence.py` iterates sequentially through pages using single-threaded PyMuPDF calls without asynchronous worker delegation.
3. **Repeated Model Unpickling**:
   - In legacy modules, `pickle.load()` is called inside request handling functions rather than maintaining a persistent singleton model in memory.

---

## 25. Research-Paper Readiness Audit

```
========================================================================================================================
RESEARCH PAPER SECTION READINESS EVALUATION
========================================================================================================================
Intended Paper Section          Target Content                                Current Status & Readiness
------------------------------------------------------------------------------------------------------------------------
1. Introduction & Background    Higher ed placement crisis, gaps CG1–CG8       READY (Phases 01–03 are comprehensive)
2. Related Work & Literature    44 papers, taxonomy, trade-off matrices       READY (Phases 01–02 are exhaustive)
3. PRIE System Architecture     M01–M12 component decomposition, data flows   READY (Phase 05 is authoritative)
4. Theoretical Methodology      22D SPV math, calibration, DiCE, Kahn's DAG  READY (Phase 06 is fully formulated)
5. Implementation Details       FastAPI, LayoutLMv3, Librosa/Whisper, SQLite  NOT READY (Codebase fragmented/incomplete)
6. Experimental Setup           Datasets (DS-BENCH), baselines, protocols     PARTIAL (Protocols defined; runners missing)
7. Empirical Results & Findings Benchmarks vs Babureddy/Azeez, ablation runs  NOT READY (Zero empirical runs executed)
8. Discussion & Threats         Usability, ethics, bias, limitations          READY (Phase 06 covers threats thoroughly)
========================================================================================================================
```

---

## 26. Missing Functionality Catalog

1. **LayoutLMv3 Spatial Token Classifier**: Fine-tuned 2D spatial NER model for resume bounding box parsing.
2. **Multimodal Late Fusion Engine**: Tensor fusion network combining acoustic, visual, and semantic vectors.
3. **DiCE Mathematical Counterfactual Explainer**: Constrained optimization solving for diverse recourse vectors.
4. **Vector Retrieval & RAG Pipeline**: ChromaDB index storing institution-specific placement guidelines and interview transcripts.
5. **Bloom's Automated Question Generator**: Dynamic question generator with difficulty calibration.
6. **Longitudinal Digital Twin Simulator**: Forward Euler state transition simulation of SPV improvements over time.
7. **Automated Experiment Execution Harness**: Standalone CLI runner to execute EXP-1 through EXP-6 across multiple seeds and export LaTeX tables.

---

## 27. Feature Gap Analysis

```
========================================================================================================================
FEATURE GAP HIERARCHICAL ANALYSIS
========================================================================================================================
Severity   Component / Feature Gap                                    Upstream Research Justification
------------------------------------------------------------------------------------------------------------------------
CRITICAL   Retrain XGBoost on Canonical 22D SPV with Platt Scaling    M01, M06, RQ1, H1, EXP-1 (Brier <= 0.08)
CRITICAL   Implement M05 Multimodal Interview Coach & Fusion Layer     M05, RQ3, H3, EXP-3 (F1 >= 0.82)
CRITICAL   Integrate DiCE Mathematical Counterfactual Optimization    M07, RQ2, H2, EXP-2 (User Agency)
HIGH       Implement LayoutLMv3 Spatial Document Parsing for Resumes  M02, RQ4, H4, EXP-4 (NER F1 >= 0.89)
HIGH       Build Automated Experiment Runner & Metric Exporter        Phase 06 Experimental Framework (EXP-1–EXP-6)
HIGH       Develop Clean UI Interfaces for Resume ATS & Interview     Phase 05 UI Architecture & ScholarCamp Mandate
MEDIUM     Connect ChromaDB Vector Store to M09 RAG Assistant         M09, RQ6, H6, EXP-6 (Faithfulness >= 92%)
MEDIUM     Connect Curricular Skill Graph to M08 Kahn's DAG Scheduler M08, RQ5, H5, EXP-5 (Mastery Velocity)
LOW        Implement M12 Digital Twin What-If Sensitivity Simulator   M12, Phase 05 Architecture
========================================================================================================================
```

---

## 28. Research-Critical vs. Product-Only Features

```
========================================================================================================================
FEATURE RESEARCH-JUSTIFICATION CLASSIFICATION
========================================================================================================================
Proposed Feature / Component              Classification      Justification & Academic Grounding
------------------------------------------------------------------------------------------------------------------------
Canonical 22D SPV Pipeline                RESEARCH-CRITICAL   Foundational representation for all predictions (RQ1)
Cost-Sensitive Platt-Scaled XGBoost       RESEARCH-CRITICAL   Core empirical contribution of calibrated prediction (H1)
DiCE Feasibility-Constrained Recourse     RESEARCH-CRITICAL   Core empirical contribution of prescriptive XAI (H2)
Late Multimodal Fusion Network            RESEARCH-CRITICAL   Core empirical contribution of behavioral coaching (H3)
LayoutLMv3 Spatial Resume NER             RESEARCH-CRITICAL   Core empirical contribution of document intelligence (H4)
Kahn's DAG Curriculum Scheduler           RESEARCH-CRITICAL   Core empirical contribution of remediation velocity (H5)
RAG Placement Retrieval with RAGAS        RESEARCH-CRITICAL   Core empirical contribution of contextual guidance (H6)
Automated Experiment Runner (EXP-1–6)     RESEARCH-CRITICAL   Mandatory infrastructure for paper empirical validation
Vanilla HTML/JS Student Dashboard         RESEARCH-SUPPORTING Required for human evaluation and study execution
Vanilla HTML/JS Mock Interview Studio     RESEARCH-SUPPORTING Required for capturing multimodal user evaluation data
Social Media OAuth Login                  PRODUCT-ONLY        Zero research relevance; standard auth suffices
Payment Gateway / Subscription Billing    PRODUCT-ONLY        Zero research relevance; university research project
Gamified Badges & Public Leaderboards     PRODUCT-ONLY        Zero research relevance; introduces confounders
========================================================================================================================
```

---

## 29. Current → Target Architecture

```
CURRENT ARCHITECTURE (Fragmented & Degraded)
├── Legacy Streamlit (src/) [BROKEN UI, PATH BUGS, WRONG SPV SCHEMA]
├── Colab Notebook [TRAINED ON SYNTHETIC NOISE, EXPORTED DIVERGENT ARTIFACTS]
└── PRIE_v1 [CLEAN FASTAPI + WEB, BUT MISSING M05, NO TRAINED MODELS, STUBBED XAI/RAG]
                                      │
                                      ▼
TARGET UNIFIED ARCHITECTURE (Research-Grade ScholarCamp PRIE)
├── 07_Implementation/
│   ├── backend/ (Promote and expand PRIE_v1)
│   │   ├── api/v1/ (Full REST endpoints: Auth, SPV, Predict, Recourse, ATS, Interview, Roadmap)
│   │   ├── ml/
│   │   │   ├── models/ (Validated xgb_model.pkl, scaler.pkl, layoutlmv3/, fusion_net.pt)
│   │   │   ├── training/ (train_spv_model.py, calibrate_model.py, evaluate_models.py)
│   │   │   └── inference/ (calibrated_predictor.py, dice_recourse.py, layout_parser.py)
│   │   ├── modules/ (Complete M01 through M12 implementations; restore M05)
│   │   └── database/ (SQLite prie_research.db with complete relational schema)
│   ├── experiments/ (Standalone empirical execution suite)
│   │   ├── datasets/ (DS-BENCH-01, DS-BENCH-02, DS-CORPUS-01 loaders)
│   │   ├── runners/ (run_exp1_calibration.py ... run_exp6_rag.py)
│   │   └── results/ (Raw metrics, JSON logs, generated LaTeX tables)
│   └── frontend/ (Clean Vanilla HTML5 / CSS3 / ES6)
│       ├── pages/ (Dashboard, Profile, Prediction, Recourse, ATS, Interview, Roadmap)
│       ├── css/style.css (Premium responsive design system)
│       └── js/ (api.js, webrtc_capture.js, charts.js, dashboard.js)
```

---

## 30. Component Migration Strategy

```
========================================================================================================================
COMPONENT MIGRATION & ACTION LEDGER
========================================================================================================================
Existing File / Component              Action      Evidence & Technical Rationale
------------------------------------------------------------------------------------------------------------------------
07_Implementation/src/                 DEPRECATE   Broken Streamlit monolith; path bugs; divergent feature schema.
07_Implementation/configs/config.json  DEPRECATE   Hardcodes legacy 22D schema omitting core canonical features.
07_Implementation/models/xgb_model.pkl DEPRECATE   Trained on synthetic noise with legacy schema; provenance invalid.
07_Implementation/notebooks/Colab.ip.. ARCHIVE     Keep as historical reference; extract calibration & SMOTE logic.
PRIE_v1/backend/spv_version.py         KEEP        Accurately specifies canonical F01–F22 SPV structure.
PRIE_v1/backend/main.py                KEEP / EXP. Clean FastAPI application factory; expand with missing routers.
PRIE_v1/backend/database/              KEEP / EXP. Excellent 14-table schema; add interview telemetry & run tables.
PRIE_v1/backend/modules/m08_roadmap/   KEEP        Kahn's DAG topological scheduler is robust and research-valid.
PRIE_v1/backend/modules/m07_xai/       REFACTOR    Keep SHAP tree explainer; replace mock counterfactual with DiCE.
PRIE_v1/backend/modules/m02_ats/       REPLACE     Replace regex keyword matching with LayoutLMv3 spatial NER.
PRIE_v1/backend/modules/m05 (None)     NEW         Implement full multimodal interview module (Audio/Video/Fusion).
PRIE_v1/frontend/                      KEEP / EXP. Clean HTML/JS architecture; build missing ATS & Interview pages.
========================================================================================================================
```

---

## 31. Priority Implementation Roadmap

```
========================================================================================================================
PRIE PHASE 07 IMPLEMENTATION EXECUTION ROADMAP
========================================================================================================================
Phase      Focus Area               Milestone Objectives                                   Research Mapping
------------------------------------------------------------------------------------------------------------------------
PHASE 07A  Foundation & Data        Consolidate on PRIE_v1; establish canonical 22D SPV     M01, DD-001, DD-002
                                    data loaders; ingest DS-BENCH-01 and DS-BENCH-02.
PHASE 07B  Core Prediction & Calib. Train cost-sensitive XGBoost on canonical SPV; fit     M06, RQ1, H1, EXP-1
                                    Platt scaling; enforce Brier score <= 0.08.
PHASE 07C  Prescriptive Recourse    Integrate dice-ml with calibrated model; enforce        M07, RQ2, H2, EXP-2
                                    actionability masks and sparsity constraints.
PHASE 07D  Resume Intelligence      Implement LayoutLMv3 spatial bounding-box token         M02, RQ4, H4, EXP-4
                                    classification for multi-column resumes.
PHASE 07E  Multimodal Interview     Build M05 interview module: WebRTC capture, Librosa     M05, RQ3, H3, EXP-3
                                    prosody, MediaPipe action units, Late Fusion layer.
PHASE 07F  Dynamic Remediation      Connect curricular knowledge graph to Kahn's DAG        M08, RQ5, H5, EXP-5
                                    scheduler; evaluate mastery velocity.
PHASE 07G  Contextual Intelligence  Set up ChromaDB vector store; implement domain RAG      M09, M10, RQ6, H6, EXP-6
                                    and Bloom's question generation.
PHASE 07H  Clean UI Completion      Build ATS resume upload and Mock Interview camera       ScholarCamp Web Mandate
                                    capture interfaces in clean Vanilla HTML5/CSS/JS.
PHASE 07I  Experimentation & Eval   Implement automated experiment runners (EXP-1–EXP-6);   Academic Paper Delivery
                                    execute statistical tests; export LaTeX tables.
========================================================================================================================
```

---

## 32. Critical Blockers

1. **Empty Model Artifact Directory in `PRIE_v1`**: The FastAPI backend cannot serve legitimate predictions because `backend/models/` contains 0 files, forcing dynamic dummy training on random numbers.
2. **SPV Schema Incompatibility in Legacy Models**: The existing pickled model (`models/xgb_model.pkl`) cannot be used with `PRIE_v1` because its input feature dimension expects `backlogs`, `internship_months`, and `skill_count` instead of `os_score`, `soft_skills_score`, and `project_quality_score`.
3. **Missing M05 (Mock Interview) Implementation in `PRIE_v1`**: Completely blocks Experiment EXP-3 and Hypothesis H3.
4. **Missing DiCE Integration in M07**: Completely blocks Experiment EXP-2 and Hypothesis H2.
5. **Absence of Empirical Training Pipeline**: No script exists to train and serialize models from the authoritative benchmark datasets.

---

## 33. Technical & Experimental Risks

1. **Computational Overhead of LayoutLMv3 on CPU**: Fine-tuning or inferencing LayoutLMv3 on local development machines lacking CUDA GPUs may introduce severe latency during resume processing. A lightweight fallback or ONNX runtime optimization must be planned.
2. **WebRTC Browser Permissions for Mock Interview**: Capturing synchronized audio and video in modern browsers requires HTTPS and strict user permission handling. Local test harnesses must account for headless testing environments.
3. **DiCE Convergence Latency**: Generating model-agnostic counterfactual recourse with strict integer and categorical constraints can take several seconds per student on large search spaces, requiring background queue processing.

---

## 34. Questions Requiring Research Decisions

1. **Benchmark Dataset Ingestion Strategy**: Should the initial training pipeline ingest the raw Babureddy (2024) dataset directly, or should it use an augmented version combined with the curated synthetic corpus (`DS-SYNTH-01`) to ensure full representation across all 22 canonical features?
2. **LayoutLMv3 Hosting / Execution**: Should the resume parsing pipeline execute local inference via PyTorch / ONNX, or should an extracted feature vector representation be used for testing environments lacking GPU acceleration?
3. **Multimodal Fusion Topology**: Should the Late Fusion layer for mock interviews use a simple linear soft-voting blend across prosody, vision, and text, or a trained multi-layer perceptron (MLP) cross-attention gate?

---

## 35. Final Readiness Assessment

### Overall Status: **REQUIRES IMPLEMENTATION WORK**

The current implementation state in `07_Implementation/` is a prototype undergoing architectural transition. While `PRIE_v1/` provides a strong structural foundation (FastAPI backend, clean 14-table database schema, canonical F01–F22 SPV definition, and Kahn's DAG roadmap scheduler), it lacks trained model artifacts, misses core architectural modules (M05 Mock Interview), stubs out critical research logic (DiCE counterfactuals, LayoutLMv3, RAG), and provides no automated experiment runners.

Execution of the prioritized roadmap (Phases 07A through 07I) will resolve all identified blockers and establish a fully validated, research-grade, publication-ready implementation of ScholarCamp PRIE.

---

```
==================================================================================================
FINAL AUDIT VERIFICATION AND DISCOVERY REPORT
==================================================================================================
FILES DISCOVERED:
  128 files discovered across Phases 01 through 07.

FILES READ:
  All primary research documentation across Phases 01–06:
  - 01_Research_Foundation/ (44 paper records, synthesis, taxonomy ledgers)
  - 02_Cross_Analysis/ (algorithmic comparison matrices, trade-offs)
  - 03_Research_Problem/ (RQ1–RQ6, H1–H6, CG1–CG8, RO1–RO6)
  - 04_Research_Evidence/ (DD-001–DD-012, Feature_Traceability.md F01–F22)
  - 05_PRIE_Architecture/ (System, Component, Module M01–M12, SPV, Data, API specs, diagrams)
  - 06_Methodology/ (Research Design, Workflow, EXP-1–EXP-6, datasets, calibration, stats)
  - 07_Implementation/ (All Python source files, configs, schemas, notebooks, models)

FILES NOT READ:
  Binary model pickles in raw hex (unpickled via Python memory inspection instead),
  raw pre-rendered raster diagrams (.png, .pdf, .svg), and compiled Python bytecode (.pyc).

CODE FILES ANALYZED:
  - 07_Implementation/src/app.py
  - 07_Implementation/src/config.py
  - 07_Implementation/src/database/db_manager.py
  - 07_Implementation/src/database/schema.sql
  - All 13 modules in 07_Implementation/src/modules/
  - 07_Implementation/PRIE_v1/backend/main.py
  - 07_Implementation/PRIE_v1/backend/config.py
  - 07_Implementation/PRIE_v1/backend/spv_version.py
  - 07_Implementation/PRIE_v1/backend/database/db_manager.py
  - 07_Implementation/PRIE_v1/backend/database/schema.sql
  - 07_Implementation/PRIE_v1/backend/ml/placement_predictor.py
  - 07_Implementation/PRIE_v1/backend/ml/data_generator.py
  - All 11 module packages in 07_Implementation/PRIE_v1/backend/modules/
  - 07_Implementation/PRIE_v1/backend/tests/test_api.py, test_spv.py
  - 07_Implementation/PRIE_v1/frontend/ (HTML, CSS, JavaScript files)
  - 07_Implementation/notebooks/ScholarCamp_PRIE_Google_Colab.ipynb (All 31 cells)
  - 07_Implementation/notebooks/ScholarCamp_PRIE_Research_From_Scratch.ipynb

MODULES ANALYZED:
  M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, plus auxiliary modules
  (behavior_analyzer.py, sus_evaluator.py, prie_orchestrator.py, recommendation_engine.py).

ARCHITECTURE COMPONENTS:
  CMP-UI-001–010, CMP-GW-001, CMP-INT-001–003, CMP-MDL-001–012, CMP-DAT-001–003, CMP-INF-001–003.

METHODOLOGY COMPONENTS:
  EXP-1 through EXP-6, SPV tensor lifecycle, Platt Scaling, SHAP TreeExplainer, DiCE Recourse,
  LayoutLMv3 NER, Librosa prosody, MediaPipe Action Units, Late Multimodal Fusion,
  Kahn's Topological Sort, ChromaDB RAG, Bloom's AQG, Wilcoxon / McNemar statistical tests.

RESEARCH GAPS:
  CG1 through CG8 fully mapped to architecture modules and implementation defects.

RQ COVERAGE:
  RQ1 through RQ6 mapped; 0 of 6 currently have complete, runnable end-to-end execution pathways.

HYPOTHESIS COVERAGE:
  H1 through H6 mapped; 0 of 6 can be empirically validated without code implementation.

EXPERIMENT READINESS:
  EXP-1: NOT READY (Needs 22D calibrated model)
  EXP-2: NOT READY (Needs DiCE integration)
  EXP-3: NOT READY (Needs M05 video & fusion build)
  EXP-4: NOT READY (Needs LayoutLMv3 pipeline)
  EXP-5: NOT READY (Needs curricular knowledge graph)
  EXP-6: NOT READY (Needs ChromaDB & LLM integration)

CRITICAL BLOCKERS:
  1. Broken Streamlit pages directory causing immediate application crash on launch.
  2. Model path resolution bug in legacy config causing silent fallback to random dummy models.
  3. Divergent SPV feature schema in legacy code and serialized models.
  4. Empty models directory in PRIE_v1 forcing random normal dummy models on API calls.
  5. M05 (Mock Interview Coach) completely missing from PRIE_v1.
  6. DiCE counterfactual optimization unimplemented (stubbed with static rules).
  7. LayoutLMv3 spatial document parser unimplemented (regex only).
  8. Lack of empirical benchmark training pipeline and automated experiment runners.

RESEARCH-CRITICAL IMPROVEMENTS:
  1. Consolidate codebase on PRIE_v1; deprecate legacy Streamlit monolith.
  2. Train cost-sensitive, Platt-scaled XGBoost on canonical 22D SPV; serialize calibrated weights.
  3. Implement DiCE constrained optimization for actionable prescriptive recourse.
  4. Implement M05 Multimodal Interview Coach with Librosa, MediaPipe, and Late Fusion.
  5. Implement LayoutLMv3 spatial token classification for ATS resume intelligence.
  6. Connect authentic curricular skill graph to Kahn's DAG roadmap scheduler.
  7. Implement automated experiment runner suite for EXP-1 through EXP-6.

UI GAPS:
  - Missing Resume Upload and ATS Spatial Visualization interface.
  - Missing Mock Interview Studio with camera/microphone streaming.
  - Missing Interactive What-If Counterfactual Recourse exploration slider interface.

TESTING GAPS:
  - Zero automated unit, integration, or regression tests in legacy prototype.
  - Only 4 basic smoke tests in PRIE_v1/backend/tests/.
  - Zero ML pipeline tests (model drift, invariance, directional sensitivity).
  - Zero end-to-end user evaluation test harnesses.

REPRODUCIBILITY GAPS:
  - Runtime models generated dynamically using unseeded random distributions.
  - No automated dataset ingestion or preparation scripts for DS-BENCH-01 or DS-BENCH-02.
  - Missing locked dependency requirements (requirements.txt lacks pinned hashes).

SECURITY GAPS:
  - Hardcoded default JWT secret key in config files.
  - Path traversal vulnerability in resume upload handling.
  - Wildcard CORS configuration with credentials enabled.
  - Missing API rate limiting on authentication routes.

FINAL STATUS:
  REQUIRES IMPLEMENTATION WORK
==================================================================================================
```
