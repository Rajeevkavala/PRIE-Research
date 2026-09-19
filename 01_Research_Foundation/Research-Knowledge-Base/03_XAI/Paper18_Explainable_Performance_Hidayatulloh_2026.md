# Paper 18 — Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction

## 1. Bibliographic Information

- **Paper ID**: Paper18
- **Full Title**: Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction
- **Authors**: Wildan Hidayatulloh (1*), Fathoni Mahardika (2), and Dani Indra Junaedi (3)
  - (1,2,3) Study Program of Informatics, Universitas Sebelas April, Sumedang, West Java, Indonesia
- **Corresponding Author**: Wildan Hidayatulloh
- **Year**: 2026 (Received: 08 October 2025, Accepted: 21 January 2026, Available online: 26 January 2026)
- **Venue**: Journal of Information System Exploration and Research (JOISER), Vol. 4, No. 1, pp. 31–40
- **ISSN (Print)**: 2964-1160
- **ISSN (Online)**: 2963-6361
- **DOI**: 10.52465/joiser.v4i1.624
- **PDF filename**: `Paper18_hidayatulloh2026explainable.pdf`
- **PDF path**: `Papers/PDFs/Paper18_hidayatulloh2026explainable.pdf`
- **Page count**: 10 pages (pp. 31–40)

> [!NOTE]
> **Corpus Reconciliation Note**: Metadata matches the authentic PDF title and author list. The legacy BibTeX had correct authors (`hidayatulloh2026explainable.bib`), validating that Paper18 represents the authors' 2026 JOISER study.

---

## 2. Research Problem

Declining academic performance and student dropouts present significant institutional challenges in higher education. While machine learning classifiers can predict student academic risk, complex models often function as uninterpretable "black boxes." Without transparent, explainable rationales behind automated predictions, academic advisors and educators cannot identify the precise underlying drivers of failure, making it difficult to trust automated alerts or design personalized, timely pedagogical interventions.

### Source Evidence
- **PDF Page**: Page 1 (p. 31), Abstract & Section 1 "Introduction".

---

## 3. Research Objectives

1. Develop and benchmark machine learning models (Random Forest and XGBoost) to classify undergraduate students into "At Risk" vs. "Not at Risk" academic categories.
2. Address class imbalance inherent in academic risk datasets where at-risk students represent a critical minority.
3. Integrate dual Explainable Artificial Intelligence (XAI) frameworks—**SHAP (SHapley Additive exPlanations)** and **LIME (Local Interpretable Model-agnostic Explanations)**—to interpret global feature importance and provide local instance-level explanations for individual predictions.
4. Establish an interpretable decision-support architecture for higher education counseling and targeted academic intervention.

### Source Evidence
- **PDF Page**: Page 1 (p. 31), Abstract & Page 4 (p. 34), Section 3 "Methods".

---

## 4. Research Questions

Not explicitly stated in numbered question format. Guided by empirical objectives:
- How do bagging (Random Forest) and boosting (XGBoost) compare in balancing precision vs. recall when detecting minority at-risk students?
- Which academic and behavioral features globally exert the strongest influence on student academic risk?
- Can local explanations from SHAP and LIME provide non-technical academic advisors with actionable insights into individual student failures and successes?

---

## 5. Dataset

- **Dataset Name**: Student Academic Dataset (Undergraduate Informatics / Computer Science)
- **Dataset Source**: University academic records / higher education institutional student records
- **Institution**: Universitas Sebelas April, Indonesia (incorporating standard educational attribute structures)
- **Target Population**: Bachelor of Computer Science and Engineering (BCSE) students
- **Total Dataset Size**: Approximately 650 records (130 test instances evaluated under an 80:20 split)
- **Target Variable**: `Risk Status` (Binary):
  - **At Risk**: Cumulative GPA (CGPA) $< 2.50$
  - **Not at Risk**: Cumulative GPA (CGPA) $\ge 2.50$
- **Data Type**: Tabular demographic, behavioral, and academic performance data
- **Real / Synthetic**: Real student academic records
- **Train / Test Split**: 80% training set (520 instances), 20% test set (130 instances: 110 Not at Risk, 20 At Risk)

