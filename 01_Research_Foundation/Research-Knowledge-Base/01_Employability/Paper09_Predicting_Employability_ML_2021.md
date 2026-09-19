# Paper 09 — Predicting Students’ Employability using Machine Learning Approach

## 1. Bibliographic Information

- **Paper ID**: Paper09
- **Full Title**: Predicting Students’ Employability using Machine Learning Approach
- **Authors**: Cherry D. Casuat, Enrique D. Festijo
- **Affiliation**: Graduate School, Technological Institute of the Philippines (TIP), Quezon City / Manila, Philippines
- **Year**: 2019 (Presented December 2019 at IEEE ICETAS; cataloged under 2021 in earlier bib)
- **Venue**: 2019 6th IEEE International Conference on Engineering Technologies and Applied Sciences (ICETAS)
- **Publisher / Identifier**: IEEE / ISBN: 978-1-7281-4082-7 / CFP19N08-ART
- **DOI**: [10.1109/ICETAS48360.2019.9117441 / Semantic Scholar](https://www.semanticscholar.org/paper/9b14accbe90efa1c0164963b6bb07108e711566a)
- **PDF filename**: `Paper09_casuat2021predicting.pdf`
- **PDF path**: `01_Research_Foundation/Papers/PDFs/Paper09_casuat2021predicting.pdf`
- **Page count**: 5 pages

---

## 2. Research Problem

Higher Education Institutions (HEIs) in the Philippines face increasing accountability to ensure engineering graduates transition smoothly into professional industry roles. However, institutional career counseling is often reactive rather than predictive, waiting until after graduation tracer studies reveal unemployment. Institutions possess diverse administrative databases (registrar GPA records, internship ratings, career center mock interview evaluations), but lack an integrated machine learning approach to merge these datasets and predict student employability prior to graduation.

### Source Evidence
- **Page**: PDF p. 1–3 (PDF pp. 1–3)
- **Section**: Section I (Introduction), Section III (Machine Learning in Education)

---

## 3. Research Objectives

The authors explicitly define the following research objectives:
1. Integrate multi-source institutional datasets—comprising academic GPAs, On-the-Job Training (OJT) performance ratings, and mock job interview evaluations—into a unified student feature space.
2. Develop and benchmark supervised machine learning classification models (Decision Trees, Random Forest, Support Vector Machine) to predict graduate employability status.
3. Optimize algorithm hyperparameters using validation and learning curves to prevent overfitting.
4. Establish an empirical baseline for institutional career guidance at the Technological Institute of the Philippines.

### Source Evidence
- **Page**: PDF p. 1, 3 (PDF pp. 1, 3)
- **Section**: Abstract, Section III, Section IV (Case Study: Students' Employability)

---

## 4. Research Questions

Not explicitly stated as numbered research questions; framed as identifying the optimal classifier and hyperparameter space for predicting whether an engineering student will be "Employable" or "Less Employable".

---

## 5. Dataset

- **Dataset name**: TIP Engineering Student Employability Dataset
- **Dataset source**: Career Center, Registrar's Office, and OJT Faculty In-Charge at Technological Institute of the Philippines (TIP) - Manila, combined with alumni tracer surveys
- **Institution**: Technological Institute of the Philippines (TIP), Manila, Philippines
- **Collection period**: School Years (SY) 2015–2016 through 2018–2019 (4 graduating cohorts)
- **Dataset size**: 3,000 engineering student records ($N = 3,000$)
- **Data matrix dimensions**: 27,000 total data points (3,000 observations $\times$ 9 features)
- **Classes**: Binary classification: "Employable" vs. "Less Employable"
- **Target variable**: Employability class label determined from alumni survey employment verification
- **Real / synthetic**: Real institutional and tracer survey data
- **Privacy Compliance**: Compliant with Republic Act 10173 (Data Privacy Act of the Philippines)
- **Public / private**: Private institutional repository

### Source Evidence
- **Page**: PDF p. 3 (PDF p. 3)
- **Section**: Section IV (Case Study), Section IV-A (Data Collection)

---

## 6. Features

The dataset comprises 9 features extracted from three institutional offices:

### Academic & Institutional (Registrar's Office)
- General Point Average (GPA) across collegiate engineering coursework.
- Engineering degree program specialization.

### Practical / Fieldwork Experience (OJT Office)
- On-the-Job Training (OJT) Performance Rating assessed by faculty and industry supervisors.
- Technical execution competency in industry immersion.

### Career Center Evaluations
- Mock Job Interview Results (evaluating communication, professional poise, interview readiness).
- Technical aptitude and behavioral readiness ratings.

### Tracer Verification
- Employment landing status within post-graduation window.

### Source Evidence
- **Page**: PDF p. 3 (PDF p. 3)
- **Section**: Section IV-A (Data Collection), Table 1

---

## 7. Data Preprocessing

- **Data Integration & Merging**: Disparate relational tables from the Registrar's Office (GPA), OJT Faculty Coordinator (internship scores), and Career Center (mock interviews) were merged using student ID keys.
- **Privacy Compliance**: Data anonymization and privacy consent implemented via Google Forms survey deployment under the Philippine Data Privacy Act.
- **Label Encoding**: Standard supervised class labeling into binary categories (Employable vs. Less Employable).

### Source Evidence
- **Page**: PDF p. 3 (PDF p. 3)
- **Section**: Section III, Section IV-A

---

## 8. Algorithms and Models

Three supervised classifiers were evaluated:
1. **Support Vector Machine (SVM)**:
   - Configuration: Radial Basis Function (RBF) kernel, optimized gamma parameter ($\gamma = 10\text{ to }100$ in validation curve analysis).
   - Role: High-dimensional non-linear margin maximization.
2. **Decision Tree (DT)**:
   - Configuration: Standard recursive partitioning tree classifier.
3. **Random Forest (RF)**:
   - Configuration: Bootstrap aggregation ensemble of decision trees.

### Source Evidence
- **Page**: PDF p. 3–5 (PDF pp. 3–5)
- **Section**: Section III, Section IV-B, Section V (Conclusion), Figure 4, Figure 5

---

## 9. Architecture

The data pipeline follows a 4-step workflow:
1. Multi-Department Data Ingestion (Registrar, OJT, Career Center).
2. Data Preprocessing & Merging into 3,000 $\times$ 9 Feature Matrix.
3. Supervised Model Training & Hyperparameter Tuning (SVM, DT, RF).
4. Validation Curve Assessment ($R^2$ and cross-validation score tracking across gamma ranges) leading to Early-Warning Classification.

### Source Evidence
- **Page**: PDF p. 2–3, 5 (PDF pp. 2–3, 5)
- **Figure**: Figure 1 ("Methods of research in developing model for students' employability"), Figure 4, Figure 5

---

## 10. Methodology

1. Extract 4 academic cohorts (SY 2015–2016 to SY 2018–2019) from TIP databases.
2. Survey alumni using Google Forms with informed privacy consent to obtain ground-truth employment landing labels.
3. Merge academic GPA, OJT ratings, and mock interview scores into a consolidated dataset.
4. Train Decision Trees, Random Forest, and Support Vector Machines.
5. Compute validation curves across gamma values to establish stability against overfitting.
6. Evaluate comparative classification performance across Accuracy, Precision, Recall, and F1-score.

### Source Evidence
- **Page**: PDF p. 3–5 (PDF pp. 3–5)
- **Section**: Section IV, Section V

---

## 11. Experimental Setup

- **Software / Platform**: Python machine learning libraries (Scikit-learn).
- **Institution**: Technological Institute of the Philippines - Manila.
- **Dataset Scale**: 3,000 samples $\times$ 9 attributes.

### Source Evidence
- **Page**: PDF p. 3 (PDF p. 3)
- **Section**: Section IV

---

## 12. Evaluation Metrics

- Accuracy: $\text{Accuracy} = \frac{TP + TN}{TP + FN + TN + FP}$
- Sensitivity / Recall: $\text{Recall} = \frac{TP}{TP + FN}$
- Specificity: $\text{Specificity} = \frac{TN}{TN + FP}$
- Positive Predictive Value (Precision): $\text{Precision} = \frac{TP}{TP + FP}$
- Negative Predictive Value (NPV): $\text{NPV} = \frac{TN}{TN + FN}$
- F1-Score: Weighted harmonic mean of Precision and Recall
- Cross-Validation Score from Validation Curves

### Source Evidence
- **Page**: PDF p. 4 (PDF p. 4)
- **Section**: Formulas 1–5, Table 5

---

## 13. Results

Reported comparative model performance metrics exactly as documented in Table 5 (PDF p. 4):

| Algorithm | Accuracy (%) | Recall (%) | Precision (%) | F1-Score (%) |
|:---|:---:|:---:|:---:|:---:|
| **Support Vector Machine (SVM)** | **91.22%** | **91.15%** | **91.00%** | **91.00%** |
| **Decision Tree (DT)** | 84.50% | 85.00% | 85.00% | 85.00% |
| **Random Forest (RF)** | 84.00% | 84.00% | 84.00% | 84.00% |

### Validation Curve Analysis (PDF p. 5):
- SVM with RBF kernel achieved a maximum training $R^2$ score of 0.912 and a maximum cross-validation score of **0.909** (at gamma range 10 to 100).
- Proved that the SVM model generalized cleanly without overfitting or underfitting.

### Source Evidence
- **Page**: PDF p. 4–5 (PDF pp. 4–5)
- **Table**: Table 5 ("Comparison of Learning Models Performance"), Figure 4, Figure 5

---

## 14. Baselines

Decision Tree (84.5% accuracy) and Random Forest (84.0% accuracy) served as baseline classifiers against the proposed tuned Support Vector Machine (91.22%).

---

## 15. Ablation Study

Hyperparameter sensitivity was evaluated through systematic gamma validation curves (Figures 4 and 5), demonstrating optimal performance within the $\gamma \in [10, 100]$ interval.

---

## 16. Explainability

Explainability was handled at the institutional level by linking model predictions back to the 3 institutional data sources: identifying whether low mock interview scores or weak OJT supervisor ratings pushed a student into the "Less Employable" class.

---

## 17. Main Findings

1. **SVM Superiority on Institutional Feature Space**: Support Vector Machine achieved 91.22% accuracy, outperforming Random Forest (84%) and Decision Trees (84.5%) on the 9-feature institutional dataset.
2. **Value of Multi-Department Data Integration**: Merging Career Center mock interview ratings with OJT internship ratings and Registrar GPA provided a significantly stronger predictive signal than academic GPA alone.
3. **Cross-Validation Stability**: Tuned SVM with RBF kernel achieved a cross-validation score of 0.909, confirming robust generalization on engineering student cohorts.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Single Institutional Scope**: The study was restricted to engineering programs at the Technological Institute of the Philippines - Manila.
- **Limited Feature Count**: The analysis used 9 features; granular competency-level skill breakdowns were not decomposed in the initial model.

### 18.2 Research Interpretation
- *Research team interpretation*: The paper describes the dataset size ($N = 3,000$) and performance metrics clearly, but does not report the exact train/test sample partition counts or detailed confusion matrix counts.

---

## 19. Future Work

Explicitly proposed by the authors:
1. Analyze specific skillsets to identify which technical and soft-skill attributes yield the highest feature importance weights.
2. Deploy the trained SVM model into an operational institutional early-warning software system to guide at-risk engineering students before graduation.
3. Validate the system in real-world deployment across additional engineering disciplines.

### Source Evidence
- **Page**: PDF p. 5 (PDF p. 5)
- **Section**: Section V (Conclusion and Future Work)

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Relevant PRIE Module**: `01_Employability`, `02_Prediction`, and `05_Mock_Interview`.
- **Architectural Validation**: Demonstrates that mock job interview ratings and internship performance are vital features for employability prediction, confirming PRIE's core architecture of combining mock interview paralinguistics with academic tracking.
- **Feature Pipeline Confirmation**: Supports PRIE's automated ingestion of diverse institutional signals (interview scores, project ratings, GPA) into a unified intelligence engine.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Top Model Performance (SVM 91.22%) | SVM achieved 91.22% accuracy, 91.15% recall, 91.00% precision, 91.00% F1 | PDF p. 4, Table 5 | Experimental result |
| High Cross-Validation Score (0.909) | Maximum cross-validation score of 0.909 at $\gamma \in [10, 100]$ | PDF p. 5, Section V | Experimental result |
| Sample Size & Dimension | 3,000 engineering student records across 9 features (27,000 data points) | PDF p. 3, Section IV | Direct statement |
| Multi-Source Institutional Ingestion | Combined Career Center mock interviews, OJT ratings, and Registrar GPA | PDF p. 3, Section IV-A | Methodology |
| Baseline Comparisons | Decision Tree achieved 84.5% accuracy; Random Forest achieved 84.0% | PDF p. 4, Table 5 | Experimental result |

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

**VERIFIED** (Fully verified from primary PDF source: `Paper09_casuat2021predicting.pdf`, 5 pages).
