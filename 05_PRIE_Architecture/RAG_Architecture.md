# RAG Architecture: Two-Stage Curriculum Retrieval & RAG Triad Verification (M09)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/RAG_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative RAG Subsystem Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & Educational Hallucination Mitigation

In higher education career preparation, unconstrained large language models (LLMs) frequently hallucinate:
1. Fabricating non-existent college syllabus policies, eligibility regulations, or course credits.
2. Generating generic, ungrounded technical study advice detached from the specific institutional curriculum.
3. Suggesting outdated programming libraries or non-standard syntax for university programming laboratory exams.

As established in Phase 02 (`02_Cross_Analysis/RAG_Comparison.md`) and validated in Phase 03 (`03_Research_Problem/Gap_Validation.md` — `RG8`):
- Single-stage vector search retrieves noisy or tangentially relevant document chunks that pollute LLM context windows.
- Unconstrained prompting lacks runtime factual verification.

PRIE addresses this vulnerability through a **Two-Stage Curriculum RAG Architecture with Runtime RAG Triad Verification** (`DD-007`, `M09`), grounding all generative advising directly in verified institutional syllabi and corporate recruitment archives.

---

## 2. RAG Subsystem Pipeline Topology

```
[Verified Institutional Syllabi & Past Placement Drive Archives]
                               │
                               ▼
┌────────────────────────────────────────────────────────┐
│ 1. DOCUMENT INGESTION & HIERARCHICAL CHUNKING          │
│ • Markdown / PDF Parser preserving section hierarchy   │
│ • Semantic Chunking: 512 tokens with 64-token overlap │
│ • Metadata Attachment: Subject, Topic, Semester, Source│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. DENSE EMBEDDING & VECTOR STORAGE (ChromaDB)         │
│ • Sentence-BERT (all-MiniLM-L6-v2) 384d Dense Embeddings│
│ • HNSW Hierarchical Navigable Small World Indexing     │
└──────────────────────────┬─────────────────────────────┘
                           │
       [Student Query: "What are the core deadlock conditions in OS?"]
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. STAGE 1 RETRIEVAL: DENSE VECTOR SEARCH              │
│ • Computes Cosine Similarity dot product in ChromaDB   │
│ • Retrieves Top-20 Candidate Chunks (High Recall)      │
└──────────────────────────┬─────────────────────────────┘
                           │ Top-20 Chunks
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. STAGE 2 RERANKING: CROSS-ENCODER                    │
│ • ms-marco-MiniLM-L-6-v2 Cross-Encoder Transformer     │
│ • Evaluates Query-Chunk Cross-Attention Pairs          │
│ • Filters Noise -> Selects Top-4 High-Precision Chunks │
└──────────────────────────┬─────────────────────────────┘
                           │ Top-4 Reranked Chunks
                           ▼
┌────────────────────────────────────────────────────────┐
│ 5. CONTEXT AUGMENTATION & LOCAL SLM GENERATION         │
│ • Constructs Grounded Prompt with System Guardrails    │
│ • Dispatches to Local Quantized Llama-3-8B-Instruct    │
│ • Synthesizes Answer with Inline Citation References   │
└──────────────────────────┬─────────────────────────────┘
                           │ Draft Answer + Citations
                           ▼
┌────────────────────────────────────────────────────────┐
│ 6. RUNTIME RAG TRIAD FACTUAL VERIFICATION GUARD        │
│ • Context Relevance Checker: Is context relevant? >=.85│
│ • Groundedness Checker: Is answer in context? >= .90   │
│ • Answer Relevance Checker: Does it answer query? >=.88│
└──────────────────────────┬─────────────────────────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
       [TRIAD: PASS]               [TRIAD: FAIL]
             │                           │
  Dispatch Grounded Answer      Block Generation / Regenerate
  with Clickable Citations      Fallback: "Topic not found in
  to Student Interface          verified syllabus archives."
```

---

## 3. Two-Stage Retrieval Mechanics

### 3.1 Stage 1: Dense Vector Retrieval (High Recall)
- **Embedding Model**: `Sentence-BERT (all-MiniLM-L6-v2)` computes 384-dimensional dense vectors:
  $$\mathbf{e}_q = \text{SBERT}(\text{Query}), \quad \mathbf{e}_d = \text{SBERT}(\text{Chunk}_d)$$
- **Index Structure**: ChromaDB utilizes HNSW (Hierarchical Navigable Small World) graph indexing with cosine distance metric.
- **Recall Target**: Retrieves Top-$K_1 = 20$ chunks within $<15$ms.

### 3.2 Stage 2: Cross-Encoder Reranking (High Precision)
- Bi-encoders compress entire chunks into single fixed-size vectors, losing fine-grained cross-token token interactions.
- PRIE introduces a second-stage Cross-Encoder (`cross-encoder/ms-marco-MiniLM-L-6-v2`):
  $$s(q, d) = \text{Softmax}\Big(\text{CrossEncoder}([\text{CLS}] \circ q \circ [\text{SEP}] \circ d)\Big)$$
- Evaluates full cross-attention across all query and chunk tokens simultaneously.
- Ranks candidate chunks and selects Top-$K_2 = 4$ chunks, discarding irrelevant background text.
- **Latency Overhead**: Adds 40–70ms reranking latency on CPU, yielding a $>24\%$ boost in contextual precision (**Paper20**).

---

## 4. Runtime RAG Triad Verification Guard

In strict adherence to **`DD-007`**, every synthesized generative response must pass an automated three-dimensional runtime verification check before transmission to the student:

```
                          ┌───────────────────────────┐
                          │   STUDENT USER QUERY (Q)  │
                          └──────┬─────────────┬──────┘
                                 │             │
                Context Relevance│             │Answer Relevance
                     (>= 0.85)   │             │   (>= 0.88)
                                 ▼             ▼
                     ┌───────────────┐     ┌───────────────┐
                     │ RETRIEVED     │────►│ GENERATED     │
                     │ CONTEXT (C)   │     │ ANSWER (A)    │
                     └───────────────┘     └───────────────┘
                                     Groundedness
                                      (>= 0.90)
```

1. **Context Relevance ($\text{CR} \ge 0.85$)**:
   - Quantifies whether the retrieved document chunks contain only information directly relevant to the user query without irrelevant tangential noise.
2. **Groundedness ($\text{GR} \ge 0.90$)**:
   - Assesses whether every factual claim in the generated answer $\mathcal{A}$ can be strictly traced back to and deduced from the retrieved context $\mathcal{C}$.
   - **Zero Hallucination Tolerance**: If the LLM asserts a claim absent from the retrieved chunks, Groundedness drops below $0.90$, triggering an immediate rejection.
3. **Answer Relevance ($\text{AR} \ge 0.88$)**:
   - Verifies that the generated response directly answers the specific technical query posed by the student without evasion or irrelevant filler.

---

## 5. Architectural Guardrails & Scientific Honesty

- **Anti-Hallucination Rule**: PRIE explicitly acknowledges that **RAG does not eliminate hallucination 100%**. Rather, RAG establishes a bounded, verifiable retrieval envelope guarded by automated Triad verification.
- **Explicit Fallback Protocol**: If no retrieved chunk exceeds a cosine similarity threshold of $0.70$, or if the Groundedness score fails ($<0.90$), PRIE aborts generation and returns:
  > *"This query cannot be verified against the official university curriculum or placement drive archives. Please consult your course instructor or syllabus guidelines."*
- **Strict Citation Requirement**: Every generated answer must append clickable source anchors: `[Ref: Operating Systems Syllabus, Section 4.2, p. 18]`.
