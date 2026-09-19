# Paper 36 — Resume Parsing and Job Recommendation Using NLP and Machine Learning

## 1. Bibliographic Information

- **Paper ID**: Paper36
- **Full Title**: Resume parsing and job recommendation using NLP and Machine learning
- **Authors**: Snehal Suryawanshi, Prajwal Mali, Sarthak Rasal, under the guidance of Prof. Santosh Bhosale
- **Institution**: Department of Computer Engineering, Prerana Pratishthan’s Universal College of Engineering and Research, Sasewadi, Pune (Affiliated to Savitribai Phule Pune University), Pune, India
- **Year**: November 2025
- **Venue**: International Journal for Research Trends and Innovation (IJRTI), Volume 10, Issue 11, November 2025, pp. a313–a314
- **ISSN**: 2456-3315 (Article ID: IJRTI2511041)
- **DOI**: Available via IJRTI (www.ijrti.org)
- **PDF filename**: `Paper36_mishra2025resume.pdf` (Note: filename reflects legacy bibtex tag `mishra2025resume`; authentic PDF confirms authors Snehal Suryawanshi, Prajwal Mali, Sarthak Rasal, and Prof. Santosh Bhosale, IJRTI November 2025)
- **PDF path**: `Papers/PDFs/Paper36_mishra2025resume.pdf`
- **Page count**: 2 pages (pp. a313–a314)

---

## 2. Research Problem

Organizations face an overwhelming influx of online job applications, receiving thousands of resumes per job opening. Manual screening and shortlisting is exceptionally time-consuming, labor-intensive, and prone to human cognitive fatigue and subjective bias. Candidates lack immediate feedback on how closely their resumes align with market requirements, while recruiters struggle to match candidate competencies to appropriate job descriptions quickly.

### Source Evidence
- **Page**: PDF p. 1 (p. a313)
- **Section**: Abstract & Section 1 — Introduction

---

## 3. Research Objectives

The authors explicitly define nine operational objectives in Section 2:
1. To develop an intelligent automated resume parsing system using Natural Language Processing (NLP).
2. To extract structured key entities: name, contact information, education, experience, and technical skills from unstructured resumes.
3. To build an efficient text preprocessing pipeline (cleaning, tokenization, lemmatization, stop-word removal).
4. To categorize candidate profiles based on extracted attributes.
5. To construct a machine learning-driven job recommendation system matching parsed resumes to job descriptions.
6. To deploy NLP embeddings (Word2Vec, BERT, TF-IDF) and similarity measures (cosine similarity) for accurate profile-job alignment.
7. To evaluate system performance using Accuracy, Precision, Recall, and F1-score.
8. To create an accessible web-based interface (Streamlit / Flask) for resume uploading and recommendation display.
9. To automate candidate screening, reducing manual recruitment overhead.

### Source Evidence
- **Page**: PDF p. 1 (p. a313)
- **Section**: Section 2 — Objectives

---

## 4. Research Questions

- *Not explicitly reported* (The paper presents an applied undergraduate engineering capstone system implementation and functional accuracy evaluation rather than formal academic hypotheses).

---

## 5. Dataset

- **Corpus**: Benchmark dataset of resumes (PDF and DOCX formats) and job postings compiled from public repositories (Kaggle Job Matching Dataset).
- **Target Attributes**: Candidate name, email/phone, degrees, work history, programming languages, and industry skill tags.
- **Evaluation Set**: Test set of resumes matched across multi-industry technical job descriptions.

### Source Evidence
- **Page**: PDF pp. 1–2 (pp. a313–a314)
- **Section**: Section 6 — Implementation & Section 10 — References

---

## 6. Features

The parsing and matching pipeline extracts:
- **Biographical & Contact Metadata**: Candidate name, email address, phone number.
- **Educational Qualifications**: Degree titles (B.Tech, B.E., M.S.), institutions, graduation years, GPA/percentages.
- **Work History & Experience**: Job titles, company names, tenure duration, project descriptions.
- **Technical Skills**: Programming languages, software tools, frameworks, and domain expertise.
- **Vector Representations**: High-dimensional TF-IDF sparse vectors and dense Word2Vec/BERT semantic embeddings.

### Source Evidence
- **Page**: PDF pp. 1–2
- **Section**: Section 2 & Section 6

---

## 7. Data Preprocessing

1. **Document Text Extraction**: PyPDF2 and `docx2txt` parse raw unstructured text from uploaded PDF and DOCX files.
2. **Text Cleansing**: Lowercasing, removal of non-alphanumeric special characters, URLs, and formatting artifacts.
3. **Linguistic Preprocessing**: Tokenization, stop-word elimination, and lemmatization using NLTK and spaCy.
4. **Named Entity Recognition (NER)**: spaCy entity recognition customized to isolate skills, education institutions, and candidate names into structured JSON/CSV files.

