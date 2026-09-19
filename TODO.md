# PRIE Research Action Agenda & TODO

This document maintains actionable, prioritized research tasks across all repository phases.

---

## Immediate Priorities (Execution Phase)

- [x] Create standardized root directory skeleton for all 12 phases.
- [x] Mirror existing `Research-Knowledge-Base` into `01_Research_Foundation/`.
- [x] Generate complete `References.bib` and 48 individual `.bib` files.
- [x] Mirror existing Colab notebook and model weights into `07_Implementation/`.
- [ ] Author 16 cross-paper synthesis documents in `02_Cross_Analysis/`.
- [ ] Formalize research problem, 5 literature gaps, and RQs in `03_Research_Problem/`.
- [ ] Build exhaustive 22-feature traceability matrix in `04_Research_Evidence/Feature_Traceability.md`.
- [ ] Author algorithm and module justifications in `04_Research_Evidence/`.
- [ ] Document multi-tier system architecture and generate SVG diagrams in `05_PRIE_Architecture/`.
- [ ] Formalize empirical methodology and mathematical equations in `06_Methodology/`.
- [ ] Detail experimental baselines and PRS ablation design in `08_Experiments/`.
- [ ] Document verified experimental metrics and SHAP rankings in `09_Results/`.
- [ ] Scaffold IEEE conference LaTeX manuscript (`paper.tex`) in `10_Publication/`.
- [ ] Author simulated Reviewer 1–3 critical reviews in `11_Review/`.
- [ ] Finalize target conference selection and cover letter in `12_Submission/`.

---

## Task List by Research Phase

### Phase 01: Research Foundation
- [x] Compile all 48 citations from literature survey into BibTeX format.
- [x] Organize individual BibTeX records in `Papers/BibTeX/`.
- [x] Verify that existing 10 domain directories in `Research-Knowledge-Base` are intact.

### Phase 02: Cross-Paper Analysis
- [ ] Compare tabular classifiers across graduate employability datasets.
- [ ] Synthesize XAI adoption patterns in educational data mining.
- [ ] Contrast lexical vs. dense semantic resume matching in ATS literature.
- [ ] Analyze demographic bias vectors in visual vs. audio-first mock interviews.
- [ ] Formulate RAG hallucination mitigation strategies across AQG studies.

### Phase 03: Research Problem
- [ ] Formalize the 5 core literature gaps: Integration, Explainability, Personalization, Scalability/Bias, Latent State.
- [ ] Define Research Questions RQ1 (Predictive validity), RQ2 (Explainability utility), RQ3 (Ablation contribution), RQ4 (Fairness & calibration).
- [ ] Define null ($H_0$) and alternative ($H_1$) hypotheses.

### Phase 04: Research Evidence
- [ ] Audit every single feature of the 22-dimensional Student Profile Vector against literature papers.
- [ ] Explicitly label unconfirmed features as *"Literature support not yet established"*.
- [ ] Formulate complete 8-stage traceability chain (Paper → Gap → Decision → Implementation → Experiment → Evidence).
- [ ] Document threats to validity (internal, external, construct, conclusion).

### Phase 05: PRIE Architecture
- [ ] Document formal mathematical definition of the 22-D SPV space.
- [ ] Define interface boundaries for all 12 modules.
- [ ] Create publication-quality SVG diagrams for PRIE workflow and pipeline.

### Phase 06: Methodology
- [ ] Formalize SMOTE minority oversampling applied strictly to training folds.
- [ ] Define TreeSHAP polynomial time computation and Shapley axiomatic properties.
- [ ] Document Bayesian optimization parameters (Optuna, 100 trials).

### Phase 07: Implementation
- [ ] Verify integrity of `ScholarCamp_PRIE_Google_Colab.ipynb`.
- [ ] Verify serialization of `xgb_model.pkl`, `scaler.pkl`, `feature_names.json`.
- [ ] Pinned dependencies documented in `requirements.txt`.

### Phase 08: Experiments
- [ ] Document 5-fold cross-validation setup and 70/15/15 stratified partition.
- [ ] Formulate benchmark comparisons against Amarnath et al. (2023), Suresh et al. (2022), Verma et al. (2023), Gupta et al. (2024).
- [ ] Document PRS component ablation experiment protocol.

### Phase 09: Results
- [ ] Record test metrics: 87.8% Accuracy, 0.941 AUC-ROC, 87.7% F1, 0.756 MCC.
- [ ] Document SHAP global importance ranking (CGPA #1, DSA #2, Gap Score #3).
- [ ] Document Mean Calibration Error (MCE = 0.025).

### Phase 10: Publication
- [ ] Structure IEEE conference template with 15 mandatory sections.
- [ ] Draft Presentation slide outline and poster design guidelines.

### Phase 11: Review
- [ ] Simulate adversarial peer reviews (Reviewer 1: EDM specialist, Reviewer 2: ML/Stats purist, Reviewer 3: Systems/HCI reviewer).
- [ ] Execute citation audit confirming zero phantom references.

### Phase 12: Submission
- [ ] Compile conference deadline calendar and formatting constraints.
- [ ] Draft formal editorial cover letter.
