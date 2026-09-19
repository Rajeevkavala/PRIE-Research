# PRIE-Research: Full Project Directory Tree Structure

> **Project Name:** PRIE (Placement Readiness Intelligence Engine) Research Repository  
> **Root Directory:** `d:/4-1 AD/All College Docs and ppts/Documentations/PDR/PRIE-Research`  
> **Total Directories:** 395  
> **Total Files:** 1587  
> **Root Files:** 5 (`CHANGELOG.md`, `LICENSE`, `README.md`, `ROADMAP.md`, `TODO.md`)  
> **Generated:** 2026-09-19 14:05:08  

---

## 1. High-Level Directory Overview

| Directory / Phase | Purpose & Scope | Subdirectories | Files |
| :--- | :--- | :---: | :---: |
| `.pytest_cache/` | Pytest internal test cache artifacts | 2 | 5 |
| `01_Research_Foundation/` | 48 literature papers, BibTeX records & thematic knowledge base across 10 functional domains | 16 | 165 |
| `02_Cross_Analysis/` | Systematic cross-paper syntheses, taxonomy matrices & thematic comparisons | 0 | 20 |
| `03_Research_Problem/` | Formal problem formulation, research questions (RQ1-RQ4), and hypotheses | 0 | 13 |
| `04_Research_Evidence/` | 22-feature SPV empirical justification, literature mapping & algorithm selection rationale | 0 | 15 |
| `05_PRIE_Architecture/` | End-to-end multi-tier system architecture, 22-D SPV schema & SVG vector diagrams | 7 | 147 |
| `06_Methodology/` | Empirical methodology, SMOTE balancing, TreeSHAP explainability & evaluation protocol | 0 | 56 |
| `07_Implementation/` | Machine learning source code, Colab notebook, pipelines & serialized model artifacts | 55 | 251 |
| `08_Experiments/` | Pre-registered experiment suites (EXP_01 to EXP_04), modality ablations & baselines | 64 | 114 |
| `09_Results/` | Empirical performance tables, calibration metrics, SHAP plots & recourse feasibility | 23 | 112 |
| `10_Publication/` | IEEE conference paper LaTeX & DOCX manuscripts, figures, tables, audits & presentation deck | 20 | 121 |
| `11_Review/` | Simulated peer review reports (Reviewers 1-3), IEEE compliance & plagiarism checks | 0 | 8 |
| `12_Submission/` | Target conference profiles, submission checklist, cover letter & submission package | 2 | 3 |
| `latex-bin/` | LaTeX compilation scripts and utility wrappers | 0 | 1 |
| `latex-document-skill/` | LaTeX document engineering skill definitions, templates & guidelines | 27 | 226 |
| `research-agent-skills/` | Research agent prompt templates, schemas & operational skills | 17 | 35 |
| `research-paper-lifecycle-skills/` | Scientific publication lifecycle skills, reviewer emulation & venue profiles | 144 | 287 |
| `VR_HMT_LaTeX_Source/` | Reference template LaTeX source (VR Human Motion Tracking paper) | 0 | 3 |
| **Total** | **Full Repository Scope** | **395** | **1587** |

---

## 2. Key Research Deliverables Map

