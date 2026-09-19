# Phase 06 — Research Methodology: Master Repository Index

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/README.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Master Methodology Index  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Phase 06 Mission & Scientific Mandate

Phase 06 formalizes the transition of the Placement Readiness Intelligence Engine (PRIE) from architectural formulation into an empirical, reproducible, and publication-grade scientific research methodology. 

While Phase 03 established the validated research voids (`RG1`–`RG8`) and foundational questions (`RQ1`–`RQ6`, `H1`–`H6`), Phase 04 formulated the empirical evidence taxonomy and design decisions (`DD-001`–`DD-012`, `EXP-1`–`EXP-6`), and Phase 05 constructed the structural subsystem topology (`M01`–`M12`), **Phase 06 establishes HOW the scientific claims will be rigorously investigated, evaluated, and statistically verified**.

### 1.1 Non-Negotiable Epistemological Boundaries
In accordance with academic integrity guidelines and the Phase 06 Master Execution Directives:
1. **Methodology is Not Implementation**: Phase 06 defines formal algorithmic mechanics, sampling protocols, feature mathematics, and statistical testing plans. Concrete software coding belongs to Phase 07 (`07_Implementation`).
2. **Zero Empirical Fabrication**: Phase 06 does not report unobtained empirical metric scores ($F1$, $AUC$, $R^2$, $p$-values, effect sizes). All metrics and thresholds are formulated as formal criteria and decision boundaries for experimental execution in Phase 08 (`08_Experiments`).
3. **Strict Epistemological Status of Datasets**: Public benchmarks (`DS-BENCH-01`, `DS-BENCH-02`, `DS-CORPUS-01`) provide initial baseline references; synthetic cohorts (`DS-SYNTH-01`) serve solely as pre-deployment stress-testing simulations; institutional longitudinal data (`DS-REAL-01`) is rigorously categorized as **NOT YET AVAILABLE / DATA COLLECTION REQUIRED**.

---

## 2. Methodology Architecture & Directory Structure

The methodology is organized into ten thematic clusters comprising 56 synchronized scientific specifications:

```
06_Methodology/
├── README.md                                  # Master index and navigation hub
│
├── [Cluster 1: Research Strategy & Foundations]
│   ├── Research_Design.md                     # Paradigmatic classification & variable topology
│   ├── Methodology_Overview.md                # End-to-end scientific pipeline overview
│   ├── Research_Workflow.md                   # Strict sequential execution & data isolation
│   └── Experimental_Framework.md              # Controlled experimental protocols & decision rules
│
├── [Cluster 2: Dataset Methodology & Governance]
│   ├── Dataset_Design.md                      # Formal specifications for DS-BENCH, CORPUS, SYNTH, REAL
│   ├── Data_Collection.md                     # Multimodal data acquisition & ingestion protocols
│   ├── Data_Governance.md                     # Zero-trust privacy, FERPA/POPIA & versioning
│   ├── Dataset_Splitting.md                   # Leakage-free stratified, grouped & rolling splits
│   ├── Synthetic_Data_Methodology.md          # Copula simulation mechanics & external validity limits
│   └── Real_Data_Methodology.md               # Institutional cohort onboarding protocol (Required)
│
├── [Cluster 3: Data Preparation & Feature Science]
│   ├── Preprocessing.md                       # Robust scaling, MICE imputation & outlier handling
│   ├── Feature_Engineering.md                 # Mathematical derivations of interaction features
│   ├── Feature_Selection.md                   # RFECV, mutual information & redundancy pruning
│   ├── Student_Profile_Vector_Methodology.md  # 22-dimensional tensor construction & updates
│   └── SMOTE.md                               # In-fold class balancing & test set protection
│
├── [Cluster 4: Predictive Modeling & Optimization]
│   ├── Model_Selection.md                     # Candidate vs Selected vs Winner taxonomy
│   ├── Algorithm_Methodology.md               # Mathematical formulation of XGBoost, TFT, S-BERT
│   ├── Hyperparameter_Tuning.md               # Optuna TPE Bayesian search & pruning schedules
│   ├── Training_Methodology.md                # Loss functions, schedules, early stopping, checkpoints
│   ├── Model_Validation.md                    # Stratified K-Fold & rolling-origin backtesting
│   └── Model_Calibration.md                   # Isotonic calibration, Brier score & ECE evaluation
│
├── [Cluster 5: Prediction & Explainability]
│   ├── Prediction_Methodology.md              # Placement probability & categorical tier mapping
│   ├── XAI_Methodology.md                     # TreeSHAP attribution & statistical vs causal separation
│   └── Counterfactual_Methodology.md          # DiCE optimization with immutable feature locking
│
├── [Cluster 6: Document Intelligence & Interview Telemetry]
│   ├── ATS_Methodology.md                     # 2D Spatial LayoutLMv3 vs flat-text NER matching
│   ├── Resume_Processing_Methodology.md       # Bounding-box extraction, chunking & entity tagging
│   ├── Interview_Methodology.md               # Sub-1.5s voice turnaround & Docker sandboxing
│   ├── Audio_Processing_Methodology.md        # Chunked Whisper STT & prosodic extraction
│   ├── Video_Processing_Methodology.md        # In-browser MediaPipe landmark kinematic analysis
│   └── Multimodal_Fusion_Methodology.md       # Hybrid parallel analysis vs raw concatenation
│
├── [Cluster 7: Recommendations, Analytics, AQG & Agents]
│   ├── Recommendation_Methodology.md          # Topological A* graph search over Concept DAGs
│   ├── Learning_Roadmap_Methodology.md        # Adaptive weekly sprint compilation & re-planning
│   ├── Learning_Analytics_Methodology.md      # Event clickstreams, login entropy & Week 3-4 alerts
│   ├── Question_Generation_Methodology.md     # Causal Concept AQG & psychometric item calibration
│   ├── RAG_Methodology.md                     # Two-stage dense retrieval & RAG Triad verification
│   ├── Digital_Twin_Methodology.md            # Multi-stakeholder triangular state synchronization
│   └── Multi_Agent_Methodology.md             # Supervisory orchestration & deterministic routing
│
├── [Cluster 8: Evaluation, Baselines, Statistics & Errors]
│   ├── Evaluation_Methodology.md              # Comprehensive metric suites across all modalities
│   ├── Statistical_Analysis.md                # Hypotheses testing, Wilcoxon, paired t-tests, alpha
│   ├── Ablation_Study_Methodology.md          # Systematic component removal & contribution quantification
│   ├── Baseline_Methodology.md                # State-of-the-art and empirical comparative baselines
│   └── Error_Analysis_Methodology.md          # Failure taxonomy, residual diagnostics & case audits
│
├── [Cluster 9: Reproducibility, Ethics & Validity]
│   ├── Reproducibility.md                     # Environment locking, containerization & artifacts
│   ├── Experiment_Configuration.md            # Declarative execution manifests for EXP-1 to EXP-6
│   ├── Randomness_and_Seeds.md                # RNG control & stochastic bounds documentation
│   ├── Ethical_Methodology.md                 # Student rights, algorithmic fairness & transparent AI
│   ├── Bias_and_Fairness_Methodology.md       # Disparate impact metrics & demographic parity audits
│   └── Threats_to_Validity_Methodology.md     # Four-quadrant validity analysis & residual risks
│
└── [Cluster 10: Traceability, Alignment & Quality Governance]
    ├── Methodology_Traceability.md            # Complete N-dimensional research traceability matrix
    ├── Methodology_to_Architecture.md         # Direct mapping between Phase 05 and Phase 06
    ├── RQ_to_Experiment_Mapping.md            # Operational experimental linkage for RQ1 to RQ6
    ├── Hypothesis_Testing_Plan.md             # Formal decision rules and statistical criteria for H1-H6
    ├── PHASE_06_IMPLEMENTATION_PLAN.md        # Execution plan and deliverable audit checklist
    ├── PHASE_06_METHODOLOGY_LEDGER.md         # Evidence-backed methodological claims ledger
    └── PHASE_06_COMPLETION_REPORT.md          # Final phase sign-off & Phase 07 handover gate
```