### Source Evidence
- **PDF Page**: Pages 3–4 (pp. 33–34), Section 3 & Table 1; Page 5 (p. 35), Section 4.1 & Figure 2.

---

## 6. Features

The feature schema encompasses academic, behavioral, and demographic attributes (Table 1, PDF p. 34):

### Academic & Prior Performance
- `CGPA`: Cumulative Grade Point Average (target threshold split at 2.50).
- `SGPA`: Semester Grade Point Average.
- `Semester`: Current active academic semester (e.g., Semester 1 to 13).
- `failures`: Number of past course failures.
- `G2`: Previous period's final academic grade.

### Behavioral & Attendance
- `Attendance`: Lecture attendance percentage (e.g., 85%, 90%, 95%, 100%).
- `absences`: Total recorded lecture absence count.
- `Study Hours`: Self-reported weekly study hours (e.g., 2 to 7 hours).

### Demographic & Financial
- `Gender`: Male / Female.
- `Age`: Student chronological age (e.g., 20–25 years).
- `Scholarship`: Financial aid status (Yes / No).
- `Program`: Study discipline (BCSE).

### Source Evidence
- **PDF Page**: Page 4 (p. 34), Table 1 & Page 6 (p. 36), Section 4.2.

---

## 7. Data Preprocessing

1. **Extraction**: Ingestion of tabular student data from CSV/Excel databases.
2. **Missing Value Imputation**: Cleaning and handling sparse or missing values across records.
3. **Categorical Encoding**: Transforming nominal variables (`Gender`, `Scholarship`, `Program`) via label encoding and one-hot encoding.
4. **Feature Scaling**: Normalization / standardization applied to continuous numeric attributes (`Attendance`, `Study Hours`, `SGPA`).
5. **Class Labeling**: Discretizing continuous CGPA into binary target classes (`CGPA < 2.50` $\rightarrow$ At Risk; `CGPA ≥ 2.50` $\rightarrow$ Not at Risk).

### Source Evidence
- **PDF Page**: Page 4 (p. 34), Section 3 "Methods".

---

## 8. Algorithms and Models

### 1. Random Forest (Bagging Paradigm)
- Constructs an ensemble of independent decision trees via bootstrap sampling.
- Reduces variance through majority voting, providing high resistance to noisy educational data.

### 2. XGBoost (Extreme Gradient Boosting)
- Constructs decision trees sequentially to minimize residual loss gradients.
- Incorporates $L_1$ and $L_2$ regularization terms to control model complexity and prevent overfitting on imbalanced minority classes.

### 3. Dual XAI Interpretability Engine
- **SHAP (SHapley Additive exPlanations)**: TreeSHAP implementation calculating exact Shapley values from cooperative game theory for global feature importance and individual force plots.
- **LIME (Local Interpretable Model-agnostic Explanations)**: Local perturbation-based surrogate modeling generating human-interpretable linear approximations around specific student predictions.

### Source Evidence
- **PDF Page**: Page 4 (p. 34), Section 3; Pages 5–8 (pp. 35–38), Section 4.

---

## 9. Architecture

The decision-support pipeline consists of:
1. **Data ETL Layer**: Database extraction, categorical encoding, and scaling.
2. **Predictive Ensemble Core**: Dual-model training (Random Forest vs XGBoost) with 80:20 train/test evaluation.
3. **Dual XAI Interpretation Engine**:
   - *Global Explainer*: SHAP summary dot plots ranking top predictors across the entire student population.
   - *Local Explainer*: SHAP Force Plots and LIME Bar Charts explaining individual true positives, true negatives, and edge-case misclassifications.
4. **Academic Advisory Interface**: Translates model outputs into actionable, transparent advisory alerts for early intervention.

### Source Evidence
- **PDF Page**: Pages 4–8 (pp. 34–38), Sections 3 and 4, Figures 1–6.

---

## 10. Methodology

