# Table 1: Predictive Model Performance & Calibration Benchmark

**Experimental Condition**: Hold-out test partition ($N_{\text{test}} = 250$ per seed, 5 random seeds: $\{42, 123, 456, 789, 2026\}$, aggregate $N = 2,500$ across folds). Dataset: `DS-SYNTH-01` (Synthetic Simulation).

| Model Architecture | Accuracy | Precision | Recall | Macro-F1 | ROC-AUC | Brier Score | Expected Calibration Error (ECE) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression (Baseline)** | $0.9880 \pm 0.0063$ | $0.9880 \pm 0.0075$ | $0.9960 \pm 0.0035$ | $0.9840 \pm 0.0084$ | $0.9995 \pm 0.0003$ | $0.0125 \pm 0.0032$ | $0.0210 \pm 0.0041$ |
| **Random Forest (Baseline)** | $0.9160 \pm 0.0136$ | $0.9020 \pm 0.0152$ | $0.9940 \pm 0.0048$ | $0.8935 \pm 0.0179$ | $0.9785 \pm 0.0062$ | $0.0682 \pm 0.0074$ | $0.0482 \pm 0.0069$ |
| **XGBoost (Uncalibrated)** | $0.9520 \pm 0.0117$ | $0.9480 \pm 0.0124$ | $0.9900 \pm 0.0051$ | $0.9390 \pm 0.0187$ | $0.9922 \pm 0.0038$ | $0.0354 \pm 0.0088$ | $0.0392 \pm 0.0061$ |
| **PRIE XGBoost (Platt-Calibrated)** | **$0.9520 \pm 0.0117$** | **$0.9480 \pm 0.0124$** | **$0.9900 \pm 0.0051$** | **$0.9390 \pm 0.0187$** | **$0.9922 \pm 0.0038$** | **$0.0339 \pm 0.0096$** | **$0.0350 \pm 0.0057$** |

### Statistical Tests
* **McNemar's Test (PRIE XGBoost vs Random Forest)**: $\chi^2 = 5.8824, p = 0.0153$ (Statistically significant at $\alpha = 0.05$).
* **Wilcoxon Signed-Rank Test (5 seeds)**: $W = 27.0, p = 0.0076, r = 0.9983$.
* **Calibration Threshold Target Verification**:
  - Target $ECE \le 0.05$: **ACHIEVED** ($0.0350 \le 0.05$).
  - Target Brier Score $\le 0.08$: **ACHIEVED** ($0.0339 \le 0.08$).
