# Paper 19 — ExplainAI: A Transparent Decision Support System for MHT-CET Engineering Admissions and Scholarship Guidance Using LightGBM and SHAP

## 1. Bibliographic Information

- **Paper ID**: Paper19
- **Full Title**: ExplainAI: A Transparent Decision Support System for MHT-CET Engineering Admissions and Scholarship Guidance Using LightGBM and SHAP
- **Authors**: Ashphak Khan (1), Roshani Satish Jain (2*), Jayashri Ravindra Gaikwad (3), and Gayatri Dilip Patil (4)
  - (1,2,3,4) Department of Computer Engineering, D. N. Patel College of Engineering, Shahada, Maharashtra, India
- **Corresponding Author**: Roshani Satish Jain (`roshanijaun1234@gmail.com`)
- **Year**: 2026 (Published: May 2026)
- **Venue**: International Research Journal of Innovations in Engineering and Technology (IRJIET), Vol. 10, Issue 5, pp. 334–344
- **ISSN (Online)**: 2581-3048
- **DOI**: 10.47001/IRJIET/2026.105044
- **PDF filename**: `Paper19_joshi2025explainai.pdf`
- **PDF path**: `Papers/PDFs/Paper19_joshi2025explainai.pdf`
- **Page count**: 11 pages (pp. 334–344)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper19_joshi2025explainai.bib`) listed synthetic authors ("Joshi, Rakesh and Kulkarni, Manoj"). Inspection of the actual PDF confirms the true authors are Ashphak Khan, Roshani Satish Jain, Jayashri Ravindra Gaikwad, and Gayatri Dilip Patil from D. N. Patel College of Engineering, Shahada.

---

## 2. Research Problem

Selecting an appropriate engineering institution and academic branch following competitive state entrance examinations (e.g., Maharashtra MHT-CET Centralized Admission Process — CAP) is a complex, anxiety-inducing task for students. Admissions data is scattered across massive PDF circulars spanning hundreds of colleges, quotas, and historical rounds. Students struggle to identify realistic cutoff percentiles, understand admission probabilities, or navigate fragmented government scholarship schemes. Traditional counseling systems are either opaque rule-based filters or uninterpretable black-box models that fail to explain *why* a college is recommended.

### Source Evidence
- **PDF Page**: Page 1 (p. 334), Abstract & Section 1 "Introduction".

---

## 3. Research Objectives

1. Develop **ExplainAI**, a transparent, web-based decision-support system predicting engineering admission closing cutoffs and recommending colleges tailored to candidate percentile ranks.
2. Ingest and harmonize a massive multi-year dataset of **231,579 CAP admission records** (2022–2025) using automated PDF parsing (`pdfplumber`).
3. Train and benchmark gradient-boosted decision trees (**LightGBM**) against Random Forest, XGBoost, and Linear Regression to forecast closing cutoff percentiles.
4. Integrate **SHAP (SHapley Additive exPlanations)** to provide transparent, explainable feature attributions for every predicted cutoff.
5. Classify recommendations into intuitive candidate probability tiers: **High Chance / Safe (54.4%)**, **Medium Chance / Moderate (33.9%)**, and **Low Chance / Ambitious (11.7%)**.
6. Incorporate a rule-driven Government Scholarship Finder matching applicant socio-economic profiles against institutional financial aid schemes.

### Source Evidence
- **PDF Page**: Page 1 (p. 334), Abstract; Pages 2–3 (pp. 335–336), Section 1 & Section 3.

---

## 4. Research Questions

Framed around system engineering and regression fidelity:
- How accurately can gradient-boosted decision trees (LightGBM) forecast institutional closing cutoffs across diverse engineering branches, locations, and seat quotas?
- Does LightGBM outperform Random Forest, XGBoost, and Linear Regression in minimizing Mean Absolute Error (MAE) on unseen multi-year admission validation splits?
- Which historical cutoff indicators and institutional attributes dominate prediction variance under TreeSHAP global interpretability?

---

## 5. Dataset

- **Dataset Name**: MHT-CET CAP Engineering Admission Dataset (2022–2025)
- **Dataset Source**: Directorate of Technical Education (DTE) / State Common Entrance Test Cell, Maharashtra
- **Data Collection Method**: Programmatic extraction from multi-round official CAP cutoff PDF notifications using Python `pdfplumber`
- **Total Records Ingested**: **231,579 admission records** (Table 2, PDF p. 337)
- **Temporal Coverage**: 4 academic years (2022, 2023, 2024, 2025)
- **Validation Split**: Held-out 2025 admission round records utilized as the primary test validation set
- **Target Variable**: Continuous Closing Cutoff Percentile (0.00 to 100.00)
- **Data Type**: Multi-relational tabular data covering 300+ engineering institutions, 50+ branches, and dozens of reservation seat categories (GOPENS, LOPENS, TFWS, EWS, OBC, SC, ST).

### Source Evidence
- **PDF Page**: Page 1 (p. 334), Abstract & Page 4 (p. 337), Section 4.1 & Table 2.

---

## 6. Features

Fourteen engineered attributes representing institutional, temporal, and quota dynamics (PDF pp. 337–338):

### Historical Cutoff Statistics
- `mean_cutoff`: Historical multi-year average closing percentile for the specific college-branch-category tuple.
- `max_cutoff`: Highest recorded historical closing percentile.
- `min_cutoff`: Lowest recorded historical closing percentile.
- `prior_year_cutoff`: Immediate preceding year closing percentile.
- `cutoff_std`: Standard deviation of cutoffs across preceding rounds.

### Institutional & Branch Attributes
- `college_code` & `college_name`: DTE institutional identifier.
- `branch_code` & `branch_name`: Academic discipline (e.g., Computer Engineering, IT, AI&DS, Mechanical).
- `district` / `region`: Geographic location of institution.
- `status`: Autonomous vs. Non-Autonomous, Government vs. Private-Unaided.

### Quota & Seat Matrix
- `seat_type`: Quota reservation category (General Open, Ladies Open, OBC, SC, ST, TFWS, EWS).
- `year`: Academic admission cycle year (2022–2025).

### Source Evidence
- **PDF Page**: Page 4 (p. 337), Section 4.3 "Feature Engineering" & Page 9 (p. 342), Figure 8.

---

## 7. Data Preprocessing

1. **PDF Text & Table Extraction**: Using `pdfplumber` to extract multi-column tabular cutoff records from complex government publication PDFs.
2. **Data Cleaning & Deduplication**: Eliminating corrupted rows, handling missing percentile values, and harmonizing inconsistent college branch naming conventions.
3. **Categorical Encoding**: Label encoding and frequency encoding for high-cardinality nominal variables (`college_code`, `branch_code`, `seat_type`).
4. **Feature Engineering**: Computing rolling historical averages, standard deviations, and prior-year deltas.
5. **Normalization & Scaling**: Standardizing continuous percentile features for baseline linear comparisons.

### Source Evidence
- **PDF Page**: Pages 4–5 (pp. 337–338), Sections 4.1–4.3.

---

## 8. Algorithms and Models

### 1. Primary Model: LightGBM (Light Gradient Boosting Machine)
- Utilizes Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB).
- Employs leaf-wise (best-first) tree growth rather than level-wise expansion.
- **Hyperparameter Configuration (Table 3, PDF p. 338)**:
  - `learning_rate`: 0.05
  - `num_leaves`: 31
  - `max_depth`: -1 (unconstrained leaf-wise growth)
  - `n_estimators`: 500
  - `min_child_samples`: 20
  - `subsample`: 0.8
  - `colsample_bytree`: 0.8
  - `objective`: `regression` (L2 loss)

### 2. Evaluated Baselines
- Linear Regression (Ordinary Least Squares).
- Random Forest Regressor (`scikit-learn`).
- XGBoost Regressor.

### 3. Explainability Engine: TreeSHAP
- Computes exact Shapley values across LightGBM tree ensembles to quantify individual feature contributions to the predicted cutoff percentile.

### Source Evidence
- **PDF Page**: Pages 5–6 (pp. 338–339), Section 4.4 & Table 3; Page 9 (p. 342), Section 5.5.

---

## 9. Architecture

The ExplainAI platform is deployed as a modular web application (Table 4, PDF p. 340):
- **User Presentation Layer**: Responsive web interface (HTML5, JavaScript, Chart.js for trend graphs, jsPDF for downloadable reports).
- **Application Backend**: **Python Flask** web server orchestrating recommendation logic, user authentication (bcrypt), and API endpoints.
- **Data Persistence**: **PostgreSQL** relational database indexing 231,579 CAP admission records.
- **Machine Learning Core**: LightGBM regression model generating real-time cutoff predictions.
- **Interpretability Layer**: SHAP TreeExplainer generating feature impact rankings.
- **Financial Aid Module**: Rule-based scholarship eligibility checker.

### Source Evidence
- **PDF Page**: Page 7 (p. 340), Section 4.9 & Table 4; Figures 2 & 3.

---

## 10. Methodology

1. **Corpus Extraction**: Extracting 231,579 records from 2022–2025 Maharashtra CAP PDF publications.
2. **Feature Engineering**: Generating 14 institutional, temporal, and historical cutoff statistical features.
3. **Model Training & Cross-Validation**: Fitting Linear Regression, Random Forest, XGBoost, and LightGBM models on historical data.
4. **Validation Benchmarking**: Evaluating models on the held-out 2025 admission round records using MAE, RMSE, and $R^2$.
5. **Chance Stratification**: Comparing candidate MHT-CET percentile against predicted closing cutoff:
   - *High Chance (Safe)*: Student percentile $\ge$ Predicted cutoff $+ 2.0$.
   - *Medium Chance (Moderate)*: Student percentile within $\pm 2.0$ of predicted cutoff.
   - *Low Chance (Ambitious)*: Student percentile below predicted cutoff $- 2.0$.
6. **Interpretability Generation**: Running TreeSHAP to display dominant feature attributions on the student dashboard.

### Source Evidence
- **PDF Page**: Pages 4–8 (pp. 337–341), Sections 4 and 5.

---

## 11. Experimental Setup

- **Operating System**: Windows.
- **Environment**: Python 3.x, Flask, PostgreSQL.
- **ML Libraries**: `lightgbm`, `scikit-learn`, `shap`, `pandas`, `numpy`, `pdfplumber`.
- **Client Libraries**: Chart.js, jsPDF.
- **Hardware**: Intel Core i5 processor, 8 GB RAM minimum.
- **Validation Dataset**: 2025 official CAP closing cutoff records.

### Source Evidence
- **PDF Page**: Page 7 (p. 340), Table 4.

---

## 12. Evaluation Metrics

- **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual closing percentiles.
- **Root Mean Squared Error (RMSE)**: Penalizes large outlier deviations in cutoff predictions.
- **Coefficient of Determination ($R^2$ Score)**: Proportion of variance in actual cutoffs explained by the model.
- **Recommendation Tiers**: Percentage distribution of safe, moderate, and ambitious recommendations.

### Source Evidence
- **PDF Page**: Page 8 (p. 341), Section 5.4 & Table 5.

---

## 13. Results

### 1. Comparative Regression Model Performance (Table 5, PDF p. 341)

| Model | MAE (Percentile Points) | RMSE | $R^2$ Score | Performance Summary |
|:---|:---:|:---:|:---:|:---|
| **Linear Regression** | 3.84 | 4.71 | 0.81 | Weakest fit; struggles with non-linear quota shifts |
| **Random Forest** | 2.16 | 2.94 | 0.90 | Substantial improvement via bagging ensemble |
| **XGBoost** | 1.58 | 2.01 | 0.93 | Strong gradient boosting baseline |
| **LightGBM (Proposed)** | **1.23** | **1.62** | **0.95** | **Superior performance across all metrics** |

### 2. Predictive Fidelity Highlights
- **Mean Error**: LightGBM achieved an **MAE of 1.23 percentile points**, meaning cutoff forecasts deviate on average by less than 1.25 percentiles from actual admission closing ranks.
- **Variance Explained**: $R^2 = 0.95$, proving that the engineered features explain 95% of the total variance across multi-year admissions.
- **Error Bounds**: Proximity of RMSE (1.62) to MAE (1.23) confirms the absence of catastrophic outlier predictions.

### 3. Recommendation Chance Distribution (Figure 5, PDF p. 341)
- **High Chance (Safe)**: **54.4%**
- **Medium Chance (Moderate)**: **33.9%**
- **Low Chance (Ambitious)**: **11.7%**
- Demonstrates balanced guidance prioritizing realistic admissions while preserving aspirational reaches.

### 4. Global SHAP Feature Importance (Figure 8, PDF p. 342)
TreeSHAP rankings confirmed that:
1. `mean_cutoff` (historical multi-year average) is the single most dominant predictor.
2. `max_cutoff` and `prior_year_cutoff` provide secondary anchor boundaries.
3. `year` captures macroeconomic trends (e.g., rising cutoff demand in Computer Science / AI branches).

### Source Evidence
- **PDF Page**: Page 8 (p. 341), Table 5, Figures 4, 5, 6; Page 9 (p. 342), Figures 7 & 8.

---

## 14. Baselines

- **Linear Regression**: Ordinary Least Squares baseline ($MAE = 3.84, R^2 = 0.81$).
- **Random Forest**: Standard scikit-learn ensemble ($MAE = 2.16, R^2 = 0.90$).
- **XGBoost**: Extreme Gradient Boosting ($MAE = 1.58, R^2 = 0.93$).

### Source Evidence
- **PDF Page**: Page 8 (p. 341), Table 5.

---

## 15. Ablation Study

Demonstrated through feature attribution and comparative model scaling:
Comparing Linear Regression ($R^2=0.81$) to tree ensembles ($R^2=0.90–0.95$) demonstrates that non-linear interaction between reservation seat type and college tier cannot be modeled linearly. LightGBM's leaf-wise tree growth reduced MAE by an additional 22% compared to XGBoost (1.23 vs. 1.58).

### Source Evidence
- **PDF Page**: Page 8 (p. 341), Section 5.5 & Table 5.

---

## 16. Explainability

A core contribution of ExplainAI:
- **TreeSHAP Implementation**: Deployed directly in the web pipeline to explain cutoff forecasts.
- **Dashboard Visualizations**: Chart.js displays historical cutoff trajectories (2022–2025) with LightGBM projected 2026 cutoff points bounded by 95% confidence intervals (Figure 4).
- **Human-Centric Categorization**: Color-coded probability tags (Green = High Chance, Yellow = Moderate, Red = Low Chance) make predictive outputs accessible to non-technical high school applicants.

### Source Evidence
- **PDF Page**: Pages 7–9 (pp. 340–342), Figures 3, 4, and 8.

---

## 17. Main Findings

1. LightGBM delivers state-of-the-art accuracy in academic admission cutoff forecasting ($MAE = 1.23, R^2 = 0.95$), outperforming XGBoost, Random Forest, and Linear Regression.
2. Historical mean cutoff, maximum cutoff, and immediate prior-year closing ranks account for the vast majority of predictive variance in centralized admission rounds.
3. Combining percentile forecasting with categorized chance tiers (High 54.4%, Medium 33.9%, Low 11.7%) and scholarship eligibility checkers significantly reduces applicant anxiety during counseling.
4. SHAP feature importance transforms an otherwise opaque admission recommendation algorithm into an accountable, transparent decision-support system.

### Source Evidence
- **PDF Page**: Page 1 (p. 334), Abstract; Page 8 (p. 341), Section 5.4; Page 10 (p. 343), Section VI "Conclusion".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **State-Specific Scope**: Validated exclusively on Maharashtra MHT-CET engineering admissions data (2022–2025); adaptation to national systems (e.g., JoSAA / JEE Main) requires re-ingestion of new quota structures.
- **Static Scholarship Rules**: Scholarship matching relies on rule-based eligibility matching rather than dynamic predictive qualification.

### 18.2 Research Interpretation
- While the dataset is exceptionally large ($N=231,579$), sudden institutional quota shifts or newly introduced academic branches with zero historical track record require heuristic cold-start handling.
- The platform focuses on admission placement into college rather than downstream post-graduation employment placement.

---

## 19. Future Work

Explicitly proposed by authors:
1. Extending the model to all-India entrance systems (JEE Main, NEET, GATE).
2. Incorporating deep learning neural architectures (TabNet) for tabular forecasting.
3. Building automated alert systems for spot rounds and institutional vacancy notifications.
4. Conducting longitudinal user studies to evaluate the impact of ExplainAI recommendations on actual candidate seat acceptance rates.

### Source Evidence
- **PDF Page**: Page 10 (p. 343), Section VI "Conclusion".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Explainability & Institutional Benchmark Engine (Module 03)**.
- **Direct Algorithmic Adoption**: LightGBM's outstanding performance ($MAE=1.23, R^2=0.95$) and low computational footprint make it an ideal engine for PRIE's placement salary band and company hiring cutoff predictors.
- **Decision Tier Blueprint**: The tripartite categorization scheme (Safe / Moderate / Ambitious) directly informs PRIE's job application targeting module, guiding students to balance safe offers with aspirational reach companies.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| LightGBM achieves MAE=1.23, RMSE=1.62, $R^2=0.95$ | Test set performance against baselines | PDF p. 8, Table 5 | Experimental result |
| Dataset contains 231,579 CAP admission records | Multi-year records from 2022 to 2025 | PDF p. 1 & p. 4, Table 2 | Dataset |
| Recommendation distribution: High 54.4%, Med 33.9%, Low 11.7% | Chance stratification test queries | PDF p. 8, Figure 5 | Experimental result |
| TreeSHAP identifies historical mean cutoff as top predictor | Global SHAP feature ranking | PDF p. 9, Figure 8 | XAI result |
| Full-stack Flask + PostgreSQL + pdfplumber architecture | System implementation specification | PDF p. 7, Table 4 | Architecture |

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

**VERIFIED** (Primary PDF read, exact regression results verified across Table 5, Figures 4–8, and dataset scale verified from Table 2).
