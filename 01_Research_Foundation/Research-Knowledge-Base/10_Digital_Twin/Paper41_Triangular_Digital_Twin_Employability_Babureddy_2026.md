# Paper 41 — A Triangular Employability Digital Twin Framework for Explainable Graduate Career Readiness Prediction through Student–Faculty–Industry Intelligence

## 1. Bibliographic Information

- **Paper ID**: Paper41
- **Full Title**: A Triangular Employability Digital Twin Framework for Explainable Graduate Career Readiness Prediction through Student–Faculty–Industry Intelligence
- **Authors**: Babureddy N S (1, 2), Binoy Mathew (2)
  - *(1) Research Scholar, Department of Management Studies (MBA), VTU Centre for Post Graduate Studies, Muddenahalli, Chikkaballapur, Visvesvaraya Technological University, Belagavi, Karnataka, India; and Head HR, Department of HRD, R L Jalappa Group of Institutions, Doddaballapur, India*
  - *(2) Associate Professor, Department of Management Studies (MBA), VTU Centre for Post Graduate Studies, Muddenahalli, Chikkaballapur, Visvesvaraya Technological University, Belagavi, Karnataka, India*
  - *Emails: babureddyns@gmail.com, drbinoymathew@gmail.com, binoymathew@vtu.ac.in*
- **Year**: 2026 (Received 10 February 2026, Revised 26 March 2026, Accepted 12 April 2026; Volume 3(1s), pp. 977–1002)
- **Venue**: Journal of Intelligent Decision Making and Information Science (JIDMIS), eISSN: 3079-0875 (www.jidmis.org)
- **DOI**: *Not explicitly reported / None assigned by journal*
- **PDF filename**: `Paper41_consortium2026triangular.pdf`
- **PDF path**: `Papers/PDFs/Paper41_consortium2026triangular.pdf`
- **Page count**: 26 pages
- **Metadata Note / Discrepancy**: The PDF filename indicates `consortium2026triangular`, but the actual printed authors on PDF p. 1 are Babureddy N S and Binoy Mathew from Visvesvaraya Technological University (VTU), Karnataka, India.

## 2. Research Problem

Conventional graduate employability prediction frameworks in machine learning suffer from fundamental systemic limitations: they treat employability as a narrow, student-centric classification problem, relying exclusively on learner academic metrics (such as CGPA) while completely neglecting the vital influence of faculty mentoring and industry collaboration. Furthermore, traditional assessment methods are point-in-time and static, failing to model the evolving academic lifecycle or provide counterfactual intervention simulations that explain how specific institutional interventions (e.g., targeted soft-skill coaching or mentorship) directly uplift a student's career readiness.

### Source Evidence
- PDF p. 1–3, Abstract, Section 1 — Introduction & Section 2 — Problem Statement and Objectives.

## 3. Research Objectives

1. Develop and validate a **Triangular Employability Digital Twin Framework** integrating Student, Faculty, and Industry stakeholder intelligence into a unified predictive and prescriptive architecture.
2. Construct a heterogeneous multi-relational knowledge graph connecting student competencies, faculty mentoring records, and industry hiring standards.
3. Train an explainable multiclass machine learning classifier to predict student employability readiness into Low, Medium, and High categories with high precision and recall.
4. Apply SHAP (SHapley Additive exPlanations) to identify global and local feature attributions driving career readiness.
5. Simulate prescriptive Digital Twin counterfactual interventions demonstrating individual and combined employability probability uplifts.

### Source Evidence
- PDF p. 1, Abstract; PDF p. 3–4, Section 2 — Problem Statement and Objectives.

## 4. Research Questions

The study investigates five core research dimensions:
1. How does the integration of multi-stakeholder intelligence (student, faculty, and industry) improve the accuracy and robustness of graduate employability prediction compared to student-only models?
2. What are the key structural communities and knowledge hubs that emerge from a heterogeneous Student–Faculty–Industry knowledge graph?
3. Which academic, soft-skill, and professional attributes exert the strongest feature attribution on employability outcomes?
4. How do targeted pedagogical and mentoring interventions (simulated via digital twin counterfactuals) quantify career readiness uplift?
5. How can post-hoc explainability (SHAP) provide transparent, actionable diagnostic feedback for institutional career services?

