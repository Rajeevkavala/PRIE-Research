# Counterfactual Methodology: Diverse Prescriptive Recourse, Constraint Optimization & Effort Minimization

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Counterfactual_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Counterfactual Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Bridging the Descriptive-to-Prescriptive Chasm (`RG3`)

While SHAP informs an unplaced student *why* they received a low score (descriptive attribution), it leaves the student paralyzed regarding *what specific minimal actions* will reverse the outcome.

**Counterfactual Recourse** provides the student with an optimized alternative profile $\mathbf{c}^* \in [0.0, 1.0]^{22}$ such that:
$$f(\mathbf{c}^*) \ge 	ext{Threshold}_{	ext{Ready}}$$
while minimizing the cognitive and physical effort required for the student to transition from their current state $\mathbf{x}_{	ext{spv}}$ to $\mathbf{c}^*$.

---

## 2. DiCE Loss Formulation & Optimization Mechanics

PRIE implements Diverse Counterfactual Explanations (DiCE) utilizing gradient-based optimization over differentiable tree surrogates (`DD-003`, `M07`):

### 2.1 Multi-Objective Loss Function
$$\mathcal{L}_{	ext{DiCE}} = rg\min_{\mathbf{c}_1, \dots, \mathbf{c}_k} rac{1}{k} \sum_{j=1}^k \Big[ 	ext{dist}(\mathbf{x}, \mathbf{c}_j) + \lambda_1 ig( f(\mathbf{c}_j) - y^* ig)^2 \Big] - \lambda_2 	ext{dpp\_diversity}(\mathbf{c}_1, \dots, \mathbf{c}_k)$$

### 2.2 Proximity & Effort Distance Metric ($L_1$)
To ensure recommendations focus on feasible, sparse student actions, distance is measured using Median Absolute Deviation (MAD) weighted $L_1$ norm:
$$	ext{dist}(\mathbf{x}, \mathbf{c}) = \sum_{i \in 	ext{mutable}} rac{|x_i - c_i|}{	ext{MAD}_i}$$
where $	ext{MAD}_i = 	ext{median}ig( |x_i - 	ext{median}(x_i)| ig)$ normalizes features by their natural cohort dispersion.

### 2.3 Diversity Enforcement via Determinantal Point Processes (DPP)
To offer students multiple distinct career pathways (e.g., Pathway A: Focus on LeetCode DSA; Pathway B: Focus on Open-Source Projects):
$$	ext{dpp\_diversity}(\mathbf{c}_1, \dots, \mathbf{c}_k) = \det(\mathbf{K})$$
where kernel matrix $\mathbf{K}_{i, j} = rac{1}{1 + 	ext{dist}(\mathbf{c}_i, \mathbf{c}_j)}$.

---

## 3. Strict Feature Mutability & Directional Constraints

To guarantee real-world feasibility and prevent nonsensical recommendations:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      COUNTERFACTUAL MUTABILITY CONSTRAINTS                      │
├──────┬────────────────────────┬─────────────┬───────────────────────────────────┤
│ ID   │ Feature Name           │ Mutability  │ Directional Bound                 │
├──────┼────────────────────────┼─────────────┼───────────────────────────────────┤
│ F01  │ cgpa                   │ IMMUTABLE   │ Strictly locked (c_i = x_i)       │
│ F17  │ branch_encoded         │ IMMUTABLE   │ Strictly locked (c_i = x_i)       │
│ F18  │ target_role_encoded    │ IMMUTABLE   │ Strictly locked (c_i = x_i)       │
│ F02  │ dsa_score              │ MUTABLE     │ Monotonically non-decreasing (>=) │
│ F03  │ dbms_score             │ MUTABLE     │ Monotonically non-decreasing (>=) │
│ F06  │ programming_score      │ MUTABLE     │ Monotonically non-decreasing (>=) │
│ F09  │ project_count          │ MUTABLE     │ Monotonically non-decreasing (>=) │
│ F11  │ has_internship         │ MUTABLE     │ Monotonically non-decreasing (>=) │
│ F13  │ resume_ats_score       │ MUTABLE     │ Bidirectional within [0, 1]       │
│ F14  │ cosine_similarity      │ MUTABLE     │ Monotonically non-decreasing (>=) │
│ F16  │ consistency_score      │ MUTABLE     │ Bidirectional within [0, 1]       │
│ F20  │ behavior_score         │ MUTABLE     │ Monotonically non-decreasing (>=) │
└──────┴────────────────────────┴─────────────┴───────────────────────────────────┘
```

**Epistemological Guarantee**: Under no circumstances will DiCE advise a student to alter their gender, engineering department, or historical semester exam scores. All generated recourse vectors are strictly bounded within feasible student improvement thresholds ($\Delta f_i \le 0.35$ per 30-day intervention window).
