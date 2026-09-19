# SCHOLARCAMP / PRIE: PHASE 09 MASTER CLAIM LEDGER
**Project**: ScholarCamp  
**Core Subsystem**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Document**: `09_Results/PHASE_09_CLAIM_LEDGER.md`  
**Authority**: Level 9 Research Governance & Epistemological Ledger  
**Status**: ACTIVE & EMPIRICALLY CERTIFIED  

---

## 1. Master Scientific Claim Ledger

This ledger rigorously evaluates every primary scientific, algorithmic, and architectural claim made within the ScholarCamp / PRIE research project against verified empirical evidence.

| Claim ID | Formal Scientific Claim | Claim Type | Source Experiment | Dataset | Primary Metric | Observed Result | Statistical Support | Primary Artifact | Verification Status |
|:---:|:---|:---:|:---:|:---:|:---|:---:|:---|:---|:---:|
| **CLM-01** | Platt-calibrated XGBoost achieves high placement classification discrimination and satisfies strict probabilistic calibration criteria ($	ext{Brier} \le 0.08, 	ext{ECE} \le 0.05$). | Empirical / Algorithmic | `EXP-01` | `DS-SYNTH-01` | Brier Score & ECE | Brier $= 0.0339 \pm 0.0096$; ECE $= 0.0350 \pm 0.0057$ | Calibration curve binning; $p < 0.001$ | `08_Experiments/15_Experiment_Results/EXP-1/metrics/` | **SUPPORTED (Synthetic)** |
| **CLM-02** | Gradient-boosted decision trees demonstrate statistically significant predictive superiority over balanced Random Forest baselines on the 22D SPV. | Algorithmic Comparison | `EXP-01` | `DS-SYNTH-01` | Macro-F1 & Accuracy | Macro-F1 $= 0.9390$ vs $0.8935$; Accuracy $= 0.9520$ vs $0.9160$ | McNemar $\chi^2 = 5.8824, p=0.0153$; Wilcoxon $W=27.0, p=0.0076$ | `08_Experiments/15_Experiment_Results/EXP-1/statistics/` | **SUPPORTED (Synthetic)** |
| **CLM-03** | Prescriptive DiCE counterfactual optimization generates sparse ($k \le 3$) actionable recourses while maintaining 100% invariance on immutable academic features ($F_{17}$). | Algorithmic / Ethical | `EXP-02` | `DS-SYNTH-01` | $F_{17}$ Invariance % & Sparsity ($k$) | $F_{17}$ Invariance $= 100.0\%$; Mean $k = 2.47 \le 3.0$ | Exact constraint verification across 30 at-risk profiles | `08_Experiments/15_Experiment_Results/EXP-3/processed/` | **SUPPORTED (Algorithmic)** |
| **CLM-04** | Late Multimodal Fusion (audio, video, speech) dampens transient single-sensor noise and reduces diagnostic assessment variance by $> 50\%$ over unimodal pipelines. | Architectural / Multimodal | `EXP-03` | `DS-INTERVIEW-SIM` | Variance Reduction % | $\sigma^2$ reduced from $79.21 	o 17.64$ ($77.98\% \pm 3.99\%$ reduction) | Paired Student's $t$-test ($t=9.88, p=0.0022$); Cohen's $d = 2.14$ | `08_Experiments/15_Experiment_Results/EXP-2/metrics/` | **SUPPORTED (Simulated)** |
| **CLM-05** | Multimodal mock interview scoring correlates strongly with independent human corporate recruiter panels ($r \ge 0.82$). | External Empirical | `EXP-03` | `DS-INTERVIEW-PILOT` | Pearson $r$ / Spearman $\rho$ | Pending live recruiter panel evaluation | N/A (Physical human trial not yet conducted) | `08_Experiments/16_Research_Evidence/Unsupported_Claims.md` | **UNSUPPORTED / PENDING TRIAL** |
| **CLM-06** | 2D spatial coordinate tokenization (PyMuPDF) resolves column interleaving on complex multi-column resumes, outperforming flat-text regex parsers. | Methodological | `EXP-04` | Resume Test Portfolio | Entity Boundary Macro-F1 | Spatial Macro-F1 $= 0.8421$ vs Flat regex $0.6857$ ($\Delta = +0.1564$) | Directional performance audit on multi-column layouts | `08_Experiments/15_Experiment_Results/EXP-4/tables/` | **PARTIALLY_SUPPORTED** |
| **CLM-07** | Fine-tuned LayoutLMv3 achieves state-of-the-art token extraction F1 on multi-column student resumes. | Deep Learning | `EXP-04` | `DS-CORPUS-01` | Token F1 | Model weights not yet trained in runtime environment | Model labeled honestly as `MODEL NOT TRAINED` | `08_Experiments/07_EXP_04_ATS/Parsing_Comparison.md` | **UNSUPPORTED / NOT TRAINED** |
| **CLM-08** | In-degree topological sorting (Kahn's algorithm) over a computer science concept DAG eliminates 100% of educational prerequisite sequencing errors. | Graph Algorithmic | `EXP-05` | `cs_concept_dag.json` | Prerequisite Violations | Kahn Violations $= 0.0$ ($0.0\%$) vs Random $3.6 \pm 1.0$ ($36.0\%$) | Wilcoxon Signed-Rank Test ($W=0.0, p=0.0416$) | `08_Experiments/15_Experiment_Results/EXP-5/metrics/` | **SUPPORTED (Graph Exact)** |
| **CLM-09** | Two-stage curriculum RAG retrieval achieves 100% in-domain retrieval precision and 100% out-of-domain conversational hallucination rejection via cosine gating. | Retrieval / Guardrail | `EXP-06` | `resource_library.json`| Retrieval Precision & OOD Rejection | In-Domain Precision $= 100.0\%$; OOD Rejection $= 100.0\%$ | Exact binary classification across standardized query battery | `08_Experiments/15_Experiment_Results/EXP-6/metrics/` | **SUPPORTED (Guardrail)** |
| **CLM-10** | Closed-loop deployment of PRIE's placement digital twin produces a $+15\%$ institutional placement conversion uplift in graduating cohorts. | Institutional Impact | `EXP-06` | `DS-REAL-01` | Offer Conversion Rate Uplift | Institutional tracking requires multi-semester live deployment | N/A (Institutional ethics and multi-semester data required) | `08_Experiments/PHASE_08_EVIDENCE_LEDGER.md` | **UNSUPPORTED / DATA REQUIRED** |

---

## 2. Claim Governance Summary

- **Total Claims Audited**: 10
- **Supported (Algorithmic / Synthetic / Graph / Guardrail)**: 6 (60%)
- **Partially Supported (Spatial Baselines Active / Deep Pending)**: 1 (10%)
- **Unsupported / Pending Real-World Data Collection**: 3 (30%)
- **Scientific Integrity Violation Rate**: 0% (All unsupported claims are explicitly disclosed, calibrated, and downgraded).
