# Paper 10 — A Machine Learning Approach for Tracking and Predicting Student Performance in Degree Programs

## 1. Bibliographic Information

- **Paper ID**: Paper10
- **Full Title**: A Machine Learning Approach for Tracking and Predicting Student Performance in Degree Programs
- **Authors**: Student Project Team (Bachelor of Technology in Computer Science and Engineering), under the guidance of Dr. Raj Kumar Patra (Assistant Professor)
- **Affiliation**: Department of Computer Science and Engineering (Affiliated Engineering Institution, India)
- **Year**: 2022
- **Document Type**: Bachelor of Technology Mini Project Report / Academic Engineering Capstone Monograph
- **Cataloged Reference**: In legacy bibliography cataloged as *Rao, Venkatesh & Swamy, K. (2022). Student Performance Prediction System: A Comparative Machine Learning Benchmark*
- **PDF filename**: `Paper10_rao2022student.pdf`
- **PDF path**: `01_Research_Foundation/Papers/PDFs/Paper10_rao2022student.pdf`
- **Page count**: 53 pages

---

## 2. Research Problem

Traditional institutional tracking of student academic performance relies primarily on manual attendance books, periodic paper records, and post-semester grading reports. These static methods prevent academic advisors and educators from detecting at-risk students early enough to intervene before formal examinations. While digital educational platforms collect substantial student background and engagement records, educational institutions require modular, web-deployable machine learning frameworks capable of ingesting diverse student features (demographics, family support, study habits, internal grades) and outputting automated performance classifications and early warnings.

### Source Evidence
- **Page**: PDF p. 4, 9–10 (PDF pp. 4, 9–10)
- **Section**: Abstract, Section 1.1 (Project Scope), Section 1.2 (Project Purpose)

---

## 3. Research Objectives

The authors explicitly define the following project objectives:
1. Design and develop a web-based educational predictive decision support system using the Django framework.
2. Implement and benchmark multiple supervised machine learning algorithms (Random Forest, Linear SVM, Gradient Boosting, XGBoost) to classify student academic trajectories.
3. Feature-engineer student demographic, familial, behavioral, and formative test attributes derived from student records.
4. Establish an automated administrative interface allowing institutional personnel to upload student datasets, train models, inspect performance comparison graphs, and generate individual student performance predictions with targeted warning alerts.

### Source Evidence
- **Page**: PDF p. 4, 9–10 (PDF pp. 4, 9–10)
- **Section**: Abstract, Section 1.3 (Project Features)

---

## 4. Research Questions

Not formulated as theoretical academic research questions; structured around engineering design and comparative classifier requirements for degree program tracking.

---

## 5. Dataset

- **Dataset name**: Student Academic and Demographic Performance Benchmark Dataset (adapted from the UCI Student Performance benchmark / institutional format)
- **Dataset source**: Academic records comprising secondary school background, family indicators, lifestyle attributes, and period examination marks
- **Target variable**: `FinalResult` (Binarized / Multi-class: "Good" vs. "Poor" / At-Risk)
- **Features count**: 20 distinct predictor attributes
- **Data preprocessing protocol**: Dropped target column (`FinalResult`), converted to NumPy array, scaled using `StandardScaler`, randomly shuffled, and partitioned into train/test splits.

### Source Evidence
- **Page**: PDF p. 12, 29, 32 (PDF pp. 12, 29, 32)
- **Section**: Literature Survey (Datasets), Section 4.1 (Source Code - View.py)

---

## 6. Features

The system implements a 20-attribute feature schema (directly verified from `View.py`, PDF p. 32):

### Academic & Historical Scores
- `score1`: First period continuous assessment mark ($G1$)
- `score2`: Second period continuous assessment mark ($G2$)
- `score3`: Third period / preliminary examination mark ($G3$)
- `failure`: Number of past class failures ($0 \le n \le 4$)

### Demographic & Family Background
- `gender`: Student gender (Binary: M/F)
- `age`: Student age (Years)
- `mother`: Mother's educational level ($0–4$ scale)
- `father`: Father's educational level ($0–4$ scale)
- `guardian`: Student guardian (Mother / Father / Other)
- `family`: Family educational support (`famsup`: Yes/No)

### Study Habits & Attendance
- `study`: Weekly study time commitment ($1–4$ scale)
- `school`: Extra school educational support (`schoolsup`: Yes/No)
- `paid`: Extra paid private tutoring classes (Yes/No)
- `absent`: Total number of school absences (Days)

### Lifestyle & Psychosocial Factors
- `reason`: Reason for choosing school/course (Home, Reputation, Course, Other)
- `activity`: Extracurricular activities participation (Yes/No)
- `internet`: Internet access at home (Yes/No)
- `free`: Free time after school (1–5 Likert scale)
- `out`: Going out with friends (1–5 Likert scale)
- `health`: Current health status (1–5 Likert scale)

