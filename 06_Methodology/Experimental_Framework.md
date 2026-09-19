# Experimental Framework: Master Protocol, Baselines & Decision Boundaries

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Experimental_Framework.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Experimental Framework  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Master Experimental Architecture

The PRIE experimental framework establishes the formal verification protocols for all six core research experiments (`EXP-1` through `EXP-6`). Each experiment is designed to test an authoritative hypothesis (`H1`–`H6`), answer an active research question (`RQ1`–`RQ6`), and validate an architectural subsystem against competitive baselines.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     MASTER EXPERIMENTAL FRAMEWORK MATRIX                        │
├───────┬──────────────────────┬─────────────┬──────────────┬─────────────────────┤
│ EXP   │ Research Focus       │ Hypothesis  │ Dataset      │ Primary Metric      │
├───────┼──────────────────────┼─────────────┼──────────────┼─────────────────────┤
│ EXP-1 │ Spatial ATS Parsing  │ H1 (RQ1)    │ DS-CORPUS-01 │ Boundary-F1         │
│ EXP-2 │ Interview Latency    │ H2 (RQ2)    │ DS-INTERVIEW │ Voice Latency & ICC │
│ EXP-3 │ Sequence Forecasting │ H3 (RQ3)    │ DS-BENCH-02  │ Quantile Loss (q50) │
│ EXP-4 │ Prescriptive XAI     │ H4 (RQ4)    │ DS-SYNTH-01  │ Actionability & Rate│
│ EXP-5 │ Causal Concept AQG   │ H5 (RQ5)    │ DS-AQG-ITEM  │ Discrimination (DI) │
│ EXP-6 │ Digital Twin Uplift  │ H6 (RQ6)    │ DS-REAL-01*  │ Placement Yield (%) │
└───────┴──────────────────────┴─────────────┴──────────────┴─────────────────────┤
│ *DS-REAL-01 is marked: NOT YET AVAILABLE / DATA COLLECTION REQUIRED             │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Granular Experimental Protocol Specifications

---

### Experiment 1 (EXP-1): Multimodal Spatial Layout Intelligence vs Flat-Text Resume Parsing
- **Scientific Objective**: Determine whether incorporating 2D spatial coordinates and vision-language pre-training resolves multi-column layout destruction in technical resume screening (`RG4`).
- **Research Question & Hypothesis**: `RQ1` and `H1`.
- **Target Hypothesis $H_1$**: Multimodal LayoutLMv3 achieves a statistically significant improvement in entity extraction Boundary-F1 ($\Delta F_1 \ge 0.15, p < 0.01$) over flat-text NER on multi-column resumes.
- **Dataset**: `DS-CORPUS-01` ($N = 1,200$ annotated resumes: 400 single-column, 500 two-column, 300 complex multi-column).
- **Independent Variable**: Document Parsing Model (`LayoutLMv3` with $[x_0, y_0, x_1, y_1]$ vs `BERT-NER` on flat text vs `spaCy` regex pipeline).
- **Dependent Variables**: Token Precision, Token Recall, Entity Boundary-F1, Semantic Cosine Similarity to target JD.
- **Baselines**:
  1. `BL1.1`: Rule-based Regex and keyword parsing.
  2. `BL1.2`: Standard `spaCy` en_core_web_trf flat-text NER.
  3. `BL1.3`: Pure text `BERT-base-uncased` fine-tuned on resume entities.
- **Experimental Procedure**:
  1. Resumes are rendered to 300 DPI images and processed via Tesseract OCR to extract word tokens and bounding boxes.
  2. Token sequences are fed to LayoutLMv3 and baseline models.
  3. Entity extraction metrics are computed separately across single-column and multi-column strata.
- **Statistical Test**: Paired Wilcoxon signed-rank test across multi-column test instances; significance threshold $lpha = 0.01$.

---

### Experiment 2 (EXP-2): Conversational Latency & Human Panel Correlation in Multimodal Mock Interviews
- **Scientific Objective**: Evaluate whether a streaming chunked speech pipeline satisfies the sub-1.5s human conversational turn latency threshold while preserving high correlation with blinded human recruiter ratings (`RG5`).
- **Research Question & Hypothesis**: `RQ2` and `H2`.
- **Target Hypothesis $H_2$**: A streaming chunked conversational pipeline achieves sub-1.5s voice-to-voice turn-taking latency while maintaining high positive Pearson correlation ($r \ge 0.70, p < 0.001$) with blinded recruiter panel evaluations.
- **Dataset**: `DS-INTERVIEW-PILOT` ($N = 150$ simulated technical interview recordings across 50 candidate sessions).
- **Independent Variable**: Pipeline Architecture (Streaming Silero VAD + Chunked Whisper + Quantized Local Llama-3 + FastTTS vs Sequential Cloud Whisper API + GPT-4 API + ElevenLabs API).
- **Dependent Variables**: Voice-to-Voice Latency (ms), Transcription Word Error Rate (WER), Paralinguistic Metric Reliability, Recruiter Panel Pearson Correlation ($r$), Two-way Mixed Intraclass Correlation Coefficient ($	ext{ICC}(2, k)$).
- **Baselines**:
  1. `BL2.1`: Sequential Cloud API Pipeline (Cloud Whisper $	o$ Cloud LLM $	o$ Cloud TTS).
  2. `BL2.2`: Standard Text-Only Chatbot Interface.
