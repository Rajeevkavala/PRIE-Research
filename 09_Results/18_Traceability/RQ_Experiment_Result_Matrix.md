# Research Question to Experiment & Result Traceability Matrix

## 1. Overview
This matrix establishes bidirectional traceability between the six foundational research questions formulated in Phase 03/06, their operationalizing experiments executed in Phase 08, and the empirical results synthesized in Phase 09.

---

## 2. RQ-Experiment-Result Mapping Matrix

| Research Question | Associated Experiment | Evaluated System Module | Primary Evaluation Metric | Empirical Result Observed | Statistical Significance | Answering Section & Status |
|:---|:---:|:---:|:---|:---|:---:|:---|
| **RQ1: Predictive Calibration**<br>*Can ensemble learning with Platt scaling yield well-calibrated placement predictions ($ECE \le 0.05$)?* | **EXP-1** | M03 Diagnostic Model | Expected Calibration Error ($ECE$), Brier Score, Macro-F1, ROC-AUC | $ECE = 0.0350 \pm 0.0057$<br>$Brier = 0.0339 \pm 0.0096$<br>$F1 = 0.9390 \pm 0.0187$<br>$AUC = 0.9922 \pm 0.0038$ | McNemar: $\chi^2 = 5.8824, p = 0.0153$<br>Wilcoxon: $W = 27.0, p = 0.0076$ | [RQ1_Answer.md](../14_Research_Questions/RQ1_Answer.md)<br>**CONFIRMED** |
| **RQ2: Actionable Recourse**<br>*Can DiCE generate sparse ($k \le 3$), feasible counterfactual interventions while strictly preserving immutable protected attributes?* | **EXP-2** | M07 Prescriptive Engine | Immutable attribute preservation ($F_{17}$), Sparsity ($k$), $L_1$ cost, Reachability | $F_{17}$ Lock $= 100.0\%$ ($\Delta=0.0$)<br>Sparsity $k = 2.47 \pm 0.52$<br>$L_1 = 0.283 \pm 0.045$<br>Reachability $= 93.3\%$ | $t = -5.84, p < 0.0001$<br>Cohen's $d = 2.82$<br>$95\%$ CI: $[2.28, 2.66]$ | [RQ2_Answer.md](../14_Research_Questions/RQ2_Answer.md)<br>**CONFIRMED** |
| **RQ3: Multimodal Diagnostic Stabilization**<br>*Does late tri-modal fusion dampen single-sensor variance ($\ge 20\%$) and latency during mock technical interviews?* | **EXP-3** | M05 Mock Interview Engine | Cross-session diagnostic variance ($\sigma^2$), Variance reduction $\%$, Turnaround latency | $\sigma^2_{\text{late}} = 17.64$<br>Variance Red. $= 77.98\% \pm 3.99\%$<br>Latency $= 1.18 \pm 0.14$s | Paired $t = 9.88, p = 0.0022$<br>Cohen's $d = 2.14$<br>$95\%$ CI: $[74.5\%, 81.5\%]$ | [RQ3_Answer.md](../14_Research_Questions/RQ3_Answer.md)<br>**CONFIRMED** |
| **RQ4: Spatial ATS Parsing**<br>*Does 2D spatial coordinate tracking reduce entity interleaving and improve resume parsing F1 ($\ge 0.80$)?* | **EXP-4** | M01 ATS Resume Engine | Entity Extraction Macro-F1, Section Scramble Interleaving $\%$, Latency | Spatial Macro-F1 $= 0.8421$<br>Scramble Interleave $= 4.2\%$<br>Parse Latency $= 0.42$s | Margin: $+0.1564$ vs 1D Regex ($0.6857$)<br>Interleave drops from $78.4\%$ to $4.2\%$ | [RQ4_Answer.md](../14_Research_Questions/RQ4_Answer.md)<br>**CONFIRMED** |
| **RQ5: Prerequisite-Preserving Sequencing**<br>*Does topological DAG scheduling eliminate prerequisite precedence violations in personalized learning roadmaps?* | **EXP-5** | M04 Personalized Roadmap Engine | Prerequisite Precedence Violation Count and $\%$, Topological reachability | Violations $= 0$ ($0.0\%$ rate)<br>Schedule Validity $= 100.0\%$ | Exact Wilcoxon: $W = 0.0, p = 0.0416$<br>Random baseline $= 36.0\%$ violations | [RQ5_Answer.md](../14_Research_Questions/RQ5_Answer.md)<br>**CONFIRMED** |
| **RQ6: RAG Precision & Hallucination Mitigation**<br>*Does cosine similarity gating ($\tau = 0.70$) ensure in-domain curriculum retrieval while rejecting out-of-domain queries?* | **EXP-6** | M06 RAG / AQG Engine | In-Domain Retrieval Precision, Out-of-Domain (OOD) Query Rejection Rate | In-Domain Precision $= 100.0\%$<br>OOD Rejection $= 100.0\%$<br>Cosine Margin $\Delta = 0.486$ | Fisher / Exact Binomial: $p = 0.0286$<br>Separation margin $t = 14.32, p < 0.0001$ | [RQ6_Answer.md](../14_Research_Questions/RQ6_Answer.md)<br>**CONFIRMED** |

---

## 3. Bidirectional Navigation Links
* Full synthesis of all research question answers: [`RQ_Synthesis.md`](../14_Research_Questions/RQ_Synthesis.md)
* Individual experimental test reports: [`02_Experiment_Results/`](../02_Experiment_Results/)
* Underlying multi-seed aggregation artifact: [`multi_seed_aggregate.json`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/08_Experiments/15_Experiment_Results/multi_seed_aggregate.json)
