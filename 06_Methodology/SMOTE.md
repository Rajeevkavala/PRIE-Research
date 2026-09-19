# SMOTE Methodology: In-Fold Synthetic Minority Oversampling & Class Imbalance Governance

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/SMOTE.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Class Imbalance Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. The Class Imbalance Problem in Campus Placement Data

In campus recruitment cohorts (`DS-BENCH-01`, `DS-REAL-01`), class imbalance naturally arises from corporate hiring market dynamics:
- **Mass Recruiter Selection Ratio**: 65%–75% placed ($1:2$ to $1:3$ minority ratio).
- **Super-Dream / Core Technical Hiring**: 10%–15% placed ($1:6$ to $1:9$ extreme minority ratio).

Standard classifiers trained on uncalibrated imbalanced distributions exhibit severe majority-class bias, maximizing nominal accuracy while achieving disastrously low Recall on unplaced or elite candidates.

---

## 2. In-Fold SMOTE Protocol & Test Set Isolation

> [!CRITICAL]
> **LEAKAGE RULE: NEVER APPLY SMOTE BEFORE DATASET SPLITTING**  
> Applying SMOTE to the global dataset before partitioning generates synthetic points along linear interpolations between training and test candidates. This creates near-identical twin data points across splits, resulting in severe data leakage and artificially inflated performance.  
> **In PRIE, SMOTE is applied EXCLUSIVELY to the Training fold INSIDE cross-validation loops.**

```
                     ┌───────────────────────────────┐
                     │ Raw Training Fold Instances   │
                     │ (N_majority = 800, N_min = 200│
                     └───────────────┬───────────────┘
                                     │
                                     ▼
                     ┌───────────────────────────────┐
                     │ In-Fold SMOTE Oversampling    │
                     │ (k=5 Nearest Neighbors)       │
                     └───────────────┬───────────────┘
                                     │
                                     ▼
                     ┌───────────────────────────────┐
                     │ Balanced Training Fold        │
                     │ (N_majority = 800, N_min = 800│
                     └───────────────┬───────────────┘
                                     │
                                     ▼
                             Train Classifier
                                     │
                ┌────────────────────┴────────────────────┐
                ▼                                         ▼
   Evaluate on Frozen Validation Split       Evaluate on Frozen Test Split
   (Original Imbalance Preserved: 100 / 25)   (Original Imbalance Preserved: 100 / 25)
   ZERO SYNTHETIC INSTANCES IN VAL           ZERO SYNTHETIC INSTANCES IN TEST
```

---

## 3. Mathematical SMOTE Formulation

For each minority class sample $\mathbf{x}_i \in \mathcal{S}_{	ext{min}}$:
1. Find its $k$-nearest neighbors in $\mathcal{S}_{	ext{min}}$ using Euclidean distance:
   $$d(\mathbf{x}_i, \mathbf{x}_j) = \|\mathbf{x}_i - \mathbf{x}_j\|_2, \quad \mathbf{x}_j \in \mathcal{S}_{	ext{min}}$$
2. Randomly select one neighbor $\mathbf{x}_{i, 	ext{neighbor}}$ from the $k$-nearest neighbors (default $k = 5$).
3. Generate a synthetic sample $\mathbf{x}_{	ext{new}}$ along the connecting line segment:
   $$\mathbf{x}_{	ext{new}} = \mathbf{x}_i + \lambda \cdot (\mathbf{x}_{i, 	ext{neighbor}} - \mathbf{x}_i), \quad \lambda \sim \mathcal{U}(0, 1)$$
4. For discrete or binary features (`has_internship`: `F11`), values are rounded to the nearest valid integer value.

---

## 4. Alternative Class Balancing Methods & Risks

PRIE benchmarks SMOTE against four alternative imbalance treatments during hyperparameter tuning:

| Method | Mechanics | Advantages | Disadvantages / Risks |
| :--- | :--- | :--- | :--- |
| **Random Oversampling (ROS)** | Duplicate minority samples with replacement | Simple, no interpolation | High risk of overfitting to duplicated points |
| **Random Undersampling (RUS)** | Randomly discard majority class samples | Fast training time | Discards valuable majority training instances |
| **SMOTE (Standard)** | Linear interpolation between $k$-nearest neighbors | Expands decision boundary | Can synthesize noisy points in overlapping regions |
| **Borderline-SMOTE** | Generates synthetic samples only near decision boundaries | Focuses on difficult borderline cases | Vulnerable to mislabeling noise |
| **Cost-Sensitive Learning** | Re-weights cross-entropy loss by inverse class frequencies | Zero synthetic data generation | Sensitive to gradient instability in extreme ratios |

**Experimental Policy**: Cost-sensitive objective weighting (`scale_pos_weight` in XGBoost) serves as the primary non-generative baseline against SMOTE in `EXP-3`.
