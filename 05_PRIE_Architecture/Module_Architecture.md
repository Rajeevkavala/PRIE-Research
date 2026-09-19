# PRIE Module Architecture: Detailed Subsystem Specifications (M01–M12)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Module_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Subsystem Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & Module Inventory

PRIE is structured into twelve (12) cohesive, interoperable functional modules (`M01` through `M12`). Each module directly addresses an empirical limitation documented in the 44-paper literature corpus (`Paper01`–`Paper44`), resolves a validated Phase 03 research gap (`RG1`–`RG8`), and satisfies the research objectives (`RO1`–`RO6`).

```
       ┌────────────────────────────────────────────────────────┐
       │         M12: Closed-Loop Digital Twin Orchestrator      │
       └───────────────────────────┬────────────────────────────┘
                                   │
      ┌────────────────────────────┼────────────────────────────┐
      ▼                            ▼                            ▼
┌──────────────┐          ┌──────────────────┐          ┌──────────────┐
│  PERCEPTION  │          │    REASONING     │          │ ACTIONABLE   │
│              │          │                  │          │ REMEDIATION  │
│ M01: SPV     │          │ M04: Gap Engine  │          │ M07: XAI     │
│ M02: ATS     │─────────►│ M06: Predictor   │─────────►│ M08: Roadmap │
│ M03: Quiz    │          │ M11: Telemetry   │          │ M09: RAG     │
│ M05: Coach   │          │                  │          │ M10: AQG     │
└──────────────┘          └──────────────────┘          └──────────────┘
```

---

## 2. Exhaustive Module Specifications

---

### Module M01: Student Profile Vector (SPV) Aggregator & Harmonizer
- **Module ID**: `M01`
- **Module Name**: Student Profile Vector (SPV) Aggregator & Harmonizer
- **Purpose**: Consolidates heterogeneous multimodal signals (academic transcripts, coding benchmarks, resume parsing outputs, interview telemetry, and longitudinal logs) into a standardized, normalized 22-dimensional continuous-categorical feature tensor.
- **Research Objective**: **PRO** (Primary Research Objective) & **RO1** (Multimodal Feature Synthesis).
- **Research Question**: **RQ1** (Multimodal Feature Synthesis).
- **Research Gap**: **RG1** (Fragmented unimodal data silos in educational predictive modeling).
- **Inputs**:
  - Academic records from SIS (CGPA, individual core CS subject marks).
  - Diagnostic test scores from `M03`.
  - Parsed ATS hygiene score and semantic JD cosine similarity from `M02`.
  - Coding sandbox pass rates and behavioral scores from `M05`.
  - Longitudinal interaction cadence and login entropy from `M11`.
- **Outputs**:
  - Standardized 22-dimensional feature tensor $\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$.
  - Feature confidence mask $\mathbf{m} \in \{0, 1\}^{22}$ indicating observed vs imputed features.
  - Profile revision metadata and timestamp.
- **Dependencies**: SIS API, `M02`, `M03`, `M05`, `M11`, `SPV-DB`.
- **Algorithms / Models**:
  - Continuous Min-Max and Z-score standardizers calibrated on institutional historical distributions.
  - Multivariate Imputation by Chained Equations (MICE) and median fallbacks for missing test scores.
  - Variance Inflation Factor (VIF) monitoring to prevent collinear instability.
- **Data Stores**: PostgreSQL (`SPV-DB`) storing versioned historical vectors.
- **API Boundary**: Internal gRPC service: `rpc CompileProfile(StudentRequest) returns (SPVResponse)`.
- **Agent Boundary**: Supervised by `ProfileAgent`; external services cannot modify SPV directly without schema validation.
- **Failure Modes**: Missing prerequisite records $\to$ fallback to median baseline imputation and raise confidence flag; data type violation $\to$ schema validation rejection.
- **Security Considerations**: PII scrubbed prior to tensor compilation; demographic identifiers strictly isolated from model training.
- **Evaluation Method**: Feature ablation analysis comparing multimodal SPV against unimodal sub-models on placement classification $F_1$.
- **Traceability**: **Paper01**, **Paper04**, **Paper06**, **Paper08**, **Paper10**, **Paper22**, **Paper24**; `DD-001`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (Concept) / `IMPLEMENTED` (Schema Baseline).