### Source Evidence
- **Page**: PDF p. 32 (PDF p. 32)
- **Section**: Section 4.1 (`View.py`, `PredictPerformanceAction`)

---

## 7. Data Preprocessing

The Python implementation explicitly executes the following preprocessing pipeline (PDF p. 29):
```python
dataset.drop(['FinalResult'], axis=1, inplace=True)
X = dataset.values
sc = StandardScaler()
X = sc.fit_transform(X)
indices = np.arange(X.shape[0])
np.random.shuffle(indices)
```
- Categorical features are encoded using `LabelEncoder`.
- Feature matrix is standardized to zero mean and unit variance using Scikit-Learn `StandardScaler`.
- Random index permutation is applied for shuffle-split cross-validation.

### Source Evidence
- **Page**: PDF p. 29 (PDF p. 29)
- **Section**: Section 4.1 (Source Code)

---

## 8. Algorithms and Models

The application implements four supervised classification algorithms in Scikit-Learn and XGBoost:
1. **Random Forest Classifier**:
   - Implementation: `RandomForestClassifier(n_estimators=1)` / tuned bagging ensemble.
2. **Support Vector Classifier (SVM)**:
   - Implementation: `svm.SVC(C=1.0, kernel="linear")`.
3. **Gradient Boosting Classifier**:
   - Implementation: Scikit-learn `GradientBoostingClassifier()`.
4. **Extreme Gradient Boosting (XGBoost)**:
   - Implementation: `XGBClassifier()`.

### Source Evidence
- **Page**: PDF p. 28, 30, 35 (PDF pp. 28, 30, 35)
- **Section**: Section 4.1 (`View.py`)

---

## 9. Architecture

The system utilizes a Model-View-Template (MVT) Django Web Application Architecture:
1. **User / Client Layer**: Web browser interface (`LoadDataset.html`, `PredictPerformance.html`, `ViewTrain.html`).
2. **Django Controller Layer (`View.py`)**: Request routing, authentication (`AdminLoginAction`), dataset ingestion (`UploadDataset`), and model execution (`TrainML`, `PredictPerformanceAction`).
3. **Machine Learning Pipeline**: Scikit-Learn preprocessing, model fitting, metric computation, and Matplotlib figure generation (encoded via base64 into HTML tables).
4. **Early Warning Rule Engine**: Generates automated intervention banners (e.g., `"Warning! Need more focus & hardwork"`) when predictions classify a student as "Poor".

### Source Evidence
- **Page**: PDF p. 14, 27–36 (PDF pp. 14, 27–36)
- **Figure**: Figure 3.1 ("Project Architecture", PDF p. 14)

---

## 10. Methodology

1. Define system requirements and design UML structural models (Use Case, Class, Sequence, Activity diagrams, PDF pp. 15–26).
2. Develop full-stack web application in Python/Django.
3. Ingest multi-attribute student dataset; apply standard scaling and label encoding.
4. Train four classifiers (Random Forest, SVM, Gradient Boosting, XGBoost).
5. Compute precision, recall, F1-score, and accuracy across all four models; plot comparative bar charts using Matplotlib.
6. Deploy interactive inference module accepting individual student profile inputs and generating immediate risk status.
7. Conduct software testing across unit, integration, and functional test cases (Section 6, PDF pp. 40–42).

### Source Evidence
- **Page**: PDF p. 14–42 (PDF pp. 14–42)
- **Section**: Section 3 (System Design), Section 4 (Implementation), Section 6 (Testing)

---

## 11. Experimental Setup

- **Language & Framework**: Python 3.x, Django Web Framework.
- **Machine Learning Stack**: Scikit-learn (`StandardScaler`, `recall_score`, `f1_score`, `accuracy_score`), XGBoost, NumPy, Pandas.
- **Visualization**: Matplotlib (renders in-memory PNGs encoded via Base64/BytesIO to dynamic HTML templates).
- **Storage**: SQLite relational database.

### Source Evidence
- **Page**: PDF p. 27–28, 35 (PDF pp. 27–28, 35)
- **Section**: Section 4.1

---

## 12. Evaluation Metrics

- Classification Accuracy: $\text{Accuracy} = \frac{TP + TN}{TP + FN + TN + FP}$
- Precision: $\text{Precision} = \frac{TP}{TP + FP}$
- Recall: $\text{Recall} = \frac{TP}{TP + FN}$
- F1-Score: Harmonic mean of precision and recall
- Software Test Cases Passed (Table 6.3.1, 6.3.2)

### Source Evidence
- **Page**: PDF p. 28, 34–35, 41–42 (PDF pp. 28, 34–35, 41–42)
- **Section**: Section 4.1, Section 6.3

