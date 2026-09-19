# Research Workflow: Phased Scientific Execution & Data Isolation Protocols

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Research_Workflow.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Research Workflow Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Strict Phase Separation & The Non-Negotiable Test Isolation Rule

A primary methodological defect identified across prior literature (`Paper01`, `Paper06`, `Paper22`) is insidious data leakage caused by fitting scalers on combined datasets or evaluating models on test splits touched during hyperparameter tuning.

PRIE enforces a **zero-leakage firewall** across five strictly separated chronological phases:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        CHRONOLOGICAL WORKFLOW BOUNDARIES                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│  PHASE A: DATA INGRESS & PARTITIONING FIREWALL                                  │
│  • Raw ingestion → Split into Train (80%), Validation (10%), Test (10%)         │
│  • TEST SPLIT IS ISOLATED AND ENCRYPTED. NO FURTHER ACCESS UNTIL PHASE D.       │
│                                                                                 │
│  PHASE B: IN-FOLD PREPROCESSING & FEATURE ENGINEERING                           │
│  • MICE Imputer fitted ONLY on Train split.                                     │
│  • RobustScaler & MinMax fitted ONLY on Train split.                            │
│  • SMOTE oversampling applied ONLY within Train folds.                          │
│                                                                                 │
│  PHASE C: MODEL TRAINING & HYPERPARAMETER OPTIMIZATION                          │
│  • Optuna Bayesian TPE executes across 5-Fold Cross-Validation on Train split.  │
│  • Validation split (10%) used solely for early stopping and pruning.           │
│  • Best model checkpoints serialized with immutable SHA-256 hashes.            │
│                                                                                 │
│  PHASE D: FINAL TEST SET BENCHMARKING & STATISTICAL EVALUATION                  │
│  • Test split decrypted and processed using frozen Train preprocessors.         │
│  • One-shot evaluation: No model tuning or threshold re-calibration allowed.    │
│  • Metric extraction and formal hypothesis significance testing.                │
│                                                                                 │
│  PHASE E: POST-EVALUATION ABLATION & ERROR DIAGNOSTICS                          │
│  • Stratified residual inspection and systematic component removal.             │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Detailed Phased Execution Protocols

### Phase A: Data Ingress & Partitioning Protocol
1. **Raw Ingestion**: Multi-modal records are read from persistent storage.
2. **Schema & Range Sanity**: Numerical values outside realistic human boundaries (e.g., $	ext{CGPA} > 10.0$) trigger immediate data rejection.
3. **Partitioning**:
   - Tabular benchmarks (`DS-BENCH-01`, `DS-SYNTH-01`): Stratified 80/10/10 split preserving target class ratio.
   - Longitudinal benchmarks (`DS-BENCH-02`): Rolling-origin temporal split preserving sequence causality.
   - Multi-modal resumes (`DS-CORPUS-01`): Grouped document split ensuring no student's multiple resume revisions cross partition lines.
4. **Test Set Lock**: The 10% test split is isolated into a separate read-only container with an audit hash.

### Phase B: In-Fold Preprocessing Protocol
1. **Missing Data Imputation**: Multivariate Imputation by Chained Equations (MICE) parameters are calculated using *only* training feature distributions. The fitted imputer is then saved as a transform pipeline.
2. **Outlier Mitigation**: Feature values are clipped to Tukey Interquartile Range boundaries:
   $$	ext{Lower} = Q_1 - 1.5 	imes 	ext{IQR}, \quad 	ext{Upper} = Q_3 + 1.5 	imes 	ext{IQR}$$
3. **Scaling & Normalization**: Continuous features are transformed using `RobustScaler` (zero median, interquartile scaling) followed by Min-Max bounding to $[0.0, 1.0]$.
4. **Class Rebalancing**: If class imbalance exceeds $2:1$, SMOTE is executed *only* on the training split to synthesize minority samples. **Validation and test splits never receive synthetic SMOTE samples**.

### Phase C: Model Training & Hyperparameter Tuning Protocol
1. **Model Instantiation**: Predictors (`XGBoost`, `LightGBM`, `CatBoost`, `TFT`) are initialized with fixed random seeds (`seed = 42`).
2. **Bayesian Optimization**: Optuna executes 100 optimization trials using Tree-structured Parzen Estimator (TPE). Each trial evaluates performance using 5-Fold Stratified Cross-Validation on the training data.
3. **Pruning**: Poorly performing trials are terminated early via the Median Pruner based on intermediate validation loss.
4. **Model Selection**: The hyperparameter configuration maximizing the primary optimization objective (Validation PR-AUC for imbalanced classification; Validation Quantile Loss for TFT) is selected and trained on the full 80% training split.

### Phase D: Final Test Set Benchmarking Protocol
1. **Unsealing the Test Set**: The isolated test set is unlocked.
2. **Deterministic Transform**: The frozen Phase B preprocessing pipeline transforms test features.
3. **One-Shot Inference**: The finalized model predicts outcomes on the test set.
4. **Zero-Feedback Rule**: Under no circumstances may hyperparameter adjustments, feature additions, or threshold manipulations occur after test set evaluation. If an error occurs, the entire pipeline must be re-run from Phase A with a logged revision.
5. **Statistical Significance Testing**: Predicted test scores are paired with baseline scores and evaluated using Wilcoxon signed-rank tests or paired $t$-tests with Bonferroni-Holm corrections.

### Phase E: Ablation & Error Diagnostic Protocol
1. **Ablation Studies**: Predefined modules (e.g., spatial layout tokens, longitudinal sequence history, causal DAG constraints) are systematically disabled to measure performance deltas.
2. **Error Stratification**: All test set prediction failures (False Positives and False Negatives) are categorized by student academic tier, department, and demographic factors to uncover systematic algorithmic blindspots.
