# Official Conference Submission Checklist

**Document**: `10_Publication/05_Conference_Submission/Submission_Checklist.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  
**Target Venue Standards**: IEEE Transactions / Conference Double-Column Format  

---

## 24-Point Comprehensive Submission Verification Checklist

### 1. Title & Metadata
- [x] Title is concise, accurate, and avoids hype words: *PRIE: An Explainable Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse*.
- [x] Blinded author block properly formatted for double-blind peer review (`Anonymous Authors`, placeholder institution).
- [x] Primary keywords indexed: Educational Data Mining, Explainable AI, Algorithmic Recourse, Student Profile Vector, Probability Calibration, Multimodal Fusion, Curriculum Knowledge Graph.

### 2. Abstract & Introduction
- [x] Abstract is self-contained (under 250 words) and covers Problem, Gap, Approach, Methodology, Validated Results, and Epistemic Scope.
- [x] Introduction clearly articulates the employability crisis and existing fragmented solutions.
- [x] Six formal research questions (`RQ1`–`RQ6`) explicitly stated.
- [x] Five primary scientific contributions clearly enumerated.

### 3. Related Work & Research Gaps
- [x] Related work synthesized thematically across 44 verified primary research papers (`Paper01` to `Paper44`).
- [x] Five formal literature gaps (`CG1` to `CG5`) mapped directly to research questions.

### 4. System Architecture & Methodology
- [x] 4-Tier microservice architecture clearly defined.
- [x] Mathematical tensor definition of the 22-dimensional Student Profile Vector ($\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$) and observation mask $\mathbf{m} \in \{0, 1\}^{22}$ articulated.
- [x] Formulas provided for Platt scaling, DiCE loss with $F_{17}$ lock, tri-modal late fusion, PyMuPDF 2D coordinate sorting, Kahn's topological sort, and cosine similarity gated RAG.

### 5. Experimental Design & Results
- [x] Experimental benchmarks described (`DS-SYNTH-01`, `DS-INTERVIEW-SIM`, `cs_concept_dag.json`).
- [x] 5-seed cross-validation strategy explained ($\{42, 123, 456, 789, 2026\}$).
- [x] Table 1 (Predictive Performance & Calibration), Table 2 (Multimodal Ablation), Table 3 (Recourse Feasibility), and Table 4 (Experimental Summary) complete and certified.
- [x] Figure 1 (Calibration), Figure 2 (ROC/PR), Figure 3 (TreeSHAP), Figure 4 (Multimodal Ablation), Figure 5 (Concept DAG), and Figure 6 (Persona Radars) embedded at 300 DPI.
- [x] Inferential statistical significance tests reported with exact test statistics and $p$-values.

### 6. Discussion, Ethics & Epistemological Boundaries
- [x] Pedagogical actionability of SHAP and DiCE discussed.
- [x] High synthetic linear separability transparently disclosed.
- [x] Controlled synthetic simulation boundaries stated.
- [x] Real-world placement rate uplift ($H_{\text{uplift}}$) and recruiter panel correlation ($H_{\text{recruiter}}$) demarcated as `DATA COLLECTION REQUIRED` for post-publication field trials.
- [x] LayoutLMv3 GPU constraint disclosed (`MODEL NOT TRAINED`).

### 7. References & Artifact Files
- [x] All 44 citations match `references.bib` without ghost references or syntax errors.
- [x] Authoritative LaTeX manuscript ready (`paper.tex`).
- [x] Native Microsoft Word manuscript compiled and verified (`paper.docx`).
- [x] Accessible Markdown manuscript provided (`paper_manuscript.md`).