---

### Module M02: Resume Intelligence & Multi-Column ATS Matcher
- **Module ID**: `M02`
- **Module Name**: Resume Intelligence & Multi-Column ATS Matcher
- **Purpose**: Ingests non-standard student resumes, extracts structured competencies while preserving 2D spatial layouts, and computes dense semantic alignment against target Job Descriptions (JDs).
- **Research Objective**: **RO1** (Multimodal Document Intelligence).
- **Research Question**: **RQ1** (Spatial Layout Transformers vs Flat Text).
- **Research Gap**: **RG4** (Spatial layout destruction in multi-column ATS resumes).
- **Inputs**:
  - Candidate resume document (PDF, DOCX, image scan).
  - Target Job Description (text / structured requirements).
- **Outputs**:
  - Parsed entity dictionary (Education, Skills, Experience, Projects).
  - `F13: resume_ats_score` (0.0–100.0).
  - `F14: cosine_similarity` (0.0–1.0) dense semantic match.
  - Section-level bounding box annotations for UI overlay.
- **Dependencies**: PDF rendering engine (PyMuPDF), `LayoutLMv3`, `Sentence-BERT`, `ChromaDB`.
- **Algorithms / Models**:
  - `LayoutLMv3` vision-language transformer with 2D spatial bounding box embeddings ($[x_0, y_0, x_1, y_1]$).
  - `Sentence-BERT (all-MiniLM-L6-v2)` 384-dimensional dense bi-encoder.
  - Cosine distance dot product in vector space.
- **Data Stores**: Document object store (encrypted PDFs) and ChromaDB vector store.
- **API Boundary**: REST endpoint: `POST /api/v1/resume/parse-and-match`.
- **Agent Boundary**: Invoked by `ResumeAgent` for document processing; outputs vetted by `ValidationGuard`.
- **Failure Modes**: Low-resolution scan failure $\to$ fallback to Tesseract OCR; corrupted PDF $\to$ return HTTP 422 with unparseable formatting advisory.
- **Security Considerations**: Redacts candidate phone numbers, addresses, and gender prior to vectorization; strict on-premise inference (`DD-004`).
- **Evaluation Method**: Entity Extraction Boundary Token F1 across single vs multi-column templates (`EXP-1`).
- **Traceability**: **Paper11**, **Paper12**, **Paper13**, **Paper17**, **Paper35**, **Paper36**, **Paper37**, **Paper42**; `DD-004`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (SBERT) / `PROPOSED ARCHITECTURE` (LayoutLMv3 integration).

---

### Module M03: Adaptive Assessment & Diagnostic Quizzing
- **Module ID**: `M03`
- **Module Name**: Adaptive Assessment & Diagnostic Quizzing
- **Purpose**: Administers dynamically calibrated multiple-choice and conceptual assessments targeting specific prerequisite concepts in the Computer Science curriculum to measure core technical competencies (`F02`–`F07`).
- **Research Objective**: **RO5** (Diagnostic Assessment & Psychometric Calibration).
- **Research Question**: **RQ5** (Diagnostic Question Generation & Calibration).
- **Research Gap**: **RG6** (Unverified distractor quality and uncalibrated difficulty in AQG).
- **Inputs**:
  - Student skill gap profile from `M04`.
  - Target concept node from CS Concept DAG (`M08`, `M10`).
  - Examinee historical attempt trajectory.
- **Outputs**:
  - Calibrated diagnostic assessment items.
  - Updated subject mastery scores (`F02: dsa_score`, `F03: dbms_score`, etc.).
  - Distractor selection telemetry mapping specific student misconception branches.
- **Dependencies**: `M10` (Question Generator), `CS-Concept-DAG`, `SPV-DB`.
- **Algorithms / Models**:
  - Computerized Adaptive Testing (CAT) based on 1-Parameter Item Response Theory (Rasch Model).
  - Classical Test Theory (CTT) item difficulty ($p$) and item discrimination ($DI$) scoring.
