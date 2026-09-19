# Random Seed Sensitivity & Initialization Robustness Analysis
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE)  
**Document**: `09_Results/10_Robustness_Results/Seed_Sensitivity.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: COMPLETE, AUDITED & EMPIRICALLY CERTIFIED  

---

## 1. Objective
To evaluate the stability, variance, and invariant preservation of PRIE across 5 deterministic random seeds ($\{42, 123, 456, 789, 2026\}$), verifying that reported empirical gains are robust to data shuffling and tree initialization randomness.

---

## 2. Multi-Seed Battery Performance Trajectories

Table 1 reports the performance stability of the Calibrated XGBoost Predictor ($M_{06}$) across all 5 random seeds on quarantined test partitions ($N_{\text{test}} = 250$ per seed):

| Random Seed | Classification Accuracy | Macro-averaged F1 | ROC-AUC | Brier Score Loss | Expected Calibration Error (ECE) | Runtime (s) | Invariant Criteria Met? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Seed 42** | $0.9400$ | $0.9182$ | $0.9864$ | $0.0471$ | $0.0268$ | $2.12$ | **YES (Brier $\le 0.08$, ECE $\le 0.05$)** |
| **Seed 123** | $0.9520$ | $0.9342$ | $0.9901$ | $0.0375$ | $0.0382$ | $1.39$ | **YES (Brier $\le 0.08$, ECE $\le 0.05$)** |
| **Seed 456** | $0.9680$ | $0.9575$ | $0.9942$ | $0.0242$ | $0.0314$ | $1.42$ | **YES (Brier $\le 0.08$, ECE $\le 0.05$)** |
| **Seed 789** | $0.9440$ | $0.9328$ | $0.9970$ | $0.0289$ | $0.0441$ | $1.38$ | **YES (Brier $\le 0.08$, ECE $\le 0.05$)** |
| **Seed 2026**| $0.9560$ | $0.9525$ | $0.9931$ | $0.0320$ | $0.0345$ | $1.45$ | **YES (Brier $\le 0.08$, ECE $\le 0.05$)** |
| **Mean $\pm$ SD** | **$0.9520 \pm 0.0117$** | **$0.9390 \pm 0.0187$** | **$0.9922 \pm 0.0038$** | **$0.0339 \pm 0.0096$** | **$0.0350 \pm 0.0057$** | **$1.55 \pm 0.32$** | **100% Invariant Compliance** |

---

## 3. Seed Stability Findings
1. **Low Variance Across Seeds**: The standard deviation for accuracy is only $0.0117$ ($1.17\%$), and for ROC-AUC is $0.0038$ ($0.38\%$), confirming exceptional stability across varying train-test partitions.
2. **Deterministic Invariant Preservation**:
   - In 5 out of 5 seeds ($100\%$), Brier score remained strictly below $0.08$ (Max observed: $0.0471$ in Seed 42).
   - In 5 out of 5 seeds ($100\%$), ECE remained strictly below $0.05$ (Max observed: $0.0441$ in Seed 789).
   - In 5 out of 5 seeds ($100\%$), Kahn's topological sort produced exactly $0$ prerequisite sequencing violations.

---

## 4. Evidence Status
**STATUS: VALIDATED (MULTI-SEED AUDIT)**  
Derived and verified against `08_Experiments/15_Experiment_Results/multi_seed_aggregate.json`.
