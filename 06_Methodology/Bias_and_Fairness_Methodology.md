# Bias and Fairness Methodology: Demographic Parity, Disparate Impact & Mitigations

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Bias_and_Fairness_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Bias and Fairness Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Sources of Algorithmic Bias in Campus Recruitment

Historical corporate hiring data reflects systemic societal and institutional inequities (`Paper01`, `Paper06`):
- **Historical Gender Hiring Disparities**: Unequal female representation in select core engineering industries.
- **Departmental Discrimination**: Biased recruiter preferences for Computer Science over Electronics or Mechanical students, even when candidates possess identical software coding skills.
- **Institutional Prestige Bias**: Over-indexing on elite institutional tier rather than verified individual technical competence.

---

## 2. Mathematical Fairness Evaluation Metrics

To evaluate model equity objectively, predictions are audited across sensitive protected attributes $A \in \{0, 1\}$ (e.g., gender, departmental origin):

### 2.1 Disparate Impact Ratio ($\text{DIR}$)
The ratio of positive selection rates between unprivileged and privileged demographic groups:
$$\text{DIR} = \frac{P(\hat{Y} = 1 \mid A = 0)}{P(\hat{Y} = 1 \mid A = 1)}$$
**Fairness Standard**: The model satisfies the EEOC Four-Fifths Rule if:
$$\text{DIR} \ge 0.80$$

### 2.2 Equalized Odds & Equal Opportunity
The true positive rate (TPR) and false positive rate (FPR) must be equal across protected groups:
$$P(\hat{Y} = 1 \mid A = 0, Y = 1) = P(\hat{Y} = 1 \mid A = 1, Y = 1) \quad (\text{Equal Opportunity})$$
$$P(\hat{Y} = 1 \mid A = 0, Y = 0) = P(\hat{Y} = 1 \mid A = 1, Y = 0)$$

---

## 3. Algorithmic Bias Mitigation Techniques

1. **Demographic Feature Exclusion**: Protected attributes (gender, age, race, socioeconomic status) are strictly excluded from the SPV feature tensor.
2. **Adversarial Debiasing**: A gradient-reversal adversary is evaluated during training to penalize representations from which protected attributes can be predicted.
3. **Threshold Calibration**: Department-specific classification thresholds are tuned to ensure equalized positive recall across engineering specializations.