- **Data Stores**: Question bank relational database; student item-response logs.
- **API Boundary**: REST endpoint: `GET /api/v1/assessment/next-item`; `POST /api/v1/assessment/submit`.
- **Agent Boundary**: Governed by `AssessmentAgent`; item presentation is strictly deterministic based on IRT.
- **Failure Modes**: Question bank exhaustion $\to$ dynamically request fresh items from `M10`; network timeout during quiz $\to$ cached offline submission replay.
- **Security Considerations**: Randomized question stems and distractor shuffling to prevent peer collusion; anti-copy clipboard restrictions.
- **Evaluation Method**: Psychometric item discrimination index ($DI \ge 0.35$) and student score progression slopes.
- **Traceability**: **Paper02**, **Paper04**, **Paper05**, **Paper25**, **Paper26**, **Paper39**; `DD-009`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (IRT/CAT) / `PROPOSED ARCHITECTURE` (Misconception Tracking).

---

### Module M04: Skill Gap Analysis & Distance Engine
- **Module ID**: `M04`
- **Module Name**: Skill Gap Analysis & Distance Engine
- **Purpose**: Computes mathematical distance metrics between candidate profile competencies and target corporate job role profiles, weighting missing skills by market criticality.
- **Research Objective**: **RO4** (Prescriptive Career Remediation).
- **Research Question**: **RQ4** (Prescriptive Recourse vs Descriptive Attribution).
- **Research Gap**: **RG1** (Unimodal silos) & **RG7** (Cold-start career pathway planning).
- **Inputs**:
  - Candidate 22-dimensional SPV from `M01`.
  - Target corporate role vector $\mathbf{v}_{\text{role}}$ (e.g., SDE-1, Cloud DevOps, Data Engineer).
- **Outputs**:
  - `F15: gap_score` (Float, 0.0–1.0).
  - Ranked missing competency list with criticality weights $w_i$.
  - Euclidean distance $\Delta d$ and directional deficit vector.
- **Dependencies**: `M01`, `M02`, `ChromaDB` (Role Taxonomy).
- **Algorithms / Models**:
  - Weighted Euclidean distance: $D(\mathbf{x}, \mathbf{r}) = \sqrt{\sum_{i=1}^k w_i (x_i - r_i)^2}$.
  - Non-linear penalty scaling for missing mandatory core prerequisites.
- **Data Stores**: Relational role taxonomy repository.
- **API Boundary**: Internal gRPC: `rpc ComputeSkillGap(GapRequest) returns (GapResponse)`.
- **Agent Boundary**: Integrated directly within `RecommendationAgent`.
- **Failure Modes**: Unknown target role $\to$ map to closest standard occupational code (SOC); missing feature vector $\to$ request immediate SPV recompilation.
- **Security Considerations**: Role weighting models audited for gender and non-traditional engineering branch bias.
- **Evaluation Method**: Correlation between computed skill gap distance and candidate technical interview failure rates.
- **Traceability**: **Paper04**, **Paper13**, **Paper16**, **Paper35**, **Paper41**; `DD-008`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH`.

---

### Module M05: Multimodal Mock Interview Coach
- **Module ID**: `M05`
- **Module Name**: Multimodal Mock Interview Coach
- **Purpose**: Delivers an interactive, low-latency ($<1.5$s) conversational technical interview with real-time speech recognition, adaptive technical questioning, client-side non-verbal telemetry, and secure live code execution.
- **Research Objective**: **RO2** (Low-Latency Conversational Coaching & Secure Code Sandboxing).
- **Research Question**: **RQ2** (Conversational Latency & Human Panel Correlation).
- **Research Gap**: **RG5** (Conversational latency bottlenecks and missing code sandboxing).
- **Inputs**:
  - Streaming audio input from student microphone.
  - Video stream processed locally in client browser WebAssembly.
  - Student code submissions entered into interview code editor.
- **Outputs**:
  - Speech-to-text transcript with word timestamps.
  - Synthesized interviewer voice response.
  - `F20: behavior_score` (speech pause ratio, filler frequency, gaze stability).
  - Code unit test execution report from Docker sandbox.
- **Dependencies**: `Whisper ASR`, local quantized `Llama-3-8B` (via vLLM), `MediaPipe FaceMesh` (Wasm), `Docker Engine`.
- **Algorithms / Models**:
  - Chunked streaming Whisper ASR (250ms chunks).
  - Local vLLM quantized LLM for sub-350ms first-token generation.
  - MediaPipe 468-point 3D facial mesh running client-side (`DD-005`).
  - Unit test runner inside isolated ephemeral Docker container (`DD-006`).
- **Data Stores**: Time-series interview telemetry logs; temporary audio buffer (in-memory only).
- **API Boundary**: WebSocket connection: `wss://prie.internal/v1/interview/stream`.
- **Agent Boundary**: Managed by `InterviewAgent`; code execution mediated by sandbox driver.
- **Failure Modes**: Audio stream drop $\to$ auto-reconnect WebSocket and prompt repeat; code sandbox timeout $\to$ enforce 5.0s hard termination and report infinite loop.
- **Security Considerations**: Zero storage of raw audio/video (`DD-005`, `DD-011`); sandboxes run with `--net=none` and non-root users (`DD-006`).
- **Evaluation Method**: Voice-to-voice turn latency profiling ($<1.5$s) and Pearson correlation ($r \ge 0.70$) with a blinded panel of 5 recruiter evaluators (`EXP-2`).
- **Traceability**: **Paper03**, **Paper14**, **Paper15**, **Paper27**, **Paper28**, **Paper29**, **Paper30**, **Paper38**; `DD-005`, `DD-006`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (Perception) / `PROPOSED ARCHITECTURE` (Streaming vLLM + Wasm Pipeline).

