# PRIE Phase 07 — Implementation Plan
## ScholarCamp: Placement Readiness Intelligence Engine

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Phase**: 07 — Implementation  
**Derived From**: Phase 05 (Architecture) → Phase 06 (Methodology) → Phase 04 (Evidence)  
**Plan Version**: v1.0  
**Date**: September 2026

---

## Background & Scientific Context

Phase 06 is **COMPLETE** (30/30 quality gates passed, PHASE 07 READINESS: CERTIFIED). The implementation must realize exactly the 12-module architecture defined in Phase 05 and the methodology defined in Phase 06. The existing `07_Implementation` prototype is a Streamlit-based reference that is **partially aligned** with the research specification. This plan details a **clean, modular, research-aligned Phase 07 implementation** derived bottom-up from the authoritative research chain.

---

## Gap Analysis: Existing Prototype vs. Research Specification

The existing prototype has the following critical gaps and misalignments:

| Aspect | Existing Prototype | Research Specification | Status |
|:---|:---|:---|:---:|
| **UI Framework** | Streamlit (notebook-like) | HTML5/CSS3/JS (browser-professional) | ❌ GAP |
| **SPV Feature names** | `backlogs`, `internship_months`, `skill_count` (ad-hoc) | `F01_cgpa` through `F22_roadmap_completion_rate` (canonical) | ❌ DIVERGENCE |
| **SPV F10** | Missing `project_quality_score` | Required per `SPV_Architecture.md` | ❌ MISSING |
| **SPV F08** | `soft_skills_score` missing separately | Required per `SPV_Architecture.md` | ❌ MISSING |
| **SPV versioning** | Not versioned | `SPV_VERSION = v1` required | ❌ MISSING |
| **XGB model provenance** | `xgb_model.pkl` — no training script | Training script and provenance required | ❌ MISSING |
| **API layer** | Streamlit pages only | REST API layer (`/api/v1/...`) required | ❌ MISSING |
| **M04: Skill Gap Engine** | Not modular | Standalone module `M04_skill_gap_engine.py` | ❌ MISSING |
| **M07: Prescriptive XAI (DiCE)** | TreeSHAP only | DiCE counterfactuals required | ❌ MISSING |
| **M08: Roadmap (A* DAG)** | Keyword-based only | A* topological DAG traversal required | ❌ MISSING |
| **M11: Behavioral Telemetry (EMA)** | Static defaults (hardcoded 0.60, 0.65) | EMA-computed F16, F21 from event log | ❌ HARDCODED |
| **M12: Digital Twin** | Not present | Triangular sync architecture | ❌ MISSING |
| **Observation mask** | Not implemented | Binary confidence mask `m ∈ {0,1}^22` required | ❌ MISSING |
| **MICE imputation** | Median fallbacks only | MICE imputation on train split | ❌ MISSING |
| **Scientific integrity flag** | None | All demo/synthetic data labeled explicitly | ❌ MISSING |

---

## Directory Structure Realization

```
07_Implementation/
├── (existing reference prototype — UNTOUCHED)
└── PRIE_v1/                          [CLEAN IMPLEMENTATION]
    ├── README.md
    ├── requirements.txt
    ├── IMPLEMENTATION_MANIFEST.json
    │
    ├── backend/                       [Python FastAPI REST Backend]
    │   ├── main.py                    [API entry point]
    │   ├── config.py                  [Env, paths, constants]
    │   ├── spv_version.py             [SPV_VERSION = "v1" constant + schema]
    │   │
    │   ├── modules/                   [M01–M12 implementations]
    │   │   ├── m01_spv_aggregator.py         [M01: SPV Harmonizer]
    │   │   ├── m02_resume_ats.py             [M02: ATS Matcher (SBERT + heuristic)]
    │   │   ├── m03_adaptive_assessment.py    [M03: IRT quiz engine]
    │   │   ├── m04_skill_gap_engine.py       [M04: Weighted Euclidean gap]
    │   │   ├── m06_placement_predictor.py    [M06: XGBoost + SHAP]
    │   │   ├── m07_prescriptive_xai.py       [M07: TreeSHAP + DiCE stub]
    │   │   ├── m08_roadmap_generator.py      [M08: A* DAG traversal]
    │   │   ├── m09_rag_assistant.py          [M09: RAG stub (grounded)]
    │   │   ├── m10_aqg.py                    [M10: AQG stub]
    │   │   ├── m11_behavioral_telemetry.py   [M11: EMA + engagement]
    │   │   └── m12_digital_twin.py           [M12: Twin sync stub]
    │   │
    │   ├── api/                       [API route handlers]
    │   │   ├── v1_profile.py          [GET /api/v1/profile/spv]
    │   │   ├── v1_predict.py          [POST /api/v1/predict/readiness]
    │   │   ├── v1_explain.py          [POST /api/v1/explain/prescribe]
    │   │   ├── v1_roadmap.py          [GET /api/v1/roadmap/active]
    │   │   ├── v1_assessment.py       [GET/POST /api/v1/assessment/...]
    │   │   └── v1_auth.py             [POST /api/v1/auth/...]
    │   │
    │   ├── database/
    │   │   ├── schema.sql             [Updated 3NF schema with F01–F22 column annotations]
    │   │   ├── db_manager.py          [SQLite WAL connection manager]
    │   │   ├── queries.py             [Parameterized SQL queries]
    │   │   └── seed_data.py           [Seed: question bank, skill taxonomy, companies]
    │   │
    │   └── ml/
    │       ├── train_xgb.py           [Clean training script: DS-BENCH-01 + DS-SYNTH-01]
    │       ├── generate_synthetic.py  [DS-SYNTH-01: Gaussian Copula SPV generator]
    │       ├── feature_schema.py      [Canonical F01–F22 definition with metadata]
    │       └── model_manifest.json    [Training provenance: dataset, params, metrics]
    │
    ├── frontend/                      [HTML5/CSS3/JS Single-Page App]
    │   ├── index.html                 [SPA shell + auth routing]
    │   ├── css/
    │   │   └── styles.css             [Premium glassmorphism dark-mode design system]
    │   ├── js/
    │   │   ├── api_client.js          [REST API client layer]
    │   │   └── auth.js                [JWT-based auth manager]
    │   └── pages/
    │       ├── login.html
    │       ├── register.html
    │       ├── dashboard.html         [Student hub: SPV radar + readiness tier]
    │       ├── profile.html           [22-dim SPV profile editor]
    │       ├── assessment.html        [M03: Adaptive quiz]
    │       ├── roadmap.html           [M08: Personalized roadmap]
    │       ├── xai.html               [M07: SHAP + counterfactual view]
    │       └── admin.html             [Faculty cohort view]
    │
    └── docs/
        ├── PHASE_07_IMPLEMENTATION_PLAN.md
        └── IMPLEMENTATION_GAP_ANALYSIS.md
```
