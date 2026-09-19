# Paper 37 — Smart AI Resume Analyzer

## 1. Bibliographic Information

- **Paper ID**: Paper37
- **Full Title**: Smart AI Resume Analyzer
- **Authors**: Dr. J. JayaPriya (Assistant Professor), Mouleeswaran R, Kishore T, Praveen G, and Arjun N (UG Scholars)
- **Institution**: Department of Computer Science and Engineering, Karpaga Vinayaga College of Engineering and Technology, GST Road, China Kolambakkam, Maduranthagam, Kanchipuram District, Tamil Nadu - 603308, India
- **Year**: May–June 2025 (Accepted: 01 June 2025, Published: 07 June 2025)
- **Venue**: International Journal of Scientific Research in Science, Engineering and Technology (IJSRSET), Volume 12, Issue 3, pp. 879–883
- **ISSN**: Print ISSN: 2395-1990; Online ISSN: 2394-4099
- **DOI**: 10.32628/IJSRSET2512147
- **PDF filename**: `Paper37_kaushik2025smart.pdf` (Note: filename reflects legacy bibtex tag `kaushik2025smart`; authentic PDF confirms authors Dr. J. JayaPriya, Mouleeswaran R, Kishore T, Praveen G, and Arjun N, IJSRSET June 2025)
- **PDF path**: `Papers/PDFs/Paper37_kaushik2025smart.pdf`
- **Page count**: 5 pages (pp. 879–883)

---

## 2. Research Problem

In contemporary technology-driven hiring, employers rely heavily on automated Applicant Tracking Systems (ATS) to screen candidates. However, ATS platforms reject up to 75% of resumes due to formatting issues, missing keywords, or non-standard layouts, frequently discarding qualified candidates before any human review. Job applicants lack objective diagnostic tools to simulate ATS screening, identify unstated role-specific skill deficiencies, and receive actionable remediation prior to submission.

### Source Evidence
- **Page**: PDF p. 1 (p. 879)
- **Section**: Abstract & Introduction

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To develop and deploy the **Smart AI Resume Analyzer**, an open-source web application combining NLP and machine learning for automated resume evaluation.
2. To compute real-time ATS compatibility scores based on keyword density, machine readability, layout structure, and font usage.
3. To perform role-specific keyword analysis and automated **Skill-Gap Identification** against chosen job profiles.
4. To integrate automated **MOOC course recommendations** mapped directly to identified skill gaps to guide student remediation.
5. To provide an interactive, real-time Streamlit dashboard with customizable, ATS-friendly resume templates for downloadable PDF export.

### Source Evidence
- **Page**: PDF pp. 1–3 (pp. 879–881)
- **Section**: Abstract, Introduction, and Core Functionalities

---

## 4. Research Questions

- *Not explicitly reported* (The paper presents an applied systems engineering platform, architecture, and functional demonstration rather than numbered theoretical hypotheses).

---

## 5. Dataset / Ingestion Scope

- **Ingestion Formats**: Unstructured candidate resumes in PDF and DOCX formats.
- **Job Role Taxonomy**: Predefined catalog of industry job roles (Software Engineer, Data Scientist, Web Developer, Android Developer, DevOps) paired with curated role-specific keyword databases.
- **Open-Source Artifact**: Deployed repository publicly available on GitHub (`https://github.com/Hunterdii/Smart-AI-Resume-Analyzer`).
- **Educational Integration**: Curated catalog of online courses drawn from major Massive Open Online Course (MOOC) providers (Coursera, edX, NPTEL).

### Source Evidence
- **Page**: PDF pp. 2–5 (pp. 880–883)
- **Section**: System Overview, Core Functionalities, References

---

## 6. Features

The platform extracts and scores multi-dimensional resume features:
- **Biographical & Structural Metadata**: Full name, contact email, phone number, section headers, education credentials.
- **Keyword Density & Coverage**: TF-IDF weights of role-specific keywords extracted from candidate text vs target job role profiles.
- **Semantic Vector Representations**: Dense phrase embeddings capturing conceptual equivalence across non-identical terminology.
- **Formatting Compliance Index**: Machine readability metrics checking layout complexity, font accessibility, tables, and column hierarchies.
- **Skill-Gap Deficiencies**: Missing core technical skills, underrepresented frameworks, and rated importance scores.

### Source Evidence
- **Page**: PDF pp. 2–4 (pp. 880–882)
- **Section**: Core Functionalities & NLP and Semantic Analysis

---

## 7. Data Preprocessing

1. **Document Parsing**: `pdfminer` / `docx2txt` extracts raw text streams from uploaded PDF and DOCX files.
2. **Text Normalization**: Tokenization and lemmatization reducing words to dictionary root forms to resolve morphological variances.
3. **Named Entity Recognition (NER)**: spaCy NER pipelines extract entities (institutions, job titles, certifications, qualifications).
4. **TF-IDF & Semantic Vectorization**: Mapping extracted resume tokens and target job descriptions into numerical vector spaces.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 881–882)
- **Section**: NLP and Semantic Analysis

---

## 8. Algorithms and Models