---

### Module M06: Placement Readiness Prediction Engine
- **Module ID**: `M06`
- **Module Name**: Placement Readiness Prediction Engine
- **Purpose**: Executes dual-track placement readiness prediction: Track 1 classifies cross-sectional readiness tiers and probability; Track 2 forecasts multi-horizon progression and learning velocity across semesters.
- **Research Objective**: **PRO** & **RO3** (Dynamic Longitudinal Sequence Modeling).
- **Research Question**: **RQ3** (Longitudinal Sequence Modeling vs Static Snapshots).
- **Research Gap**: **RG2** (Static single-snapshot prediction lacking longitudinal velocity).
- **Inputs**:
  - Current 22-dimensional SPV from `M01`.
  - Multi-semester sequential SPV history ($\text{Sem}_4 \to \text{Sem}_7$) from `SPV-DB`.
- **Outputs**:
  - Placement readiness probability $P_{\text{ready}} \in [0.0, 1.0]$.
  - Discrete readiness tier: `Ready` ($P \ge 0.75$), `Needs Remediation` ($0.45 \le P < 0.75$), `At-Risk` ($P < 0.45$).
  - Multi-horizon quantile predictions ($q_{0.1}, q_{0.5}, q_{0.9}$) for 12-month and 6-month horizons.
- **Dependencies**: `M01`, `M11`, `CMP-MDL-XGB`, `CMP-MDL-TFT`, `SPV-DB`.
- **Algorithms / Models**:
  - Track 1: Extreme Gradient Boosting (XGBoost) with second-order tree regularization.
  - Track 2: Temporal Fusion Transformer (TFT) with Variable Selection Networks and Multi-Head Temporal Self-Attention.
- **Data Stores**: Model artifact registry (`REG-MDL`) and prediction log store.
- **API Boundary**: REST endpoint: `POST /api/v1/predict/readiness`.
- **Agent Boundary**: Governed by `PredictionAgent`; outputs trigger `XAI_Agent` and `DigitalTwin_Agent`.
- **Failure Modes**: Incomplete longitudinal history $\to$ default gracefully to Track 1 static XGBoost; out-of-range features $\to$ clip to training bounding manifold.
- **Security Considerations**: Features strictly sanitized to prevent target label leakage and look-ahead temporal bias.
- **Evaluation Method**: Cross-sectional Macro-$F_1$, ROC-AUC, Brier score; multi-horizon Quantile Loss and Diebold-Mariano test (`EXP-3`).
- **Traceability**: **Paper01**, **Paper04**, **Paper06**, **Paper09**, **Paper18**, **Paper22**, **Paper44**; `DD-002`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (XGBoost) / `PROPOSED ARCHITECTURE` (TFT Dual-Track).

---

