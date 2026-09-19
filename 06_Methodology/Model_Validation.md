# Model Validation Methodology: Cross-Validation, Hold-Out Partitioning & Generalization Audits

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Model_Validation.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Model Validation Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Strict Separation: Validation Performance vs Final Test Performance

> [!IMPORTANT]
> **EPISTEMOLOGICAL RULE: NEVER CONFOUND VALIDATION WITH TEST PERFORMANCE**  
> **Validation Performance** represents model performance across internal cross-validation folds utilized for model selection, pruning, and hyperparameter tuning.  
> **Test Performance** represents final, un-tuned, one-shot evaluation on the isolated holdout test partition (`test_split.parquet`).  
> Phase 06 enforces a strict firewall between validation metrics and definitive test reporting.

---

## 2. Validation Protocols by Architecture

### 2.1 Repeated 5-Fold Stratified Cross-Validation (Static Models)
- **Protocol**: 5-Fold Stratified Cross-Validation repeated across 3 independent random seed initializations (15 total validation evaluations).
- **Stratification**: Enforces identical positive class placement ratios across all validation folds.
- **Reporting Standard**: Mean and 95% Confidence Intervals calculated via student's $t$-distribution:
  $$	ext{CI}_{95\%} = ar{x} \pm t_{0.025, df=14} 	imes rac{s}{\sqrt{15}}$$

### 2.2 Rolling-Origin Forward-Chaining Backtesting (Longitudinal Models)
- **Protocol**: 4-window temporal rolling-origin split across sequence records (`DS-BENCH-02`).
- **Temporal Horizon**: 16-week observation window forecasting +6 month and +12 month placement readiness tiers.
- **Zero Lookahead Rule**: No model may observe features from semester $T+1$ when forecasting semester $T+1$.

---

## 3. Generalization & Robustness Audits

To verify that model performance does not collapse outside standard cohort distributions, three robustness stress-tests are executed:
1. **Gaussian Noise Perturbation**: Adding zero-mean Gaussian noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$ ($\sigma \in [0.01, 0.10]$) to input SPV features to verify prediction stability.
2. **Missing Modality Drop-Test**: Randomly masking entire feature groups (e.g., dropping all ATS features or all mock interview features) to verify graceful degradation via the observation mask $\mathbf{m}$.
3. **Subgroup Performance Parity**: Auditing Macro-F1 deltas across engineering departments (CSE vs ECE vs MECH) to confirm cross-domain generalizability.
