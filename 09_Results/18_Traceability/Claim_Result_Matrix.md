# Scientific Claim to Empirical Result Traceability Matrix

## 1. Overview
This matrix provides strict scientific accountability by mapping each research claim made in ScholarCamp / PRIE documentation to its empirical validation status in Phase 09.

---

## 2. Claim Evaluation Ledger

| Claim ID | Core Scientific Claim | Associated Exp / Evidence ID | Empirical Verification Result | Scientific Decision Status | Epistemological Boundary / Caveat |
|:---:|:---|:---:|:---|:---:|:---|
| **CLM-01** | Gradient boosted ensembles with Platt scaling achieve superior calibration ($ECE \le 0.05$) on placement readiness prediction. | `EXP-1`<br>`EVD-01` | $ECE = 0.0350 \pm 0.0057$<br>$Brier = 0.0339 \pm 0.0096$<br>$ROC\text{-}AUC = 0.9922$ | **SUPPORTED** | Evaluated on synthetic tabular benchmark `DS-SYNTH-01`; real-world transfer remains to be tested in Phase 10. |
| **CLM-02** | Non-linear tree ensembles outperform linear models on complex student readiness features. | `EXP-1`<br>`EVD-02` | Logistic Regression achieved higher Macro-F1 ($0.9840$) than XGBoost ($0.9390$) due to linear separability of synthetic generator. | **CONDITIONALLY REJECTED** (On Synthetic Data) | In synthetic distributions, linear models dominate; tree ensembles are retained for non-linear real-world interactions and tabular tree interpretability. |
| **CLM-03** | Constrained DiCE optimization produces actionable, sparse recourse ($k \le 3$) while strictly preserving immutable protected attributes. | `EXP-2`<br>`EVD-03` | Sparsity $k = 2.47 \le 3.0$<br>$F_{17}$ lock $= 100.0\%$ preserved<br>Reachability $= 93.3\%$ | **SUPPORTED** | Tested on $N=30$ at-risk profiles; recourse paths are associative algorithmic recommendations, not causal guarantees. |
| **CLM-04** | Weighted late multimodal fusion dampens single-sensor noise and reduces diagnostic variance by $\ge 20\%$. | `EXP-3`<br>`EVD-04` | Variance reduction $= 77.98\% \pm 3.99\%$<br>$\sigma^2_{\text{late}} = 17.64$ vs $\sigma^2_{\text{speech}} = 79.21$<br>$t = 9.88, p = 0.0022$ | **SUPPORTED** | Evaluated on $N=50$ simulated sessions (`DS-INTERVIEW-SIM`); physical acoustic trials with human panels pending. |
| **CLM-05** | Multimodal mock interview scoring correlates strongly ($r \ge 0.82$) with expert corporate recruiter evaluations. | `EXP-3`<br>`EVD-05` | Human recruiter pilot panel dataset `DS-INTERVIEW-PILOT` has not yet been physically gathered. | **UNVERIFIED**<br>(`DATA COLLECTION REQUIRED`) | Ground truth recruiter correlation is explicitly marked as unverified pending Phase 10 human subject trials. |
| **CLM-06** | 2D spatial coordinate tracking mitigates column scrambling and improves resume entity extraction F1 ($\ge 0.80$). | `EXP-4`<br>`EVD-06` | PyMuPDF spatial Macro-F1 $= 0.8421$<br>Scrambling drops from $78.4\%$ to $4.2\%$ | **SUPPORTED** (Via Heuristics) | LayoutLMv3 deep model remains `MODEL NOT TRAINED`; verification achieved via PyMuPDF 2D geometric parsing. |
| **CLM-07** | Topological graph scheduling over prerequisite DAGs eliminates curriculum sequencing violations ($0.0\%$). | `EXP-5`<br>`EVD-07` | Precedence violations $= 0$ ($0.0\%$ rate)<br>Across all 5 evaluation seeds<br>$W = 0.0, p = 0.0416$ | **SUPPORTED** | Assumes acyclic knowledge graph (`cs_concept_dag.json`); non-linear/cyclic learning loops not currently supported. |
| **CLM-08** | Dense curriculum retrieval with cosine similarity gating ($\tau = 0.70$) prevents out-of-domain hallucinations. | `EXP-6`<br>`EVD-08` | In-domain retrieval precision $= 100.0\%$<br>OOD rejection rate $= 100.0\%$<br>Cosine margin $\Delta = 0.486$ | **SUPPORTED** | Evaluated on 1,420 curriculum chunks; performance depends on embedding quality and strictness of threshold $\tau$. |
| **CLM-09** | PRIE intervention produces a $\ge 15.0\%$ longitudinal uplift in campus recruitment conversion. | Longitudinal<br>`EVD-09` | Physical multi-semester student deployment has not been executed (`DS-REAL-01`). | **UNVERIFIED**<br>(`DATA COLLECTION REQUIRED`) | Strictly bounded as a prospective Phase 10 research hypothesis; zero causal uplift is claimed in Phase 09. |
| **CLM-10** | PRIE operates within sub-2-second turnaround latency for real-time interactive interview and diagnostic feedback. | System<br>`EVD-10` | Multimodal turnaround latency $= 1.18 \pm 0.14$s<br>ATS parse latency $= 0.42$s<br>Total pipeline $\le 1.80$s | **SUPPORTED** | Evaluated on local development benchmark environment (Intel/NVIDIA GPU setup). |

---

## 3. Claim Synthesis Summary
* **Fully Supported Claims**: 6 of 10 (`CLM-01`, `CLM-03`, `CLM-04`, `CLM-07`, `CLM-08`, `CLM-10`).
* **Supported with Algorithmic Caveats**: 1 of 10 (`CLM-06` supported via PyMuPDF; deep vision model unexecuted).
* **Conditionally Rejected**: 1 of 10 (`CLM-02` rejected on synthetic data due to high linear separability).
* **Unverified / Awaiting Human Trials**: 2 of 10 (`CLM-05` recruiter correlation, `CLM-09` placement uplift $\rightarrow$ `DATA COLLECTION REQUIRED`).
