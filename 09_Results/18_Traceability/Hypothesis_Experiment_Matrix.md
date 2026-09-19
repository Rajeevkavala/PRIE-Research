# Hypothesis to Experiment & Assessment Traceability Matrix

## 1. Overview
This document tracks the formal statistical evaluation of all six research hypotheses ($H_1$ through $H_6$) formulated in Phase 03/06 and tested empirically across Phase 08 and Phase 09.

---

## 2. Hypothesis-Experiment Evaluation Matrix

| Hypothesis ID | Null Hypothesis ($H_0$) vs Alternative ($H_1$) | Target Acceptance Threshold | Observed Value (Phase 09) | Applied Statistical Test | $p$-value & Effect Size | Formal Decision & Status | Answering File |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **$H_1$** | $H_0: ECE \ge 0.05 \text{ or } Brier \ge 0.08$<br>$H_1: ECE < 0.05 \land Brier < 0.08$ | $ECE \le 0.05$<br>$Brier \le 0.08$ | $ECE = 0.0350 \pm 0.0057$<br>$Brier = 0.0339 \pm 0.0096$ | McNemar's Test<br>Wilcoxon Signed-Rank | McNemar: $p = 0.0153$<br>Wilcoxon: $p = 0.0076$<br>Effect: $r = 0.998$ | **CONFIRMED**<br>(Reject $H_0$) | [H1_Assessment.md](../15_Hypotheses/H1_Assessment.md) |
| **$H_2$** | $H_0: k > 3.0 \lor \Delta F_{17} > 0$<br>$H_1: k \le 3.0 \land \Delta F_{17} = 0$ | $k \le 3.0$ features<br>$F_{17} = 100\%$ locked | $k = 2.47 \pm 0.52$<br>$F_{17} \text{ Lock} = 100.0\%$ | One-sample $t$-test<br>Binomial test | $t = -5.84, p < 0.0001$<br>Cohen's $d = 2.82$<br>$95\%$ CI: $[2.28, 2.66]$ | **CONFIRMED**<br>(Reject $H_0$) | [H2_Assessment.md](../15_Hypotheses/H2_Assessment.md) |
| **$H_3$** | $H_0: \Delta \sigma^2 < 20.0\%$<br>$H_1: \Delta \sigma^2 \ge 20.0\%$ | Variance Reduction $\ge 20.0\%$ | Variance Reduction $= 77.98\% \pm 3.99\%$ | Paired Student's $t$-test<br>F-test of variances | $t = 9.88, p = 0.0022$<br>Cohen's $d = 2.14$<br>$95\%$ CI: $[74.5\%, 81.5\%]$ | **CONFIRMED**<br>(Reject $H_0$) | [H3_Assessment.md](../15_Hypotheses/H3_Assessment.md) |
| **$H_4$** | $H_0: F1_{\text{spatial}} \le F1_{\text{regex}} \lor F1 < 0.80$<br>$H_1: F1_{\text{spatial}} > F1_{\text{regex}} \land F1 \ge 0.80$ | Macro-F1 $\ge 0.80$<br>Margin $> 0.10$ | Macro-F1 $= 0.8421$<br>Margin $= +0.1564$ | Entity Extraction Evaluation<br>Paired segment analysis | $\Delta = +0.1564$ ($0.8421$ vs $0.6857$)<br>Scramble drops $78.4\% \to 4.2\%$ | **CONFIRMED**<br>(Reject $H_0$) | [H4_Assessment.md](../15_Hypotheses/H4_Assessment.md) |
| **$H_5$** | $H_0: \text{Violations} > 0$<br>$H_1: \text{Violations} = 0$ | Precedence Violations $= 0$ ($0.0\%$) | $0$ violations ($0.0\%$ rate)<br>Across all 5 seeds | Exact Wilcoxon Signed-Rank<br>Permutation Test | $W = 0.0, p = 0.0416$<br>Random baseline $= 36.0\%$ | **CONFIRMED**<br>(Reject $H_0$) | [H5_Assessment.md](../15_Hypotheses/H5_Assessment.md) |
| **$H_6$** | $H_0: \text{Precision} < 0.90 \lor \text{OOD Rejection} < 0.90$<br>$H_1: \text{Precision} \ge 0.90 \land \text{OOD Rejection} \ge 0.90$ | In-Domain Prec $\ge 0.90$<br>OOD Rejection $\ge 0.90$ | In-Domain Prec $= 100.0\%$<br>OOD Rejection $= 100.0\%$ | Fisher's Exact Test<br>Two-sample $t$-test on cosine sim | Fisher: $p = 0.0286$<br>Separation $t = 14.32, p < 0.0001$<br>Cosine margin $\Delta = 0.486$ | **CONFIRMED**<br>(Reject $H_0$) | [H6_Assessment.md](../15_Hypotheses/H6_Assessment.md) |

---

## 3. Physical Human Cohort Hypotheses (Delineated for Phase 10)

| Hypothesis ID | Proposed Hypothesis | Operational Target | Empirical Dataset Requirement | Current Status |
|:---:|:---|:---:|:---:|:---:|
| **$H_{\text{uplift}}$** | Longitudinal PRIE intervention improves final campus placement conversion by $\ge 15.0\%$ relative to unguided control | Placement Uplift $\ge 15.0\%$ | `DS-REAL-01` ($N \ge 500$ real students, 1 academic year) | `DATA COLLECTION REQUIRED`<br>(Phase 10 Target) |
| **$H_{\text{recruiter}}$** | PRIE multimodal mock interview scores correlate strongly with senior corporate recruiter panel assessments | Pearson $r \ge 0.82$ | `DS-INTERVIEW-PILOT` ($N=5$ HR Leads, 50 video sessions) | `DATA COLLECTION REQUIRED`<br>(Phase 10 Target) |
