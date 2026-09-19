# Experimental Protocols: Standard Operating Procedures (EXP-01 to EXP-06)
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/01_Experiment_Design/Experimental_Protocols.md`  

---

## Standard 20-Field Protocol Specification

Every experiment in Phase 08 is executed under a standardized 20-field scientific protocol:

### Protocol EXP-01: Calibrated Placement Prediction & Baselines
1. **Research Question**: `RQ1` / `RQ3`
2. **Hypothesis**: `H1`: Calibrated XGBoost satisfies Brier $\le 0.08$ and ECE $\le 0.05$.
3. **Objective**: Evaluate probabilistic reliability and classification accuracy on canonical 22D SPV.
4. **Dataset**: `DS-SYNTH-01` ($N = 2,500$ Gaussian Copula SPV simulation cohort).
5. **Inclusion Criteria**: Complete 22D SPV vectors with valid binary placement labels.
6. **Exclusion Criteria**: Profiles containing NaN or out-of-bounds normalized values ($x_i 
otin [0.0, 1.0]$).
7. **Sample Size**: Total $N = 2,500$ ($N_{	ext{train}} = 2,000$, $N_{	ext{val}} = 250$, $N_{	ext{test}} = 250$).
8. **Feature Set**: Canonical 22D SPV ($F_{01}$ to $F_{22}$).
9. **Preprocessing**: StandardScaler fitted strictly on training fold only; no test contamination.
10. **Training Procedure**: XGBoost with 150 estimators, max depth 5, learning rate 0.1, cost-sensitive weighting.
11. **Validation Procedure**: Platt scaling (sigmoid calibration) fitted on validation fold (`CalibratedClassifierCV`).
12. **Test Procedure**: Blind evaluation on held-out test fold (never seen during training or calibration).
13. **Baseline**: Logistic Regression (L2, $C=1.0$), Random Forest (100 trees, balanced).
14. **Proposed Method**: Platt-Calibrated XGBoost ($M_{06}$).
15. **Metrics**: Brier score loss, Expected Calibration Error (ECE), Macro-F1, ROC-AUC, Accuracy.
16. **Statistical Test**: McNemar's test on paired predictions; Wilcoxon signed-rank test.
17. **Random Seed**: Multi-seed battery: 42, 123, 456, 789, 2026.
18. **Repetitions**: 5 independent deterministic seed runs.
19. **Expected Artifacts**: `raw_metrics.json`, `run_metadata.json`, `summary.csv`, `statistical_tests.json`, `paper_table.tex`.
20. **Reproducibility Requirements**: Deterministic seed execution via `run_experiment.py --experiment EXP-1 --seed <seed>`.

*(Protocols for EXP-02 through EXP-06 follow this exact 20-field schema and are detailed in their respective subsystem folders `05_EXP_02_` through `09_EXP_06_`).*