### Source Evidence
- PDF p. 1, Abstract; PDF p. 2–4, Section 1 & Section 2.

## 5. Dataset

- **Dataset Name**: Triangular Higher Education Employability Multi-Stakeholder Dataset (8 consolidated relational tables).
- **Dataset Source**: Primary empirical data collected through structured online surveys across multiple engineering, arts, and science colleges in Karnataka, India.
- **Institution**: Visvesvaraya Technological University (VTU) affiliated network and R L Jalappa Group of Institutions ecosystem.
- **Collection Period**: 2025–2026.
- **Dataset Size**: **1,000 student records** alongside corresponding linked faculty mentoring logs and industry recruiter evaluations.
- **Classes**: 3 balanced employability classes partitioned via percentile thresholding of a composite score:
  - Medium Employability: 339 students (33.9%)
  - High Employability: 331 students (33.1%)
  - Low Employability: 330 students (33.0%)
- **Target Variable**: Categorical Employability Level (`Low`, `Medium`, `High`) derived from a weighted composite employability score (ranging from 0 to 40; empirical scores distributed between 24 and 39.8).
- **Real / Synthetic**: Real survey-collected empirical institutional data.
- **Public / Private**: Private institutional survey dataset.
- **Train/Test Split**: 80/20 stratified split (800 training samples, 200 held-out test samples).

### Source Evidence
- PDF p. 1, Abstract; PDF p. 8–9, Section 4 — Methodology of Implementation; PDF p. 13–14, Section 5, Figure 3 & Figure 5.

## 6. Features

The framework engineers 12 core input features structured across three stakeholder pillars (PDF p. 8–10, Section 4.1):

### Student Pillar (Academic & Competency)
- **CGPA**: Cumulative Grade Point Average (scale 0–10).
- **SGPA**: Semester Grade Point Average.
- **Attendance Percentage**: Classroom and laboratory attendance records (55%–100%).
- **Soft Skill Competency Ratings** (self-assessed and verified across 7 dimensions on a 1–10 scale):
  - Communication Skills
  - Teamwork
  - Leadership
  - Problem-Solving
  - Critical Thinking
  - Professionalism
  - Adaptability
- **Experiential Exposure**: Internship counts and academic project participation records.

### Faculty Pillar (Mentoring & Guidance)
- **Mentoring Hours**: Total faculty guidance hours invested per student cohort.
- **Faculty Research Activity**: Research activity levels and academic involvement metrics.

### Industry Pillar (Recruitment Standards)
- **Hiring Readiness Score**: Employer assessment of graduate readiness for entry-level professional roles.
- **Skill Demand Priority**: Alignment between student technical portfolio and current industry hiring criteria.

## 7. Data Preprocessing

- **Multi-Key Relational Merging**: Merging eight discrete survey datasets across student IDs, faculty mentor IDs, and industry partner codes.
- **Data Cleansing & Validation**: Imputation and consistency validation across all 1,000 records; duplicate removal.
- **Feature Scaling**: Min-max normalization and standard scaling applied to numerical features for distance-based graph algorithms.
- **Percentile Thresholding**: Generating ground-truth labels by computing a weighted multi-attribute composite employability score and partitioning into equal terciles (Low: bottom 33%, Medium: middle 34%, High: top 33%) to guarantee perfect class balance and prevent classifier bias (PDF p. 1, 14).

## 8. Algorithms and Models

