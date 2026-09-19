# Phase 10: Master Publication Plan & Dissemination Strategy

**Project**: ScholarCamp  
**Core System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  
**Document**: `10_Publication/PHASE_10_PUBLICATION_PLAN.md`  
**Date**: September 19, 2026  
**Status**: COMPLETE & AUTHORITATIVE  

---

## 1. Executive Summary & Publication Objective

The primary objective of Phase 10 is to engineer a publication-ready scientific conference paper and complete dissemination package for ScholarCamp / PRIE. The research directly addresses the severe fragmentation of contemporary higher-education placement preparation systems by demonstrating a continuous, explainable, and multi-modal intelligence engine.

---

## 2. Target Academic Venues & Conference Ranking

The manuscript is structured according to the double-column format of premier academic publishing bodies:

| Target Venue | Organizing Body | Focus Area | Acceptance Rate / H5-Index | Fit Rationale |
|:---|:---|:---|:---:|:---|
| **IEEE Transactions on Learning Technologies (TLT)** | IEEE Computer Society | AI in Higher Education, Adaptive Learning, Educational Data Mining | H5: 48 (Q1 Journal/Conference Track) | Perfect alignment with PRIE's continuous student state modeling, learning analytics, and adaptive roadmaps. |
| **IEEE Frontiers in Education (FIE)** | IEEE Education Society | Engineering Education, Curricular Analytics, Career Readiness | Tier-1 Engineering Education | Direct relevance to engineering student cohort placement preparation and diagnostic assessment. |
| **ACM Conference on Learning @ Scale (L@S)** | ACM SIGCHI | Scalable Learning Systems, Adaptive Feedback, Automated Assessment | ~25% Acceptance Rate | High alignment with automated question generation, RAG, and scalable ATS parsing. |
| **International Conference on Educational Data Mining (EDM)** | IEDMS | Predictive Student Modeling, Explainability, Fairness in Education | Leading Specialist Venue | Core fit for Platt calibration, TreeSHAP feature attributions, and DiCE counterfactual recourse. |

---

## 3. Paper Master Title & Scientific Nomenclature

* **Primary Title**:  
  **PRIE: An Explainable Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse**
* **Short Running Title**:  
  **PRIE: Explainable Placement Readiness Intelligence**
* **Prohibited Phrasing**:  
  Terms such as *"Revolutionary"*, *"World's First"*, *"Unprecedented"*, *"Flawless"*, or *"Ultimate"* are strictly prohibited. The system is rigorously characterized as an *explainable, calibrated intelligence architecture with constrained prescriptive recourse*.

---

## 4. Manuscript Architectural Outline

The conference paper is engineered to adhere to the standard 11-section IEEE double-column format:

1. **Title, Blinded Author Block, Abstract & Keywords**:
   - Comprehensive abstract summarizing the higher-education placement gap, PRIE architecture, 22D Student Profile Vector, Platt-calibrated XGBoost ($ECE = 0.0350$, $AUC = 0.9922$), DiCE recourse ($k = 2.47 \le 3.0$), late multimodal fusion ($77.98\%$ variance damping), and topological roadmap scheduling ($0$ violations).
2. **Section I: Introduction**:
   - Contextualization of the engineering graduate employability crisis.
   - Critique of fragmented, point-in-time point solutions (isolated ATS scanners, uncalibrated interview tools).
   - Introduction of PRIE's closed-loop paradigm: Diagnosis $\rightarrow$ Prediction $\rightarrow$ Explanation $\rightarrow$ Remediation.
   - Core research questions (`RQ1`–`RQ6`) and five explicit research contributions.
3. **Section II: Related Work / Literature Positioning**:
   - Thematic synthesis across the 44-paper verified corpus:
     - *Educational Data Mining & Tabular Employability Prediction* (Olipas 2024, 2025; Patel & Nair 2024; Casuat 2021).
     - *Explainable AI & Algorithmic Recourse in Education* (Hidayatulloh 2026; Joshi 2025; Talmoudi 2026).
     - *Multimodal Interview & Behavioral Assessment* (Srinivasan 2025; Deshmukh 2025; Kulkarni 2024).
     - *Automated Resume Screening & Spatial Document Parsing* (Verma 2026; Roy 2024; Kapula 2025).
     - *Curriculum Sequencing, Knowledge Graphs & Retrieval-Augmented Generation* (Fernandez 2025; Tan 2024; Sutherland 2025).
4. **Section III: Research Problem & Research Gaps**:
   - Formal mathematical formulation of placement readiness.
   - The 5 core literature gaps (`CG1` to `CG5`): Integration, Calibration, Actionability, Spatial Layout Integrity, and Prerequisite Precedence.
