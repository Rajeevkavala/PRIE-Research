# Baseline Fairness & Parity Audit
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  

## Fairness Check Matrix

| Subsystem | Fairness Criterion | Implementation Safeguard | Status |
|:---|:---|:---|:---:|
| **Tabular Models** | Same Train/Val/Test Split | Seed-locked 80/10/10 stratified split across all models | **PASS** |
| **Preprocessing** | Same Feature Scaling | `StandardScaler` fitted on training fold only, applied to all | **PASS** |
| **Evaluation** | Same Held-Out Test Set | $N=250$ test instances evaluated with identical metric functions | **PASS** |
| **Class Imbalance**| Equivalent Cost Sensitivity | Balanced weighting enabled across both XGBoost and Random Forest | **PASS** |
| **Hyperparameters**| Non-Degraded Baseline Config | Random Forest allotted 100 trees and depth 10; LR given 1000 iters | **PASS** |

**Conclusion**: No baseline was artificially crippled. Fair comparison protocol satisfied.
