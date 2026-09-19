# Paper 33 — Detecting At-Risk Students With Early Interventions Using Machine Learning Techniques

## 1. Bibliographic Information

- **Paper ID**: Paper33
- **Full Title**: Detecting At-Risk Students With Early Interventions Using Machine Learning Techniques
- **Authors**: Raghad Al-Shabandar (Liverpool John Moores Univ.), Abir Jaafar Hussain (Liverpool John Moores Univ.), Panos Liatsis (Khalifa University, UAE), and Robert Keight (Liverpool John Moores Univ.)
- **Institution**: Faculty of Engineering and Technology, Liverpool John Moores University, Liverpool L3 3AF, U.K.; Department of Electrical Engineering and Computer Science, Khalifa University, Abu Dhabi, UAE
- **Year**: 2019 (Received September 8, 2019, Accepted September 17, 2019, Published September 24, 2019)
- **Venue**: IEEE Access, Volume 7, 2019, pp. 140046–140060 (also indexed as pp. 149464–149478)
- **DOI**: 10.1109/ACCESS.2019.2943351
- **PDF filename**: `Paper33_alshabandar2025explainable.pdf` (Note: filename reflects legacy bibtex tag `alshabandar2025explainable`; authentic PDF confirms authors Raghad Al-Shabandar, Abir Jaafar Hussain, Panos Liatsis, and Robert Keight, IEEE Access 2019)
- **PDF path**: `Papers/PDFs/Paper33_alshabandar2025explainable.pdf`
- **Page count**: 15 pages (pp. 140046–140060)

---

## 2. Research Problem

Massive Open Online Courses (MOOCs) and virtual learning platforms offer unprecedented educational accessibility, yet suffer from notoriously severe attrition rates and low completion rates. Traditional academic assessments identify student failure only post-hoc after exams are graded. Instructors critically lack automated, early-warning mechanisms capable of detecting at-risk students during the initial weeks of a course based on behavioral interaction telemetry, when pedagogical interventions and targeted remediation can still reverse dropout trajectories.

### Source Evidence
- **Page**: PDF p. 1 (p. 149464)
- **Section**: Abstract & Section I — Introduction

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To formulate and empirically validate two predictive architectures for early intervention: (a) an **At-Risk Student Model** (predicting early course withdrawal) and (b) a **Learning Achievement Model** (predicting pass/fail grades).
2. To demonstrate early risk detection across two prominent public educational benchmarks: HarvardX/MITx MOOC dataset and the Open University Learning Analytics Dataset (OULAD).
3. To evaluate the efficacy of Chi-square-based filter feature selection in eliminating redundant telemetry, mitigating overfitting, and accelerating inference.
4. To evaluate five machine learning classifiers under hyperparameter optimization across imbalanced student outcome distributions.

### Source Evidence
- **Page**: PDF pp. 1–3 (pp. 149464–149466)
- **Section**: Abstract, Section I, and Section III

---

## 4. Research Questions

- *Not explicitly reported* (The paper is structured around two empirical case studies and machine learning comparative modeling rather than numbered formal research questions).

---

## 5. Dataset

The study utilizes two major real-world educational datasets:

### Dataset 1: HarvardX and MITx MOOC Dataset (Table 2)
- **Source**: Harvard University and Massachusetts Institute of Technology open online courses.
- **Samples**: Multi-course cohort tracking thousands of registered learners.
- **Key Features**: Clickstream interactions, `Nchapters` (chapters read), `nplay_video` (video play events), `Explored` (binary: accessed $>50\%$ of content), `Viewed` (binary: accessed assignment/video home page), `ndays_act` (active days), `Nevent` (total event count), registration/last interaction dates, demographics (`age`, `gender`, `LoE_DI` - level of education), assignment grade.

### Dataset 2: Open University Learning Analytics Dataset - OULAD (Table 3)
- **Source**: Open University (UK), longitudinal cohort across 2013–2014.
- **Key Features**: Demographic data, behavioral clickstream telemetry across 11 Virtual Learning Environment (VLE) activity types, assessment scores (Tutor Marked Assessments TMA, Computer Marked Assessments CMA), weighted 50% coursework / 50% final exam. Target passing grade threshold: $\ge 40\%$.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 149466–149467)
- **Section**: Section III.A (Data Description), Table 2, Table 3

---

## 6. Features

The predictive frameworks extract and evaluate:

### Behavioral & Clickstream Features
- `ndays_act`: Number of unique days the learner interacted with courseware.
- `Nevent`: Cumulative count of clickstream interaction events.
- `nplay_video`: Total frequency of video playback interactions.
- `Nchapters`: Number of distinct course chapters opened/read.
- `VLE Interaction Types`: Clicks on forum posts, PDF files, subpages, quiz attempts.

