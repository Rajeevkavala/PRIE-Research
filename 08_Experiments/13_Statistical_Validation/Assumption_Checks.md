# Statistical Assumption Checks
1. **Normality Test**: Shapiro-Wilk test applied to prediction error residuals.
   - Result: $W = 0.814, p < 0.001$ (Normality rejected; non-parametric tests mandated).
2. **Paired Structure**: Models evaluated on identical instance indices ($N=250$ test fold), satisfying pairing assumptions for McNemar and Wilcoxon.
3. **Multiple Testing Correction**: Bonferroni adjustment applied across the 6 primary hypothesis tests:
   $$lpha_{	ext{adjusted}} = rac{0.05}{6} pprox 0.0083$$
