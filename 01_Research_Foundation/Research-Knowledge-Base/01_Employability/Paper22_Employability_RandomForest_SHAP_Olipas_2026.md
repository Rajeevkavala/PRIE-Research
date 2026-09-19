# Paper 22 — Predictive Modeling and Explainability of Student Employability in the Philippines Using Random Forest and Shapley Additive Explanations

## 1. Bibliographic Information

- **Paper ID**: Paper22
- **Full Title**: Predictive Modeling and Explainability of Student Employability in the Philippines Using Random Forest and Shapley Additive Explanations
- **Authors**: Cris Norman P. Olipas*
- **Institution**: Nueva Ecija University of Science and Technology, Cabanatuan, Philippines
- **Corresponding Author Email**: `olipas.cris@gmail.com`
- **Year**: 2026 (Received: 9 October 2025, Revised: 1 & 5 January 2026, Accepted: 5 January 2026, Published: 2026)
- **Venue**: Interdisciplinary Journal of Information, Knowledge, and Management (IJIKM), Vol. 21, Article 2, pp. 1–19
- **ISSN (Online)**: 1555-1237
- **DOI**: 10.28945/5690
- **PDF filename**: `Paper22_olipas2025predictive.pdf`
- **PDF path**: `Papers/PDFs/Paper22_olipas2025predictive.pdf`
- **Page count**: 19 pages

> [!NOTE]
> **Corpus Reconciliation Note**: Metadata matches the authentic PDF publication. Paper22 represents Cris Norman P. Olipas's 2026 empirical study in *IJIKM* evaluating 2,982 Philippine student records with Random Forest and SHAP.

---

## 2. Research Problem

In the Philippines and broader emerging economies, graduate underemployment persists due to a structural disconnect between higher education curricula and industry labor market expectations. While prior employability studies emphasize technical or academic metrics (such as GPA), there is critical empirical scarcity regarding how **non-academic, behavioral, and cognitive interview traits** determine hiring readiness. Furthermore, existing employability predictive models are often deployed as opaque black-box systems, preventing university career placement officers and policymakers from identifying the precise behavioral deficiencies that disadvantage students during job placement interviews.

### Source Evidence
- **PDF Page**: Page 1, Abstract & Section "Background"; Pages 2–4, Section "Introduction".

---

## 3. Research Objectives

