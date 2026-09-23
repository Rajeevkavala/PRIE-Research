# PRIE Paper — Final Claim-Precision Update Audit Report

**Date**: 2026-09-19  
**Document**: `FINAL_CLAIM_PRECISION_UPDATE.md`  
**Manuscript**: `10_Publication/Conference_Paper/paper.tex`  
**Target Paper**: *PRIE: Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse*  

---

## 1. Changes Made

| ID | Location | Original Text | Updated Text | Reason |
|---|---|---|---|---|
| **C1.1** | Section I (Line 79) | `across our systematic review of the 44 verified career-readiness and educational analytics systems analyzed in our research foundation, 42 studies (95.5%, 42/44) address only one or two dimensions in isolation...` | `across our systematic review of the 44 verified career-readiness and educational analytics systems analyzed in our research foundation, 42 systems (95.5\%, 42/44) address only one or two dimensions in isolation...` | Aligns numerator ("systems") with denominator ("44 verified career-readiness systems") for terminology consistency. |
| **C1.2** | Section II-B (Line 138) | `Across our systematic review of the 44 verified career-readiness systems analyzed in our research foundation, 42 studies (95.5%, 42/44) evaluate only one or two functional dimensions in isolation...` | `Across our systematic review of the 44 verified career-readiness systems analyzed in our research foundation, 42 systems (95.5\%, 42/44) evaluate only one or two functional dimensions in isolation...` | Standardizes unit of analysis across research gap formulation to "systems". |
| **C2** | Section I (Line 103) | `...providing statistically calibrated probabilities for high-stakes advising.` | `...reducing probability calibration error under the evaluated synthetic-cohort conditions.` | Replaces wording implying real-world high-stakes advising deployment with precise synthetic experimental scope. Preserves ECE ($0.0350 \pm 0.0057$) and Brier ($0.0339 \pm 0.0096$). |
| **C3** | Section VII (Line 488) | `The empirical findings validate the central thesis of this research...` | `The empirical findings provide evidence supporting the central thesis of this research...` | Scientifically tempers "validate" to "provide evidence supporting", reflecting evaluation on synthetic cohorts and simulated sessions without prospective institutional validation. |
| **C4** | Section VI-E (Line 482) | `...100.0% rejection of evaluated out-of-domain queries and adversarial prompt injections...` | `...100.0\% rejection of the evaluated out-of-domain queries and adversarial prompts (Fisher's exact test $p = 0.02857$)...` | Restricts RAG guardrail claim strictly to the evaluated test set; removes unverified implication of universal prompt-injection immunity. |
| **C5** | Section VII-D (Line 500) | `...we interpret this reduction as algorithmic sensor stabilization on simulated students...` | `...we interpret this reduction as algorithmic variance reduction across the evaluated simulated interview sessions (\texttt{DS-INTERVIEW-SIM}), rather than human recruiter consensus.` | Replaces ambiguous "sensor stabilization" with exact statistical construct ("algorithmic variance reduction") and reinforces simulated evaluation scope. |
| **C6.1** | Section VI-A (Line 382) | `Real-world university recruitment rules exhibit sharp non-linear cutoffs (such as minimum GPA cutoffs and strict backlog limits)...` | `University recruitment policies can include threshold-based constraints (such as minimum GPA cutoffs and strict backlog limits) that are not naturally represented by a purely linear decision boundary;` | Removes overgeneralized empirical claim about all real-world recruitment rules, replacing it with domain-grounded threshold policy formulation. |
| **C6.2** | Section VII-B (Line 494) | `Real-world university recruitment rules exhibit non-linear threshold dynamics that cannot be captured by linear hyperplanes...` | `University recruitment policies can include threshold-based constraints that are not naturally represented by a purely linear decision boundary (e.g., strict backlog limits regardless of high project counts).` | Harmonizes discussion justification with Section VI-A without inventing external empirical citations. |

---

## 2. Numerical Integrity

All verified experimental numbers, dataset sizes, statistical test values, and parameter thresholds have been rigorously preserved without modification:

- [x] **No experimental numerical result changed**
  - Predictive accuracy: $95.20\% \pm 1.17\%$ (5-seed mean), $94.80\%$ (uncalibrated), $94.60\%$ (seed 42 holdout)
  - ROC-AUC: $0.9922 \pm 0.0038$
  - Expected Calibration Error (ECE): $0.0350 \pm 0.0057$ (5-seed), $0.0212$ (seed 42 calibrated), $0.0370$ (uncalibrated)
  - Brier Score Loss: $0.0339 \pm 0.0096$
  - Algorithmic recourse sparsity: $k = 2.47 \pm 0.52 \le 3.0$
  - Immutable attribute lock: $100.0\%$ invariance across all evaluated profiles
  - Recourse reachability: $93.3\%$
  - Mock interview variance reduction: $77.98\% \pm 3.99\%$ (from $79.21$ to $17.64$)
  - Conversational latency: $1.18 \pm 0.14$\,s ($1,120$\,ms)
  - Concept DAG prerequisite violations: $0.0\%$ ($0.0$ violations vs $3.6 \pm 1.0$ unconstrained)
  - RAG retrieval precision: $100.0\%$ in-domain ($\tau = 0.70$, 1,420 passages)
  - RAG OOD / adversarial rejection: $100.0\%$
  - Spatial resume parsing Entity F1: $0.8421$ vs $0.6857$ flat-regex ($\Delta\text{F1} = +0.1564$)
  - Column interleaving error rate: $78.4\% \rightarrow 4.2\%$
