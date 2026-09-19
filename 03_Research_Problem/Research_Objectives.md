# Research Objectives

**Project**: ScholarCamp — AI-Powered Placement Preparation and Career Acceleration Platform  
**Core System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `03_Research_Problem/Research_Objectives.md`  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers, 71 Processed Documents)  
**Cross-Analysis Foundation**: `02_Cross_Analysis/` (20 Authoritative Synthesis Documents)  
**Master Evidence Ledger**: `03_Research_Problem/PHASE_03_EVIDENCE_LEDGER.md`  
**Parent Problem Statement**: `03_Research_Problem/Problem_Statement.md`  
**Date**: September 2026  
**Status**: Authoritative Research Objectives Formulation  

---

## 1. Formulation Principles & Methodological Discipline

In strict accordance with Phase 03 academic standards, the research objectives for ScholarCamp / PRIE are derived directly from the validated literature gaps (`CG1`–`CG8`) and the core problem statement. Each objective adheres to four scientific criteria:
1. **Directly Relates to the Research Problem**: Directly targets the multi-dimensional fragmentation, static modeling bias, or descriptive-to-prescriptive divide documented in the literature.
2. **Research-Oriented Phrasing**: Formulated as a formal scientific investigation rather than a software engineering task (avoiding operational phrases like *"Build a dashboard"* or *"Code an API"* in favor of *"Investigate whether..."*, *"Mathematically formalize..."*, and *"Quantitatively evaluate..."*).
3. **Measurable & Benchmarkable**: Specifies explicit quantitative target metrics derived from the verified empirical corpus.
4. **Experimentally Testable**: Structured to enable rigorous statistical testing, ablation studies, and comparative benchmarking in subsequent research phases.

---

## 2. Primary Research Objective (PRO)

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           PRIMARY RESEARCH OBJECTIVE (PRO)                       │
├──────────────────────────────────────────────────────────────────────────────────┤
│ To formulate, engineer, and empirically validate an integrated, closed-loop      │
│ Placement Readiness Intelligence Engine (PRIE) that synchronizes heterogeneous,  │
│ multimodal candidate telemetry—spanning spatial resume document representations, │
│ real-time conversational speech prosody, containerized coding verification, and   │
│ dynamic longitudinal learning analytics—into a continuous latent readiness state  │
│ capable of generating distance-constrained, prescriptive counterfactual          │
│ remediation pathways that significantly outperform siloed preparation systems.   │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Logically Derived Secondary Research Objectives (RO1–RO6)

---

