# RAG Methodology: Two-Stage Curriculum Retrieval, ChromaDB & RAG Triad Runtime Guards

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/RAG_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative RAG Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Two-Stage Retrieval Architecture (`DD-007`, `M09`)

To provide factually grounded learning assistance without hallucinations:

```
[Student Query / Skill Deficit Context]
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1: DENSE BI-ENCODER RETRIEVAL (CHROMADB)              │
│ • Model: all-MiniLM-L6-v2 (384-dimensional dense vectors)   │
│ • Corpus: 450+ accredited CS textbook & lecture modules     │
│ • Candidate Extraction: Top-K = 20 candidate text chunks    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 2: CROSS-ENCODER RERANKING                            │
│ • Model: ms-marco-MiniLM-L-6-v2 Cross-Encoder               │
│ • Full query-document token self-attention scoring          │
│ • Refined Candidate Set: Top-N = 3 highest-ranking chunks   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ STAGE 3: RUNTIME RAG TRIAD VERIFICATION GUARD               │
│ • Context Relevance >= 0.85                                 │
│ • Groundedness >= 0.90                                      │
│ • Answer Relevance >= 0.88                                  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
                Validated Grounded Output
```

---

## 2. Runtime RAG Triad Verification Metrics

> [!CAUTION]
> **SCIENTIFIC GUARDRAIL: RAG DOES NOT GUARANTEE 100% FACTUALITY**  
> While RAG substantially mitigates hallucinations, it does not mathematically guarantee complete factual correctness. PRIE enforces automated runtime gating using the RAG Triad:

1. **Context Relevance ($\mathcal{S}_{\text{CR}}$)**: Evaluates whether retrieved chunks contain information strictly relevant to the query:
   $$\mathcal{S}_{\text{CR}} = \text{Sim}\Big( \text{Query}, \text{Retrieved Chunks} \Big) \ge 0.85$$
2. **Groundedness ($\mathcal{S}_{\text{ground}}$)**: Measures the extent to which every claim in the generated response can be traced directly to sentences in the retrieved context:
   $$\mathcal{S}_{\text{ground}} = \frac{\text{Verifiable Claims in Response}}{\text{Total Claims in Response}} \ge 0.90$$
3. **Answer Relevance ($\mathcal{S}_{\text{AR}}$)**: Measures whether the generated answer directly addresses the student's question without extraneous digression ($\mathcal{S}_{\text{AR}} \ge 0.88$).

If any score breaches threshold, the system suppresses the generated answer and serves the raw verified textbook chunk with a human tutor escalation flag.
