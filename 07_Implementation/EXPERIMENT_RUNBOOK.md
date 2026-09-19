# PRIE EXPERIMENT RUNBOOK & REPRODUCIBILITY GUIDE
**System**: ScholarCamp / Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 07 — Research-Grade Implementation  
**Execution Subsystem**: `07_Implementation/PRIE_v1/experiments/`  
**Protocol Compliance**: Sections 29, 30, 31, 32, 33

---

## 1. Overview of Experimental Pathways

The PRIE research methodology defines six foundational experimental pathways to validate hypotheses $H_1$ through $H_6$:

1. **`EXP-1`**: Calibrated Placement Prediction & Multi-Baseline Benchmarks (Hypothesis $H_1$)
2. **`EXP-2`**: Multimodal Behavioral Mock Interview Ablation (Hypothesis $H_2$)
3. **`EXP-3`**: Prescriptive Counterfactual Recourse Feasibility & Invariance (Hypothesis $H_3$)
4. **`EXP-4`**: Spatial Resume Intelligence & ATS Scoring Ablation (Hypothesis $H_4$)
5. **`EXP-5`**: Placement Curriculum RAG Grounding & Hallucination Rejection (Hypothesis $H_5$)
6. **`EXP-6`**: A* Concept DAG Roadmap Precedence Scheduling (Hypothesis $H_6$)

---

## 2. CLI Execution Instructions

Navigate to the experiment root directory:
```bash
cd 07_Implementation/PRIE_v1/experiments
```

### Running Individual Experiments
To execute an experiment with a deterministic random seed:
```bash
python run_experiment.py --experiment EXP-1 --seed 42
python run_experiment.py --experiment EXP-2 --seed 42
python run_experiment.py --experiment EXP-3 --seed 42
python run_experiment.py --experiment EXP-4 --seed 42
python run_experiment.py --experiment EXP-5 --seed 42
python run_experiment.py --experiment EXP-6 --seed 42
```

### Executing All Experiments End-to-End
To run the complete experimental battery in a single deterministic pass:
```bash
python run_experiment.py --experiment all --seed 42
```

---

## 3. Output Artifact Structure

Every execution run exports a standardized research bundle under:
`07_Implementation/PRIE_v1/experiments/results/{EXPERIMENT_ID}/`

Each directory contains:
* `run_metadata.json`: Exact seed, timestamp, git commit, Python version, hardware configuration, and artifact SHA-256 checksums.
* `raw_metrics.json`: Full numerical metric dictionary (Accuracy, Precision, Recall, Macro-F1, ROC-AUC, Brier score, ECE).
* `summary.csv`: Tabular metric summary for spreadsheet analysis.
* `statistical_tests.json`: Formal hypothesis testing outputs (test name, test statistic, p-value, effect size, confidence interval, and hypothesis support verdict).
* `paper_table.tex`: Formatted publication-ready LaTeX table block ready for direct inclusion in the research paper.

---

## 4. Verification Quality Gates

Before incorporating results into academic manuscripts, verify that:
1. **$H_1$ Criterion**: Brier score $\le 0.08$ and $\text{ECE} \le 0.05$ for the calibrated model.
2. **$H_2$ Criterion**: Paired t-test / Wilcoxon $p < 0.05$ demonstrating multimodal superiority over unimodal baselines.
3. **$H_3$ Criterion**: 100% invariance on immutable feature $F_{17}$ (`branch_encoded`) and mean sparsity $k \le 3$.
4. **$H_4$ Criterion**: Multi-dimensional ATS demonstrates higher Macro-F1 than flat regex matching.
5. **$H_5$ Criterion**: Out-of-domain query rejection rate $= 100\%$.
6. **$H_6$ Criterion**: Kahn topological sort eliminates 100% of concept precedence violations ($0$ violations).
