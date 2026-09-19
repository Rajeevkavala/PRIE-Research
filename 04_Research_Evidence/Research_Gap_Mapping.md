# Research Gap to Architectural Solution Mapping

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `04_Research_Evidence/Research_Gap_Mapping.md`  
**Phase**: 04 — Research Evidence & Traceability  
**Status**: Authoritative Gap-to-Solution Mapping  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`)  
**Date**: September 2026  

---

## 1. Scope & Epistemological Framework

In Phase 03 (`03_Research_Problem/Gap_Validation.md`), ten candidate gaps were rigorously audited against literature evidence; eight candidate gaps (`CG1` through `CG8`) were formally validated as genuine, unresolved voids in the scientific literature, while two (`CG9` and `CG10`) were explicitly rejected as unfeasible or scientifically unsound.

This document maps all eight **Validated Research Gaps (`RG1`–`RG8`)** through the complete research chain:
$$\text{Validated Gap} \longrightarrow \text{Objective} \longrightarrow \text{Research Question} \longrightarrow \text{PRIE Module} \longrightarrow \text{Methodological Approach} \longrightarrow \text{Evaluation Protocol}$$

---

## 2. Complete Traceability Chains for Validated Gaps (RG1–RG8)

### RG1: Fragmented Multi-Modal Readiness Signals
- **Gap ID**: `RG1` (Validated from Candidate Gap CG1).
- **Gap Statement**: Existing placement prediction systems operate on isolated, unimodal data silos (either purely tabular academic transcripts, or isolated resume text, or mock interview recordings), failing to synthesize academic fundamentals, practical software engineering fluency, resume ATS hygiene, and interview delivery into a unified, coherent readiness representation.
- **Supporting Literature**: **Paper01** (Olipas 2024), **Paper04** (Patel & Nair 2024), **Paper06** (Senthil 2021), **Paper08** (Alam 2023), **Paper10** (Rao 2022), **Paper11** (Mishra 2025), **Paper15** (Inamdar 2025), **Paper22** (Olipas 2025).
- **Phase 02 Evidence**: `Feature_Comparison.md` & `Cross_Paper_Comparison.md`: 38 out of 44 papers analyzed candidate ability within a single isolated domain. Unimodal models achieve high nominal accuracy on their specific task but fail to predict overall corporate hiring outcomes.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 9.6/10). Reconciles the primary structural divide in educational recruitment AI.
- **PRIE Research Objective**: **PRO** (Primary Research Objective) & **RO1** (Multi-Modal Intelligence).
- **PRIE Research Question**: **RQ1** (Multi-Modal Feature Synthesis).
- **Relevant PRIE Component**: **M01** (Student Profile Vector Aggregator) & **M06** (Placement Readiness Predictor).
- **Methodological Approach**: Construct a unified 22-dimensional Student Profile Vector (SPV) combining continuous academic metrics (CGPA, core CS scores), dense semantic resume vectors (`cosine_similarity`), coding execution pass rates, and paralinguistic interview scores into a normalized feature tensor.
- **Evaluation Protocol**: Ablation study comparing classification accuracy and Macro-$F_1$ of the full multimodal SPV model against unimodal sub-models (Academic-Only, Resume-Only, Interview-Only) on a multi-institutional cohort ($N \ge 1,000$).

---

### RG2: Static, Single-Snapshot Prediction Lacking Longitudinal Modeling
- **Gap ID**: `RG2` (Validated from Candidate Gap CG2).
- **Gap Statement**: Existing educational and placement predictive models evaluate candidate employability as a single, static point-in-time snapshot (typically measured at the end of Year 3 or Year 4), failing to capture dynamic learning velocity, habit persistence, skill acquisition trajectory, or temporal decay over time.
- **Supporting Literature**: **Paper02** (Van Wyk & Du Plessis 2025), **Paper05** (Chen 2024), **Paper33** (Al-Shabandar 2019/2025), **Paper44** (Azeez et al. 2026).
- **Phase 02 Evidence**: `Learning_Analytics_Comparison.md`: Out of 44 studies, only 3 incorporated multi-temporal observations. Static models cannot distinguish between a student with an upward trajectory and a student with declining academic momentum.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 9.4/10). Formulates the temporal modeling imperative.
- **PRIE Research Objective**: **RO3** (Dynamic Longitudinal Sequence Modeling & Multi-Horizon Placement Forecasting).
- **PRIE Research Question**: **RQ3** (Longitudinal vs Static Benchmark).
- **Relevant PRIE Component**: **M06** (Temporal Sequence Track) & **M11** (Behavioral Telemetry Engine).
- **Methodological Approach**: Implement Temporal Fusion Transformers (TFT) with Variable Selection Networks and multi-head temporal self-attention to model longitudinal interaction sequences across 4 semesters, predicting placement readiness at 12-month, 6-month, and 3-month horizons.
- **Evaluation Protocol**: Multi-horizon forecasting benchmark measuring Quantile Loss ($q_{0.1}, q_{0.5}, q_{0.9}$), MAE, and RMSE against static XGBoost with lagged features and standard LSTM networks.

---

### RG3: Descriptive Feature Attribution Lacking Prescriptive Counterfactuals
- **Gap ID**: `RG3` (Validated from Candidate Gap CG3).
- **Gap Statement**: Explainable AI implementations in higher education are overwhelmingly restricted to descriptive post-hoc attribution (e.g., standard SHAP summary beeswarms and LIME feature weights) that inform students *why* they were classified as unready, without providing distance-constrained, feasible, prescriptive counterfactual recourse indicating *what specific minimum actions* will achieve placement readiness.
- **Supporting Literature**: **Paper02** (Van Wyk 2025), **Paper18** (Hidayatulloh 2026), **Paper19** (Joshi & Khan 2025), **Paper22** (Olipas 2025), **Paper32** (Talmoudi 2026), **Paper34** (Babu & Saravanan 2025).
- **Phase 02 Evidence**: `XAI_Comparison.md`: 100% of reviewed XAI papers stopped at descriptive attribution. None implemented constraint-optimized counterfactual generation with immutable feature locking.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 9.8/10). Identifies the "Descriptive-to-Prescriptive Chasm."
- **PRIE Research Objective**: **RO4** (Distance-Constrained Prescriptive Counterfactual Career Remediation).
- **PRIE Research Question**: **RQ4** (Prescriptive Recourse vs Descriptive Attribution).
- **Relevant PRIE Component**: **M07** (Prescriptive Explainability Engine) & **M08** (Roadmap Generator).
- **Methodological Approach**: Combine TreeSHAP (for descriptive global and local attribution) with DiCE (Diverse Counterfactual Explanations) constrained by domain concept prerequisite DAGs, locking immutable demographic features and minimizing $L_1$ student intervention effort.
- **Evaluation Protocol**: Controlled human-in-the-loop study with 60 engineering students; measure Counterfactual Proximity ($L_1$), Sparsity ($L_0$), Actionability Score ($\ge 80\%$), and 30-day milestone remediation completion rate against a SHAP-only control group.

---

### RG4: Spatial Layout Destruction in Multi-Column ATS Resume Parsing
- **Gap ID**: `RG4` (Validated from Candidate Gap CG4).
- **Gap Statement**: Automated recruitment screening and resume parsing frameworks rely predominantly on flat-text OCR or sequential regex string matching that destroys 2D spatial layouts, interleaving parallel multi-column text and scrambling technical skills, project dates, and institutional credentials in over 60% of non-standard candidate resumes.
- **Supporting Literature**: **Paper11** (Mishra 2025), **Paper12** (Roy 2024), **Paper17** (Verma & Mehta 2026), **Paper36** (Suryawanshi 2025), **Paper37** (Kaushik 2025), **Paper42** (Davenport 2025).
- **Phase 02 Evidence**: `ATS_Comparison.md`: Multi-column layout destruction identified as the #1 technical vulnerability of existing campus ATS software, leading to false negative rejection rates between 55% and 68%.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 9.2/10).
- **PRIE Research Objective**: **RO1** (Multimodal Document Intelligence & Spatial Skill Extraction).
- **PRIE Research Question**: **RQ1** (Spatial Layout Transformers vs Flat-Text NER).
- **Relevant PRIE Component**: **M02** (Resume Intelligence & Multi-Column ATS Matcher).
- **Methodological Approach**: Implement LayoutLMv3 vision-language transformer incorporating 2D spatial bounding box coordinates ($[x_0, y_0, x_1, y_1]$) and visual document patches, combined with Sentence-BERT (`all-MiniLM-L6-v2`) dense embeddings for semantic JD alignment.
- **Evaluation Protocol**: Entity Extraction Precision, Recall, and Boundary-F1 benchmark on 200 real-world resumes (100 single-column, 100 complex multi-column) against spaCy NER and Tesseract flat OCR baselines.

---

### RG5: Conversational Latency Bottlenecks & Missing Code Sandboxing in Mock Interviews
- **Gap ID**: `RG5` (Validated from Candidate Gap CG5).
- **Gap Statement**: Automated mock interview systems suffer from compounding conversational turn-taking latency ($>2.8$s) caused by sequential cloud API pipelines, which breaks natural dialogue cadence and causes student anxiety, while completely omitting secure, live execution sandboxes for validating practical coding skills during technical interview rounds.
- **Supporting Literature**: **Paper03** (Joshi 2025), **Paper14** (Deshmukh 2025), **Paper15** (Inamdar 2025), **Paper27** (Amarnath 2025), **Paper28** (Gupta 2025), **Paper29** (Srinivasan 2025), **Paper30** (Kulkarni 2024), **Paper38** (Pillai 2026).
- **Phase 02 Evidence**: `Interview_Comparison.md`: Turn latency across commercial API pipelines averaged 3.4 seconds; 0 out of 8 mock interview systems implemented isolated Docker code execution.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 9.5/10).
- **PRIE Research Objective**: **RO2** (Low-Latency Conversational Coaching & Secure Code Sandboxing).
- **PRIE Research Question**: **RQ2** (Conversational Latency & Panel Correlation).
- **Relevant PRIE Component**: **M05** (Multimodal Mock Interview Coach).
- **Methodological Approach**: Architect a streaming chunked audio pipeline using Whisper ASR and local quantized SLM (Llama-3-8B via vLLM) to achieve sub-1.5s voice turnaround; execute MediaPipe FaceMesh in browser WebAssembly for zero-trust client vision; deploy ephemeral Docker containers for live coding unit test validation.
- **Evaluation Protocol**: End-to-end Voice-to-Voice Latency profiling ($<1.5$s target); Pearson correlation ($r \ge 0.70$) between PRIE interview scores and blinded ratings from a 5-member enterprise recruiter panel.

---

### RG6: Unverified Distractor Quality and Uncalibrated Difficulty in AQG
- **Gap ID**: `RG6` (Validated from Candidate Gap CG6).
- **Gap Statement**: Automatic question generation (AQG) in higher education relies on unconstrained large language model prompting that frequently hallucinates domain facts and generates trivial, non-functional distractors that fail standard psychometric discrimination metrics, rendering diagnostic assessments ineffective for pinpointing student conceptual voids.
- **Supporting Literature**: **Paper25** (Wang 2026), **Paper26** (Fernandez & Gomez 2025), **Paper39** (Kurdi 2020).
- **Phase 02 Evidence**: `Future_Work_Matrix.md`: 78% of LLM-generated MCQs suffer from non-functional distractors that can be eliminated through simple grammatical or superficial elimination.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 8.9/10).
- **PRIE Research Objective**: **RO5** (Causal Graph-Guided Cognitive Question Generation & Assessment Calibrations).
- **PRIE Research Question**: **RQ5** (Causal Graph AQG vs Unconstrained Prompting).
- **Relevant PRIE Component**: **M03** (Adaptive Assessment) & **M10** (Causal Concept AQG Engine).
- **Methodological Approach**: Ground Chain-of-Thought LLM question generation in verified Computer Science Causal Concept Directed Acyclic Graphs (DAGs), ensuring distractors reflect specific verified conceptual misconception branches.
- **Evaluation Protocol**: Item Difficulty ($p \in [0.30, 0.70]$), Item Discrimination Index ($DI \ge 0.35$), and Distractor Plausibility Index ($DPI \ge 0.70$) evaluated across 300 student quiz attempts.

---

### RG7: Cold-Start Vulnerability and Lack of Market-Aligned Career Pathways
- **Gap ID**: `RG7` (Validated from Candidate Gap CG7).
- **Gap Statement**: Recommendation and pathway generation frameworks in educational and career counseling collapse when applied to cold-start students or rare career transitions due to sparse collaborative filtering matrices, while generating generic advice disconnected from real-time corporate hiring requirement shifts.
- **Supporting Literature**: **Paper04** (Patel 2024), **Paper13** (Zhang 2023), **Paper16** (Tan 2024), **Paper35** (Qin 2020), **Paper41** (Consortium 2026), **Paper43** (Rajeevan 2026).
- **Phase 02 Evidence**: `Recommendation_Comparison.md`: Extreme cold-start matrix sparsity ($>99.2\%$) prevents collaborative filtering from generating valid pathways for junior students.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 9.1/10).
- **PRIE Research Objective**: **RO4** (Prescriptive Remediation) & **RO6** (Closed-Loop Platform).
- **PRIE Research Question**: **RQ4** & **RQ6**.
- **Relevant PRIE Component**: **M04** (Skill Gap Engine) & **M08** (Personalized Roadmap Generator).
- **Methodological Approach**: Formulate career pathway generation as a graph traversal problem across a curriculum-to-market ontology DAG, computing the shortest topological path that resolves diagnosed skill gaps while respecting prerequisite constraints.
- **Evaluation Protocol**: Recommendation Precision@K, Recall@K, Catalog Coverage, Gini Diversity, and student milestone completion rate.

---

### RG8: Lack of Closed-Loop Multi-Stakeholder Governance and Privacy Compliance
- **Gap ID**: `RG8` (Validated from Candidate Gap CG8).
- **Gap Statement**: Existing educational career systems operate in an open loop where predictive outputs are never dynamically re-ingested into model retraining, while completely excluding faculty mentors and corporate placement officers from synchronized governance, and failing to provide mathematically verified data privacy compliance under regulations like POPIA and FERPA.
- **Supporting Literature**: **Paper02** (Van Wyk 2025), **Paper41** (Consortium 2026), **Paper44** (Azeez 2026).
- **Phase 02 Evidence**: `Architecture_Comparison.md`: 41 out of 44 systems were pure open-loop prototypes with zero longitudinal feedback integration or formal role-based privacy architectures.
- **Phase 03 Validation**: Validated in `Gap_Validation.md` (Score: 9.3/10).
- **PRIE Research Objective**: **RO6** (Closed-Loop Multi-Stakeholder Digital Twin Integration & Privacy Compliance).
- **PRIE Research Question**: **RQ6** (Closed-Loop Digital Twin vs Point Solutions).
- **Relevant PRIE Component**: **M12** (Triangular Digital Twin & Closed-Loop Orchestrator).
- **Methodological Approach**: Implement a synchronized triangular digital twin maintaining real-time readiness representations across Student, Faculty Advisor, and Placement Cell dashboards, guarded by differential privacy ($\epsilon \le 1.0$) and automated telemetry feedback into model updating loops.
- **Evaluation Protocol**: Institutional placement conversion rate uplift, faculty mentoring intervention efficiency (time-to-intervention reduction $\ge 40\%$), and empirical privacy leakage audits.

---

## 3. Summary Gap-to-Solution Traceability Grid

| Gap ID | Research Gap Summary | Core PRIE Module | Primary Algorithmic Method | Quantitative Target / Verification Metric |
|:---:|:---|:---:|:---|:---|
| **RG1** | Unimodal Data Silos | **M01, M06** | 22-Dimensional Student Profile Vector (SPV) + XGBoost | Macro-$F_1 \ge 0.88$ ($>10\%$ uplift over unimodal baselines) |
| **RG2** | Static Single-Point Predictions | **M06, M11** | Temporal Fusion Transformer (TFT) with Multi-Head Attention | Multi-horizon Quantile Loss; MAE reduction $\ge 12\%$ vs LSTM |
| **RG3** | Descriptive-Only XAI | **M07, M08** | TreeSHAP + DiCE Constraint-Optimized Counterfactuals | Actionability Score $\ge 80\%$; Counterfactual Proximity $L_1 \le 0.15$ |
| **RG4** | Multi-Column Resume Layout Destruction | **M02** | LayoutLMv3 2D Spatial OCR + Sentence-BERT Embeddings | Boundary-F1 $\ge 0.90$ on multi-column resumes ($>20\%$ over spaCy) |
| **RG5** | Interview Turn Latency & Lack of Sandbox | **M05** | Streaming Whisper ASR + Local Llama-3-8B + Docker Sandbox | Voice-to-voice latency $<1.5$s; Pearson $r \ge 0.70$ with HR panel |
| **RG6** | Trivial Distractors & Hallucinated AQG | **M03, M10** | CS Causal Concept DAG + Chain-of-Thought LLM | Item Discrimination $DI \ge 0.35$; Distractor Plausibility $DPI \ge 0.70$ |
| **RG7** | Cold-Start Collaborative Filtering Collapse| **M04, M08** | Prerequisite Ontology Graph Traversal ($A^*$ Shortest Path)| Precision@5 $\ge 0.85$; Catalog Coverage $\ge 90\%$ |
| **RG8** | Open-Loop Architecture & Privacy Deficits | **M12** | Triangular Digital Twin + Differential Privacy ($\epsilon \le 1.0$)| Institutional placement conversion uplift $\ge 15\%$ |

**Traceability Guarantee**: Every single validated research gap from Phase 03 directly dictates a concrete, mathematically defined subsystem in PRIE, accompanied by an empirical evaluation protocol.
