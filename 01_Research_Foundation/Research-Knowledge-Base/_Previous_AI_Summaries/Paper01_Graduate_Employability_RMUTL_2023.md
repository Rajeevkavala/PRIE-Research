# Paper01 — Graduate Employability Prediction Using Multi-Model Data Mining Frameworks

## Evidence status

This record is extracted from a secondary plan’s profile of the paper. The plan calls the authors “RMUTL Research Group”; exact author names, DOI, feature schema, split protocol, tuning procedure, and implementation stack were not provided.

## Paper metadata

| Field | Extracted value |
|---|---|
| Title | Graduate Employability Prediction Using Multi-Model Data Mining Frameworks |
| Authors | RMUTL Research Group (as reported) |
| Year | 2023 |
| Venue | *SciTechAsia* |
| Publisher | TCI |
| DOI | Not reported; source plan maps this profile to [ThaiJo paper](https://ph02.tci-thaijo.org/index.php/SciTechAsia/article/view/259949). |
| Citation supplied by plan | RMUTL Research Group. (2023). *Graduate employability prediction using multi-model data mining frameworks*. SciTechAsia. |
| Research domain | Educational data mining; graduate employability prediction; supervised classification |
| Core keywords | employability, employment prediction, educational data mining, feature selection, Random Forest, XGBoost |

## Research context, problem, and objectives

### Problem statement

Prior graduate-employability studies were reported to use limited datasets and narrow model evaluations without systematic feature assessment. This limits robustness and generalizability of placement predictions.

### Motivation and real-world impact

- Universities require an evidence-based way to identify employment risk and salient institutional predictors.
- Binary employment-outcome prediction can support early intervention, placement-cell planning, and allocation of student-support resources.
- Unselected feature sets and insufficient model comparison may overfit, producing unreliable decisions.

### Objectives extracted or inferred

1. Predict binary graduate employment outcomes from anonymized university records.
2. Compare multiple conventional and ensemble classifiers.
3. Apply filter-based feature selection to identify useful predictors and reduce overfitting.
4. Establish high-performing baselines for structured educational data.

### Research questions

No explicit research questions were reported. Conservative inferred questions:

1. Which candidate classifier best predicts graduate employment outcomes on this institutional dataset?
2. Does filter-based feature selection improve or stabilize employability prediction?
3. Which institutional variables are informative for the target outcome?

## Methodology

### Workflow

```text
Anonymized graduate records
  → filter-based feature assessment (Chi-Square; Information Gain)
  → train multiple classifiers
  → compare binary employment prediction performance
  → report accuracy and class-separation AUC
```

### Algorithms and techniques

| Category | Reported techniques | Role |
|---|---|---|
| Classifiers | Decision Tree, Random Forest, XGBoost / Gradient Boosted Trees, Naïve Bayes, K-Nearest Neighbors | Predict binary employment outcome |
| Feature selection | Chi-Square, Information Gain | Filter/rank predictive variables before modelling |
| ML type | Traditional supervised ML; ensemble tree models | Tabular classification |
| NLP / DL / XAI / optimization | Not reported / not used in the reported profile | No transformer, deep learning, SHAP/LIME, or optimizer is specified |

### Feature engineering and preprocessing

- Example institution-specific predictors identified in the plan: department, campus, and GPA.
- The source plan confirms anonymization and filter-based feature selection.
- Missing-value handling, encoding, scaling, outlier treatment, balancing, feature-count threshold, and feature-ranking results: **not reported**.
- Hyperparameter search strategy, parameter values, random seed, cross-validation folds, and final train/test split: **not reported**. The plan notes that robust cross-validation is important in this research area, but does not establish that the paper used it.

## Dataset

| Attribute | Extracted value |
|---|---|
| Dataset/source | Anonymized university graduate records |
| Collection period | 2023 academic year |
| Size | 4,352 records |
| Data type | Structured/tabular institutional data |
| Target label | Binary employment outcome |
| Reported features | Department, campus, GPA are examples; complete schema not reported |
| Missing values | Not reported |
| Train/test split | Not reported |

## Experimental setup and evaluation

### Setup reproducibility record

Hardware, operating system, programming language, library/framework versions, compute budget, test protocol, class distribution, tuning, and confidence intervals are not reported in the source plan.

### Metrics explicitly reported

| Metric | Best reported result | Interpretation |
|---|---:|---|
| Accuracy | Random Forest: **83.72%** | Overall correct binary predictions |
| AUC | Gradient Boosted Trees / XGBoost: **0.813** | Class-separation/discrimination performance |

Precision, recall, F1-score, specificity, calibration, ROC curve, confusion matrix, MAE/RMSE, MCC, and statistical significance: **not reported**.

## Results, strengths, and limitations

### Key numerical and comparative results

- Random Forest was the highest-accuracy model at **83.72%**.
- Gradient Boosted Trees / XGBoost achieved the highest reported AUC, **0.813**.
- The profile positions Random Forest and XGBoost as useful baselines for structured educational classification.
- No tables, figures, classifier-by-classifier score matrix, or feature-importance values are reproduced in the plan.

### Strengths

- Uses a comparatively substantial institutional dataset (4,352 records).
- Compares diverse inductive biases, including tree, boosting, probabilistic, and instance-based approaches.
- Adds systematic filter-based feature selection.
- Reports two complementary metrics: accuracy and AUC.
- Produces deployable baselines for a ScholarCamp PRIE structured-data predictor.

### Limitations explicitly reported

- Data come from a single institution, limiting cross-domain generalization.
- Models are treated as black boxes, with no XAI explanation for users.

### Implied limitations

- A binary outcome obscures degrees and trajectories of readiness.
- Historical, primarily institutional data may omit resume quality, interview behavior, technical-skill evidence, and dynamic engagement.
- Reproducibility cannot be assessed from the available profile because implementation and validation details are missing.
- Accuracy alone may conceal class imbalance; per-class error behavior is unavailable.

## Novelty, gaps, and future work

### Novel contribution reported

The profile credits the work with establishing Random Forest and XGBoost as optimal baseline algorithms for tabular educational employability classification and demonstrating systematic feature selection.

### Gap addressed

It addresses limited datasets, restricted model comparison, and lack of systematic feature assessment in employability prediction.

### Remaining gap

It does not create an interpretable, longitudinal, multimodal, intervention-capable placement ecosystem; does not demonstrate cross-institution transfer; and does not connect predictions to adaptive learning actions.

### Future work reported

- Add real-time behavioral data.
- Use cross-institutional federated learning for robustness.

## Relevance to ScholarCamp and reusable ideas

| ScholarCamp component | Transferable knowledge |
|---|---|
| PRIE / placement readiness | Use Random Forest and XGBoost as transparent baseline comparators before more complex models; predict readiness from structured historic and live features. |
| Learning analytics | Maintain an auditable feature dictionary including GPA, department, campus, quiz performance, resume evidence, and interview measures. |
| XAI | Close the paper’s black-box limitation with SHAP/LIME explanations and calibrated probability displays. |
| Recommendation / personalized learning | Convert top negative predictors into intervention targets; validate that interventions improve later readiness. |
| ATS and mock interview | Extend the feature space with semantic resume match and audio/response metrics, but measure ablation gain. |

### Suggested ScholarCamp baseline protocol

1. Compare Logistic Regression, Decision Tree, KNN, Naïve Bayes, Random Forest, and XGBoost on the same temporally separated cohort.
2. Compare academic-only features against academic + ATS + quiz + interview feature sets.
3. Report ROC-AUC, PR-AUC, F1, recall, precision, MCC, Brier score, calibration, subgroup performance, and confidence intervals.
4. Use SHAP only after validating stability, fairness, and predictive calibration.

## Important citations to follow

- [Data Mining Model Approach for Employment Prediction for University Graduates](https://ph02.tci-thaijo.org/index.php/SciTechAsia/article/view/259949)
- [Predicting Student Career Readiness Using ML/DL with XAI](https://impactfactor.org/PDF/IJDDT/16/IJDDT,Vol16,Issue26s,Article20.pdf)
- [Employability prediction: a survey of current approaches](https://pmc.ncbi.nlm.nih.gov/articles/PMC8208070/)

## Technical keywords

graduate employability; placement prediction; employment outcome; educational data mining; supervised classification; tabular learning; Random Forest; XGBoost; gradient boosting; Decision Tree; Naïve Bayes; KNN; filter feature selection; Chi-Square; Information Gain; AUC; accuracy; cross-validation; generalization; federated learning; readiness score.

## IEEE-style reviewer notes

| Criterion | Score / 10 | Assessment |
|---|---:|---|
| Novelty | 5 | Model benchmarking and feature filtering are useful but familiar. |
| Technical depth | 5 | Breadth is good; details available in the plan are limited. |
| Research quality | 6 | Practical dataset and comparison; external validity is constrained. |
| Experimental quality | 5 | Accuracy/AUC are useful, but validation and per-class metrics are unavailable. |
| Writing quality | 6 | The profile is clear; original-paper quality needs direct inspection. |
| Reproducibility | 3 | Split, preprocessing, tuning, hardware, and code are absent from the plan. |
| Conference readiness | 5 | Suitable as a baseline study; needs XAI, multi-site validation, and fuller reporting for a strong venue. |

## How can this paper improve ScholarCamp?

Implement its multi-model, feature-selection-first baseline as PRIE v0. Build it as a reproducible benchmark rather than the final product: use a versioned feature schema, time-aware validation, and a holdout institution if available. Then add live quiz, resume, and interview features, quantify their ablation value, and expose per-student SHAP explanations with action-linked recommendations.
