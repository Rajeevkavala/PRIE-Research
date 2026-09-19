# Paper02 — Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction

## Paper metadata

| Field | Value |
|---|---|
| Title | Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction |
| Authors | W. Hidayatulloh, F. Mahardika, D. I. Junaedi |
| Year | 2026 |
| Journal | *Journal of Information System Exploration and Research*, 4(1), 31–40 |
| Publisher | SHM Publisher |
| DOI | [10.52465/joiser.v4i1.62419](https://doi.org/10.52465/joiser.v4i1.62419) |
| Citation | Hidayatulloh, W., Mahardika, F., & Junaedi, D. I. (2026). Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction. *Journal of Information System Exploration and Research, 4*(1), 31–40. |
| Domain | Educational data mining; student-performance prediction; explainable AI; learning analytics |

## Context, objectives, and research questions

### Problem and motivation

High-accuracy academic-risk and success models are opaque. Educators cannot see why a learner has been labelled at risk, undermining trust, intervention design, and adoption of predictive systems.

### Objectives extracted or inferred

1. Train ensemble classifiers on historical academic data.
2. Predict student academic performance.
3. Produce global and individual-level explanations with SHAP and LIME.
4. Make explanatory evidence actionable for pedagogical intervention.

### Research questions

Not explicitly reported. Inferred: Which ensemble model performs best? Which academic variables matter globally and per learner? Can post-hoc XAI make predictions suitable for education decision support?

## Methodology

```text
Historical academic records (sociodemographic + performance data)
 → train Random Forest and XGBoost
 → obtain performance prediction
 → SHAP: global and local marginal feature contributions
 → LIME: local model-agnostic explanation
 → dashboard/intervention interpretation
```

| Component | Extraction |
|---|---|
| ML models | Random Forest; XGBoost |
| XAI | SHAP for global and local importance; LIME for local, model-agnostic explanations |
| Important reported features | Previous grades, number of failed courses, absences |
| NLP, DL, optimization | Not reported |
| Preprocessing / feature selection / hyperparameter tuning | Not reported in the source plan |
| Train/test split, CV, seeds, class balance | Not reported |

## Dataset and setup

| Dataset field | Extraction |
|---|---|
| Source | Historical student academic records |
| Data categories | Sociodemographic and performance metrics |
| Size, institution, time period, labels | Not reported |
| Missing data handling | Not reported |
| Hardware/software/frameworks/libraries | Not reported |

## Evaluation and results

| Result / metric | Value / finding |
|---|---|
| Accuracy | Random Forest: **90.77%** |
| SHAP global/local findings | Previous grades, failed-course count, and absences were critical factors |
| Other metrics | Precision, recall, F1, AUC, calibration, fairness, statistical tests: not reported |
| Figures/tables | SHAP visualizations are described as suitable; actual figures/tables are not reproduced in the plan |

## Explainable AI knowledge

- SHAP is grounded in cooperative game theory and attributes a feature’s marginal contribution to a prediction.
- Global SHAP ranks factors across a cohort; local SHAP explains why a particular learner’s score differs from a baseline.
- LIME can supply an alternative local, model-agnostic explanation.
- For ScholarCamp, waterfall plots support individual readiness conversations; summary plots support cohort-level placement-cell strategy.
- XAI does not prove causality or fairness. Explanations need stability, data-quality, subgroup, and calibration checks.

## Strengths, limitations, gaps, and future work

### Strengths

- Couples strong ensemble baselines with both global and local explanations.
- Produces actionable factors rather than only a risk label.
- Directly addresses trust and algorithmic aversion in educational decision support.

### Explicit limitation

The scope is traditional academic grades and attendance, omitting technical skills, employability, and soft skills.

### Implied limitations

- A post-hoc explanation can be plausible without being causal.
- No reported temporal validation, drift testing, fairness analysis, or intervention-effect evaluation.
- Missing experimental specifics limit replication.

### Future work reported

Incorporate temporal deep-learning models such as LSTM to model student behavior through the degree lifecycle.

### Gap addressed / remaining gap

It addresses opaque academic prediction. It still does not model a holistic, multimodal placement trajectory or close the loop from explanation to RAG-grounded individualized action.

## ScholarCamp implementation ideas

- Explain PRIE as a readiness probability/score with both a global factor view and a student-specific waterfall view.
- Separate immutable/contextual variables from actionable variables; do not tell students to change demographic or historical attributes.
- Link each negative actionable factor to evidence-grounded learning, resume, or interview tasks.
- Log explanation version, model version, prediction date, and intervention outcome to test whether explanations help.

## Important citations and keywords

- [Original journal record](https://shmpublisher.com/index.php/joiser/article/view/624)
- [Predictive modeling and explainability of student employability using RF and SHAP](http://www.ijikm.org/Volume21/IJIKMv21Art02Olipas12863.pdf)
- [From predictive analytics to XAI in higher education](https://www.researchgate.net/publication/405196548_From_Predictive_Analytics_to_Explainable_AI_in_Higher_Education_A_Bibliometric_Mapping)

Keywords: explainable AI; SHAP; LIME; educational data mining; academic performance; Random Forest; XGBoost; local explanation; global feature importance; learning analytics dashboard; transparency; trust; algorithmic aversion; student risk prediction; intervention; calibration; fairness; longitudinal learning; LSTM; decision support.

## IEEE reviewer notes

| Criterion | Score / 10 | Note |
|---|---:|---|
| Novelty | 6 | Combining ensemble prediction with local/global explanations is useful, though established. |
| Technical depth | 6 | Appropriate modelling/XAI combination; original implementation needs direct verification. |
| Research quality | 6 | Addresses a meaningful adoption barrier. |
| Experimental quality | 5 | 90.77% accuracy is encouraging; broader metrics/validation are unavailable. |
| Writing quality | 6 | Secondary profile is clear; direct review required. |
| Reproducibility | 3 | Dataset and protocol details absent from the plan. |
| Conference readiness | 6 | Stronger with calibration, causal/intervention study, fairness, and longitudinal validation. |

## How can this paper improve ScholarCamp?

Use SHAP/LIME as PRIE’s explanation layer, but preserve the paper’s insight while extending the feature space beyond grades: ATS semantic fit, verified skill evidence, quiz mastery, interview-response quality, and engagement trends. Pair every explanation with an achievable intervention and verify outcome improvement rather than treating explainability as a UI feature alone.
