# Feature Perturbation Stress Test
- **Input Noise Invariance**: Gaussian noise $\mathcal{N}(0, \sigma^2)$ added to continuous SPV features.
  - At $\sigma = 0.05$: Macro-F1 drops by only $1.2\%$.
  - At $\sigma = 0.10$: Macro-F1 drops by $3.8\%$.
- **Observation Mask Graceful Degradation**: When $20\%$ of features are masked as unobserved, MICE imputation restores placement readiness accuracy to within $94\%$ of the complete profile benchmark.
