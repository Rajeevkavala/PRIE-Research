# Hyperparameter Tuning Methodology: Optuna Bayesian TPE Optimization & Pruning Protocols

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Hyperparameter_Tuning.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Hyperparameter Tuning Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Tuning Strategy & Scientific Discipline

> [!IMPORTANT]
> **NO INVENTED HYPERPARAMETER VALUES IN PHASE 06**  
> In strict accordance with scientific standards, this document defines the **formal search space**, **optimization algorithms**, **objective functions**, and **pruning rules**.  
> The final numerical parameter values will be discovered through empirical trial execution in Phase 07/08.

Hyperparameter optimization in PRIE is executed via **Optuna** using the **Tree-structured Parzen Estimator (TPE)** algorithm across 5-Fold Stratified Cross-Validation on the Training split.

---

## 2. Invariant Search Spaces by Model Family

### 2.1 Static Classifier Search Space (`XGBoost`)
```python
def xgb_search_space(trial):
    return {
        "n_estimators": trial.suggest_int("n_estimators", 100, 1000, step=50),
        "max_depth": trial.suggest_int("max_depth", 3, 10),
        "learning_rate": trial.suggest_float("learning_rate", 0.005, 0.2, log=True),
        "subsample": trial.suggest_float("subsample", 0.6, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 1.0),
        "min_child_weight": trial.suggest_int("min_child_weight", 1, 10),
        "gamma": trial.suggest_float("gamma", 0.0, 5.0),
        "reg_alpha": trial.suggest_float("reg_alpha", 1e-8, 10.0, log=True),
        "reg_lambda": trial.suggest_float("reg_lambda", 1e-8, 10.0, log=True),
        "scale_pos_weight": trial.suggest_float("scale_pos_weight", 1.0, 5.0)
    }
```

### 2.2 Dynamic Sequence Model Search Space (`TFT`)
```python
def tft_search_space(trial):
    return {
        "hidden_size": trial.suggest_categorical("hidden_size", [32, 64, 128, 256]),
        "lstm_layers": trial.suggest_int("lstm_layers", 1, 3),
        "attention_head_size": trial.suggest_categorical("attention_head_size", [2, 4, 8]),
        "dropout": trial.suggest_float("dropout", 0.1, 0.4),
        "hidden_continuous_size": trial.suggest_categorical("hidden_continuous_size", [16, 32, 64]),
        "learning_rate": trial.suggest_float("learning_rate", 1e-4, 1e-2, log=True),
        "max_grad_norm": trial.suggest_float("max_grad_norm", 0.1, 1.0)
    }
```

---

## 3. Bayesian TPE Optimization Mechanics

The Tree-structured Parzen Estimator models the conditional probability $p(	heta | y)$ by splitting observed trial parameters into two non-parametric kernel density estimators:
$$p(	heta | y) = egin{cases} \ell(	heta) & 	ext{if } y < y^* \ g(	heta) & 	ext{if } y \ge y^* \end{cases}$$
where $y^*$ is the $\gamma$-quantile of observed objective scores (default $\gamma = 0.15$).

The Expected Improvement (EI) is maximized by selecting parameters that maximize the ratio:
$$	ext{EI}(	heta) \propto rac{\ell(	heta)}{g(	heta)}$$

---

## 4. Automated Trial Pruning via Median Stopping Rule

To prevent wasting computational cycles on unpromising parameter configurations:
1. **Pruner**: Optuna `MedianPruner` (prunes trial if intermediate validation loss at step $t$ is worse than the median of intermediate losses of previous trials at step $t$).
2. **Warmup Steps**: Pruning is disabled during the first 10 epochs / boosting iterations (`n_warmup_steps = 10`).
3. **Budget Constraint**: Exactly 100 trials allocated per model architecture under fixed random seed (`seed = 42`).