- **Experimental Procedure**:
  1. Standardized technical questions are delivered to candidate sessions under controlled audio conditions.
  2. Turn latencies are measured programmatically from user speech termination ($VAD_{	ext{end}}$) to first audio chunk playback ($TTS_{	ext{start}}$).
  3. Three blinded corporate technical recruiters independently score candidate responses on a standardized 10-point rubric.
  4. PRIE automated scores are correlated against median recruiter panel ratings.
- **Statistical Test**: Pearson correlation significance test ($t$-test for $r$), paired $t$-test for latency reduction; $lpha = 0.001$.

---

### Experiment 3 (EXP-3): Dynamic Longitudinal Multi-Horizon Forecasting vs Static Tabular Models
- **Scientific Objective**: Determine whether longitudinal sequence modeling using Temporal Fusion Transformers (TFT) outperforms static cross-sectional classifiers in predicting student readiness across multiple future horizons (`RG2`).
- **Research Question & Hypothesis**: `RQ3` and `H3`.
- **Target Hypothesis $H_3$**: Deep longitudinal sequence models (TFT) utilizing multi-week telemetry achieve superior forecasting accuracy (Quantile Loss reduction $\ge 12\%, p < 0.01$) over static tabular models at 12-month and 6-month prediction horizons.
- **Dataset**: `DS-BENCH-02` (OULAD longitudinal interaction sequences, $N = 32,593$) and `DS-SYNTH-01` multi-week temporal cohort ($N = 2,500$).
- **Independent Variable**: Predictive Model Architecture (`TFT` with multi-head self-attention vs Static `XGBoost` vs Static `LightGBM` vs `LSTM`).
- **Dependent Variables**: Continuous Quantile Loss ($q_{0.1}, q_{0.5}, q_{0.9}$), Normalized Mean Squared Error (NMSE), Binary Placement Classification Macro-F1, ROC-AUC.
- **Baselines**:
  1. `BL3.1`: Static `XGBoost` operating on historical cumulative feature aggregates.
  2. `BL3.2`: Static `Random Forest` baseline.
  3. `BL3.3`: Standard `LSTM` recurrent neural network.
- **Experimental Procedure**:
  1. Telemetry is formatted into weekly sequence tensors over 16-week academic periods.
  2. TFT is trained with rolling-origin temporal validation to forecast readiness scores at Horizon +6 months and +12 months.
  3. Static models are trained on cumulative snapshots at identical cutoff timestamps.
- **Statistical Test**: Diebold-Mariano test for forecasting accuracy comparisons; Wilcoxon signed-rank test for quantile loss deltas; $lpha = 0.01$.

---

### Experiment 4 (EXP-4): Actionability & Usability of Prescriptive Counterfactuals vs Descriptive SHAP
- **Scientific Objective**: Investigate whether distance-constrained prescriptive counterfactual recourse (DiCE) yields superior student actionability and remediation velocity compared to descriptive feature attributions (TreeSHAP) (`RG3`).
- **Research Question & Hypothesis**: `RQ4` and `H4`.
- **Target Hypothesis $H_4$**: Distance-constrained prescriptive counterfactual explanations produce a statistically significant increase in student-rated actionability ($\ge 40\%$ increase, $p < 0.001$) and 30-day milestone completion rate over standard descriptive SHAP attribution charts.
- **Dataset**: `DS-SYNTH-01` ($N = 300$ unplaced student profiles) and user evaluation cohort ($N = 60$ participating engineering students).
- **Independent Variable**: Explanation Presentation Format (`DiCE` Prescriptive Recourse Table with locked immutable features vs `TreeSHAP` Feature Importance Beeswarm & Waterfall plots).
- **Dependent Variables**: Subjective Actionability Rating (1–5 Likert scale), Perceived Feasibility Rating (1–5), Mean Time to Milestone Initiation (hours), 30-Day Remediation Milestone Completion Rate (%).
- **Baselines**:
  1. `BL4.1`: Raw Prediction Probability with zero explanation.
  2. `BL4.2`: Global Feature Importance ranking.
  3. `BL4.3`: Standard Local `TreeSHAP` waterfall explanation.
