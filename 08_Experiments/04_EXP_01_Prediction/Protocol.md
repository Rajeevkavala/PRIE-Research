# Experiment Protocol: EXP-01 (Placement Prediction & Calibration)
- **Experiment ID**: `EXP-01`
- **Target Hypothesis**: `H1`: Calibrated XGBoost satisfies Brier $\le 0.08$ and ECE $\le 0.05$.
- **Dataset**: `DS-SYNTH-01` ($N = 2,500$, stratified 80/10/10 split).
- **Models**: Platt-Calibrated XGBoost ($M_{06}$), Random Forest (`BL-02`), Logistic Regression (`BL-01`).
- **Statistical Tests**: McNemar's test on discordant predictions, Wilcoxon signed-rank test.
