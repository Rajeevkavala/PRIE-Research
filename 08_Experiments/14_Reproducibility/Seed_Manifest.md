# Authoritative Random Seed Manifest
Every stochastic module in PRIE accepts an explicit `seed` parameter:
- **Baseline Master Seed**: `42`
- **Multi-Seed Robustness Battery**: `42`, `123`, `456`, `789`, `2026`
- **NumPy RNG**: Initialized via `np.random.default_rng(seed)`
- **Scikit-Learn / XGBoost**: Initialized via `random_state=seed`
