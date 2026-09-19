# Research Questions

**Project**: ScholarCamp — AI-Powered Placement Preparation and Career Acceleration Platform  
**Core System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `03_Research_Problem/Research_Questions.md`  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers, 71 Processed Documents)  
**Cross-Analysis Foundation**: `02_Cross_Analysis/` (20 Authoritative Synthesis Documents)  
**Master Evidence Ledger**: `03_Research_Problem/PHASE_03_EVIDENCE_LEDGER.md`  
**Parent Objectives**: `03_Research_Problem/Research_Objectives.md`  
**Date**: September 2026  
**Status**: Authoritative Research Questions Formulation  

---

## 1. Formulation Principles & Research Rigor

The research questions (RQs) governing ScholarCamp / PRIE are formulated to interrogate the fundamental theoretical, algorithmic, and empirical uncertainties identified in the literature. In strict compliance with academic standards:
1. **Scientific Interrogation vs Software Tasks**: Every RQ poses an empirical or theoretical hypothesis regarding AI behavior, multimodal integration, or pedagogical effectiveness (avoiding engineering questions like *"How do we code an API endpoint?"*).
2. **End-to-End Traceability**: Every RQ maps strictly to a validated literature gap (`CG1`–`CG8`), a formal research objective (`RO1`–`RO6`), an explicit algorithmic method, and a concrete evaluation benchmark.
3. **Falsifiability & Experimental Testability**: Each question is structured to yield measurable, statistically verifiable answers during subsequent experimental phases.

---

## 2. Master Research Questions & Traceability Matrix

The table below establishes the comprehensive end-to-end mapping from literature gaps to empirical evaluation:

| Research Question (RQ) | Addressed Literature Gap | Mapped Research Objective | Primary Investigated Method | Quantitative Evaluation Protocol | Expected Primary Evidence |
|:---|:---:|:---:|:---|:---|:---|
| **RQ1**: Multimodal ATS Spatial Parsing & Retrieval | `CG4` | `RO1` | LayoutLMv3 2D spatial coordinate parsing + SBERT-BM25 hybrid Reciprocal Rank Fusion (RRF) | Entity Extraction F1, Layout boundary tolerance %, MRR@10, Top-5 Match Accuracy | LayoutLMv3 eliminates column interleaving; Entity F1 $\ge 0.92$; MRR@10 $\ge 0.90$ (P17, P42) |
| **RQ2**: Low-Latency Multimodal Interview & Coding | `CG5`, `CG1` | `RO2` | WebRTC bidirectional audio streaming + Gemini 1.5 Flash + openSMILE + Docker code sandbox | End-to-end turn latency (ms), Pearson $r$ and Spearman $\rho$ with human recruiter panels | Sub-1.5s turn latency; Recruiter correlation $r \ge 0.82$; Zero security sandbox breaches (P15, P28, P29) |
| **RQ3**: Dynamic Longitudinal Placement Modeling | `CG3` | `RO3` | Temporal Fusion Transformer (TFT) on weekly multi-variate activity vs static CatBoost/RF | Multi-Horizon PR-AUC, Macro-F1, ROC curves, statistical divergence week test ($p<0.001$) | Temporal sequence modeling yields $+8\%$ F1 uplift over static CGPA; Week 4 risk divergence (P08, P33, P44) |
| **RQ4**: Prescriptive Counterfactual Remediation | `CG2` | `RO4` | Distance-constrained DiCE counterfactual optimization bounded by weekly student cognitive load | Counterfactual validity %, feature sparsity ($L_0$), advisor & student usability ratings | Validity $\ge 92\%$; $\le 3$ intervenable features modified; $\ge 85\%$ student comprehension (P19, P32) |
| **RQ5**: Causal Concept AQG & Psychometrics | `CG7` | `RO5` | Causal Concept DAGs in Neo4j + Bloom's Level 3–5 prompting + dual distractor feedback | Item Difficulty ($p$), Item Discrimination ($D$), SME pedagogical validity audit %, distractor ambiguity | Discrimination $D \ge 0.80$; Validity $\ge 90\%$; Distractor ambiguity $\le 4\%$ (P25, P26, P39) |
| **RQ6**: Closed-Loop Placement Digital Twin | `CG1`, `CG6`, `CG8`| `RO6` | Multi-agent Triangular Digital Twin (Neo4j) + MACO prerequisite optimization + POPIA privacy | Simulation offer fidelity %, graduation delay reduction %, candidate placement conversion uplift | Twin fidelity $\ge 90\%$; Prep efficiency $+20\%$; Zero privacy/FERPA leakage (P02, P16, P41) |

---

## 3. In-Depth Elaboration of Research Questions

---

### Research Question 1 (RQ1)
> **To what extent does integrating spatial 2D vision-language document representations (LayoutLMv3) with hybrid dense-sparse retrieval (SBERT + BM25) improve Named Entity Recognition F1-scores and candidate-job matching accuracy on complex multi-column technical resumes compared to standard linear text-scraping ATS baselines?**