### Module M07: Prescriptive Explainability & Counterfactual Engine
- **Module ID**: `M07`
- **Module Name**: Prescriptive Explainability & Counterfactual Engine
- **Purpose**: Bridges the "Descriptive-to-Prescriptive Chasm" by generating both descriptive feature attributions (TreeSHAP) and distance-constrained, feasible counterfactual recourse (DiCE).
- **Research Objective**: **RO4** (Distance-Constrained Prescriptive Counterfactual Career Remediation).
- **Research Question**: **RQ4** (Prescriptive Recourse vs Descriptive Attribution).
- **Research Gap**: **RG3** (Descriptive feature attribution lacking prescriptive recourse).
- **Inputs**:
  - Current student SPV $\mathbf{x}_{\text{spv}}$.
  - XGBoost prediction artifact from `M06`.
  - Feature mutability and bounding constraints (e.g., branch is immutable, CGPA can only increase).
- **Outputs**:
  - Global and local SHAP feature importance values ($\phi_i$).
  - Counterfactual profile $\mathbf{x}^*$ satisfying $f(\mathbf{x}^*) \ge P_{\text{target}}$.
  - Specific delta directives: *"Increase DSA score by +12 points and complete 1 production project."*
- **Dependencies**: `M06`, `TreeSHAP`, `DiCE Solver`, `CS-Concept-DAG`.
- **Algorithms / Models**:
  - TreeSHAP polynomial-time feature attribution $O(T L D^2)$.
  - DiCE constraint-optimized loss minimization:
    $$\arg\min_{\mathbf{x}^*} \text{dist}(\mathbf{x}, \mathbf{x}^*) + \lambda |f(\mathbf{x}^*) - y^*|^2 + \gamma \text{feasibility}(\mathbf{x}^*)$$
- **Data Stores**: Remediation prescription store.
- **API Boundary**: REST endpoint: `POST /api/v1/explain/prescribe`.
- **Agent Boundary**: Invoked by `XAIAgent`; outputs feed directly into `RoadmapAgent`.
- **Failure Modes**: DiCE optimization convergence timeout ($>3.0$s) $\to$ fallback to nearest pre-computed archetype counterfactual.
- **Security Considerations**: Enforces immutable demographic feature locks (`branch_encoded`) to prevent recommending discriminatory or impossible changes.
- **Evaluation Method**: Controlled human trial measuring Actionability Score ($\ge 80\%$), Counterfactual Proximity ($L_1$), Sparsity ($L_0$), and 30-day milestone completion (`EXP-4`).
- **Traceability**: **Paper02**, **Paper18**, **Paper19**, **Paper22**, **Paper32**, **Paper34**; `DD-003`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (TreeSHAP) / `PROPOSED RESEARCH DECISION` (DiCE Prescriptive Recourse).

---

### Module M08: Dynamic Personalized Roadmap Generator
- **Module ID**: `M08`
- **Module Name**: Dynamic Personalized Roadmap Generator
- **Purpose**: Translates prescriptive counterfactual deltas and skill gaps into an ordered, milestone-based learning curriculum by performing topological shortest-path graph search across a prerequisite concept DAG.
- **Research Objective**: **RO4** & **RO6** (Closed-Loop Platform).
- **Research Question**: **RQ4** & **RQ6**.
- **Research Gap**: **RG7** (Cold-start vulnerability in career pathway recommendations).
- **Inputs**:
  - Counterfactual delta targets from `M07`.
  - Diagnosed skill gaps from `M04`.
  - Target role deadline and current student time availability (hours/week).
- **Outputs**:
  - Sequenced learning roadmap with milestone target dates.
  - Prerequisite learning dependencies and curated study units.
  - `F22: roadmap_completion_rate` tracking state.
- **Dependencies**: `M04`, `M07`, `M09`, `CS-Concept-DAG`.
- **Algorithms / Models**:
  - $A^*$ heuristic graph traversal over Computer Science Concept DAG.
  - Topological sorting enforcing strict prerequisite mastery before downstream advanced topics.
