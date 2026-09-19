# PRIE Research Paper & Complete Asset Package

This directory is the unified, self-contained publication package for the research paper:
> **PRIE: Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse**  
> *Authors*: Sivasubramanian R, Kavala Rajeev, Kundala Dhana Naga Shankar, Kouru Rudra Teja  
> *Department of Artificial Intelligence and Machine Learning (AIML), Malla Reddy University, Hyderabad, India*

---

## Package Directory Structure

```
Research_Paper_Package/
├── README.md                                 # Package index, directory overview, and guide
├── FULL_RESEARCH_PAPER.md                    # Complete, publication-grade research paper in Markdown
├── pics/                                     # High-resolution architectural figures and experimental plots
│   ├── Component_Diagram.png                 # Microservice component interaction diagram
│   ├── High_Level_Architecture.png           # End-to-end 4-tier high level architecture
│   ├── PRIE_Pipeline.png                     # End-to-end analytics and remediation pipeline
│   ├── SPV_Pipeline.png                      # SPV aggregation and preprocessing pipeline
│   ├── fig1_calibration_reliability.png      # Platt calibration reliability diagrams (EXP-1)
│   ├── fig2_roc_pr_curves.png                # ROC and Precision-Recall comparison curves (EXP-1)
│   ├── fig2_spv_feature_distribution.png     # Correlation and distribution of 22 SPV features
│   ├── fig3_shap_importance.png              # TreeSHAP global feature attribution beeswarm (EXP-2)
│   ├── fig4_multimodal_ablation.png          # Tri-modal ablation and variance reduction (EXP-3)
│   ├── fig5_concept_dag_progression.png      # 38-node computer science prerequisite DAG (EXP-5)
│   ├── fig6_persona_radar_profiles.png       # Radar competency profiles for student archetypes
│   ├── prie_dashboard_output.png             # Placement officer and student dashboard interface
│   ├── prie_page1.png                        # Conference paper rendered preview page 1
│   ├── vr_page1.png                          # Dual-format camera-ready preview page 1
│   ├── Figure_Inventory.md                   # Full caption, dimensions, and provenance inventory
│   └── figures_manifest.md                   # Machine-readable figure metadata manifest
├── tables/                                   # All empirical result tables in Markdown, LaTeX, and CSV
│   ├── Table_Inventory.md                    # Table catalog and structural documentation
│   ├── table1_model_performance.md           # EXP-1 discrimination & calibration table (Markdown)
│   ├── table1_model_performance.tex          # EXP-1 discrimination & calibration table (IEEE LaTeX)
│   ├── table2_modality_ablation.md           # EXP-3 mock interview modality ablation (Markdown)
│   ├── table2_modality_ablation.tex          # EXP-3 mock interview modality ablation (IEEE LaTeX)
│   ├── table3_recourse_feasibility.md        # EXP-2 counterfactual recourse & sparsity (Markdown)
│   ├── table3_recourse_feasibility.tex       # EXP-2 counterfactual recourse & sparsity (IEEE LaTeX)
│   ├── table4_experimental_summary.md        # EXP-1 to EXP-6 comprehensive summary matrix (Markdown)
│   ├── table4_experimental_summary.tex       # EXP-1 to EXP-6 comprehensive summary matrix (IEEE LaTeX)
│   ├── table5_literature_benchmark_comparison.md # Benchmarking against published EDM literature
│   ├── ablation_table.md                     # Markdown view of multimodal ablation
│   ├── model_performance_table.md            # Markdown view of predictive benchmark
│   └── recourse_table.md                     # Markdown view of counterfactual recourse
└── data/                                     # Raw datasets, feature configurations, and aggregate metrics
    ├── dataset_manifest.md                   # Complete specification of benchmark cohorts (N=2,500)
    ├── model_performance.csv                 # Raw CSV metrics across Logistic Reg, RF, and XGBoost
    ├── modality_ablation.csv                 # Raw CSV variance reduction metrics across interview streams
    ├── recourse_feasibility.csv              # Raw CSV counterfactual distances, sparsity, and lock rates
    ├── multi_seed_aggregate.json             # Exhaustive 5-seed benchmark metric distribution JSON
    └── config.json                           # 22-dimensional SPV definition and model hyperparameters
```

---

## How to View and Use the Research Paper

- **Markdown Paper**: Open [FULL_RESEARCH_PAPER.md](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/Research_Paper_Package/FULL_RESEARCH_PAPER.md) in any standard Markdown viewer, VS Code / Antigravity IDE preview, GitHub, or Obsidian. All embedded images link directly to the local `pics/` directory (`pics/...`).
- **LaTeX Paper**: The camera-ready IEEE conference LaTeX source is maintained in [paper.tex](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/01_Conference_Paper/paper.tex).
- **Compiled PDF**: The compiled 6-page IEEE two-column paper is available at [paper.pdf](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/01_Conference_Paper/paper.pdf).
- **Word Document**: The Word formatted manuscript is available at [paper.docx](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/01_Conference_Paper/paper.docx).

---

## Key Experimental Results Summary

| Metric | Target | Observed Result | Significance / Test |
|:---|:---:|:---:|:---:|
| **Expected Calibration Error ($ECE$)** | $\le 0.05$ | **$0.0350 \pm 0.0057$** | Platt Sigmoid Scaling |
| **Brier Score** | $\le 0.08$ | **$0.0339 \pm 0.0096$** | 5-seed cross-validation |
| **ROC-AUC** | $\ge 0.95$ | **$0.9922 \pm 0.0038$** | Hold-out evaluation |
| **Accuracy** | Baseline | **$94.60\%$** | +3.4% to +16.2% over literature |
| **Counterfactual Sparsity ($k$)** | $\le 3.0$ features | **$2.47 \pm 0.52$** | $t = -5.84, p < 0.0001$ |
| **Protected Attribute Invariance ($F_{17}$)** | $100.0\%$ | **$100.0\%$ Locked** | Zero demographic leakage |
| **Multimodal Variance Reduction** | $\ge 20.0\%$ | **$77.98\% \pm 3.99\%$** | $t = 9.88, p = 0.0022$ |
| **Curriculum DAG Precedence Violations** | $0.0\%$ | **$0.0\%$ ($0$ violations)** | $W = 0.0, p = 0.0416$ |
| **Adversarial RAG OOD Rejection** | $\ge 90.0\%$ | **$100.0\%$ Rejection** | Fisher's exact $p = 0.0286$ |