- **XGBoost Multiclass Classifier**: Primary gradient-boosted decision tree algorithm trained on the 12 engineered features for 3-class employability classification (PDF p. 1, 13–14).
- **Heterogeneous Knowledge Graph Construction**: Multi-relational graph representation mapping students, faculty mentors, skills, academic metrics, and industry roles into typed nodes and edges (PDF p. 14, Figure 4).
- **Community Detection**: **Greedy Modularity Algorithm** applied to the knowledge graph to extract structural clusters (PDF p. 1, 14).
- **Graph Centrality Metrics**: Degree centrality, betweenness centrality, and eigenvector centrality identifying key knowledge hubs.
- **SHAP (SHapley Additive exPlanations)**: TreeSHAP implementation calculating global feature importance rankings and local individual force plots (PDF p. 1, 16–17, Figure 8).
- **Counterfactual Digital Twin Simulation Engine**: Prescriptive simulation adjusting feature vectors (e.g., adding +2 points to communication or +5 hours to mentorship) to observe resulting probability transitions in the digital twin state space (PDF p. 15–16, Figure 7).

### Source Evidence
- PDF p. 1, Abstract; PDF p. 9–12, Section 4.1–4.3; PDF p. 13–17, Section 5.

## 9. Architecture

The framework is organized into **four hierarchical layers** (PDF p. 9–10, Section 4.1 & Figure 1):
1. **Layer 1: Foundational Stakeholder Pillars**: Captures raw inputs from Student, Faculty, and Industry entities.
2. **Layer 2: Integration & Knowledge Graph Layer**: Executes multi-key data merging, preprocessing, vectorization, and builds the typed heterogeneous knowledge graph (1,150 nodes, 2,908 edges).
3. **Layer 3: Digital Twin Core & Analytics Engine**: Houses the predictive machine learning models (XGBoost), community detection algorithms, and SHAP explainability processors.
4. **Layer 4: Prescriptive Decision & Simulation Layer**: Delivers student readiness dashboards, recruiter matching tools, institutional analytics, and counterfactual uplift simulation interfaces.
- **Architecture Diagram**: Figure 1 (PDF p. 10) details the complete block diagram of the four-layer implementation.

## 10. Methodology

1. **Multi-Stakeholder Survey Administration**: Distributing tailored instruments to students, faculty, and industry HR heads across Karnataka technical colleges.
2. **Data Ingestion & Integration**: Merging eight relational survey tables into a master consolidated matrix of 1,000 records.
3. **Target Label Derivation**: Formulating a composite employability index and establishing balanced tercile thresholds.
4. **Knowledge Graph Modeling**: Mapping entities into a multi-relational graph and executing greedy modularity clustering.
5. **Supervised Classifier Training**: Training an XGBoost multiclass model using 80/20 stratified cross-validation.
6. **Interpretability & Explainability**: Computing SHAP summary plots and dependence plots.
7. **Digital Twin Uplift Simulation**: Modeling counterfactual feature enhancements and measuring predicted probability shifts.

## 11. Experimental Setup

- **Platform & Libraries**: Python, XGBoost, NetworkX / graph libraries, SHAP, Scikit-learn, Pandas, Matplotlib, Seaborn.
- **Dataset Partitioning**: 800 training records (80%) and 200 held-out testing records (20%) using stratified sampling.
- **Hardware**: Standard x86-64 computational environment.
- **Validation**: Stratified 5-fold cross-validation and independent held-out test set evaluation ($N = 200$).

## 12. Evaluation Metrics

- **Classification Metrics**:
  - Accuracy
  - Precision (per-class and macro/weighted)
  - Recall (per-class and macro/weighted)
  - F1-Score (per-class and macro/weighted)
  - Confusion Matrix
- **Graph Metrics**:
  - Node count ($N = 1,150$)
  - Edge count ($E = 2,908$)
  - Modularity score ($Q = 0.4442$)
  - Number of detected communities ($k = 12$)
- **Correlation & Explainability Metrics**:
  - Pearson correlation coefficient ($r$)
  - SHAP Mean Absolute Importance value
- **Digital Twin Simulation Metric**:
  - High Employability Probability Uplift ($\Delta P$)

## 13. Results

### Supervised Classification Performance ($N = 200$ test set, PDF p. 13, Figure 3):
- **Overall Accuracy**: **94.5%** (189 out of 200 test students classified correctly).
- **High Employability Class**:
  - Precision: **0.94**
  - Recall: **0.92**
  - F1-Score: **0.93**
