# Retrieval-Augmented Generation (RAG) Comparison & Synthesis

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/RAG_Comparison.md`  
**Status**: Authoritative RAG Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. RAG in Educational & Campus Systems

Large Language Models deployed in academic environments suffer from factual hallucination, lack of syllabus grounding, and inability to access localized campus regulations. Retrieval-Augmented Generation (RAG) solves these vulnerabilities by dynamically retrieving authoritative institutional documents to condition LLM generation. Across the 44 verified papers, four (4) primary studies investigate RAG:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            EDUCATIONAL RAG PARADIGMS                             │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Paradigm                      │ Representative Studies & Systems                 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Systematic Survey & Triad  │ P20 (Swacha & Gracel, 2025)                      │
│                               │ Review of 72 educational RAG implementations;    │
│                               │ RAG Triad benchmark framework.                   │
│ 2. Localized Private RAG      │ P21 (Nisanth et al., 2025)                       │
│                               │ Offline 4-bit LLaMA-3-8B + ChromaDB; zero cloud. │
│ 3. Multimodal Contextual RAG  │ P23 (Venkatesh et al., 2025)                     │
│                               │ Gemini 1.5 Pro + FAISS + Cross-Encoder re-ranker.│
│ 4. Technology Acceptance (TAM)│ P40 (Murti et al., 2025)                         │
│                               │ Structural Equation Modeling of student adoption.│
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master Educational RAG Benchmark Matrix

The table below benchmarks the primary RAG architectures across the corpus on ingestion, chunking, retrieval, generation, evaluation metrics, and institutional adoption:

| Dimension | P20 (Swacha & Gracel, 2025) | P21 (Nisanth et al., 2025) | P23 (Venkatesh et al., 2025) | P40 (Murti et al., 2025) |
|:---|:---|:---|:---|:---|
| **System Classification** | Meta-Survey (72 Studies) | Local Offline Campus Tutor | Multimodal Academic Advisor | Empirical Student TAM Study |
| **Ingested Knowledge Base**| Standardized Curricula & QA | 15 CS Syllabi, 45 Textbooks | 2,000 Transcripts, 500 Slides | University Course Materials |
| **Chunking Protocol** | 256–512 Tokens (Survey Consensus)| 512 Tokens (50-token overlap) | Semantic Section-Aware Window | Curricular Unit-Based Chunks |
| **Vector Embedding Model** | Dense Bi-Encoders (BGE, SBERT) | BAAI BGE-small-en-v1.5 | Google Vertex Embedding Text | Standard Pre-trained Embeddings |
| **Vector Database Engine** | ChromaDB, FAISS, Milvus | **ChromaDB (Local On-Disk)** | **FAISS (GPU In-Memory)** | In-Memory Vector Store |
| **Re-Ranking Architecture**| Cross-Encoder (MS-MARCO) | None (Pure dense cosine) | **Cohere Cross-Encoder Re-ranker**| None |
| **Generation Model (LLM)** | GPT-3.5, LLaMA-2/3, Mistral | **LLaMA-3-8B-Instruct (4-bit AWQ)**| **Google Gemini 1.5 Pro** | University Hosted LLM |
| **Execution Environment** | Mixed Cloud & Edge | Local Consumer GPU (RTX 4060) | Cloud API (Google Cloud) | University Cloud Cluster |
| **Evaluated Metrics** | Hallucination Rate, RAG Triad | Faithfulness: 89.2%, Relevancy: 86.4%| Factual Precision: 92.8%, ROUGE: 0.74| Perceived Usefulness ($\beta=0.68$) |
| **Inference Latency** | Variable (1.5s–6.0s) | 1.8 seconds per answer | 2.2 seconds per answer | ~2.5 seconds |
| **Student Privacy / FERPA**| Identified as Major Barrier | **100% On-Premise Data Isolation**| Cloud Transmission Required | University Governed |

---

## 3. Critical Methodological Findings & System Insights

### 3.1 The RAG Triad as Educational Evaluation Standard (P20)
- `[AUTHOR-STATED FACT]` Swacha & Gracel (P20) synthesized 72 studies to establish that standard NLP metrics (BLEU, ROUGE) are fundamentally inadequate for evaluating educational RAG. They advocate for the **RAG Triad**:
  1. **Context Relevance**: Is the retrieved curriculum snippet pertinent to the student's question?
  2. **Groundedness / Faithfulness**: Is every statement in the LLM's response directly supported by the retrieved chunk without hallucinated external knowledge?
  3. **Answer Relevance**: Does the final response directly answer the student's query without verbose digressions?
- `[AUTHOR-STATED FACT]` Across surveyed systems, adopting a verified RAG architecture reduced educational hallucination rates from **34% (zero-shot LLM)** to **under 4.5%**.

### 3.2 The Privacy & Cost Breakthrough of Quantized Local RAG (P21)
- `[AUTHOR-STATED FACT]` Nisanth et al. (P21) proved that deploying **LLaMA-3-8B quantized to 4-bit AWQ** on a single consumer GPU (RTX 4060, 8GB VRAM) paired with **ChromaDB** achieved **89.2% faithfulness** and **86.4% answer relevancy**.
- `[CROSS-PAPER OBSERVATION]` This proves that university departments do not need thousands of dollars in cloud API credits to deploy private, offline, FERPA-compliant course assistants.

### 3.3 The Necessity of Cross-Encoder Re-Ranking (P23)
- `[AUTHOR-STATED FACT]` Venkatesh et al. (P23) demonstrated that initial bi-encoder vector search retrieves relevant paragraphs in the top-10, but frequently places the exact answer snippet at positions 4 to 8. Inserting a secondary **Cross-Encoder Re-ranker** to score query-document pairs elevated factual retrieval precision by **14.6%**, achieving **92.8% factual precision**.

### 3.4 Student Adoption Drivers: Trust and Usefulness (Murti et al., 2025)
- `[AUTHOR-STATED FACT]` Through Structural Equation Modeling on 320 university students, Murti et al. (P40) demonstrated that **Perceived Usefulness ($\beta=0.68$, $p<0.001$)** and **Trust ($\beta=-0.42$ on anxiety)** are the primary determinants of student adoption. If a bot hallucinates even once during exam preparation, student trust drops precipitously, leading to platform abandonment.

---

## 4. ScholarCamp / PRIE Contextual RAG Architecture

ScholarCamp / PRIE combines the offline privacy of P21 with the re-ranking precision of P23:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           PRIE CONTEXTUAL RAG ASSISTANT                          │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ Pipeline Stage           │ Implementation & Literature Grounding                 │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 1. Document Chunking     │ Semantic section-aware chunking (384 tokens with      │
│                          │ 40-token overlap) over university course syllabi.     │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 2. Dense Vector Index    │ ChromaDB local vector store indexed with              │
│                          │ BAAI BGE-small-en-v1.5 dense embeddings (P21).        │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 3. Cross-Encoder Ranker  │ Cohere / MS-MARCO Cross-Encoder re-ranking the        │
│                          │ top-15 retrieved chunks to isolate top-3 context (P23)│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 4. Grounded Generation   │ LLaMA-3-8B-Instruct (4-bit local) with strict prompt: │
│                          │ "Answer in $\le$3 sentences using ONLY provided context"│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 5. Automated RAG Triad   │ Continuous logging and monitoring of Faithfulness and │
│    Audit Monitoring      │ Answer Relevancy scores before student display (P20).  │
└──────────────────────────┴───────────────────────────────────────────────────────┘
```
