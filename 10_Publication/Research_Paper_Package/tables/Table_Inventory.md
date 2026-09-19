# Master Publication Table Inventory

**Project**: ScholarCamp  
**Core System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  
**Document**: `10_Publication/04_Tables/Table_Inventory.md`  
**Date**: September 19, 2026  
**Status**: COMPLETE & VERIFIED  

---

## Table Catalog & Provenance

### Table 1: Predictive Model Performance & Calibration Benchmark
* **LaTeX Source**: `table1_model_performance.tex`
* **Markdown Source**: `model_performance_table.md`
* **CSV Source**: `model_performance.csv`
* **Evaluated Benchmark**: $N=500$ Hold-Out Test Split (Seed 42) on `DS-SYNTH-01`
* **Content**: Accuracy, Precision, Recall, Macro-F1, ROC-AUC, Brier Score, and Expected Calibration Error (ECE) across Logistic Regression, Random Forest, Uncalibrated XGBoost, and Platt-Calibrated XGBoost.
* **Paper Section**: Section VII (Results, Subsection A)

### Table 2: Multimodal Mock Interview Modality Ablation
* **LaTeX Source**: `table2_modality_ablation.tex`
* **Markdown Source**: `ablation_table.md`
* **CSV Source**: `modality_ablation.csv`
* **Evaluated Benchmark**: $N=50$ Simulated Sessions (`DS-INTERVIEW-SIM`)
* **Content**: Feature modalities (Acoustic Prosody, Visual Composure, Speech Clarity, Late Multimodal Fusion), extracted indicators, diagnostic variance ($R^2$), Macro-F1, and statistical significance ($p$-value vs Fusion).
* **Paper Section**: Section VII (Results, Subsection C)

### Table 3: Prescriptive Counterfactual Recourse Optimization & Invariance
* **LaTeX Source**: `table3_recourse_feasibility.tex`
* **Markdown Source**: `recourse_table.md`
* **CSV Source**: `recourse_feasibility.csv`
* **Evaluated Benchmark**: $N=30$ At-Risk Student Candidate Profiles
* **Content**: Comparison between Unconstrained Gradient Descent, Standard DiCE (Without Lock), and PRIE Constrained DiCE across Mean $L_1$ Distance, Mean $L_2$ Distance, Mean Sparsity ($k$), and $F_{17}$ Immutable Lock Preservation Rate.
* **Paper Section**: Section VII (Results, Subsection B)

### Table 4: Comprehensive Empirical Research Validation Suite
* **LaTeX Source**: `table4_experimental_summary.tex`
* **Markdown Source**: `experimental_summary_table.md`
* **Evaluated Benchmark**: Complete Experimental Protocol (`EXP-1` through `EXP-6`)
* **Content**: Summary of Experiment ID, core experimental focus, dataset/artifact, primary metric, observed performance, and formal statistical significance test results.
* **Paper Section**: Section VII (Results, Subsection E)