- **Low Employability Class**:
  - Precision: **0.98**
  - Recall: **0.98**
  - F1-Score: **0.98** (highest discrimination performance).
- **Medium Employability Class**:
  - Precision: **0.91**
  - Recall: **0.93**
  - F1-Score: **0.92**
- **Macro Average**: Precision: 0.95 | Recall: 0.94 | F1-Score: 0.94.
- **Weighted Average**: Precision: 0.95 | Recall: 0.95 | F1-Score: 0.95.

### Heterogeneous Knowledge Graph Analysis (PDF p. 14, Figure 4):
- **Graph Topology**: 1,150 nodes and 2,908 edges.
- **Community Detection**: Greedy Modularity identified **12 structurally cohesive communities**.
- **Modularity Score**: **$Q = 0.4442$**, confirming strong structural separation between academic/skill sub-clusters.

### Correlation Analysis (PDF p. 23, Figure 11 & Section 5):
- **CGPA vs. Employability Score**: Strong positive correlation (**$r = 0.75$**).
- **SGPA vs. Employability Score**: Strong positive correlation (**$r = 0.70$**).
- **Hiring Readiness vs. Employability Score**: Moderate-strong positive correlation (**$r = 0.63$**).
- **Attendance vs. Employability Score**: Weak correlation; points widely dispersed, proving attendance alone does not dictate readiness.

### SHAP Feature Importance Ranking (PDF p. 1, 16–17, 23–24, Figure 8):
1. **Hiring Readiness**: Importance score = **0.40** (most dominant predictive signal).
2. **CGPA**: Importance score = **0.31** (second dominant predictor).
3. Soft skills (Teamwork, Communication, Critical Thinking): contributed moderate, independent positive signals.

### Digital Twin Counterfactual Uplift Simulation (PDF p. 1, 15–16, 23–24, Figure 7):
- Baseline High Employability Probability: **0.9944**.
- Isolated Communication Skill Intervention: Raised probability to **0.9962** (+0.0018).
- **Combined Multi-Intervention Strategy** (soft skills + mentoring + project training): Maximized probability to **0.9975** (+0.0031).

## 14. Baselines

- Traditional single-stakeholder student-only models (evaluating only CGPA and academic grades without faculty mentoring or industry hiring signals) and conventional un-tuned classifiers (Random Forest, Logistic Regression).

## 15. Ablation Study

- Feature contribution was systematically quantified via SHAP summary plots and pair-plot correlation breakdowns, demonstrating the incremental predictive power of industry hiring readiness (0.40) over academic metrics (0.31) and isolated attendance.

## 16. Explainability

- **Global Explainability**: TreeSHAP global importance plots demonstrate that employer-assessed hiring readiness and academic CGPA jointly account for over 70% of feature attribution (PDF p. 16–17, Figure 8).
- **Local / Individual Explainability**: SHAP force plots decompose predictions for individual students, highlighting exact positive drivers (e.g., high communication rating, strong internship portfolio) and negative drags (e.g., low mentoring hours) (PDF p. 17).
- **Graph Explainability**: 12 modular communities allow students and advisors to visually inspect which skill clusters and industry roles align with their profile (PDF p. 14).

## 17. Main Findings

1. Employability is an interconnected ecosystem property: predicting career readiness using only student academic data introduces significant error; integrating faculty mentoring and industry hiring perspectives achieves 94.5% classification accuracy.
2. Employer-evaluated Hiring Readiness (SHAP 0.40) is more predictive of placement outcomes than academic CGPA (0.31), although CGPA remains the strongest academic correlate ($r = 0.75$).
3. Attendance exhibits negligible correlation with actual employability readiness, showing that mere classroom presence does not equate to workplace competence.
4. Digital Twin simulation provides actionable prescriptive value: counterfactual intervention modeling allows academic departments to simulate the exact career readiness uplift achievable through targeted soft-skill or mentorship programs.

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Survey Self-Report Bias**: Portions of soft-skill attributes are self-assessed by students, introducing potential subjective rating inflation (PDF p. 8–9).
- **Cross-Sectional Regional Focus**: Dataset collected within regional engineering and arts/science colleges in Karnataka, India, requiring cross-regional external validation.
- **Simulated Counterfactuals**: Uplift simulations represent model-based counterfactual inferences rather than a controlled randomized longitudinal cohort trial.

