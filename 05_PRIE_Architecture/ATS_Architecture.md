# ATS Architecture: 2D Spatial Layout Document Intelligence & Semantic Role Matching (M02)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/ATS_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative ATS Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & The Multi-Column Parsing Crisis

In campus placement recruitment, candidate resumes increasingly utilize non-standard, multi-column graphical templates (e.g., modern two-column sidebar resumes popular on Overleaf and Canva). 

As established in Phase 02 (`02_Cross_Analysis/ATS_Comparison.md`) and validated in Phase 03 (`03_Research_Problem/Gap_Validation.md` — `RG4`):
- **Literature Finding**: **Paper17** (Verma & Mehta 2026) and **Paper42** (Davenport et al. 2025) demonstrated that traditional ATS parsers relying on flat-text linear OCR streams suffer an error rate of **64.2%** on multi-column resumes.
- **Root Cause**: Flat OCR reads across the horizontal line regardless of vertical column gutters, concatenating unrelated text spans across adjacent columns into scrambled, nonsensical strings (e.g., interleaving project descriptions with skill keywords).
- **Recruitment Consequence**: Over 60% of well-qualified engineering candidates are falsely rejected before human recruiter review due to parsed token corruption.

PRIE resolves this vulnerability through a **2D Spatial Layout Document Intelligence Architecture** (`DD-004`, `M02`) combining `LayoutLMv3` spatial bounding box extraction with `Sentence-BERT` dense semantic matching.

---

## 2. ATS Subsystem Architectural Topology

```
[Candidate Multi-Column PDF Resume]
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│ 1. DOCUMENT PREPROCESSING & SPATIAL EXTRACTION         │
│ • PyMuPDF / Tesseract PDF Parsing                      │
│ • Extract Word Tokens, Fonts, & Visual Document Patches│
│ • Generate Normalized 2D Bounding Boxes [x0, y0, x1, y1│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. MULTIMODAL SPATIAL TOKEN CLASSIFICATION (LayoutLMv3)│
│ • Visual Patches (ResNet/ViT backbone)                 │
│ • Text Token Embeddings + 2D Spatial Position Embeddings│
│ • BIO Entity Tagger (Education, Skills, Experience,    │
│   Projects, Certifications)                            │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. STRUCTURED ENTITY RECONSTRUCTION & HYGIENE SCORING  │
│ • Reconstruct Logical Reading Order from Bounding Boxes│
│ • Compute F13: resume_ats_score (0.0–100.0)            │
│   (Layout parseability, section hygiene, font health)  │
└──────────────────────────┬─────────────────────────────┘
                           │ Structured Entity Text
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. DENSE SEMANTIC EMBEDDING & JD ALIGNMENT (SBERT)     │
│ • Sentence-BERT (all-MiniLM-L6-v2) 384d Bi-Encoder    │
│ • Vectorize Resume Competencies & Projects             │
│ • Cosine Dot Product against Target Job Description    │
│ • Compute F14: cosine_similarity (0.0–1.0)             │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ├─────────────────────────────┐
                           ▼                             ▼
              [Feature Outputs to M01]       [Visual UI Feedback Layer]
              • F13: resume_ats_score        • Bounding Box Highlighting
              • F14: cosine_similarity       • Scrambled Section Warnings
              • Extracted Skills -> M04      • Missing Keyword Suggestions
```

---

## 3. Detailed Processing Pipeline

### 3.1 Step 1: Document Preprocessing & Bounding Box Normalization
- Ingests native vector PDFs, Word documents (converted to PDF via LibreOffice headless), and scanned document images.
- PyMuPDF extracts text tokens, font sizes, and precise coordinates $[X_0, Y_0, X_1, Y_1]$ in points.
- Normalizes all bounding box coordinates to an integer grid $[0, 1000]$ relative to page width $W$ and height $H$:
  $$x_0 = \left\lfloor \frac{X_0}{W} \cdot 1000 \right\rfloor, \quad y_0 = \left\lfloor \frac{Y_0}{H} \cdot 1000 \right\rfloor, \quad x_1 = \left\lfloor \frac{X_1}{W} \cdot 1000 \right\rfloor, \quad y_1 = \left\lfloor \frac{Y_1}{H} \cdot 1000 \right\rfloor$$
- Renders page images at 150 DPI for visual patch embedding extraction.

### 3.2 Step 2: Multimodal LayoutLMv3 Inference
LayoutLMv3 represents each token $i$ as a fused embedding of three modalities:
$$\mathbf{e}_i = \mathbf{t}_i + \mathbf{p}_i^{\text{1D}} + \mathbf{p}_i^{\text{2D}} + \mathbf{v}_i$$
where:
- $\mathbf{t}_i$ is the WordPiece token embedding.
- $\mathbf{p}_i^{\text{1D}}$ is the sequential 1D reading order positional embedding.
- $\mathbf{p}_i^{\text{2D}}$ is the 2D spatial layout embedding combining $[x_0, y_0, x_1, y_1, w, h]$.
- $\mathbf{v}_i$ is the visual patch token embedding extracted by a linear projection layer.

