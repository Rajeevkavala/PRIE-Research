# Evaluation Metrics Justification & Methodological Standards

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `04_Research_Evidence/Evaluation_Justification.md`  
**Phase**: 04 — Research Evidence & Traceability  
**Status**: Authoritative Evaluation Standard  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`)  
**Date**: September 2026  

---

## 1. Epistemological Evaluation Principles

A primary methodological defect uncovered in the Phase 02 cross-paper analysis (`Evaluation_Metrics_Comparison.md`) is the careless application of evaluation metrics:
- Reporting classification **Accuracy** on severely imbalanced placement datasets ($>70\%$ placed), masking total failure on the minority "At-Risk" class.
- Using surface-level n-gram overlap metrics (**BLEU / ROUGE**) for educational question generation or RAG answers, where semantic correctness has zero correlation with verbatim token matching.
- Claiming a model is "statistically superior" based on a 0.5% accuracy difference without testing for statistical significance.

In PRIE, every metric must be mathematically justified, explicitly tied to a Research Question (RQ) and Hypothesis (H), and accompanied by an explicit disclosure of **what the metric cannot prove**.

---

## 2. Multi-Disciplinary Evaluation Metrics Justification

### 2.1 Tabular Placement Classification Metrics

#### Metric 1: Macro-Averaged F1-Score ($\text{Macro-}F_1$)
- **Mathematical Definition**: 
  $$\text{Macro-}F_1 = \frac{1}{|C|} \sum_{c \in C} \frac{2 \cdot P_c \cdot R_c}{P_c + R_c}$$
- **What it Measures**: Unweighted harmonic mean of Precision and Recall across all readiness classes (Ready, Needs Remediation, At-Risk).
- **Why Appropriate for PRIE**: Institutional placement datasets typically exhibit substantial class imbalance (e.g., 70% placed, 30% unplaced). Accuracy can be artificially inflated to 70% by a trivial majority-class classifier. Macro-$F_1$ penalizes poor performance on the critical minority at-risk class equally.
- **Relevant RQ & Hypothesis**: **RQ1**, **RQ3**, **H3**.
- **Relevant PRIE Module**: **M06** (Placement Readiness Predictor).
- **Literature Usage**: **Paper01** (Olipas 2024), **Paper04** (Patel 2024), **Paper18** (Hidayatulloh 2026), **Paper22** (Olipas 2025).
- **Baseline Comparison**: Logistic Regression, Random Forest.
- **Limitations**: Treats all misclassifications as having equal cost; does not reflect real-world asymmetrical costs (failing to identify an at-risk student is more damaging than giving extra remediation to an almost-ready student).

---

#### Metric 2: Area Under the Precision-Recall Curve (PR-AUC) & ROC-AUC
- **Mathematical Definition**:
  $$\text{ROC-AUC} = \int_{0}^{1} \text{TPR}(\text{FPR}) \, d(\text{FPR}), \quad \text{PR-AUC} = \int_{0}^{1} \text{Precision}(\text{Recall}) \, d(\text{Recall})$$
- **What it Measures**: Discriminative ability of the predicted probability distribution across all possible classification decision thresholds $\tau \in [0, 1]$.
- **Why Appropriate for PRIE**: Campus recruitment operates under varying corporate selectivity bars (e.g., Tier-1 product firms require high precision thresholds, whereas mass recruiters operate at lower thresholds). ROC-AUC and PR-AUC evaluate threshold-agnostic ranking quality. PR-AUC is specifically sensitive to false positives in the minority class.
- **Relevant RQ & Hypothesis**: **RQ3**, **H3**.
- **Relevant PRIE Module**: **M06** (Placement Readiness Predictor).
- **Literature Usage**: **Paper02** (Van Wyk 2025), **Paper18** (Hidayatulloh 2026), **Paper22** (Olipas 2025: AUC = 0.93).
- **Baseline Comparison**: Naive prior probability baseline.
- **Limitations**: An outstanding AUC does not guarantee well-calibrated probabilities; a model can rank perfectly while outputting distorted probability values.

---

#### Metric 3: Brier Score (Probability Calibration)
- **Mathematical Definition**:
  $$\text{Brier Score} = \frac{1}{N} \sum_{i=1}^{N} (P_i - y_i)^2$$
- **What it Measures**: Mean squared difference between predicted readiness probabilities $P_i \in [0, 1]$ and actual binary outcomes $y_i \in \{0, 1\}$.
- **Why Appropriate for PRIE**: PRIE outputs a placement readiness percentage to students. If the model outputs "75% readiness," exactly 75 out of 100 such students must empirically succeed. Brier score directly measures whether output probabilities represent true empirical frequencies.
- **Relevant RQ & Hypothesis**: **RQ3**, **H3**.
- **Relevant PRIE Module**: **M06** (Placement Readiness Predictor).
- **Literature Usage**: Standard metric in medical and high-stakes educational data mining (**Paper02**, **Paper18**).
- **Baseline Comparison**: Climatological baseline (constant prediction equal to overall placement rate).
- **Limitations**: Highly influenced by baseline base rate prevalence; must be evaluated alongside reliability diagrams.

---

### 2.2 Longitudinal Multi-Horizon Forecasting Metrics

#### Metric 4: Quantile Loss ($q$-Risk / Pinball Loss)
- **Mathematical Definition**:
  $$\mathcal{L}_q(y, \hat{y}_q) = \max \Big( q(y - \hat{y}_q), (1 - q)(\hat{y}_q - y) \Big)$$
- **What it Measures**: Asymmetric error penalty for quantile forecasts at specific target percentiles ($q \in \{0.1, 0.5, 0.9\}$).
- **Why Appropriate for PRIE**: Student trajectories are inherently stochastic. Point forecasts (predicting a single readiness score 12 months ahead) are misleading. Evaluating at 10th, 50th, and 90th percentiles provides upper and lower uncertainty bounds, critical for advising.
- **Relevant RQ & Hypothesis**: **RQ3**, **H3**.
- **Relevant PRIE Module**: **M06** (Temporal Sequence Track).
- **Literature Usage**: **Paper44** (Azeez et al. 2026: primary loss metric for Temporal Fusion Transformers).
- **Baseline Comparison**: LSTM point forecasts converted to heuristic intervals via historical standard deviation.
- **Limitations**: Requires sufficiently large sequential observation histories; sensitive to temporal outliers (e.g., student illness).

---

### 2.3 Document Intelligence & ATS Resume Matching Metrics

#### Metric 5: Entity Extraction Boundary Token F1
- **Mathematical Definition**: Harmonic mean of Precision and Recall on exact entity character/token spans:
  $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}, \quad \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
- **What it Measures**: Accuracy in identifying the exact start, end, and label of resume entities (College Name, Degree, Skill, Date, Project Description).
- **Why Appropriate for PRIE**: A resume parser that extracts "Python" from "Python programming" achieves token overlap, but if it misattributes a project skill to the education section due to column interleaving, downstream matching fails. Boundary-F1 strictly penalizes structural boundary corruption.
- **Relevant RQ & Hypothesis**: **RQ1**, **H1**.
- **Relevant PRIE Module**: **M02** (Resume Intelligence Engine).
- **Literature Usage**: **Paper17** (Verma 2026), **Paper42** (Davenport 2025).
- **Baseline Comparison**: Standard spaCy linear text NER (`en_core_web_sm`).
- **Limitations**: Strict exact-match boundary evaluation can penalize minor punctuation variations (e.g., "AWS Certified" vs "AWS Certified Developer").

---

#### Metric 6: Normalized Discounted Cumulative Gain (NDCG@K)
- **Mathematical Definition**:
  $$\text{DCG}@K = \sum_{i=1}^{K} \frac{2^{\text{rel}_i} - 1}{\log_2(i + 1)}, \quad \text{NDCG}@K = \frac{\text{DCG}@K}{\text{IDCG}@K}$$
- **What it Measures**: Quality of candidate resume ranking against corporate job descriptions, heavily penalizing relevant matches placed low in the top-$K$ list.
- **Why Appropriate for PRIE**: Corporate recruiters only review the top 5 to 10 candidates recommended by campus placement cells. Ranking a highly qualified candidate at position 8 instead of position 1 severely degrades recruiter trust.
- **Relevant RQ & Hypothesis**: **RQ1**, **RQ7**.
- **Relevant PRIE Module**: **M02** (ATS Matching Engine) & **M08** (Pathway Recommender).
- **Literature Usage**: **Paper13** (Zhang 2023), **Paper35** (Qin 2020), **Paper36** (Mishra 2025).
- **Baseline Comparison**: BM25 keyword ranking, TF-IDF cosine similarity.
- **Limitations**: Requires graded relevance judgments ($\text{rel}_i \in \{0, 1, 2, 3\}$), which can be labor-intensive to establish from human recruiters.

---

### 2.4 Multimodal Mock Interview Metrics

#### Metric 7: Voice-to-Voice Turn-Taking Latency (Milliseconds)
- **Mathematical Definition**: 
  $$\Delta t_{\text{turn}} = t_{\text{audio\_out\_start}} - t_{\text{speech\_in\_stop}}$$
- **What it Measures**: End-to-end elapsed time between the candidate finishing an utterance and the AI interviewer playing the first audio frame of response.
- **Why Appropriate for PRIE**: Human conversational dialogue breaks down when response latency exceeds 1.5 seconds, creating unnatural pauses and inducing cognitive stress.
- **Relevant RQ & Hypothesis**: **RQ2**, **H2**.
- **Relevant PRIE Module**: **M05** (Multimodal Mock Interview Coach).
- **Literature Usage**: **Paper03** (Joshi 2025), **Paper29** (Srinivasan 2025).
- **Baseline Comparison**: Sequential cloud pipeline (Whisper Cloud $\to$ GPT-4 $\to$ ElevenLabs TTS).
- **Limitations**: Latency measures speed, not response quality or pedagogical empathy.

---

#### Metric 8: Pearson Correlation ($r$) & Intraclass Correlation (ICC) with Expert Panel
- **Mathematical Definition**:
  $$r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2 \sum (Y_i - \bar{Y})^2}}$$
- **What it Measures**: Degree of linear alignment between PRIE's automated interview scores and independent blind ratings from senior enterprise technical recruiters.
- **Why Appropriate for PRIE**: Automated interview systems frequently suffer from scoring artifacts (e.g., rewarding verbose candidates who say little of technical substance). Proving high Pearson correlation ($r \ge 0.70$) with professional recruiters validates scoring validity.
- **Relevant RQ & Hypothesis**: **RQ2**, **H2**.
- **Relevant PRIE Module**: **M05** (Multimodal Mock Interview Coach).
- **Literature Usage**: **Paper15** (Inamdar 2025), **Paper30** (Kulkarni 2024).
- **Baseline Comparison**: Unweighted length-heuristic scoring baseline.
- **Limitations**: Pearson $r$ measures linear association, but not absolute score calibration; must be coupled with ICC(2,1) for absolute agreement.

---

### 2.5 Explainability & Prescriptive Recourse Metrics

#### Metric 9: Counterfactual Proximity ($L_1$ Norm) & Sparsity ($L_0$ Norm)
- **Mathematical Definition**:
  $$\text{Proximity}(x, x^*) = \frac{1}{D} \sum_{d=1}^{D} \frac{|x_d - x_d^*|}{\text{MAD}_d}, \quad \text{Sparsity}(x, x^*) = \sum_{d=1}^{D} \mathbb{I}(x_d \neq x_d^*)$$
- **What it Measures**: Mathematical effort required to execute the counterfactual plan ($L_1$ distance normalized by Median Absolute Deviation) and the total number of features that must be changed ($L_0$).
- **Why Appropriate for PRIE**: A remediation recommendation that tells a student to change 18 different features simultaneously will be abandoned due to cognitive overload. Optimal prescriptive recourse changes the fewest features ($\text{Sparsity} \le 3$) by the smallest feasible increment ($\text{Proximity} \le 0.15$).
- **Relevant RQ & Hypothesis**: **RQ4**, **H4**.
- **Relevant PRIE Module**: **M07** (Prescriptive Explainability Engine).
- **Literature Usage**: **Paper18** (Hidayatulloh 2026), **Paper19** (Joshi & Khan 2025).
- **Baseline Comparison**: Random feature perturbation, Unconstrained gradient counterfactuals.
- **Limitations**: Proximity is a mathematical proxy for study effort; in reality, raising a DSA score by 10 points may be far more difficult than completing an online quiz.

---

#### Metric 10: Student-Rated Actionability Score
- **Mathematical Definition**: Composite mean score on a validated 7-point Likert psychometric scale measuring:
  1. *Clarity*: Understanding what actions are required.
  2. *Feasibility*: Perceived capability to complete recommendations within 30 days.
  3. *Relevance*: Perceived alignment with corporate placement goals.
- **What it Measures**: Human cognitive usability and actionable utility of the generated explanation.
- **Why Appropriate for PRIE**: A mathematically optimal counterfactual is useless if students find it confusing or unachievable.
- **Relevant RQ & Hypothesis**: **RQ4**, **H4**.
- **Relevant PRIE Module**: **M07** (Prescriptive Explainability Engine) & **M08** (Roadmap Generator).
- **Literature Usage**: **Paper19** (Joshi 2025), **Paper34** (Babu 2025).
- **Baseline Comparison**: SHAP force plots and feature importance charts.
- **Limitations**: Subject to subjective student self-reporting bias; must be triangulated with objective 30-day milestone completion data.

---

### 2.6 Automatic Question Generation & Psychometric Metrics

#### Metric 11: Item Discrimination Index ($DI$) & Classical Difficulty ($p$-Value)
- **Mathematical Definition**:
  $$p = \frac{R}{N}, \quad DI = p_{\text{upper 27\%}} - p_{\text{lower 27\%}}$$
  where $R$ is correct responses, $N$ is total examinees, and $p_{\text{upper}}$ and $p_{\text{lower}}$ are success rates in the top and bottom scoring quartiles.
- **What it Measures**: Whether a generated assessment item effectively differentiates between students who have mastered the underlying CS concept and those who have not.
- **Why Appropriate for PRIE**: Diagnostic quizzes must identify specific student skill voids. Items with $DI < 0.20$ are psychometrically flawed (testing trivia or confusion rather than true skill). Items must maintain $DI \ge 0.35$ and $p \in [0.30, 0.70]$.
- **Relevant RQ & Hypothesis**: **RQ5**, **H5**.
- **Relevant PRIE Module**: **M03** (Adaptive Assessment) & **M10** (Causal Concept AQG).
- **Literature Usage**: Standard Classical Test Theory (CTT) standards in Educational Measurement (**Paper25**, **Paper26**, **Paper39**).
- **Baseline Comparison**: Unconstrained few-shot LLM question generation.
- **Limitations**: Sample dependent; requires an evaluation cohort of at least 100 examinees to obtain stable item statistics.

---

#### Metric 12: Distractor Plausibility Index ($DPI$)
- **Mathematical Definition**: Proportion of non-keyed options (distractors) selected by $\ge 5\%$ of lower-quartile examinees:
  $$DPI = \frac{\sum_{k=1}^{K-1} \mathbb{I}\Big( \frac{C_k}{N_{\text{lower}}} \ge 0.05 \Big)}{K - 1}$$
- **What it Measures**: Functionality of incorrect options in multiple-choice questions.
- **Why Appropriate for PRIE**: In unconstrained LLM MCQs, distractors are often absurdly wrong, allowing students to guess the correct answer by simple elimination. $DPI \ge 0.70$ guarantees that distractors represent realistic misconceptions.
- **Relevant RQ & Hypothesis**: **RQ5**, **H5**.
- **Relevant PRIE Module**: **M10** (Causal Concept AQG).
- **Literature Usage**: **Paper25** (Wang 2026), **Paper26** (Fernandez 2025).
- **Baseline Comparison**: Raw GPT-4o few-shot distractor generation.
- **Limitations**: Does not evaluate whether a distractor is accidentally correct due to an edge-case semantic ambiguity (requires SME review).

---

### 2.7 Retrieval-Augmented Generation (RAG) Triad Metrics

#### Metric 13: The RAG Triad (Context Relevance, Groundedness, Answer Relevance)
- **Mathematical Definitions**:
  1. **Context Relevance**: Cosine similarity and cross-encoder score of retrieved syllabus chunks relative to student query.
  2. **Groundedness (Faithfulness)**: Ratio of generated response statements that can be directly attributed to retrieved context.
  3. **Answer Relevance**: Semantic similarity of generated response relative to original student query intent.
- **What it Measures**: Factual integrity, hallucination avoidance, and curriculum alignment of the conversational AI assistant.
- **Why Appropriate for PRIE**: Academic and placement guidance must be strictly grounded in university syllabi and verified hiring policies. RAG Triad provides automated evaluation of factual safety.
- **Relevant RQ & Hypothesis**: **RQ6**.
- **Relevant PRIE Module**: **M09** (RAG Assistant).
- **Literature Usage**: **Paper20** (Sutherland & Swacha 2025: established RAG Triad standard in educational bots).
- **Baseline Comparison**: Zero-shot ungrounded LLM.
- **Limitations**: Evaluated using LLM-as-a-judge (TruLens / Ragas); inherits underlying evaluator LLM biases (requires calibration against human expert checks).

---

## 3. Master Evaluation Metric Summary Grid

| Evaluation Dimension | Primary Metric | Mathematical Target | Linked RQ & Hypothesis | Supporting Literature |
|:---|:---|:---:|:---:|:---|
| **Tabular Placement** | Macro-$F_1$ & PR-AUC | Macro-$F_1 \ge 0.88$, AUC $\ge 0.92$ | **RQ1, RQ3, H3** | **Paper01, Paper04, Paper18, Paper22** |
| **Longitudinal Trajectory**| Quantile Loss ($q_{0.1}, q_{0.5}, q_{0.9}$) | $\ge 12\%$ reduction vs LSTM | **RQ3, H3** | **Paper02, Paper44** |
| **ATS Document Parsing** | Boundary Token F1 | $F_1 \ge 0.90$ on multi-column | **RQ1, H1** | **Paper17, Paper42** |
| **ATS Semantic Matching** | NDCG@10 | NDCG@10 $\ge 0.85$ | **RQ1** | **Paper13, Paper35, Paper36** |
| **Mock Interview Cadence** | Turn-Taking Latency | $\Delta t_{\text{turn}} < 1.5$s | **RQ2, H2** | **Paper03, Paper29** |
| **Mock Interview Scoring** | Pearson $r$ with HR Panel | $r \ge 0.70$ ($p < 0.001$) | **RQ2, H2** | **Paper15, Paper30** |
| **Prescriptive Recourse** | Actionability Score & Proximity | Actionability $\ge 80\%$, $L_1 \le 0.15$| **RQ4, H4** | **Paper18, Paper19** |
| **Item Discrimination** | Psychometric $DI$ | $DI \ge 0.35$ ($p < 0.01$) | **RQ5, H5** | **Paper25, Paper26, Paper39** |
| **Distractor Quality** | Distractor Plausibility ($DPI$) | $DPI \ge 0.70$ | **RQ5, H5** | **Paper25, Paper26** |
| **RAG Factual Grounding** | Groundedness (Faithfulness) | Score $\ge 0.90$ | **RQ6** | **Paper20, Paper40** |
| **Institutional Impact** | DiD Placement Conversion | $\ge 15\%$ uplift ($p < 0.05$) | **RQ6, H6** | **Paper41** |

**Evidentiary Rigor Certified**: No metric claims to prove what it cannot mathematically establish. All metrics are mapped to falsifiable hypotheses and empirical baselines.
