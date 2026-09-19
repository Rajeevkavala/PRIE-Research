# Paper 21 — RAG-Based AI Chatbot for Student and Institutional Assistance

## 1. Bibliographic Information

- **Paper ID**: Paper21
- **Full Title**: RAG-Based AI Chatbot for Student and Institutional Assistance
- **Authors**: Nisanth P, Arohan A R, Adhithyan P C, Muhammed Suhail, Shahzad Bin Muhammed, and Linsa V U
- **Institution**: Department of Artificial Intelligence and Machine Learning, Vidya Academy of Science and Technology, Thrissur, Kerala, India
- **Year**: 2025 (Published: September 2025)
- **Venue**: International Journal for Research in Applied Science & Engineering Technology (IJRASET), Vol. 13, Issue IX, pp. 858–865
- **ISSN**: 2321-9653
- **DOI**: 10.22214/ijraset.2025.73970
- **PDF filename**: `Paper21_chawla2025rag.pdf`
- **PDF path**: `Papers/PDFs/Paper21_chawla2025rag.pdf`
- **Page count**: 8 pages (pp. 858–865)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper21_chawla2025rag.bib`) listed synthetic authors ("Chawla, Divya and Saxena, Rohit"). Inspection of the actual PDF confirms the true authors are Nisanth P, Arohan A R, Adhithyan P C, Muhammed Suhail, Shahzad Bin Muhammed, and Linsa V U from Vidya Academy of Science and Technology, Thrissur.

---

## 2. Research Problem

Higher education institutions face persistent challenges in delivering responsive, accurate student support. Frontline administrative offices are burdened with continuous queries regarding admissions, fees, academic calendars, syllabi, and campus regulations. Generic foundation Large Language Models (LLMs) hallucinate plausible but factually incorrect policies and lack access to confidential, private, or frequently updated institutional documentation. Existing commercial cloud-based conversational tools often pose data privacy and recurring API cost concerns, creating a critical need for an open-source, on-premise, privacy-preserving conversational agent strictly grounded in verified institutional records.

### Source Evidence
- **PDF Page**: Page 2 (p. 858), Section I "INTRODUCTION" & Page 3 (p. 859).

---

## 3. Research Objectives

1. Develop a locally hosted, privacy-preserving Retrieval-Augmented Generation (RAG) chatbot for institutional assistance in higher education.
2. Formulate an end-to-end multi-format document ingestion pipeline handling PDF and tabular Excel university files.
3. Integrate dense semantic vector indexing using `nomic-embed-text` and local `ChromaDB`.
4. Implement a two-tier retrieval architecture featuring a **Sentence Transformers Cross-Encoder** to re-rank candidate context passages prior to generation.
5. Deploy a local open-weight language model (**Gemma 3:4B**) via **Ollama** within an interactive **Streamlit** user interface supporting streaming token delivery.

### Source Evidence
- **PDF Page**: Pages 2–3 (pp. 858–859), Section I; Pages 6–7 (pp. 862–863), Sections V & VI.

---

## 4. Research Questions

Not explicitly stated in question format. Structured around system architecture goals:
- Can an entirely local, open-source RAG stack (Ollama + Gemma + ChromaDB) eliminate hallucinations regarding college policies without leaking student data to commercial clouds?
- Does integrating a Cross-Encoder re-ranking stage measurably improve the contextual relevance of retrieved passages over single-stage vector similarity?

---

## 5. Dataset / Document Knowledge Base

- **Knowledge Base Source**: Real collegiate administrative and academic documents from Vidya Academy of Science and Technology, Thrissur.
- **File Modalities Supported**: Unstructured text / PDF circulars, course catalogs, academic handbooks, and structured tabular Excel spreadsheets (e.g., fee schedules, faculty directories).
- **Document Processing**: Chunking into semantic segments with metadata tagging (filename, section).

### Source Evidence
- **PDF Page**: Pages 4–6 (pp. 860–862), Section IV "SYSTEM ARCHITECTURE" & Section V "IMPLEMENTATION".

---

## 6. Features & System Pipeline

### Ingestion & Processing Pipeline
- Document upload handler (PDF / Excel file parser).
- Recursive character text chunking with token overlap.
- Dense semantic vector embeddings.

### Retrieval & Re-ranking Attributes
- Vector-space cosine distance scores from ChromaDB.
- Cross-Encoder relevance probability scores.
- Query intent tokens and contextual prompt injection.

### Generation Attributes
- System instructions constraining responses strictly to retrieved passages.
- Fallback messaging when retrieved context does not contain sufficient factual evidence.

### Source Evidence
- **PDF Page**: Pages 4–6 (pp. 860–862), Section IV.

---

## 7. Data Preprocessing

1. **Document Parsing**: Reading PDF binaries and Excel sheets, converting raw content into clean textual strings.
2. **Chunk Partitioning**: Splitting extended documents into discrete passages to conform to embedding and LLM context windows.
3. **Embedding Vectorization**: Passing text chunks through the `nomic-embed-text` model running locally inside Ollama.
4. **Vector Database Persistence**: Writing embedding vectors and associated text chunks into local `ChromaDB` collections.

### Source Evidence
- **PDF Page**: Pages 5–6 (pp. 861–862), Section IV & V.

---

## 8. Algorithms and Models

### 1. Embedding Model
- **`nomic-embed-text`**: High-performance, open-weights text embedding model executed locally via Ollama.

### 2. Vector Indexing Engine
- **ChromaDB**: Lightweight, local vector store performing approximate nearest neighbor (ANN) similarity search.

### 3. Re-Ranking Model
- **Sentence Transformers Cross-Encoder (`cross-encoder/ms-marco-MiniLM-L-6-v2`)**: Evaluates query-passage pairs jointly to compute deep interaction relevance scores, filtering out irrelevant top-$k$ vector matches before LLM injection.

### 4. Generative Language Model
- **Gemma 3:4B**: Google's lightweight open-weights instruction-tuned model, served entirely on-premise via Ollama.

### Source Evidence
- **PDF Page**: Pages 3, 5, 6, and 7 (pp. 859, 861–863), Sections II, IV, V, VI.

---

## 9. Architecture

The system utilizes a fully local, cloud-independent architecture (Figure on PDF p. 5):
1. **User Interface Layer**: Built with **Streamlit**, providing document upload widgets, ingestion status indicators, query input boxes, and token streaming output.
2. **Local Model Server**: **Ollama** managing local CPU/GPU execution of `nomic-embed-text` and `Gemma 3:4B`.
3. **Vector Database**: Embedded **ChromaDB** storing persistent vector representations of processed college catalogs.
4. **Two-Stage Retrieval Pipeline**:
   - *Stage 1 (Coarse Retrieval)*: ChromaDB fetches top-$k$ nearest neighbors via vector distance.
   - *Stage 2 (Fine Re-ranking)*: Cross-Encoder scores and re-orders passages, pruning irrelevant context.
5. **Grounded Generation Core**: Gemma 3:4B receives the user query augmented with re-ranked passages, streaming answers back to the UI.

### Source Evidence
- **PDF Page**: Pages 4–6 (pp. 860–862), Figures 1 & 2, Section IV.

---

## 10. Methodology

1. **Document Loading**: Administrator uploads official campus documents via Streamlit UI.
2. **Ingestion & Indexing**: Ingestion pipeline chunks documents, generates embeddings via Ollama `nomic-embed-text`, and indexes them into ChromaDB.
3. **Query Ingestion**: Student submits natural language inquiry into chat interface.
4. **Semantic Retrieval**: ChromaDB performs similarity search, returning initial candidate chunks.
5. **Cross-Encoder Re-Ranking**: Cross-encoder re-evaluates candidate chunks against the prompt, eliminating false positives.
6. **Constrained Prompting**: Generating an augmented prompt enforcing strict grounding: *"Answer only based on the provided context. If unknown, state that the information is unavailable."*
7. **Streaming Response**: Gemma 3:4B generates and streams the response to the user.

### Source Evidence
- **PDF Page**: Pages 5–6 (pp. 861–862), Section V "SYSTEM WORKFLOW".

---

## 11. Experimental Setup

- **Hardware**: Standard institutional local workstation (CPU/GPU-accelerated local execution).
- **Inference Runtime**: Ollama local model runner.
- **Frontend Framework**: Streamlit.
- **Embedding Model**: `nomic-embed-text`.
- **LLM**: `Gemma 3:4B`.
- **Vector DB**: ChromaDB.
- **Re-ranker**: Sentence Transformers Cross-Encoder.

### Source Evidence
- **PDF Page**: Pages 5–7 (pp. 861–863).

---

## 12. Evaluation Metrics

Evaluated through qualitative verification and expert manual consistency checking:
- **Factual Fidelity / Groundedness**: Manual verification confirming answers correspond verbatim to uploaded source policies.
- **Contextual Informativeness**: Impact of the Cross-Encoder re-ranking step on reducing irrelevant context passed to the LLM.
- **Inference Latency & Streaming Responsiveness**: System responsiveness under interactive single-user testing.

### Source Evidence
- **PDF Page**: Page 7 (p. 863), Section VI "CONCLUSION".

---

## 13. Results

- **Local Pipeline Feasibility**: Proved that an entirely open-source, on-premise stack (Ollama + Gemma 3:4B + ChromaDB + Streamlit) can run reliably on collegiate hardware without incurring commercial API subscription costs or compromising data privacy.
- **Hallucination Suppression**: By restricting the system prompt to retrieved passages, the chatbot successfully avoided generating unsupported claims; when queries fell outside the uploaded documents, the system appropriately declined to answer.
- **Re-Ranking Impact**: Qualitative analysis confirmed that the Sentence Transformers Cross-Encoder significantly pruned vector search noise, ensuring higher factual precision in the prompt window.
- *Notice*: Specific numerical benchmark tables (e.g., RAGAS automated scores or multi-user throughput numbers) are **not reported** by the authors.

### Source Evidence
- **PDF Page**: Pages 6–7 (pp. 862–863), Section V & VI.

---

## 14. Baselines

- **General-Purpose Foundation LLMs (Zero-Shot)**: Base LLMs queried directly without retrieval, known to produce hallucinations on private institutional policies.
- **Single-Stage Vector RAG**: Standard RAG pipelines lacking a Cross-Encoder re-ranking phase.

### Source Evidence
- **PDF Page**: Page 3 (p. 859), Section II & Page 7 (p. 863).

---

## 15. Ablation Study

Evaluated qualitatively through the inclusion vs. exclusion of the Cross-Encoder re-ranking module: authors noted that vector-only retrieval frequently retrieved semantically similar but legally irrelevant college clauses, which the Cross-Encoder successfully eliminated prior to generation.

### Source Evidence
- **PDF Page**: Page 6 (p. 862) & Page 7 (p. 863).

---

## 16. Explainability

Source-grounded transparency: The system achieves operational explainability by strictly grounding its answers in named, uploaded files and displaying the specific contextual excerpts from which the answers were synthesized.

### Source Evidence
- **PDF Page**: Page 6 (p. 862), Section V.

---

## 17. Main Findings

1. Locally hosted open-source models (Gemma 3:4B via Ollama) provide an effective, zero-cost alternative to commercial cloud LLMs for educational institutional assistance.
2. Open-source local deployments guarantee full data privacy and regulatory compliance, ensuring sensitive institutional records never leave campus premises.
3. Adding a Cross-Encoder re-ranker between ChromaDB vector retrieval and LLM generation is crucial for filtering out semantic false-positive document chunks.
4. Streamlit offers a responsive, easily maintainable user interface for document ingestion and streaming chat interaction.

### Source Evidence
- **PDF Page**: Pages 6–7 (pp. 862–863), Section V & Section VI.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Static Knowledge Base**: The vector index cannot reflect real-time policy modifications unless documents are manually re-ingested.
- **Subjective Evaluation**: Evaluation was restricted to qualitative manual checking rather than automated multi-metric benchmarks (e.g., RAGAS).
- **Hardware & Scalability Bottlenecks**: Serving local LLMs on standard institutional hardware exhibits noticeable latency and struggles to scale under high concurrent multi-student workloads without dedicated GPU clusters.

### 18.2 Research Interpretation
- The authors do not report formal RAGAS scores (Faithfulness, Context Recall, Answer Relevance) or concurrent user latency figures.
- The document collection tested was limited to a localized institutional pilot.

---

## 19. Future Work

Explicitly proposed by authors:
1. Developing automated document-change tracking pipelines to dynamically synchronize ChromaDB with live institutional portals.
2. Integrating automated RAG evaluation frameworks (such as RAGAS) to quantitatively benchmark faithfulness and context recall.
3. Conducting formal large-scale user testing across campus student and faculty bodies.
4. Applying model quantization and local cluster serving (e.g., vLLM) to improve multi-user throughput.

### Source Evidence
- **PDF Page**: Page 7 (p. 863), Section VI "CONCLUSION".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Contextual RAG Placement Assistant & Policy Navigator (Module 06)**.
- **Architectural Contribution**: Confirms the practical viability of a local open-source stack (Ollama + ChromaDB + Cross-Encoder re-ranking) for campus deployment, protecting student placement data.
- **PRIE Enhancement Opportunity**: ScholarCamp extends this architecture by implementing automated RAGAS auditing and hybrid vector search (BM25 + dense embeddings) to overcome the static evaluation limitations identified by the authors.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Local RAG stack using Ollama and ChromaDB | System design specification | PDF p. 3 & p. 6 | Architecture |
| Gemma 3:4B and nomic-embed-text models | Implemented models | PDF p. 6 & p. 7 | Experimental setup |
| Sentence Transformers Cross-Encoder re-ranking | Two-tier retrieval pipeline | PDF p. 6, Section V | Methodology |
| Qualitative hallucination elimination | Author observation on manual checking | PDF p. 7, Section VI | Result |
| Call for automated RAGAS evaluation | Explicit future work recommendation | PDF p. 7, Section VI | Future work |

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

**VERIFIED** (Primary PDF read, complete open-source RAG architecture verified, discrepancy from legacy BibTeX documented).