- **Conference Paper Manuscript**: [`10_Publication/Conference_Paper/paper.tex`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/Conference_Paper/paper.tex) & [`paper.pdf`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/Conference_Paper/paper.pdf)
- **Publication Figures & Manifest**: [`10_Publication/03_Figures/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/03_Figures/)
- **Publication Tables & Metrics**: [`10_Publication/04_Tables/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/04_Tables/)
- **Audit & Evidence Reports**: [`10_Publication/09_Final_Audit/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/10_Publication/09_Final_Audit/)
- **Empirical Results & Curves**: [`09_Results/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/09_Results/)
- **Experimental Suites**: [`08_Experiments/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/08_Experiments/)
- **Implementation & Models**: [`07_Implementation/src/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/07_Implementation/src/)
- **Architecture Diagrams**: [`05_PRIE_Architecture/diagrams/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/diagrams/)
- **Literature Knowledge Base**: [`01_Research_Foundation/Research-Knowledge-Base/`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/01_Research_Foundation/Research-Knowledge-Base/)

---

## 3. Complete Recursive Project Tree

```text
PRIE-Research/
├── .pytest_cache/
│   ├── v/
│   │   └── cache/
│   │       ├── lastfailed
│   │       └── nodeids
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   └── README.md
├── 01_Research_Foundation/
│   ├── Papers/
│   │   ├── BibTeX/
│   │   │   ├── UnDownloaded_BibTeX/
│   │   │   │   ├── Paper02_global_edu2025connecting.bib
│   │   │   │   ├── Paper32_romero2024supervision.bib
│   │   │   │   ├── Paper33_wiharto2024datadriven.bib
│   │   │   │   └── Paper47_zhou2024explainable.bib
│   │   │   ├── Paper01_olipas2024predicting.bib
│   │   │   ├── Paper02_vanwyk2025engagement.bib
│   │   │   ├── Paper03_sharma2025preplyte.bib
│   │   │   ├── Paper04_patel2024ai.bib
│   │   │   ├── Paper05_chen2024artificial.bib
│   │   │   ├── Paper06_senthil2021employability.bib
│   │   │   ├── Paper07_ismail2021role.bib
│   │   │   ├── Paper08_alam2023factors.bib
│   │   │   ├── Paper09_casuat2021predicting.bib
│   │   │   ├── Paper10_rao2022student.bib
│   │   │   ├── Paper11_consortium2025resume.bib
│   │   │   ├── Paper12_roy2024resume.bib
│   │   │   ├── Paper13_zhang2023careergai.bib
│   │   │   ├── Paper14_deshmukh2025review.bib
│   │   │   ├── Paper15_consortium2025multimodal.bib
│   │   │   ├── Paper16_tan2024unified.bib
│   │   │   ├── Paper17_verma2026resumatch.bib
│   │   │   ├── Paper18_hidayatulloh2026explainable.bib
│   │   │   ├── Paper19_joshi2025explainai.bib
│   │   │   ├── Paper20_sutherland2025retrieval.bib
│   │   │   ├── Paper21_chawla2025rag.bib
│   │   │   ├── Paper22_olipas2025predictive.bib
│   │   │   ├── Paper23_mathew2025ai.bib
│   │   │   ├── Paper24_rmutl2023data.bib
│   │   │   ├── Paper25_cognitive2026automatic.bib
│   │   │   ├── Paper26_fernandez2025automated.bib
│   │   │   ├── Paper27_amarnath2025intelligent.bib
│   │   │   ├── Paper28_gupta2025indusai.bib
│   │   │   ├── Paper29_srinivasan2025aimock.bib
│   │   │   ├── Paper30_kulkarni2024aipowered.bib
│   │   │   ├── Paper31_banerjee2024swarm.bib
│   │   │   ├── Paper32_viberg2025predictive.bib
│   │   │   ├── Paper33_alshabandar2025explainable.bib
│   │   │   ├── Paper34_dwivedi2025explainable.bib
│   │   │   ├── Paper35_qin2020implicit.bib
│   │   │   ├── Paper36_mishra2025resume.bib
│   │   │   ├── Paper37_kaushik2025smart.bib
│   │   │   ├── Paper38_pillai2026prepwise.bib
│   │   │   ├── Paper39_kurdi2020systematic.bib
│   │   │   ├── Paper40_schmidt2025utilizing.bib
│   │   │   ├── Paper41_consortium2026triangular.bib
│   │   │   ├── Paper42_davenport2025intelligent.bib
│   │   │   ├── Paper43_knowledge2026transforming.bib
│   │   │   └── Paper44_consortium2024artificial.bib
│   │   ├── PDFs/
│   │   │   ├── Paper01_olipas2024predicting.pdf
│   │   │   ├── Paper02_vanwyk2025engagement.pdf
│   │   │   ├── Paper03_sharma2025preplyte.pdf
│   │   │   ├── Paper04_patel2024ai.pdf
│   │   │   ├── Paper05_chen2024artificial.pdf
│   │   │   ├── Paper06_senthil2021employability.pdf
│   │   │   ├── Paper07_ismail2021role.pdf
│   │   │   ├── Paper08_alam2023factors.pdf
│   │   │   ├── Paper09_casuat2021predicting.pdf
│   │   │   ├── Paper10_rao2022student.pdf
│   │   │   ├── Paper11_consortium2025resume.pdf
│   │   │   ├── Paper12_roy2024resume.pdf
│   │   │   ├── Paper13_zhang2023careergai.pdf
│   │   │   ├── Paper14_deshmukh2025review.pdf
│   │   │   ├── Paper15_consortium2025multimodal.pdf
│   │   │   ├── Paper16_tan2024unified.pdf
│   │   │   ├── Paper17_verma2026resumatch.pdf
│   │   │   ├── Paper18_hidayatulloh2026explainable.pdf
│   │   │   ├── Paper19_joshi2025explainai.pdf
│   │   │   ├── Paper20_sutherland2025retrieval.pdf
│   │   │   ├── Paper21_chawla2025rag.pdf
│   │   │   ├── Paper22_olipas2025predictive.pdf
│   │   │   ├── Paper23_mathew2025ai.pdf
│   │   │   ├── Paper24_rmutl2023data.pdf
│   │   │   ├── Paper25_cognitive2026automatic.pdf
│   │   │   ├── Paper26_fernandez2025automated.pdf
│   │   │   ├── Paper27_amarnath2025intelligent.pdf
│   │   │   ├── Paper28_gupta2025indusai.pdf
│   │   │   ├── Paper29_srinivasan2025aimock.pdf
│   │   │   ├── Paper30_kulkarni2024aipowered.pdf
│   │   │   ├── Paper31_banerjee2024swarm.pdf
│   │   │   ├── Paper32_viberg2025predictive.pdf
│   │   │   ├── Paper33_alshabandar2025explainable.pdf
│   │   │   ├── Paper34_dwivedi2025explainable.pdf
│   │   │   ├── Paper35_qin2020implicit.pdf
│   │   │   ├── Paper36_mishra2025resume.pdf
│   │   │   ├── Paper37_kaushik2025smart.pdf
│   │   │   ├── Paper38_pillai2026prepwise.pdf
│   │   │   ├── Paper39_kurdi2020systematic.pdf
│   │   │   ├── Paper40_schmidt2025utilizing.pdf
│   │   │   ├── Paper41_consortium2026triangular.pdf
│   │   │   ├── Paper42_davenport2025intelligent.pdf
│   │   │   ├── Paper43_knowledge2026transforming.pdf
│   │   │   └── Paper44_consortium2024artificial.pdf
│   │   ├── Downloaded_Papers_Catalog.md
│   │   ├── References.bib
│   │   └── Remaining_Papers_Download_Links.md
│   ├── Research-Knowledge-Base/
│   │   ├── 01_Employability/
│   │   │   ├── Paper01_Career_Readiness_ML_DL_XAI_2024.md
│   │   │   ├── Paper04_Placement_Success_SkillGaps_2024.md
│   │   │   ├── Paper06_Employability_Prediction_Survey_2021.md
│   │   │   ├── Paper07_Social_Support_Self_Efficacy_TVET_2021.md
│   │   │   ├── Paper09_Predicting_Employability_ML_2021.md
│   │   │   ├── Paper22_Employability_RandomForest_SHAP_Olipas_2026.md
│   │   │   └── Paper24_Graduate_Employability_RMUTL_2026.md
│   │   ├── 02_Prediction/
│   │   │   ├── Paper08_Academic_Performance_Factors_2023.md
│   │   │   ├── Paper10_Student_Performance_Benchmark_2022.md
│   │   │   ├── Paper31_Feature_Dimensionality_Reduction_Review_Jia_2022.md
│   │   │   ├── Paper33_Early_Intervention_At_Risk_AlShabandar_2019.md
│   │   │   └── README.md
│   │   ├── 03_XAI/
│   │   │   ├── Paper18_Explainable_Performance_Hidayatulloh_2026.md
│   │   │   ├── Paper19_ExplainAI_Khan_2026.md
│   │   │   ├── Paper32_XAI_Higher_Education_Bibliometric_Talmoudi_2026.md
│   │   │   └── Paper34_Explainable_AI_Student_Performance_Babu_2025.md
│   │   ├── 04_ATS/
│   │   │   ├── Paper11_Job_Scraping_Mishra_2025.md
│   │   │   ├── Paper12_Resume_Parser_Kashif_2024.md
│   │   │   ├── Paper17_ResuMatch_Solanki_2026.md
│   │   │   ├── Paper36_Resume_Parsing_Job_Recommendation_Suryawanshi_2025.md
│   │   │   ├── Paper37_Smart_AI_Resume_Analyzer_JayaPriya_2025.md
│   │   │   └── Paper42_Intelligent_Document_Processing_Automation_Kapula_2025.md
│   │   ├── 05_Mock_Interview/
│   │   │   ├── Paper03_Preplyte_Placement_Prep_2025.md
│   │   │   ├── Paper14_Mock_Interview_Koli_2025.md
│   │   │   ├── Paper15_Multimodal_Mock_Interview_Inamdar_2025.md
│   │   │   ├── Paper27_AI_FollowUp_Questions_Interviews_Zhang_2025.md
│   │   │   ├── Paper28_Smart_AI_Interviewer_Resume_Analyzer_Vachkal_2025.md
│   │   │   ├── Paper29_Voice_Driven_Mock_Interview_Wahid_2026.md
│   │   │   ├── Paper30_AI_Mock_Interview_Verma_2025.md
│   │   │   └── Paper38_PrepWise_GenAI_Interview_Platform_Kulkarni_2026.md
│   │   ├── 06_RAG/
│   │   │   ├── Paper20_RAG_Chatbots_Swacha_2025.md
│   │   │   ├── Paper21_RAG_Chatbot_Nisanth_2025.md
│   │   │   ├── Paper23_RAG_Chatbot_Venkatesh_2025.md
│   │   │   └── Paper40_RAG_Chatbot_Higher_Education_Murti_2025.md
│   │   ├── 07_Recommendation/
│   │   │   ├── Paper13_CareergAIde_Ashrafi_2023.md
│   │   │   ├── Paper16_Learning_Pathway_Zheng_2024.md
│   │   │   ├── Paper35_Implicit_Skills_Job_Recommendation_Gugnani_2020.md
│   │   │   ├── Paper43_Smart_OPAC_Knowledge_Graph_Discovery_Rajeevan_2026.md
│   │   │   └── README.md
│   │   ├── 08_Learning_Analytics/
│   │   │   ├── Paper02_AI_Learning_Analytics_HE_2025.md
│   │   │   ├── Paper05_AI_Education_Bibliometric_2024.md
│   │   │   ├── Paper44_AI_Learning_Analytics_TFT_RL_Azeez_2026.md
│   │   │   └── README.md
│   │   ├── 09_Question_Generation/
│   │   │   ├── Paper25_AQG_Causal_Graph_Wang_2025.md
│   │   │   ├── Paper26_LLM_MCQ_Generation_Review_Wiharto_2025.md
│   │   │   ├── Paper39_AQG_Educational_Systematic_Review_Kurdi_2020.md
│   │   │   └── README.md
│   │   ├── 10_Digital_Twin/
│   │   │   ├── Paper41_Triangular_Digital_Twin_Employability_Babureddy_2026.md
│   │   │   └── README.md
│   │   ├── _Previous_AI_Summaries/
│   │   │   ├── Paper01_Graduate_Employability_RMUTL_2023.md
│   │   │   ├── Paper02_XAI_Academic_Performance_2026.md
│   │   │   ├── Paper03_Resume_Parser_NLP_2025.md
│   │   │   ├── Paper04_Multimodal_Mock_Interview_2025.md
│   │   │   └── Paper05_Causal_Graph_AQG_2026.md
│   │   ├── algorithms.md
│   │   ├── comparison-table.md
│   │   ├── datasets.md
│   │   ├── evaluation-metrics.md
│   │   ├── future-ideas.md
│   │   ├── methodologies.md
│   │   ├── novelty.md
│   │   ├── README.md
│   │   └── research-gap.md
│   ├── Paper_Corpus_Reconciliation.md
│   ├── Paper_Inventory.md
│   ├── PHASE_01_REBUILD_REPORT.md
│   ├── Previous_KB_Audit.md
│   ├── Reference_Validation.md
│   ├── scratch_pdf_headers.txt
│   └── Source_Quality_Assessment.md
├── 02_Cross_Analysis/
│   ├── AI_Model_Comparison.md
│   ├── Algorithm_Comparison.md
│   ├── Architecture_Comparison.md
│   ├── ATS_Comparison.md
│   ├── Cross_Paper_Comparison.md
│   ├── Dataset_Comparison.md
│   ├── Evaluation_Metrics_Comparison.md
│   ├── Feature_Comparison.md
│   ├── Future_Work_Matrix.md
│   ├── Interview_Comparison.md
│   ├── Learning_Analytics_Comparison.md
│   ├── Limitation_Matrix.md
│   ├── PHASE_02_ANALYSIS_PLAN.md
│   ├── PHASE_02_COMPLETION_REPORT.md
│   ├── PHASE_02_EVIDENCE_LEDGER.md
│   ├── PHASE_02_IMPLEMENTATION_PLAN.md
│   ├── RAG_Comparison.md
│   ├── Recommendation_Comparison.md
│   ├── Technology_Stack.md
│   └── XAI_Comparison.md
├── 03_Research_Problem/
│   ├── Assumptions.md
│   ├── Contributions.md
│   ├── Gap_Validation.md
│   ├── Hypotheses.md
│   ├── Limitations.md
│   ├── PHASE_03_COMPLETION_REPORT.md
│   ├── PHASE_03_EVIDENCE_LEDGER.md
│   ├── PHASE_03_IMPLEMENTATION_PLAN.md
│   ├── Problem_Statement.md
│   ├── Research_Gap.md
│   ├── Research_Objectives.md
│   ├── Research_Questions.md
│   └── Scope.md
├── 04_Research_Evidence/
│   ├── Algorithm_Justification.md
│   ├── Dataset_Justification.md
│   ├── Design_Decisions.md
│   ├── Evaluation_Justification.md
│   ├── Experimental_Decisions.md
│   ├── Feature_Source_Mapping.md
│   ├── Feature_Traceability.md
│   ├── Literature_to_PRIE.md
│   ├── Model_Selection_Justification.md
│   ├── Module_Traceability.md
│   ├── PHASE_04_COMPLETION_REPORT.md
│   ├── PHASE_04_EVIDENCE_LEDGER.md
│   ├── PHASE_04_IMPLEMENTATION_PLAN.md
│   ├── Research_Gap_Mapping.md
│   └── Threats_to_Validity.md
├── 05_PRIE_Architecture/
│   ├── diagrams/
│   │   ├── drawio/
│   │   │   ├── Agent_Orchestration.drawio
│   │   │   ├── ATS_Pipeline.drawio
│   │   │   ├── Component_Diagram.drawio
│   │   │   ├── Data_Architecture_Diagram.drawio
│   │   │   ├── Data_Flow_Diagram.drawio
│   │   │   ├── High_Level_Architecture.drawio
│   │   │   ├── Interview_Pipeline.drawio
│   │   │   ├── Learning_Feedback_Loop.drawio
│   │   │   ├── Model_Serving_Diagram.drawio
│   │   │   ├── Prediction_Pipeline.drawio
│   │   │   ├── PRIE_Pipeline.drawio
│   │   │   ├── Recommendation_Pipeline.drawio
│   │   │   ├── SPV_Pipeline.drawio
│   │   │   └── System_Context_Diagram.drawio
│   │   ├── excalidraw/
│   │   │   ├── Agent_Orchestration.excalidraw
│   │   │   ├── Agent_Orchestration.excalidraw.json
│   │   │   ├── ATS_Pipeline.excalidraw
│   │   │   ├── ATS_Pipeline.excalidraw.json
│   │   │   ├── Component_Diagram.excalidraw
│   │   │   ├── Component_Diagram.excalidraw.json
│   │   │   ├── Data_Architecture_Diagram.excalidraw
│   │   │   ├── Data_Architecture_Diagram.excalidraw.json
│   │   │   ├── Data_Flow_Diagram.excalidraw
│   │   │   ├── Data_Flow_Diagram.excalidraw.json
│   │   │   ├── High_Level_Architecture.excalidraw
│   │   │   ├── High_Level_Architecture.excalidraw.json
│   │   │   ├── Interview_Pipeline.excalidraw
│   │   │   ├── Interview_Pipeline.excalidraw.json
│   │   │   ├── Learning_Feedback_Loop.excalidraw
│   │   │   ├── Learning_Feedback_Loop.excalidraw.json
│   │   │   ├── Model_Serving_Diagram.excalidraw
│   │   │   ├── Model_Serving_Diagram.excalidraw.json
│   │   │   ├── Prediction_Pipeline.excalidraw
│   │   │   ├── Prediction_Pipeline.excalidraw.json
│   │   │   ├── PRIE_Pipeline.excalidraw
│   │   │   ├── PRIE_Pipeline.excalidraw.json
│   │   │   ├── Recommendation_Pipeline.excalidraw
│   │   │   ├── Recommendation_Pipeline.excalidraw.json
│   │   │   ├── SPV_Pipeline.excalidraw
│   │   │   ├── SPV_Pipeline.excalidraw.json
│   │   │   ├── System_Context_Diagram.excalidraw
│   │   │   └── System_Context_Diagram.excalidraw.json
│   │   ├── mermaid/
│   │   │   ├── Agent_Orchestration.mmd
│   │   │   ├── ATS_Pipeline.mmd
│   │   │   ├── Component_Diagram.mmd
│   │   │   ├── Data_Architecture_Diagram.mmd
│   │   │   ├── Data_Flow_Diagram.mmd
│   │   │   ├── High_Level_Architecture.mmd
│   │   │   ├── Interview_Pipeline.mmd
│   │   │   ├── Learning_Feedback_Loop.mmd
│   │   │   ├── Model_Serving_Diagram.mmd
│   │   │   ├── Prediction_Pipeline.mmd
│   │   │   ├── PRIE_Pipeline.mmd
│   │   │   ├── Recommendation_Pipeline.mmd
│   │   │   ├── SPV_Pipeline.mmd
│   │   │   └── System_Context_Diagram.mmd
│   │   ├── pdf/
│   │   │   ├── Agent_Orchestration.pdf
│   │   │   ├── ATS_Pipeline.pdf
│   │   │   ├── Component_Diagram.pdf
│   │   │   ├── Data_Architecture_Diagram.pdf
│   │   │   ├── Data_Flow_Diagram.pdf
│   │   │   ├── High_Level_Architecture.pdf
│   │   │   ├── Interview_Pipeline.pdf
│   │   │   ├── Learning_Feedback_Loop.pdf
│   │   │   ├── Model_Serving_Diagram.pdf
│   │   │   ├── Prediction_Pipeline.pdf
│   │   │   ├── PRIE_Pipeline.pdf
│   │   │   ├── Recommendation_Pipeline.pdf
│   │   │   ├── SPV_Pipeline.pdf
│   │   │   └── System_Context_Diagram.pdf
│   │   ├── png/
│   │   │   ├── Agent_Orchestration.png
│   │   │   ├── ATS_Pipeline.png
│   │   │   ├── Component_Diagram.png
│   │   │   ├── Data_Architecture_Diagram.png
│   │   │   ├── Data_Flow_Diagram.png
│   │   │   ├── High_Level_Architecture.png
│   │   │   ├── Interview_Pipeline.png
│   │   │   ├── Learning_Feedback_Loop.png
│   │   │   ├── Model_Serving_Diagram.png
│   │   │   ├── Prediction_Pipeline.png
│   │   │   ├── PRIE_Pipeline.png
│   │   │   ├── Recommendation_Pipeline.png
│   │   │   ├── SPV_Pipeline.png
│   │   │   └── System_Context_Diagram.png
│   │   ├── svg/
│   │   │   ├── Agent_Orchestration.svg
│   │   │   ├── ATS_Pipeline.svg
│   │   │   ├── Component_Diagram.svg
│   │   │   ├── Data_Architecture_Diagram.svg
│   │   │   ├── Data_Flow_Diagram.svg
│   │   │   ├── High_Level_Architecture.svg
│   │   │   ├── Interview_Pipeline.svg
│   │   │   ├── Learning_Feedback_Loop.svg
│   │   │   ├── Model_Serving_Diagram.svg
│   │   │   ├── Prediction_Pipeline.svg
│   │   │   ├── prie_architecture.svg
│   │   │   ├── PRIE_Pipeline.svg
│   │   │   ├── Recommendation_Pipeline.svg
│   │   │   ├── SPV_Pipeline.svg
│   │   │   └── System_Context_Diagram.svg
│   │   ├── Agent_Orchestration.md
│   │   ├── ATS_Pipeline.md
│   │   ├── Component_Diagram.md
│   │   ├── Data_Architecture_Diagram.md
│   │   ├── Data_Flow_Diagram.md
│   │   ├── High_Level_Architecture.md
│   │   ├── Interview_Pipeline.md
│   │   ├── Learning_Feedback_Loop.md
│   │   ├── Model_Serving_Diagram.md
│   │   ├── Prediction_Pipeline.md
│   │   ├── PRIE_Pipeline.md
│   │   ├── README.md
│   │   ├── Recommendation_Pipeline.md
│   │   ├── SPV_Pipeline.md
│   │   └── System_Context_Diagram.md
│   ├── API_Architecture.md
│   ├── Architecture_Assumptions.md
│   ├── Architecture_Constraints.md
│   ├── Architecture_Decision_Records.md
│   ├── Architecture_Traceability.md
│   ├── Architecture_Validation_Plan.md
│   ├── ATS_Architecture.md
│   ├── Component_Architecture.md
│   ├── Data_Architecture.md
│   ├── Data_Flow_Architecture.md
│   ├── Digital_Twin_Architecture.md
│   ├── Failure_Recovery_Architecture.md
│   ├── Learning_Analytics_Architecture.md
│   ├── Learning_Roadmap_Architecture.md
│   ├── Mock_Interview_Architecture.md
│   ├── Model_Serving_Architecture.md
│   ├── Module_Architecture.md
│   ├── Multi_Agent_Orchestration.md
│   ├── PHASE_05_ARCHITECTURE_LEDGER.md
│   ├── PHASE_05_COMPLETION_REPORT.md
│   ├── PHASE_05_IMPLEMENTATION_PLAN.md
│   ├── Prediction_Engine_Architecture.md
│   ├── PRIE_Architecture_Overview.md
│   ├── Question_Generation_Architecture.md
│   ├── RAG_Architecture.md
│   ├── README.md
│   ├── Recommendation_Engine_Architecture.md
│   ├── Scalability_Architecture.md
│   ├── Security_Privacy_Architecture.md
│   ├── Student_Profile_Vector_Architecture.md
│   ├── System_Architecture.md
│   ├── Technology_Stack_Architecture.md
│   └── XAI_Architecture.md
├── 06_Methodology/
│   ├── Ablation_Study_Methodology.md
│   ├── Algorithm_Methodology.md
│   ├── ATS_Methodology.md
│   ├── Audio_Processing_Methodology.md
│   ├── Baseline_Methodology.md
│   ├── Bias_and_Fairness_Methodology.md
│   ├── Counterfactual_Methodology.md
│   ├── Data_Collection.md
│   ├── Data_Governance.md
│   ├── Dataset_Design.md
│   ├── Dataset_Splitting.md
│   ├── Digital_Twin_Methodology.md
│   ├── Error_Analysis_Methodology.md
│   ├── Ethical_Methodology.md
│   ├── Evaluation_Methodology.md
│   ├── Experiment_Configuration.md
│   ├── Experimental_Framework.md
│   ├── Feature_Engineering.md
│   ├── Feature_Selection.md
│   ├── Hyperparameter_Tuning.md
│   ├── Hypothesis_Testing_Plan.md
│   ├── Interview_Methodology.md
│   ├── Learning_Analytics_Methodology.md
│   ├── Learning_Roadmap_Methodology.md
│   ├── Methodology_Overview.md
│   ├── Methodology_to_Architecture.md
│   ├── Methodology_Traceability.md
│   ├── Model_Calibration.md
│   ├── Model_Selection.md
│   ├── Model_Validation.md
│   ├── Multi_Agent_Methodology.md
│   ├── Multimodal_Fusion_Methodology.md
│   ├── PHASE_06_COMPLETION_REPORT.md
│   ├── PHASE_06_IMPLEMENTATION_PLAN.md
│   ├── PHASE_06_METHODOLOGY_LEDGER.md
│   ├── Prediction_Methodology.md
│   ├── Preprocessing.md
│   ├── Question_Generation_Methodology.md
│   ├── RAG_Methodology.md
│   ├── Randomness_and_Seeds.md
│   ├── README.md
│   ├── Real_Data_Methodology.md
│   ├── Recommendation_Methodology.md
│   ├── Reproducibility.md
│   ├── Research_Design.md
│   ├── Research_Workflow.md
│   ├── Resume_Processing_Methodology.md
│   ├── RQ_to_Experiment_Mapping.md
│   ├── SMOTE.md
│   ├── Statistical_Analysis.md
│   ├── Student_Profile_Vector_Methodology.md
│   ├── Synthetic_Data_Methodology.md
│   ├── Threats_to_Validity_Methodology.md
│   ├── Training_Methodology.md
│   ├── Video_Processing_Methodology.md
│   └── XAI_Methodology.md
├── 07_Implementation/
│   ├── checkpoints/
│   ├── configs/
│   │   └── config.json
│   ├── figures/
│   │   ├── fig1_calibration_reliability.png
│   │   ├── fig2_roc_pr_curves.png
│   │   ├── fig3_shap_importance.png
│   │   ├── fig4_multimodal_ablation.png
│   │   ├── fig5_concept_dag_progression.png
│   │   ├── fig6_persona_radar_profiles.png
│   │   ├── table1_model_performance.tex
│   │   ├── table2_modality_ablation.tex
│   │   └── table3_recourse_feasibility.tex
│   ├── logs/
│   ├── models/
│   │   ├── .gitkeep
│   │   ├── feature_names.json
│   │   ├── jd_embeddings.npy
│   │   ├── jd_metadata.json
│   │   ├── scaler.pkl
│   │   └── xgb_model.pkl
│   ├── notebooks/
│   │   ├── generate_paper_figures.py
│   │   ├── research_model_manifest.json
│   │   ├── ScholarCamp_PRIE_Google_Colab.ipynb
│   │   └── ScholarCamp_PRIE_Research_From_Scratch.ipynb
│   ├── outputs/
│   ├── PRIE_v1/
│   │   ├── .pytest_cache/
│   │   │   ├── v/
│   │   │   │   └── cache/
│   │   │   │       ├── lastfailed
│   │   │   │       └── nodeids
│   │   │   ├── .gitignore
│   │   │   ├── CACHEDIR.TAG
│   │   │   └── README.md
│   │   ├── __pycache__/
│   │   │   └── generate_research_notebook.cpython-310.pyc
│   │   ├── backend/
│   │   │   ├── __pycache__/
│   │   │   │   ├── config.cpython-310.pyc
│   │   │   │   ├── main.cpython-310.pyc
│   │   │   │   └── spv_version.cpython-310.pyc
│   │   │   ├── api/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── v1_aqg.cpython-310.pyc
│   │   │   │   │   ├── v1_assessment.cpython-310.pyc
│   │   │   │   │   ├── v1_auth.cpython-310.pyc
│   │   │   │   │   ├── v1_company.cpython-310.pyc
│   │   │   │   │   ├── v1_experiments.cpython-310.pyc
│   │   │   │   │   ├── v1_explain.cpython-310.pyc
│   │   │   │   │   ├── v1_interview.cpython-310.pyc
│   │   │   │   │   ├── v1_predict.cpython-310.pyc
│   │   │   │   │   ├── v1_profile.cpython-310.pyc
│   │   │   │   │   ├── v1_rag.cpython-310.pyc
│   │   │   │   │   ├── v1_resume.cpython-310.pyc
│   │   │   │   │   ├── v1_roadmap.cpython-310.pyc
│   │   │   │   │   └── v1_twin.cpython-310.pyc
│   │   │   │   ├── v1_aqg.py
│   │   │   │   ├── v1_assessment.py
│   │   │   │   ├── v1_auth.py
│   │   │   │   ├── v1_company.py
│   │   │   │   ├── v1_experiments.py
│   │   │   │   ├── v1_explain.py
│   │   │   │   ├── v1_interview.py
│   │   │   │   ├── v1_predict.py
│   │   │   │   ├── v1_profile.py
│   │   │   │   ├── v1_rag.py
│   │   │   │   ├── v1_resume.py
│   │   │   │   ├── v1_roadmap.py
│   │   │   │   └── v1_twin.py
│   │   │   ├── database/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── db_manager.cpython-310.pyc
│   │   │   │   │   └── queries.cpython-310.pyc
│   │   │   │   ├── db_manager.py
│   │   │   │   ├── queries.py
│   │   │   │   ├── schema.sql
│   │   │   │   └── seed_data.py
│   │   │   ├── ml/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── baselines.cpython-310.pyc
│   │   │   │   │   ├── calibration.cpython-310.pyc
│   │   │   │   │   ├── generate_synthetic.cpython-310.pyc
│   │   │   │   │   └── train_xgb.cpython-310.pyc
│   │   │   │   ├── baselines.py
│   │   │   │   ├── calibration.py
│   │   │   │   ├── feature_schema.py
│   │   │   │   ├── generate_synthetic.py
│   │   │   │   └── train_xgb.py
│   │   │   ├── modules/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── m01_spv_aggregator.cpython-310.pyc
│   │   │   │   │   ├── m02_resume_ats.cpython-310.pyc
│   │   │   │   │   ├── m03_adaptive_assessment.cpython-310.pyc
│   │   │   │   │   ├── m04_skill_gap_engine.cpython-310.pyc
│   │   │   │   │   ├── m05_mock_interview.cpython-310.pyc
│   │   │   │   │   ├── m06_placement_predictor.cpython-310.pyc
│   │   │   │   │   ├── m07_prescriptive_xai.cpython-310.pyc
│   │   │   │   │   ├── m08_roadmap_generator.cpython-310.pyc
│   │   │   │   │   ├── m09_rag_assistant.cpython-310.pyc
│   │   │   │   │   ├── m10_aqg.cpython-310.pyc
│   │   │   │   │   ├── m11_behavioral_telemetry.cpython-310.pyc
│   │   │   │   │   ├── m11_company_matcher.cpython-310.pyc
│   │   │   │   │   └── m12_digital_twin.cpython-310.pyc
│   │   │   │   ├── m01_spv_aggregator.py
│   │   │   │   ├── m02_resume_ats.py
│   │   │   │   ├── m03_adaptive_assessment.py
│   │   │   │   ├── m04_skill_gap_engine.py
│   │   │   │   ├── m05_mock_interview.py
│   │   │   │   ├── m06_placement_predictor.py
│   │   │   │   ├── m07_prescriptive_xai.py
│   │   │   │   ├── m08_roadmap_generator.py
│   │   │   │   ├── m09_rag_assistant.py
│   │   │   │   ├── m10_aqg.py
│   │   │   │   ├── m11_behavioral_telemetry.py
│   │   │   │   ├── m11_company_matcher.py
│   │   │   │   └── m12_digital_twin.py
│   │   │   ├── tests/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   ├── test_ats.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_database.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_e2e_api.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_interview.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_modules.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_predictor.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_rag_aqg.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_spv_schema.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_spv_validation.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   ├── test_twin_company.cpython-310-pytest-9.0.3.pyc
│   │   │   │   │   └── test_xai.cpython-310-pytest-9.0.3.pyc
│   │   │   │   ├── test_ats.py
│   │   │   │   ├── test_database.py
│   │   │   │   ├── test_e2e_api.py
│   │   │   │   ├── test_interview.py
│   │   │   │   ├── test_modules.py
│   │   │   │   ├── test_predictor.py
│   │   │   │   ├── test_rag_aqg.py
│   │   │   │   ├── test_spv_schema.py
│   │   │   │   ├── test_spv_validation.py
│   │   │   │   ├── test_twin_company.py
│   │   │   │   └── test_xai.py
│   │   │   ├── config.py
│   │   │   ├── main.py
│   │   │   └── spv_version.py
│   │   ├── data/
│   │   │   ├── cs_concept_dag.json
│   │   │   ├── ds_synth_01.csv
│   │   │   ├── prie_v1.db
│   │   │   ├── question_bank.json
│   │   │   └── resource_library.json
│   │   ├── docs/
│   │   │   ├── IMPLEMENTATION_GAP_ANALYSIS.md
│   │   │   └── PHASE_07_IMPLEMENTATION_PLAN.md
│   │   ├── experiments/
│   │   │   ├── __pycache__/
│   │   │   │   ├── exporters.cpython-310.pyc
│   │   │   │   └── run_experiment.cpython-310.pyc
│   │   │   ├── metrics/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── evaluators.cpython-310.pyc
│   │   │   │   └── evaluators.py
│   │   │   ├── results/
│   │   │   │   ├── EXP-1/
│   │   │   │   │   ├── paper_table.tex
│   │   │   │   │   ├── raw_metrics.json
│   │   │   │   │   ├── run_metadata.json
│   │   │   │   │   ├── statistical_tests.json
│   │   │   │   │   └── summary.csv
│   │   │   │   ├── EXP-2/
│   │   │   │   │   ├── paper_table.tex
│   │   │   │   │   ├── raw_metrics.json
│   │   │   │   │   ├── run_metadata.json
│   │   │   │   │   └── summary.csv
│   │   │   │   ├── EXP-3/
│   │   │   │   │   ├── paper_table.tex
│   │   │   │   │   ├── raw_metrics.json
│   │   │   │   │   ├── run_metadata.json
│   │   │   │   │   └── summary.csv
│   │   │   │   ├── EXP-4/
│   │   │   │   │   ├── paper_table.tex
│   │   │   │   │   ├── raw_metrics.json
│   │   │   │   │   ├── run_metadata.json
│   │   │   │   │   └── summary.csv
│   │   │   │   ├── EXP-5/
│   │   │   │   │   ├── paper_table.tex
│   │   │   │   │   ├── raw_metrics.json
│   │   │   │   │   ├── run_metadata.json
│   │   │   │   │   └── summary.csv
│   │   │   │   └── EXP-6/
│   │   │   │       ├── paper_table.tex
│   │   │   │       ├── raw_metrics.json
│   │   │   │       ├── run_metadata.json
│   │   │   │       └── summary.csv
│   │   │   ├── statistical/
│   │   │   │   ├── __pycache__/
│   │   │   │   │   └── hypothesis_tests.cpython-310.pyc
│   │   │   │   └── hypothesis_tests.py
│   │   │   ├── exporters.py
│   │   │   └── run_experiment.py
│   │   ├── frontend/
│   │   │   ├── css/
│   │   │   │   └── styles.css
│   │   │   ├── js/
│   │   │   │   ├── api_client.js
│   │   │   │   └── auth.js
│   │   │   ├── pages/
│   │   │   │   ├── admin.html
│   │   │   │   ├── assessment.html
│   │   │   │   ├── ats.html
│   │   │   │   ├── dashboard.html
│   │   │   │   ├── experiments.html
│   │   │   │   ├── interview.html
│   │   │   │   ├── login.html
│   │   │   │   ├── profile.html
│   │   │   │   ├── register.html
│   │   │   │   ├── roadmap.html
│   │   │   │   ├── twin_company.html
│   │   │   │   └── xai.html
│   │   │   └── index.html
│   │   ├── logs/
│   │   ├── models/
│   │   │   ├── feature_names_v1.json
│   │   │   ├── model_manifest.json
│   │   │   ├── scaler_v1.pkl
│   │   │   └── xgb_model_v1.pkl
│   │   ├── notebooks/
│   │   │   └── ScholarCamp_PRIE_Research_From_Scratch.ipynb
│   │   ├── uploads/
│   │   │   └── resumes/
│   │   ├── build_notebook.py
│   │   ├── generate_research_notebook.py
│   │   ├── IMPLEMENTATION_MANIFEST.json
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── src/
│   │   ├── database/
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── db_init.cpython-310.pyc
│   │   │   │   ├── db_manager.cpython-310.pyc
│   │   │   │   └── queries.cpython-310.pyc
│   │   │   ├── __init__.py
│   │   │   ├── db_init.py
│   │   │   ├── db_manager.py
│   │   │   ├── indexes.sql
│   │   │   ├── queries.py
│   │   │   └── schema.sql
│   │   ├── modules/
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── assessment_engine.cpython-310.pyc
│   │   │   │   ├── behavior_analyzer.cpython-310.pyc
│   │   │   │   ├── company_predictor.cpython-310.pyc
│   │   │   │   ├── explainability.cpython-310.pyc
│   │   │   │   ├── mock_interview.cpython-310.pyc
│   │   │   │   ├── placement_predictor.cpython-310.pyc
│   │   │   │   ├── prie_orchestrator.cpython-310.pyc
│   │   │   │   ├── recommendation_engine.cpython-310.pyc
│   │   │   │   ├── resume_intelligence.cpython-310.pyc
│   │   │   │   ├── roadmap_generator.cpython-310.pyc
│   │   │   │   ├── skill_gap_engine.cpython-310.pyc
│   │   │   │   ├── student_profiling.cpython-310.pyc
│   │   │   │   └── sus_evaluator.cpython-310.pyc
│   │   │   ├── __init__.py
│   │   │   ├── assessment_engine.py
│   │   │   ├── behavior_analyzer.py
│   │   │   ├── company_predictor.py
│   │   │   ├── explainability.py
│   │   │   ├── mock_interview.py
│   │   │   ├── placement_predictor.py
│   │   │   ├── prie_orchestrator.py
│   │   │   ├── recommendation_engine.py
│   │   │   ├── resume_intelligence.py
│   │   │   ├── roadmap_generator.py
│   │   │   ├── skill_gap_engine.py
│   │   │   ├── student_profiling.py
│   │   │   └── sus_evaluator.py
│   │   ├── utils/
│   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── auth.cpython-310.pyc
│   │   │   │   ├── text_processing.cpython-310.pyc
│   │   │   │   ├── validators.cpython-310.pyc
│   │   │   │   └── visualization.cpython-310.pyc
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── text_processing.py
│   │   │   ├── validators.py
│   │   │   └── visualization.py
│   │   ├── app.py
│   │   └── config.py
│   ├── API_REFERENCE.md
│   ├── DATA_CONTRACTS.md
│   ├── EXPERIMENT_RUNBOOK.md
│   ├── IMPLEMENTATION_ARCHITECTURE.md
│   ├── IMPLEMENTATION_DECISIONS.md
│   ├── IMPLEMENTATION_STATUS.md
│   ├── IMPLEMENTATION_TRACEABILITY.md
│   ├── MODEL_ARTIFACTS.md
│   ├── PHASE_07_CODEBASE_RESEARCH_READINESS_AUDIT.md
│   ├── PHASE_07_IMPLEMENTATION_COMPLETION_REPORT.md
│   ├── README.md
│   ├── REPRODUCIBILITY.md
│   ├── requirements.txt
│   └── SECURITY.md
├── 08_Experiments/
│   ├── 01_Experiment_Design/
│   │   ├── Experimental_Protocols.md
│   │   ├── Hypothesis_Experiment_Matrix.md
│   │   ├── Leakage_Prevention_Protocol.md
│   │   ├── Research_Question_Experiment_Matrix.md
│   │   └── Train_Validation_Test_Protocol.md
│   ├── 02_Baselines/
│   │   ├── Baseline_Fairness_Audit.md
│   │   ├── Baseline_Specifications.md
│   │   └── README.md
│   ├── 03_Benchmark/
│   │   ├── DS_BENCH_01_Protocol.md
│   │   ├── DS_BENCH_02_Protocol.md
│   │   └── README.md
│   ├── 04_EXP_01_Prediction/
│   │   ├── Metrics_Report.md
│   │   ├── Protocol.md
│   │   ├── Run_Manifest.json
│   │   └── Statistical_Tests.md
│   ├── 05_EXP_02_Recourse/
│   │   ├── Feasibility_Report.md
│   │   ├── Invariance_Audit.md
│   │   ├── Protocol.md
│   │   └── Run_Manifest.json
│   ├── 06_EXP_03_Multimodal/
│   │   ├── Fusion_Analysis.md
│   │   ├── Modality_Ablation_Report.md
│   │   ├── Protocol.md
│   │   └── Run_Manifest.json
│   ├── 07_EXP_04_ATS/
│   │   ├── Error_Analysis.md
│   │   ├── Parsing_Comparison.md
│   │   ├── Protocol.md
│   │   └── Run_Manifest.json
│   ├── 08_EXP_05_Roadmap/
│   │   ├── DAG_Scheduling_Report.md
│   │   ├── Precedence_Verification.md
│   │   ├── Protocol.md
│   │   └── Run_Manifest.json
│   ├── 09_EXP_06_RAG_AQG/
│   │   ├── Guardrail_Evaluation.md
│   │   ├── Protocol.md
│   │   ├── Retrieval_Precision.md
│   │   └── Run_Manifest.json
│   ├── 10_Ablation_Study/
│   │   ├── Component_Contribution_Ledger.md
│   │   ├── README.md
│   │   └── Systematic_Ablation_Matrix.md
│   ├── 11_Robustness/
│   │   ├── Perturbation_Stress_Test.md
│   │   ├── README.md
│   │   └── Seed_Sensitivity.md
│   ├── 12_Generalization/
│   │   ├── Domain_Shift_Analysis.md
│   │   ├── Epistemological_Limits.md
│   │   └── README.md
│   ├── 13_Statistical_Validation/
│   │   ├── Assumption_Checks.md
│   │   ├── Effect_Size_Analysis.md
│   │   ├── Hypothesis_Test_Results.md
│   │   └── README.md
│   ├── 14_Reproducibility/
│   │   ├── Environment_Manifest.json
│   │   ├── Hardware_Software_Audit.md
│   │   ├── README.md
│   │   └── Seed_Manifest.md
│   ├── 15_Experiment_Results/
│   │   ├── EXP-1/
│   │   │   ├── figures/
│   │   │   │   ├── fig1_calibration_reliability.png
│   │   │   │   ├── fig2_roc_pr_curves.png
│   │   │   │   ├── fig3_shap_importance.png
│   │   │   │   └── fig6_persona_radar_profiles.png
│   │   │   ├── metrics/
│   │   │   │   ├── raw_metrics.json
│   │   │   │   └── summary.csv
│   │   │   ├── processed/
│   │   │   │   └── summary.csv
│   │   │   ├── raw/
│   │   │   │   └── raw_metrics.json
│   │   │   ├── run_manifests/
│   │   │   │   └── run_metadata.json
│   │   │   ├── statistics/
│   │   │   │   └── statistical_tests.json
│   │   │   └── tables/
│   │   │       └── paper_table.tex
│   │   ├── EXP-2/
│   │   │   ├── figures/
│   │   │   │   └── fig4_multimodal_ablation.png
│   │   │   ├── metrics/
│   │   │   │   ├── raw_metrics.json
│   │   │   │   └── summary.csv
│   │   │   ├── processed/
│   │   │   │   └── summary.csv
│   │   │   ├── raw/
│   │   │   │   └── raw_metrics.json
│   │   │   ├── run_manifests/
│   │   │   │   └── run_metadata.json
│   │   │   ├── statistics/
│   │   │   └── tables/
│   │   │       └── paper_table.tex
│   │   ├── EXP-3/
│   │   │   ├── figures/
│   │   │   ├── metrics/
│   │   │   │   ├── raw_metrics.json
│   │   │   │   └── summary.csv
│   │   │   ├── processed/
│   │   │   │   └── summary.csv
│   │   │   ├── raw/
│   │   │   │   └── raw_metrics.json
│   │   │   ├── run_manifests/
│   │   │   │   └── run_metadata.json
│   │   │   ├── statistics/
│   │   │   └── tables/
│   │   │       └── paper_table.tex
│   │   ├── EXP-4/
│   │   │   ├── figures/
│   │   │   ├── metrics/
│   │   │   │   ├── raw_metrics.json
│   │   │   │   └── summary.csv
│   │   │   ├── processed/
│   │   │   │   └── summary.csv
│   │   │   ├── raw/
│   │   │   │   └── raw_metrics.json
│   │   │   ├── run_manifests/
│   │   │   │   └── run_metadata.json
│   │   │   ├── statistics/
│   │   │   └── tables/
│   │   │       └── paper_table.tex
│   │   ├── EXP-5/
│   │   │   ├── figures/
│   │   │   │   └── fig5_concept_dag_progression.png
│   │   │   ├── metrics/
│   │   │   │   ├── raw_metrics.json
│   │   │   │   └── summary.csv
│   │   │   ├── processed/
│   │   │   │   └── summary.csv
│   │   │   ├── raw/
│   │   │   │   └── raw_metrics.json
│   │   │   ├── run_manifests/
│   │   │   │   └── run_metadata.json
│   │   │   ├── statistics/
│   │   │   └── tables/
│   │   │       └── paper_table.tex
│   │   ├── EXP-6/
│   │   │   ├── figures/
│   │   │   ├── metrics/
│   │   │   │   ├── raw_metrics.json
│   │   │   │   └── summary.csv
│   │   │   ├── processed/
│   │   │   │   └── summary.csv
│   │   │   ├── raw/
│   │   │   │   └── raw_metrics.json
│   │   │   ├── run_manifests/
│   │   │   │   └── run_metadata.json
│   │   │   ├── statistics/
│   │   │   └── tables/
│   │   │       └── paper_table.tex
│   │   └── multi_seed_aggregate.json
│   ├── 16_Research_Evidence/
│   │   ├── Claim_Evidence_Matrix.md
│   │   ├── Research_vs_Engineering_Ledger.md
│   │   └── Unsupported_Claims.md
│   ├── Ablation_Study.md
│   ├── Baselines.md
│   ├── Benchmark.md
│   ├── Experiment_Design.md
│   ├── Generalization.md
│   ├── PHASE_08_COMPLETION_REPORT.md
│   ├── PHASE_08_EVIDENCE_LEDGER.md
│   ├── PHASE_08_EXPERIMENT_PLAN.md
│   ├── PHASE_08_EXPERIMENT_REGISTRY.md
│   ├── PHASE_08_READING_AUDIT.md
│   ├── PHASE_08_REPRODUCIBILITY_MANIFEST.md
│   ├── README.md
│   ├── Reproducibility.md
│   ├── Robustness.md
│   └── Statistical_Validation.md
├── 09_Results/
│   ├── 02_Experiment_Results/
│   │   ├── EXP-1_Prediction.md
│   │   ├── EXP-2_Recourse.md
│   │   ├── EXP-3_Multimodal.md
│   │   ├── EXP-4_ATS.md
│   │   ├── EXP-5_Roadmap.md
│   │   └── EXP-6_RAG_AQG.md
│   ├── 03_Model_Performance/
│   │   ├── Accuracy.md
│   │   ├── Benchmark_Comparison.md
│   │   ├── Brier_Score.md
│   │   ├── Calibration.md
│   │   ├── ECE.md
│   │   ├── PR_AUC.md
│   │   ├── Precision_Recall_F1.md
│   │   └── ROC_AUC.md
│   ├── 04_XAI_Results/
│   │   ├── Counterfactual_Recourse.md
│   │   ├── Feature_Importance.md
│   │   └── SHAP.md
│   ├── 05_Multimodal_Results/
│   │   ├── Diagnostic_Variance.md
│   │   ├── Fusion_Analysis.md
│   │   └── Multimodal_Ablation.md
│   ├── 06_ATS_Results/
│   │   ├── ATS_Parsing_Comparison.md
│   │   ├── Error_Analysis.md
│   │   └── Spatial_Layout_Evaluation.md
│   ├── 07_Roadmap_Results/
│   │   ├── Prerequisite_Satisfaction.md
│   │   └── Topological_Scheduling.md
│   ├── 08_RAG_AQG_Results/
│   │   ├── Curriculum_Retrieval_Precision.md
│   │   └── Guardrail_Hallucination_Rejection.md
│   ├── 09_Ablation_Results/
│   │   ├── Component_Contributions.md
│   │   └── Systematic_Ablation_Analysis.md
│   ├── 10_Robustness_Results/
│   │   ├── Perturbation_Stress_Test.md
│   │   └── Seed_Sensitivity.md
│   ├── 11_Generalization_Results/
│   │   ├── Cross_Dataset_Analysis.md
│   │   └── Domain_Shift_Epistemological_Limits.md
│   ├── 12_Statistical_Results/
│   │   ├── Distributional_Assumption_Audits.md
│   │   ├── Effect_Sizes_and_Confidence_Intervals.md
│   │   └── Hypothesis_Testing_Ledger.md
│   ├── 13_Error_Analysis/
│   │   ├── ATS_Boundary_Errors.md
│   │   ├── Multimodal_Sensor_Noise.md
│   │   ├── Prediction_Failures.md
│   │   └── Taxonomy_of_System_Failures.md
│   ├── 14_Research_Questions/
│   │   ├── RQ1_Answer.md
│   │   ├── RQ2_Answer.md
│   │   ├── RQ3_Answer.md
│   │   ├── RQ4_Answer.md
│   │   ├── RQ5_Answer.md
│   │   ├── RQ6_Answer.md
│   │   └── RQ_Synthesis.md
│   ├── 15_Hypotheses/
│   │   ├── H1_Assessment.md
│   │   ├── H2_Assessment.md
│   │   ├── H3_Assessment.md
│   │   ├── H4_Assessment.md
│   │   ├── H5_Assessment.md
│   │   ├── H6_Assessment.md
│   │   └── Hypothesis_Synthesis.md
│   ├── 16_Research_Interpretation/
│   │   ├── Contributions_Evidence.md
│   │   ├── Discussion.md
│   │   ├── Findings.md
│   │   ├── Limitations.md
│   │   ├── Practical_Implications.md
│   │   ├── Theoretical_Implications.md
│   │   └── Threats_to_Validity.md
│   ├── 17_Publication_Artifacts/
│   │   ├── figures/
│   │   │   ├── fig1_calibration_reliability.png
│   │   │   ├── fig2_roc_pr_curves.png
│   │   │   ├── fig3_shap_importance.png
│   │   │   ├── fig4_multimodal_ablation.png
│   │   │   ├── fig5_concept_dag_progression.png
│   │   │   ├── fig6_persona_radar_profiles.png
│   │   │   └── figures_manifest.md
│   │   ├── latex/
│   │   │   ├── table1_model_performance.tex
│   │   │   ├── table2_modality_ablation.tex
│   │   │   ├── table3_recourse_feasibility.tex
│   │   │   └── table4_experimental_summary.tex
│   │   └── tables/
│   │       ├── ablation_table.md
│   │       ├── experimental_summary_table.md
│   │       ├── modality_ablation.csv
│   │       ├── model_performance.csv
│   │       ├── model_performance_table.md
│   │       ├── recourse_feasibility.csv
│   │       └── recourse_table.md
│   ├── 18_Traceability/
│   │   ├── Claim_Result_Matrix.md
│   │   ├── Hypothesis_Experiment_Matrix.md
│   │   ├── Result_Artifact_Provenance.md
│   │   └── RQ_Experiment_Result_Matrix.md
│   ├── charts/
│   ├── figures/
│   │   ├── fig1_calibration_reliability.png
│   │   ├── fig2_roc_pr_curves.png
│   │   ├── fig3_shap_importance.png
│   │   ├── fig4_multimodal_ablation.png
│   │   ├── fig5_concept_dag_progression.png
│   │   ├── fig6_persona_radar_profiles.png
│   │   └── figures_manifest.md
│   ├── tables/
│   │   ├── ablation_table.md
│   │   ├── experimental_summary_table.md
│   │   ├── modality_ablation.csv
│   │   ├── model_performance.csv
│   │   ├── model_performance_table.md
│   │   ├── recourse_feasibility.csv
│   │   └── recourse_table.md
│   ├── Accuracy.md
│   ├── Benchmark_Comparison.md
│   ├── Conclusions.md
│   ├── Discussion.md
│   ├── Error_Analysis.md
│   ├── Feature_Importance.md
│   ├── PHASE_09_CLAIM_LEDGER.md
│   ├── PHASE_09_COMPLETION_REPORT.md
│   ├── PHASE_09_EVIDENCE_LEDGER.md
│   ├── PHASE_09_READING_AUDIT.md
│   ├── PHASE_09_RESULT_REGISTRY.md
│   ├── Precision_Recall.md
│   ├── README.md
│   ├── ROC.md
│   └── SHAP.md
├── 10_Publication/
│   ├── 01_Conference_Paper/
│   │   ├── figures/
│   │   │   ├── Component_Diagram.png
│   │   │   ├── fig1_calibration_reliability.png
│   │   │   ├── fig2_roc_pr_curves.png
│   │   │   ├── fig3_shap_importance.png
│   │   │   ├── fig4_multimodal_ablation.png
│   │   │   ├── fig5_concept_dag_progression.png
│   │   │   ├── fig6_persona_radar_profiles.png
│   │   │   ├── figures_manifest.md
│   │   │   ├── High_Level_Architecture.png
│   │   │   ├── PRIE_Pipeline.png
│   │   │   └── SPV_Pipeline.png
│   │   ├── tables/
│   │   │   ├── ablation_table.md
│   │   │   ├── experimental_summary_table.md
│   │   │   ├── modality_ablation.csv
│   │   │   ├── model_performance.csv
│   │   │   ├── model_performance_table.md
│   │   │   ├── recourse_feasibility.csv
│   │   │   ├── recourse_table.md
│   │   │   ├── table1_model_performance.tex
│   │   │   ├── table2_modality_ablation.tex
│   │   │   ├── table3_recourse_feasibility.tex
│   │   │   └── table4_experimental_summary.tex
│   │   ├── template/
│   │   ├── generate_paper_docx.py
│   │   ├── IEEEtran.cls
│   │   ├── paper.docx
│   │   ├── paper.pdf
│   │   ├── paper.tex
│   │   ├── paper_manuscript.md
│   │   └── references.bib
│   ├── 02_Citations/
│   │   ├── BibTeX_Audit.md
│   │   ├── Citation_to_Claim_Matrix.md
│   │   └── references.bib
│   ├── 03_Figures/
│   │   ├── Component_Diagram.png
│   │   ├── fig1_calibration_reliability.png
│   │   ├── fig2_roc_pr_curves.png
│   │   ├── fig3_shap_importance.png
│   │   ├── fig4_multimodal_ablation.png
│   │   ├── fig5_concept_dag_progression.png
│   │   ├── fig6_persona_radar_profiles.png
│   │   ├── Figure_Inventory.md
│   │   ├── figures_manifest.md
│   │   ├── High_Level_Architecture.png
│   │   ├── PRIE_Pipeline.png
│   │   └── SPV_Pipeline.png
│   ├── 04_Tables/
│   │   ├── ablation_table.md
│   │   ├── experimental_summary_table.md
│   │   ├── modality_ablation.csv
│   │   ├── model_performance.csv
│   │   ├── model_performance_table.md
│   │   ├── recourse_feasibility.csv
│   │   ├── recourse_table.md
│   │   ├── table1_model_performance.tex
│   │   ├── table2_modality_ablation.tex
│   │   ├── table3_recourse_feasibility.tex
│   │   ├── table4_experimental_summary.tex
│   │   └── Table_Inventory.md
│   ├── 05_Conference_Submission/
│   │   ├── Author_Metadata.md
│   │   ├── Page_Limit_Check.md
│   │   └── Submission_Checklist.md
│   ├── 06_Demo/
│   │   ├── Demo_Checklist.md
│   │   ├── Demo_Flow.md
│   │   ├── Demo_Scenario.md
│   │   └── Demo_Script.md
│   ├── 07_Poster/
│   │   ├── Poster_Checklist.md
│   │   ├── Poster_Content.md
│   │   └── Poster_Layout.md
│   ├── 08_Presentation/
│   │   ├── Presentation_Checklist.md
│   │   ├── Presentation_Outline.md
│   │   ├── Slide_Content.md
│   │   └── Speaker_Notes.md
│   ├── 09_Final_Audit/
│   │   ├── Claim_Evidence_Audit.md
│   │   ├── Numerical_Consistency_Audit.md
│   │   ├── Reproducibility_Audit.md
│   │   └── Research_Integrity_Audit.md
│   ├── Conference_Paper/
│   │   ├── figures/
│   │   │   ├── Component_Diagram.png
│   │   │   ├── fig1_calibration_reliability.png
│   │   │   ├── fig2_roc_pr_curves.png
│   │   │   ├── fig3_shap_importance.png
│   │   │   ├── fig4_multimodal_ablation.png
│   │   │   ├── fig5_concept_dag_progression.png
│   │   │   ├── fig6_persona_radar_profiles.png
│   │   │   ├── figures_manifest.md
│   │   │   ├── High_Level_Architecture.png
│   │   │   ├── PRIE_Pipeline.png
│   │   │   └── SPV_Pipeline.png
│   │   ├── previews/
│   │   │   ├── page_1.png
│   │   │   ├── page_2.png
│   │   │   ├── page_3.png
│   │   │   ├── page_4.png
│   │   │   ├── page_5.png
│   │   │   └── page_6.png
│   │   ├── tables/
│   │   │   ├── ablation_table.md
│   │   │   ├── experimental_summary_table.md
│   │   │   ├── modality_ablation.csv
│   │   │   ├── model_performance.csv
│   │   │   ├── model_performance_table.md
│   │   │   ├── recourse_feasibility.csv
│   │   │   ├── recourse_table.md
│   │   │   ├── table1_model_performance.tex
│   │   │   ├── table2_modality_ablation.tex
│   │   │   ├── table3_recourse_feasibility.tex
│   │   │   └── table4_experimental_summary.tex
│   │   ├── template/
│   │   │   └── Vr-Hmt_Human_Motion_Tracking_Paper.docx
│   │   ├── generate_conference_paper_artifacts.py
│   │   ├── IEEEtran.cls
│   │   ├── paper.docx
│   │   ├── paper.docx.txt
│   │   ├── paper.pdf
│   │   ├── paper.tex
│   │   └── references.bib
│   ├── Demo/
│   │   └── Demo_Script.md
│   ├── Poster/
│   │   └── Poster_Layout.md
│   ├── Presentation/
│   │   └── Presentation_Outline.md
│   ├── PHASE_10_CITATION_AUDIT.md
│   ├── PHASE_10_CLAIM_AUDIT.md
│   ├── PHASE_10_COMPLETION_REPORT.md
│   ├── PHASE_10_FIGURE_TABLE_AUDIT.md
│   ├── PHASE_10_PUBLICATION_LEDGER.md
│   ├── PHASE_10_PUBLICATION_PLAN.md
│   ├── PHASE_10_READING_AUDIT.md
│   └── README.md
├── 11_Review/
│   ├── Citation_Audit.md
│   ├── Grammar_Check.md
│   ├── IEEE_Checklist.md
│   ├── Plagiarism_Report.md
│   ├── Reviewer1.md
│   ├── Reviewer2.md
│   ├── Reviewer3.md
│   └── Submission_Checklist.md
├── 12_Submission/
│   ├── Camera_Ready/
│   ├── Final_PDF/
│   ├── Conference_List.md
│   ├── Cover_Letter.md
│   └── Submission_History.md
├── latex-bin/
│   └── tectonic.exe
├── latex-document-skill/
│   ├── .git/
│   │   ├── hooks/
│   │   │   ├── applypatch-msg.sample
│   │   │   ├── commit-msg.sample
│   │   │   ├── fsmonitor-watchman.sample
│   │   │   ├── post-update.sample
│   │   │   ├── pre-applypatch.sample
│   │   │   ├── pre-commit.sample
│   │   │   ├── pre-merge-commit.sample
│   │   │   ├── pre-push.sample
│   │   │   ├── pre-rebase.sample
│   │   │   ├── pre-receive.sample
│   │   │   ├── prepare-commit-msg.sample
│   │   │   ├── push-to-checkout.sample
│   │   │   ├── sendemail-validate.sample
│   │   │   └── update.sample
│   │   ├── info/
│   │   │   └── exclude
│   │   ├── logs/
│   │   │   ├── refs/
│   │   │   │   ├── heads/
│   │   │   │   │   └── main
│   │   │   │   └── remotes/
│   │   │   │       └── origin/
│   │   │   │           └── HEAD
│   │   │   └── HEAD
│   │   ├── objects/
│   │   │   ├── info/
│   │   │   └── pack/
│   │   │       ├── pack-7ae69d3c01e64736a08aafc48315a06db3d3b836.idx
│   │   │       ├── pack-7ae69d3c01e64736a08aafc48315a06db3d3b836.pack
│   │   │       └── pack-7ae69d3c01e64736a08aafc48315a06db3d3b836.rev
│   │   ├── refs/
│   │   │   ├── heads/
│   │   │   │   └── main
│   │   │   ├── remotes/
│   │   │   │   └── origin/
│   │   │   │       └── HEAD
│   │   │   └── tags/
│   │   ├── config
│   │   ├── description
│   │   ├── FETCH_HEAD
│   │   ├── HEAD
│   │   ├── index
│   │   └── packed-refs
│   ├── .github/
│   │   └── workflows/
│   │       └── collect-traffic.yml
│   ├── assets/
│   │   ├── templates/
│   │   │   ├── academic-cv.tex
│   │   │   ├── academic-paper.tex
│   │   │   ├── book.tex
│   │   │   ├── cheatsheet-code.tex
│   │   │   ├── cheatsheet-exam.tex
│   │   │   ├── cheatsheet.tex
│   │   │   ├── conditional-document.tex
│   │   │   ├── cover-letter.tex
│   │   │   ├── exam.tex
│   │   │   ├── fillable-form.tex
│   │   │   ├── homework.tex
│   │   │   ├── invoice.tex
│   │   │   ├── lab-report.tex
│   │   │   ├── lecture-notes.tex
│   │   │   ├── letter.tex
│   │   │   ├── mail-merge-letter.tex
│   │   │   ├── poster-landscape.tex
│   │   │   ├── poster.tex
│   │   │   ├── presentation.tex
│   │   │   ├── references.bib
│   │   │   ├── report.tex
│   │   │   ├── resume-classic-ats.tex
│   │   │   ├── resume-entry-level.tex
│   │   │   ├── resume-executive.tex
│   │   │   ├── resume-modern-professional.tex
│   │   │   ├── resume-technical.tex
│   │   │   ├── resume.tex
│   │   │   └── thesis.tex
│   │   ├── capy-printer.png
│   │   ├── capy-professor.png
│   │   ├── capy-wizard.png
│   │   ├── happycapy-capy.png
│   │   ├── happycapy-logo.png
│   │   └── happycapy-logo.svg
│   ├── examples/
│   │   ├── academic-cv-p1.png
│   │   ├── academic-cv-p2.png
│   │   ├── academic-cv-p3.png
│   │   ├── academic-cv-p4.png
│   │   ├── academic-cv.png
│   │   ├── academic-paper-p1.png
│   │   ├── academic-paper-p2.png
│   │   ├── academic-paper-p3.png
│   │   ├── academic-paper-p4.png
│   │   ├── academic-paper.png
│   │   ├── book-p1.png
│   │   ├── book-p10.png
│   │   ├── book-p2.png
│   │   ├── book-p3.png
│   │   ├── book-p4.png
│   │   ├── book-p5.png
│   │   ├── book-p6.png
│   │   ├── book-p7.png
│   │   ├── book-p8.png
│   │   ├── book-p9.png
│   │   ├── book.png
│   │   ├── charts.png
│   │   ├── cheatsheet-p1.png
│   │   ├── cheatsheet-p2.png
│   │   ├── cover-letter.png
│   │   ├── exam-p1.png
│   │   ├── exam-p2.png
│   │   ├── exam-p3.png
│   │   ├── exam-p4.png
│   │   ├── exam-p5.png
│   │   ├── exam-p6.png
│   │   ├── exam.png
│   │   ├── ieee-twocolumn-p1.png
│   │   ├── ieee-twocolumn-p2.png
│   │   ├── ieee-twocolumn.png
│   │   ├── invoice.png
│   │   ├── lecture-notes-p1.png
│   │   ├── lecture-notes-p2.png
│   │   ├── lecture-notes-p3.png
│   │   ├── lecture-notes-p4.png
│   │   ├── lecture-notes-p5.png
│   │   ├── lecture-notes-p6.png
│   │   ├── lecture-notes-p7.png
│   │   ├── lecture-notes-p8.png
│   │   ├── lecture-notes.png
│   │   ├── letter.png
│   │   ├── poster-landscape.png
│   │   ├── poster.png
│   │   ├── presentation-p1.png
│   │   ├── presentation-p10.png
│   │   ├── presentation-p2.png
│   │   ├── presentation-p3.png
│   │   ├── presentation-p4.png
│   │   ├── presentation-p5.png
│   │   ├── presentation-p6.png
│   │   ├── presentation-p7.png
│   │   ├── presentation-p8.png
│   │   ├── presentation-p9.png
│   │   ├── presentation.png
│   │   ├── report-p1.png
│   │   ├── report-p2.png
│   │   ├── report-p3.png
│   │   ├── report-p4.png
│   │   ├── report.png
│   │   ├── resume-classic-ats.png
│   │   ├── resume-entry-level.png
│   │   ├── resume-executive-p1.png
│   │   ├── resume-executive-p2.png
│   │   ├── resume-executive.png
│   │   ├── resume-modern-professional.png
│   │   ├── resume-technical.png
│   │   ├── resume.png
│   │   ├── thesis-p1.png
│   │   ├── thesis-p2.png
│   │   ├── thesis-p3.png
│   │   ├── thesis-p4.png
│   │   ├── thesis-p5.png
│   │   ├── thesis-p6.png
│   │   ├── thesis-p7.png
│   │   ├── thesis-p8.png
│   │   └── thesis.png
│   ├── references/
│   │   ├── profiles/
│   │   │   ├── business-document.md
│   │   │   ├── general-notes.md
│   │   │   ├── legal-document.md
│   │   │   └── math-notes.md
│   │   ├── accessibility-guide.md
│   │   ├── advanced-features.md
│   │   ├── beamer-guide.md
│   │   ├── bibliography-guide.md
│   │   ├── charts-and-graphs.md
│   │   ├── cheatsheet-guide.md
│   │   ├── code-patterns.md
│   │   ├── collaboration-guide.md
│   │   ├── debugging-guide.md
│   │   ├── font-guide.md
│   │   ├── format-conversion.md
│   │   ├── graphviz-plantuml.md
│   │   ├── ieee-journal-twocolumn-guide.md
│   │   ├── interactive-features.md
│   │   ├── long-form-best-practices.md
│   │   ├── mermaid-diagrams.md
│   │   ├── packages.md
│   │   ├── pdf-conversion.md
│   │   ├── pdf-extraction-prompts.md
│   │   ├── pdf-operations.md
│   │   ├── poster-design-guide.md
│   │   ├── python-charts.md
│   │   ├── qa-test-report.md
│   │   ├── resume-ats-guide.md
│   │   ├── script-tools.md
│   │   ├── tables-and-images.md
│   │   └── visual-packages.md
│   ├── scripts/
│   │   ├── compile_latex.sh
│   │   ├── convert_document.sh
│   │   ├── csv_to_latex.py
│   │   ├── fetch_bibtex.sh
│   │   ├── generate_chart.py
│   │   ├── graphviz_to_pdf.sh
│   │   ├── install_deps.sh
│   │   ├── latex_analyze.sh
│   │   ├── latex_citation_extract.sh
│   │   ├── latex_diff.sh
│   │   ├── latex_lint.sh
│   │   ├── latex_package_check.sh
│   │   ├── latex_wordcount.sh
│   │   ├── mail_merge.py
│   │   ├── mermaid_to_image.sh
│   │   ├── pdf_check_form.py
│   │   ├── pdf_encrypt.sh
│   │   ├── pdf_extract_fields.py
│   │   ├── pdf_extract_pages.sh
│   │   ├── pdf_fill_annotations.py
│   │   ├── pdf_fill_form.py
│   │   ├── pdf_merge.sh
│   │   ├── pdf_optimize.sh
│   │   ├── pdf_to_images.sh
│   │   ├── pdf_validate_boxes.py
│   │   ├── plantuml_to_pdf.sh
│   │   └── validate_latex.py
│   ├── stats/
│   │   ├── clone-stats.csv
│   │   └── views.csv
│   ├── tests/
│   │   ├── fixtures/
│   │   │   ├── references.bib
│   │   │   ├── simple_diagram.puml
│   │   │   ├── simple_graph.dot
│   │   │   ├── simple_mermaid.mmd
│   │   │   ├── test_document.tex
│   │   │   ├── test_packages.tex
│   │   │   ├── test_v1.tex
│   │   │   └── test_v2.tex
│   │   ├── README.md
│   │   ├── run_all_tests.sh
│   │   ├── test_analysis_tools.sh
│   │   ├── test_compile_latex.sh
│   │   ├── test_pdf_forms.py
│   │   ├── test_pdf_utils.sh
│   │   ├── test_python_scripts.py
│   │   └── test_templates.sh
│   ├── .chktexrc
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.sh
│   └── SKILL.md
├── research-agent-skills/
│   ├── .git/
│   │   ├── hooks/
│   │   │   ├── applypatch-msg.sample
│   │   │   ├── commit-msg.sample
│   │   │   ├── fsmonitor-watchman.sample
│   │   │   ├── post-update.sample
│   │   │   ├── pre-applypatch.sample
│   │   │   ├── pre-commit.sample
│   │   │   ├── pre-merge-commit.sample
│   │   │   ├── pre-push.sample
│   │   │   ├── pre-rebase.sample
│   │   │   ├── pre-receive.sample
│   │   │   ├── prepare-commit-msg.sample
│   │   │   ├── push-to-checkout.sample
│   │   │   ├── sendemail-validate.sample
│   │   │   └── update.sample
│   │   ├── info/
│   │   │   └── exclude
│   │   ├── logs/
│   │   │   ├── refs/
│   │   │   │   ├── heads/
│   │   │   │   │   └── main
│   │   │   │   └── remotes/
│   │   │   │       └── origin/
│   │   │   │           └── HEAD
│   │   │   └── HEAD
│   │   ├── objects/
│   │   │   ├── info/
│   │   │   └── pack/
│   │   │       ├── pack-84efca640575735247cf64bf496f40c58e7b47f0.idx
│   │   │       ├── pack-84efca640575735247cf64bf496f40c58e7b47f0.pack
│   │   │       └── pack-84efca640575735247cf64bf496f40c58e7b47f0.rev
│   │   ├── refs/
│   │   │   ├── heads/
│   │   │   │   └── main
│   │   │   ├── remotes/
│   │   │   │   └── origin/
│   │   │   │       └── HEAD
│   │   │   └── tags/
│   │   ├── config
│   │   ├── description
│   │   ├── FETCH_HEAD
│   │   ├── HEAD
│   │   ├── index
│   │   └── packed-refs
│   ├── research-paper-review/
│   │   ├── package.json
│   │   ├── README.md
│   │   └── SKILL.md
│   ├── .gitignore
│   ├── LICENSE
│   └── README.md
├── research-paper-lifecycle-skills/
│   ├── .claude-plugin/
│   │   └── marketplace.json
│   ├── .git/
│   │   ├── hooks/
│   │   │   ├── applypatch-msg.sample
│   │   │   ├── commit-msg.sample
│   │   │   ├── fsmonitor-watchman.sample
│   │   │   ├── post-update.sample
│   │   │   ├── pre-applypatch.sample
│   │   │   ├── pre-commit.sample
│   │   │   ├── pre-merge-commit.sample
│   │   │   ├── pre-push.sample
│   │   │   ├── pre-rebase.sample
│   │   │   ├── pre-receive.sample
│   │   │   ├── prepare-commit-msg.sample
│   │   │   ├── push-to-checkout.sample
│   │   │   ├── sendemail-validate.sample
│   │   │   └── update.sample
│   │   ├── info/
│   │   │   └── exclude
│   │   ├── logs/
│   │   │   ├── refs/
│   │   │   │   ├── heads/
│   │   │   │   │   └── main
│   │   │   │   └── remotes/
│   │   │   │       └── origin/
│   │   │   │           └── HEAD
│   │   │   └── HEAD
│   │   ├── objects/
│   │   │   ├── info/
│   │   │   └── pack/
│   │   │       ├── pack-481840bc23c9a6d76ce0609aaf5c1a4702766cc1.idx
│   │   │       ├── pack-481840bc23c9a6d76ce0609aaf5c1a4702766cc1.pack
│   │   │       └── pack-481840bc23c9a6d76ce0609aaf5c1a4702766cc1.rev
│   │   ├── refs/
│   │   │   ├── heads/
│   │   │   │   └── main
│   │   │   ├── remotes/
│   │   │   │   └── origin/
│   │   │   │       └── HEAD
│   │   │   └── tags/
│   │   ├── config
│   │   ├── description
│   │   ├── FETCH_HEAD
│   │   ├── HEAD
│   │   ├── index
│   │   └── packed-refs
│   ├── .github/
│   │   ├── ISSUE_TEMPLATE/
│   │   │   ├── bug_report.yml
│   │   │   ├── config.yml
│   │   │   ├── documentation.yml
│   │   │   └── skill_request.yml
│   │   ├── workflows/
│   │   │   └── validate-skills.yml
│   │   └── pull_request_template.md
│   ├── assets/
│   │   ├── community-conduct.svg
│   │   ├── community-contributing.svg
│   │   ├── community-security.svg
│   │   ├── community-templates.svg
│   │   ├── hero.svg
│   │   └── lifecycle.svg
│   ├── docs/
│   │   ├── assets/
│   │   │   ├── favicon.svg
│   │   │   ├── hero.svg
│   │   │   ├── lifecycle.svg
│   │   │   ├── social-preview.png
│   │   │   └── social-preview.svg
│   │   ├── ai-research-tools.html
│   │   ├── index.html
│   │   ├── llms-full.txt
│   │   ├── llms.txt
│   │   ├── robots.txt
│   │   └── sitemap.xml
│   ├── skills/
│   │   ├── add-venue-profile/
│   │   │   ├── references/
│   │   │   │   ├── pr-checklist.md
│   │   │   │   └── profile-walkthrough.md
│   │   │   ├── scripts/
│   │   │   │   ├── fetch_cfp.py
│   │   │   │   ├── init_profile.py
│   │   │   │   └── validate_profile.py
│   │   │   └── SKILL.md
│   │   ├── anonymize-paper/
│   │   │   ├── references/
│   │   │   │   ├── camera-ready-reversal.md
│   │   │   │   └── leak-catalog.md
│   │   │   ├── scripts/
│   │   │   │   └── scan_anonymization.py
│   │   │   └── SKILL.md
│   │   ├── assess-paper/
│   │   │   └── SKILL.md
│   │   ├── benchmark-paper/
│   │   │   ├── references/
│   │   │   │   └── scoring-rubric.md
│   │   │   ├── scripts/
│   │   │   │   └── scorecard.py
│   │   │   └── SKILL.md
│   │   ├── check-originality/
│   │   │   ├── references/
│   │   │   │   └── detection-methods.md
│   │   │   ├── scripts/
│   │   │   │   └── overlap_check.py
│   │   │   └── SKILL.md
│   │   ├── draft-related-work/
│   │   │   ├── references/
│   │   │   │   ├── clustering-and-deltas.md
│   │   │   │   └── placement-conventions.md
│   │   │   ├── scripts/
│   │   │   │   ├── audit_bib.py
│   │   │   │   ├── check_coverage.py
│   │   │   │   ├── gather_candidates.py
│   │   │   │   └── polite_http.py
│   │   │   └── SKILL.md
│   │   ├── draft-survey/
│   │   │   ├── references/
│   │   │   │   └── ranking-criteria.md
│   │   │   ├── scripts/
│   │   │   │   └── rank_papers.py
│   │   │   └── SKILL.md
│   │   ├── fetch-paper/
│   │   │   ├── references/
│   │   │   │   ├── copyright-and-politeness.md
│   │   │   │   └── oa-sources.md
│   │   │   ├── scripts/
│   │   │   │   └── resolve_oa.py
│   │   │   └── SKILL.md
│   │   ├── find-papers/
│   │   │   ├── references/
│   │   │   │   ├── api-notes.md
│   │   │   │   ├── citation-graph-expansion.md
│   │   │   │   └── venue-aliases.md
│   │   │   ├── scripts/
│   │   │   │   ├── arxiv_search.py
│   │   │   │   ├── citation_graph.py
│   │   │   │   ├── crossref_search.py
│   │   │   │   ├── dblp_search.py
│   │   │   │   ├── polite_http.py
│   │   │   │   ├── resolve_canonical.py
│   │   │   │   ├── resolve_papers.py
│   │   │   │   └── s2_search.py
│   │   │   └── SKILL.md
│   │   ├── fit-page-limit/
│   │   │   ├── references/
│   │   │   │   └── resize-tactics.md
│   │   │   ├── scripts/
│   │   │   │   └── section_budget.py
│   │   │   └── SKILL.md
│   │   ├── literature-review/
│   │   │   ├── references/
│   │   │   │   ├── claim-extraction.md
│   │   │   │   ├── methodology.md
│   │   │   │   └── review-structure.md
│   │   │   ├── scripts/
│   │   │   │   ├── check_review.py
│   │   │   │   ├── corpus.py
│   │   │   │   ├── forward_refs.py
│   │   │   │   └── init_review.py
│   │   │   └── SKILL.md
│   │   ├── make-poster/
│   │   │   ├── scripts/
│   │   │   │   ├── pitch_check.py
│   │   │   │   ├── poster_figures.py
│   │   │   │   ├── poster_lint.py
│   │   │   │   └── poster_size.py
│   │   │   └── SKILL.md
│   │   ├── make-slides/
│   │   │   ├── references/
│   │   │   │   ├── deck-formats.md
│   │   │   │   ├── narrative-storyboard.md
│   │   │   │   └── venue-timing.md
│   │   │   ├── scripts/
│   │   │   │   ├── deck_lint.py
│   │   │   │   ├── extract_figures.py
│   │   │   │   └── slide_budget.py
│   │   │   └── SKILL.md
│   │   ├── match-style/
│   │   │   ├── references/
│   │   │   │   └── style-dimensions.md
│   │   │   ├── scripts/
│   │   │   │   └── style_signature.py
│   │   │   └── SKILL.md
│   │   ├── orchestrate-paper/
│   │   │   ├── references/
│   │   │   │   ├── pipeline-map.md
│   │   │   │   └── verification-signals.md
│   │   │   ├── scripts/
│   │   │   │   └── pipeline_state.py
│   │   │   └── SKILL.md
│   │   ├── paper-profile/
│   │   │   ├── references/
│   │   │   │   ├── downstream-consumption.md
│   │   │   │   ├── paper-memory-convention.md
│   │   │   │   └── positioning-axes.md
│   │   │   ├── scripts/
│   │   │   │   └── profile_io.py
│   │   │   └── SKILL.md
│   │   ├── parse-cfp/
│   │   │   ├── references/
│   │   │   │   ├── extraction-guide.md
│   │   │   │   └── templates-and-systems.md
│   │   │   ├── scripts/
│   │   │   │   └── fetch_cfp.py
│   │   │   └── SKILL.md
│   │   ├── plan-submission/
│   │   │   ├── references/
│   │   │   │   ├── milestone-playbook.md
│   │   │   │   └── submission-systems.md
│   │   │   ├── scripts/
│   │   │   │   ├── build_timeline.py
│   │   │   │   ├── fetch_page.py
│   │   │   │   └── venue_profile.py
│   │   │   └── SKILL.md
│   │   ├── polish-prose/
│   │   │   ├── references/
│   │   │   │   ├── hedging-and-claims.md
│   │   │   │   ├── llm-tells.md
│   │   │   │   └── venue-register.md
│   │   │   ├── scripts/
│   │   │   │   ├── prose_lint.py
│   │   │   │   ├── terminology_check.py
│   │   │   │   └── texprose.py
│   │   │   └── SKILL.md
│   │   ├── polish-tables-figures/
│   │   │   ├── references/
│   │   │   │   ├── captions-crossrefs.md
│   │   │   │   ├── color-accessibility.md
│   │   │   │   ├── figures.md
│   │   │   │   └── tables.md
│   │   │   ├── scripts/
│   │   │   │   ├── check_floats.py
│   │   │   │   ├── palettes.py
│   │   │   │   └── venueyaml.py
│   │   │   └── SKILL.md
│   │   ├── preflight-check/
│   │   │   ├── references/
│   │   │   │   ├── desk-reject-triggers.md
│   │   │   │   └── manual-checks.md
│   │   │   ├── scripts/
│   │   │   │   ├── check_abstract.py
│   │   │   │   ├── check_anonymization.py
│   │   │   │   ├── check_sections.py
│   │   │   │   ├── check_template.py
│   │   │   │   ├── run_preflight.py
│   │   │   │   ├── texlib.py
│   │   │   │   └── venue_profile.py
│   │   │   └── SKILL.md
│   │   ├── prepare-artifacts/
│   │   │   ├── references/
│   │   │   │   ├── archival-hosting.md
│   │   │   │   ├── badging-standards.md
│   │   │   │   └── venue-artifact-rails.md
│   │   │   ├── scripts/
│   │   │   │   ├── badge_advisor.py
│   │   │   │   ├── check_artifact.py
│   │   │   │   └── venue_profile.py
│   │   │   └── SKILL.md
│   │   ├── prepare-camera-ready/
│   │   │   ├── references/
│   │   │   │   ├── acm-taps-rail.md
│   │   │   │   ├── deanonymize-and-extra-pages.md
│   │   │   │   └── ieee-pdfexpress-rail.md
│   │   │   ├── scripts/
│   │   │   │   ├── camera_ready_checklist.py
│   │   │   │   ├── check_camera_ready.py
│   │   │   │   └── venue_profile.py
│   │   │   └── SKILL.md
│   │   ├── refactor-research-code/
│   │   │   ├── references/
│   │   │   │   └── release-refactor-catalog.md
│   │   │   ├── scripts/
│   │   │   │   └── release_audit.py
│   │   │   └── SKILL.md
│   │   ├── refactor-structure/
│   │   │   ├── references/
│   │   │   │   ├── architecture-checklist.md
│   │   │   │   └── diagnosis-patterns.md
│   │   │   ├── scripts/
│   │   │   │   └── outline_extract.py
│   │   │   └── SKILL.md
│   │   ├── reflect-and-improve/
│   │   │   ├── references/
│   │   │   │   ├── paper-memory-schema.md
│   │   │   │   └── reflection-loop.md
│   │   │   ├── scripts/
│   │   │   │   └── reflect_log.py
│   │   │   └── SKILL.md
│   │   ├── reflect-paper/
│   │   │   └── SKILL.md
│   │   ├── rehearse-qa/
│   │   │   ├── references/
│   │   │   │   ├── answer-coaching.md
│   │   │   │   ├── audience-personas.md
│   │   │   │   └── dreaded-questions.md
│   │   │   ├── scripts/
│   │   │   │   ├── grade_answers.py
│   │   │   │   └── qa_drill.py
│   │   │   └── SKILL.md
│   │   ├── render-workspace-html/
│   │   │   ├── scripts/
│   │   │   │   └── build_dashboard.py
│   │   │   └── SKILL.md
│   │   ├── select-venue/
│   │   │   ├── references/
│   │   │   │   ├── ranking-sources.md
│   │   │   │   └── track-fit.md
│   │   │   ├── scripts/
│   │   │   │   ├── dblp_venue_lookup.py
│   │   │   │   └── list_venues.py
│   │   │   └── SKILL.md
│   │   ├── simulate-reviewers/
│   │   │   ├── references/
│   │   │   │   ├── reviewer-personas.md
│   │   │   │   ├── rubrics.md
│   │   │   │   └── weakness-hunting.md
│   │   │   ├── scripts/
│   │   │   │   ├── aggregate_scores.py
│   │   │   │   └── review_form.py
│   │   │   └── SKILL.md
│   │   ├── study-exemplars/
│   │   │   ├── references/
│   │   │   │   ├── analysis-rubric.md
│   │   │   │   └── finding-exemplars.md
│   │   │   ├── scripts/
│   │   │   │   ├── build_exemplar_bundle.py
│   │   │   │   ├── lookup_exemplar.py
│   │   │   │   ├── polite_http.py
│   │   │   │   └── rank_top_cited.py
│   │   │   └── SKILL.md
│   │   ├── tailor-to-venue/
│   │   │   ├── references/
│   │   │   │   ├── anonymization-sweep.md
│   │   │   │   ├── contribution-reframing.md
│   │   │   │   ├── page-budget-cutting.md
│   │   │   │   └── template-switching.md
│   │   │   ├── scripts/
│   │   │   │   ├── anon_sweep.py
│   │   │   │   ├── page_budget.py
│   │   │   │   ├── texscan.py
│   │   │   │   ├── venue_diff.py
│   │   │   │   └── venueyaml.py
│   │   │   └── SKILL.md
│   │   ├── test-research-code/
│   │   │   ├── references/
│   │   │   │   ├── artifact-standards.md
│   │   │   │   ├── repro-essentials.md
│   │   │   │   └── smoke-tests.md
│   │   │   ├── scripts/
│   │   │   │   └── repro_check.py
│   │   │   └── SKILL.md
│   │   ├── triage-reviews/
│   │   │   ├── references/
│   │   │   │   ├── platform-formats.md
│   │   │   │   └── triage-rubric.md
│   │   │   ├── scripts/
│   │   │   │   ├── build_matrix.py
│   │   │   │   └── parse_reviews.py
│   │   │   └── SKILL.md
│   │   ├── verify-citations/
│   │   │   ├── references/
│   │   │   │   ├── relevance-gate.md
│   │   │   │   ├── triage-guide.md
│   │   │   │   └── verification-sources.md
│   │   │   ├── scripts/
│   │   │   │   └── check_bibtex.py
│   │   │   └── SKILL.md
│   │   ├── verify-claims/
│   │   │   ├── references/
│   │   │   │   ├── claim-taxonomy.md
│   │   │   │   └── overclaiming-rules.md
│   │   │   ├── scripts/
│   │   │   │   └── claim_audit.py
│   │   │   └── SKILL.md
│   │   ├── verify-results/
│   │   │   ├── references/
│   │   │   │   ├── repro-standards.md
│   │   │   │   └── sandbox-and-run.md
│   │   │   ├── scripts/
│   │   │   │   ├── audit_repo.py
│   │   │   │   ├── compare_metrics.py
│   │   │   │   ├── extract_claims.py
│   │   │   │   └── verifylib.py
│   │   │   └── SKILL.md
│   │   ├── work-with-overleaf/
│   │   │   ├── scripts/
│   │   │   │   └── overleaf_status.py
│   │   │   └── SKILL.md
│   │   ├── write-abstract/
│   │   │   ├── references/
│   │   │   │   ├── abstract-structure.md
│   │   │   │   ├── keywords-blocks.md
│   │   │   │   └── venue-norms.md
│   │   │   ├── scripts/
│   │   │   │   ├── abstract_check.py
│   │   │   │   ├── abstract_registration.py
│   │   │   │   ├── keywords_block.py
│   │   │   │   └── venueyaml.py
│   │   │   └── SKILL.md
│   │   ├── write-rebuttal/
│   │   │   ├── assets/
│   │   │   │   └── rebuttal-template.tex
│   │   │   ├── references/
│   │   │   │   ├── cvpr-one-page.md
│   │   │   │   ├── openreview-threads.md
│   │   │   │   ├── response-patterns.md
│   │   │   │   └── revise-and-resubmit.md
│   │   │   ├── scripts/
│   │   │   │   ├── check_budget.py
│   │   │   │   ├── check_coverage.py
│   │   │   │   └── venueyaml.py
│   │   │   └── SKILL.md
│   │   └── write-talk-script/
│   │       ├── references/
│   │       │   ├── script-craft.md
│   │       │   └── timing-and-cuts.md
│   │       ├── scripts/
│   │       │   ├── script_timer.py
│   │       │   └── word_budget.py
│   │       └── SKILL.md
│   ├── .gitignore
│   ├── CITATION.cff
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   ├── LAUNCH.md
│   ├── LICENSE
│   ├── NOTICE
│   ├── README.md
│   └── SECURITY.md
├── VR_HMT_LaTeX_Source/
│   ├── IEEEtran.cls
│   ├── paper.pdf
│   └── paper.tex
├── CHANGELOG.md
├── LICENSE
├── README.md
├── ROADMAP.md
└── TODO.md
```