### Source Evidence
- **Page**: PDF pp. 1–2
- **Section**: Section 5 & Section 6

---

## 8. Algorithms and Models

1. **Text Extraction & NER**: **spaCy** NLP model trained for entity recognition, supplemented by regular expressions for contact details.
2. **Feature Representation**: **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Word2Vec / BERT** dense embeddings.
3. **Similarity Scoring**: **Cosine Similarity** computing the angular distance between candidate vector $u$ and job vector $v$:
   $$\text{Cosine Similarity}(u, v) = \frac{u \cdot v}{\|u\| \|v\|}$$
4. **Classification Models**: **Random Forest** and **Logistic Regression** classifiers trained to classify candidate-job matches into binary relevance categories.

### Source Evidence
- **Page**: PDF p. 2 (p. a314)
- **Section**: Section 5 & Section 6

---

## 9. Architecture

The system implements a six-layer modular pipeline (Section 4):
1. **Input Layer**: Web portal accepting PDF and DOCX resume uploads.
2. **Processing Layer**: PyPDF2 / docx2txt text extraction and NLTK/spaCy cleansing.
3. **Feature Extraction Layer**: spaCy NER entity tagging and TF-IDF / embedding vectorization.
4. **Model Layer**: Random Forest / Logistic Regression classification models.
5. **Recommendation Layer**: Cosine similarity ranking engine outputting top matched job descriptions.
6. **Database Layer**: MongoDB / Firebase storing parsed candidate profiles, job descriptions, and session logs.

### Source Evidence
- **Page**: PDF p. 2 (p. a314)
- **Section**: Section 4 — System Architecture

---

## 10. Methodology

1. **Upload & Parse**: Candidate uploads resume via Streamlit/Flask UI; PyPDF2 extracts raw text.
2. **NER Entity Extraction**: spaCy extracts skills, education, and experience, structuring them into a JSON profile.
3. **Vector Transformation**: Resume text and target job postings are converted into numerical vectors via TF-IDF / embeddings.
4. **Relevance Computation**: Cosine similarity scores the match between candidate profile and active job descriptions.
5. **Ranked Delivery**: The system filters, ranks, and renders top matching job openings on the user interface.

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section 5 (Algorithm Steps 1 to 10)

---

## 11. Experimental Setup

- **Programming Language**: Python 3.x
- **Core Libraries**: spaCy, NLTK, Scikit-learn, PyPDF2, docx2txt.
- **Web Interface**: Streamlit / Flask web dashboard.
- **Backend Storage**: Firebase / MongoDB document database.
- **Dataset Source**: Kaggle Job Matching Dataset.

### Source Evidence
- **Page**: PDF pp. 1–2
- **Section**: Abstract, Section 6, Section 10

---

## 12. Evaluation Metrics

1. **Entity Extraction Accuracy**: Percentage of correctly identified entities (skills, education, contact info) across parsed resumes (**92%**).
2. **Job Recommendation Relevance Accuracy**: Percentage of top recommended jobs judged relevant by recruiters (**88%**).
3. **Precision, Recall, F1-Score**: Evaluated on candidate-job matching classification.

### Source Evidence
- **Page**: PDF p. 2 (p. a314)
- **Section**: Section 7 — Results and Evaluation

---

## 13. Results

### Quantitative Evaluation (Section 7, PDF p. 2)
- **Resume Parsing Entity Extraction Accuracy**: **92%** accuracy in extracting structured entities (skills, qualifications, contact data) from unstructured resumes.
- **Job Recommendation Accuracy**: **88%** accuracy in recommending relevant job openings based on cosine similarity and ML classification.
- **Operational Feasibility**: Demonstrated end-to-end execution from raw PDF upload to ranked job cards within seconds on a lightweight web server.

### Qualitative Comparison with Commercial Systems (Section 3)
- *HireVue*: Focused on video; lacks detailed text-based skill extraction.
- *RChilli*: High accuracy but proprietary paid API with limited customization.
- *TextKernel*: Enterprise-grade but requires heavy institutional infrastructure.
- *Proposed System*: Open-source, customizable, lightweight full-stack implementation.

### Source Evidence
- **Page**: PDF pp. 1–2 (pp. a313–a314)
- **Section**: Section 3 (Literature Review Table) & Section 7 (Results and Evaluation)

---

## 14. Baselines

- Commercial ATS parsers (RChilli, TextKernel) and video interviewing platforms (HireVue) benchmarked conceptually in Section 3.
- Traditional manual recruitment screening by human HR personnel.

### Source Evidence
- **Page**: PDF pp. 1–2
- **Section**: Section 1 & Section 3

---

## 15. Ablation Study

- *Not reported* (Two-page applied systems conference paper focusing on overall pipeline accuracy).

---

## 16. Explainability

- The system outputs direct cosine similarity match percentages and highlights overlapping extracted skill keywords, providing transparent visibility into why a particular job was recommended over another.

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section 5 & Section 6

