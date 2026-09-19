# Model Calibration Methodology: Probability Reliability, Isotonic Scaling & Expected Calibration Error

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Model_Calibration.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Model Calibration Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Why Probability Calibration is Essential in Career Placement AI

In educational decision support, an uncalibrated classifier that outputs raw sigmoid outputs is dangerous:
- An uncalibrated score of $0.85$ might only reflect a $60\%$ empirical probability of placement, creating dangerous false complacency.
- Conversely, a score of $0.35$ might reflect a $50\%$ empirical chance, inducing severe student anxiety.

**Formal Calibration Definition**: A predictor is perfectly calibrated if:
$$P\Big( Y = 1 \;\Big|\; \hat{P}_{	ext{placement}} = p \Big) = p, \quad orall p \in [0, 1]$$
That is, of all students assigned a placement probability of $0.70$, exactly $70\%$ actually secure placement.

---

## 2. Calibration Procedures

PRIE evaluates two distinct post-hoc calibration techniques fitted on the inner validation split:

### 2.1 Isotonic Regression (Non-Parametric)
Fits a piece-wise constant non-decreasing monotonic step function $m$:
$$\min_m \sum_{i=1}^{N_{	ext{val}}} \Big( y_i - m(\hat{f}_i) \Big)^2, \quad 	ext{subject to } m(\hat{f}_i) \ge m(\hat{f}_j) 	ext{ whenever } \hat{f}_i \ge \hat{f}_j$$
Optimized via the **Pool Adjacent Violators Algorithm (PAVA)**.

### 2.2 Platt Scaling (Parametric Logistic)
Fits a scalar sigmoid transform over raw model logit margins $z_i$:
$$\hat{P}_{	ext{calibrated}}(\mathbf{x}_i) = rac{1}{1 + \exp( A z_i + B )}$$
where scalar parameters $A$ and $B$ are optimized via maximum likelihood on validation predictions.

---

## 3. Calibration Evaluation Metrics

### 3.1 Brier Score
The mean squared error of probability forecasts:
$$	ext{BS} = rac{1}{N} \sum_{i=1}^N \Big( \hat{p}_i - y_i \Big)^2 \in [0, 1]$$
Lower scores indicate superior probability calibration and sharpness.

### 3.2 Expected Calibration Error (ECE)
Predictions are grouped into $M = 10$ equally spaced confidence bins $B_m \subset ( rac{m-1}{M}, rac{m}{M} ]$:
$$	ext{ECE} = \sum_{m=1}^M rac{|B_m|}{N} \Big| 	ext{acc}(B_m) - 	ext{conf}(B_m) \Big|$$
where:
- $	ext{acc}(B_m) = rac{1}{|B_m|} \sum_{i \in B_m} y_i$ is empirical positive accuracy in bin $m$.
- $	ext{conf}(B_m) = rac{1}{|B_m|} \sum_{i \in B_m} \hat{p}_i$ is average model confidence in bin $m$.
