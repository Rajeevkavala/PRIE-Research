# ATS Methodology: 2D Spatial Layout Intelligence, Multi-Column Parsing & Semantic Skill Matching

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/ATS_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative ATS Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. The Multi-Column Layout Destruction Crisis (`RG4`)

Campus recruitment Applicant Tracking Systems (ATS) predominantly rely on flat-text sequential parsers or regular expressions (`Paper11`, `Paper12`, `Paper17`). When presented with modern multi-column resumes (used by $>60\%$ of technical students), these parsers read horizontally across columns, interleaving unrelated text lines:

```
[Visual Two-Column Resume Layout]
Left Column: Technical Skills             Right Column: Work Experience
- Python, Docker, Kubernetes              - Software Intern at TechCorp
- PostgreSQL, Redis                       - Built microservices in Go

[Catastrophic Flat-Text OCR Output]
"Python, Docker, Kubernetes Software Intern at TechCorp PostgreSQL, Redis Built microservices in Go"
```
This layout scrambling causes regex extractors to miss skills, misattribute project dates, and generate false-negative candidate rejections ($55\%–68\%$ rejection rate).

---

## 2. LayoutLMv3 Spatial Document Intelligence Architecture

PRIE resolves `RG4` via vision-language multimodal spatial transformers (`DD-004`, `M02`, `EXP-1`):

```
[Resume PDF Upload] ──► Render 300 DPI Image ──► Tesseract OCR (Word Tokens + Bounding Boxes)
                                                                 │
                                                                 ▼
                                                Normalize Coordinates [0, 1000]
                                                                 │
                                                                 ▼
                                            LayoutLMv3 Multimodal Spatial Transformer
                                            [Text Embeddings + 2D Spatial + Visual Patches]
                                                                 │
                                                                 ▼
                                            Sequence BIO Entity Classification Head
                                            [B-SKILL, I-SKILL, B-EXP, B-EDU, B-PROJ]
                                                                 │
                                                                 ▼
                                            Structured Candidate Profile Dictionary
                                            (Skills, Experience Months, Projects, Certs)
```

---

## 3. Semantic Skill Matching & Gap Quantification

Extracted skills are matched against target corporate Job Descriptions (JDs) via a two-tier semantic pipeline:

### 3.1 Exact & Taxonomy Alias Matching
Extracted text spans are normalized against the ESCO/O*NET skill taxonomy using Levenshtein string distance ($\text{dist} \le 1$) and alias lookup dictionaries (e.g., `k8s` $\to$ `Kubernetes`, `react.js` $\to$ `React`).

### 3.2 Dense Semantic Vector Matching via Sentence-BERT
For descriptive project bullets and unlisted technical competencies, dense embeddings are computed using `all-MiniLM-L6-v2`:
$$\mathbf{e}_{\text{resume}} = \text{S-BERT}(\text{Resume Text}), \quad \mathbf{e}_{\text{jd}} = \text{S-BERT}(\text{Job Description})$$
$$\text{cosine\_similarity} = \frac{\mathbf{e}_{\text{resume}} \cdot \mathbf{e}_{\text{jd}}}{\|\mathbf{e}_{\text{resume}}\|_2 \|\mathbf{e}_{\text{jd}}\|_2} \in [0.0, 1.0]$$

---

## 4. ATS Evaluation Protocol & Metrics

To evaluate ATS accuracy scientifically in `EXP-1`:
- **Boundary-F1 Score**: Measures exact span boundary recognition for multi-word technical skills (e.g., recognizing `Apache Spark Streaming` as a single unit rather than three disjoint tokens).
- **Macro-Precision & Recall**: Evaluated across single-column, two-column, and non-standard resume strata in `DS-CORPUS-01`.