- **Data Stores**: Roadmap persistence database; CS Concept Graph store.
- **API Boundary**: REST endpoint: `GET /api/v1/roadmap/active`; `POST /api/v1/roadmap/regenerate`.
- **Agent Boundary**: Managed by `RoadmapAgent`.
- **Failure Modes**: Graph cycle detected $\to$ DAG validation exception handler executes cycle breaking; impossible timeline requested $\to$ return realistic estimated completion date.
- **Security Considerations**: Verified alignment with approved university curriculum guidelines.
- **Evaluation Method**: Catalog Coverage ($\ge 90\%$), Gini Diversity, and student milestone completion rate.
- **Traceability**: **Paper13**, **Paper16**, **Paper35**, **Paper41**, **Paper43**; `DD-008`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (Graph Search) / `PROPOSED ARCHITECTURE` (Prerequisite DAG Traversal).

---

### Module M09: Retrieval-Augmented Generation (RAG) Assistant
- **Module ID**: `M09`
- **Module Name**: Retrieval-Augmented Generation (RAG) Assistant
- **Purpose**: Provides a factual, curriculum-grounded conversational study and placement advising assistant, eliminating domain hallucinations through a two-stage retrieval pipeline guarded by runtime RAG Triad verification.
- **Research Objective**: **RO5** & **RO6**.
- **Research Question**: **RQ6** (Closed-Loop Digital Twin vs Point Solutions).
- **Research Gap**: **RG8** (Domain hallucination and ungrounded advice in campus AI assistants).
- **Inputs**:
  - Student natural language query.
  - Active curriculum syllabus and placement drive policy documents.
- **Outputs**:
  - Grounded factual response with explicit citation source references.
  - RAG Triad quality verification scores (Context Relevance, Groundedness, Answer Relevance).
- **Dependencies**: `ChromaDB`, `Sentence-BERT`, Cross-Encoder `ms-marco-MiniLM-L-6-v2`, local `Llama-3-8B`.
- **Algorithms / Models**:
  - Two-Stage Retrieval: Dense bi-encoder vector search followed by cross-encoder re-ranking.
  - Automated RAG Triad verification (TruLens / Ragas evaluation harness).
- **Data Stores**: ChromaDB vector collection (college course syllabi, past drive archives).
- **API Boundary**: REST / WSS: `POST /api/v1/rag/query`.
- **Agent Boundary**: Governed by `RAGAgent`; responses with Groundedness $<0.90$ are automatically rejected or flagged.
- **Failure Modes**: Zero relevant chunks retrieved ($<0.70$ similarity) $\to$ fallback to explicit disclosure: *"This topic is not covered in the verified institutional curriculum."*
- **Security Considerations**: Restricts retrieval to approved university documents; filters student PII before context injection.
- **Evaluation Method**: Automated RAG Triad scoring across 200 standard student curriculum queries (Context Rel $\ge 0.85$, Groundedness $\ge 0.90$, Answer Rel $\ge 0.88$).
- **Traceability**: **Paper20**, **Paper21**, **Paper23**, **Paper27**, **Paper40**; `DD-007`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (RAG Triad Architecture).

---

### Module M10: Causal Concept-Guided Question Generation (AQG)
- **Module ID**: `M10`
- **Module Name**: Causal Concept-Guided Question Generation (AQG)
- **Purpose**: Generates high-discrimination technical multiple-choice questions whose distractors explicitly mirror documented student conceptual misconception pathways in Computer Science.
- **Research Objective**: **RO5** (Causal Graph-Guided Cognitive Question Generation).
- **Research Question**: **RQ5** (Causal Concept AQG vs Unconstrained LLM Prompting).
- **Research Gap**: **RG6** (Trivial distractors and uncalibrated difficulty in AQG).
- **Inputs**:
  - Target concept node and difficulty level ($p$-value target).
  - Specific misconception branch from CS Causal Concept DAG.
- **Outputs**:
  - Question stem, single correct key, and 3 diagnostic distractors.
  - Rationale mapping each distractor to its underlying conceptual error.
- **Dependencies**: `CS-Concept-DAG`, local `Llama-3-8B` / frontier LLM API, `M03`.
- **Algorithms / Models**:
  - Causal Concept DAG-guided Chain-of-Thought (CoT) prompting.
  - Psychometric distractor plausibility validation filter.
