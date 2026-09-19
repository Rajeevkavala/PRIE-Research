# Evaluation Methodology: Comprehensive Metric Suites, Operational Justifications & Decision Criteria

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Evaluation_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Evaluation Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Multi-Dimensional Evaluation Philosophy

In strict adherence to scientific rigor, PRIE does not indiscriminately report standard accuracy across all subsystems. Instead, each subsystem is evaluated using domain-tailored, psychometrically validated, and mathematically justified metrics:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          PRIE METRIC EVALUATION SUITE                           │
├────────────────────┬────────────────────────────────────────────────────────────┤
│ Evaluation Domain  │ Selected Primary & Secondary Metrics                       │
├────────────────────┼────────────────────────────────────────────────────────────┤
│ Tabular Prediction │ PR-AUC, ROC-AUC, Macro-F1, Matthews Correlation (MCC), ECE │
├────────────────────┼────────────────────────────────────────────────────────────┤
│ Sequence Forecast  │ Quantile Loss (q0.1, q0.5, q0.9), Normalized RMSE, MAE     │
├────────────────────┼────────────────────────────────────────────────────────────┤
│ ATS Parsing        │ Boundary-F1, Entity Precision/Recall, Cosine Similarity    │
├────────────────────┼────────────────────────────────────────────────────────────┤
│ Mock Interview     │ Voice Turnaround Latency (ms), Pearson r, ICC(2, k)        │
├────────────────────┼────────────────────────────────────────────────────────────┤
│ Explainable AI     │ Proximity (L1 MAD), Sparsity, Usability Likert (1–5)       │
├────────────────────┼────────────────────────────────────────────────────────────┤
│ Recommendation     │ Prerequisite Violation Rate (PVR), Milestone Velocity (MCV)│
├────────────────────┼────────────────────────────────────────────────────────────┤
│ Question Gen (AQG) │ Item Discrimination (DI), Distractor Plausibility (DPI)    │
├────────────────────┼────────────────────────────────────────────────────────────┤
│ Curriculum RAG     │ RAG Triad: Context Relevance, Groundedness, Answer Relev.  │
└────────────────────┴────────────────────────────────────────────────────────────┘
```

---

## 2. Mathematical Metric Definitions & Justifications

### 2.1 Classification: Area Under Precision-Recall Curve (PR-AUC)
Due to class imbalance in corporate selection ($1:4$ or $1:8$ minority ratios), standard ROC-AUC presents an overly optimistic view by over-crediting true negatives. PR-AUC evaluates the true precision-recall tradeoff:
$$\text{PR-AUC} = \int_0^1 P(R) \, dR \approx \sum_{k=1}^K P(k) \Delta R(k)$$

### 2.2 Classification: Matthews Correlation Coefficient (MCC)
The single most informative metric for imbalanced binary classification, incorporating all four confusion matrix quadrants:
$$\text{MCC} = \frac{\text{TP} \times \text{TN} - \text{FP} \times \text{FN}}{\sqrt{(\text{TP} + \text{FP})(\text{TP} + \text{FN})(\text{TN} + \text{FP})(\text{TN} + \text{FN})}} \in [-1.0, +1.0]$$

### 2.3 Forecasting: Pinball Quantile Loss ($\text{QL}_q$)
Evaluates asymmetric multi-horizon trajectory curves ($q \in \{0.1, 0.5, 0.9\}$):
$$\text{QL}_q(y, \hat{y}) = \begin{cases} q (y - \hat{y}) & \text{if } y \ge \hat{y} \\ (1 - q)(\hat{y} - y) & \text{if } y < \hat{y} \end{cases}$$

### 2.4 Document Intelligence: Entity Boundary-F1
Evaluates token span boundary identification for technical skill phrases:
$$\text{Boundary-F1} = 2 \times \frac{\text{Precision}_{\text{span}} \times \text{Recall}_{\text{span}}}{\text{Precision}_{\text{span}} + \text{Recall}_{\text{span}}}$$
A predicted entity is marked correct if and only if both the text span boundaries and entity category match the gold standard annotation.

### 2.5 Mock Interview: Recruiter Panel Correlation ($r$) & Intraclass Correlation ($\text{ICC}$)
- **Pearson Correlation ($r$)**: Measures linear alignment between automated scores $X$ and median human recruiter panel ratings $Y$:
  $$r = \frac{\sum_{i=1}^N (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^N (X_i - \bar{X})^2 \sum_{i=1}^N (Y_i - \bar{Y})^2}}$$
- **Two-Way Mixed Single-Score ICC ($\text{ICC}(2, 1)$)**: Evaluates inter-rater agreement among the three human recruiter evaluators to confirm ground-truth reliability:
  $$\text{ICC}(2, 1) = \frac{\text{MS}_R - \text{MS}_E}{\text{MS}_R + (k - 1)\text{MS}_E + \frac{k}{n}(\text{MS}_C - \text{MS}_E)}$$
