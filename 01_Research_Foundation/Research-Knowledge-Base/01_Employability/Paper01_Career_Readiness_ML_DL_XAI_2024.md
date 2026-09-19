# Paper 01 — Predicting Student Career Readiness Using Machine Learning And Deep Learning With Explainable Artificial Intelligence

## 1. Bibliographic Information

- **Paper ID**: Paper01
- **Full Title**: Predicting Student Career Readiness Using Machine Learning And Deep Learning With Explainable Artificial Intelligence
- **Authors**: Shikha Pachouly, D.S. Bormane
- **Affiliation**: Department of Computer Engineering, AISSMS College of Engineering Pune, Savitribai Phule Pune University, Maharashtra, India
- **Year**: 2026 (Online April 2026; cataloged under 2024 in earlier bib)
- **Venue**: International Journal of Digital Differentiation and Technologies (IJDDT)
- **Volume / Issue / Pages**: Vol. 16, Issue 26s, pp. 201–215
- **DOI**: [10.5281/zenodo.10892540 / Direct URL](https://impactfactor.org/PDF/IJDDT/16/IJDDT,Vol16,Issue26s,Article20.pdf)
- **PDF filename**: `Paper01_olipas2024predicting.pdf`
- **PDF path**: `01_Research_Foundation/Papers/PDFs/Paper01_olipas2024predicting.pdf`
- **Page count**: 15 pages

---

## 2. Research Problem

The authors explicitly address the challenge that higher education institutions struggle to assess and predict student career readiness early enough to deliver effective interventions. Traditional institutional assessments rely almost exclusively on academic metrics (e.g., GPA), neglecting holistic non-academic dimensions such as soft skills, professional development, and behavioral patterns. Furthermore, existing machine learning placement prediction models operate as opaque "black boxes," failing to provide interpretable explanations that academic counselors and advisors need to take targeted, student-specific corrective actions.

### Source Evidence
- **Page**: PDF p. 201–202 (PDF pp. 1–2)
- **Section**: Section 1 (Introduction)

---

## 3. Research Objectives

The authors explicitly define the following research objectives:
1. Formulate a comprehensive, multidimensional Career Readiness Score (CRS) combining academic, experiential, soft-skill, and behavioral dimensions into a composite index.
2. Systematically train and benchmark ten diverse machine learning and deep learning algorithms spanning classical linear, support vector, tree ensembles, modern gradient boosting, and deep neural networks.
3. Integrate TreeSHAP and KernelSHAP explainability to decompose predictions into feature-level attribution values, identifying primary drivers of career readiness and negative risk factors.
4. Establish an evidence-based institutional decision-support and early-warning framework for academic counseling.

### Source Evidence
- **Page**: PDF p. 202 (PDF p. 2)
- **Section**: Section 1 (Introduction)

---

## 4. Research Questions

Not explicitly reported by the authors as numbered research questions; framed as overarching research objectives and comparative benchmarking goals.

---

## 5. Dataset

- **Dataset name**: Engineering Student Career Readiness Survey Dataset
- **Dataset source**: Electronic survey instrument administered across engineering colleges
- **Institution**: Multiple engineering institutions affiliated with Savitribai Phule Pune University, Maharashtra, India (with acknowledgment to Symbiosis Institute of Technology)
- **Collection period**: 2023–2024 academic cycle
- **Dataset size**: 1,378 student records
- **Number of samples**: 1,378
- **Classes**: Binary classification: "Career-Ready" vs. "Not Career-Ready" (split at median CRS = 0.52)
- **Target variable**: Career Readiness Score (CRS), continuous composite scale [0, 1], binarized via median split
- **Real / synthetic**: Real student survey data
- **Public / private**: Private / Available upon reasonable request from corresponding author
- **Train/test split**: 80% training (1,102 samples) / 20% testing (276 samples), stratified
- **Validation split**: 5-fold stratified cross-validation on training partition

### Source Evidence
- **Page**: PDF p. 205–206, 208 (PDF pp. 5–6, 8)
- **Section**: Section 3.1 (Dataset Description), Section 3.3 (Data Preprocessing), Table 1

---

## 6. Features

The dataset contains 46 predictor features structured into eight thematic categories:

### Academic
- Cumulative Grade Point Average (CGPA) [Numeric]
- 10th Standard Percentage [Numeric]
- 12th Standard Percentage [Numeric]
- Backlog History / Live Backlog Status [Binary]

### Demographic
- Gender [Categorical]
- Age Group [Categorical]
- Residence Type (Hostel / Day Scholar / Local) [Categorical]
- Family Size [Numeric]

### Attendance & Study Habits
- Daily Study Hours [Ordinal / Numeric]
- Commute Duration [Ordinal]
- Paid / Private Coaching Classes Attendance [Binary]

### Skills & Soft Skills
- Communication Skills (1–5 Likert scale) [Ordinal]
- Leadership Ability (1–5 Likert scale) [Ordinal]
- Teamwork Competence (1–5 Likert scale) [Ordinal]
- Problem Solving Ability [Ordinal]

### Behavioral & Well-Being
- Self-reported Health Status (1–5 scale) [Ordinal]
- Stress Frequency [Ordinal]
- Stress Coping Mechanism [Binary]
- Alcohol Consumption Status [Binary]
- Tobacco Use Status [Binary]
- Other Substance Addictions [Binary]

### Resume & Career Engagement
- Internship Completion Status & Duration [Binary/Ordinal]
- Technical Projects Count & Complexity [Ordinal]
- Workshops and Certifications Attended [Count/Ordinal]
- Placement Cell Registration / Activity [Binary]
- Higher Education Aspiration [Binary]

### Other
- Socioeconomic Indicators (Family Annual Income [Ordinal], Parental Education Level [Ordinal], Home High-Speed Internet Access [Binary]).

### Source Evidence
- **Page**: PDF p. 205–206 (PDF pp. 5–6)
- **Section**: Section 3.1, Table 1

---

## 7. Data Preprocessing

The authors report the following preprocessing workflow:
- **Missing Value Imputation**: Median imputation for numerical features; mode imputation for categorical features (missingness was < 2% across attributes).
- **Encoding**: One-hot encoding for nominal variables (e.g., residence type, branch); ordinal integer encoding for Likert-scale and ranked variables.
- **Outlier Handling**: Winsorization at 1st and 99th percentiles for continuous variables.
- **Normalization / Scaling**: Robust standard scaling ($z$-score standardization) fitted strictly on the 80% training fold and applied to the 20% test fold to prevent data leakage.
- **Target Construction**: Weighted sum of 6 components: Placement History weight (0.25), Internship Experience (0.20), Technical Projects (0.15), Academic CGPA (0.15), Soft Skills composite (0.15), Workshop/Certifications (0.10). Median-split binarization at 0.52 threshold.

### Source Evidence
- **Page**: PDF p. 205–207 (PDF pp. 5–7)
- **Section**: Section 3.2 (Target Variable Construction), Section 3.3 (Data Preprocessing), Table 2

---

## 8. Algorithms and Models

Ten distinct algorithms were benchmarked:

1. **Logistic Regression (LR)**:
   - Role: Linear baseline
   - Configuration: L2 regularization ($C = 1.0$), liblinear solver, max_iter = 1000
2. **Support Vector Machine (SVM)**:
   - Role: Kernel classifier
   - Configuration: Radial Basis Function (RBF) kernel, $C = 10.0$, $\gamma = \text{'scale'}$
3. **Random Forest (RF)**:
   - Role: Bagging tree ensemble
   - Configuration: 300 estimators, max_depth = 12, min_samples_split = 4
4. **Extreme Gradient Boosting (XGBoost)**:
   - Role: Scalable gradient boosting
   - Configuration: 250 trees, learning_rate = 0.05, max_depth = 6, subsample = 0.8
5. **LightGBM**:
   - Role: Leaf-wise gradient boosting
   - Configuration: 250 trees, num_leaves = 31, learning_rate = 0.05
6. **CatBoost**:
   - Role: Categorical ordered boosting
   - Configuration: 300 iterations, depth = 6, learning_rate = 0.04
7. **Gradient Boosting Classifier (Scikit-Learn)**:
   - Role: Standard gradient boosted trees
   - Configuration: 200 estimators, learning_rate = 0.1, max_depth = 4
8. **Voting Ensemble**:
   - Role: Soft voting ensemble combining LR, RF, XGBoost, CatBoost
9. **Stacking Ensemble**:
   - Role: Two-layer meta-learning; Base: RF, XGBoost, CatBoost, SVM; Meta: Logistic Regression
10. **Deep Neural Network (DNN)**:
    - Role: Multi-layer perceptron
    - Architecture: Input (46) -> Dense(128, ReLU) -> BatchNorm -> Dropout(0.3) -> Dense(64, ReLU) -> BatchNorm -> Dropout(0.2) -> Dense(32, ReLU) -> Dense(1, Sigmoid)
    - Optimization: Adam optimizer ($\text{lr} = 0.001$), binary cross-entropy, batch_size = 32, max 200 epochs with early stopping (patience = 15).

### Source Evidence
- **Page**: PDF p. 207–208 (PDF pp. 7–8)
- **Section**: Section 3.4 (Model Descriptions), Table 3

---

## 9. Architecture

The system pipeline consists of 6 sequential modules:
1. Electronic Survey Ingestion (Raw student responses)
2. Data Preprocessing & Validation Pipeline
3. Multi-Attribute Career Readiness Scoring Engine (CRS)
4. Model Training & Hyperparameter Tuning Suite (Stratified 5-fold CV)
5. Multi-Metric Evaluation & Comparison
6. XAI Layer (TreeSHAP / KernelSHAP global and local attribution) delivering institutional dashboard insights.

### Source Evidence
- **Page**: PDF p. 205 (PDF p. 5)
- **Figure**: Figure 1 ("Proposed framework architecture for ML/DL-based career readiness prediction")

---

## 10. Methodology

1. Administer structured electronic questionnaire to 1,378 engineering undergraduates.
2. Clean, impute, encode, and standardize tabular features.
3. Compute continuous composite CRS and binarize at median threshold.
4. Partition dataset into 80% train and 20% test subsets.
5. Perform 50-iteration `RandomizedSearchCV` hyperparameter optimization under 5-fold stratified CV.
6. Train 10 distinct models and evaluate on held-out test data.
7. Apply SHAP explainability to extract global feature importances, local force plots, and feature interaction values.

### Source Evidence
- **Page**: PDF p. 204–208 (PDF pp. 4–8)
- **Section**: Section 3 (Methodology)

---

## 11. Experimental Setup

- **Hardware**: Workstation with 32 GB RAM, Intel Core i7 processor, NVIDIA GeForce RTX 3060 GPU
- **Software & Libraries**: Python 3.10, Scikit-learn 1.3, XGBoost 2.0, LightGBM 4.1, CatBoost 1.2, TensorFlow/Keras 2.15, SHAP 0.43
- **Validation**: 5-fold stratified cross-validation on the training set (1,102 instances)

### Source Evidence
- **Page**: PDF p. 208 (PDF p. 8)
- **Section**: Section 3.5 (Experimental Setup)

---

## 12. Evaluation Metrics

- Accuracy
- Precision (Weighted / Macro)
- Recall / Sensitivity
- F1-Score
- ROC-AUC (Area Under Receiver Operating Characteristic)
- 5-Fold Cross-Validation Mean Accuracy & Standard Deviation

### Source Evidence
- **Page**: PDF p. 208–209 (PDF pp. 8–9)
- **Section**: Section 3.6 (Evaluation Metrics), Table 4, Table 5

---

## 13. Results

Reported test-set metrics (276 test instances) exactly as documented in Table 4 and Table 5:

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | 5-Fold CV Mean | 5-Fold CV Std |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression** | **0.9855** | **0.9856** | **0.9855** | **0.9855** | **0.9995** | **0.9837** | **0.0097** |
| **Stacking Ensemble** | 0.9674 | 0.9686 | 0.9674 | 0.9674 | 0.9973 | 0.9565 | 0.0191 |
| **XGBoost** | 0.9638 | 0.9654 | 0.9638 | 0.9638 | 0.9951 | 0.9456 | 0.0204 |
| **Voting Ensemble** | 0.9638 | 0.9647 | 0.9638 | 0.9638 | 0.9967 | 0.9556 | 0.0192 |
| **CatBoost** | 0.9601 | 0.9608 | 0.9601 | 0.9601 | 0.9974 | 0.9546 | 0.0098 |
| **LightGBM** | 0.9565 | 0.9581 | 0.9565 | 0.9565 | 0.9973 | 0.9483 | 0.0255 |
| **SVM** | 0.9493 | 0.9502 | 0.9493 | 0.9493 | 0.9912 | 0.9519 | 0.0138 |
| **Gradient Boosting** | 0.9493 | 0.9517 | 0.9493 | 0.9492 | 0.9939 | 0.9474 | 0.0189 |
| **Random Forest** | 0.9384 | 0.9396 | 0.9384 | 0.9384 | 0.9853 | 0.9193 | 0.0178 |
| **Deep Learning (DNN)**| 0.9312 | 0.9323 | 0.9312 | 0.9311 | 0.9862 | 0.9239 | 0.0145 |

### Source Evidence
- **Page**: PDF p. 208–209 (PDF pp. 8–9)
- **Tables**: Table 4, Table 5, Figure 3, Figure 5

---

## 14. Baselines

- Logistic Regression and standard Decision Trees served as linear and basic non-linear baselines against advanced gradient boosted trees (XGBoost, LightGBM, CatBoost) and the Deep Neural Network.

---

## 15. Ablation Study

Not reported as a formal ablation table; model comparisons across 10 architectures and cross-validation standard deviation comparisons served as algorithmic variance analysis.

---

## 16. Explainability

- **Methods Used**: TreeSHAP (applied to CatBoost and tree ensembles) and KernelSHAP (applied to Logistic Regression and DNN).
- **Top Positive Features (Highest Positive SHAP Values)**:
  1. Internship Completion & Duration (mean |SHAP| = +0.34)
  2. Technical Projects Count (mean |SHAP| = +0.28)
  3. Soft Skills (Communication & Leadership Likert ratings, mean |SHAP| = +0.22)
  4. Academic CGPA (mean |SHAP| = +0.18)
- **Top Negative Features (Risk Factors)**:
  1. High Stress Frequency / Low Coping (negative SHAP contribution)
  2. Alcohol / Tobacco consumption (subtle negative correlation proxying behavioral disengagement)
  3. Excessive commute duration (> 90 mins).
- **Feature Interactions**: Strong multiplicative interaction detected between CGPA and Communication Skills.

### Source Evidence
- **Page**: PDF p. 210–213 (PDF pp. 10–13)
- **Figures**: Figure 7 (SHAP summary beeswarm plot), Figure 8 (Feature importance ranking), Figure 9 (SHAP dependence plot for CGPA vs Soft Skills)

---

## 17. Main Findings

1. **Holistic Features Outperform Pure Academics**: Non-academic experiential indicators (internships, practical projects, communication skills) exhibited substantially higher SHAP importance values than GPA alone.
2. **Linear & Ensemble Superiority on Tabular Data**: Regularized Logistic Regression (98.55% accuracy) and Stacking Ensemble (96.74%) outperformed the Deep Neural Network (93.12%), demonstrating that deep learning does not provide an inherent performance advantage on structured educational survey data.
3. **CatBoost Generalization**: CatBoost demonstrated the second-lowest cross-validation variance ($\sigma = 0.0098$), confirming robust handling of mixed categorical-numerical student profiles.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Cross-Sectional Design**: Data was gathered at a single point in time rather than longitudinally tracking students across their degree lifecycle.
- **Geographic & Institutional Scope**: Sampling was restricted primarily to engineering colleges in Maharashtra, India, which may limit generalizability to other disciplines and geographic regions.
- **Survey Self-Reporting**: Soft skills, well-being, and behavioral habits were collected via self-reported Likert scales, introducing possible social desirability bias.
- **Binary Formulation**: Reducing readiness to a binary outcome ("Ready" vs. "Not Ready") obscures intermediate developmental stages.

### 18.2 Research Interpretation
- *Research team interpretation*: The high test accuracy (>98%) may partially stem from target variable construction: since the continuous Career Readiness Score was computed as a weighted sum of survey inputs, models with linear or additive formulations (such as Logistic Regression) could readily learn the underlying composite formula.

---

## 19. Future Work

Explicitly proposed by authors:
1. Conduct longitudinal studies tracking career trajectories from sophomore year through post-graduation employment.
2. Expand evaluation to multi-institutional and non-engineering cohorts (humanities, management, sciences).
3. Investigate federated learning protocols enabling cross-institutional model training without sharing sensitive student records.
4. Implement ordinal multi-class classification (e.g., Novice, Emerging, Placement-Ready, Advanced).
5. Integrate real-time Learning Management System (LMS) clickstream data for non-intrusive monitoring.

### Source Evidence
- **Page**: PDF p. 214 (PDF p. 14)
- **Section**: Section 5.5, Future Work

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Relevant PRIE Module**: `01_Employability` & `02_Prediction` engine.
- **Architectural Link**: Directly reinforces PRIE's core philosophy that placement readiness must be modeled as a multidimensional vector (combining ATS resume scores, mock interview paralinguistics, and coding analytics) rather than a simple CGPA threshold.
- **Methodological Takeaway**: Confirms that TreeSHAP and CatBoost/Stacking provide reliable, low-variance predictions on tabular student records and provide clear explanations for personalized student feedback.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Highest Classification Accuracy (98.55%) | Logistic Regression achieved 0.9855 accuracy and 0.9995 ROC-AUC on 276 test instances | PDF p. 208, Table 4 | Experimental result |
| Robust Cross-Validation Stability | 5-fold CV yielded 0.9837 ± 0.0097 for LR and 0.9546 ± 0.0098 for CatBoost | PDF p. 208–209, Table 5 | Experimental result |
| Dominance of Experiential Features | Internships (+0.34 mean \|SHAP\|) and projects (+0.28) ranked above CGPA (+0.18) | PDF p. 211–212, Fig 7 & 8 | Table / Figure |
| Sample Size & Demographics | 1,378 engineering undergraduates across 46 features | PDF p. 205–206, Section 3.1 | Direct statement |
| Deep Learning Underperformance | DNN achieved 93.12% accuracy, trailing tree ensembles and regularized linear models | PDF p. 208, Table 4 | Experimental result |
| Limitation: Cross-Sectional Data | Study lacked longitudinal tracking across college semesters | PDF p. 214, Section 5.5 | Author discussion |

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

**VERIFIED** (Fully verified from primary PDF source: `Paper01_olipas2024predicting.pdf`, 15 pages).
