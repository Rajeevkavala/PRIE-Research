# Feature Selection Methodology: Information Theoretic Pruning, RFECV & Dimensionality Optimization

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Feature_Selection.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Feature Selection Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Scientific Principles & Traceability Anchor

In educational machine learning, unconstrained feature proliferation introduces multicollinearity, inflates model variance, and compromises explainability. In PRIE, feature selection is governed by three foundational rules:

1. **Phase 04 Invariance Rule**: The candidate feature space must remain anchored to the evidence baseline established in `04_Research_Evidence/Feature_Traceability.md`.
2. **No Arbitrary Dropping**: No feature may be discarded merely because it is challenging to measure or missing in convenient public datasets.
3. **In-Fold Execution**: All selection algorithms (RFECV, Mutual Information) execute strictly *inside* cross-validation training folds to prevent selection leakage.

---

## 2. Multi-Stage Feature Selection Pipeline

```
[Candidate Multimodal Feature Pool (36 Raw & Derived Signals)]
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1: VARIANCE & LOW-INFORMATION FILTERING               │
│ • Drop zero-variance and quasi-constant features (Var < 1e-4)│
│ • Prune uninformative metadata (Timestamps, IDs)            │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 2: MULTICOLLINEARITY & REDUNDANCY PRUNING             │
│ • Pairwise Spearman Rank Correlation Matrix (|r_s| > 0.85)  │
│ • Variance Inflation Factor (VIF < 5.0)                     │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 3: NON-LINEAR RELEVANCE RANKING                       │
│ • Mutual Information (MI) against placement target y        │
│ • Top ranking features retained                             │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 4: RECURSIVE FEATURE ELIMINATION WITH CV (RFECV)      │
│ • Estimator: XGBoost Classifier with 5-Fold Stratified CV   │
│ • Metric: Area Under Precision-Recall Curve (PR-AUC)        │
│ • Optimization Goal: Validate Invariant 22-Dim SPV Subspace │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Mathematical Selection Mechanics

### 3.1 Mutual Information Scoring
Mutual Information evaluates non-linear statistical dependencies between continuous candidate feature $X$ and binary placement outcome $Y$:
$$I(X; Y) = \sum_{y \in \{0, 1\}} \int_{\mathcal{X}} p(x, y) \log rac{p(x, y)}{p(x) p(y)} \, dx$$
Features with $I(X; Y) < 0.015$ are flagged as uninformative noise candidates.

### 3.2 Multicollinearity & Variance Inflation Factor (VIF)
For candidate continuous features, severe multicollinearity distorts TreeSHAP attribution fidelity. VIF is computed by regressing feature $x_i$ on all remaining features:
$$	ext{VIF}_i = rac{1}{1 - R_i^2}$$
Any auxiliary engineered feature exhibiting $	ext{VIF}_i > 5.0$ is either regularized or merged into a composite interaction term.

### 3.3 RFECV with XGBoost Estimator
1. An XGBoost model is fitted across 5 Stratified folds on the training split.
2. Feature importance weights $w_i = \sum 	ext{Gain}(f_i)$ are extracted.
3. The lowest-ranked feature is recursively eliminated.
4. Validation PR-AUC is recorded at each dimension $d \in [10, 36]$.
5. The optimization curve validates that the **invariant 22-dimensional feature subspace captures $\ge 98.5\%$ of maximum achievable PR-AUC**, confirming the optimality of the `DD-001` SPV design.
