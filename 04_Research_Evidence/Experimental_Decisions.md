# Experimental Setup & Methodological Decisions

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `04_Research_Evidence/Experimental_Decisions.md`  
**Phase**: 04 — Research Evidence & Traceability  
**Status**: Authoritative Pre-Experimental Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`)  
**Date**: September 2026  

---

## 1. Methodological Purpose & Scientific Discipline

This document formalizes the pre-experimental design linking the six Phase 03 Research Questions (**RQ1**–**RQ6**) and Hypotheses (**H1**–**H6**) directly to future experimental protocols to be executed in Phase 08 and Phase 09.

### Fundamental Non-Fabrication Rule:
Under no circumstances are experimental results, empirical outcomes, $p$-values, or benchmark scores fabricated in this document. This document strictly defines:
- **What will be tested?**
- **Under what experimental controls?**
- **Against which baseline algorithms?**
- **Using which exact mathematical metrics?**
- **What constitutes empirical falsification or validation of each hypothesis?**

---

## 2. Master Pre-Experimental Specifications (Experiments EXP-1 to EXP-6)

### EXP-1: Multimodal Spatial Layout Intelligence vs Flat-Text Resume Parsing
- **Linked Research Question**: **RQ1** (Multi-Modal Spatial Parsing vs Flat Text).
- **Linked Hypothesis**: **H1** — Multi-modal document intelligence models incorporating 2D spatial coordinates (LayoutLMv3) achieve a statistically significant improvement in entity extraction Boundary-F1 ($\ge 0.15$ uplift, $p < 0.01$) over flat-text NER on multi-column resumes.
- **Experimental Setup**:
  - *Independent Variable*: Document parsing architecture (Flat-Text Tesseract + spaCy NER vs 2D Spatial LayoutLMv3 + Sentence-BERT).
  - *Dependent Variable*: Entity Extraction Precision, Recall, Boundary Token F1 across 4 entity classes (Education, Skills, Projects, Experience).
  - *Baseline System*: Tesseract OCR with linear text stream concatenated into standard spaCy NER (`en_core_web_sm`).
  - *Experimental System*: PRIE Module M02 (LayoutLMv3 with $[x_0, y_0, x_1, y_1]$ bounding box token classification).
  - *Dataset*: Stratified evaluation corpus of 200 student resumes: 100 single-column standard templates, 100 complex multi-column/graphical templates, with ground-truth entity spans annotated by 3 independent human annotators.
  - *Validation Approach*: 5-fold cross-validation with exact span boundary matching; compute Cohen's kappa for inter-annotator agreement.
  - *Statistical Test*: Paired two-tailed Student's t-test and Wilcoxon signed-rank test ($\alpha = 0.01$).
  - *Expected Evidence*: LayoutLMv3 maintains $F_1 \ge 0.90$ across both single- and multi-column formats, whereas baseline drops from $0.85$ on single-column to $\le 0.65$ on multi-column.
  - *Threats to Validity*: High-resolution PDF rendering variance; OCR engine quality on compressed scanned images.

---

### EXP-2: Conversational Latency and Human Panel Correlation in Multimodal Mock Interviews
- **Linked Research Question**: **RQ2** (Conversational Latency & Human Expert Correlation).
- **Linked Hypothesis**: **H2** — A streaming chunked conversational pipeline achieves sub-1.5s voice-to-voice turn-taking latency while maintaining a high positive Pearson correlation ($r \ge 0.70, p < 0.001$) with blinded human recruiter interview panel ratings.
- **Experimental Setup**:
  - *Independent Variable*: Interview architecture (Sequential Cloud API: Whisper $\to$ GPT-4 $\to$ Cloud TTS vs Streaming Chunked Whisper $\to$ Local Llama-3-8B $\to$ Local TTS with Client MediaPipe Wasm).
  - *Dependent Variables*:
    1. Voice-to-Voice Turn-Taking Latency (milliseconds from end of student speech to start of audio response).
    2. Candidate Evaluation Score (0–100 scale across Technical Accuracy, Communication Clarity, and Behavioral Composure).
  - *Baseline System*: Sequential cloud API pipeline as implemented in **Paper03** and **Paper29**.
  - *Experimental System*: PRIE Module M05 (Streaming Whisper + vLLM Llama-3-8B + Docker Code Sandbox + Browser Wasm MediaPipe).
  - *Dataset*: 50 live mock technical interview sessions across computer science seniors, recording audio, video telemetry, and code submissions.
  - *Validation Approach*: Blinded scoring: identical interview recordings independently evaluated by a panel of 5 senior enterprise technical recruiters using a standardized rubric.
  - *Statistical Test*: Pearson correlation coefficient ($r$), Spearman's rank correlation ($\rho$), and two-way intraclass correlation coefficient (ICC).
  - *Expected Evidence*: Voice turnaround latency drops from $>3.0$s to $<1.5$s; PRIE composite score achieves $r \ge 0.70$ and $\text{ICC} \ge 0.75$ with panel ratings.
  - *Threats to Validity*: Recruiter subjectivity and inter-rater disagreement; student microphone acoustic variation.

---

### EXP-3: Dynamic Longitudinal Multi-Horizon Forecasting vs Static Tabular Models
- **Linked Research Question**: **RQ3** (Longitudinal Sequence Modeling vs Static Snapshots).
- **Linked Hypothesis**: **H3** — Deep longitudinal sequence models (Temporal Fusion Transformer) utilizing continuous telemetry achieve superior placement readiness prediction accuracy (Quantile Loss reduction $\ge 12\%$, $p < 0.01$) over static tabular models at 12-month and 6-month prediction horizons.
- **Experimental Setup**:
  - *Independent Variable*: Temporal modeling architecture (Static XGBoost with lagged static features vs LSTM with Attention vs Temporal Fusion Transformer).
  - *Dependent Variables*: Quantile Loss ($q_{0.1}, q_{0.5}, q_{0.9}$), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Binary Placement Classification Macro-$F_1$.
  - *Baseline Systems*:
    1. Static XGBoost trained on static snapshot data.
    2. Static XGBoost trained on manually engineered temporal delta features ($\Delta \text{score}_{\text{Sem5}-\text{Sem4}}$).
    3. Standard Long Short-Term Memory (LSTM) network.
  - *Experimental System*: PRIE Module M06 (Temporal Fusion Transformer with multi-head self-attention and Variable Selection Networks).
  - *Dataset*: Multi-semester student cohort tracking dataset ($N \ge 1,500$) spanning Semesters 4, 5, 6, and 7, containing academic grades, weekly quiz attempts, login cadence, and eventual placement outcome.
  - *Validation Approach*: Rolling-window temporal cross-validation: train on Sem 4–5, evaluate on Sem 6 (12-month horizon); train on Sem 4–6, evaluate on Sem 7 (6-month horizon).
  - *Statistical Test*: Diebold-Mariano test for predictive accuracy of time series forecasts.
  - *Expected Evidence*: TFT demonstrates statistically significant reduction in Quantile Loss over static models at both 12-month and 6-month horizons.
  - *Threats to Validity*: Historical cohort temporal drift; curricular changes between academic years.

---

### EXP-4: Actionability and Usability of Prescriptive Counterfactuals vs Descriptive SHAP
- **Linked Research Question**: **RQ4** (Prescriptive Counterfactual Recourse vs Descriptive Attribution).
- **Linked Hypothesis**: **H4** — Distance-constrained prescriptive counterfactual explanations (DiCE) produce a statistically significant increase in student-rated actionability ($\ge 40\%$ increase, $p < 0.001$) and 30-day milestone completion rate over standard descriptive SHAP attribution charts.
- **Experimental Setup**:
  - *Independent Variable*: Explainability interface presented to student (Descriptive SHAP Beeswarm/Force Plot vs Constraint-Optimized DiCE Counterfactual Remediation Roadmap).
  - *Dependent Variables*:
    1. Actionability Score (Standardized 7-point Likert usability instrument measuring clarity, feasibility, and cognitive load).
    2. Objective 30-Day Milestone Completion Rate (Proportion of diagnosed skill gaps actively resolved on platform).
    3. Counterfactual Proximity ($L_1$ norm of recommended feature changes).
    4. Counterfactual Sparsity ($L_0$ count of modified features).
  - *Baseline System*: Standard TreeSHAP force plots and feature importance bar charts (as in **Paper18**, **Paper22**, **Paper34**).
  - *Experimental System*: PRIE Module M07 (DiCE counterfactuals with immutable demographic locks and curriculum DAG prerequisite constraints).
  - *Dataset*: Randomized controlled trial with 60 computer science undergraduates classified as "Needs Remediation" ($P_{\text{ready}} \in [0.35, 0.60]$), split into Group A (SHAP) and Group B (DiCE).
  - *Validation Approach*: Double-blind intervention study over a 30-day preparation sprint.
  - *Statistical Test*: Independent two-sample t-test and Mann-Whitney U test on survey scores; Chi-square test on milestone completion rates.
  - *Expected Evidence*: Group B reports mean actionability score $>5.8/7.0$ vs $<3.8/7.0$ for Group A ($p < 0.001$); Group B achieves $\ge 35\%$ higher milestone completion.
  - *Threats to Validity*: Hawthorne effect (students performing better simply because they are being observed); student extrinsic academic workload interference.

---

### EXP-5: Psychometric Discrimination and Distractor Quality in Causal Concept AQG
- **Linked Research Question**: **RQ5** (Causal Concept AQG vs Unconstrained LLM Generation).
- **Linked Hypothesis**: **H5** — Automatic question generation guided by causal concept DAGs yields technical multiple-choice questions with statistically higher psychometric Item Discrimination ($DI \ge 0.35$) and Distractor Plausibility ($DPI \ge 0.70$) than unconstrained zero-shot LLM generation.
- **Experimental Setup**:
  - *Independent Variable*: Question generation methodology (Unconstrained Few-Shot LLM Prompting vs CS Causal Concept DAG-Constrained Chain-of-Thought Generation).
  - *Dependent Variables*:
    1. Classical Item Difficulty ($p$-value: proportion of correct examinee responses).
    2. Item Discrimination Index ($DI = p_{\text{upper 27\%}} - p_{\text{lower 27\%}}$).
    3. Distractor Plausibility Index ($DPI$: proportion of non-keyed options selected by $\ge 5\%$ of lower-scoring students).
    4. Factual Hallucination Rate (Percentage of questions containing invalid technical assertions verified by subject matter experts).
  - *Baseline System*: Standard GPT-4o / Llama-3-8B few-shot prompt: "Generate 10 technical MCQs on Operating Systems with 1 correct answer and 3 distractors."
  - *Experimental System*: PRIE Module M10 (Causal Concept DAG traversal generating distractors mapped to specific misconception nodes).
  - *Dataset*: Diagnostic assessments administered to 300 engineering students across Data Structures, DBMS, and Operating Systems.
  - *Validation Approach*: Classical Test Theory (CTT) psychometric item analysis on student response matrices ($300 \text{ students} \times 40 \text{ items}$).
  - *Statistical Test*: Two-sample Kolmogorov-Smirnov test comparing $DI$ distributions; Fisher's exact test on non-functional distractor frequencies.
  - *Expected Evidence*: Causal DAG AQG yields mean $DI \ge 0.38$ (vs $0.18$ baseline) and reduces non-functional distractors from $42\%$ to $<8\%$.
  - *Threats to Validity*: Item leakage / student collusion; variance in prior student cohort preparation.

---

### EXP-6: Placement Conversion Uplift in Closed-Loop Digital Twin Platform
- **Linked Research Question**: **RQ6** (Closed-Loop Triangular Digital Twin vs Disconnected Systems).
- **Linked Hypothesis**: **H6** — A closed-loop triangular digital twin architecture synchronizing student practice, faculty mentoring, and placement office criteria yields a statistically significant uplift ($\ge 15\%$ increase, $p < 0.05$) in institutional campus placement conversion compared to uncoordinated point solutions.
- **Experimental Setup**:
  - *Independent Variable*: Institutional operational platform (Status-quo disconnected departmental spreadsheets and point tools vs PRIE Module M12 Closed-Loop Triangular Digital Twin).
  - *Dependent Variables*:
    1. Institutional Placement Conversion Rate (Offers Issued / Eligible Candidates).
    2. Mean Time-to-Placement (Days from recruitment drive start to first offer).
    3. Faculty Mentoring Intervention Efficiency (Days elapsed from student performance dip to recorded advisor contact).
  - *Baseline Condition*: Historical departmental performance across the preceding 2 academic cycles under status-quo workflows.
  - *Experimental Condition*: Deployment of PRIE M12 across the active graduating engineering cohort ($N \ge 400$).
  - *Dataset*: Comprehensive institutional placement office recruitment drive records and live telemetry logs.
  - *Validation Approach*: Difference-in-Differences (DiD) quasi-experimental econometric design using an adjacent un-intervened engineering department as an external control group.
  - *Statistical Test*: Difference-in-Differences regression model with robust standard errors clustered at the department level.
  - *Expected Evidence*: Positive, statistically significant DiD interaction coefficient ($\beta_3 \ge +0.12, p < 0.05$) on placement conversion probability.
  - *Threats to Validity*: Macro-economic hiring slowdowns; industry recruiter hiring quota volatility.

---

## 3. Summary of Experimental Decision Portfolio

| Experiment ID | Primary Objective / RQ | Primary Hypothesis | Independent Variable | Primary Quantitative Benchmark Metric | Planned Sample Size |
|:---:|:---:|:---:|:---|:---|:---:|
| **EXP-1** | **RO1 / RQ1** | **H1** | 2D Spatial LayoutLMv3 vs Flat spaCy | Entity Extraction Boundary-F1 $\ge 0.90$ | 200 Resumes |
| **EXP-2** | **RO2 / RQ2** | **H2** | Streaming Whisper/Llama vs Cloud Pipeline | Turn Latency $<1.5$s; Pearson $r \ge 0.70$ with panel | 50 Interviews |
| **EXP-3** | **RO3 / RQ3** | **H3** | Longitudinal TFT vs Static XGBoost/LSTM | Quantile Loss reduction $\ge 12\%$ at 6-month horizon | 1,500 Students |
| **EXP-4** | **RO4 / RQ4** | **H4** | Prescriptive DiCE vs Descriptive SHAP | Actionability Score $\ge 80\%$; Milestone completion $\ge 35\%$ | 60 Students |
| **EXP-5** | **RO5 / RQ5** | **H5** | Causal DAG AQG vs Unconstrained LLM | Item Discrimination $DI \ge 0.35$; $DPI \ge 0.70$ | 300 Examinees |
| **EXP-6** | **RO6 / RQ6** | **H6** | Closed-Loop Digital Twin vs Status Quo | DiD Placement Conversion Uplift $\ge 15\%$ ($p < 0.05$) | 400 Students |

**Scientific Rigor Certified**: Zero fabricated experimental outcomes. Every protocol represents an executable, falsifiable scientific experiment designed to validate or refute PRIE's core hypotheses in subsequent phases.