---

## 3. Core Traceability Backbone

Every methodology file is strictly linked along the unified research spine:

$$	ext{Research Gap } (RG) \longrightarrow 	ext{Research Objective } (RO) \longrightarrow 	ext{Research Question } (RQ) \longrightarrow 	ext{Hypothesis } (H) \longrightarrow 	ext{Design Decision } (DD) \longrightarrow 	ext{Module } (M) \longrightarrow 	ext{Experiment } (EXP)$$

| Component | Identifier Range | Authoritative Source Document |
| :--- | :---: | :--- |
| **Research Gaps** | `RG1` – `RG8` | `03_Research_Problem/Research_Gap.md` |
| **Research Objectives** | `RO1` – `RO6` | `03_Research_Problem/Research_Objectives.md` |
| **Research Questions** | `RQ1` – `RQ6` | `03_Research_Problem/Research_Questions.md` |
| **Hypotheses** | `H1` – `H6` | `03_Research_Problem/Hypotheses.md` |
| **Design Decisions** | `DD-001` – `DD-012` | `04_Research_Evidence/Design_Decisions.md` |
| **Experimental Decisions** | `EXP-1` – `EXP-6` | `04_Research_Evidence/Experimental_Decisions.md` |
| **Functional Modules** | `M01` – `M12` | `05_PRIE_Architecture/Module_Architecture.md` |
| **Feature Vector** | `F01` – `F22` (22-dim SPV) | `05_PRIE_Architecture/Student_Profile_Vector_Architecture.md` |

---

## 4. Methodological Reading Order & Navigation Guide

For peer reviewers, researchers, and implementation engineers:
1. **To understand the scientific framing and variables**: Read `Research_Design.md` $	o$ `Methodology_Overview.md` $	o$ `Research_Workflow.md`.
2. **To examine the data protocols and feature tensor**: Read `Dataset_Design.md` $	o$ `Dataset_Splitting.md` $	o$ `Student_Profile_Vector_Methodology.md`.
3. **To review predictive, XAI, and multimodal methods**: Read `Algorithm_Methodology.md` $	o$ `Prediction_Methodology.md` $	o$ `XAI_Methodology.md` $	o$ `ATS_Methodology.md` $	o$ `Interview_Methodology.md`.
4. **To inspect experimental plans and statistical tests**: Read `Experimental_Framework.md` $	o$ `Evaluation_Methodology.md` $	o$ `Statistical_Analysis.md` $	o$ `Hypothesis_Testing_Plan.md`.
5. **To verify research integrity and reproducibility**: Read `Reproducibility.md` $	o$ `Methodology_Traceability.md` $	o$ `PHASE_06_COMPLETION_REPORT.md`.
