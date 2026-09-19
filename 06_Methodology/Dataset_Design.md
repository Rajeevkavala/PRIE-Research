# Dataset Design: Multi-Modal Portfolio, Schema Specifications & Epistemological Taxonomy

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Dataset_Design.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Dataset Portfolio Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Epistemological Stance on Research Datasets

A critical flaw identified across the literature corpus (`Paper01`, `Paper06`, `Paper22`) is the unscientific conflation of synthetic mock datasets with empirical real-world evidence. In PRIE, every dataset is assigned an immutable epistemological tier:

1. **`REAL (Public Benchmark)`**: Open-source, peer-reviewed benchmark datasets used strictly for cross-paper baseline comparison and model pre-training.
2. **`SYNTHETIC (Simulation)`**: Statistically generated cohorts designed strictly for algorithmic stress-testing, optimization convergence, and boundary edge testing. **Never claimed as empirical evidence**.
3. **`REAL (Proposed Cohort)`**: Multi-modal longitudinal telemetry collected from actual undergraduate students under approved institutional governance. When not yet collected, it is explicitly cataloged as **`NOT YET AVAILABLE / DATA COLLECTION REQUIRED`**.

---

## 2. Exhaustive Dataset Portfolio Inventory

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                             PRIE DATASET PORTFOLIO ARCHITECTURE                             │
├──────────────┬──────────────┬──────────────┬──────────────────┬─────────────────────────────┤
│ Dataset ID   │ Modality     │ Sample Size  │ Epistemological  │ Primary Scientific Role     │
│              │              │              │ Status           │                             │
├──────────────┼──────────────┼──────────────┼──────────────────┼─────────────────────────────┤
│ DS-BENCH-01  │ Tabular      │ N = 215      │ REAL (Public)    │ Static classifier baseline  │
│ DS-BENCH-02  │ Longitudinal │ N = 32,593   │ REAL (Public)    │ Temporal sequence modeling  │
│ DS-CORPUS-01 │ PDF / Text   │ N = 1,200    │ REAL (Public)    │ Spatial ATS entity parsing  │
│ DS-SYNTH-01  │ Multi-Modal  │ N = 2,500    │ SYNTHETIC        │ Pre-deployment simulation   │
│ DS-REAL-01   │ Multi-Modal  │ Target N≥1000│ PROPOSED         │ Institutional validation    │
└──────────────┴──────────────┴──────────────┴──────────────────┴─────────────────────────────┘
```

---

## 3. Granular Dataset Specifications

---

### Dataset DS-BENCH-01: Public Campus Placement Benchmark
- **Dataset Identifier**: `DS-BENCH-01`
- **Source**: Kaggle Campus Placement Dataset (Secondary education and MBA placement records).
- **Unit of Analysis**: Individual Student Candidate ($N = 215$).
- **Features Captured**: Secondary percentage (`ssc_p`), Higher secondary percentage (`hsc_p`), Degree percentage (`degree_p`), Specialization (`specialisation`), Employability test percentage (`etest_p`), Work experience flag (`workex`), MBA percentage (`mba_p`).
- **Target Variable**: Binary placement status (`status` $\in \{	ext{Placed}, 	ext{Not Placed}\}$).
- **Class Balance**: 148 Placed (68.8%), 67 Not Placed (31.2%).
- **Primary Use in Research**: Evaluates baseline static tabular classifiers (Logistic Regression, Random Forest, Decision Tree, XGBoost) to replicate historical literature baselines (`Paper01`, `Paper06`, `Paper22`).
- **Limitations**: Modest sample size ($N=215$); tabular academic indicators only; completely lacks technical coding, resume, and interview signals.

---

### Dataset DS-BENCH-02: Open University Learning Analytics Dataset (OULAD)
- **Dataset Identifier**: `DS-BENCH-02`
- **Source**: Kuzilek et al., Open University (OULAD public release).
- **Unit of Analysis**: Student-Module Registration Course ($N = 32,593$ students across 22 module presentations).
- **Features Captured**: Longitudinal daily Virtual Learning Environment (VLE) clickstream events across 20 activity types (forum, quiz, resource, homepage, subpage), assessment submission timestamps, submission delays, formative assessment scores.
- **Target Variable**: Student outcome category (`final_result` $\in \{	ext{Distinction}, 	ext{Pass}, 	ext{Fail}, 	ext{Withdrawn}\}$), mapped to binary academic risk.
- **Primary Use in Research**: Training and benchmarking the Temporal Fusion Transformer (`TFT`) for longitudinal multi-horizon forecasting (`EXP-3`).
- **Limitations**: Distance-learning demographic context; activity logs reflect general modular study rather than live software coding practice.

---

### Dataset DS-CORPUS-01: Multi-Modal Resume & Technical Job Description Corpus
- **Dataset Identifier**: `DS-CORPUS-01`
- **Source**: Aggregation of Kaggle Resume Entities, open-source technical resume repositories, and verified technical job postings.
- **Unit of Analysis**: Resume Document ($N = 1,200$ resumes) paired against Technical Job Descriptions ($N = 500$ JDs).
- **Layout Distribution**:
  - Single-column standard chronological layouts: 400 documents (33.3%).
  - Two-column modern technical layouts: 500 documents (41.7%).
  - Complex multi-column, icon-heavy, non-standard layouts: 300 documents (25.0%).
- **Annotations**: Word-level 2D bounding boxes $[x_0, y_0, x_1, y_1]$ with BIO entity tagging across: `SKILL`, `EDUCATION`, `EXPERIENCE`, `PROJECT`, `CERTIFICATION`, `ORGANIZATION`.
- **Primary Use in Research**: Validating LayoutLMv3 multimodal spatial parsing against flat-text NER (`EXP-1`).
- **Limitations**: Annotation noise in public labels; required manual gold-standard verification on a 200-document test subset.

---

### Dataset DS-SYNTH-01: PRIE Synthetic SPV Simulation Cohort
- **Dataset Identifier**: `DS-SYNTH-01`
- **Generation Mechanics**: Gaussian Copula fitted to marginal empirical distributions and correlation structures from `DS-BENCH-01` and published higher education engineering cohorts (`DD-012`).
- **Unit of Analysis**: Synthetic Student Profile Vector ($N = 2,500$ complete 22-dimensional tensors $\mathbf{x}_{	ext{spv}} \in \mathbb{R}^{22}$).
- **Features Generated**: All 22 invariant features (`F01` to `F22`) with calibrated inter-feature correlations (e.g., Pearson $r = 0.68$ between `cgpa` and `dsa_score`; $r = -0.54$ between `gap_score` and `cosine_similarity`).
- **Target Variable**: Synthetic Placement Readiness Tier $\in \{	ext{Ready}, 	ext{Remediating}, 	ext{Unready}\}$.
- **Primary Use in Research**: Pre-deployment system stress-testing, Optuna hyperparameter tuning, TreeSHAP attribution verification, and DiCE counterfactual convergence benchmarking (`EXP-4`).
- **Strict Scientific Limitation**: **Synthetic data is a computational stress-testing tool. It does not constitute real-world empirical proof of human student behavior or predictive validity.**

---

### Dataset DS-REAL-01: Proposed Real-World Institutional Longitudinal Cohort
- **Dataset Identifier**: `DS-REAL-01`
- **Current Status**: **`NOT YET AVAILABLE / DATA COLLECTION REQUIRED`**
- **Target Population**: Undergraduate engineering students (B.Tech / B.E. Computer Science, Information Technology, Electronics) across Semesters 5 through 8.
- **Target Sample Scope**: Target $N \ge 1,000$ active students tracked across a 12-month placement preparation cycle.
- **Multimodal Telemetry Scope**: SIS registrar records, Git commit telemetry, LayoutLMv3 parsed resumes, Docker sandbox test pass rates, chunked Whisper interview transcripts, MediaPipe facial kinematics, and LMS login cadence.
- **Target Variable**: Verified campus recruitment placement outcome (`Placed` / `Unplaced`, corporate salary tier, hiring company category).
- **Governance**: Pre-approved institutional ethics review, informed digital consent, zero raw biometric storage, and FERPA/POPIA compliant anonymization.