1. **Data Ingestion & Annotation**: Labeling students as "At Risk" based on the institutional threshold ($CGPA < 2.50$).
2. **Preprocessing**: One-hot encoding, missing value imputation, and feature scaling.
3. **Model Training**: Fitting Random Forest and XGBoost classifiers on the 80% training split.
4. **Performance Evaluation**: Benchmarking Accuracy, Precision, Recall, and F1-Score on the held-out 20% test set ($N=130$).
5. **Global XAI Analysis**: Generating SHAP summary plots to evaluate macroscopic feature weights.
6. **Local XAI Dissection**: Running SHAP force plots and LIME local surrogates on specific correct and misclassified student instances.

### Source Evidence
- **PDF Page**: Pages 4–8 (pp. 34–38).

---

## 11. Experimental Setup

- **Platform**: Google Colaboratory (Cloud environment).
- **Runtime**: Python 3.10.
- **Core Libraries**: `scikit-learn`, `xgboost`, `shap`, `lime`, `pandas`, `matplotlib`, `seaborn`.
- **Dataset Partition**: 80% Training ($N=520$), 20% Testing ($N=130$).

### Source Evidence
- **PDF Page**: Page 4 (p. 34), Section 3.

---

## 12. Evaluation Metrics

- **Overall Accuracy**: Total correct classifications over all test instances.
- **Precision (Risk Class)**: $\frac{TP}{TP + FP}$ (reliability of at-risk alert).
- **Recall (Risk Class)**: $\frac{TP}{TP + FN}$ (sensitivity in catching at-risk students).
- **F1-Score (Risk Class)**: Harmonic mean of precision and recall.
- **Confusion Matrix**: Full breakdown of TP, TN, FP, FN.

### Source Evidence
- **PDF Page**: Page 4 (p. 34), Section 3 & Page 5 (p. 35), Table 2.

---

## 13. Results

### Classification Performance on Test Set ($N=130$) (Table 2, PDF p. 35)

| Metric | Random Forest | XGBoost | Best Model Tradeoff |
|:---|:---:|:---:|:---|
| **Accuracy** | **90.77%** (0.9077) | 89.23% (0.8923) | Random Forest (+1.54%) |
| **Precision (Risk Class)** | **0.7500** (75.00%) | 0.6364 (63.64%) | Random Forest (+11.36%) |
| **Recall (Risk Class)** | 0.6000 (60.00%) | **0.7000** (70.00%) | XGBoost (+10.00%) |
| **F1-Score (Risk Class)** | **0.6667** | **0.6667** | Identical Balance |

### Confusion Matrix Breakdown (PDF p. 5, Figure 2)
- **Random Forest**: True Negative (TN) = 106, True Positive (TP) = 12, False Positive (FP) = 4, False Negative (FN) = 8.
- **XGBoost**: True Negative (TN) = 102, True Positive (TP) = 14, False Positive (FP) = 8, False Negative (FN) = 6.

### XAI Global & Local Findings (PDF pp. 6–8)
1. **Global Top Predictors**: SHAP summary plots reveal that `G2` (previous period final grade), `failures` (past failed courses), and `absences` (lecture absences) dominate academic risk.
2. **Precision vs. Recall Tradeoff**:
   - Random Forest minimizes false alarms ($FP=4$), making it suitable when intervention resources are tightly constrained.
   - XGBoost catches more at-risk students ($TP=14, FN=6$), making it ideal when missing an at-risk student incurs severe academic consequences.
3. **Local Explanations**: SHAP force plots and LIME bar charts successfully illustrated how individual students with high absences were pushed toward "At Risk" despite moderate study hours.

### Source Evidence
- **PDF Page**: Page 5 (p. 35), Table 2, Figure 2; Pages 6–8 (pp. 36–38), Figures 3–6.

---

## 14. Baselines

- **Random Forest vs. XGBoost**: Comparing Bagging against Boosting paradigms under identical preprocessing and feature sets.

### Source Evidence
- **PDF Page**: Page 4 (p. 34) & Page 5 (p. 35).

---

## 15. Ablation Study

Evaluated through dual-model comparison and local XAI counterfactual dissection: comparing instances with identical attendance but varying prior failures demonstrates the marginal contribution of individual features on model decision boundaries.