5. **Section IV: PRIE System Architecture**:
   - 4-tier microservice architecture: Data Acquisition, Latent State Engine, Analytics & XAI, Adaptive Remediation.
   - Rigorous mathematical definition of the 22-dimensional Student Profile Vector ($\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$) and observation mask $\mathbf{m}$.
6. **Section V: Methodology**:
   - *Diagnostic Calibration*: Cost-sensitive XGBoost with Platt sigmoid probability calibration.
   - *Prescriptive Recourse*: Constrained DiCE optimization with $L_1$ sparsity and immutable feature preservation.
   - *Multimodal Late Fusion*: Tri-modal linear late fusion over acoustic prosody, video composure, and speech clarity.
   - *Spatial ATS Parsing*: PyMuPDF 2D coordinate-based geometric extraction and reading order recovery.
   - *Pedagogical Scheduling*: Kahn's topological sort over directed acyclic curriculum graphs.
   - *Guardrailed Curriculum RAG*: Cosine similarity threshold gating ($\tau = 0.70$) over curriculum vector embeddings.
7. **Section VI: Experimental Design**:
   - Benchmarking suites `EXP-1` through `EXP-6`.
   - Datasets: `DS-SYNTH-01` ($N=2,500$), `DS-INTERVIEW-SIM` ($N=50$), `cs_concept_dag.json` (38 concepts).
   - Cross-validation protocol: 5-seed stratified 80/10/10 split ($\{42, 123, 456, 789, 2026\}$).
   - Baselines: Logistic Regression, Random Forest, Uncalibrated XGBoost, 1D Regex, Unconstrained Schedulers.
8. **Section VII: Results & Empirical Analysis**:
   - Table 1: Predictive calibration and discrimination benchmark.
   - Table 2: Multimodal interview modality ablation.
   - Table 3: Prescriptive counterfactual recourse feasibility.
   - Table 4: Experimental validation suite summary.
   - Figures 1–6: Calibration reliability curves, ROC/PR trajectories, TreeSHAP importance, multimodal ablation, concept DAG, persona radars.
9. **Section VIII: Research Discussion**:
   - Pedagogical actionability of SHAP waterfall plots and sparse counterfactual cards.
   - Socio-technical positioning: moving beyond punitive student ranking to supportive guidance.
   - Addressing synthetic linearity: why tree ensembles are maintained despite logistic regression synthetic scores.
10. **Section IX: Threats to Validity & Limitations**:
    - Construct, internal, external, and statistical validity analysis.
    - Explicit disclosure of synthetic simulation boundaries (`DS-SYNTH-01`).
    - Delineation of prospective human cohort trials (`DATA COLLECTION REQUIRED` for $H_{\text{uplift}}$ and $H_{\text{recruiter}}$).
    - Resource boundary: LayoutLMv3 categorized as `MODEL NOT TRAINED`.
11. **Section X: Conclusion & Future Work**:
    - Summary of verified algorithmic and system contributions.
    - Future roadmap: Federated cross-institutional learning, full vision-language resume transformers, live pilot deployments.
12. **References**:
    - 44 primary corpus literature citations formatted according to IEEEtran specifications.

---

## 5. Secondary Academic Artifacts Plan

Alongside the primary conference paper, Phase 10 produces:
1. **Interactive Demo Package (`06_Demo/`)**:
   - 5-stage live demonstration walkthrough illustrating student onboarding, 22D vector assembly, TreeSHAP waterfall diagnosis, 4-week prerequisite-valid roadmap generation, and multimodal mock interview evaluation.
2. **Academic Conference Poster Package (`07_Poster/`)**:
   - High-impact 3-column academic poster specification designed for standard A0 portrait/landscape presentation.
3. **Conference Presentation Deck (`08_Presentation/`)**:
   - 16-slide structured slide deck with verbatim presenter speaker notes and visual aids.
4. **Conference Submission Package (`05_Conference_Submission/`)**:
   - Comprehensive pre-submission checklist, page limit audit, and author metadata.
5. **Research Integrity & Auditing Suite (`09_Final_Audit/`)**:
   - Four rigorous audits covering research integrity, numerical consistency, claim evidence, and reproducibility.

---

## 6. Execution Timeline & Verification Milestones

* **Milestone 1**: Complete research-context ingestion and reading audit. *(Completed)*
* **Milestone 2**: Final publication directory creation and asset synchronization. *(Completed)*
* **Milestone 3**: Authoring foundational publication ledgers and claim/citation matrices.
* **Milestone 4**: Complete drafting of `paper.tex` and compilation of native `paper.docx`.
* **Milestone 5**: Generation of Demo, Poster, and Presentation packages.
* **Milestone 6**: Execution of final research integrity and numerical consistency audits.
* **Milestone 7**: Compilation of authoritative Phase 10 completion report.