---

## 17. Main Findings

1. Open-source NLP libraries (spaCy, NLTK, PyPDF2) achieve competitive entity extraction accuracy (**92%**) on standardized resumes without requiring expensive commercial APIs (RChilli/TextKernel).
2. Combining TF-IDF / embeddings with cosine similarity provides a lightweight, scalable recommendation engine yielding **88% job relevance accuracy**.
3. A modular six-layer architecture deployed on Flask/Streamlit with MongoDB enables rapid candidate resume parsing and job matching.

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section 7 & Section 9 (Conclusion)

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Failure on Image-Based / Scanned Resumes**: The parser relies on text extraction libraries (PyPDF2); it completely fails on scanned, image-based, or non-selectable PDF resumes.
2. **Fragility on Non-Standard Layouts**: Struggles with complex multi-column, graphical, or unconventional resume layouts.
3. **Lexical Matching Limitations**: TF-IDF and basic embeddings occasionally miss nuanced semantic synonyms in niche technical domains.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The paper is an applied 2-page brief report; it lacks detailed confusion matrices, precision/recall per entity type (e.g., skill precision vs degree precision), or testing on multi-thousand candidate batches.

### Source Evidence
- **Page**: PDF p. 2 (p. a314)
- **Section**: Section 8 — Limitations and Future Work

---

## 19. Future Work

Explicitly proposed by the authors (Section 8, PDF p. 2):
1. Integrating Optical Character Recognition (OCR) using tools like Tesseract to support scanned and image-based resumes.
2. Deploying deep contextual language models (fine-tuned BERT / RoBERTa) for superior semantic understanding and cross-domain skill matching.
3. Enhancing user interface capabilities with real-time resume optimization tips.

### Source Evidence
- **Page**: PDF p. 2 (p. a314)
- **Section**: Section 8 — Limitations and Future Work

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides a clean, open-source architectural baseline for PRIE's **ATS Resume Analyzer**:
1. **Lightweight Baseline Validation**: Confirms that a standard spaCy + TF-IDF + Cosine Similarity pipeline achieves **92% entity extraction** and **88% recommendation relevance**, establishing a baseline for PRIE's more advanced hybrid parsers.
2. **Solving the Stated OCR Limitation**: Suryawanshi et al. explicitly identify their system's failure on scanned/image PDFs as their primary limitation; PRIE resolves this by incorporating OCR preprocessing (Tesseract / pdf2image) as an essential ingestion layer.
3. **Streamlit / Web Integration**: Validates the end-to-end integration of PDF text extraction, structured JSON caching, and job recommendation ranking in an interactive web application.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **System Scope** | "Resume Parsing and Job Recommendation System... automatically extract, analyze, and match candidate profiles with relevant job openings." | PDF p. 1, Abstract | Direct statement |
| **Parsing Accuracy** | "The resume parser achieved 92% accuracy in entity extraction." | PDF p. 2, Section 7 | Experimental result |
| **Recommendation Accuracy** | "recommender achieved 88% accuracy in job relevance." | PDF p. 2, Section 7 | Experimental result |
| **Software Stack** | Python, spaCy, PyPDF2, docx2txt, Scikit-learn, Flask/Streamlit, Firebase/MongoDB. | PDF pp. 1–2, Abstract & Section 6 | Technical specification |
| **Architecture Layers** | 6 layers: Input, Processing, Feature Extraction, Model, Recommendation, Database. | PDF p. 2, Section 4 | Architecture |
| **Stated Limitation** | "The system struggles with unstructured or image-based resumes. Future improvements include OCR integration." | PDF p. 2, Section 8 | Author limitation |

---

## 22. Verification Checklist

- [x] PDF read (`Paper36_mishra2025resume.pdf`, 2 pages)
- [x] Introduction inspected
- [x] Objectives verified (9 operational objectives in Section 2)
- [x] Methodology inspected (spaCy NER, PyPDF2, TF-IDF, Cosine Similarity, RF/LR)
- [x] Dataset verified (Kaggle Job Matching Dataset, PDF/DOCX resumes)
- [x] Features verified (Contact info, education, skills, experience, TF-IDF vectors)
- [x] Algorithms verified (spaCy NER, Cosine similarity, Random Forest, Logistic Regression)
- [x] Architecture inspected (6-layer architecture described in Section 4)
- [x] Results verified (92% entity extraction accuracy, 88% recommendation relevance accuracy)
- [x] Limitations verified (Struggles with image-based/scanned resumes and multi-column layouts)
- [x] Future work verified (OCR integration, BERT deep contextual embeddings)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact 92% parsing accuracy, 88% recommendation accuracy from Section 7, 6-layer architecture from Section 4, and 9 explicit objectives from Section 2 verified directly from source text; legacy filename discrepancy documented).
