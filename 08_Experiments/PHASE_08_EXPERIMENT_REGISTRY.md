# PHASE 08 — MASTER EXPERIMENT REGISTRY
**Project**: ScholarCamp  
**Core Research Subsystem**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/PHASE_08_EXPERIMENT_REGISTRY.md`  
**Date**: September 2026  
**Authority Level**: Level 9 Empirical Registry  
**Status**: ACTIVE AUTHORITATIVE REGISTRY  

---

## 1. Registry Architecture & Scientific Invariants

This registry serves as the authoritative single source of truth for every experiment executed or specified within the ScholarCamp / PRIE empirical evaluation. In compliance with the Phase 08 Master Protocol:
1. No required fields are fabricated. Where empirical real-world cohorts or models are pending data collection or training, the exact status `NOT YET AVAILABLE / DATA COLLECTION REQUIRED` or `MODEL NOT TRAINED` is declared.
2. Synthetic simulation datasets (`DS-SYNTH-01`) are strictly labeled as **SYNTHETIC SIMULATION**, certifying algorithmic and software correctness without asserting unearned human outcome validity.
3. Bidirectional mapping connects Phase 03/06 theoretical definitions with Phase 07/08 operational execution.

---

## 2. Master Experiment Registry Entries

### Entry EXP-01: Calibrated Placement Prediction & Multi-Baseline Benchmarks
- **Experiment ID**: `EXP-01` (Operational) / `EXP-1` (Runner) / Linked to `RQ1`, `RQ3`, `H1`, `H3`
- **Experiment Name**: Probability Calibration & Baseline Predictive Benchmarking on Canonical 22D SPV
- **Research Question**: `RQ1` / `RQ3`: Can a gradient-boosted decision tree calibrated via Platt scaling achieve superior probabilistic reliability and placement classification accuracy compared to linear and ensemble baselines?
- **Hypothesis**: `H1`: Calibrated XGBoost satisfies Brier Score $\le 0.08$ and Expected Calibration Error (ECE) $\le 0.05$ with statistically significant F1 uplift over linear baselines.
- **Research Objective**: `RO1`, `RO3`: Establish a well-calibrated, high-accuracy placement readiness foundation using the 22-dimensional Student Profile Vector ($\mathbf{x}_{	ext{spv}} \in \mathbb{R}^{22}$).
- **Research Gap**: `CG1`, `CG3`: Literature relies on uncalibrated black-box classifiers that output distorted probabilities, risking misguided academic interventions.
- **Independent Variables**: Classification Model Architecture (`Calibrated XGBoost` + Platt Scaling vs `Random Forest` vs `Logistic Regression`), Random Seeds ($\{42, 123, 456, 789, 2026\}$).
- **Dependent Variables**: Brier Score Loss, Expected Calibration Error (ECE), Macro-averaged F1, ROC-AUC, Accuracy, Runtime (s).
- **Controlled Variables**: Canonical 22D SPV schema ($F_{01}$–$F_{22}$), train/val/test split ratio (80/10/10 stratified), zero data leakage (scalers fitted only on train fold).
- **Dataset**: `DS-SYNTH-01` (Gaussian Copula SPV simulation cohort, $N = 2,500$ complete vectors).
- **Population**: Undergraduate engineering candidate simulation reflecting Indian technical universities.
- **Sample Size**: Total $N = 2,500$ ($N_{	ext{train}} = 2,000$, $N_{	ext{val}} = 250$, $N_{	ext{test}} = 250$).
- **Baseline**: `BL-01`: Logistic Regression (L2 regularization, $C=1.0$), `BL-02`: Random Forest (100 trees, balanced class weights).
- **PRIE Method**: Extreme Gradient Boosting (`XGBoost`, 150 estimators, max depth 5, learning rate 0.1, cost-sensitive `scale_pos_weight`) with Platt Sigmoid Calibration fitted on held-out validation fold.
- **Evaluation Metrics**: Macro-F1, ROC-AUC, Accuracy, Brier Score, ECE.
- **Statistical Test**: McNemar's Test (continuity corrected) on paired test predictions; Wilcoxon Signed-Rank Test across test instances; $lpha = 0.05$.
- **Random Seeds**: Multi-seed battery: `42`, `123`, `456`, `789`, `2026`.
- **Expected Output**: Calibrated XGBoost Brier $\le 0.08$, ECE $\le 0.05$, Macro-F1 $\ge 0.92$, ROC-AUC $\ge 0.95$.
- **Implementation Entry Point**: `07_Implementation/PRIE_v1/experiments/run_experiment.py::run_exp1`
- **Status**: **EXECUTED & EMPIRICALLY VALIDATED (SYNTHETIC SIMULATION)**
- **Reproducibility Status**: Fully reproducible via deterministic script; raw outputs preserved under `15_Experiment_Results/EXP-1/`.

---

### Entry EXP-02: Prescriptive Counterfactual Recourse Feasibility & Invariance
- **Experiment ID**: `EXP-02` (Operational) / `EXP-3` (Runner) / Linked to `RQ4`, `H4`
- **Experiment Name**: Distance-Constrained DiCE Counterfactual Recourse Feasibility & Immutability Audit
- **Research Question**: `RQ4`: Does distance-constrained counterfactual optimization (DiCE) over intervenable student variables produce sparse ($k \le 3$), feasible remediation plans while strictly respecting immutable demographic features?
- **Hypothesis**: `H4`: DiCE counterfactual recourse achieves 100% invariance on locked immutable feature $F_{17}$ (`branch_encoded`), average sparsity $k \le 3$ intervenable features, and $\ge 90\%$ target readiness reachability.
- **Research Objective**: `RO4`: Provide students with actionable prescriptive remediation targets rather than static, unhelpful descriptive attributions.
- **Research Gap**: `CG2`: Existing XAI in education is purely descriptive (TreeSHAP), explaining historical failure without specifying forward-looking recourse.
- **Independent Variables**: Explanation Engine (`DiCE` constrained optimization with locked $F_{17}$ and bounded mutable features vs unconstrained feature search).
- **Dependent Variables**: Immutable Feature ($F_{17}$) Invariance Rate (%), Average Sparsity ($L_0$ feature count), Average $L_1$ Proximity Distance, Target Readiness Reachability Rate (%).
- **Controlled Variables**: Target readiness threshold ($P \ge 0.75$), maximum allowed feature changes ($k = 3$), student low-readiness profile cohort ($N = 30$).
- **Dataset**: `DS-SYNTH-01` low-readiness student subset ($P_{	ext{pred}} < 0.50$).
- **Population**: Simulated at-risk engineering students requiring academic and skill remediation.
- **Sample Size**: $N = 30$ randomly sampled low-readiness candidate vectors.
- **Baseline**: Unconstrained feature perturbation; Descriptive TreeSHAP waterfall attributions.
- **PRIE Method**: Prescriptive Explainable AI Engine (`PrescriptiveXAIEngine` via $M_{07}$) with integer/continuous bounding and locked $F_{17}$.
- **Evaluation Metrics**: Invariance %, Sparsity ($k$), $L_1$ Distance, Target Reachability %.
- **Statistical Test**: Exact constraint audit; paired comparison against unconstrained search; $lpha = 0.01$.
- **Random Seeds**: `42`, `123`, `456`, `789`, `2026`.
- **Expected Output**: 100% $F_{17}$ invariance, mean sparsity $k \le 3$, reachability $\ge 90\%$.
- **Implementation Entry Point**: `07_Implementation/PRIE_v1/experiments/run_experiment.py::run_exp3`
- **Status**: **EXECUTED & EMPIRICALLY VALIDATED (ALGORITHMIC RECOURSE)**
- **Reproducibility Status**: Fully reproducible; raw results stored in `15_Experiment_Results/EXP-2/`.

---

### Entry EXP-03: Multimodal Mock Interview Behavioral Diagnostic Ablation
- **Experiment ID**: `EXP-03` (Operational) / `EXP-2` (Runner) / Linked to `RQ2`, `H2`
- **Experiment Name**: Multimodal Behavioral Diagnostic Ablation & Late Fusion Analysis
- **Research Question**: `RQ2`: To what extent does Late Multimodal Fusion combining acoustic prosody, facial composure, and speech clarity reduce diagnostic variance and outperform unimodal assessment baselines?
- **Hypothesis**: `H2`: Late Multimodal Fusion yields statistically significant variance reduction ($> 50\%$) and higher diagnostic stability over unimodal audio, video, or speech models ($p < 0.05$).
- **Research Objective**: `RO2`: Construct a comprehensive multimodal behavioral interview assessment pipeline.
- **Research Gap**: `CG5`: Prior mock interview systems operate in unimodal silos or suffer from extreme scoring instability.
- **Independent Variables**: Modality Configuration (`Audio Alone` [Librosa prosody], `Video Alone` [OpenCV composure], `Speech Alone` [Faster-Whisper lexical], `Late Multimodal Fusion` [0.35 Audio + 0.35 Video + 0.30 Speech]).
- **Dependent Variables**: Diagnostic Score Variance ($\sigma^2$), Variance Reduction Percentage (%), Mean Assessment Score, Paired $t$-test statistic, $p$-value.
- **Controlled Variables**: Controlled test session cases ($N = 50$), identical question sets, calibrated modality score clipping $[40.0, 95.0]$.
- **Dataset**: `DS-INTERVIEW-SIM` ($N = 50$ simulated multimodal candidate interview sessions).
- **Population**: Simulated technical software engineering interviewees.
- **Sample Size**: $N = 50$ standardized candidate sessions evaluated across 5 seeds.
- **Baseline**: Unimodal Audio, Unimodal Video, Unimodal Speech pipelines.
- **PRIE Method**: Multimodal Mock Interview Coach ($M_{05}$) with weighted Late Multimodal Fusion.
- **Evaluation Metrics**: Score Variance, Percentage Variance Reduction, Paired $t$-test $p$-value.
- **Statistical Test**: Paired Student's $t$-test comparing fused diagnostic scores against unimodal baselines; $lpha = 0.05$.
- **Random Seeds**: `42`, `123`, `456`, `789`, `2026`.
- **Expected Output**: Variance reduction $\ge 50\%$, $p < 0.05$ demonstrating multimodal stability.
- **Implementation Entry Point**: `07_Implementation/PRIE_v1/experiments/run_experiment.py::run_exp2`
- **Status**: **EXECUTED & EMPIRICALLY VALIDATED (SIMULATED MULTIMODAL SESSIONS)**
- **Reproducibility Status**: Fully reproducible; raw results stored in `15_Experiment_Results/EXP-3/`.
- **Epistemological Constraint**: Blinded human recruiter correlation ($r \ge 0.82$) requires physical human recruiter panel trials (`DS-INTERVIEW-PILOT`), marked as **NOT YET AVAILABLE / HUMAN TRIAL REQUIRED**.

---

### Entry EXP-04: Resume ATS Spatial Extraction & Multi-Column Document Intelligence
- **Experiment ID**: `EXP-04` (Operational) / `EXP-4` (Runner) / Linked to `RQ1`, `H1`
- **Experiment Name**: Resume ATS Extraction & Spatial Layout Ablation
- **Research Question**: `RQ1`: Does incorporating 2D spatial layout coordinates resolve multi-column document text interleaving compared to standard flat-text regex parsing?
- **Hypothesis**: `H1`: Spatial bounding-box parsing achieves higher entity extraction F1 and semantic job description alignment than linear text parsing on complex technical resumes.
- **Research Objective**: `RO1`: Resolve ATS document parsing failure on non-linear multi-column resumes.
- **Research Gap**: `CG4`: Linear text extractors concatenate parallel columns horizontally, corrupting technical skill tokens and destroying entity boundaries.
- **Independent Variables**: Document Parser Architecture (`Spatial PyMuPDF Bounding Boxes + Semantic Scoring` vs `Flat Regex Heuristics` vs `LayoutLMv3`).
- **Dependent Variables**: Overall ATS Score, Entity Extraction Macro-F1, Keyword Match Recall, Bounding Box Layout Preservation Rate (%).
- **Controlled Variables**: Target Job Description ("Software Development Engineer"), technical skill ontology, standardized test resume battery.
- **Dataset**: Test resume portfolio (single-column, two-column, technical resumes).
- **Population**: Undergraduate and early-career software engineering applicants.
- **Sample Size**: Controlled test portfolio ($N = 3$ representative architectural profiles); Full benchmark corpus `DS-CORPUS-01` ($N = 1,200$).
- **Baseline**: Flat-text Regex and keyword extraction (`ResumeATSEngine` baseline mode).
- **PRIE Method**: 2D Spatial PyMuPDF layout tokenization ($M_{02}$) with normalized $[0, 1000]$ coordinate bounding boxes and SBERT dense similarity.
- **Evaluation Metrics**: ATS Alignment Score, Keyword Coverage, Bounding Box Extraction Status.
- **Statistical Test**: McNemar's test on discordant entity detections; $lpha = 0.05$.
- **Random Seeds**: Deterministic parsing across seeds.
- **Expected Output**: Macro-F1 gain on multi-column resumes over flat regex; LayoutLMv3 pipeline status reported honestly.
- **Implementation Entry Point**: `07_Implementation/PRIE_v1/experiments/run_experiment.py::run_exp4`
- **Status**: **PARTIALLY VALIDATED (BASELINE ACTIVE / LAYOUTLMV3 LABELED: MODEL NOT TRAINED)**
- **Reproducibility Status**: Fully reproducible; raw results stored in `15_Experiment_Results/EXP-4/`.

---

### Entry EXP-05: A* Concept DAG Roadmap Precedence Scheduling
- **Experiment ID**: `EXP-05` (Operational) / `EXP-6` (Runner) / Linked to `RQ5`, `RQ6`, `H5`, `H6`
- **Experiment Name**: A* Concept DAG Milestone Topological Scheduling Optimization
- **Research Question**: `RQ5` / `RQ6`: Does graph-topological scheduling over a computer science concept DAG eliminate prerequisite sequencing violations compared to unconstrained or heuristic ordering?
- **Hypothesis**: `H6`: Kahn's topological sort over the CS concept DAG achieves 0% prerequisite violations ($0$ violations), whereas randomized or unconstrained milestone scheduling yields significant sequencing errors ($> 25\%$).
- **Research Objective**: `RO5`, `RO6`: Ensure that dynamic learning roadmaps respect strict educational prerequisite dependencies.
- **Research Gap**: `CG7`, `CG8`: Generic recommendation platforms schedule advanced topics before foundational prerequisites, leading to cognitive overload.
- **Independent Variables**: Milestone Scheduling Algorithm (`Kahn's Topological DAG Scheduler` vs `Randomized Milestone Ordering`).
- **Dependent Variables**: Total Prerequisite Violations (count), Prerequisite Violation Rate (%), Runtime (ms).
- **Controlled Variables**: Test topic curriculum subset ($N = 10$ interconnected CS topics: arrays, trees, dynamic programming, SQL, indexing), verified 38-node master DAG (`cs_concept_dag.json`).
- **Dataset**: `cs_concept_dag.json` (38 concept nodes, 52 directed prerequisite edges).
- **Population**: Computer Science and Engineering undergraduate curriculum graph.
- **Sample Size**: 10 interdependent topics evaluated across 5 seeds.
- **Baseline**: Randomized / unconstrained milestone ordering.
- **PRIE Method**: Dynamic Learning Roadmap Generator ($M_{08}$) executing in-degree topological sorting.
- **Evaluation Metrics**: Prerequisite Violation Count, Violation Percentage.
- **Statistical Test**: Wilcoxon Signed-Rank Test on paired violation counts across random permutations; $lpha = 0.05$.
- **Random Seeds**: `42`, `123`, `456`, `789`, `2026`.
- **Expected Output**: Kahn scheduler: 0 violations ($0.0\%$); Randomized baseline: $> 3$ violations ($> 30\%$).
- **Implementation Entry Point**: `07_Implementation/PRIE_v1/experiments/run_experiment.py::run_exp6`
- **Status**: **EXECUTED & EMPIRICALLY VALIDATED (GRAPH ALGORITHMIC VERIFICATION)**
- **Reproducibility Status**: Fully reproducible; raw results stored in `15_Experiment_Results/EXP-5/`.

