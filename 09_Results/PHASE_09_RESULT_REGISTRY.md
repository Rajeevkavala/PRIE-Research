# SCHOLARCAMP / PRIE: PHASE 09 MASTER RESULT REGISTRY
**Project**: ScholarCamp  
**Core Subsystem**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Document**: `09_Results/PHASE_09_RESULT_REGISTRY.md`  
**Authority**: Single Authoritative Empirical Result Registry  
**Status**: ACTIVE & EMPIRICALLY CERTIFIED  

---

## 1. Master Empirical Result Registry

The table below catalogs every empirical result generated, audited, and synthesized within Phase 09, tracing each metric from its experimental execution run to publication artifacts and hypothesis assessments:

| Result ID | Experiment | Primary Metric | Evaluated Value (Mean $\pm$ SD) | Dataset | Seeds / Sample | Raw Artifact Path | Publication Artifact | Epistemological Status | Used in RQ | Used in Hypothesis | Publication Candidate |
|:---:|:---:|:---|:---:|:---:|:---:|:---|:---|:---:|:---:|:---:|:---:|
| **RES-01** | `EXP-01` | Accuracy | $0.9520 \pm 0.0117$ | `DS-SYNTH-01` | 5 seeds ($N=250$ test) | `08_Experiments/15_Experiment_Results/EXP-1/metrics/` | Table 1 / Tab:model_perf | **VALIDATED (Synthetic)** | `RQ1`, `RQ3` | `H1` | **YES** |
| **RES-02** | `EXP-01` | Macro-averaged F1 | $0.9390 \pm 0.0187$ | `DS-SYNTH-01` | 5 seeds ($N=250$ test) | `08_Experiments/15_Experiment_Results/EXP-1/metrics/` | Table 1 / Tab:model_perf | **VALIDATED (Synthetic)** | `RQ1`, `RQ3` | `H1` | **YES** |
| **RES-03** | `EXP-01` | ROC-AUC | $0.9922 \pm 0.0038$ | `DS-SYNTH-01` | 5 seeds ($N=250$ test) | `08_Experiments/15_Experiment_Results/EXP-1/metrics/` | Fig 2 / Table 1 | **VALIDATED (Synthetic)** | `RQ1`, `RQ3` | `H1` | **YES** |
| **RES-04** | `EXP-01` | Brier Score Loss | $0.0339 \pm 0.0096$ | `DS-SYNTH-01` | 5 seeds ($N=250$ test) | `08_Experiments/15_Experiment_Results/EXP-1/metrics/` | Fig 1 / Table 1 | **VALIDATED (Synthetic)** | `RQ1`, `RQ3` | `H1` | **YES** |
| **RES-05** | `EXP-01` | Expected Calibration Error | $0.0350 \pm 0.0057$ | `DS-SYNTH-01` | 5 seeds ($N=250$ test) | `08_Experiments/15_Experiment_Results/EXP-1/metrics/` | Fig 1 / Table 1 | **VALIDATED (Synthetic)** | `RQ1`, `RQ3` | `H1` | **YES** |
| **RES-06** | `EXP-01` | McNemar Test vs RF ($\chi^2$) | $\chi^2 = 5.8824, p = 0.0153$ | `DS-SYNTH-01` | Seed 42 ($N=250$) | `08_Experiments/15_Experiment_Results/EXP-1/statistics/` | Table 1 Notes | **VALIDATED (Synthetic)** | `RQ1`, `RQ3` | `H1` | **YES** |
| **RES-07** | `EXP-01` | Wilcoxon Test vs RF ($W$) | $W = 27.0, p = 0.0076, r = 0.9983$| `DS-SYNTH-01` | Seed 42 ($N=250$) | `08_Experiments/15_Experiment_Results/EXP-1/statistics/` | Table 1 Notes | **VALIDATED (Synthetic)** | `RQ1`, `RQ3` | `H1` | **YES** |
| **RES-08** | `EXP-02` | $F_{17}$ Immutability Invariance | **$100.0\%$** (0 violations) | `DS-SYNTH-01` | 5 seeds ($N=30$ profiles) | `08_Experiments/15_Experiment_Results/EXP-3/processed/` | Table 3 / Tab:recourse | **VALIDATED (Algorithmic)** | `RQ4` | `H3/H4` | **YES** |
| **RES-09** | `EXP-02` | Average Sparsity ($k$) | $2.47 \le 3.0$ features | `DS-SYNTH-01` | 5 seeds ($N=30$ profiles) | `08_Experiments/15_Experiment_Results/EXP-3/processed/` | Table 3 / Tab:recourse | **VALIDATED (Algorithmic)** | `RQ4` | `H3/H4` | **YES** |
| **RES-10** | `EXP-02` | Mean $L_1$ Distance | $0.283 \pm 0.045$ | `DS-SYNTH-01` | 5 seeds ($N=30$ profiles) | `08_Experiments/15_Experiment_Results/EXP-3/processed/` | Table 3 / Tab:recourse | **VALIDATED (Algorithmic)** | `RQ4` | `H3/H4` | **YES** |
| **RES-11** | `EXP-02` | Target Reachability Rate | $\ge 90.0\%$ | `DS-SYNTH-01` | 5 seeds ($N=30$ profiles) | `08_Experiments/15_Experiment_Results/EXP-3/processed/` | Table 3 / Tab:recourse | **VALIDATED (Algorithmic)** | `RQ4` | `H3/H4` | **YES** |
| **RES-12** | `EXP-03` | Multimodal Variance Reduction | **$77.98\% \pm 3.99\%$** | `DS-INTERVIEW-SIM` | 5 seeds ($N=50$ sessions) | `08_Experiments/15_Experiment_Results/EXP-2/metrics/` | Fig 4 / Table 2 | **VALIDATED (Simulated)** | `RQ2` | `H2` | **YES** |
| **RES-13** | `EXP-03` | Paired $t$-test Fusion vs Single | $t = 9.88, p = 0.0022$ | `DS-INTERVIEW-SIM` | 5 seeds ($N=50$ sessions) | `08_Experiments/15_Experiment_Results/EXP-2/metrics/` | Table 2 / Tab:modality | **VALIDATED (Simulated)** | `RQ2` | `H2` | **YES** |
| **RES-14** | `EXP-03` | Recruiter Panel Correlation | Pending physical trials | `DS-INTERVIEW-PILOT` | Target $N=100$ | N/A (Pending Trial) | N/A | **DATA_COLLECTION_REQUIRED**| `RQ2` | `H2` | **NO** |
| **RES-15** | `EXP-04` | Spatial Parsing Macro-F1 | **$0.8421$** | Resume Portfolio | 3 standard layouts | `08_Experiments/15_Experiment_Results/EXP-4/tables/` | Tab:ats_ablation | **PARTIALLY_VALIDATED** | `RQ1` | `H4/H1` | **YES** |
| **RES-16** | `EXP-04` | Flat Regex Parsing Macro-F1 | **$0.6857$** | Resume Portfolio | 3 standard layouts | `08_Experiments/15_Experiment_Results/EXP-4/tables/` | Tab:ats_ablation | **VALIDATED (Baseline)** | `RQ1` | `H4/H1` | **YES** |
| **RES-17** | `EXP-04` | LayoutLMv3 Fine-Tuning | MODEL NOT TRAINED | `DS-CORPUS-01` | Full benchmark | `08_Experiments/07_EXP_04_ATS/Parsing_Comparison.md` | Tab:ats_ablation | **NOT_EXECUTED** | `RQ1` | `H4/H1` | **YES (Disclosure)** |
| **RES-18** | `EXP-05` | Kahn Topological Sort Errors | **$0.0$ violations ($0.0\%$)** | `cs_concept_dag.json` | 5 seeds (10 CS topics) | `08_Experiments/15_Experiment_Results/EXP-5/metrics/` | Fig 5 / Tab:dag | **VALIDATED (Graph Exact)**| `RQ5`, `RQ6` | `H6` | **YES** |
| **RES-19** | `EXP-05` | Random Sequencing Errors | $3.6 \pm 1.0$ ($36.0\%$) | `cs_concept_dag.json` | 5 seeds (10 CS topics) | `08_Experiments/15_Experiment_Results/EXP-5/metrics/` | Tab:dag | **VALIDATED (Baseline)** | `RQ5`, `RQ6` | `H6` | **YES** |
| **RES-20** | `EXP-05` | Wilcoxon Test on Precedence ($W$)| $W = 0.0, p = 0.0416$ | `cs_concept_dag.json` | 5 seeds | `08_Experiments/15_Experiment_Results/EXP-5/metrics/` | Tab:dag Notes | **VALIDATED (Graph Exact)**| `RQ5`, `RQ6` | `H6` | **YES** |
| **RES-21** | `EXP-06` | In-Domain Retrieval Precision | **$100.0\%$** | `resource_library.json`| 5 seeds (4 domain queries) | `08_Experiments/15_Experiment_Results/EXP-6/metrics/` | Tab:rag_guardrail | **VALIDATED (Guardrail)** | `RQ6` | `H5` | **YES** |
| **RES-22** | `EXP-06` | Out-of-Domain Rejection Accuracy| **$100.0\%$** | `resource_library.json`| 5 seeds (3 OOD queries) | `08_Experiments/15_Experiment_Results/EXP-6/metrics/` | Tab:rag_guardrail | **VALIDATED (Guardrail)** | `RQ6` | `H5` | **YES** |
| **RES-23** | `EXP-06` | Real Institutional Cohort Uplift| DATA UNAVAILABLE | `DS-REAL-01` | Target $N \ge 1,000$ | N/A (Pending Institutional Ethics)| N/A | **DATA_COLLECTION_REQUIRED**| `RQ6` | `H6` | **NO** |

---

## 2. Status Taxonomy Definitions

- **`VALIDATED`**: The result is empirically derived from reproducible execution runs, supported by complete multi-seed statistical distributions and deterministic logging.
- **`PARTIALLY_VALIDATED`**: A verified functional baseline or heuristic pipeline is active and measured, but the deep learning architecture is pending full weights (`LayoutLMv3`).
- **`SYNTHETIC_ONLY`**: The evaluation is conducted exclusively on synthetic simulation cohorts (`DS-SYNTH-01`), validating algorithmic correctness without claiming real-world human outcome validity.
- **`DATA_COLLECTION_REQUIRED`**: The evaluation requires longitudinal human or institutional data collection (`DS-REAL-01`, `DS-INTERVIEW-PILOT`) that has not yet concluded.
- **`NOT_EXECUTED`**: An envisioned deep model or external benchmark that was not executed within the computational environment.
