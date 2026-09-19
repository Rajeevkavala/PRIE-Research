# Research Assumptions & Foundational Premises

**Project**: ScholarCamp — AI-Powered Placement Preparation and Career Acceleration Platform  
**Core System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `03_Research_Problem/Assumptions.md`  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers, 71 Processed Documents)  
**Cross-Analysis Foundation**: `02_Cross_Analysis/` (20 Authoritative Synthesis Documents)  
**Master Evidence Ledger**: `03_Research_Problem/PHASE_03_EVIDENCE_LEDGER.md`  
**Parent Scope**: `03_Research_Problem/Scope.md`  
**Date**: September 2026  
**Status**: Authoritative Assumptions Specification  

---

## 1. Epistemological Role of Assumptions in Educational AI

In designing and evaluating artificial intelligence systems within complex socio-technical environments like higher education and talent recruitment, explicit documentation of underlying assumptions is mandatory. In accordance with Phase 03 directives, every assumption documented below is directly relevant to the ScholarCamp / PRIE research ecosystem and reflects the structural realities substantiated by the 44 verified primary research papers.

---

## 2. Granular Categorical Assumptions

### 2.1 Data Assumptions
- **Authenticity & Integrity**: It is assumed that student academic records retrieved from institutional registrar databases and Learning Management Systems (LMS) represent authentic, uncorrupted evaluations of course performance [P02, P05, P10].
- **Sufficient Logging Resolution**: It is assumed that institutional digital learning platforms record student engagement at a minimum temporal resolution of weekly clickstream events and quiz submission timestamps, enabling sequence modeling [P08, P33, P44].
- **Representativeness of Resumes**: It is assumed that submitted PDF/DOCX resumes represent the student's genuine self-reported academic, project, and certification history, with formatting adhering to standard PDF document layout norms [P12, P17, P42].

### 2.2 Student Population Assumptions
- **Basic Digital Literacy**: It is assumed that target undergraduate engineering students possess standard digital literacy, personal access to a modern web browser (Chrome, Firefox, Edge), and basic computer hardware equipped with a functioning webcam and microphone [P03, P29, P30].
- **Sincere Engagement Intent**: It is assumed that students interact with the mock interview, coding sandbox, and adaptive quiz systems with genuine intent to improve their technical competence, rather than intentionally attempting to game or deceive the AI scoring rubrics [P27, P38].
- **English Language Medium of Instruction**: It is assumed that the primary medium of corporate technical recruitment interviews and assessment challenges is English, reflecting standard industry hiring conventions in the analyzed literature [P24, P28].

### 2.3 Ground-Truth Label Assumptions
- **Placement Outcome Validity**: It is assumed that institutional placement records (binary `Placed` vs `Unplaced` flags and corporate offer letters) constitute the definitive ground-truth label for employability prediction models [P01, P06, P07, P22].
- **Human Recruiter Panel Reliability**: It is assumed that independent corporate recruitment panels evaluating candidate mock interview videos and code submissions exhibit acceptable inter-rater reliability (Cohen’s $\kappa \ge 0.75$, Pearson $r \ge 0.82$) [P15, P28].
- **Course Prerequisite Topological Correctness**: It is assumed that university curriculum committees have established logically sound, acyclic prerequisite dependencies between introductory and advanced engineering courses [P13, P16].

### 2.4 Employment Outcome & Market Assumptions
- **Predictability of Placement Criteria**: It is assumed that corporate campus recruitment selection criteria (technical coding thresholds, core engineering knowledge, communication clarity, and behavioral poise) exhibit sufficient statistical consistency from year to year to enable predictive machine learning [P04, P09, P41].
- **Stability of Technical Skill Taxonomies**: It is assumed that foundational software engineering competencies (Data Structures, Algorithms, Object-Oriented Programming, Relational Databases) remain core hiring criteria across hiring seasons, even as specific cloud or framework trends evolve [P13, P17, P35].

### 2.5 Model Training & Algorithmic Assumptions
- **Tabular Ensemble Optimality**: In accordance with the cross-paper findings of Phase 02 (`Algorithm_Comparison.md` §3.1), it is assumed that Gradient Boosted Tree Ensembles (CatBoost, XGBoost, LightGBM) represent the optimal inductive bias for static tabular educational data, outperforming deep MLPs in training efficiency and sample efficiency [P01, P06, P22, P34].
- **Temporal Markovian Properties**: It is assumed that a student's current placement readiness state $\mathbf{s}_t$ can be effectively modeled by a finite temporal history of past engagement velocity ($\mathbf{s}_{t-1}, \dots, \mathbf{s}_{t-k}$) using self-attention mechanisms [P08, P44].
- **Feature Differentiability**: It is assumed that student attributes can be partitioned into immutable historical features (past semester GPA, 10th% marks) and mutable, intervenable features (weekly practice hours, LeetCode milestones, mock interview frequency) for counterfactual optimization [P19].

### 2.6 Feature Availability Assumptions
- **Multi-Source Data Accessibility**: It is assumed that the PRIE data pipeline can successfully ingest and merge student academic registrar records, LMS interaction logs, public GitHub repository metrics, and LeetCode problem-solving activity via institutional APIs or authenticated student oauth tokens [P09].
- **WebAssembly Client Capability**: It is assumed that client browser environments support WebAssembly and WebGL execution to process MediaPipe 3D FaceMesh landmark extraction locally at $\ge 30$ frames per second without hardware acceleration failures [P03, P14].

