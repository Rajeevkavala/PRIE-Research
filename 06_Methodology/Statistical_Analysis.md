# Statistical Analysis Methodology: Null Hypotheses, Parametric/Non-Parametric Tests & Corrections

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Statistical_Analysis.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Statistical Analysis Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Formal Statistical Hypotheses Testing Architecture

In strict avoidance of empirical fabrication, this document establishes the formal statistical test procedures, distributional assumptions, effect size formulations, and decision thresholds for verifying hypotheses `H1` through `H6`:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                STATISTICAL HYPOTHESES TESTING MATRIX                                    │
├──────┬──────────────────────┬────────────────────────────┬────────────────────────┬─────────────────────┤
│ Hyp  │ Dependent Variable   │ Statistical Test Selected  │ Distribution Assump.   │ Effect Size Metric  │
├──────┼──────────────────────┼────────────────────────────┼────────────────────────┼─────────────────────┤
│ H1   │ Resume Boundary-F1   │ Wilcoxon Signed-Rank Test  │ Non-parametric, paired │ Rank-Biserial r     │
│ H2   │ Turn Latency (ms)    │ Paired t-test              │ Normal deltas (Shapiro)│ Cohen's d           │
│ H2b  │ Recruiter Alignment  │ Pearson Correlation Test   │ Bivariate normal       │ Correlation r       │
│ H3   │ Quantile Loss        │ Diebold-Mariano / Wilcoxon │ Non-parametric paired  │ Percentage Delta %  │
│ H4   │ Actionability Likert │ Paired Student's t-test    │ Quasi-continuous paired│ Cohen's d           │
│ H4b  │ 30-Day Completion    │ Chi-Square / Fisher Exact  │ Discrete counts        │ Odds Ratio (OR)     │
│ H5   │ Item Discrimination  │ Independent Samples t-test │ Equal variance (Levene)│ Cohen's d           │
│ H6   │ Placement Conversion │ Two-Proportion Z-Test      │ Independent binomial   │ Relative Risk / ARR │
└──────┴──────────────────────┴────────────────────────────┴────────────────────────┴─────────────────────┘
```

---

## 2. Test Selection Rationale & Assumption Testing

### 2.1 Normality & Homoscedasticity Pre-Testing
Prior to executing parametric hypothesis tests:
1. **Shapiro-Wilk Test**: Evaluates normality of difference scores:
   $$W = \frac{(\sum_{i=1}^n a_i x_{(i)})^2}{\sum_{i=1}^n (x_i - \bar{x})^2}$$
   If $p < 0.05$, normality is rejected, automatically routing the evaluation to non-parametric equivalents (Wilcoxon Signed-Rank Test or Mann-Whitney $U$ Test).
2. **Levene's Test**: Evaluates equality of variances across groups ($p > 0.05$ required for standard Student's $t$-test; Welch's $t$-test applied upon violation).

### 2.2 Wilcoxon Signed-Rank Test Formulation (H1, H3)
For paired performance differences $d_i = \text{Metric}_{\text{PRIE}}^{(i)} - \text{Metric}_{\text{Baseline}}^{(i)}$:
1. Rank absolute differences $|d_i|$ while discarding zero differences.
2. Calculate test statistic $W$:
   $$W = \min(W^+, W^-), \quad W^+ = \sum_{d_i > 0} \text{Rank}(|d_i|)$$
3. The rank-biserial correlation effect size is computed as:
   $$r = \frac{4 |W - \frac{n(n+1)}{4}|}{n(n+1)}$$

---

## 3. Multiple Comparison Correction (Bonferroni-Holm)

When evaluating multiple ablation variants or departmental sub-cohorts, testing $m$ simultaneous hypotheses inflates the family-wise Type I error rate ($\alpha_{\text{FWER}} = 1 - (1 - \alpha)^m$).

PRIE strictly applies the step-down **Bonferroni-Holm procedure**:
1. Sort unadjusted $p$-values in ascending order: $p_{(1)} \le p_{(2)} \le \dots \le p_{(m)}$.
2. Reject $H_{(k)}$ if:
   $$p_{(k)} \le \frac{\alpha}{m - k + 1}$$
3. Continue testing until the first non-significant result ($p_{(j)} > \frac{\alpha}{m - j + 1}$), after which all remaining hypotheses are retained.