### Research Objective 1 (RO1): Multimodal Document Intelligence & Spatial Skill Extraction
- **Formal Objective**: **Investigate whether integrating spatial 2D visual-language document representations with dense-sparse hybrid retrieval eliminates multi-column text interleaving and improves candidate skill extraction accuracy compared to traditional linear ATS parsing pipelines.**
- **Target Gap & Evidence**: Addresses `CG4` (Spatial Layout Destruction in ATS); supported by P04, P11, P12, P17, P35, P36, P37, P42 [`EVID-P03-011`, `EVID-P03-012`, `EVID-P03-017`, `EVID-P03-042`].
- **Researchable Scope**: Evaluate LayoutLMv3 spatial coordinate bounding boxes against linear extraction libraries (PyPDF2, pdfminer) across standard and multi-column technical resumes; combine dense SBERT embeddings with sparse BM25 indices via Reciprocal Rank Fusion (RRF); assess implicit technical competency mining using Doc2Vec paragraph representations.
- **Measurable Benchmark**:
  - Entity Extraction F1-Score $\ge 0.92$ (matching Kapula P42's 0.948 benchmark).
  - Multi-column layout boundary tolerance $\ge 95\%$.
  - Mean Reciprocal Rank (MRR@10) $\ge 0.90$ on job description candidate ranking (matching Solanki P17's 0.92 benchmark).
- **Experimental Testability**: Direct comparative extraction on the 2,500 enterprise resume corpus; statistical significance testing (paired t-test on entity extraction F1 across 1-column vs 2-column formats).

---

### Research Objective 2 (RO2): Low-Latency Multimodal Conversational Coaching & Secure Code Sandboxing
- **Formal Objective**: **Investigate whether an asynchronous edge-streaming architecture unifying bidirectional WebRTC audio, client-side visual landmark tracking, and rootless containerized code sandboxes can achieve sub-1.5s conversational turn latency while maintaining high correlation with human expert technical and behavioral evaluation.**
- **Target Gap & Evidence**: Addresses `CG5` (Mock Interview Latency & Modality Disconnect); supported by P03, P14, P15, P27, P28, P29, P30, P38 [`EVID-P03-003`, `EVID-P03-014`, `EVID-P03-015`, `EVID-P03-028`, `EVID-P03-029`].
- **Researchable Scope**: Measure end-to-end turnaround latency from candidate audio chunking to Gemini 1.5 Flash speech synthesis; stream openSMILE acoustic prosody (pitch F0, jitter, shimmer) concurrently with WebAssembly MediaPipe 3D FaceMesh gaze tracking; execute candidate Python/Java source code inside ephemeral, network-isolated Docker containers; correlate automated paralinguistic and coding scores against independent corporate recruiter panels.
- **Measurable Benchmark**:
  - Conversational turn latency $\le 1.5\text{ seconds}$ (sub-second target: $<1.2\text{s}$, matching Wahid P29).
  - Human expert rubric correlation: Pearson $r \ge 0.82$ for behavioral composure (matching Inamdar P15) and $r \ge 0.84$ for technical code evaluation (matching Vachkal P28).
  - Security isolation: Zero container breakout or file system tampering across malicious test scripts.
- **Experimental Testability**: Controlled latency benchmarking under variable network conditions; Pearson and Spearman correlation analysis against a panel of 5 corporate technical recruiters on 100 recorded interview sessions.

---

### Research Objective 3 (RO3): Dynamic Longitudinal Sequence Modeling & Multi-Horizon Placement Forecasting
- **Formal Objective**: **Investigate whether formulating placement readiness as a dynamic, continuous temporal sequence tracked via Temporal Fusion Transformers (TFT) achieves statistically superior early risk detection and predictive accuracy compared to static cross-sectional classifiers.**
- **Target Gap & Evidence**: Addresses `CG3` (Static Point-in-Time Retrospective Bias); supported by P01, P06, P07, P08, P09, P10, P22, P24, P31, P33, P44 [`EVID-P03-001`, `EVID-P03-008`, `EVID-P03-010`, `EVID-P03-022`, `EVID-P03-044`, `EVID-P03-047`].
- **Researchable Scope**: Ingest weekly multi-variate time-series telemetry (LMS clickstream frequency, weekly LeetCode problems solved, Git commit velocity, and mock interview scores); train a multi-horizon Temporal Fusion Transformer to forecast placement readiness probability at Week 3, Week 6, and Week 12 of a pre-placement preparation cycle; compare against static Random Forest, XGBoost, and CatBoost baselines trained on cumulative CGPA.
- **Measurable Benchmark**:
  - Classification Accuracy $\ge 93\%$ and PR-AUC $\ge 0.92$ (matching Azeez P44's 94.6% TFT benchmark).
  - Statistically significant early divergence detection by **Week 4** ($p < 0.001$, replicating Al-Shabandar P33 and Anoop P08).
  - Macro F1-score uplift $\ge +8\%$ over static cumulative GPA classifiers.
- **Experimental Testability**: Longitudinal multi-cohort validation across 4 academic terms; McNemar's test and DeLong's test comparing ROC curves between temporal TFT and static CatBoost.

---

### Research Objective 4 (RO4): Distance-Constrained Prescriptive Counterfactual Career Remediation
- **Formal Objective**: **Investigate whether distance-constrained counterfactual optimization (DiCE) over intervenable student variables generates actionable, pedagogically feasible remediation roadmaps that yield significantly higher user comprehension and willingness-to-act than traditional descriptive feature attributions (TreeSHAP).**
- **Target Gap & Evidence**: Addresses `CG2` (Descriptive-to-Prescriptive Chasm); supported by P02, P05, P07, P18, P19, P22, P32, P34, P44 [`EVID-P03-002`, `EVID-P03-005`, `EVID-P03-018`, `EVID-P03-019`, `EVID-P03-032`, `EVID-P03-048`].
- **Researchable Scope**: Formulate a multi-objective loss function minimizing $L_1$ intervention distance while strictly bounding mutable variables (e.g., weekly study hours $\le 15$, LeetCode practice $\le 5$ problems/week) and locking immutable features (10th%, 12th%, past semester SGPA); evaluate counterfactual validity, sparsity, and feasibility; conduct randomized user trials contrasting counterfactual cards against TreeSHAP waterfall plots.
- **Measurable Benchmark**:
  - Counterfactual validity $\ge 92\%$ (matching Kumar P19's 94.2% validity).
  - Sparsity $\le 3$ intervenable features modified per generated recourse.
  - Student and faculty advisor usability comprehension rating $\ge 85\%$ in human-in-the-loop trials (addressing Talmoudi P32).
- **Experimental Testability**: Algorithmic benchmark of counterfactual generation latency and proximity loss; randomized controlled user trial with 150 engineering students measuring actionable task completion rates post-explanation.

---

### Research Objective 5 (RO5): Causal Graph-Guided Cognitive Question Generation & Assessment Calibrations
- **Formal Objective**: **Investigate whether grounding automated technical question generation in Causal Concept Directed Acyclic Graphs (DAGs) and Bloom's cognitive taxonomy prompting elevates assessment item discrimination and eliminates distractor ambiguity compared to unconstrained LLM generation.**
- **Target Gap & Evidence**: Addresses `CG7` (Cognitive Depth in AQG); supported by P25, P26, P39 [`EVID-P03-025`, `EVID-P03-026`, `EVID-P03-039`].
- **Researchable Scope**: Construct a Neo4j knowledge graph of technical CS competencies and causal prerequisite edges; deploy fine-tuned open-weights models (LLaMA-3) conditioned on identified candidate resume skill gaps; prompt specifically for Bloom's Levels 3–5 (Apply, Analyze, Evaluate: code debugging and complexity trade-offs); generate dual explanatory feedback rationales for the correct key and every incorrect distractor; calibrate psychometric Item Difficulty ($p$) and Item Discrimination ($D$).
- **Measurable Benchmark**:
  - Pedagogical Validity $\ge 90\%$ verified by Subject Matter Experts (matching Wang P25's 91.5%).
  - Item Discrimination Index $D \ge 0.80$ across student assessment cohorts.
  - Distractor ambiguity rate $\le 4\%$ under expert peer audit.
- **Experimental Testability**: Classical Test Theory (CTT) psychometric evaluation on 1,000 generated assessment items administered across 200 undergraduate computer science students.

---

### Research Objective 6 (RO6): Closed-Loop Multi-Stakeholder Digital Twin Integration & Privacy Compliance
- **Formal Objective**: **Investigate whether integrating student diagnostic telemetry, faculty mentoring logs, and corporate recruiter demand signals into a privacy-preserving Triangular Placement Digital Twin achieves statistically higher placement offer fidelity and preparation efficiency than isolated point interventions.**
- **Target Gap & Evidence**: Addresses `CG1` (Subsystem Fragmentation), `CG6` (Prerequisite Blindness), and `CG8` (Privacy & Validation Deficit); supported by P02, P13, P16, P21, P27, P41, P44 [`EVID-P03-002`, `EVID-P03-013`, `EVID-P03-016`, `EVID-P03-041`, `EVID-P03-044`, `EVID-P03-045`].
- **Researchable Scope**: Model students, faculty mentors, and corporate recruiters as interacting agents over a Neo4j graph database; synchronize real-time updates from ATS parsers, mock interviews, and coding sandboxes into an evolving 22-dimensional student profile vector; enforce topological prerequisite constraints via Multi-Objective Ant Colony Optimization (MACO); enforce role-based access control and tokenized anonymization adhering to POPIA/GDPR data protection standards.
- **Measurable Benchmark**:
  - Placement simulation fidelity $\ge 90\%$ (matching Babureddy P41's 91.4%).
  - Preparation efficiency uplift $\ge +20\%$ in student competency acquisition speed over unassisted preparation.
  - Zero FERPA/POPIA privacy violations under automated vulnerability and compliance audit.
- **Experimental Testability**: Prospective multi-cohort trial comparing placement conversion rates between students prepared via the closed-loop PRIE digital twin versus students utilizing disconnected point tools.

---

## 4. Objective-to-Gap Traceability Matrix

The matrix below certifies that every research objective maps directly to validated literature gaps, primary empirical papers, and target benchmark metrics:

| Research Objective | Core Research Target | Validated Gaps Addressed | Primary Literature Foundations | Target Empirical Benchmark |
|:---|:---|:---:|:---|:---|
| **RO1** | Multimodal Spatial ATS Parsing & Semantic Retrieval | `CG4` | P04, P11, P12, P17, P35, P42 | Entity F1 $\ge 0.92$; MRR@10 $\ge 0.90$; Layout Acc $\ge 95\%$ |
| **RO2** | Low-Latency WebRTC Interview & Docker Sandbox | `CG5`, `CG1` | P03, P14, P15, P28, P29 | Turn Latency $\le 1.5$s; Recruiter Corr $r \ge 0.82$ |
| **RO3** | Dynamic Multi-Horizon Temporal Placement Forecasting | `CG3` | P08, P10, P31, P33, P44 | PR-AUC $\ge 0.92$; Week 4 Divergence ($p<0.001$) |
| **RO4** | Distance-Constrained DiCE Counterfactual Remediation | `CG2` | P02, P07, P18, P19, P22, P44 | Counterfactual Validity $\ge 92\%$; Sparsity $\le 3$ vars |
| **RO5** | Causal Concept DAG AQG & Psychometric Assessment | `CG7` | P25, P26, P39 | Item Discrimination $D \ge 0.80$; Validity $\ge 90\%$ |
| **RO6** | Closed-Loop Triangular Digital Twin & Privacy Shield | `CG1`, `CG6`, `CG8`| P02, P13, P16, P21, P41, P44 | Simulation Fidelity $\ge 90\%$; Prep Uplift $\ge +20\%$ |