### 18.2 Research Interpretation
- **Target Variable Derivation**: The target employability classes (Low, Medium, High) were derived from an author-defined composite weighted score rather than ground-truth post-graduation placement offer letters, though validated through industry readiness correlations.

## 19. Future Work

Explicitly proposed by the authors (PDF p. 24–25, Section 6):
1. Integrating real-time continuous learning telemetry from institutional LMS platforms into the digital twin data stream.
2. Incorporating longitudinal career trajectory tracking of graduates at 6, 12, and 24 months post-graduation.
3. Expanding knowledge graph reasoning using Graph Neural Networks (GNNs) for automated career pathway recommendation.

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Direct Foundational Precedent for PRIE's Placement Readiness Digital Twin**: Babureddy & Mathew provides the explicit conceptual and architectural justification for PRIE's core Digital Twin module (`10_Digital_Twin/`).
- **Triangular Stakeholder Architecture**: Directly mirrors ScholarCamp's multi-stakeholder ecosystem (Student Learner, Faculty Mentor/Placement Officer, and Industry Recruiter).
- **Prescriptive Counterfactual Engine**: Demonstrates how digital twin simulation can move beyond passive prediction to prescribe specific, high-ROI interventions (e.g., showing a student: "improving your communication rubric by 1.5 points increases your high-readiness probability from 84% to 96%").
- **SHAP Feature Weighting**: Informs the weighting logic in PRIE's multi-dimensional scoring engine, validating that industry readiness assessments must be weighted alongside academic GPA.

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|---|---|---|---|
| Multiclass XGBoost accuracy | Overall accuracy of 94.5% (189/200 correct) on held-out test set | PDF p. 1, Abstract; p. 13, Figure 3 | Experimental result |
| Low employability discrimination | Low class achieved precision, recall, and F1 of 0.98 | PDF p. 13, Figure 3 | Experimental result |
| Knowledge graph scale & modularity | 1,150 nodes, 2,908 edges, 12 communities, modularity Q = 0.4442 | PDF p. 1, Abstract; p. 14, Figure 4 | Experimental result |
| Top SHAP feature importances | Hiring Readiness (0.40) and CGPA (0.31) are dominant predictors | PDF p. 1, Abstract; p. 16–17, 23 | Experimental result |
| Empirical correlations | CGPA (r = 0.75), SGPA (r = 0.70), Hiring Readiness (r = 0.63) | PDF p. 23, Section 5 | Experimental result |
| Digital twin simulation uplift | Combined intervention raised High Employability Probability from 0.9944 to 0.9975 | PDF p. 1, Abstract; p. 15–16, 23 | Experimental result |

## 22. Verification Checklist

- [x] PDF read (26-page research monograph inspected)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (4-layer digital twin architecture)
- [x] Dataset verified (1,000 students, 8 relational tables, Karnataka colleges)
- [x] Features verified (12 features across Student, Faculty, and Industry pillars)
- [x] Algorithms verified (XGBoost, Knowledge Graph, Greedy Modularity, SHAP)
- [x] Architecture inspected (Figure 1 block diagram, Figure 4 KG)
- [x] Experiments inspected (80/20 train/test split, 200 test samples)
- [x] Results verified (94.5% accuracy, 0.98 Low F1, 0.93 High F1, 0.92 Med F1)
- [x] Limitations verified (Self-report soft skills, regional focus)
- [x] Future work verified (Real-time telemetry, GNNs, longitudinal tracking)
- [x] Evidence locations recorded

## 23. Verification Status

**VERIFIED**
*(Empirical digital twin and machine learning study in JIDMIS verified directly from source PDF with exact multi-stakeholder sample counts, classification metrics, graph statistics, and SHAP importance values.)*
