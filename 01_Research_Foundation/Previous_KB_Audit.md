# Previous Knowledge Base Audit Report — Phase 01

> **Objective**: Rigorous audit of the 5 legacy AI-generated notes found in `Research-Knowledge-Base/` before the rebuild, comparing their claims against the primary PDF evidence.
> **Preservation**: All 5 legacy notes have been preserved under `Research-Knowledge-Base/_Previous_AI_Summaries/` for full audit traceability.

---

## 1. Executive Summary of Audit Findings

The previous knowledge base consisted of only 5 notes (out of the intended corpus), which were generated largely without reading the actual downloaded research papers. A systematic comparison against the source PDFs reveals critical deficiencies:

1. **Hallucinated / Placeholder Metadata**:
   - The previous notes repeatedly cited authors as "Anonymous / Independent Consortium", "Independent Researchers", or generic placeholder names, when the actual PDFs clearly display the full names, departments, and academic institutions of the true authors.
   - For example, `Paper01` was attributed to "RMUTL Research Group" with a modified title, while the actual PDF author list is **Tewa Promnuchanont, Sureenat Manola, and Worakarn Jaidee**; `Paper05` was attributed to "Independent Researchers", while the actual PDF is by **Nicholas X. Wang, Neel V. Parpia, and Aaryan D. Parikh (Stellar Learning Technologies)** published in IEEE MIPR.
2. **Incorrect Paper Assignment**:
   - `Paper03_Resume_Parser_NLP_2025.md` in the legacy KB was written as a resume parser paper based on secondary snippets. In reality, the PDF file in the corpus (`Paper11_consortium2025resume.pdf`) contains a completely different research article: **"Web Scraping for Job Listings Using Python and BeautifulSoup" by Dr. Reeta Mishra**.
3. **Missing Empirical Evidence**:
   - All 5 previous notes lacked verifiable page-level and table-level source citations (`PDF p. X, Section Y, Table Z`).
   - Numerical results and preprocessing protocols were either described in vague qualitative terms or accompanied by disclaimers such as: *"exact author names, DOI, feature schema, split protocol, tuning procedure, and implementation stack were not provided."*

---

## 2. Item-by-Item Paper Audit

### Legacy Note 1: `Paper01_Graduate_Employability_RMUTL_2023.md`
- **Current Corpus ID**: Maps to `Paper24` (`Paper24_rmutl2023data.pdf`)
- **Legacy Title**: Graduate Employability Prediction Using Multi-Model Data Mining Frameworks
- **Actual PDF Title**: Data Mining Model Approach for Employment Prediction for University Graduates
- **Legacy Authors**: RMUTL Research Group (as reported)
- **Actual PDF Authors**: Tewa Promnuchanont, Sureenat Manola*, Worakarn Jaidee (Department of Business Information System, Rajamangala University of Technology Lanna)
- **Legacy Venue**: SciTechAsia (2023)
- **Actual PDF Venue**: Science & Technology Asia Vol. 31 No. 1, Jan–Mar 2026, pp. 145–158
- **Claim Classifications**:
  - Author / Institution: **INCORRECT** (True authors were omitted and replaced with institution alias)
  - Title: **PARTIALLY VERIFIED** (Approximated title)
  - Dataset & Results: **UNSUPPORTED** in legacy note; must be re-extracted directly from PDF p. 147–154.
- **Verdict**: Replaced by fully grounded research note under `Research-Knowledge-Base/01_Employability/Paper24_Employment_Prediction_RMUTL_2026.md`.

---

### Legacy Note 2: `Paper02_XAI_Academic_Performance_2026.md`
- **Current Corpus ID**: Maps to `Paper18` (`Paper18_hidayatulloh2026explainable.pdf`)
- **Legacy Title**: Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction
- **Actual PDF Title**: Explainable Artificial Intelligence-Based Model for Student Academic Performance Prediction
- **Legacy Authors**: W. Hidayatulloh, F. Mahardika, D. I. Junaedi
- **Actual PDF Authors**: Wildan Hidayatulloh, Fathoni Mahardika, Dani Indra Junaedi (Universitas Sebelas April, Indonesia)
- **Legacy Venue**: Journal of Information System Exploration and Research (JOISER), Vol. 4 No. 1, 2026
- **Actual PDF Venue**: JOISER Vol. 4, No. 1, January 2026, pp. 31–40 (DOI: 10.52465/joiser.v4i1.62419)
- **Claim Classifications**:
  - Metadata: **VERIFIED**
  - Empirical Findings: **PARTIALLY VERIFIED** (General model choices noted, but specific split, hyperparameter configurations, and exact SHAP feature rankings lacked page/table citations)
- **Verdict**: Replaced by fully grounded research note with explicit page citations under `Research-Knowledge-Base/03_XAI/Paper18_Explainable_Student_Performance_2026.md`.

---

### Legacy Note 3: `Paper03_Resume_Parser_NLP_2025.md`
- **Current Corpus ID**: Associated with `Paper11` (`Paper11_consortium2025resume.pdf`)
- **Legacy Title**: Resume Parser and Auto-Formatter Using NLP
- **Actual PDF Content**: Web Scraping for Job Listings Using Python and BeautifulSoup
- **Legacy Authors**: Anonymous / Independent Consortium
- **Actual PDF Author**: Dr. Reeta Mishra (IILM University, Greater Noida)
- **Legacy Venue**: IJCRT equivalent
- **Actual PDF Venue**: Scientific Journal of Artificial Intelligence and Blockchain Technologies, Vol. 2, Issue 3, July–Sept 2025, pp. 63–70 (DOI: 10.63345/sjaibt.v2.i3.308)
- **Claim Classifications**:
  - Entire Note Content: **INCORRECT / MISMATCH** (The legacy note described an NLP resume parser, whereas the actual downloaded PDF is an empirical paper on web scraping job postings using BeautifulSoup).
