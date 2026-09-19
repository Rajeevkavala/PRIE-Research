# Seed Sensitivity & Stochastic Stability Analysis
**Battery Evaluated**: Seeds $\{42, 123, 456, 789, 2026\}$

| Metric | Mean Value | Standard Deviation | 95% Confidence Interval | Min Observed | Max Observed | Stability Verdict |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **XGBoost Macro-F1** | $0.9390$ | $\pm 0.0187$ | $[0.9226, 0.9554]$ | $0.9167$ | $0.9602$ | Highly Stable |
| **XGBoost ROC-AUC** | $0.9922$ | $\pm 0.0038$ | $[0.9889, 0.9955]$ | $0.9868$ | $0.9961$ | Extremely Stable |
| **XGBoost Brier Score** | $0.0339$ | $\pm 0.0096$ | $[0.0255, 0.0423]$ | $0.0246$ | $0.0468$ | Invariant ($< 0.08$) |
| **XGBoost ECE** | $0.0350$ | $\pm 0.0057$ | $[0.0300, 0.0400]$ | $0.0289$ | $0.0421$ | Invariant ($< 0.05$) |
| **Multimodal Var Red %**| $77.98\%$ | $\pm 3.99\%$ | $[74.48\%, 81.48\%]$ | $72.11\%$ | $82.45\%$ | Invariant ($> 50\%$) |
| **Kahn DAG Violations** | $0.0$ | $\pm 0.0$ | $[0.0, 0.0]$ | $0$ | $0$ | Deterministic Zero |

**Conclusion**: All core research targets hold with narrow confidence intervals across all random seeds.