The platform combines NLP libraries and vector similarity algorithms:
1. **Linguistic Parsing & NER**: **spaCy** NLP toolkit for tokenization, dependency parsing, and entity categorization.
2. **Keyword Relevance Weighting**: **TF-IDF (Term Frequency-Inverse Document Frequency)** algorithm scoring word significance against a role-specific keyword database.
3. **Semantic Similarity Engine**: Vector-based semantic similarity scoring comparing phrase embeddings to match conceptual synonyms (e.g., matching "data visualization" with "Tableau/PowerBI").
4. **Keyword Gap Detector**: Set difference and frequency analysis identifying absent or underutilized role competencies.
5. **Course Recommendation Mapping**: Rule-based mapping engine linking missing skill tags to curated MOOC courses.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 881–882)
- **Section**: NLP and Semantic Analysis & References

---

## 9. Architecture

The system implements an interactive, full-stack micro-architecture (System Overview, PDF p. 2):
- **User Interface Layer**: Streamlit reactive dashboard providing drag-and-drop resume ingestion, job role selection dropdowns, and dynamic progress gauges.
- **Parsing & NER Layer**: spaCy pipeline extracting structured entities (skills, experience, education).
- **Analytics & Scoring Layer**:
  - Keyword density evaluator (TF-IDF).
  - Semantic similarity engine (phrase vector matching).
  - Formatting / ATS compatibility checker.
- **Remediation & Recommendation Layer**: Skill-gap detector $\rightarrow$ MOOC course recommendation engine.
- **Template Synthesis Layer**: Template-based resume builder generating ATS-compliant PDF downloads (Modern, Minimal, Professional, Creative).

### Source Evidence
- **Page**: PDF pp. 2–4 (pp. 880–882)
- **Figures / Text**: System Overview, Core Functionalities, Figures 2 and 4

---

## 10. Methodology

1. **Upload & Ingestion**: Candidate uploads resume (PDF/DOCX) and selects desired target job role.
2. **Text Extraction & NER**: Text is extracted, tokenized, lemmatized, and tagged via spaCy.
3. **Multi-Factor Scoring**: System computes overall ATS score, keyword relevance percentage, and formatting quality index.
4. **Skill-Gap Analysis**: Compares candidate skill set against expected role skills, highlighting missing high-priority competencies.
5. **Curated Course Suggestions**: Automatically queries and displays MOOC course links addressing identified gaps.
6. **Iterative Template Rebuilding**: Candidate modifies text in the live feedback panel or selects an ATS-friendly template to export a freshly compiled PDF.

### Source Evidence
- **Page**: PDF pp. 2–5
- **Section**: Core Functionalities & User Interface and Experience

---

## 11. Experimental Setup

- **Frontend & App Framework**: Streamlit web framework.
- **Core NLP Engine**: spaCy toolkit.
- **Machine Learning**: Scikit-learn (TF-IDF vectorizer, cosine distance).
- **Supported Formats**: PDF, DOCX input; standardized PDF export.
- **Public Codebase**: `https://github.com/Hunterdii/Smart-AI-Resume-Analyzer`.

### Source Evidence
- **Page**: PDF pp. 2, 4–5
- **Section**: User Interface and Experience & References

---

## 12. Evaluation Metrics

1. **ATS Compatibility Score**: Composite $0–100\%$ score reflecting machine readability, section clarity, and formatting compliance.
2. **Keyword Match Percentage**: Ratio of matched role-specific technical keywords to total expected keywords.
3. **Formatting Quality Index**: Structural readability rating (font consistency, absence of unparseable tables/graphics).
4. **Skill-Gap Count**: Integer count and importance rating of unfulfilled role competencies.

### Source Evidence
- **Page**: PDF pp. 2–4 (pp. 880–882)
- **Section**: Core Functionalities (Subsections A, B, C, E, F)

---

## 13. Results

### System Functionality & Verification (Section 4 & Figures 2, 4)
- **Real-Time Feedback Engine**: Successfully deployed an interactive Streamlit application delivering instantaneous ATS score updates as users edit their resumes.
- **Skill-Gap & Course Integration**: Demonstrated end-to-end mapping from missing skill keywords (e.g., "Docker", "Kubernetes") to direct MOOC course enrollments.
- **Template-Based PDF Generation**: Validated export across four distinct ATS-optimized layout styles (Modern, Minimal, Professional, Creative), guaranteeing 100% machine-readable font and heading structures.
- **Open-Source Adoption**: The platform was packaged and published as an open-source tool (`Hunterdii/Smart-AI-Resume-Analyzer`) for student career readiness.

### Source Evidence
- **Page**: PDF pp. 2–5 (pp. 880–883)
- **Figures / Text**: Figures 2 & 4, User Interface and Experience, Conclusion

---

## 14. Baselines

- **Standard Enterprise ATS**: Unforgiving black-box commercial ATS parsers that filter candidates without feedback.
- **Manual Resume Review**: Subjective, non-standardized feedback from university placement advisors.

### Source Evidence
- **Page**: PDF pp. 1–2
- **Section**: Introduction & System Overview