- **Verdict**: **CRITICAL AUDIT FINDING**. The previous note must be completely discarded and replaced by an authentic research note covering Dr. Reeta Mishra's actual job web scraping methodology.

---

### Legacy Note 4: `Paper04_Multimodal_Mock_Interview_2025.md`
- **Current Corpus ID**: Maps to `Paper15` (`Paper15_consortium2025multimodal.pdf`)
- **Legacy Title**: Multimodal AI-Based Mock Interview System: Integrating Facial Expression Analysis, Speech Emotion Recognition, and NLP for Holistic Candidate Evaluation
- **Actual PDF Title**: Multimodal AI-Based Mock Interview System: Integrating Facial Expression Analysis, Speech Emotion Recognition, and NLP for Holistic Candidate Evaluation
- **Legacy Authors**: Independent Consortium
- **Actual PDF Authors**: Shoaib Inamdar, Abhijeet Panchal, Priyanka Kumbhar, Yogita Sontakke, Asma Hannure (A G Patil Institute of Technology, Solapur)
- **Legacy Venue**: IJSRED Vol. 8, Issue 6, Nov–Dec 2025, pp. 681–683
- **Claim Classifications**:
  - Authors: **INCORRECT** in legacy note (actual student/faculty authors were replaced with "Independent Consortium")
  - System Architecture: **PARTIALLY VERIFIED** (Described high-level concepts, but lacked page-specific evidence for CNN/OpenCV models)
- **Verdict**: Replaced by authentic, verified research note under `Research-Knowledge-Base/05_Mock_Interview/Paper15_Multimodal_Mock_Interview_2025.md`.

---

### Legacy Note 5: `Paper05_Causal_Graph_AQG_2026.md`
- **Current Corpus ID**: Maps to `Paper25` (`Paper25_cognitive2026automatic.pdf`)
- **Legacy Title**: Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning
- **Actual PDF Title**: Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided Chain of Thought Reasoning
- **Legacy Authors**: Independent Researchers / Anonymous
- **Actual PDF Authors**: Nicholas X. Wang, Neel V. Parpia, Aaryan D. Parikh (Stellar Learning Technologies, San Jose, USA)
- **Legacy Venue**: arXiv preprint
- **Actual PDF Venue**: IEEE International Conference on Multimedia Information Processing and Retrieval (IEEE MIPR 2025), August 2025
- **Claim Classifications**:
  - Authors & Venue: **INCORRECT** in legacy (IEEE MIPR peer-reviewed conference paper was mischaracterized as anonymous preprint)
  - Methodology & Results: **PARTIALLY VERIFIED** (High-level concepts described, but lacking exact BLEU/ROUGE scores and ablation tables from PDF)
- **Verdict**: Replaced by authentic research note with exact IEEE MIPR citations under `Research-Knowledge-Base/09_Question_Generation/Paper25_Causal_Graph_AQG_2025.md`.

---

## 3. Discrepancy Classification Summary

| Legacy Note | Associated Actual PDF | Claim: Authors | Claim: Title | Claim: Venue | Claim: Methodology | Overall Audit Classification |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| `Paper01_Graduate_Employability` | `Paper24_rmutl2023data.pdf` | INCORRECT | PARTIALLY VERIFIED | PARTIALLY VERIFIED | UNSUPPORTED | **REJECTED (REQUIRES REWRITE)** |
| `Paper02_XAI_Academic_Perf` | `Paper18_hidayatulloh2026explainable.pdf` | VERIFIED | VERIFIED | VERIFIED | PARTIALLY VERIFIED | **NEEDS EVIDENCE LOCATION UPGRADE** |
| `Paper03_Resume_Parser_NLP` | `Paper11_consortium2025resume.pdf` | INCORRECT | INCORRECT | INCORRECT | INCORRECT | **REJECTED (TOTAL CONTENT MISMATCH)** |
| `Paper04_Multimodal_Interview`| `Paper15_consortium2025multimodal.pdf` | INCORRECT | VERIFIED | VERIFIED | PARTIALLY VERIFIED | **NEEDS TRUE AUTHORS & CITATIONS** |
| `Paper05_Causal_Graph_AQG` | `Paper25_cognitive2026automatic.pdf` | INCORRECT | VERIFIED | INCORRECT | PARTIALLY VERIFIED | **NEEDS TRUE AUTHORS & IEEE CITATIONS** |

---

## 4. Conclusion

The audit conclusively validates the necessity of the Phase 01 Rebuild: 
- 0 out of 5 legacy notes met the strict academic standard required for formal publication.
- None contained page-specific evidence locations.
- Authors were frequently fabricated or replaced with "Consortium" / "Anonymous".
- One note (`Paper03`) described a completely different paper than what the PDF file actually contains.

All 44 downloaded research papers will now be read directly from their source PDFs, extracting authentic authors, institutions, datasets, hyperparameters, and numerical findings with exact page and table references.