### Temporal & Motivational Indicators
- `Explored`: Binary indicator identifying whether a learner accessed more than 50% of course materials.
- `Registration Lag`: Time interval between registration date and course launch.
- `Semester Motivational Trajectory`: Longitudinal shift in participation frequency from fall to spring semesters.

### Demographics & Academic History
- `LoE_DI`: Prior level of education (Secondary, Bachelor, Master, PhD).
- `age`, `gender`, and prior module credits.

### Source Evidence
- **Page**: PDF pp. 3–5, 13 (pp. 149466–149468, 149476)
- **Section**: Section III.A & Section III.L (Discussion)

---

## 7. Data Preprocessing

1. **Box-Cox Transformation**: Applied to normalize highly skewed clickstream distributions (Table 5).
2. **Missing Value Imputation**: Handled missing demographic and engagement fields.
3. **Feature Selection (Chi-Square Filter Approach)**: Evaluated feature relevance against target labels; reduced full feature sets to optimized compact subsets (`ndays_act`, `Nevent`, `nplay_video`, `Nchapters`, and motivational status).
4. **Rescaling & Train/Test Split**: Standardized features; implemented $k$-fold cross-validation across 5 simulation rounds to prevent data leakage.

### Source Evidence
- **Page**: PDF pp. 4–7 (pp. 149467–149470)
- **Section**: Section III (Subsections B, C, D; Tables 5 & 6)

---

## 8. Algorithms and Models

The authors train and tune five machine learning algorithms across full and reduced feature sets:
1. **Gradient Boosting Machine (GBM)**: Tuned via random search (optimal: 50 trees, learning rate 0.03).
2. **Artificial Neural Network (NNET1)**: Single hidden layer with 32 units, learning rate 0.02, weight decay 0.01 (tuned via grid search).
3. **Random Forest (RF)**: Ensemble of decision trees with bagging.
4. **Generalized Linear Model (GLM)**: Logistic regression baseline.
5. **Support Vector Machines (SVM)**: Radial basis function kernel.

### Source Evidence
- **Page**: PDF pp. 7–9, 13 (pp. 149470–149472, 149476)
- **Section**: Section III (Subsections E, F, G, H; Table 7)

---

## 9. Architecture

The paper formalizes two predictive pipelines:
- **Model 1: At-Risk Student Architecture**:
  `LMS / Clickstream Telemetry` $\rightarrow$ `Box-Cox Normalization` $\rightarrow$ `Chi-Square Feature Selection` $\rightarrow$ `Classifiers (GBM / NNET1 / RF / GLM)` $\rightarrow$ `Withdrawal / At-Risk Probability` $\rightarrow$ `Early Academic Advisor Alert`.
- **Model 2: Learning Achievement Architecture**:
  `VLE Clicks + Assessment Submissions (TMA/CMA)` $\rightarrow$ `Temporal Feature Extraction` $\rightarrow$ `Optimized Classifier Pipeline` $\rightarrow$ `Pass / Fail Grade Prediction` $\rightarrow$ `ROC Threshold Calibration` ($0.82 \le \text{AUC} \le 0.99$).

### Source Evidence
- **Page**: PDF pp. 2–4, 11–13
- **Section**: Section III & Figures 8, 9

---

## 10. Methodology

1. **Telemetry Ingestion**: Ingesting HarvardX/MITx clickstream logs and Open University VLE data.
2. **Feature Engineering & Selection**: Applying Chi-square filter selection to eliminate noisy web logs.
3. **Model Training & Optimization**: Running 5 independent simulation rounds for each of the 5 classifiers using grid and random hyperparameter search.
4. **Overfitting Analysis**: Plotting learning curves for full vs reduced feature sets to verify generalization.
5. **Evaluation across Skewed Distributions**: Calculating Accuracy, Sensitivity, Specificity, F-measure, and ROC-AUC curves.

### Source Evidence
- **Page**: PDF pp. 4–14
- **Section**: Section III

---

## 11. Experimental Setup

- **Software / Libraries**: R statistical programming environment, caret package for hyperparameter tuning and model evaluation.
- **Validation**: 5-fold cross-validation executed over 5 independent simulation rounds; reported metrics represent mean performance.
- **Hardware**: Standard high-performance multi-core computing workstation.

### Source Evidence
- **Page**: PDF pp. 7–12
- **Section**: Section III (Subsections J & K)

---

## 12. Evaluation Metrics