- **Theoretical Foundation**: A multi-column resume is inherently a two-dimensional spatial document. Linear 1D text extraction libraries (PyPDF2, pdfminer) read across the physical page width, concatenating left-column technical skills into right-column project narrative streams [P11, P12, P37]. This syntax destruction severely penalizes dense bi-encoders and degrades entity extraction F1 [P42].
- **Methodological Investigation**:
  - Compare LayoutLMv3 (which jointly embeds visual bounding boxes, font typography, and text tokens) against baseline linear parsers across standard single-column and complex two-column resumes.
  - Implement a hybrid retrieval engine combining dense Sentence-BERT vectors (`all-MiniLM-L6-v2`) and sparse BM25 term matrices via Reciprocal Rank Fusion (RRF), testing whether RRF balances conceptual synonym matching with exact requirement verification [P17].
  - Mine unstated implicit competencies using Distributed Memory Doc2Vec (PV-DM) trained on software engineering project corpora [P35].
- **Evaluation & Target Metrics**:
  - Entity Extraction Macro-F1 across `Education`, `Experience`, `Skills`, and `Certifications` ($\ge 0.92$).
  - Multi-column layout boundary preservation rate ($\ge 95\%$).
  - Mean Reciprocal Rank (MRR@10) on 2,500 candidate resumes evaluated against 800 IT job descriptions ($\ge 0.90$).

---

### Research Question 2 (RQ2)
> **Can an asynchronous streaming architecture uniting bidirectional WebRTC audio, client-side WebAssembly video tracking, and isolated containerized code execution maintain conversational turn latency under 1.5 seconds while demonstrating high psychometric and technical evaluation correlation ($r \ge 0.82$) with independent human corporate recruitment panels?**

- **Theoretical Foundation**: Natural human conversational flow requires turn latencies under 1.2 to 1.5 seconds. Delays exceeding 2.5 seconds disrupt cognitive speech pacing and elevate candidate anxiety [P03, P27]. Furthermore, technical software interviews require simultaneous evaluation of behavioral composure, oral explanation fluency, and algorithmic code execution, which existing single-modality systems evaluate in disconnected silos [P14, P15, P28].
- **Methodological Investigation**:
  - Establish a bidirectional WebRTC streaming gateway streaming raw audio frames to a local C++ openSMILE acoustic prosody engine and Google Gemini 1.5 Flash [P29].
  - Execute client-side MediaPipe 3D FaceMesh via WebAssembly to extract eye-contact ratio, blink rate, and Action Unit smile frequency (AU12) at 60 FPS without server GPU video transfer overhead [P03, P14].
  - Provision ephemeral, rootless Docker container sandboxes with strict CPU, memory, and network isolation to compile candidate code, parse Abstract Syntax Trees (ASTs), and execute unit tests within 3.5 seconds [P28].
- **Evaluation & Target Metrics**:
  - End-to-end turnaround latency from candidate voice pause to AI audio response ($\le 1.5$s; target $<1.2$s).
  - Pearson ($r$) and Spearman ($\rho$) correlation coefficients against a panel of 5 corporate technical recruiters evaluating 100 mock interview sessions ($r \ge 0.82$ on communication, $r \ge 0.84$ on coding correctness).
  - Security audit: 100% containment of sandbox escape, fork-bomb, and malicious file exfiltration attempts.

---

### Research Question 3 (RQ3)
> **How significantly does formulating graduate placement readiness as a dynamic, continuous temporal state vector tracked via Temporal Fusion Transformers (TFT) improve early at-risk detection and placement outcome prediction compared to static cross-sectional classifiers trained on cumulative academic records?**

- **Theoretical Foundation**: Static academic metrics (final CGPA) provide post-hoc descriptive classifications that cannot capture mid-semester disengagement or preparation acceleration [P01, P06, P07]. Educational data mining proves that engagement velocity over time contains predictive signals that statistically diverge as early as Week 3 of a learning cycle [P08, P33, P44].
- **Methodological Investigation**:
  - Construct a longitudinal feature vector combining weekly LMS interactions, weekly LeetCode challenge velocity, GitHub commit frequency, and periodic mock interview performance over multi-semester horizons [P09, P44].
  - Train a Temporal Fusion Transformer (TFT) utilizing self-attention layers to forecast multi-horizon placement probabilities at Week 3, Week 6, and Week 12 of a pre-placement preparation window.
  - Benchmark TFT performance against classical static classifiers (Random Forest, XGBoost, CatBoost) trained exclusively on cumulative GPA and static demographic records.
- **Evaluation & Target Metrics**:
  - Area Under the Precision-Recall Curve (PR-AUC) $\ge 0.92$ and Classification Accuracy $\ge 93\%$.
  - Detection of statistically significant risk divergence trajectories by **Week 4** ($p < 0.001$ via two-sample Kolmogorov-Smirnov test).
  - Statistically significant performance uplift over static classifiers verified via DeLong's test on ROC curves ($p < 0.01$).

---

### Research Question 4 (RQ4)
> **Does distance-constrained counterfactual optimization (DiCE) over intervenable student variables produce remediation roadmaps with higher validity ($\ge 92\%$), sparsity ($\le 3$ features), and human stakeholder comprehension than traditional game-theoretic feature attributions (TreeSHAP)?**