### 2.7 Evaluation & Benchmark Assumptions
- **Benchmark Stability**: It is assumed that public benchmark datasets (OULAD in P33, Kaggle Campus Placement in P01) and curated institutional corpora provide stationary test distributions for baseline comparative evaluations.
- **RAG Triad Validity**: In accordance with Swacha & Gracel (P20), it is assumed that automated RAG Triad metrics (Faithfulness, Answer Relevancy, Groundedness) correlate strongly with human expert curriculum evaluations, serving as a reliable proxy for assessing educational hallucination.

### 2.8 Deployment & Infrastructure Assumptions
- **Network Bandwidth Sufficiency**: It is assumed that university campus Wi-Fi or student home broadband maintains a minimum sustained bandwidth of 2.0 Mbps upstream and downstream with latency under 150ms, enabling real-time WebRTC audio streaming [P29].
- **Container Sandbox Security Isolation**: It is assumed that rootless Docker containerization coupled with Linux kernel cgroups and seccomp profiles provides sufficient isolation to prevent malicious candidate code from compromising host server infrastructure [P28].

### 2.9 External Cloud APIs & LLM Behavior Assumptions
- **API Availability & Rate Limits**: It is assumed that commercial foundation model APIs (Google Gemini 1.5 Flash, Claude 3) maintain $\ge 99.5\%$ operational uptime with latency budgets under 1,000ms per turn during active interview sessions [P28, P29].
- **Local Fallback Feasibility**: In accordance with Nisanth et al. (P21), it is assumed that local 4-bit quantized open-weights models (LLaMA-3-8B) deployed on on-premise GPUs provide acceptable functional fallback if cloud API rate limits or network outages occur.
- **Prompt Adherence**: It is assumed that modern instruction-tuned LLMs adhere strictly to system prompt constraints (e.g., *"Generate questions strictly within Bloom's Taxonomy Level 4 and provide explicit distractor rationales"*) without uncontrollable drift [P25, P39].

### 2.10 Recommendation Generation Assumptions
- **Directed Acyclic Graph Topology**: It is assumed that course prerequisite matrices and skill competency graphs can be modeled as formal Directed Acyclic Graphs (DAGs) without containing circular dependency deadlocks [P13, P16].
- **Pareto Optimality Feasibility**: It is assumed that multi-objective optimization algorithms (MACO) can converge to an acceptable Pareto frontier balancing skill acquisition velocity against academic risk within reasonable computational iterations [P16].

### 2.11 Privacy & Legal Governance Assumptions
- **Informed Student Consent**: It is assumed that participating students and faculty mentors provide informed consent for their academic clickstreams, resume text, and interview audio to be analyzed by the PRIE platform for career acceleration purposes [P02].
- **Tokenized Anonymization Protection**: It is assumed that cryptographic tokenization of student identifiers (replacing names, emails, and student ID numbers with secure pseudo-random hashes) satisfies institutional compliance requirements under POPIA, FERPA, and GDPR [P02].

### 2.12 Generalization & Disciplinary Boundary Assumptions
- **Inter-Institutional Transferability**: It is assumed that models pre-trained on standardized technical datasets and calibrated on regional engineering curricula can generalize across similar accredited engineering institutions with minimal domain adaptation [P04, P06, P22].
- **CS/IT Disciplinary Homogeneity**: It is assumed that the core technical competencies evaluated across Computer Science, Information Technology, and Software Engineering degree programs share sufficient curricular overlap to be represented within a common competency graph [P13, P25].

---

## 3. Master Assumptions Summary Matrix

| Assumption Category | Core Operational Premise | Risk if Violated | Literature Foundation |
|:---|:---|:---|:---:|
| **Data Integrity** | LMS & registrar records are authentic and uncorrupted | Garbage-in, garbage-out model degradation | P02, P05, P10 |
| **Student Intent** | Candidates engage sincerely without deliberate adversarial spoofing | Skewed interview prosody & code metrics | P27, P38 |
| **Label Ground Truth** | Official campus placement offers reflect true employability | Inaccurate predictive model supervision | P01, P06, P22 |
| **Ensemble Inductive Bias**| Tree ensembles dominate tabular data; sequence models dominate time-series| Sub-optimal model architecture selection | P01, P08, P22, P34, P44 |
| **Cognitive Feasibility**| Intervenable student effort is realistically bounded ($\le 15$ hrs/week) | Unrealistic, un-actionable counterfactuals | P19 |
| **Network & Latency** | WebRTC connection maintains $<1.5$s turn latency | Broken conversational interview flow | P29 |
| **Code Sandboxing** | Rootless Docker containers contain malicious candidate code | Host server system compromise | P28 |
| **Graph Topology** | Competency prerequisites form formal Directed Acyclic Graphs | Infinite loops in path recommendation | P13, P16 |
| **Privacy Compliance** | Tokenized anonymization satisfies POPIA / GDPR statutes | Legal shutdown of campus deployment | P02 |