---

## 13. Results

- **System Implementation**: Successfully engineered an operational end-to-end web system allowing non-technical college administrators to upload datasets, trigger batch model training, and view comparative performance bar graphs.
- **Classification Pipeline**: Verified execution of Random Forest, Linear SVM, Gradient Boosting, and XGBoost on 20 input attributes.
- **Functional Testing**: Validated 100% pass rate across test cases (Dataset uploading, feature preprocessing, model classification, and risk alert rendering, PDF pp. 41–42).
- **Screenshot Pages (PDF pp. 38–47)**: The report allocated pages 38–47 for visual runtime screenshots (`All Algorithms Performance Graph`, `Admin Dashboard`), which appear as blank bounding placeholders in the compiled PDF monograph.

### Source Evidence
- **Page**: PDF p. 34–38, 41–42 (PDF pp. 34–38, 41–42)
- **Section**: Section 4.1, Section 5 (Results), Section 6.3

---

## 14. Baselines

Linear Support Vector Machine (`SVC(kernel="linear")`) and baseline single-tree Random Forest served as comparative benchmarks against gradient boosted ensembles (Gradient Boosting and XGBoost).

---

## 15. Ablation Study

Not reported (engineering software project monograph).

---

## 16. Explainability

Explainability is handled at the **application rule layer**:
- When a student is classified into the "Poor" performance class, the system triggers a localized warning notification: `"Warning! Need more focus & hardwork"`, displaying the student's roll number and predicted status on the institutional portal.

### Source Evidence
- **Page**: PDF p. 33 (PDF p. 33)
- **Section**: Section 4.1 (`PredictPerformanceAction`)

---

## 17. Main Findings

1. **Practical Web Engineering Feasibility**: Demonstrates that educational data mining models can be integrated into standard Django web platforms with automated in-memory graph rendering for institutional users.
2. **20-Feature Holistic Input Space**: Reaffirms that tracking degree completion requires combining academic marks (G1, G2, G3) with non-academic indicators (parental education, study time, absences, health, and lifestyle).
3. **Software Architecture Completeness**: Provides detailed UML design blueprints (Use Case, Class, Sequence, Activity diagrams) for building institutional performance tracking tools.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Monograph Nature**: Developed as an academic undergraduate capstone project rather than a multi-institutional randomized controlled trial.
- **Missing Printed Result Graphics**: Pages 38–47 in the compiled PDF contain blank image frames where GUI output screenshots were omitted during PDF generation.

### 18.2 Research Interpretation
- *Research team interpretation*: The report contains the complete Python/Django source code and UML architecture, but numerical precision and recall decimals are generated dynamically at runtime within the Django view rather than printed as a static text table in the monograph.

---

## 19. Future Work

Explicitly proposed by the authors:
1. Integrate time-series analysis to model continuous grade trajectories across multi-year degree programs.
2. Incorporate Natural Language Processing (NLP) to parse student qualitative feedback and sentiment.
3. Implement privacy-preserving machine learning frameworks to ensure compliance with student data regulations (e.g., FERPA, GDPR).

### Source Evidence
- **Page**: PDF p. 14, 51 (PDF pp. 14, 51)
- **Section**: Literature Survey (Summary), Section 7.2 (Future Scope)

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Relevant PRIE Module**: `02_Prediction`, `08_Learning_Analytics`, and overall system engineering.
- **Architectural Link**: Provides concrete software implementation patterns for integrating Scikit-Learn/XGBoost pipelines into web controllers, illustrating how real-time inference can be triggered via POST requests from student dashboards.
- **Feature Benchmark**: Confirms the utility of the 20-attribute UCI student performance schema as a baseline for academic tracking within PRIE.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Document Characterization | Bachelor of Technology Computer Science and Engineering Capstone Report | PDF p. 1–3 | Direct statement |
| 20 Feature Schema | Inputs: gender, age, Medu, Fedu, reason, guardian, studytime, failures, etc. | PDF p. 32, Section 4.1 | Methodology / Code |
| Algorithms Implemented | Code confirms RF, Linear SVM, Gradient Boosting, and XGBoost | PDF p. 30, 35, Section 4.1 | Methodology / Code |
| Django MVT Architecture | Complete View.py implementation with dynamic Matplotlib base64 plots | PDF p. 27–36, Section 4.1 | Figure / Architecture |
| Early Warning Alert Rule | Generates "Warning! Need more focus & hardwork" for at-risk students | PDF p. 33, Section 4.1 | Methodology / Code |
| Test Case Verification | Table 6.3.1 and 6.3.2 document functional and integration testing pass | PDF p. 41–42, Section 6.3 | Experimental result |

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

**VERIFIED** (Fully verified from primary PDF source: `Paper10_rao2022student.pdf`, 53 pages).