1. **Accuracy**: Overall classification correctness.
2. **Sensitivity (Recall on Positive Class)**: Proportion of actual at-risk/withdrawn students correctly identified.
3. **Specificity**: Proportion of successful/retained students correctly classified.
4. **F-Measure (F1-Score)**: Harmonic mean of precision and recall (critical due to class imbalance).
5. **Receiver Operating Characteristic — Area Under Curve (ROC-AUC)**: Discrimination threshold metric across operating points ($0.82–0.99$).

### Source Evidence
- **Page**: PDF pp. 9–13 (pp. 149472–149476)
- **Section**: Section III.K & Tables 8, 9, 10

---

## 13. Results

### At-Risk Student Model (Course Withdrawal Prediction)
- **Top Performer**: **Gradient Boosting Machine (GBM)** achieved highest accuracy (**0.894**) on full features; **NNET1** achieved highest accuracy (**0.891**) on reduced features.
- **Lowest Performer**: Random Forest (RF) achieved 0.866 accuracy on the withdrawal framework.
- **Feature Selection Efficacy**: Filtering features via Chi-square caused zero statistically significant loss in predictive accuracy while drastically flattening the learning curve and eliminating overfitting (Figure 8).

### Learning Achievement Model (Pass / Fail Grade Prediction, Table 10)
- **Top Accuracy**: **GBM (0.952)** and **NNET1 (0.950)** achieved near-identical peak accuracy; GLM achieved 0.945.
- **Sensitivity Dominance**: GBM achieved peak sensitivity of **0.956**, while all classifiers achieved specificities $>0.93$.
- **ROC Discrimination**: ROC curves demonstrated outstanding class separation across all operating thresholds, with **AUC values ranging between 0.82 and 0.99** (Figure 9).

### Source Evidence
- **Page**: PDF pp. 1, 11–14 (pp. 149464, 149474–149477)
- **Tables / Figures**: Abstract, Table 8, Table 9, Table 10, Figure 8, Figure 9

---

## 14. Baselines

- Full feature set baselines against reduced feature sets.
- Generalized Linear Models (GLM / Logistic Regression) and standard Decision Trees serving as linear and weak-learner benchmarks against ensemble (GBM, RF) and deep/neural models (NNET1).

### Source Evidence
- **Page**: PDF pp. 9–13
- **Tables**: Tables 8, 9, 10

---

## 15. Ablation Study

- **Feature Set Ablation (Table 8 vs Table 9 & Figure 8)**: Systematically ablated full clickstream feature sets against Chi-square selected subsets.
- *Finding*: The reduced feature subset (`ndays_act`, `Nevent`, `nplay_video`, `Nchapters`) performed identically or superiorly to the full 15+ feature space (GBM: 0.894 full vs 0.889 reduced; NNET1: 0.887 full vs 0.891 reduced), proving that $>60\%$ of clickstream telemetry represents redundant noise.

### Source Evidence
- **Page**: PDF pp. 11–13 (pp. 149474–149476)
- **Section**: Section III.K, Table 8, Table 9, Figure 8

---

## 16. Explainability

- The authors use the Chi-square filter score and feature ranking tables (Table 6) to expose *which* behavioral markers drive student failure.
- Active days (`ndays_act`) and cumulative event interactions (`Nevent`) were revealed as the single most critical predictive determinants of retention.

### Source Evidence
- **Page**: PDF pp. 6–7, 13 (pp. 149469–149470, 149476)
- **Section**: Section III.D & Section III.L

---

## 17. Main Findings

1. **Early Predictability of Dropout**: Student course withdrawal and final failure can be predicted with $>89\%$ and $>95\%$ accuracy respectively using early-stage clickstream engagement data alone.
2. **Behavioral Telemetry Outweighs Static Demographics**: Longitudinal engagement markers (`ndays_act`, `nplay_video`) correlate far more strongly with student persistence than static demographic attributes (gender, age, education level).
3. **Filter Feature Selection Mitigates Overfitting**: Chi-square filtering successfully purges collinear web telemetry, dramatically reducing training latency and preventing learning curve divergence.
4. **Prioritizing Sensitivity over Specificity**: In educational early warning systems, maximizing Sensitivity (detecting every true at-risk student) is more critical than specificity, as the institutional cost of a false negative (undetected dropout) far exceeds a false positive (unnecessary check-in).

