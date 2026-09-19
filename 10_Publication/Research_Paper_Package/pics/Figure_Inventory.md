# Master Publication Figure Inventory

**Project**: ScholarCamp  
**Core System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  
**Document**: `10_Publication/03_Figures/Figure_Inventory.md`  
**Date**: September 19, 2026  
**Status**: COMPLETE & VERIFIED  

---

## Figure Catalog & Provenance

### Figure 1: Calibration Reliability Diagrams
* **Filename**: `fig1_calibration_reliability.png`
* **Resolution**: 300 DPI ($3300 \times 2400$)
* **Source Experiment**: Phase 09 / `EXP-1`
* **Dataset**: `DS-SYNTH-01` ($N=250$ test partition, Seed 42)
* **Description**: Dual-panel reliability diagram comparing uncalibrated models (Left) against Platt-calibrated XGBoost (Right) across 10 empirical probability bins.
* **Key Metric**: ECE contracts from $0.0392$ to $0.0350 \pm 0.0057$; Brier score from $0.0354$ to $0.0339 \pm 0.0096$.
* **Paper Section**: Section VII (Results, Subsection A)

### Figure 2: ROC and Precision-Recall Trajectories
* **Filename**: `fig2_roc_pr_curves.png`
* **Resolution**: 300 DPI ($3300 \times 1650$)
* **Source Experiment**: Phase 09 / `EXP-1`
* **Dataset**: `DS-SYNTH-01` (Multi-seed aggregate across 5 seeds)
* **Description**: Multi-model ROC (Left) and Precision-Recall (Right) curves comparing Logistic Regression, PRIE XGBoost, and Random Forest.
* **Key Metric**: XGBoost achieves ROC-AUC of $0.9922 \pm 0.0038$ and PR-AUC of $0.9912 \pm 0.0045$.
* **Paper Section**: Section VII (Results, Subsection A)

### Figure 3: TreeSHAP Global Feature Importance
* **Filename**: `fig3_shap_importance.png`
* **Resolution**: 300 DPI ($3000 \times 2400$)
* **Source Experiment**: Phase 09 / `EXP-1` (XAI Module $M_{07}$)
* **Dataset**: `DS-SYNTH-01` ($N=250$ test students)
* **Description**: TreeSHAP summary bee-swarm plot showing marginal log-odds impacts of tabular features $F_1$ to $F_{18}$.
* **Key Finding**: Technical coding ($F_1$) and CGPA ($F_2$) dominate predictions; protected attributes ($F_{17}$ branch) have near-zero impact ($|\phi| < 0.002$).
* **Paper Section**: Section VII (Results, Subsection B)

### Figure 4: Multimodal Modality Ablation
* **Filename**: `fig4_multimodal_ablation.png`
* **Resolution**: 300 DPI ($3000 \times 1800$)
* **Source Experiment**: Phase 09 / `EXP-3` (Interview Module $M_{05}$)
* **Dataset**: `DS-INTERVIEW-SIM` ($N=50$ simulated sessions)
* **Description**: Bar chart showing diagnostic score variance ($\sigma^2$) across unimodal, bimodal, and tri-modal late fusion.
* **Key Metric**: Late fusion reduces variance by $77.98\% \pm 3.99\%$ ($\sigma^2 = 17.64$ vs unimodal speech $79.21$, $t=9.88, p=0.0022$).
* **Paper Section**: Section VII (Results, Subsection C)

### Figure 5: Concept DAG Prerequisite Structure
* **Filename**: `fig5_concept_dag_progression.png`
* **Resolution**: 300 DPI ($3600 \times 2400$)
* **Source Experiment**: Phase 09 / `EXP-5` (Roadmap Module $M_{08}$)
* **Dataset**: `cs_concept_dag.json` (38 concepts, 52 directed edges)
* **Description**: Hierarchical directed acyclic graph illustrating concept dependencies across 5 foundational tiers and student mastery heatmap.
* **Key Metric**: Kahn's topological sort eliminates prerequisite precedence violations ($0$ violations, $0.0\%$, $p=0.0416$).
* **Paper Section**: Section VII (Results, Subsection D)

### Figure 6: Student Persona Radar Profiles
* **Filename**: `fig6_persona_radar_profiles.png`
* **Resolution**: 300 DPI ($3000 \times 2400$)
* **Source Experiment**: Phase 09 / `EXP-1` & `EXP-2`
* **Dataset**: Representative diagnostic vectors
* **Description**: Six-axis competency radar plot overlaying 4 student archetypes (At-Risk Beginner, Coding Specialist, Balanced High-Performer, Communication-Deficient Engineer).
* **Key Finding**: Demonstrates multi-dimensional diagnostic separation, isolating actionable skill gaps for DiCE recourse.
* **Paper Section**: Section I (Introduction) / Section VIII (Discussion)

### Architecture Figures
* **Figure 7**: `High_Level_Architecture.png` — PRIE 4-tier microservice architecture (Data Acquisition, Latent State Engine, Analytics/XAI, Adaptive Remediation).
* **Figure 8**: `SPV_Pipeline.png` — Continuous data ingestion pipeline transforming heterogeneous inputs into the 22-D Student Profile Vector.
