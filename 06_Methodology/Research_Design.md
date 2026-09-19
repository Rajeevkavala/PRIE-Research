# Research Design: Paradigmatic Classification, Variable Topology & Methodological Strategy

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Research_Design.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Research Design Formulation  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Epistemological Foundation & Research Paradigm

The overarching research paradigm governing the ScholarCamp / PRIE investigation is **Design-Science Research (DSR)** augmented with **Empirical Computational Evaluation** and **Psychometric Measurement Theory**.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           RESEARCH PARADIGM TOPOLOGY                            │
├─────────────────────────────────────────────────────────────────────────────────┤
│  1. DESIGN SCIENCE RESEARCH (DSR)                                               │
│     - Construct: Invariant 22-Dimensional Student Profile Vector (SPV)          │
│     - Model: Dual-Track Predictive Framework (Tabular GBDT + Sequence TFT)      │
│     - Method: Two-Tiered XAI (TreeSHAP + DiCE) & Topological A* Graph Search    │
│     - Instantiation: PRIE Subsystems M01–M12                                    │
│                                                                                 │
│  2. EMPIRICAL COMPUTATIONAL EVALUATION                                          │
│     - Supervised Benchmark Classification & Multi-Horizon Forecasting           │
│     - Natural Language Document Intelligence & Semantic Embedding Retrieval     │
│     - Acoustic Speech Recognition & Paralinguistic Latency Budgeting            │
│                                                                                 │
│  3. PSYCHOMETRIC & BEHAVIORAL MEASUREMENT THEORY                                │
│     - Item Response Theory (IRT) & Classical Test Theory for AQG               │
│     - Recruiter Panel Inter-Rater Reliability (Intraclass Correlation ICC)      │
│     - Controlled User Actionability & Milestone Completion Velocity             │
└─────────────────────────────────────────────────────────────────────────────────┘
```

This tripartite design resolves the acute fragmentation identified in `RG1` (where educational research either creates disconnected theoretical surveys or isolated machine learning scripts lacking clinical utility). PRIE treats placement readiness as a dynamic, latent psychological-technical state that must be formally captured, predicted, explained, and remediated in an active educational loop.

---

## 2. Formal Research Strategy

The research strategy combines **controlled comparative experimentation**, **longitudinal observational modeling**, and **counterfactual scenario simulation**:

1. **Comparative In-Silico Benchmarking**: Evaluating candidate models against established literature baselines across standardized corpora (`DS-BENCH-01`, `DS-BENCH-02`, `DS-CORPUS-01`).
2. **Longitudinal Sequential Modeling**: Tracking dynamic temporal velocity and habit persistence across multi-week telemetry windows rather than collapsing student ability into static snapshots (`RG2`).
3. **Interventional Usability Trials**: Assessing the cognitive actionability of prescriptive recourse versus descriptive attribution using structured evaluation instruments (`RG3`).
4. **Psychometric Distractor Calibration**: Measuring the functional discrimination of causal concept-guided multiple choice questions against unconstrained LLM outputs (`RG6`).

---

## 3. Systematic Variable Taxonomy

To ensure scientific rigor and prevent confounding, variables across the PRIE experimental framework are formally categorized:

### 3.1 Independent Variables (IV)
The primary manipulated or experimental conditions:
- **$	ext{IV}_1$ (Document Parsing Representation)**: Vision-Language Spatial 2D Bounding Boxes (`LayoutLMv3`) vs Sequential Flat-Text NER (`BERT-NER` / RegEx). Linked to `EXP-1`.
- **$	ext{IV}_2$ (Conversational Architecture)**: Streaming chunked Whisper ASR + local quantized LLM vs sequential cloud-hosted batch APIs. Linked to `EXP-2`.
- **$	ext{IV}_3$ (Temporal Predictive Horizon)**: Dynamic longitudinal sequence modeling (`Temporal Fusion Transformer` on rolling telemetry) vs static cross-sectional tabular evaluation (`XGBoost` on final semester aggregate). Linked to `EXP-3`.
- **$	ext{IV}_4$ (Explainability Recourse Tier)**: Distance-constrained prescriptive counterfactuals (`DiCE`) with immutable feature locks vs standard descriptive global/local attribution (`TreeSHAP`). Linked to `EXP-4`.
- **$	ext{IV}_5$ (AQG Generation Mechanism)**: Causal Concept DAG-constrained distractor formulation vs unconstrained zero-shot prompt generation. Linked to `EXP-5`.
- **$	ext{IV}_6$ (Intervention Ecology)**: Synchronized triangular digital twin platform (`M12`) vs uncoordinated, disconnected point preparation tools. Linked to `EXP-6`.

### 3.2 Dependent Variables (DV)
The primary outcome measures evaluated:
- **$	ext{DV}_1$ (Parsing Accuracy)**: Entity-level Boundary-F1 Score, Token-level Precision/Recall, and Semantic Cosine Match against Job Descriptions.
- **$	ext{DV}_2$ (Conversational Cadence & Validity)**: End-to-end voice-to-voice turn latency (milliseconds) and Pearson correlation coefficient ($r$) against blinded expert recruiter panel scores.
- **$	ext{DV}_3$ (Predictive & Forecasting Performance)**: Classification Accuracy, Macro-F1, ROC-AUC, Precision-Recall AUC, and Quantile Loss ($q_{0.1}, q_{0.5}, q_{0.9}$) across 6- and 12-month forecasting horizons.
- **$	ext{DV}_4$ (Recourse Actionability & Compliance)**: Likert-scale Actionability Rating (1–5), Feasibility Score, and Empirical 30-Day Milestone Completion Rate (%).
- **$	ext{DV}_5$ (Psychometric Assessment Quality)**: Item Difficulty ($P$-value), Item Discrimination Index ($DI$), and Non-Functional Distractor Proportion ($NFD\%$).
- **$	ext{DV}_6$ (Institutional Placement Yield)**: Campus placement conversion rate (%) and average days-to-placement.

### 3.3 Control Variables (CV)
Variables held constant or mathematically controlled to prevent bias:
- **$	ext{CV}_1$ (Candidate Prior Academic Tier)**: Normalized CGPA category (Tier 1: $\ge 8.5$, Tier 2: $7.0–8.49$, Tier 3: $< 7.0$).
- **$	ext{CV}_2$ (Departmental Specialization)**: Engineering branch fixed effects (Computer Science, Information Technology, Electronics).
- **$	ext{CV}_3$ (Target Role Complexity)**: Standardized corporate profile benchmark (e.g., Software Development Engineer - Backend).
- **$	ext{CV}_4$ (Hardware Inference Environment)**: Fixed GPU/CPU resource constraints (1x NVIDIA RTX 4090 / 24GB VRAM) for all latency benchmarks.
- **$	ext{CV}_5$ (Resume Complexity Baseline)**: Standardized test corpus containing balanced proportions of single-column, two-column, and multi-column document layouts.

---

## 4. Experimental Units & Study Populations

The experimental units differ systematically across the methodological phases:

| Experiment ID | Experimental Unit | Target Population / Corpus | Sample Scope |
| :--- | :--- | :--- | :--- |
| **EXP-1** (ATS Parsing) | Resume Document | Undergraduate technical resumes & verified public tech JDs | $N = 1,200$ Resumes (`DS-CORPUS-01`) |
| **EXP-2** (Interview Coach) | Interview Turn / Session | Simulated technical interview responses & audio streams | $N = 150$ Audio sessions (`DS-INTERVIEW-PILOT`) |
| **EXP-3** (Predictive Modeling) | Student Profile Sequence | Multi-semester longitudinal academic & interaction records | $N = 32,593$ records (`DS-BENCH-02`) / $N=2,500$ (`DS-SYNTH-01`) |
| **EXP-4** (Prescriptive XAI) | Diagnostic Recommendation | Evaluated student profile states requiring skill remediation | $N = 300$ Profile intervention scenarios |
| **EXP-5** (Causal AQG) | Assessment Item (MCQ) | Computer Science concept domain assessment items | $N = 500$ Generated test items |
| **EXP-6** (Digital Twin) | Student Cohort | Multi-semester undergraduate engineering student cohorts | Institutional pilot cohort (`DS-REAL-01`, Planned) |

---

## 5. Methodological Validity & Reliability Strategy

To satisfy IEEE/Springer scientific publication standards, the research design incorporates four layers of methodological verification:

1. **Construct Validity**: Operational definitions for latent constructs (such as "readiness", "consistency", and "behavior") are mathematically grounded in validated educational literature (`Paper01`, `Paper02`, `Paper06`, `Paper14`, `Paper19`).
2. **Internal Validity**: Strict temporal partitioning and cross-fold data isolation eliminate data leakage; holdout test splits remain untouched until final evaluation.
3. **External Validity**: Methodologies are validated across multiple independent datasets (public benchmarks, synthetic populations, and multi-institutional corpora) to identify boundary conditions.
4. **Statistical Conclusion Validity**: Non-parametric tests (Wilcoxon signed-rank) and family-wise error rate corrections (Bonferroni-Holm) are enforced to prevent Type I false-positive discoveries.
