# Hypothesis H1 Assessment: Probability Calibration & Predictive Superiority
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE) — Module $M_{06}$  
**Document**: `09_Results/15_Hypotheses/H1_Assessment.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Decision Outcome**: **SUPPORTED (SYNTHETIC SIMULATION)**  

---

## 1. Formal Hypothesis Definition
- **Identifier**: `H1` (Maps to `RQ1`, `RQ3`, `RO1`, `RO3`, `CG1`, `CG3`)
- **Null Hypothesis ($H_{0,1}$)**:
  $$\text{Brier} > 0.08 \quad \lor \quad \text{ECE} > 0.05$$
  (Platt-calibrated XGBoost does not satisfy the strict calibration bounds on the 22-dimensional SPV).
- **Alternative Hypothesis ($H_{1,1}$)**:
  $$\text{Brier} \le 0.08 \quad \land \quad \text{ECE} \le 0.05$$
  with statistically significant Macro-F1 improvement over baseline models at significance level $\alpha = 0.05$.

---

## 2. Pre-Registered Decision Criteria (from Phase 06)
- Reject $H_{0,1}$ if and only if:
  1. Mean Brier score loss $\le 0.08$ across 5-seed battery.
  2. Mean Expected Calibration Error (ECE) $\le 0.05$ across 10 uniform bins.
  3. McNemar's test on paired predictions indicates statistically significant superiority over Random Forest ($p < 0.05$).

---

## 3. Observed Empirical Evidence (5 Seeds on `DS-SYNTH-01`, $N_{\text{test}} = 250$)
1. **Brier Score Loss**:
   $$\text{Observed Mean Brier} = \mathbf{0.0339 \pm 0.0096} \le 0.08 \quad (\text{Criterion Satisfied})$$
2. **Expected Calibration Error (ECE)**:
   $$\text{Observed Mean ECE} = \mathbf{0.0350 \pm 0.0057} \le 0.05 \quad (\text{Criterion Satisfied})$$
3. **Statistical Superiority vs Random Forest**:
   - McNemar's test: $\chi^2 = 5.8824, p = 0.01529 < 0.05 \implies$ **Significant**.
   - Wilcoxon signed-rank test: $W = 27.0, p = 0.00763 < 0.01$, $r = 0.9983 \implies$ **Significant**.
   - Macro-F1: $0.9390$ vs $0.8935$ ($\Delta = +4.55\%$).

---

## 4. Formal Decision & Verdict
$$\mathbf{DECISION: \quad REJECT \quad H_{0,1} \implies VERDICT: \quad SUPPORTED}$$

All pre-registered quantitative criteria are met across all 5 random seeds.

---

## 5. Limitations & Boundary Conditions
Evaluated on Gaussian Copula simulation cohort `DS-SYNTH-01`. Generalization to physical student populations requires institutional ethics trials.
