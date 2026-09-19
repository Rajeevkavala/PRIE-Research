# Systematic Ablation Study Matrix
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  

| Ablation Code | Subsystem | Full Model Configuration | Ablated Component Variant | Expected Impact | Observed Empirical Impact | Statistical Delta |
|:---:|:---|:---|:---|:---|:---|:---:|
| **ABL-1** | ATS Document Parser | LayoutLMv3 with $[x_0,y_0,x_1,y_1]$ spatial coordinates | Strip spatial coords (linear text only) | Boundary-F1 drops by $\ge 0.15$ | Flat regex Macro-F1 $= 0.6857$ vs Spatial $0.8421$ | $\Delta = -0.1564$ |
| **ABL-2** | Placement Predictor | Platt-Calibrated XGBoost ($M_{06}$) | Uncalibrated XGBoost | Calibration error degrades | ECE increases from $0.0236 	o 0.0612$, Brier from $0.0356 	o 0.0520$ | Brier $\Delta = +0.0164$ |
| **ABL-3** | Prescriptive Recourse | DiCE with locked $F_{17}$ and bounded mutable features | Unconstrained DiCE search | Suggests changing branch or lowering GPA | $F_{17}$ invariance drops from $100\% 	o 12\%$ | Violates educational ethics |
| **ABL-4** | Mock Interview | Late Multimodal Fusion (Audio + Video + Speech) | Single modality alone (Audio / Video / Speech) | Significant increase in diagnostic variance | Score variance increases by $170\%$ to $349\%$ | $p = 0.0022$ |
| **ABL-5** | Learning Roadmap | Kahn's Topological Sort on CS Concept DAG | Randomized milestone ordering | Severe prerequisite sequencing violations | Precedence violations increase from $0.0\% 	o 36.0\%$ | $p = 0.0416$ |
| **ABL-6** | Curriculum RAG | Dense retrieval with Cosine Gating | Zero cosine threshold gating | Model attempts to answer out-of-domain queries | OOD hallucination rejection drops from $100\% 	o 0\%$ | Exact safeguard failure |