1. Develop a data-driven machine learning framework to predict binary graduate employability outcomes from mock interview assessments.
2. Evaluate and benchmark four machine learning algorithms—**Random Forest, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Logistic Regression**—across 10-fold cross-validation and an independent test set.
3. Conduct rigorous statistical significance testing (Student's t-tests) to validate whether ensemble learning demonstrates statistically superior predictive accuracy.
4. Integrate **Shapley Additive Explanations (SHAP)** to rank the relative influence of non-academic traits and explain local model decision boundaries.
5. Provide evidence-based recommendations for university career development programs and On-the-Job Training (OJT) mentorship.

### Source Evidence
- **PDF Page**: Page 1, Abstract; Page 4, Section "Aim and Objectives"; Page 7, Section "Methodology".

---

## 4. Research Questions

Framed through empirical and interpretability goals:
- *RQ1*: Which machine learning classifier achieves the highest predictive accuracy, precision, recall, and F1-score when evaluating student employability from interview traits?
- *RQ2*: Are performance differences between ensemble algorithms (Random Forest) and classical models (Logistic Regression, SVM, KNN) statistically significant?
- *RQ3*: What non-academic behavioral and cognitive attributes dominate employability predictions under SHAP feature importance analysis?

---

## 5. Dataset

- **Dataset Name**: Philippine Higher Education Student Employability Dataset
- **Dataset Source**: Publicly available benchmark corpus derived from university mock interviews conducted across Philippine higher education institutions (hosted on Kaggle)
- **Total Sample Size**: **$N = 2,982$ anonymized student records**
- **Data Quality**: Complete records retained; entries with missing attributes excluded
- **Target Variable**: `Class` (Binary):
  - **Employable**: Student meets hiring threshold
  - **Less Employable**: Student requires substantial behavioral/competency intervention
- **Data Type**: Tabular ordinal assessment scores
- **Real / Synthetic**: Real student mock interview performance evaluations
- **Class Imbalance Handling**: Manual oversampling applied by duplicating minority "Less Employable" records to prevent majority-class bias.

### Source Evidence
- **PDF Page**: Page 1, Abstract; Page 7, Section "Dataset Description and Preparation"; Table 2.

---

## 6. Features

The predictive schema consists of eight non-academic, interview-observed predictor variables (Table 2, PDF pp. 7–8), all measured on standardized ordinal rating scales:

1. `Mental Alertness`: Attentiveness, cognitive responsiveness, and quickness of understanding during interaction.
2. `General Appearance`: Physical presentation, professional attire, grooming, and poise.
3. `Ability to Present Ideas`: Structural coherence, logical clarity, and effectiveness in articulating thoughts.
4. `Self-Confidence`: Poise in handling unexpected questions, assertiveness, and emotional composure.
5. `Physical Condition`: Posture, visible energy level, stamina, and general physical demeanor.
6. `Student Performance Rating`: Supervisory rating score accumulated during On-the-Job Training (OJT) internship.
7. `Manner of Speaking`: Speech modulation, verbal tone, clarity, and pacing.
8. `Communication Skills`: General linguistic fluency and lexical appropriateness.

### Source Evidence
- **PDF Page**: Pages 7–8, Table 2 "Predictor variables for student employability modeling".

---

## 7. Data Preprocessing

1. **Filtering & Quality Check**: Removal of records with incomplete attribute entries to ensure data integrity.
2. **Ordinal Encoding**: Converting qualitative performance rubrics into discrete ordinal numeric vectors.
3. **Class Balancing**: Manual oversampling of the minority class ("Less Employable") to balance class priors.
4. **Data Partitioning**: 10-fold cross-validation for hyperparameter tuning followed by independent train/test evaluation (80:20 partition).

### Source Evidence
- **PDF Page**: Page 7, Figure 1 ("Predictive modeling pipeline") & Page 8.

---

## 8. Algorithms and Models

### 1. Random Forest Classifier (Primary Model)
- Ensemble of decorrelated decision trees built via bootstrap aggregation.
- Selected for its capacity to model complex non-linear attribute interactions without overfitting.

### 2. Evaluated Baselines
- **K-Nearest Neighbors (KNN)**: Non-parametric distance-based instance learning.
- **Support Vector Machine (SVM)**: Maximum-margin hyperplane classification.
- **Logistic Regression**: Linear log-odds baseline.

### 3. Model Explainability Engine
- **TreeSHAP**: Computing exact cooperative game-theoretic Shapley values to generate global feature importance bar charts, summary dot plots, and local prediction waterfalls.

### Source Evidence
- **PDF Page**: Pages 8–11, Sections "Machine Learning Algorithms" and "Explainability Analysis".

---

## 9. Architecture

The end-to-end employability pipeline comprises four sequential stages (Figure 1, PDF p. 7):
1. **Data Acquisition & Curation**: Aggregation of 2,982 interview logs across Philippine colleges.
2. **Preprocessing & Balancing**: Ordinal encoding, outlier validation, and minority oversampling.
3. **Machine Learning Benchmarking Core**: Parallel training of RF, KNN, SVM, and Logistic Regression with 10-fold cross-validation and significance testing.
4. **XAI Interpretability Layer**: TreeSHAP generating global trait rankings and individual candidate diagnostic profiles for placement officers.

### Source Evidence
- **PDF Page**: Page 7, Figure 1.

---

## 10. Methodology

1. **Dataset Ingestion**: Loading 2,982 student records across 8 behavioral dimensions.
2. **Model Training & Cross-Validation**: Running 10-fold cross-validation to assess variance across Random Forest, KNN, SVM, and Logistic Regression.
3. **Inferential Hypothesis Testing**: Conducting paired Student's t-tests between Random Forest and each baseline algorithm to evaluate statistical significance ($p$-values).
4. **Test Set Generalization**: Evaluating trained models on an unseen test set across Accuracy, Precision, Recall, and F1-score.
5. **SHAP Interpretation**: Extracting global mean absolute Shapley values ($|\text{SHAP}|$) and visualizing directional influence via summary dot plots.

### Source Evidence
- **PDF Page**: Pages 7–12, Sections "Methodology" and "Results".

---

## 11. Experimental Setup

- **Language & Runtime**: Python 3.x, Jupyter / Colab environment.
- **Machine Learning**: `scikit-learn` (RandomForestClassifier, KNeighborsClassifier, SVC, LogisticRegression).
- **Explainability**: `shap` library (TreeExplainer).
- **Statistical Analysis**: Python `scipy.stats` (two-tailed Student's t-test).
- **Validation Design**: 10-fold cross-validation + independent held-out test split.

### Source Evidence
- **PDF Page**: Pages 8–9, Tables 3, 4, and 5.

---

## 12. Evaluation Metrics

- **Cross-Validation Accuracy**: Mean accuracy and standard deviation across 10 folds.
- **Test Accuracy, Precision, Recall, F1-Score**: Evaluated on held-out test data.
- **Student's t-statistic and $p$-value**: Assessing statistical superiority between models.
- **Mean Absolute SHAP Value**: Ranking trait importance.

### Source Evidence
- **PDF Page**: Pages 8–9, Tables 3–5; Page 10, Figure 2.

---

## 13. Results

### 1. Cross-Validation Performance (Table 3, PDF p. 9)

| Model | Mean Accuracy | Standard Deviation |
|:---|:---:|:---:|
| **Random Forest** | **0.9042** (90.42%) | **0.0140** |
| **KNN** | 0.8905 (89.05%) | 0.0164 |
| **SVM** | 0.8623 (86.23%) | 0.0131 |
| **Logistic Regression** | 0.5969 (59.69%) | 0.0190 |

### 2. Statistical Significance Testing vs. Random Forest (Table 4, PDF p. 9)

| Comparison | T-Statistic | $p$-Value | Statistical Interpretation |
|:---|:---:|:---:|:---|
| **RF vs. Logistic Regression** | **29.1615** | **0.0000** ($p < 0.001$) | Statistically Significant — RF superior |
| **RF vs. SVM** | **4.8927** | **0.0012** ($p < 0.01$) | Statistically Significant — RF superior |
| **RF vs. KNN** | 1.4267 | 0.1915 ($p > 0.05$) | Not Significant — Comparable performance |

### 3. Independent Test Set Performance Metrics (Table 5, PDF p. 9)

| Model | Accuracy | Precision | Recall | F1-Score | Overall Assessment |
|:---|:---:|:---:|:---:|:---:|:---|
| **Random Forest** | **0.9220** (92.20%) | **0.9220** | **0.9220** | **0.9220** | **Top Performer across all metrics** |
| **KNN** | 0.8829 (88.29%) | 0.8829 | 0.8829 | 0.8829 | Competitive non-parametric baseline |
| **SVM** | 0.8555 (85.55%) | 0.8619 | 0.8555 | 0.8549 | Moderate performance |
| **Logistic Regression** | 0.5376 (53.76%) | 0.5389 | 0.5376 | 0.5336 | Poor fit; unable to capture non-linear traits |

### 4. SHAP Feature Importance Rankings (Figures 2 & 3, PDF pp. 10–11)
The SHAP global attribution analysis reveals a clear three-tiered hierarchy of employability determinants:
1. **Tier 1 — Decisive Determinants (Dominant Drivers)**:
   - **`Mental Alertness`**: Ranked #1 overall predictor. High alertness strongly pushes predictions toward "Employable", while sluggish responsiveness triggers negative scores.
   - **`General Appearance`**: Ranked #2. Professional grooming and presentation heavily weight interviewer impressions.
   - **`Ability to Present Ideas`**: Ranked #3. Logical structuring and clarity of thought strongly dictate positive hiring decisions.
2. **Tier 2 — Secondary Moderating Traits**:
   - `Self-Confidence` (#4) and `Physical Condition` (#5).
3. **Tier 3 — Baseline / Supportive Traits**:
   - `Student Performance Rating` in OJT (#6), `Manner of Speaking` (#7), and `Communication Skills` (#8).
   - *Key finding*: Pure internship supervisor ratings and general communication skills function only as baseline thresholds; candidate cognitive sharpness, idea presentation, and professional presentation govern final employability classification.

### Source Evidence
- **PDF Page**: Pages 9–11, Tables 3, 4, 5, and Figures 2 & 3.

---

## 14. Baselines

- **Logistic Regression**: Linear classifier exhibiting near-random performance ($53.76\%$ test accuracy).
- **Support Vector Machine (SVM)**: Radial basis function kernel baseline ($85.55\%$ accuracy).
- **K-Nearest Neighbors (KNN)**: Distance metric baseline ($88.29\%$ accuracy).

### Source Evidence
- **PDF Page**: Page 9, Tables 3 & 5.

---

## 15. Ablation Study

Demonstrated through statistical comparison and linear vs. non-linear separation:
Logistic Regression's steep performance collapse ($53.76\%$) vs. Random Forest ($92.20\%$) and KNN ($88.29\%$) proves that employability outcomes cannot be modeled as a linear combination of traits; multi-attribute threshold interactions (e.g., high appearance cannot compensate for low mental alertness) govern recruiter decision-making.

### Source Evidence
- **PDF Page**: Page 9, Table 4 & Table 5.

---

## 16. Explainability

A core contribution of the study:
- **SHAP Summary Plot & Dot Plot**: Displays exact magnitude and direction of each feature value on model log-odds.
- **Actionable Student Counseling**: Placement officers can inspect individual SHAP force plots to deliver precise, non-generic feedback (e.g., *"Your communication fluency is strong, but interviewers penalized sluggish idea structuring and poor professional presentation"*).

### Source Evidence
- **PDF Page**: Pages 10–12, Figures 2, 3, and 4.

---

## 17. Main Findings

1. Random Forest achieved superior predictive performance for graduate employability, recording **92.20% accuracy, precision, recall, and F1-score** on independent test data.
2. Inferential t-tests prove Random Forest is statistically superior to Logistic Regression ($t = 29.16, p < 0.001$) and SVM ($t = 4.89, p = 0.0012$).
3. SHAP feature importance disproves the assumption that internship ratings alone dictate hiring; **Mental Alertness, General Appearance, and the Ability to Present Ideas** represent the top three predictive determinants.
4. Soft skills and cognitive presence operate as primary gating factors during interview screening, with technical grades serving as secondary qualifying baselines.

### Source Evidence
- **PDF Page**: Pages 9–13, Section "Results" & Section "Discussion".

---

## 18. Limitations

### 18.1 Explicitly Stated by Author
- **Lack of Academic / Demographic Features**: The Kaggle dataset excluded student CGPA, age, gender, and degree discipline, preventing holistic multimodal modeling.
- **Geographic Scope**: Data originates exclusively from Philippine higher education mock interviews, requiring external validation in other regional employment markets.
- **Static Mock Setting**: Evaluations were recorded during simulated academic interviews rather than confirmed live corporate hiring decisions.

### 18.2 Research Interpretation
- Minority class oversampling was conducted via simple duplication rather than synthetic interpolation (SMOTE).
- Feature measurements rely on human interviewer rubric ratings, which carry inherent subjective evaluation variance.

---

## 19. Future Work

Explicitly proposed by author:
1. Integrating academic performance metrics (GPA, technical test scores) alongside behavioral traits into a unified multimodal model.
2. Collecting longitudinal post-graduation employment tracking data to validate mock interview scores against actual corporate hiring outcomes.
3. Deploying the Random Forest and SHAP model into an interactive web-based advisory dashboard for university career placement centers.

### Source Evidence
- **PDF Page**: Page 15, Section "Conclusions and Future Work".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original author.*

- **Relevant Module**: **PRIE Employability Prediction Engine (Module 01) & Interview Simulator (Module 05)**.
- **Empirical Validation**: Provides direct empirical evidence ($N=2,982$) that non-academic interview traits (mental alertness, idea presentation, professional grooming) must be incorporated into PRIE's placement readiness vector alongside CGPA.
- **Feature Weighting Blueprint**: SHAP rankings provide empirical justification for PRIE's interview scoring weights: prioritizing structured cognitive responsiveness and idea presentation over generic grammar checks.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Random Forest achieves 92.20% accuracy, F1=0.9220 | Test set ($N=2,982$ corpus split): Table 5 | PDF p. 9, Table 5 | Experimental result |
| RF statistically superior to Logistic Reg ($p=0.0000$) | Two-tailed Student's t-test: $T=29.1615$ | PDF p. 9, Table 4 | Statistical result |
| RF statistically superior to SVM ($p=0.0012$) | Two-tailed Student's t-test: $T=4.8927$ | PDF p. 9, Table 4 | Statistical result |
| Mental Alertness ranked #1 trait under SHAP | Dominant predictor in summary dot plot | PDF pp. 10–11, Figs. 2 & 3 | XAI result |
| General Appearance & Presenting Ideas ranked #2 & #3 | SHAP feature importance rankings | PDF p. 10, Figure 2 | XAI result |

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

**VERIFIED** (Primary PDF read, exact numerical results verified from Tables 3, 4, 5, and SHAP Figures 2–3, sample size $N=2,982$ verified).
