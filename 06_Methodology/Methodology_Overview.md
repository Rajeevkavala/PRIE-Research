# Methodology Overview: End-to-End Scientific Architecture & Pipeline Execution

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Methodology_Overview.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Methodological Overview  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. The End-to-End Methodological Pipeline

The scientific methodology of PRIE transforms heterogeneous, raw student telemetry into actionable, mathematically verified, and institutionally synchronized career readiness intelligence. The complete pipeline executes across twelve strictly phased methodological operations:

```
[Raw Telemetry Sources]
(SIS Transcripts, Resume PDFs, Interview Audio/Video, LMS Logs, Code Sandboxes)
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. DATA VALIDATION & INGRESS SANITIZATION                   │
│    • Schema verification, type casting, range bounding      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. LEAKAGE-FREE DATASET SPLITTING                           │
│    • Stratified 80/10/10 split (Tabular)                    │
│    • Rolling-Origin Backtesting Split (Longitudinal)        │
│    • Group-Student Split (Prevents Identity Leakage)        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. MULTIMODAL PREPROCESSING & FEATURE EXTRACTION            │
│    • MICE imputation (fitted on Train split only)           │
│    • Tukey IQR outlier clipping & RobustScaler transforms   │
│    • LayoutLMv3 2D bounding boxes & S-BERT dense embeddings │
│    • Silero VAD + Whisper STT & MediaPipe 30 FPS landmarks  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. INVARIANT 22-DIMENSIONAL SPV HARMONIZATION (M01)         │
│    • Normalized feature tensor x_spv in [0.0, 1.0]^22       │
│    • Observation confidence mask m in {0, 1}^22             │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. DUAL-TRACK PREDICTIVE MODELING (M06)                     │
│    • Track 1: Static Cross-Sectional XGBoost Classifier     │
│    • Track 2: Longitudinal Sequence Temporal Fusion Trans.  │
│    • Optuna Bayesian TPE Hyperparameter Tuning (CV Folds)   │
│    • Isotonic Probability Calibration                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. TWO-TIERED EXPLAINABLE AI & RECOURSE (M07)               │
│    • Tier 1: Fast TreeSHAP Feature Attribution              │
│    • Tier 2: DiCE Prescriptive Counterfactual Optimization  │
│    • Immutable demographic locking (branch, gender, SIS)    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. TOPOLOGICAL CAREER PATHWAY & ROADMAP GENERATION (M08)    │
│    • Constrained A* graph search over Concept DAG           │
│    • Prerequisite safety filter & milestone sprint compiling│
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 8. FORMATIVE INTERVENTION & ADAPTIVE ASSESSMENT (M09, M10)  │
│    • Two-stage Curriculum RAG with RAG Triad Runtime Guard  │
│    • Causal Concept DAG-guided Question & Distractor Gen    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 9. MULTI-STAKEHOLDER DIGITAL TWIN SYNCHRONIZATION (M12)     │
│    • Triangular sync: Student, Faculty, Placement Cell      │
│    • Differential Privacy Proxy (eps <= 1.0)                │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 10. STATISTICAL EVALUATION & HYPOTHESIS TESTING             │
│    • Wilcoxon signed-rank & paired t-tests (EXP-1 to EXP-6) │
│    • Bonferroni-Holm family-wise error control (alpha=0.05) │
│    • Systematic ablation & stratified error audits          │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Granular Methodological Stages

### Stage 1: Data Ingress, Validation & Sanitization
All multimodal inputs pass through strict boundary sanitizers. Numerical records are clipped to domain limits; text files undergo encoding normalization; PDFs are inspected for corrupted stream objects; audio waveforms are resampled to 16 kHz mono PCM.

### Stage 2: Leakage-Free Dataset Splitting
Data partitioning occurs **prior** to any data transformation. Scalers, imputers, and encoders are fit exclusively on the Training set and then applied deterministically to Validation and Test splits. Cross-student group partitioning prevents identity leakage.

### Stage 3: Specialized Perception & Feature Science
- **Document Intelligence**: LayoutLMv3 processes resume pages as multi-modal tokens combining word text, 2D coordinates $[x_0, y_0, x_1, y_2]$, and visual image patches.
- **Audio/Video Processing**: Streaming audio is segmented via Silero VAD and transcribed via Whisper. Browser-side MediaPipe FaceMesh computes facial landmark kinematics without transferring raw video frames.
- **Coding Assessment**: Student code runs in isolated Docker containers with non-root privileges, generating test pass rates and execution efficiency metrics.

### Stage 4: Invariant SPV Harmonization
Extracted features are mapped into the invariant 22-dimensional Student Profile Vector $\mathbf{x}_{	ext{spv}} \in \mathbb{R}^{22}$. Incomplete features are flagged in the observation mask $\mathbf{m} \in \{0, 1\}^{22}$ and imputed via MICE without altering the 22-dimensional schema.

### Stage 5: Dual-Track Predictive Modeling
Readiness is evaluated through two complementary tracks:
1. **Static Track (XGBoost)**: Evaluates current employability eligibility against corporate hiring cutoffs.
2. **Dynamic Track (Temporal Fusion Transformer)**: Ingests longitudinal telemetry vectors over multi-week windows to forecast multi-horizon trajectory curves ($q_{0.1}, q_{0.5}, q_{0.9}$).

### Stage 6: Two-Tiered Explainable AI
Predictions are interpreted via TreeSHAP to reveal which features drove the score down. These deficits are ingested by DiCE to compute a minimal-effort, feasible counterfactual vector showing the exact metric targets required to transition to the ready class.

### Stage 7: Prescriptive Recommendation & Learning Roadmaps
Counterfactual targets are passed to an $A^*$ topological graph traversal engine operating over a Computer Science Concept DAG. The engine identifies the shortest valid learning sequence that satisfies all prerequisite dependencies.

### Stage 8: Formative Support & Assessment
- **Curriculum RAG**: Provides grounded learning materials retrieved via dense embeddings and verified at runtime by the RAG Triad.
- **Causal AQG**: Generates diagnostic multiple-choice questions targeting specific conceptual misconceptions identified in the student's skill gap.

### Stage 9: Closed-Loop Digital Twin Governance
The updated student profile is synchronized across student, faculty, and placement cell dashboards. Faculty receive early-warning alerts for disengaged students; placement officers receive differentially private candidate shortlists.

### Stage 10: Statistical Verification & Hypothesis Testing
Experimental protocols (`EXP-1`–`EXP-6`) evaluate model accuracy, latency, forecasting precision, actionability, item discrimination, and placement uplift against rigorous null hypotheses with family-wise error rate control.
