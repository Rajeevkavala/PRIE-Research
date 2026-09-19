# PRIE Research Roadmap

This document outlines the operational status, deliverables, dependencies, and next milestones for the PRIE research lifecycle.

---

## 1. Phase Status Summary

```text
Phase 01 — Research Foundation:      DONE
Phase 02 — Cross-Paper Analysis:      NOT STARTED
Phase 03 — Research Problem:          NOT STARTED
Phase 04 — Research Evidence:         NOT STARTED
Phase 05 — PRIE Architecture:         EXISTING / VALIDATE
Phase 06 — Methodology:               NOT STARTED
Phase 07 — Implementation:            EXISTING / VALIDATE
Phase 08 — Experiments:               NOT STARTED
Phase 09 — Results:                   EXISTING / VALIDATE
Phase 10 — Publication:               NOT STARTED
Phase 11 — Review:                    NOT STARTED
Phase 12 — Submission:                NOT STARTED
```

> **Research Integrity Gate:** A phase is marked as `DONE` only when all of its empirical deliverables have been systematically completed, cross-checked against primary sources, and verified.

---

## 2. Granular Phase Deliverables and Dependencies

### Phase 01: Research Foundation
- **Status:** `DONE`
- **Deliverables:**
  - Collection of 48 peer-reviewed research papers (2020–2026).
  - Consolidated `References.bib` and 48 individual BibTeX entries in `Papers/BibTeX/`.
  - Comprehensive `Research-Knowledge-Base` with 10 functional domain folders and 9 synthesis assets.
- **Dependencies:** None.
- **Next Action:** Maintain bibliography audit log.

### Phase 02: Cross-Paper Analysis
- **Status:** `NOT STARTED`
- **Deliverables:**
  - 16 cross-cutting comparative synthesis markdown files analyzing algorithms, datasets, features, and architectures across the 48 papers.
- **Dependencies:** Phase 01.
- **Next Action:** Author cross-paper comparative matrices.

### Phase 03: Research Problem
- **Status:** `NOT STARTED`
- **Deliverables:**
  - Grounded Problem Statement, 5 Core Research Gaps, Research Objectives (RO1–RO5), Research Questions (RQ1–RQ4), and Null/Alternative Hypotheses ($H_0/H_1$).
- **Dependencies:** Phase 01, Phase 02.
- **Next Action:** Formalize gap validation and research questions.

### Phase 04: Research Evidence
- **Status:** `NOT STARTED`
- **Deliverables:**
  - **Feature Traceability Matrix**: Full mapping for all 22 Student Profile Vector features.
  - **Algorithm Justification**: Theoretical and empirical defense of XGBoost, TreeSHAP, Sentence-BERT, etc.
  - **Module Traceability**: 12 PRIE modules mapped to addressed gaps and novel contributions.
  - **Literature-to-PRIE Chain**: 8-stage traceability chain.
- **Dependencies:** Phase 02, Phase 03.
- **Next Action:** Build exhaustive feature traceability table.

### Phase 05: PRIE Architecture
- **Status:** `EXISTING / VALIDATE`
- **Deliverables:**
  - Multi-tier system architecture specification, 22-D Student Profile Vector schema, component designs, and publication-ready SVG/drawio diagrams.
- **Dependencies:** Phase 03, Phase 04.
- **Next Action:** Validate formal vector spaces against production codebase.

### Phase 06: Methodology
- **Status:** `NOT STARTED`
- **Deliverables:**
  - Dataset design, preprocessing protocols, SMOTE class balancing, Bayesian hyperparameter tuning, TreeSHAP formulation, and 5-fold cross-validation setup.
- **Dependencies:** Phase 04, Phase 05.
- **Next Action:** Document formal mathematical formulations.

### Phase 07: Implementation
- **Status:** `EXISTING / VALIDATE`
- **Deliverables:**
  - Preserved `ScholarCamp_PRIE_Google_Colab.ipynb`, source modules (`modules/`, `utils/`, `database/`), production model artifacts (`xgb_model.pkl`, `scaler.pkl`, `feature_names.json`), and `requirements.txt`.
- **Dependencies:** Phase 05, Phase 06.
- **Next Action:** Validate reproducibility on clean virtual environment.

### Phase 08: Experiments
- **Status:** `NOT STARTED`
- **Deliverables:**
  - Pre-registered experimental protocols, multi-classifier benchmarks, 7-component PRS ablation studies, statistical validation (t-tests, confidence intervals), and robustness checks.
- **Dependencies:** Phase 06, Phase 07.
- **Next Action:** Compile baseline comparative experiments.

### Phase 09: Results
- **Status:** `EXISTING / VALIDATE`
- **Deliverables:**
  - Quantitative results (XGBoost 87.8% test accuracy, 0.941 AUC-ROC, 88.2% 5-fold CV), TreeSHAP feature importance rankings, confusion matrix analysis, and calibration curves.
- **Dependencies:** Phase 08.
- **Next Action:** Generate publication-quality figures and tables.

### Phase 10: Publication
- **Status:** `NOT STARTED`
- **Deliverables:**
  - Complete IEEE conference paper LaTeX manuscript (`paper.tex`), Word template, conference presentation deck outline, poster layout, and demonstration walkthrough.
- **Dependencies:** Phase 04, Phase 08, Phase 09.
- **Next Action:** Draft IEEE format manuscript sections.

### Phase 11: Review
- **Status:** `NOT STARTED`
- **Deliverables:**
  - Simulated peer review reports from Reviewers 1, 2, and 3; citation audits; grammar checks; plagiarism screen; IEEE compliance checklist.
- **Dependencies:** Phase 10.
- **Next Action:** Conduct adversarial peer review simulation.

### Phase 12: Submission
- **Status:** `NOT STARTED`
- **Deliverables:**
  - Target conference list (IEEE TLT, IEEE EDUCON, Springer EAIT), editor cover letter, submission history log, and camera-ready repository.
- **Dependencies:** Phase 11.
- **Next Action:** Finalize conference venue selection and deadline calendar.
