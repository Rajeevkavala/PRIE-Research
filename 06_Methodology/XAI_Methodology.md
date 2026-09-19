# XAI Methodology: TreeSHAP Feature Attribution, Consistency Guarantees & Causal Boundaries

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/XAI_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Explainable AI Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Epistemological Firewall: Statistical Attribution vs Causal Claims

> [!CAUTION]
> **CRITICAL SCIENTIFIC PRINCIPLE: SHAP VALUES DO NOT PROVE CAUSALITY**  
> In strict adherence to scientific rigor:  
> **TreeSHAP provides descriptive statistical feature attribution within a predictive model. It quantifies how much feature $f_i$ shifted the model output relative to the base value. It DOES NOT prove that manually intervening on $f_i$ will causally produce a real-world placement offer.**  
> Confusing predictive feature importance with causal intervention is a severe epistemological fallacy. Real-world actionable guidance is handled strictly through constrained counterfactual search (`Counterfactual_Methodology.md`).

---

## 2. TreeSHAP Mathematical Mechanics

PRIE deploys the polynomial-time exact TreeSHAP algorithm for all tree ensemble explanations (`DD-003`, `M07`).

### 2.1 Classical Shapley Value Formulation
The attribution $\phi_i$ allocated to feature $i$ across all possible feature subsets $\mathcal{S} \subseteq \mathcal{F} \setminus \{i\}$ is:
$$\phi_i(f, \mathbf{x}) = \sum_{\mathcal{S} \subseteq \mathcal{F} \setminus \{i\}} rac{|\mathcal{S}|! (|\mathcal{F}| - |\mathcal{S}| - 1)!}{|\mathcal{F}|!} \Big( f_{\mathbf{x}}(\mathcal{S} \cup \{i\}) - f_{\mathbf{x}}(\mathcal{S}) \Big)$$
where $f_{\mathbf{x}}(\mathcal{S}) = \mathbb{E}[f(\mathbf{x}) | \mathbf{x}_{\mathcal{S}}]$ is the conditional expectation of model output given observed subset $\mathcal{S}$.

### 2.2 Invariant Efficiency Property (Local Accuracy)
The sum of all 22 feature attributions plus the expected base score $\phi_0$ equals the exact uncalibrated prediction margin:
$$f(\mathbf{x}_{	ext{spv}}) = \phi_0 + \sum_{i=1}^{22} \phi_i(f, \mathbf{x}_{	ext{spv}})$$
where $\phi_0 = \mathbb{E}[f(\mathbf{x})]$ is the average prediction over the training population.

---

## 3. Explanatory Presentations & Visual Analytics

The XAI engine compiles explanations into three standardized visual instruments:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           XAI PRESENTATION INSTRUMENTS                          │
├───────────────────┬─────────────────────────────────────────────────────────────┤
│ Visual Form       │ Educational Interpretation                                  │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Waterfall Plot    │ Local decomposition for an individual student, showing      │
│                   │ exact positive drivers (green) and negative drags (red)     │
│                   │ pushing probability away from base rate phi_0.             │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Summary Beeswarm  │ Global cohort overview showing feature importance ranking   │
│                   │ and directionality across the entire student population.    │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Force Plot        │ Compact inline visualization embedded in Student Hub        │
│                   │ showing opposing feature forces balancing readiness.        │
└───────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 4. Subgroup Explanation Consistency Audits

To ensure explanations are reliable across diverse student cohorts:
1. **Monotonicity Check**: Higher scores in positive academic features (`dsa_score`, `programming_score`) must yield non-negative Shapley values ($\phi_i \ge 0$).
2. **Attribution Stability**: Adding small Gaussian noise ($\sigma = 0.01$) to non-critical inputs must not cause chaotic rank-order flips in top-3 explanatory features.
