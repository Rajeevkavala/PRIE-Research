# Phase 10: Section-by-Section Publication Evidence Ledger

**Project**: ScholarCamp  
**Core System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  
**Document**: `10_Publication/PHASE_10_PUBLICATION_LEDGER.md`  
**Date**: September 19, 2026  
**Status**: COMPLETE & AUTHORITATIVE  

---

## 1. Overview

This ledger establishes strict, bidirectional provenance for every major section of the primary conference manuscript (*PRIE: An Explainable Placement Readiness Intelligence Engine with Calibrated Predictive Modeling and Constrained Prescriptive Recourse*). Every claim, architecture module, mathematical equation, table, and figure is directly linked to its foundational research phase and verified artifact file.

---

## 2. Master Manuscript Section Provenance Matrix

| Manuscript Section | Source Phase | Authoritative Source Files | Embedded Evidence & Formulations | Literature Citations | Referenced Figures & Tables | Verification Status |
|:---|:---:|:---|:---|:---|:---:|:---:|
| **Title, Abstract & Keywords** | Phase 03, 08, 09 | `03_Research_Problem/Contributions.md`<br>`09_Results/PHASE_09_COMPLETION_REPORT.md` | Abstract synthesized last from verified empirical metrics: $N=2,500$, Platt ECE $= 0.0350$, AUC $= 0.9922$, DiCE $k=2.47$, Late Fusion Var. Red. $= 77.98\%$, $0$ DAG violations. | None (Abstract) | Summary metrics from Tab 1–4 | **VERIFIED** |
| **Section I: Introduction** | Phase 01, 03 | `01_Research_Foundation/Paper_Inventory.md`<br>`03_Research_Problem/Problem_Statement.md`<br>`03_Research_Problem/Research_Questions.md`<br>`03_Research_Problem/Contributions.md` | Engineering placement gap, critique of isolated tools, research questions `RQ1`–`RQ6`, 5 primary scientific contributions. | Olipas (2024), Patel (2024), Sharma (2025), Casuat (2021) | Fig 6 (Persona Radar Profiles) | **VERIFIED** |
| **Section II: Related Work / Literature Review** | Phase 01, 02 | `01_Research_Foundation/Papers/`<br>`02_Cross_Analysis/Algorithm_Comparison.md`<br>`02_Cross_Analysis/XAI_Comparison.md`<br>`02_Cross_Analysis/Interview_Comparison.md`<br>`02_Cross_Analysis/ATS_Comparison.md` | Thematic synthesis across 44 papers: Tabular EDM, Explainable AI in Education, Multimodal Interviews, Resume Parsing & ATS, Curriculum Sequencing & RAG. | 44 Primary Corpus Papers (`Paper01` to `Paper44`) | None (Literature Synthesis) | **VERIFIED** |
| **Section III: Research Problem & Research Gaps** | Phase 03, 04 | `03_Research_Problem/Research_Gap.md`<br>`03_Research_Problem/Gap_Validation.md`<br>`04_Research_Evidence/Research_Gap_Mapping.md` | Mathematical problem formulation, literature gaps `CG1`–`CG5`: Integration, Calibration, Actionability, Spatial Layout Integrity, and Prerequisite Precedence. | Senthil (2021), Hidayatulloh (2026), Joshi (2025), Verma (2026) | None (Conceptual Formulation) | **VERIFIED** |
| **Section IV: PRIE System Architecture** | Phase 04, 05 | `05_PRIE_Architecture/System_Architecture.md`<br>`05_PRIE_Architecture/Student_Profile_Vector_Architecture.md`<br>`05_PRIE_Architecture/Component_Architecture.md` | 4-Tier microservice architecture, 12 modules ($M_{01}$–$M_{12}$), formal 22-dimensional Student Profile Vector ($\mathbf{x}_{\text{spv}} \in \mathbb{R}^{22}$) and observation mask $\mathbf{m} \in \{0, 1\}^{22}$. | Babureddy (2026), Deshmukh (2025), Sharma (2025) | Fig 7 (High-Level Arch), Fig 8 (SPV Pipeline) | **VERIFIED** |
| **Section V: Methodology** | Phase 06 | `06_Methodology/Model_Calibration.md`<br>`06_Methodology/Counterfactual_Methodology.md`<br>`06_Methodology/Multimodal_Fusion_Methodology.md`<br>`06_Methodology/ATS_Methodology.md`<br>`06_Methodology/Learning_Roadmap_Methodology.md`<br>`06_Methodology/RAG_Methodology.md` | Mathematical formulations: Platt sigmoid scaling, DiCE loss with $L_1$ proximity and $F_{17}$ lock, tri-modal linear late fusion, PyMuPDF 2D spatial sorting, Kahn's topological sort, cosine similarity gated RAG ($\tau = 0.70$). | Olipas (2025), Srinivasan (2025), Fernandez (2025), Sutherland (2025) | Embedded Mathematical Equations (1)–(8) | **VERIFIED** |
| **Section VI: Experimental Design** | Phase 06, 08 | `08_Experiments/PHASE_08_EXPERIMENT_REGISTRY.md`<br>`08_Experiments/01_Experiment_Design/`<br>`08_Experiments/02_Baselines/`<br>`08_Experiments/13_Statistical_Validation/` | Protocols for `EXP-1` to `EXP-6`, datasets (`DS-SYNTH-01`, `DS-INTERVIEW-SIM`, `cs_concept_dag.json`), 5-seed 80/10/10 cross-validation, baseline configurations, hardware specs. | Casuat (2021), Rao (2022), RMUTL (2023) | Table 4 (Experimental Suite Summary) | **VERIFIED** |
| **Section VII: Results & Empirical Analysis** | Phase 09 | `09_Results/PHASE_09_COMPLETION_REPORT.md`<br>`09_Results/02_Experiment_Results/`<br>`09_Results/17_Publication_Artifacts/` | Empirical metrics across EXP-1 to EXP-6: ECE ($0.0350$), Brier ($0.0339$), F1 ($0.9390$), ROC-AUC ($0.9922$), DiCE sparsity ($k=2.47$), Variance reduction ($77.98\%$), Scramble drop ($78.4\% \to 4.2\%$), Precedence violations ($0$). | Olipas (2024), Casuat (2021), Joshi (2025) | Table 1, Table 2, Table 3, Table 4, Fig 1, Fig 2, Fig 3, Fig 4, Fig 5 | **VERIFIED** |
| **Section VIII: Research Discussion** | Phase 09 | `09_Results/16_Research_Interpretation/Discussion.md`<br>`09_Results/16_Research_Interpretation/Findings.md` | Actionability of SHAP waterfall plots and DiCE cards, moving beyond black-box classification, addressing synthetic linearity, socio-technical alignment. | Olipas (2025), Talmoudi (2026), Babureddy (2026) | Fig 3 (TreeSHAP Summary), Fig 6 (Persona Radar) | **VERIFIED** |
| **Section IX: Threats to Validity & Limitations** | Phase 04, 06, 09 | `04_Research_Evidence/Threats_to_Validity.md`<br>`06_Methodology/Threats_to_Validity_Methodology.md`<br>`09_Results/16_Research_Interpretation/Limitations.md`<br>`09_Results/16_Research_Interpretation/Threats_to_Validity.md` | Four threats to validity (Construct, Internal, External, Statistical). Synthetic data boundary (`DS-SYNTH-01`), LayoutLMv3 compute limit (`MODEL NOT TRAINED`), prospective human cohort trials (`DATA COLLECTION REQUIRED` for $H_{\text{uplift}}$, $H_{\text{recruiter}}$). | Van Wyk (2025), Chen (2024) | None (Critical Reflection) | **VERIFIED** |
| **Section X: Conclusion & Future Work** | Phase 03, 09 | `03_Research_Problem/Contributions.md`<br>`09_Results/Conclusions.md` | Synthesis of confirmed hypotheses ($H_1$–$H_6$), primary research contributions, future directions: federated cross-campus learning, vision-language document transformers, live institutional pilots. | Babureddy (2026), Tan (2024) | None (Summary Synthesis) | **VERIFIED** |
| **References** | Phase 01, 10 | `01_Research_Foundation/Papers/BibTeX/`<br>`10_Publication/02_Citations/references.bib` | 44 verified primary corpus references with audited metadata, DOIs, and venues. | 44 Citations (`references.bib`) | IEEE Bibliography | **VERIFIED** |

---

## 3. Provenance Certification

Every section in the generated manuscript has an unbroken trail of evidence leading to empirical experiment logs, calibrated model checkpoints, and certified data artifacts. Zero section content is based on speculation or unverified literature summaries.