- **Experimental Procedure**:
  1. Unplaced profiles are generated; both SHAP and DiCE explanations are computed.
  2. In a randomized, double-blind crossover study, students receive either SHAP attributions or DiCE actionable milestone targets.
  3. Students complete validated usability instruments and are tracked for 30 days in the learning management system.
- **Statistical Test**: Two-tailed paired $t$-test on Likert actionability ratings; Chi-square test of independence on 30-day milestone completion rates; $lpha = 0.001$.

---

### Experiment 5 (EXP-5): Psychometric Discrimination & Distractor Quality in Causal Concept AQG
- **Scientific Objective**: Verify whether constraining LLM distractor formulation with Computer Science Causal Concept DAGs eliminates non-functional distractors and elevates psychometric item discrimination (`RG6`).
- **Research Question & Hypothesis**: `RQ5` and `H5`.
- **Target Hypothesis $H_5$**: Automatic question generation guided by causal concept DAGs yields technical multiple-choice items with statistically higher Item Discrimination ($DI \ge 0.35$) and Distractor Plausibility ($DPI \ge 0.70$) than unconstrained zero-shot LLM generation.
- **Dataset**: `DS-AQG-ITEM` ($N = 500$ multiple-choice questions across Data Structures, Algorithms, OS, DBMS: 250 Causal DAG-guided, 250 Unconstrained Zero-Shot).
- **Independent Variable**: Generation Method (Causal Concept DAG Chain-of-Thought with misconception path mapping vs Unconstrained Zero-Shot `Llama-3-70B` prompting).
- **Dependent Variables**: Item Difficulty Index ($P$-value), Item Discrimination Index ($DI$), Distractor Plausibility Index ($DPI$), Non-Functional Distractor Proportion ($NFD\%$), Domain Factual Correctness (%).
- **Baselines**:
  1. `BL5.1`: Human Expert-Authored Benchmark Questions (Gold Standard).
  2. `BL5.2`: Zero-Shot Prompted `Llama-3-70B-Instruct`.
  3. `BL5.3`: Few-Shot In-Context Prompted `GPT-4o`.
- **Experimental Procedure**:
  1. Questions are generated across five CS domains for identical difficulty tiers.
  2. Subject matter experts audit factual correctness and code syntax.
  3. Validated items are administered to a testing cohort of 120 undergraduate students.
  4. Psychometric item statistics are calculated from response distributions.
- **Statistical Test**: Two-sample independent $t$-test on Item Discrimination ($DI$) and Mann-Whitney $U$ test on Distractor Plausibility ($DPI$); $lpha = 0.01$.

---

### Experiment 6 (EXP-6): Placement Conversion Uplift in Closed-Loop Digital Twin Platform
- **Scientific Objective**: Evaluate whether a synchronized triangular digital twin architecture (connecting students, faculty mentors, and placement cells) delivers higher institutional placement yields than disconnected point tools (`RG8`).
- **Research Question & Hypothesis**: `RQ6` and `H6`.
- **Target Hypothesis $H_6$**: A closed-loop triangular digital twin architecture synchronizing student practice, faculty mentoring, and placement office criteria yields a statistically significant uplift ($\Delta \ge 15\%, p < 0.05$) in campus placement conversion compared to uncoordinated point solutions.
- **Dataset**: Institutional longitudinal pilot cohort (`DS-REAL-01`, Status: **NOT YET AVAILABLE / DATA COLLECTION REQUIRED**).
- **Independent Variable**: Platform Architecture (Closed-loop synchronized triangular PRIE platform vs Uncoordinated legacy preparation: separate coding portals, external mock interviews, paper resumes).
- **Dependent Variables**: Overall Cohort Placement Conversion Rate (%), Median Time-to-Placement (days), Faculty Intervention Velocity (days to intervene on Week 3 disengagement).
- **Baselines**:
  1. `BL6.1`: Historical Institutional Control Cohort (Prior academic year, same department).
  2. `BL6.2`: Concurrent Unassisted Cohort (Students using uncoordinated public web tools).
- **Experimental Procedure**:
  1. Institutional onboarding protocol executed under approved institutional governance (`Data_Governance.md`).
  2. Treatment cohort utilizes PRIE closed-loop platform throughout final pre-placement semesters.
  3. Placement outcomes and verified corporate offers are audited by the central placement cell.
- **Statistical Test**: Two-proportion $Z$-test for placement conversion rates; Kaplan-Meier survival analysis with log-rank test for time-to-placement; $lpha = 0.05$.
