# ScholarCamp — Placement Readiness Intelligence Engine (PRIE v1)
## Phase 07 — Production Implementation Baseline

```
  ____  ____  ___ _____             _ 
 |  _ \|  _ \|_ _| ____| __   _____/ |
 | |_) | |_) || ||  _|   \ \ / / _ \ |
 |  __/|  _ < | || |___   \ V /  __/ |
 |_|   |_| \_\___|_____|   \_/ \___|_|
 Placement Readiness Intelligence Engine
```

**Project**: ScholarCamp AI-Powered Placement Readiness Ecosystem  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Version**: `1.0.0` | **SPV Protocol**: `v1` (22 Invariant Dimensions)  
**Phase**: Phase 07 Implementation (Certified from Phase 06 Quality Gates G01–G30)  
**Architecture**: FastAPI (Backend REST) + 3NF SQLite WAL (Data Layer) + HTML5/CSS3/Vanilla JS (SPA Frontend)

---

## 1. System Overview

**PRIE** is an AI-driven, research-grade cognitive engine designed to evaluate, predict, explain, and prescribe interventions for undergraduate student placement readiness.

Unlike black-box or heuristic placement scoring tools, PRIE grounds all analytics upon an invariant 22-dimensional **Student Profile Vector (SPV)** and guarantees:
1. **Confidence Mask Tracking**: Every profile snapshot maintains an explicit binary observation mask $m \in \{0, 1\}^{22}$ distinguishing empirically observed features from Bayesian-imputed baselines.
2. **Transparent Explainability**: Every prediction is attributed using game-theoretic **TreeSHAP** Shapley values.
3. **Actionable Recourse**: Provides directional counterfactual prescriptions with **immutable feature locks** (e.g. academic branch is never recommended for modification).
4. **Prerequisite-Aware Roadmaps**: Sequences weekly milestones using **A* shortest-path topological traversal** over a Computer Science Concept DAG.

---

## 2. Directory Structure

```
07_Implementation/PRIE_v1/
├── README.md                           # This documentation
├── requirements.txt                    # Python runtime dependencies
├── IMPLEMENTATION_MANIFEST.json        # Machine-readable architecture manifest
│
├── backend/                            # Python REST & ML Engine
│   ├── main.py                         # FastAPI application entry point
│   ├── config.py                       # Global configuration & paths
│   ├── spv_version.py                  # Authoritative F01–F22 SPV schema (SPV_VERSION="v1")
│   │
│   ├── database/                       # 3NF SQLite WAL Data Layer
│   │   ├── schema.sql                  # Database DDL with foreign keys & indexes
│   │   ├── db_manager.py               # Thread-safe connection manager
│   │   ├── queries.py                  # Parameterized SQL query catalog
│   │   └── seed_data.py                # Question bank, companies & demo student seeder
│   │
│   ├── ml/                             # Machine Learning Pipeline
│   │   ├── feature_schema.py           # Canonical feature specifications
│   │   ├── generate_synthetic.py       # Gaussian Copula synthetic cohort generator (DS-SYNTH-01)
│   │   ├── train_xgb.py                # Leakage-free XGBoost training with Bayesian HPO
│   │   └── model_manifest.json         # Real computed model evaluation metrics
│   │
│   ├── modules/                        # Core Intelligence Engines (M01–M12)
│   │   ├── m01_spv_aggregator.py       # M01: Multi-source SPV tensor harmonizer
│   │   ├── m02_resume_ats.py           # M02: SBERT semantic match + ATS analyzer
│   │   ├── m03_adaptive_assessment.py  # M03: 1-PL IRT dynamic quiz engine
│   │   ├── m04_skill_gap_engine.py     # M04: Weighted Euclidean distance deficit ranker
│   │   ├── m06_placement_predictor.py  # M06: Calibrated XGBoost + Bootstrap CI
│   │   ├── m07_prescriptive_xai.py     # M07: TreeSHAP attribution & recourse directives
│   │   ├── m08_roadmap_generator.py    # M08: A* Concept DAG traversal & sequencer
│   │   ├── m09_rag_assistant.py        # M09: Curriculum retrieval assistant (Stub)
│   │   ├── m10_aqg.py                  # M10: Adaptive question generator (Stub)
│   │   ├── m11_behavioral_telemetry.py # M11: EMA consistency & 14-day early warning
│   │   └── m12_digital_twin.py         # M12: Triangular digital twin snapshot (Stub)
│   │
│   └── api/                            # REST Route Controllers
│       ├── v1_auth.py                  # JWT register & login
│       ├── v1_profile.py               # SPV tensor retrieval & update
│       ├── v1_predict.py               # Placement readiness inference
│       ├── v1_explain.py               # TreeSHAP & counterfactual prescriptions
│       ├── v1_roadmap.py               # A* DAG milestone progression
│       └── v1_assessment.py            # IRT adaptive quiz session routing
│
├── frontend/                           # HTML5 / CSS3 / Vanilla JS SPA
│   ├── index.html                      # Landing & architecture overview shell
│   ├── css/
│   │   └── styles.css                  # Premium dark-mode glassmorphism design system
│   ├── js/
│   │   ├── api_client.js               # Centralized REST client with token management
│   │   └── auth.js                     # Client-side session and auth guard
│   └── pages/
│       ├── login.html                  # Student sign-in portal
│       ├── register.html               # Multi-field student registration
│       ├── dashboard.html              # Main student cockpit (Radar chart + Readiness gauge)
│       ├── profile.html                # 22-dimensional SPV inspector & editor
│       ├── assessment.html             # Real-time IRT adaptive quiz interface
│       ├── roadmap.html                # Interactive weekly milestone timeline
│       ├── xai.html                    # TreeSHAP waterfall & counterfactual cards
│       └── admin.html                  # Institutional faculty cohort view
│
└── docs/                               # Formal Research & Audit Records
    ├── IMPLEMENTATION_GAP_ANALYSIS.md  # Detailed audit vs legacy prototype
    └── PHASE_07_IMPLEMENTATION_PLAN.md # Execution blueprint copy
```

