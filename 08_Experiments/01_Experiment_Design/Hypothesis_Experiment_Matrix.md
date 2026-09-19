# Hypothesis to Experiment Traceability Matrix
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  
**Document**: `08_Experiments/01_Experiment_Design/Hypothesis_Experiment_Matrix.md`  

---

## 1. Master Hypothesis Verification Matrix

| Hypothesis | Subsystem Tested | Null Hypothesis ($H_0$) | Alternative Hypothesis ($H_1$) | Experimental Pathway | Decision Rule | Empirical Outcome | Support Verdict |
|:---:|:---|:---|:---|:---:|:---|:---|:---:|
| **H1** | Predictive Calibration & Baselines | $	ext{Brier} > 0.08 \lor 	ext{ECE} > 0.05$ | $	ext{Brier} \le 0.08 \land 	ext{ECE} \le 0.05$ | `EXP-01` | Reject $H_0$ if Brier $\le 0.08$ and ECE $\le 0.05$ at $lpha = 0.05$ | Brier $= 0.0339 \pm 0.0096$; ECE $= 0.0350 \pm 0.0057$ | **SUPPORTED** |
| **H2** | Multimodal Mock Interview Fusion | $\sigma^2_{	ext{fused}} \ge \sigma^2_{	ext{unimodal}}$ | $\sigma^2_{	ext{fused}} < \sigma^2_{	ext{unimodal}}$ | `EXP-03` | Reject $H_0$ if Variance Reduction $> 50\%$ and $p < 0.05$ | Variance Reduction $= 77.98\% \pm 3.99\%$, $p = 0.0022$ | **SUPPORTED** |
| **H3** | Prescriptive Counterfactual Recourse | $	ext{Invar}(F_{17}) < 1.0 \lor k > 3.0$ | $	ext{Invar}(F_{17}) = 1.0 \land k \le 3.0$ | `EXP-02` | Reject $H_0$ if $F_{17}$ Invariance $= 100\%$ and mean $k \le 3$ | Invariance $= 100.0\%$, mean $k = 2.47$ | **SUPPORTED** |
| **H4** | ATS Spatial Document Intelligence | $	ext{F1}_{	ext{spatial}} \le 	ext{F1}_{	ext{flat}}$ | $	ext{F1}_{	ext{spatial}} > 	ext{F1}_{	ext{flat}}$ | `EXP-04` | Reject $H_0$ if spatial extraction F1 significantly exceeds flat regex | Spatial macro-F1 $= 0.8421$ vs regex $0.6857$; LayoutLMv3 pending | **PARTIALLY SUPPORTED** |
| **H5** | Curriculum RAG Grounding & AQG | $	ext{Rej}_{	ext{OOD}} < 0.90 \lor 	ext{Prec}_{	ext{In}} < 0.90$ | $	ext{Rej}_{	ext{OOD}} \ge 0.90 \land 	ext{Prec}_{	ext{In}} \ge 0.90$ | `EXP-06` | Reject $H_0$ if In-Domain Prec $= 100\%$ and OOD Rejection $= 100\%$ | Precision $= 100.0\%$, Rejection $= 100.0\%$ | **SUPPORTED** |
| **H6** | Concept DAG Topological Scheduling | $	ext{Violations}_{	ext{Kahn}} > 0$ | $	ext{Violations}_{	ext{Kahn}} = 0$ | `EXP-05` | Reject $H_0$ if Kahn sort eliminates 100% of prerequisite violations | Kahn Violations $= 0.0$ vs Random $= 3.6 \pm 1.0$ ($p = 0.0416$) | **SUPPORTED** |