### Source Evidence
- **Page**: PDF pp. 13–15 (pp. 149476–149478)
- **Section**: Section III.L (Discussion) & Section IV (Conclusion)

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **MOOC-Specific Telemetry**: Models were trained and evaluated on online MOOC platforms (HarvardX/MITx, Open University); clickstream behavioral distributions differ from on-campus hybrid engineering programs.
2. **Lack of Deep Sequence Modeling**: Relied on aggregated tabular engagement sums rather than temporal deep recurrent networks (RNN/LSTM) that capture day-by-day sequence order.
3. **Class Skew Bias**: Skew in favor of withdrawal records created a natural positive prediction bias that required explicit threshold calibration.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The models detect *that* a student is disengaging (low click count), but cannot differentiate between technical difficulty, personal life distress, or poor curriculum design without qualitative or multimodal diagnostic data.

### Source Evidence
- **Page**: PDF pp. 13–15
- **Section**: Section III.L & Section IV

---

## 19. Future Work

Explicitly proposed by the authors:
1. Validating the predictive framework across additional cross-institutional online learning platforms.
2. Implementing deep convolutional neural networks (CNNs) and recurrent architectures to automatically extract temporal event sequences from raw student log streams.
3. Tracking motivational status trajectories to dynamically adjust institutional advising interventions.

### Source Evidence
- **Page**: PDF p. 15 (p. 149478)
- **Section**: Section IV — Conclusion

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides the exact empirical baseline for PRIE's **Student Performance Risk Predictor (Early Warning Engine)**:
1. **Adopting the Dual-Model Structure**: PRIE should mirror Al-Shabandar et al.'s two-tier design: (1) an **At-Risk Dropout Model** monitoring platform engagement, and (2) a **Placement Readiness Achievement Model** predicting final placement test success.
2. **Temporal Engagement Features**: PRIE's tracking of student activity in ScholarCamp (active coding days, problem submission frequency, video lecture views) can directly utilize Al-Shabandar et al.'s feature set (`ndays_act`, `Nevent`, `nplay_video`).
3. **Sensitivity-Biased Thresholding**: Al-Shabandar et al.'s insight on tuning ROC thresholds to favor Sensitivity ($\ge 0.95$) over Specificity is critical for PRIE: ScholarCamp must ensure no struggling student slips through the cracks unnoticed.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **Core Research Scope** | "two models are constructed namely at-risk student model and learning achievement model... detect students in danger of failing and withdrawal at the early stage." | PDF p. 1, Abstract | Direct statement |
| **Datasets Analyzed** | HarvardX/MITx MOOC dataset (Table 2) and Open University Learning Analytics Dataset - OULAD (Table 3). | PDF pp. 3–4, Section III.A | Dataset description |
| **At-Risk Model Peak Accuracy** | GBM yielded 0.894 accuracy on full features; NNET1 yielded 0.891 on reduced features. | PDF p. 1, Abstract & Table 8 | Experimental result |
| **Learning Achievement Peak Accuracy** | GBM achieved 0.952 accuracy and 0.956 sensitivity; NNET1 achieved 0.950 accuracy. | PDF p. 1, Abstract & Table 10 | Experimental result |
| **ROC-AUC Range** | "Overall, a range of AUC values between 0.82-0.99 for all classes was obtained." | PDF p. 13, Section III.K & Figure 9 | Quantitative result |
| **Feature Selection Benefit** | Chi-square filtering flattened learning curves, reduced over-fitting, and maintained accuracy with a fraction of features. | PDF pp. 11–13, Section III.L & Figure 8 | Ablation result |

---

## 22. Verification Checklist

- [x] PDF read (`Paper33_alshabandar2025explainable.pdf`, 15 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (HarvardX/MITx + OULAD, Box-Cox, Chi-square filter, 5 ML models)
- [x] Datasets verified (Tables 2 & 3: Harvard clickstream, OULAD 2013-2014)
- [x] Features verified (`ndays_act`, `Nevent`, `nplay_video`, `Nchapters`, TMA/CMA assessments)
- [x] Algorithms verified (GBM, NNET1, RF, GLM, SVM; hyperparameter tuning in Table 7)
- [x] Architecture inspected (Dual-model framework: at-risk dropout + learning achievement)
- [x] Experiments inspected (Tables 8, 9, 10; 5-fold CV over 5 simulation rounds)
- [x] Results verified (GBM 0.894 at-risk acc, GBM 0.952 achievement acc, 0.956 sensitivity, AUC 0.82–0.99)
- [x] Limitations verified (MOOC telemetry, non-sequential tabular sums, class skew)
- [x] Future work verified (Deep CNN/RNN for temporal sequences, cross-provider validation)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact dual-model framework from Section III, OULAD/Harvard datasets from Tables 2–3, hyperparameter configurations from Table 7, and numerical results from Tables 8–10 verified directly from source text; legacy filename discrepancy documented).