---

## 3. Canonical 22-Dimensional Feature Vector ($F_{01} \dots F_{22}$)

| ID | Feature Name | Domain | Normalization Formula | Epistemological Status |
|:---|:---|:---|:---|:---|
| **F01** | `cgpa` | $0.0 \dots 10.0$ | $f / 10.0$ | `DIRECTLY_SUPPORTED` |
| **F02** | `dsa_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F03** | `dbms_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F04** | `os_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F05** | `cn_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F06** | `programming_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F07** | `aptitude_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F08** | `soft_skills_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F09** | `project_count` | $0 \dots 30$ | $\min(f, 30) / 30.0$ | `DIRECTLY_SUPPORTED` |
| **F10** | `project_quality_score` | $0 \dots 100$ | $f / 100.0$ | `PROPOSED` |
| **F11** | `has_internship` | $\{0, 1\}$ | $\{0, 1\}$ | `DIRECTLY_SUPPORTED` |
| **F12** | `certifications_count` | $0 \dots 20$ | $\min(f, 20) / 20.0$ | `PARTIALLY_SUPPORTED` |
| **F13** | `resume_ats_score` | $0 \dots 100$ | $f / 100.0$ | `DIRECTLY_SUPPORTED` |
| **F14** | `cosine_similarity` | $0.0 \dots 1.0$ | $f$ | `DIRECTLY_SUPPORTED` |
| **F15** | `gap_score` | $0.0 \dots 1.0$ | Weighted Euclidean distance | `IMPLEMENTATION_DERIVED` |
| **F16** | `consistency_score` | $0.0 \dots 1.0$ | Exponential Moving Average (EMA) | `IMPLEMENTATION_DERIVED` |
| **F17** | `branch_encoded` | Categorical | Target encoding (**IMMUTABLE**) | `DIRECTLY_SUPPORTED` |
| **F18** | `target_role_encoded` | Categorical | Role profile index | `DIRECTLY_SUPPORTED` |
| **F19** | `assessment_attempts` | Count $\ge 0$ | $\log(1 + f) / \log(51)$ | `DIRECTLY_SUPPORTED` |
| **F20** | `behavior_score` | $0 \dots 100$ | $f / 100.0$ | `PROPOSED` |
| **F21** | `engagement_score` | $0.0 \dots 1.0$ | Log-scaled platform active time | `IMPLEMENTATION_DERIVED` |
| **F22** | `roadmap_completion_rate` | $0.0 \dots 1.0$ | Completed / Total milestones | `IMPLEMENTATION_DERIVED` |

---

## 4. Quickstart Guide

### 4.1 Prerequisites
- Python 3.10+ installed
- Modern web browser (Chrome, Firefox, Edge, Safari)

### 4.2 Setup & Installation

```bash
# 1. Navigate to PRIE_v1 root
cd "07_Implementation/PRIE_v1"

# 2. (Optional) Create virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### 4.3 Initialize Database & Seed Content

```bash
# Initializes 3NF SQLite schema & seeds question bank, companies, skills, and demo user
python backend/database/seed_data.py
```

### 4.4 Train XGBoost Model & Verify Provenance

```bash
# Generates DS-SYNTH-01 (Gaussian Copula) and trains calibrated XGBoost classifier
python backend/ml/train_xgb.py
```

### 4.5 Start FastAPI REST Backend

```bash
# Launch server on port 8000
python -m uvicorn backend.main:app --reload --port 8000
```
Interactive OpenAPI documentation will be accessible at `http://127.0.0.1:8000/docs`.

### 4.6 Launch Frontend Single-Page Application
Open `frontend/index.html` in your web browser, or serve it using any lightweight HTTP server:
```bash
# Simple Python static server
python -m http.server 3000 --directory frontend
```
Navigate to `http://127.0.0.1:3000/` to access the application.

**Default Demo Credentials:**
- **Email**: `demo@scholarcamp.ai`
- **Password**: `password123`

---

## 5. Scientific Integrity Commitments

1. **Zero Metric Fabrication**: No artificial accuracy or AUC metrics are claimed. All reported figures derive from rigorous stratified 80/10/10 train-validation-test evaluation runs.
2. **Explicit Synthetic Identification**: All data synthesized via Gaussian Copula is programmatically and structurally tagged as `SYNTHETIC_SIMULATION`.
3. **Immutable Constraint Safety**: Academic branch ($F_{17}$) is hard-coded as immutable in recourse engines to guarantee realistic, ethical student guidance.

---

*ScholarCamp Research Ecosystem · Placement Readiness Intelligence Engine (PRIE)*
