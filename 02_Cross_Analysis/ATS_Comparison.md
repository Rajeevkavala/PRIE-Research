# ATS & Resume Intelligence Comparison

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/ATS_Comparison.md`  
**Status**: Authoritative ATS Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. The Resume Intelligence Paradigm

Applicant Tracking Systems (ATS) and automated resume screening engines represent critical gatekeepers in campus recruitment and enterprise hiring. Across the 44 verified papers, seven (7) primary studies investigate resume intelligence, spanning lexical parsing, semantic embedding alignment, implicit skill discovery, and layout-invariant document processing:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         RESUME INTELLIGENCE PARADIGMS                            │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Paradigm                      │ Representative Studies & Technologies            │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Lexical & Keyword Matching │ P11 (Mishra, 2025), P37 (JayaPriya et al., 2025) │
│                               │ TF-IDF, NLTK, CountVectorizer, Regex scrapers.   │
│ 2. Named Entity Recognition   │ P04 (Kazi, 2025), P12 (Kashif, 2024), P36 (2025) │
│                               │ Custom spaCy token pipelines, BIO entity tags.   │
│ 3. Dense Semantic Bi-Encoders │ P12 (Kashif & Kumar, 2024), P17 (Solanki, 2026)  │
│                               │ Sentence-BERT (all-MiniLM-L6-v2), Cosine Space.  │
│ 4. Hybrid Lexical-Dense Fusion│ P17 (Solanki et al., 2026 ResuMatch)             │
│                               │ Dense SBERT + Sparse BM25 + Reciprocal Rank.     │
│ 5. Implicit Skill Mining      │ P35 (Gugnani & Misra, 2020)                      │
│                               │ Distributed Memory Doc2Vec (PV-DM), Skill Graphs.│
│ 6. Cognitive Document Vision  │ P42 (Kapula, 2025)                               │
│                               │ LayoutLMv3 multimodal transformer, TrOCR, OCR.   │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master ATS Cross-System Benchmark Matrix

The table below provides a comprehensive architectural and empirical comparison across all resume intelligence systems in the corpus:

| Paper ID & System | Document Extraction Engine | Skill & Entity Extraction | Semantic Matching Model | Tested Dataset / Resumes | Entity F1 / Extraction Acc | Screening Precision / MRR | Multi-Column Layout Tolerance | Parsing Latency |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **P11** (Mishra, 2025) | BeautifulSoup / PyPDF2 | Regex + Tokenizer | TF-IDF Cosine Similarity | 500 Resumes, 1,200 JDs | 84.5% Precision | r = 0.81 (Ranking Corr) | **Fails** (Linear flow break) | ~1.20s |
| **P12** (Kashif & Kumar, 2024) | pdfminer.six | Custom spaCy NER | SBERT (`all-MiniLM-L6-v2`) | 1,200 Resumes (Kaggle) | 88.4% Entity F1 | Precision: 91.3%, F1: 0.894 | **Poor** (Text interleaving) | ~0.45s |
| **P17** (Solanki et al., 2026) | PyMuPDF (fitz) | spaCy + Section Rules | Dual-Encoder SBERT + BM25 | 2,500 Resumes, 800 JDs | 90.2% Section Acc | **MRR@10: 0.92, Top-5: 89.4%** | **Moderate** (Section heuristic)| **~0.04s (40ms)** |
| **P35** (Gugnani & Misra, 2020)| Text Scraper | Project Text Tokenizer | Doc2Vec (PV-DM) Cosine | 4,500 Resumes, 12,000 Projs | Unsupervised Cluster | Recall: 86.7% (Implicit) | Not Evaluated (Raw text) | ~0.60s |
| **P36** (Suryawanshi, 2025) | PyMuPDF | Custom Rule Pipeline | Exact & Fuzzy Keyword Overlap| 650 Resumes, 120 Job Roles | 87.5% Section Acc | Match Score (Fuzzy overlap) | **Fails** on tabular CVs | ~0.85s |
| **P37** (JayaPriya et al., 2025)| Python-docx / PyPDF2 | NLTK Lemmatizer | Scikit-Learn TF-IDF Cosine | 800 Resumes, 200 JDs | 81.2% Keyword Acc | Accuracy: 83.2%, F1: 0.794 | **Fails** on multi-column | ~1.10s |
| **P42** (Kapula, 2025 IDP) | **LayoutLMv3 + Tesseract OCR**| **Multimodal Visual Tokenizer**| Spatial Coordinate Bounding | 10,000 Multi-Column Resumes | **Entity F1: 0.948, Acc: 98.2%**| **Layout Tolerance: 98.2%** | **State-of-the-Art (Spatial)**| ~1.50s (GPU) |

---

## 3. Critical Engineering Debates & Architectural Findings

### 3.1 The Multi-Column Layout Destruction Problem
- `[CROSS-PAPER OBSERVATION]` Over 65% of modern professional resumes utilize two-column or multi-column visual layouts (e.g., contact info and skills on the left column, work experience and projects on the right).
- `[AUTHOR-STATED LIMITATION]` Standard linear text extraction libraries (PyPDF2 in P11/P37, pdfminer in P12) read PDF text streams horizontally across the entire page width. Consequently, they interleave the left-column skills directly into the right-column project descriptions, completely destroying sentence syntax and causing spaCy NER to drop entity extraction F1 by over 34%.
- `[AUTHOR-STATED FACT]` Kapula (P42) solved this spatial destruction by deploying **LayoutLMv3**, which jointly embeds 2D visual bounding boxes, typography font sizes, and textual tokens. LayoutLMv3 achieved an **Entity F1 of 0.948** and a **98.2% layout boundary tolerance**, representing a 32% error reduction over standard text scrapers.

### 3.2 Semantic Mismatch: Lexical TF-IDF vs Dense SBERT Bi-Encoders
- `[CROSS-PAPER OBSERVATION]` Lexical ATS matchers (P11, P37) penalize candidates severely for minor vocabulary differences (e.g., candidate lists "PostgreSQL", but JD specifies "Relational Databases"; candidate lists "React", JD specifies "Frontend Web Frameworks").
- `[AUTHOR-STATED FACT]` Kashif & Kumar (P12) and Solanki et al. (P17) demonstrated that mapping resumes into 384-dimensional dense semantic spaces using **Sentence-BERT (`all-MiniLM-L6-v2`)** boosts retrieval precision from 74.5% (TF-IDF) to **91.3%**, successfully capturing conceptual synonyms.
- `[AUTHOR-STATED FACT]` Solanki et al. (P17) further demonstrated that pure semantic search occasionally misses critical exact requirements (e.g., "5+ years experience" or specific certification acronyms like "AWS-SAA"). Combining dense SBERT with sparse BM25 lexical ranking via **Reciprocal Rank Fusion (RRF)** achieved the corpus-highest **MRR@10 of 0.92**.

### 3.3 Implicit Skill Discovery (Doc2Vec in P35)
- `[AUTHOR-STATED FACT]` Gugnani & Misra (P35) uncovered that candidates frequently omit foundational skills from their explicit skill lists (e.g., writing "Built distributed microservices with Kubernetes and Helm" without explicitly listing "Docker" or "Linux"). By training a **Distributed Memory Doc2Vec (PV-DM)** model on 12,000 project descriptions, their system uncovered unstated implicit competencies with **86.7% recall**.

---

## 4. ScholarCamp / PRIE Comprehensive ATS Architecture

To establish an enterprise-grade, open-source ATS engine, ScholarCamp / PRIE synthesizes the best findings from P12, P17, P35, and P42:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         PRIE MULTI-STAGE ATS PIPELINE                            │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ Stage 1: Document OCR    │ LayoutLMv3 spatial vision-language parser (P42)       │
│ & Layout Normalization   │ to extract multi-column text without flow corruption. │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Stage 2: Entity & Skill  │ Fine-tuned spaCy NER pipeline (P12) +                 │
│ Extraction               │ Doc2Vec implicit competency inference (P35).         │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Stage 3: Hybrid Semantic │ Dual-Encoder SBERT (`all-MiniLM-L6-v2`) +             │
│ Match Scoring            │ BM25 sparse keyword index combined via RRF (P17).     │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Stage 4: Prescriptive    │ Section-by-section gap visualizer (P36) generating    │
│ Feedback Generation      │ explicit candidate recommendations for missing skills.│
└──────────────────────────┴───────────────────────────────────────────────────────┘
```