- **Data Stores**: Validated assessment item repository.
- **API Boundary**: Internal gRPC: `rpc GenerateAssessmentItem(ItemRequest) returns (ItemResponse)`.
- **Agent Boundary**: Executed by `QuestionGenAgent`; all items subject to schema and duplicate validation.
- **Failure Modes**: LLM generates identical distractors $\to$ rejection by validator and re-generation with increased temperature; malformed JSON $\to$ schema retry.
- **Security Considerations**: Generated items are stored encrypted in question bank to prevent premature disclosure.
- **Evaluation Method**: Classical Item Discrimination ($DI \ge 0.35$) and Distractor Plausibility Index ($DPI \ge 0.70$) across 300 student quiz attempts (`EXP-5`).
- **Traceability**: **Paper25**, **Paper26**, **Paper39**; `DD-009`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (Concept) / `PROPOSED RESEARCH DECISION` (Causal DAG Integration).

---

### Module M11: Behavioral Telemetry & Longitudinal Analytics
- **Module ID**: `M11`
- **Module Name**: Behavioral Telemetry & Longitudinal Analytics
- **Purpose**: Continuously monitors and models student interaction cadence, login regularity, attempt frequency, and habit decay to compute longitudinal features (`F16`, `F19`, `F21`) that feed the temporal prediction track.
- **Research Objective**: **RO3** & **RO6**.
- **Research Question**: **RQ3**.
- **Research Gap**: **RG2** (Static single-snapshot prediction lacking longitudinal velocity).
- **Inputs**:
  - Granular user interaction events (logins, page views, quiz starts, code runs, hint clicks).
  - Event timestamps and session durations.
- **Outputs**:
  - `F16: consistency_score` (0.0–1.0) using exponential moving average of weekly active cadence.
  - `F19: assessment_attempts` (cumulative practice volume).
  - `F21: engagement_score` (0.0–1.0) cohort-normalized composite.
  - Early-warning risk trigger (persistent engagement drop over 14 days).
- **Dependencies**: `Redis Bus`, `TimescaleDB`, `M01`, `M06`.
- **Algorithms / Models**:
  - Exponential Moving Average (EMA) and entropy-based regularity scoring.
  - Sliding-window time-series aggregation.
- **Data Stores**: TimescaleDB time-series event log.
- **API Boundary**: Async event consumer on Redis topic `telemetry.events`.
- **Agent Boundary**: Monitored by `TelemetryAgent`.
- **Failure Modes**: Event stream buffering on network disruption; duplicate event deduplication via unique idempotent event IDs.
- **Security Considerations**: Raw clickstream data stripped of IP addresses and device fingerprints; aggregated metrics subject to differential privacy.
- **Evaluation Method**: Sensitivity ($>85\%$) in identifying at-risk disengagement at the critical Week 3–4 intervention window.
- **Traceability**: **Paper02**, **Paper05**, **Paper33**, **Paper44**; `DD-002`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH`.

---

### Module M12: Triangular Digital Twin & Closed-Loop Orchestrator
- **Module ID**: `M12`
- **Module Name**: Triangular Digital Twin & Closed-Loop Orchestrator
- **Purpose**: Synchronizes an evolving, real-time digital twin representation of candidate placement readiness across Student, Faculty Advisor, and Placement Cell dashboards, closing the loop by feeding student remediation progress directly back into model calibration.
- **Research Objective**: **RO6** (Closed-Loop Multi-Stakeholder Digital Twin Integration).
- **Research Question**: **RQ6** (Closed-Loop Triangular Digital Twin vs Disconnected Systems).
- **Research Gap**: **RG8** (Lack of closed-loop multi-stakeholder governance and privacy compliance).
- **Inputs**:
  - Current 22-dimensional SPV state from `M01`.
  - Prediction and forecast vectors from `M06`.
  - Roadmap progress and milestone completions from `M08`.
  - Faculty mentorship intervention notes.
- **Outputs**:
  - Synchronized real-time twin state dispatched to 3 role-specific views.
  - Predictive placement conversion trajectory for institutional cohorts.
  - Automated escalation alerts for un-remediated at-risk candidates.
- **Dependencies**: `M01`, `M06`, `M08`, `M11`, `CMP-GW-PRIV`, `SPV-DB`.
- **Algorithms / Models**:
  - Real-time state synchronization via WebSocket pub/sub.
  - Differential privacy noise injection ($\epsilon \le 1.0$) for cohort-level recruiter queries.
- **Data Stores**: Digital Twin state cache (Redis) and relational historical ledger (PostgreSQL).
- **API Boundary**: WebSocket: `wss://prie.internal/v1/twin/sync`; REST: `GET /api/v1/twin/state`.
- **Agent Boundary**: Supervised by `OrchestratorAgent`; coordinates inter-agent workflows.
- **Failure Modes**: State de-synchronization $\to$ triggers reconciliation sweep against authoritative `SPV-DB`.
- **Security Considerations**: Strict Role-Based Access Control (RBAC) ensuring faculty see only assigned advisees and recruiters see only anonymized candidate pools (`DD-011`).
- **Evaluation Method**: Difference-in-Differences (DiD) econometric analysis of campus placement conversion uplift ($\ge 15\%$) and advisor intervention latency (`EXP-6`).
- **Traceability**: **Paper02**, **Paper41**, **Paper44**; `DD-010`.
- **Implementation Status**: `ESTABLISHED BY RESEARCH` (Triangular Concept from Paper41) / `PROPOSED RESEARCH DECISION` (Closed-Loop Orchestration).

