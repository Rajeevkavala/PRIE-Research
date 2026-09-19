# PRIE IMPLEMENTATION ARCHITECTURE
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Epistemological Basis**: Phase 05 (`PRIE_Architecture/`)  
**Baseline Subsystem**: `07_Implementation/PRIE_v1/`

---

## 1. System Topology Overview

PRIE v1 is structured as a decoupled, modular, research-first architecture designed to support empirical experimentation while delivering an accessible web application interface:

```
                            SCHOLARCAMP INTERFACE
                 ┌──────────────────────────────────────────┐
                 │  HTML5 / CSS3 / Vanilla ES6 JavaScript   │
                 │  (Dashboard, ATS, Interview, Twin, XAI)  │
                 └────────────────────┬─────────────────────┘
                                      │ HTTP / REST / JSON
                                      ▼
                             FASTAPI GATEWAY (v1)
                 ┌──────────────────────────────────────────┐
                 │   Pydantic Validation · CORS · JWT Auth  │
                 │   Structured Logging · Explicit Errors   │
                 └────────────────────┬─────────────────────┘
                                      │
       ┌──────────────────────────────┼──────────────────────────────┐
       ▼                              ▼                              ▼
  M01 SPV Aggregator             M02 Resume ATS                 M03 Adaptive Quiz
  (Canonical 22D Tensor)         (PyMuPDF + SBERT)              (Item Bank & History)
       │                              │                              │
       └──────────────────────────────┼──────────────────────────────┘
                                      ▼
                            M04 Skill Gap Engine
                          (Deficit Vector Δx_gap)
                                      │
                                      ▼
                            M06 Placement Predictor
                       (Platt-Calibrated XGBoost 3.2)
                                      │
                   ┌──────────────────┴──────────────────┐
                   ▼                                     ▼
          M07 Prescriptive XAI                  M12 Digital Twin
        (TreeSHAP + DiCE Recourse)             (What-If Simulation)
                   │                                     │
                   ▼                                     │
          M08 Dynamic Roadmap                            │
       (Kahn Topological Sort)                           │
         ┌─────────┴─────────┐                           │
         ▼                   ▼                           ▼
    M09 RAG Assist     M10 Bloom AQG            M11 Company Matcher
  (Dense Retrieval)   (Cognitive Items)         (Enterprise Benchmarks)
                                      ▲
                                      │
                        M05 Multimodal Mock Interview
                      (Librosa + OpenCV + Faster-Whisper)
                                      │
                             Late Multimodal Fusion
```

---

## 2. Layered Architectural Subsystems

### Layer 1: Browser Presentation Layer (`frontend/`)
* **Technology**: Semantic HTML5, Vanilla CSS3 (glassmorphic dark theme, CSS custom variables), Vanilla JavaScript (ES6+ async/await, modular `ApiClient`).
* **Design Philosophy**: Zero framework overhead (no React/Next.js/Vue/Angular build steps), maximum reproducibility, direct API consumption.
* **Pages**:
  - `pages/dashboard.html`: Holistic placement overview, SPV radar breakdown, top strengths and barriers.
  - `pages/profile.html`: Student demographic and academic profile editing with live 22D SPV inspector.
  - `pages/ats.html`: Drag-and-drop resume upload, PyMuPDF spatial bounding box inspector, multi-dimensional ATS scoring.
  - `pages/interview.html`: HTML5 webcam/microphone recorder, timer, and multimodal diagnostics breakdown.
  - `pages/assessment.html`: Topic-based adaptive quizzes with immediate explanation and mastery tracking.
  - `pages/roadmap.html`: DAG-derived weekly milestone progression with prerequisite resolution.
  - `pages/xai.html`: TreeSHAP feature attributions and DiCE actionable recourse directives.
  - `pages/twin_company.html`: What-if perturbation sliders and enterprise benchmark compatibility matcher.
  - `pages/experiments.html`: Research dashboard displaying empirical metrics, hypothesis tests, and LaTeX exports.

### Layer 2: API Gateway Layer (`backend/api/`)
* **Technology**: FastAPI 0.115+, Pydantic v2 data contracts, OAuth2 / Bearer JWT token verification.
* **Endpoints**:
  - `/api/v1/auth/`: Registration, token issuance, password verification (bcrypt).
  - `/api/v1/profile/`: Student profiles, 22D canonical SPV assembly, feature updates.
  - `/api/v1/predict/`: Calibrated placement readiness probability and confidence bounds.
  - `/api/v1/explain/`: TreeSHAP feature attributions and DiCE counterfactual prescriptions.
  - `/api/v1/resume/`: Spatial PDF parsing, keyword matching, ATS scoring.
  - `/api/v1/interview/`: Audio prosody, visual composure, speech diagnostics, multimodal late fusion.
  - `/api/v1/assessment/`: Topic taxonomy, adaptive question serving, answer evaluation.
  - `/api/v1/roadmap/`: CS concept DAG topological sequencing, milestone completion.
  - `/api/v1/rag/`: Dense semantic retrieval against curriculum corpus with grounding safeguard.
  - `/api/v1/aqg/`: Bloom's taxonomy cognitive question generation.
  - `/api/v1/company/`: Enterprise company benchmark matching.
  - `/api/v1/twin/`: Forward feature perturbation simulation and sensitivity matrix.
  - `/api/v1/experiments/`: Execution metadata, metric results, statistical test results, LaTeX exports.

### Layer 3: Research Engine Modules ($M_{01}$ through $M_{12}$)
* Each module is encapsulated in `backend/modules/` with a defined epistemological status, research gap mapping, and automated unit/integration test suite.

### Layer 4: Machine Learning & Inference Subsystem (`backend/ml/`)
* **Base Classifier**: Cost-sensitive `XGBClassifier` tuned with Optuna (`scale_pos_weight` set to handle class imbalance).
* **Calibration**: `CalibratedClassifierCV` utilizing Platt scaling (sigmoid) fitted strictly on calibration splits without data leakage.
* **Model Artifacts**: Stored in `backend/models/` accompanied by `model_manifest.json` recording SHA-256 checksums, hyperparameters, validation scores, and training provenance.

### Layer 5: Multimodal Processing Subsystem (`backend/modules/m05_mock_interview.py`)
* **Acoustic Processing**: `librosa` extracting pitch fundamental frequency $F_0$, jitter, shimmer, tempo (BPM), and silent pause ratio.
* **Visual Processing**: `opencv-python` evaluating face detection confidence, center-screen gaze persistence, and inter-frame motion variance.
* **ASR & Speech Processing**: `faster-whisper` generating verbatim transcripts, computing words per minute (WPM), filler word density, and lexical diversity (Type-Token Ratio).
* **Late Fusion**: Weighted linear combination into a unified composure score ($[0, 100]$) mapping directly to canonical SPV $F_{20}$ (`behavior_score`).

### Layer 6: Persistence & Storage (`backend/database/`)
* **Engine**: SQLite / PostgreSQL compatible schema with foreign keys, cascading rules, and indexed lookup fields across 17 relational tables.
* **Schema**: Defined in `database/schema.sql`.

### Layer 7: Offline Experimentation Subsystem (`experiments/`)
* Fully independent research runner executing experiments `EXP-1` to `EXP-6`.
* Parameterized seed control (`--seed 42`), metric calculators, non-parametric statistical hypothesis evaluators (Wilcoxon, McNemar), and multi-format exporters (JSON, CSV, LaTeX).