### Source Evidence
- **PDF Page**: Pages 6–8 (pp. 36–38).

---

## 16. Explainability

A core contribution of the paper:
- **SHAP (TreeSHAP)**: Generates global feature importance rankings and instance-level force plots showing push/pull contributions toward the base value.
- **LIME**: Builds a local surrogate around individual student records, outputting explicit human-readable decision rules (e.g., `absences > 12.0` contributes $+0.42$ toward risk).

### Source Evidence
- **PDF Page**: Pages 6–8 (pp. 36–38), Figures 3, 4, 5, and 6.

---

## 17. Main Findings

1. Both Random Forest (90.77% accuracy) and XGBoost (89.23% accuracy) provide strong predictive efficacy for student academic risk, sharing an identical F1-score of 0.6667.
2. Random Forest is superior for minimizing false positives (Precision = 0.7500), while XGBoost is superior for catching true at-risk cases (Recall = 0.7000).
3. Dual XAI integration (SHAP + LIME) eliminates the black-box dilemma, identifying prior grade trajectory (`G2`), accumulated failures, and attendance as the three decisive risk factors.
4. Transparent, instance-level explanations provide actionable justifications that counselors and non-technical educators can readily interpret.

### Source Evidence
- **PDF Page**: Page 1 (p. 31), Abstract; Page 5 (p. 35), Section 4.1; Pages 8–9 (pp. 38–39), Section 5 "Conclusion".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Contextual Generalizability**: Dataset is derived from a specific higher education context (informatics/BCSE program), potentially limiting direct transferability to other institutions with different curricula.
- **Static Temporal Nature**: Relies on static historical snapshots rather than streaming, real-time weekly behavioral changes during the semester.

### 18.2 Research Interpretation
- The test set includes 20 at-risk students ($N_{test}=130$), reflecting real-world class imbalance, but larger cross-institutional cohorts would further validate model stability.
- The model focuses primarily on academic performance risk rather than holistic placement/career readiness.

---

## 19. Future Work

Explicitly proposed by authors:
1. Expanding the dataset to multi-institutional cohorts across diverse geographic regions.
2. Incorporating longitudinal and temporal time-series data to track dynamic student trajectories.
3. Integrating advanced deep learning ensembles interpreted through XAI.
4. Developing interactive, web-based counselor dashboards for real-time academic risk monitoring.

### Source Evidence
- **PDF Page**: Page 9 (p. 39), Section 5 "Conclusion".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Explainability & Early Risk Detection Engine (Module 03)**.
- **Direct Algorithmic Integration**: Validates the complementary use of SHAP (for global dashboard feature importance) and LIME (for localized candidate diagnostic feedback cards) in educational intelligence.
- **Policy Threshold Blueprint**: Demonstrates how placement systems should select between Random Forest (high precision for automated alert delivery) and XGBoost (high recall for counselor intervention queues).

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Random Forest achieves 90.77% accuracy, 0.7500 precision | Test set ($N=130$): Acc=0.9077, Prec=0.7500 | PDF p. 5, Table 2 | Experimental result |
| XGBoost achieves 0.7000 recall, 89.23% accuracy | Test set ($N=130$): Acc=0.8923, Rec=0.7000 | PDF p. 5, Table 2 | Experimental result |
| Identical F1-score of 0.6667 for risk class | Both models reach F1=0.6667 | PDF p. 5, Table 2 | Experimental result |
| Confusion matrix: RF (106 TN, 12 TP, 4 FP, 8 FN) | Full matrix values reported | PDF p. 5, Figure 2 | Experimental result |
| G2, failures, and absences are top SHAP predictors | SHAP summary plot analysis | PDF p. 6 & p. 9 | XAI result |

---

## 22. Verification Checklist

- [x] PDF read
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected
- [x] Dataset verified
- [x] Features verified
- [x] Algorithms verified
- [x] Architecture inspected
- [x] Experiments inspected
- [x] Results verified
- [x] Limitations verified
- [x] Future work verified
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read, exact numerical performance metrics and confusion matrices verified from Table 2 and Figure 2, dual XAI methodology documented).