**Token Classification Head**: Multi-layer perceptron classifying each token under the standard BIO (Beginning, Inside, Outside) entity tagging scheme across target classes:
- `B-SKILL` / `I-SKILL`: Technical languages, frameworks, developer tools.
- `B-EDU` / `I-EDU`: Degree, university name, graduation year, GPA.
- `B-EXP` / `I-EXP`: Company name, job title, employment dates, responsibilities.
- `B-PROJ` / `I-PROJ`: Project title, technologies used, architecture description.
- `B-CERT` / `I-CERT`: Professional industry certifications.

### 3.3 Step 3: Structural ATS Hygiene Scoring (`F13`)
The structural hygiene score $F_{13} \in [0.0, 100.0]$ is computed as a weighted heuristic evaluating document parseability:
$$F_{13} = 0.35 \cdot S_{\text{sections}} + 0.25 \cdot S_{\text{layout\_coherence}} + 0.20 \cdot S_{\text{font\_hygiene}} + 0.20 \cdot S_{\text{contact\_completeness}}$$
where:
- $S_{\text{sections}}$: Presence of all 4 standard sections (Education, Skills, Experience, Projects).
- $S_{\text{layout\_coherence}}$: Measure of bounding box overlap and margin consistency (penalizes chaotic text wrapping).
- $S_{\text{font\_hygiene}}$: Absence of unmapped glyphs, symbol fonts, or non-standard Unicode characters.
- $S_{\text{contact\_completeness}}$: Presence of verified email, LinkedIn URL, and GitHub handle.

### 3.4 Step 4: Dense Semantic Matching with Sentence-BERT (`F14`)
Traditional ATS keyword matchers fail on semantic synonyms (e.g., candidate lists "FastAPI" while JD specifies "Python REST API"). PRIE utilizes a Siamese Bi-Encoder:
1. Candidate profile text (extracted skills + project summaries) is encoded into a 384-dimensional dense vector:
   $$\mathbf{v}_{\text{cand}} = \text{SBERT}(\text{Candidate\_Summary}) \in \mathbb{R}^{384}$$
2. Target Job Description text is encoded:
   $$\mathbf{v}_{\text{jd}} = \text{SBERT}(\text{Job\_Description}) \in \mathbb{R}^{384}$$
3. Feature `F14: cosine_similarity` is computed as the normalized dot product:
   $$F_{14} = \frac{\mathbf{v}_{\text{cand}} \cdot \mathbf{v}_{\text{jd}}}{\|\mathbf{v}_{\text{cand}}\| \|\mathbf{v}_{\text{jd}}\|}$$

---

## 4. Architectural Boundaries & Data Privacy

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ARCHITECTURAL BOUNDARIES                        │
├───────────────────┬────────────────────────────────────────────────────┤
│ BOUNDARY          │ SPECIFICATION & IMPLEMENTATION                     │
├───────────────────┼────────────────────────────────────────────────────┤
│ Ingestion Gate    │ Upload endpoint validates PDF magic bytes, max 5MB.│
│ Document Storage  │ Encrypted on-premise storage; zero public S3 bucket│
│ Model Execution   │ Local ONNX FP16 runtime inside worker container;   │
│                   │ ZERO external cloud API forwarding (enforces DD-004│
│                   │ and student PII privacy).                          │
│ Privacy Redaction │ Candidate name, address, phone number, and gender  │
│                   │ are redacted prior to storing vectors in ChromaDB. │
└───────────────────┴────────────────────────────────────────────────────┘
```

---

## 5. Candidate Model Portfolio & Comparative Controls

In accordance with the Tripartite Standard (`Model_Selection_Justification.md`):

| Model Architecture | Role in PRIE | Literature Grounding | Engineering Rationale | Experimental Validation Target |
|:---|:---|:---|:---|:---|
| **LayoutLMv3 (Primary)** | Spatial Document Parsing | **Paper17, Paper42** | Preserves 2D bounding boxes; resolves multi-column text interleaving | Boundary-F1 $\ge 0.90$ on multi-column resumes (`EXP-1`) |
| **Sentence-BERT (Primary)** | Dense Semantic Matching | **Paper13, Paper35, Paper36** | Sub-20ms bi-encoder inference; pre-indexable in vector store | NDCG@10 $\ge 0.85$ against recruiter relevance rubric |
| **Tesseract + SpaCy (Baseline)**| Flat OCR Baseline | **Paper17** | Standard status-quo academic benchmark | Control to prove that 2D spatial models provide $\ge 15\%$ uplift |
| **TF-IDF / BM25 (Baseline)** | Sparse Keyword Baseline | **Paper35, Paper36** | Standard lexical recruitment baseline | Control to prove dense semantic superiority |

**Anti-Hallucination Rule**: Under no circumstances is LayoutLMv3 declared "the best ATS parser" without executing `EXP-1`. It is designated as the *Hypothesized Primary Candidate*.

---

## 6. Experimental Validation Plan Linkage

The ATS architecture is directly validated under **`EXP-1`** (`Experimental_Decisions.md`):
- **Hypothesis H1**: Multi-modal document intelligence models incorporating 2D spatial coordinates (LayoutLMv3) achieve a statistically significant improvement in entity extraction Boundary-F1 ($\ge 0.15$ uplift, $p < 0.01$) over flat-text NER on multi-column resumes.
- **Dataset**: Stratified benchmark corpus of 200 real student resumes (100 standard single-column, 100 complex multi-column) annotated by 3 independent human evaluators.
- **Statistical Falsification Test**: Paired two-tailed Student's t-test and Wilcoxon signed-rank test ($\alpha = 0.01$).
