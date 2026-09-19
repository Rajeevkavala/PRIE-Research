# SCHOLARCAMP / PRIE: PHASE 08 MASTER EVIDENCE LEDGER
**Project**: ScholarCamp  
**Core System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/PHASE_08_EVIDENCE_LEDGER.md`  
**Date**: September 2026  
**Status**: AUTHORITATIVE EMPIRICAL EVIDENCE LEDGER  

---

## 1. Master Evidence Ledger Entries

| Evidence ID | Experiment | RQ | Hyp. | Dataset | Sample Size | Method | Metric | Observed Value (Mean $\pm$ SD) | Statistical Test | p-value | Effect Size | Artifact Path | Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **EVD-01** | `EXP-01` | `RQ1/3` | `H1` | `DS-SYNTH-01` | $N=250$ test | Platt-Calibrated XGBoost | Brier Score Loss | **$0.0339 \pm 0.0096$** | Calibrated CV | $p < 0.001$ | Brier $\le 0.08$ | `15_Experiment_Results/EXP-1/metrics/` | **SUPPORTED (Synthetic)** |
| **EVD-02** | `EXP-01` | `RQ1/3` | `H1` | `DS-SYNTH-01` | $N=250$ test | Platt-Calibrated XGBoost | Expected Calibration Error | **$0.0350 \pm 0.0057$** | Reliability Binning | $p < 0.001$ | ECE $\le 0.05$ | `15_Experiment_Results/EXP-1/metrics/` | **SUPPORTED (Synthetic)** |
| **EVD-03** | `EXP-01` | `RQ1/3` | `H1` | `DS-SYNTH-01` | $N=250$ test | Platt-Calibrated XGBoost | Macro-averaged F1 | **$0.9390 \pm 0.0187$** | McNemar vs RF | $p = 0.0153$ | Wilcoxon $r=0.9983$ | `15_Experiment_Results/EXP-1/metrics/` | **SUPPORTED (Synthetic)** |
| **EVD-04** | `EXP-01` | `RQ1/3` | `H1` | `DS-SYNTH-01` | $N=250$ test | Platt-Calibrated XGBoost | ROC-AUC | **$0.9922 \pm 0.0038$** | ROC Analysis | $p < 0.001$ | AUC $\ge 0.95$ | `15_Experiment_Results/EXP-1/figures/fig2_roc_pr_curves.png` | **SUPPORTED (Synthetic)** |
| **EVD-05** | `EXP-03` | `RQ2` | `H2` | `DS-INTERVIEW-SIM` | $N=50$ sessions | Late Multimodal Fusion | Variance Reduction % | **$77.98\% \pm 3.99\%$** | Paired $t$-test | $p = 0.0022$ | Cohen's $d = 2.14$ | `15_Experiment_Results/EXP-2/metrics/` | **SUPPORTED (Simulated)** |
| **EVD-06** | `EXP-02` | `RQ4` | `H4` | `DS-SYNTH-01` | $N=30$ profiles | Prescriptive DiCE Recourse | $F_{17}$ Immutability Invariance | **$100.0\%$** | Exact Constraint Check | Exact | Invariance $= 1.0$ | `15_Experiment_Results/EXP-3/processed/` | **SUPPORTED (Algorithmic)** |
| **EVD-07** | `EXP-02` | `RQ4` | `H4` | `DS-SYNTH-01` | $N=30$ profiles | Prescriptive DiCE Recourse | Average Feature Sparsity ($k$) | **$2.47 \le 3.0$** | Sparsity Counting | Exact | $k \le 3$ Target Met | `15_Experiment_Results/EXP-3/processed/` | **SUPPORTED (Algorithmic)** |
| **EVD-08** | `EXP-05` | `RQ5/6` | `H6` | `cs_concept_dag.json` | 10 test topics | Kahn Topological Sort | Prerequisite Violations | **$0.0$ ($0.0\%$)** | Wilcoxon Signed-Rank | $p = 0.0416$ | 100% Precedence Match | `15_Experiment_Results/EXP-5/metrics/` | **SUPPORTED (Graph Invariant)** |
| **EVD-09** | `EXP-06` | `RQ6` | `H5` | `resource_library.json`| 7 queries | Two-Stage Curriculum RAG | OOD Hallucination Rejection | **$100.0\%$** | Exact Gating Check | Exact | Zero Hallucinations | `15_Experiment_Results/EXP-6/metrics/` | **SUPPORTED (Guardrail)** |
| **EVD-10** | `EXP-04` | `RQ1` | `H1` | Resume Test Portfolio | 3 resumes | Spatial PyMuPDF Parsing | Entity Extraction Macro-F1 | **$0.8421$** (Spatial) | Directional Audit | Directional | Higher than flat regex | `15_Experiment_Results/EXP-4/tables/` | **PARTIALLY VALIDATED** |
| **EVD-11** | `EXP-06` | `RQ6` | `H6` | `DS-REAL-01` | Target $N \ge 1,000$ | Closed-Loop Digital Twin | Placement Conversion Uplift | **DATA UNAVAILABLE** | Survival Analysis | N/A | N/A | N/A | **DATA_COLLECTION_REQUIRED** |
