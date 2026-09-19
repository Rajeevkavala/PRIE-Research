# Research Question to Experiment Traceability Matrix
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/01_Experiment_Design/Research_Question_Experiment_Matrix.md`  

---

## 1. Master RQ Traceability Matrix

This matrix establishes the bidirectional deductive chain connecting each Phase 03 Research Question to its empirical operationalization:

| RQ ID | Research Question Focus | Linked Literature Gap | Theoretical Hypothesis | Operational Experiment | Primary Quantitative Metric | Statistical Test | Target Empirical Standard | Status |
|:---:|:---|:---:|:---:|:---:|:---|:---|:---|:---:|
| **RQ1** | Multimodal Spatial ATS Resume Parsing & NER | `CG4` | `H1` | `EXP-04` (ATS Parsing) & `EXP-01` (Calibration) | Entity Boundary-F1; Brier Score; ECE | Paired Wilcoxon; McNemar's test | $\Delta F1 \ge +0.15$ on multi-column; Brier $\le 0.08$ | **SUPPORTED (EXP-01) / PARTIAL (EXP-04)** |
| **RQ2** | Low-Latency Real-Time Multimodal Mock Interview | `CG5`, `CG1` | `H2` | `EXP-03` (Multimodal Ablation) | Diagnostic Score Variance ($\sigma^2$); Latency (ms) | Paired Student's $t$-test | Variance Reduction $> 50\%$; Latency $< 1.5$s | **SUPPORTED (Simulation)** |
| **RQ3** | Dynamic Placement Prediction & Sequence Modeling | `CG3` | `H3` | `EXP-01` (Predictive Calibration) | Macro-F1; ROC-AUC; Quantile Loss | McNemar's test; DeLong's test | Macro-F1 $\ge 0.92$; ROC-AUC $\ge 0.95$ | **SUPPORTED (Synthetic)** |
| **RQ4** | Prescriptive Distance-Constrained Counterfactuals | `CG2` | `H4` | `EXP-02` (DiCE Recourse) | $F_{17}$ Invariance %; Sparsity ($k$); Reachability % | Exact constraint audit; $t$-test | Invariance $= 100\%$; Sparsity $k \le 3$ | **SUPPORTED (Algorithmic)** |
| **RQ5** | Causal Concept DAG Guided AQG & Discrimination | `CG7` | `H5` | `EXP-05` (Roadmap DAG) & `EXP-06` (RAG Guardrails) | Prerequisite Violations; Item Discrimination ($D$) | Wilcoxon Signed-Rank; Fisher's exact | Violations $= 0$; Discrimination $D \ge 0.80$ | **SUPPORTED (DAG Verification)** |
| **RQ6** | Closed-Loop Triangular Digital Twin Integration | `CG1`, `CG6`, `CG8` | `H6` | `EXP-05` (Roadmap) & `EXP-06` (RAG Guardrails) | Placement Yield Uplift (%); OOD Rejection % | Two-proportion $Z$-test; Survival analysis | Conversion Uplift $\ge 15\%$; OOD Rej $= 100\%$ | **GUARDRAIL SUPPORTED / COHORT NOT YET AVAIL** |
