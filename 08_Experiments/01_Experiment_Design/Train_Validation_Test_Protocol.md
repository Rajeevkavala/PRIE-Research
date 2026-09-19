# Train / Validation / Test Splitting Protocol
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/01_Experiment_Design/Train_Validation_Test_Protocol.md`  

---

## 1. Data Partitioning Architecture

To guarantee absolute methodological rigor and eliminate data snooping, all tabular learning pipelines in PRIE adhere to an invariant **80/10/10 Stratified Split**:

```
Total Cohort (N = 2,500)
├── Training Fold: 80% (N = 2,000)   -> Feature scaling, in-fold SMOTE, base model training
├── Validation Fold: 10% (N = 250)   -> Optuna hyperparameter tuning, Platt probability calibration
└── Test Fold: 10% (N = 250)         -> Held-out final benchmark inference ONLY
```

---

## 2. Preprocessing & Leakage Isolation Boundaries

1. **Scalers & Normalizers**: Fitted exclusively on the training fold ($\mathbf{X}_{	ext{train}}$). Validation ($\mathbf{X}_{	ext{val}}$) and test ($\mathbf{X}_{	ext{test}}$) splits are transformed using training parameters.
2. **Missing Value Imputation**: MICE regression chains are fitted only on $\mathbf{X}_{	ext{train}}$.
3. **Probability Calibration**: Platt scaling (sigmoid mapping) and Isotonic regression are fitted exclusively on the validation fold ($\mathbf{X}_{	ext{val}}, \mathbf{y}_{	ext{val}}$). The test fold is never used to calibrate probabilities.
4. **Class Balancing**: Cost-sensitive weighting (`scale_pos_weight`) is calculated strictly from the training label distribution:
   $$	ext{scale\_pos\_weight} = rac{\sum(\mathbf{y}_{	ext{train}} == 0)}{\sum(\mathbf{y}_{	ext{train}} == 1)}$$