---

## 15. Ablation Study

- *Not reported* (Applied software systems paper describing platform design, open-source release, and operational workflows).

---

## 16. Explainability

- **Transparent Diagnostic Breakdown**: Rather than returning a single opaque score, the dashboard provides a clear itemized breakdown:
  - Exact matched keywords vs missing keywords.
  - Granular formatting flaws (e.g., flagging unreadable multi-column tables or non-standard fonts).
  - Explicit justification for *why* a particular course is recommended based on the detected skill deficit.

### Source Evidence
- **Page**: PDF pp. 3–4
- **Section**: Core Functionalities & User Interface and Experience

---

## 17. Main Findings

1. Providing candidates with real-time, interactive ATS simulation bridges the gap between academic preparation and corporate recruitment screening.
2. Coupling skill-gap identification with direct MOOC course recommendations transforms an ATS parser from a passive gatekeeper into an active instructional tool.
3. Streamlit combined with spaCy and Scikit-learn provides an accessible, rapid-deployment architecture for student-facing placement diagnostic portals.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Conclusion

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Predefined Job Role Scope**: Evaluations depend on static, predefined keyword databases rather than dynamically scraping live job postings.
2. **Text-Only Processing**: Does not evaluate portfolios, GitHub links, or coding repositories directly.
3. **English Language Focus**: Preprocessing models and keyword lists are exclusively tailored to English resumes.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The paper describes system architecture and functional workflows; it does not report statistical precision/recall metrics or large-scale user retention trials across thousands of students.

### Source Evidence
- **Page**: PDF pp. 2–5
- **Section**: Core Functionalities & Conclusion

---

## 19. Future Work

Explicitly proposed by the authors:
1. Expanding the job catalog with dynamic real-time job market API synchronization.
2. Integrating multimodal portfolio analysis (GitHub project analysis, LinkedIn profile ingestion).
3. Developing automated resume tailoring agents that dynamically suggest bullet-point rewrites using generative LLMs.

### Source Evidence
- **Page**: PDF pp. 4–5
- **Section**: Conclusion

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides immediate functional precedents for PRIE's **ATS Resume Analyzer** and **Course Recommendation Engine**:
1. **Connecting ATS Analysis to Learning Recommendations**: JayaPriya et al. validate ScholarCamp's exact philosophy: identifying a resume gap is only half the battle; the engine must immediately recommend curated learning modules to bridge that gap.
2. **Open-Source Codebase Verification**: The authors provide an accessible, working GitHub codebase (`Hunterdii/Smart-AI-Resume-Analyzer`) whose Streamlit interface patterns, spaCy NER pipelines, and ReportLab PDF template exporters can be benchmarked against PRIE's internal ATS services.
3. **Closing the Stated Dynamic Sync Limitation**: JayaPriya et al. note their reliance on static keyword lists; PRIE directly resolves this limitation by integrating live job-portal scraping (Mishra 2025, Paper 11) and Doc2Vec implicit skill mining (Gugnani & Misra 2020, Paper 35).

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **System Overview** | "Smart AI Resume Analyzer is an innovative solution... evaluates and enhances resumes using Natural Language Processing (NLP) and machine learning." | PDF p. 1, Abstract | Direct statement |
| **Eight Core Features** | Real-time scoring, keyword analysis, formatting evaluation, template builder, ATS checker, skill-gap detection, course recommendations, dashboard. | PDF pp. 2–3, Core Functionalities | System specification |
| **NLP Stack** | spaCy tokenization and lemmatization, NER for qualifications, TF-IDF keyword weighting, vector semantic similarity. | PDF pp. 3–4, NLP & Semantic Analysis | Methodology |
| **Frontend Framework** | Streamlit framework with interactive charts, color-coded indicators, and live feedback panel. | PDF p. 4, UI & Experience | Technical specification |
| **Open Source Codebase** | Cites public GitHub repository `https://github.com/Hunterdii/Smart-AI-Resume-Analyzer`. | PDF p. 5, Reference [1] | Open source citation |
| **Author Future Scope** | Dynamic job-market synchronization, portfolio integration, and generative resume rewriting. | PDF p. 5, Conclusion | Author future work |

---

## 22. Verification Checklist

- [x] PDF read (`Paper37_kaushik2025smart.pdf`, 5 pages)
- [x] Introduction inspected
- [x] Core functionalities inspected (8 explicit modules in Section 3)
- [x] Methodology inspected (spaCy NER, TF-IDF, vector semantic similarity, Streamlit)
- [x] Features verified (Biographical metadata, keyword coverage, formatting index, skill gaps)
- [x] Architecture inspected (System overview, Figures 2 and 4 verified)
- [x] Repository verified (GitHub `Hunterdii/Smart-AI-Resume-Analyzer` cited in Ref 1)
- [x] Limitations verified (Predefined role scope, text-only, English restriction)
- [x] Future work verified (Live job sync, portfolio analysis, generative rewriting)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact 8 core functionalities from Section 3, spaCy/TF-IDF methodology, and open-source GitHub citation verified directly from source text; legacy filename discrepancy documented).
