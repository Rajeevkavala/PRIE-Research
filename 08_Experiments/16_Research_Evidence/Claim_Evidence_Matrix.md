# Claim to Empirical Evidence Traceability Matrix
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/16_Research_Evidence/Claim_Evidence_Matrix.md`  

---

## Master Claim Traceability Matrix

| Claim ID | Claim Text | Claim Type | Experiment | Dataset | Metric | Observed Value | Statistical Support | Epistemological Status |
|:---:|:---|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| **CLM-01** | Calibrated XGBoost meets strict probabilistic reliability criteria | EMPIRICAL | `EXP-01` | `DS-SYNTH-01` | Brier Score & ECE | Brier $= 0.0339 \pm 0.0096$; ECE $= 0.0350 \pm 0.0057$ | $p < 0.001$ calibration CV | **SUPPORTED (Synthetic)** |
| **CLM-02** | Calibrated XGBoost outperforms Random Forest on held-out test predictions | EMPIRICAL | `EXP-01` | `DS-SYNTH-01` | Macro-F1 | Macro-F1 $= 0.9390$ vs RF $0.8935$ | McNemar $p = 0.0153$; Wilcoxon $p = 0.0076$ | **SUPPORTED (Synthetic)** |
| **CLM-03** | Late Multimodal Fusion significantly reduces mock interview scoring variance | EMPIRICAL | `EXP-03` | `DS-INTERVIEW-SIM` | Score Variance ($\sigma^2$) | Variance reduction $= 77.98\% \pm 3.99\%$ | Paired $t$-test $p = 0.0022$ | **SUPPORTED (Simulated)** |
| **CLM-04** | DiCE recourse strictly guarantees immutability of student branch | METHODOLOGICAL | `EXP-02` | `DS-SYNTH-01` | $F_{17}$ Invariance % | $100.0\%$ Invariance | Exact constraint audit | **SUPPORTED (Algorithmic)** |
| **CLM-05** | DiCE recourse generates sparse, achievable remedial directives | EMPIRICAL | `EXP-02` | `DS-SYNTH-01` | Sparsity ($k$) | Mean $k = 2.47 \le 3$ features changed | Boundary audit | **SUPPORTED (Algorithmic)** |
| **CLM-06** | Kahn's topological sort eliminates prerequisite ordering violations | METHODOLOGICAL | `EXP-05` | `cs_concept_dag.json` | Prerequisite Violations | 0 Violations ($0.0\%$) vs Random $3.6 \pm 1.0$ ($36\%$) | Wilcoxon $W = 0.0, p = 0.0416$ | **SUPPORTED (Graph Invariant)** |
| **CLM-07** | Curriculum RAG retrieval reliably rejects out-of-domain conversational queries | IMPLEMENTATION | `EXP-06` | `resource_library.json` | OOD Rejection Rate | $100.0\%$ Rejection Accuracy | Exact query audit | **SUPPORTED (Guardrail)** |
| **CLM-08** | Real-world placement conversion rate is elevated by 15% across student cohorts | EMPIRICAL | `EXP-06 (Proposed)` | `DS-REAL-01` | Placement Conversion % | `NOT YET AVAILABLE` | Pending institutional trial | **NOT TESTABLE (Data Collection Required)** |
