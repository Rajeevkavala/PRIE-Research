# Paper 12 — Resume Parser Using NLP

## 1. Bibliographic Information

- **Paper ID**: Paper12
- **Full Title**: Resume Parser Using NLP
- **Authors**: Mohammed Kashif (Student) and Parimal Kumar K R (Assistant Professor)
- **Institution**: Department of Masters of Computer Application, Vidya Vikas Institute of Engineering & Technology, Mysuru, Karnataka, India
- **Year**: 2024 (Published: September 2024)
- **Venue**: International Journal of Advanced Research in Computer and Communication Engineering (IJARCCE), Vol. 13, Issue 9, pp. 33–37
- **ISSN (Online)**: 2278-1021
- **ISSN (Print)**: 2319-5940
- **DOI**: 10.17148/IJARCCE.2024.13905
- **PDF filename**: `Paper12_roy2024resume.pdf`
- **PDF path**: `Papers/PDFs/Paper12_roy2024resume.pdf`
- **Page count**: 5 pages (pp. 33–37)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper12_roy2024resume.bib`) listed synthetic authors ("Roy, Soumya and Bhattacharya, Anirban") and title extension ("Resume Parser Using NLP and Contextual Information Extraction"). Inspection of the actual PDF confirms the true authors are Mohammed Kashif and Parimal Kumar K R from Vidya Vikas Institute of Engineering & Technology.

---

## 2. Research Problem

The paper addresses the labor-intensive, slow, and subjective nature of manual resume screening in modern recruitment. Manual reviews frequently introduce human evaluation inconsistencies, recruiter fatigue, and cognitive biases, which often cause qualified candidates to be overlooked. Organizations receiving large volumes of unstructured resumes require an automated, context-aware solution that standardizes extraction, reduces hiring turnaround time, and provides objective candidate-to-job matching with actionable feedback.

### Source Evidence
- **PDF Page**: Page 2 (p. 34), Section "Problem statement:" & Section I "INTRODUCTION".

---

## 3. Research Objectives

1. Develop an automated "AI Resume Analyzer" capable of parsing unstructured resume files (PDF/Word/Text) into standardized structured entities.
2. Implement Named Entity Recognition (NER) and tokenization using spaCy and NLTK to extract contact information, skills, qualifications, and work experience.
3. Train a Linear Support Vector Machine (Linear SVM) classifier to categorize and match resumes against target job roles.
4. Construct a cosine similarity recommendation engine to identify skill deficits and suggest personalized courses, certifications, and suitable career tracks.
5. Deploy an interactive web portal using Streamlit integrated with a MySQL database for candidate uploads and administrator recruitment analytics.

### Source Evidence
- **PDF Page**: Page 2 (p. 34), Section "Problem statement:"; Page 3 (p. 35), Section III "METHODOLOGY".

---

## 4. Research Questions

Not explicitly reported in formal question syntax. The study is structured around system development, pipeline integration, and empirical precision validation.

---

## 5. Dataset

- **Dataset Name**: Resume and Job Description Screening Dataset
- **Dataset Source**: Multi-source collection of resumes and job descriptions (collected from various industry sectors and publicly available recruitment formats)
- **Institution**: Vidya Vikas Institute of Engineering & Technology, Mysuru, India
- **Collection Period**: 2024
- **Dataset Size / Samples**: Not explicitly reported in total count numbers; described as a labeled corpus of resumes and corresponding job descriptions.
- **Target Variable**: Job role suitability classification and skill similarity score
- **Data Type**: Unstructured text documents (PDF/Word formats) converted to standardized plaintext
- **Real / Synthetic**: Real applicant resumes and industry job descriptions
- **Public / Private**: Private / Curated academic project dataset
- **Train / Test Split**: Labeled dataset utilized with cross-validation for hyperparameter tuning (exact split ratio not explicitly reported).

### Source Evidence
- **PDF Page**: Page 3 (p. 35), Section III "METHODOLOGY".

---

## 6. Features

The extracted feature schema spans:

### Demographic & Contact
- Applicant Name
- Email Address
- Phone Number / Contact Information

### Academic & Educational
- Degree / Qualification level
- Academic institutions attended
- Graduation timeline

### Skills & Competencies
- Technical skills inventory
- Domain-specific toolkits
- Professional certifications

### Experience & Roles
- Past job titles
- Years of professional experience
- Project summaries and organizational affiliations

### Source Evidence
- **PDF Page**: Page 3 (p. 35), Section III "METHODOLOGY" & Page 4 (p. 36), Section IV "ALGORITHMS".

---

## 7. Data Preprocessing

The document transformation pipeline consists of:
1. **Format Harmonization**: Converting uploaded document formats (PDF/DOCX) into consistent plain text streams.
2. **Text Normalization**: Tokenization, lowercase transformation, and punctuation filtering.
3. **Stopword Removal**: Eliminating non-informative lexical stopwords using NLTK corpora.
4. **Part-of-Speech (POS) Tagging**: Tagging grammatical classes to disambiguate noun phrases representing technical competencies.
5. **Entity Recognition (NER)**: Applying spaCy pipelines to identify named entities (person names, organizations, dates, locations).
6. **Relational Schema Mapping**: Inserting parsed structured attributes into relational MySQL database tables.

### Source Evidence
- **PDF Page**: Page 3 (p. 35), Section III "METHODOLOGY" & Page 4 (p. 36), Section IV "ALGORITHMS".

---

## 8. Algorithms and Models

- **Information Extraction**:
  - `spaCy` NLP pipeline: Dependency parsing and custom Named Entity Recognition (NER).
  - `NLTK`: Tokenization, POS tagging, and stopword filtering.
- **Job Role Classification**:
  - **Linear Support Vector Machine (Linear SVM)**: Supervised classifier trained on labeled feature vectors of resumes and job descriptions to categorize candidate suitability across job roles.
- **Recommendation & Matching Engine**:
  - **Cosine Similarity**: Vector-space cosine distance computed between extracted candidate skill vectors and target job requirement profiles to rank role alignment and compute skill gaps.

### Source Evidence
- **PDF Page**: Page 3 (p. 35), Section III & Page 4 (p. 36), Section IV "ALGORITHMS".

---

## 9. Architecture

The system is architected across four operational tiers:
1. **User Interface Layer**: Built with **Streamlit**, providing candidate profile submission, real-time recommendation viewing, and administrator analytics dashboards.
2. **NLP & Parsing Engine**: Tokenizer, POS tagger, and NER parser transforming unstructured resume text into standardized attribute dictionaries.
3. **Machine Learning & Matching Core**:
   - Linear SVM classifier predicting job category fit.
   - Cosine similarity matching engine calculating alignment scores and recommending targeted skills/certifications.
4. **Persistence & Analytics Layer**: **MySQL database** storing applicant profiles, similarity scores, and administrative analytics (activity maps, applicant trend pie charts, CSV report exports).

### Source Evidence
- **PDF Page**: Page 3 (p. 35), Section III & Page 4 (p. 36), Section IV.

---

## 10. Methodology

1. **Document Ingestion**: Applicant uploads resume via Streamlit web portal.
2. **Text Extraction & Cleaning**: Document is parsed into raw text; NLTK and spaCy perform tokenization, stopword removal, and POS tagging.
3. **Information Structuring**: NER extracts candidate entities (skills, experience, education, contacts) into structured attributes.
4. **Supervised Classification**: Linear SVM evaluates candidate vectors against labeled job category profiles.
5. **Similarity & Gap Analysis**: Cosine similarity calculates profile alignment against target job requirements, detecting missing skills.
6. **Prescriptive Guidance**: Generation of personalized advice (additional skills, online courses, role suggestions).
7. **Storage & Administrative Reporting**: Data is committed to MySQL; administrators inspect aggregate recruitment dashboards.

### Source Evidence
- **PDF Page**: Pages 3–4 (pp. 35–36), Sections III and IV.

---

## 11. Experimental Setup

- **Software Framework**: Python, Streamlit web framework.
- **NLP Libraries**: `spaCy`, `nltk`.
- **Machine Learning**: `scikit-learn` (Linear SVM, Cosine Similarity).
- **Database Engine**: MySQL.
- **Reporting Tools**: Integrated charting libraries producing pie charts, activity maps, and CSV exports.

### Source Evidence
- **PDF Page**: Page 3 (p. 35), Section III & Page 4 (p. 36), Section V.

---

## 12. Evaluation Metrics

- **Precision**: Proportion of correctly assigned job roles over total positive predictions.
- **Accuracy**: Overall parsing and extraction correctness across resumes.
- **Recall & F1-Score**: Evaluated across information extraction and role classification tasks.
- **User Satisfaction**: Qualitative usability and accessibility feedback from applicants and administrative users.

### Source Evidence
- **PDF Page**: Page 4 (p. 36), Section V "RESULT AND DISCUSSION".

---

## 13. Results

### Reported Performance Values
- **Classification Precision**: The Linear SVM classifier achieved a **precision of over 85%** in matching and categorizing resumes based on job role requirements.
- **Parsing Accuracy**: High accuracy demonstrated in extracting contact details, skills, education, and work experience entities.
- **Usability & Administrative Throughput**: Streamlit UI enabled real-time feedback; administrative features successfully generated visual analytics and CSV reports, significantly reducing HR administrative burden.

### Source Evidence
- **PDF Page**: Page 4 (p. 36), Section V "RESULT AND DISCUSSION".

---

## 14. Baselines

- **Manual Resume Screening**: Conventional human HR screening process characterized by manual document review, spreadsheet logging, and subjective evaluations.

### Source Evidence
- **PDF Page**: Page 2 (p. 34), Section "Problem statement:" & Page 4 (p. 36), Section V.

---

## 15. Ablation Study

Not reported.

---

## 16. Explainability

Feature-based transparent feedback: While formal Shapley (SHAP) or LIME models are not used, the system provides transparent candidate feedback by explicitly outputting the matched vs. missing skills that drove the cosine similarity ranking score.

### Source Evidence
- **PDF Page**: Page 4 (p. 36), Section V "Personalized Recommendations".

---

## 17. Main Findings

1. Named Entity Recognition (NER) combined with POS tagging accurately transforms unstructured multi-format resume documents into standardized relational attributes.
2. Linear SVM provides robust, reliable candidate categorization across job domains, achieving $>85\%$ precision.
3. Vector-space cosine similarity effectively surfaces specific skill deficiencies and enables automated, personalized upskilling recommendations.
4. Streamlit and MySQL provide a lightweight, accessible full-stack architecture for deployment in institutional placement cells.

### Source Evidence
- **PDF Page**: Page 4 (p. 36), Section V & Page 5 (p. 37), Section VI "CONCLUSION".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Complex Layout Fragility**: The system struggled with resumes possessing unconventional layouts, multi-column designs, or heavy graphical formatting, leading to occasional parsing inaccuracies.
- **Lexical Ambiguity**: NLP models occasionally misclassified ambiguous text strings or poorly structured candidate descriptions.
- **Static Job Profiles**: The recommendation engine relies on a predefined set of job requirements, limiting its adaptability to highly specialized or emerging niche roles.

### 18.2 Research Interpretation
- The authors do not report sample size numbers ($N$) or a complete multi-class confusion matrix.
- Semantic matching relies primarily on surface-level keyword/cosine overlap rather than dense bi-encoder transformer embeddings (e.g., SBERT).

---

## 19. Future Work

Explicitly proposed by authors:
1. Incorporating advanced deep learning NLP models (e.g., Transformers/BERT) to improve parsing accuracy on complex layouts.
2. Direct integration with commercial Applicant Tracking Systems (ATS) and live job portals for real-time submission analysis.
3. Expanding domain taxonomy to support broader international industries and multi-language resume parsing.

### Source Evidence
- **PDF Page**: Page 5 (p. 37), Section VI "CONCLUSION".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE ATS & Resume Analysis Engine (Module 04)**.
- **Methodological Value**: Confirms that combining entity parsing (spaCy) with supervised classification (Linear SVM $>85\%$ precision) and similarity ranking delivers effective resume optimization feedback.
- **PRIE Enhancement**: Directly addresses the authors' stated limitation (fragility on complex formatting and static job requirements) by motivating PRIE's use of dense transformer representations and live scraped job ontologies.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Linear SVM achieves $>85\%$ precision | "achieved a precision of over 85%" | PDF p. 4, Section V | Experimental result |
| spaCy NER and NLTK pipeline | Extraction of contact details, skills, education, experience | PDF pp. 3–4, Sections III & IV | Methodology |
| Cosine similarity for recommendation | Matching extracted skills against job requirements | PDF p. 4, Section IV & V | Methodology |
| Streamlit UI and MySQL backend | Interface and storage architecture | PDF pp. 3–4, Sections III & IV | Architecture |
| Fragility on unconventional resume formats | "faced challenges... in handling resumes with unconventional formats" | PDF p. 4, Section V | Author discussion |

---

## 22. Verification Checklist

- [x] PDF read
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected
- [x] Dataset verified
- [x] Features verified
- [x] Algorithms verified
- [x] Architecture inspected
- [x] Experiments inspected
- [x] Results verified
- [x] Limitations verified
- [x] Future work verified
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read, exact precision metric cited, author correction from legacy BibTeX documented).