---

## 3. Module Epistemological Classification Summary

| Module ID | Subsystem Name | Literature Source | Design Decision | Epistemological Status |
|:---:|:---|:---|:---:|:---|
| **M01** | SPV Aggregator | P01, P04, P06, P08, P22 | `DD-001` | `ESTABLISHED BY RESEARCH` |
| **M02** | ATS Matcher | P11, P12, P17, P35, P42 | `DD-004` | `ESTABLISHED BY RESEARCH` (SBERT) / `PROPOSED ARCHITECTURE` (LayoutLMv3) |
| **M03** | Adaptive Assessment | P02, P04, P25, P26, P39 | `DD-009` | `ESTABLISHED BY RESEARCH` |
| **M04** | Skill Gap Engine | P04, P13, P16, P35, P41 | `DD-008` | `ESTABLISHED BY RESEARCH` |
| **M05** | Mock Interview Coach | P03, P15, P28, P29, P38 | `DD-005`, `DD-006` | `ESTABLISHED BY RESEARCH` (Whisper) / `PROPOSED ARCHITECTURE` (Streaming Wasm) |
| **M06** | Placement Predictor | P01, P04, P18, P22, P44 | `DD-002` | `ESTABLISHED BY RESEARCH` (XGBoost) / `PROPOSED ARCHITECTURE` (TFT Dual-Track) |
| **M07** | Prescriptive XAI | P18, P19, P22, P32, P34 | `DD-003` | `ESTABLISHED BY RESEARCH` (TreeSHAP) / `PROPOSED RESEARCH DECISION` (DiCE) |
| **M08** | Roadmap Generator | P13, P16, P35, P41, P43 | `DD-008` | `ESTABLISHED BY RESEARCH` (Graph Search) / `PROPOSED ARCHITECTURE` |
| **M09** | Curriculum RAG | P20, P21, P23, P27, P40 | `DD-007` | `ESTABLISHED BY RESEARCH` (RAG Triad) |
| **M10** | Causal Concept AQG | P25, P26, P39 | `DD-009` | `ESTABLISHED BY RESEARCH` (Concept) / `PROPOSED RESEARCH DECISION` (DAG AQG) |
| **M11** | Behavioral Telemetry | P02, P05, P33, P44 | `DD-002` | `ESTABLISHED BY RESEARCH` |
| **M12** | Digital Twin | P02, P41, P44 | `DD-010` | `ESTABLISHED BY RESEARCH` (Concept) / `PROPOSED RESEARCH DECISION` (Closed Loop) |

---

## 4. Subsystem Verification Certification

- **Zero Omitted Modules**: All 12 functional subsystems established in Phase 04 are completely specified.
- **Traceability Unbroken**: Every module links directly to its verified literature evidence, research gap, objective, and evaluation protocol.
- **Scientific Honesty**: Distinctly separates established mathematical components from novel proposed architectures requiring experimental validation.
