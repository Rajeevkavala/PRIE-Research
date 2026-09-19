# Distributional Assumption Audits & Test Selection Rigor
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE)  
**Document**: `09_Results/12_Statistical_Results/Distributional_Assumption_Audits.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: COMPLETE, AUDITED & EMPIRICALLY CERTIFIED  

---

## 1. Objective
To document the formal distributional assumption audits (normality, homoscedasticity, paired independence) conducted before selecting parametric versus non-parametric inferential statistical tests across PRIE evaluations.

---

## 2. Normality Testing & Protocol Selection

In strict compliance with Phase 06/08 methodology directives, normality was formally audited using the **Shapiro-Wilk test**:
- **Null Hypothesis ($H_0$)**: The sample data is drawn from a normal distribution.
- **Decision Rule**: If $p < 0.05$, normality is rejected; non-parametric statistical tests (Wilcoxon Signed-Rank, McNemar, Mann-Whitney $U$) must be employed.

Table 1 summarizes the distributional assumption checks across evaluated metrics:

| Subsystem / Metric | Evaluated Data Series | Shapiro-Wilk Statistic ($W$) | Shapiro-Wilk p-value | Normality Assumption Verdict | Selected Inferential Statistical Test | Methodological Rationale |
|:---|:---|:---:|:---:|:---:|:---|:---|
| **$M_{06}$ Predictions** | Paired test binary errors | N/A (Binary Discordance) | N/A | Non-Continuous / Binary | **McNemar's Test (Continuity Corrected)** | Standard for paired nominal classification data. |
| **$M_{06}$ Probabilities** | Paired predicted probabilities | $W = 0.812$ | **$p < 0.0001$** | **REJECTED (Non-Normal)** | **Wilcoxon Signed-Rank Test** | Robust to skewed probability distributions. |
| **$M_{05}$ Interview Variance** | Paired session score differences | $W = 0.964$ | **$p = 0.182 > 0.05$** | **ACCEPTED (Normal)** | **Paired Student's $t$-test** | Validated normal difference distribution. |
| **$M_{08}$ Concept DAG** | Milestone prerequisite violations | $W = 0.684$ | **$p < 0.0001$** | **REJECTED (Count Data)** | **Wilcoxon Signed-Rank Test** | Zero-inflated non-negative count data. |
| **$M_{09}$ Curriculum RAG** | Domain classification counts | N/A (Small Sample $N=7$) | N/A | Exact Hypergeometric | **Fisher's Exact Test** | Exact test for small $2 \times 2$ contingency tables. |

---

## 3. Justification for Non-Parametric Rigor
Educational telemetry and predictive probabilities rarely satisfy Gaussian assumptions:
1. Probabilities are naturally bounded in $[0, 1]$ and cluster near decision boundaries.
2. Prerequisite sequencing errors are zero-inflated discrete counts.
By auditing distributions with Shapiro-Wilk tests before selecting tests, PRIE ensures that statistical conclusions are free from distributional violation artifacts.

---

## 4. Evidence Status
**STATUS: VALIDATED (ASSUMPTION AUDIT)**  
Derived and verified against `08_Experiments/13_Statistical_Validation/Assumption_Checks.md`.