- [x] **No dataset size changed**
  - Prediction cohort: `DS-SYNTH-01` ($N = 2,500$; $65.2\%$ placed / $34.8\%$ unplaced; $80/10/10$ split)
  - Recourse evaluation set: $N = 30$ student profiles
  - Mock interview cohort: `DS-INTERVIEW-SIM` ($N = 50$ simulated sessions)
  - Curricular graph: 38 nodes, 45 prerequisite directed edges
  - RAG corpus: 1,420 curriculum passages
  - Multi-column resume benchmark: 50 synthetically formatted resumes
- [x] **No statistical result changed**
  - Predictive model McNemar test: $\chi^2 = 5.8824, p = 0.0153$
  - Predictive model Wilcoxon signed-rank test: $W = 27.0, p = 0.0076, r = 0.9983$
  - Multimodal variance paired Student's $t$-test: $t = 9.88, p = 0.0022, d = 2.14$
  - Topological scheduling Wilcoxon test: $W = 0.0, p = 0.0416$
  - RAG guardrail Fisher's exact test: $p = 0.02857$
- [x] **No hypothesis result changed**
  - Hypotheses H1, H2, H3, H5, H6 confirmed; H4 partially confirmed.

---

## 3. Claim Scope

- [x] **Synthetic results remain identified as synthetic**: Evaluated explicitly under `DS-SYNTH-01` ($N=2,500$) generated via Gaussian copula.
- [x] **Simulated interview results remain identified as simulated**: Framed strictly as `DS-INTERVIEW-SIM` ($N=50$) simulated audio/video/text sessions; human recruiter agreement explicitly acknowledged as prospective future work.
- [x] **No real-world validation is implied**: Section VIII (*Limitations and Threats to Validity*) explicitly quarantines longitudinal field validation (`DS-REAL-01`) as future work requiring institutional review board (IRB) ethics approval.
- [x] **RAG result is limited to evaluated queries**: Wording states "rejection of the evaluated out-of-domain queries and adversarial prompts", eliminating unverified universal robustness assertions.
- [x] **42/44 terminology is internally consistent**: "42 systems (95.5%, 42/44)" is used uniformly across Section I and Section II-B.
- [x] **Calibration claim does not imply deployment validation**: Scoped to "reducing probability calibration error under the evaluated synthetic-cohort conditions."

---

## 4. Evidence Integrity

| Manuscript Section | Claim / Correction | Supporting Phase 01–04 Evidence Source | Evidence Status |
|---|---|---|---|
| **Section I (Line 79)** | 42/44 career-readiness systems isolation chasm | `03_Research_Problem/PHASE_03_EVIDENCE_LEDGER.md` (`EVID-P03-045`), `02_Cross_Analysis/Cross_Paper_Comparison.md` | **SUPPORTED** |
| **Section I (Line 103)** | Probability calibration reduction under synthetic conditions | `04_Research_Evidence/Evidence_Ledger.md` (`EVID-P04-004`), `09_Results/EXP-01_Results.md` | **SUPPORTED** |
| **Section II-B (Line 138)** | 42/44 systems address only 1 or 2 dimensions | `03_Research_Problem/PHASE_03_EVIDENCE_LEDGER.md` (`EVID-P03-045`), `01_Research_Foundation/` (All 44 Papers) | **SUPPORTED** |
| **Section VI-A (Line 382)** | Recruitment policies include threshold-based constraints | `01_Research_Foundation/` (P01 Olipas 2024, P04 Patel & Nair 2024), `03_Research_Problem/Research_Gap_Analysis.md` | **SUPPORTED** |
| **Section VI-E (Line 482)** | RAG guardrail rejection on evaluated OOD and adversarial queries | `08_Experiments/EXP-06_RAG_Guardrail_Manifest.md`, `09_Results/EXP-06_Results.md` | **SUPPORTED** |
| **Section VII (Line 488)** | Empirical evidence supporting the central thesis | `03_Research_Problem/Research_Gap_Analysis.md`, `09_Results/Master_Results_Registry.md` | **SUPPORTED** |
| **Section VII-B (Line 494)** | Recruitment threshold-based constraints | `03_Research_Problem/Research_Gap_Analysis.md`, `05_PRIE_Architecture/` | **SUPPORTED** |
| **Section VII-D (Line 500)** | Algorithmic variance reduction across simulated sessions | `08_Experiments/EXP-02_Multimodal_Interview_Manifest.md`, `09_Results/EXP-02_Results.md` | **SUPPORTED** |

---

## 5. Final Status

**PASS**

*Summary Statement*: All six surgical corrections have been implemented with minimal diff impact. Terminology across the 44-system corpus review is 100% harmonized. Overclaiming in calibration, thesis validation, adversarial RAG filtering, interview sensor stabilization, and recruitment policies has been successfully eliminated. The LaTeX source compiles cleanly via Tectonic to exactly 9 pages in standard IEEE two-column format, and all derivative artifacts (`paper.pdf`, `paper.docx`, `paper.docx.txt`) in both `10_Publication/Conference_Paper` and `10_Publication/01_Conference_Paper` are fully synchronized.