- **Theoretical Foundation**: Cooperative game-theoretic feature attribution (TreeSHAP) is fundamentally descriptive; it explains *why* a model classified a student as at-risk (e.g., *“High school marks were 54%”*), but provides no recourse because historical records are immutable [P02, P18, P22]. Prescriptive intervention requires solving a constrained optimization problem over mutable features only [P19].
- **Methodological Investigation**:
  - Formulate a loss function balancing prediction loss, $L_1$ proximity to the student's current state, and diversity across counterfactual candidates, while enforcing hard bounds on intervenable variables (weekly study hours $\le 15$, LeetCode practice $\le 5$ problems/week) and freezing immutable features [P19].
  - Generate actionable "what-if" counterfactual cards for students (e.g., *“Increasing weekly coding practice from 2 to 5 problems and raising mock interview fluency score from 6.0 to 7.5 flips placement status from Unlikely to Likely with 94% confidence”*).
  - Conduct randomized user comprehension trials comparing counterfactual cards against TreeSHAP waterfall plots across 150 engineering students and 25 faculty advisors [P32].
- **Evaluation & Target Metrics**:
  - Counterfactual validity ($\ge 92\%$) and sparsity ($\le 3$ actionable features altered).
  - Counterfactual generation latency ($\le 2.0$ seconds).
  - Usability and actionable comprehension rating $\ge 85\%$ on the System Usability Scale (SUS) in human-in-the-loop trials.

---

### Research Question 5 (RQ5)
> **How effectively does conditioning Automated Question Generation on Causal Concept Directed Acyclic Graphs (DAGs) and Bloom's cognitive taxonomy prompting improve assessment item discrimination ($D \ge 0.80$) and eliminate distractor ambiguity compared to unconstrained zero-shot LLM generation?**

- **Theoretical Foundation**: Over 70% of automated question generators produce lower-order Bloom's Recall questions (Level 1–2) that fail to test technical problem-solving [P26, P39]. Furthermore, unconstrained LLMs frequently produce ambiguous or factually flawed distractors, destroying psychometric test validity [P25].
- **Methodological Investigation**:
  - Construct a Neo4j knowledge graph representing computer science competencies, topic prerequisite dependencies, and common conceptual misconceptions [P13, P25].
  - Prompt a fine-tuned open-weights language model (LLaMA-3) to generate scenario-based questions targeting Bloom's Levels 3–5 (Apply, Analyze, Evaluate: code debugging, runtime complexity trade-offs, system architecture choices) [P39].
  - Condition question generation directly on specific skill deficits identified during the candidate's ATS resume screening and mock interview assessments.
  - Implement a dual-agent verification loop: an adversarial validator LLM checks that the correct option is uniquely true and that all distractors are unambiguously false, generating explicit rationales for both [P25].
- **Evaluation & Target Metrics**:
  - Psychometric Item Discrimination Index $D \ge 0.80$ and Item Difficulty $0.40 \le p \le 0.70$ evaluated via Classical Test Theory (CTT).
  - Subject Matter Expert (SME) pedagogical validity rating $\ge 90\%$.
  - Distractor ambiguity error rate $\le 4\%$ under blind peer review.

---

### Research Question 6 (RQ6)
> **To what extent does a closed-loop Triangular Placement Digital Twin synchronizing student telemetry, faculty mentor logs, and corporate recruiter demand over a prerequisite-constrained graph yield higher placement simulation fidelity ($\ge 90\%$) and preparation efficiency than fragmented single-stakeholder interventions?**

- **Theoretical Foundation**: Employability is not an isolated student attribute; it is an equilibrium emerging from the interaction between student capability, faculty pedagogical intervention, and live corporate recruiter hiring standards [P41]. Systemic isolation among these three stakeholders results in misaligned curricula, delayed advisor interventions, and mismatched recruitment drives [P02, P06, P41].
- **Methodological Investigation**:
  - Architect a multi-agent digital twin environment over Neo4j modeling 1,500+ skills, course prerequisite DAGs, student latent states, faculty intervention tickets, and live corporate job role demand matrices [P13, P41].
  - Deploy Multi-Objective Ant Colony Optimization (MACO) to optimize personalized remedial learning paths balancing skill acquisition velocity against GPA risk [P16].
  - Deploy a Proximal Policy Optimization (PPO) reinforcement learning agent to simulate and dispatch calibrated micro-nudges to students and alert tickets to faculty advisors [P44].
  - Implement cryptographic tokenized data anonymization and role-based access control complying with POPIA and GDPR privacy statutes [P02].
- **Evaluation & Target Metrics**:
  - Real-world placement offer simulation fidelity $\ge 90\%$ (matching Babureddy P41's 91.4%).
  - Preparation efficiency uplift: $\ge +20\%$ faster mastery of target technical competencies compared to unguided student cohorts.
  - Graduation and placement readiness delay reduction $\ge 15\%$ (matching Senthil P16's 18% delay reduction).
  - Privacy compliance: Zero plaintext transmission of student biometric or academic records under audited vulnerability testing.
