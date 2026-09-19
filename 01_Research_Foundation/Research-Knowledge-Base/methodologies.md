# Research and Experimental Methodologies (Phase 01 Corpus)

This document synthesizes the overarching research paradigms, experimental designs, engineering workflows, and validation methodologies identified across the **44 verified research papers** in the Phase 01 corpus.

> [!NOTE]
> All methodological classifications, workflow steps, and validation protocols documented herein are derived directly from the primary source PDF notes.

---

## 1. Methodological Paradigms Across the 44 Papers

The reviewed literature exhibits five primary research paradigms:

`mermaid
graph TD
    A[Research Methodologies in Reviewed Corpus] --> B[Supervised Empirical ML/DL Pipeline]
    A --> C[Design Science Research Methodology DSRM]
    A --> D[Systematic Reviews & Bibliometric Analysis]
    A --> E[Randomized Controlled Trials & User Studies]
    A --> F[Cognitive Document & Multimodal Ingestion]
`

### 1.1. Distribution of Methodological Paradigms

| Methodology Paradigm | Representative Papers | Core Focus & Typical Workflow |
|:---|:---|:---|
| **Empirical ML / DL Prediction Pipeline** | Paper 01, 04, 09, 10, 18, 19, 22, 24, 33, 34, 41, 44 | Data collection $ightarrow$ Preprocessing & SMOTE $ightarrow$ Feature selection $ightarrow$ Stratified cross-validation $ightarrow$ Model training $ightarrow$ Metric evaluation $ightarrow$ SHAP/LIME interpretation |
| **Design Science Research Methodology (DSRM)** | Paper 03, 20, 21, 23, 28, 38, 40, 41, 43 | Problem identification $ightarrow$ Objective formulation $ightarrow$ Artifact design & development $ightarrow$ Demonstration $ightarrow$ Evaluation (TAM/qualitative) $ightarrow$ Communication |
| **Systematic Literature Review (SLR) & PRISMA** | Paper 06, 08, 26, 31, 39 | Formal search string formulation across databases $ightarrow$ Multi-reviewer screening $ightarrow$ Quality appraisal $ightarrow$ Taxonomy synthesis $ightarrow$ Meta-analysis |
| **Bibliometric & Scientometric Analysis** | Paper 05, 32 | Scopus/Web of Science extraction $ightarrow$ VOSviewer / CiteSpace co-citation mapping $ightarrow$ Keyword co-occurrence clustering $ightarrow$ Longitudinal publication trends |
| **Randomized Controlled Trials (RCT) & User Evaluation** | Paper 27, 40, 44 | Experimental vs. Control cohort partitioning $ightarrow$ System intervention $ightarrow$ Pre/post outcome measurement $ightarrow$ TAM surveys & advisor interviews |
| **Applied NLP / Multimodal Engineering** | Paper 11, 12, 14, 15, 17, 25, 29, 30, 35, 36, 37, 42 | Multi-source web scraping / OCR $ightarrow$ Tokenization / Facial tracking $ightarrow$ Embeddings / Acoustic analysis $ightarrow$ Scoring & Recommendation |

---

## 2. Detailed Breakdown of Standard Pipelines

### 2.1. Supervised Machine Learning Pipeline (e.g., Paper 01, 18, 22, 41)
1. **Institutional Data Ingestion**: Gathering historical academic records (CGPA, semester grades), attendance percentages, and competency assessments.
2. **Data Cleaning & Imputation**: Handling missing entries via median/mean replacement or KNN imputation; outlier filtering.
3. **Class Balancing**: Applying SMOTE (Synthetic Minority Over-sampling Technique) or percentile-based thresholding (e.g., Paper 41 terciles) to prevent majority-class bias.
4. **Feature Engineering & Selection**: Calculating rolling grade trends, soft skill aggregates, and applying mutual information, Pearson correlation, or Random Forest feature importance.
5. **Stratified Partitioning**: 70/30 or 80/20 train/test splitting ensuring identical class distributions in both sets; k-fold stratified cross-validation ( = 5$ or  = 10$).
6. **Model Induction & Hyperparameter Tuning**: Training baseline classifiers (Logistic Regression, Decision Trees) and advanced ensembles (Random Forest, XGBoost, LightGBM) using grid or random search.
7. **Model Assessment**: Computing confusion matrices, per-class Precision, Recall, F1-scores, and ROC-AUC curves.
8. **Explainability Processing**: Generating TreeSHAP global summary bar plots and individual force plots to explain positive/negative risk drivers.

### 2.2. Design Science Research Methodology (DSRM) Pipeline (e.g., Paper 40 Murti 2025)
1. **Problem Identification**: Identifying digital fragmentation and student cognitive overload in higher education learning platforms.
2. **Define Solution Objectives**: Establishing requirements for multi-source retrieval, factual grounding, and transparent source citations.
3. **Artifact Design & Development**: Constructing a 6-stage RAG document processing pipeline (ingestion, text cleaning, semantic chunking, SBERT dense embedding, vector database indexing, query-context retrieval).
4. **Demonstration**: Deploying prototype chatbot across diverse academic queries (accounting, economics, marketing, computer science).
5. **Rigorous Dual Evaluation**:
   - Quantitative Technology Acceptance Model (TAM) survey ( = 267$ students) evaluating Perceived Usefulness, Perceived Ease of Use, and Intention to Use.
   - Qualitative semi-structured inquiry with faculty members ( = 5$) evaluating pedagogical validity and governance.
6. **Communication**: Documenting design principles, operational metrics, and institutional adoption guidelines.

### 2.3. Temporal Sequential & Intervention Pipeline (e.g., Paper 44 Azeez 2026)
1. **Longitudinal Clickstream Tracking**: Capturing continuous weekly telemetry from 3,400+ students across 24 courses over 3 academic years.
2. **Temporal Fusion Transformer Induction**: Combining Variable Selection Networks, LSTM encoders, and interpretable multi-head attention to forecast Week 9 risk from Weeks 1–6 data.
3. **Explainability & Advisor Trust**: Decomposing predictions via SHAP to determine whether failure risk stems from quiz drops (cognitive) or login drops (motivational).
4. **Reinforcement Learning Policy (PPO)**: Training a policy network to recommend personalized interventions (study tips, peer tutoring, advisor meetings).
5. **Randomized Controlled Trial (RCT)**: Testing intervention efficacy across 450 students (Control =225$ vs Treatment =225$), measuring causal impact on course failure rates and engagement scores.

---

## 3. Methodological Recommendations for ScholarCamp / PRIE

1. **Adopt DSRM as the Master Research Method**: The development of ScholarCamp/PRIE aligns directly with Design Science Research Methodology, combining artifact engineering with empirical user and institutional evaluation.
2. **Integrate Stratified Multi-Stakeholder Pipelines**: Following Paper 41, the prediction pipeline should ingest triangulated features (Student, Faculty Mentor, Industry) rather than isolated student academic records.
3. **Combine Longitudinal Sequence Modeling with RCT Validation**: Following Paper 44, PRIE should track temporal skill trajectories and validate career intervention policies using prospective controlled comparison cohorts.