---

### Entry EXP-06: Placement Curriculum RAG Grounding & Hallucination Guardrails
- **Experiment ID**: `EXP-06` (Operational) / `EXP-5` (Runner) / Linked to `RQ6`, `H5`
- **Experiment Name**: Curriculum RAG Semantic Retrieval Precision & Out-of-Domain Guardrail Evaluation
- **Research Question**: `RQ6`: Can a dense curriculum retrieval pipeline maintain 100% in-domain precision while reliably rejecting out-of-domain conversational queries without hallucinating?
- **Hypothesis**: `H5`: Two-stage curriculum retrieval with cosine similarity gating achieves 100% in-domain retrieval precision and 100% rejection of irrelevant or adversarial out-of-domain queries.
- **Research Objective**: `RO6`: Deliver trustworthy, grounded curriculum assistance with zero hallucinated technical facts.
- **Research Gap**: `CG6`: Unconstrained LLMs frequently hallucinate incorrect technical answers and engage with irrelevant off-topic queries.
- **Independent Variables**: Query Domain Classification (`In-Domain Technical Curriculum Queries` vs `Out-of-Domain / Adversarial Distractor Queries`).
- **Dependent Variables**: In-Domain Retrieval Precision (%), Out-of-Domain Rejection Accuracy (%), Grounding Verification Flag.
- **Controlled Variables**: Standardized query test battery ($N = 7$ total: 4 technical, 3 out-of-domain), indexed technical curriculum corpus (10 semantic chunks across 5 core CS subjects).
- **Dataset**: `resource_library.json` (Curriculum knowledge chunks across DBMS, OS, Computer Networks, DSA).
- **Population**: Technical curriculum corpus for engineering placements.
- **Sample Size**: 7 test queries evaluated across 5 seeds.
- **Baseline**: Unconstrained zero-shot LLM with zero retrieval safeguard.
- **PRIE Method**: Curriculum RAG Assistant ($M_{09}$) with dense embedding indexing and similarity gating.
- **Evaluation Metrics**: Retrieval Precision %, Hallucination Rejection Accuracy %.
- **Statistical Test**: Exact binary classification accuracy audit; $lpha = 0.01$.
- **Random Seeds**: `42`, `123`, `456`, `789`, `2026`.
- **Expected Output**: In-domain precision = 100.0%, Out-of-domain rejection = 100.0%.
- **Implementation Entry Point**: `07_Implementation/PRIE_v1/experiments/run_experiment.py::run_exp5`
- **Status**: **EXECUTED & EMPIRICALLY VALIDATED (RETRIEVAL & GUARDRAIL TEST)**
- **Reproducibility Status**: Fully reproducible; raw results stored in `15_Experiment_Results/EXP-6/`.
