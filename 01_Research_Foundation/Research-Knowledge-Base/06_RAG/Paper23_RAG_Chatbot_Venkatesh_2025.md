# Paper 23 — AI-Driven RAG Chatbot: Combining Information Retrieval with Generative AI

## 1. Bibliographic Information

- **Paper ID**: Paper23
- **Full Title**: AI-Driven RAG Chatbot: Combining Information Retrieval with Generative AI
- **Authors**: Venkatesh S. (1), Dhanya K R. (2), and Kaniska P. (3)
  - (1,2,3) Department of Computer Science with Data Analytics, Dr N.G.P Arts and Science College, Coimbatore, Tamil Nadu, India
- **Author Emails**: `venkateshkaviya1234@gmail.com`, `dhanyafab@gmail.com`, `kaniskaprabhakaran573@gmail.com`
- **Year**: 2024/2025 (Received: 11.12.2024, Revised: 02.01.2025, Accepted: 25.01.2025, Published: 06.02.2025)
- **Venue**: Journal of IoT in Social, Mobile, Analytics, and Cloud (JISMAC), Vol. 6, Issue 4, pp. 364–373
- **ISSN**: 2582-1369
- **DOI**: 10.36548/jismac.2024.4.005
- **PDF filename**: `Paper23_mathew2025ai.pdf`
- **PDF path**: `Papers/PDFs/Paper23_mathew2025ai.pdf`
- **Page count**: 10 pages (pp. 364–373)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper23_mathew2025ai.bib`) listed synthetic authors ("Mathew, Elizabeth and Thomas, Binu") and title extension ("...in Academic Institutions"). Inspection of the actual PDF confirms the true authors are Venkatesh S., Dhanya K R., and Kaniska P. from Dr N.G.P Arts and Science College, Coimbatore, published in *Journal of IoT in Social, Mobile, Analytics, and Cloud*.

---

## 2. Research Problem

In higher education and e-learning environments, students require immediate, accurate, and context-specific answers to technical course questions and learning materials. Standard commercial generative language models frequently hallucinate incorrect technical explanations when queried on specialized academic topics, leading to misconceptions. Conversely, traditional keyword-based FAQ systems cannot handle natural language conversational phrasing. To address these limitations, the paper develops a Retrieval-Augmented Generation (RAG) assistant combining dense semantic vector retrieval with Google's Gemini-1.5-Pro model to deliver concise, grounded answers strictly derived from course documents.

### Source Evidence
- **PDF Page**: Page 1 (p. 364), Abstract & Section 1 "Introduction".

---

## 3. Research Objectives

1. Develop a full-stack **RAG Chatbot** serving as an interactive e-learning study assistant for university students.
2. Formulate a document processing pipeline extracting text from educational course PDFs and converting segments into dense semantic vectors using `GoogleGenerativeAIEmbeddings`.
3. Deploy a local instance of **Chroma Vector Database** for efficient similarity indexing and chunk retrieval.
4. Integrate Google's **Gemini-1.5-Pro** generative foundation model to synthesize concise, grounded responses bounded by strict prompt constraints (maximum 3 sentences).
5. Build an intuitive web user interface using **React and Bootstrap**, communicating via a **Flask** backend API.

### Source Evidence
- **PDF Page**: Page 1 (p. 364), Abstract; Pages 3–5 (pp. 366–368), Section 3 "Proposed Methodology".

---

## 4. Research Questions

Not explicitly stated in question syntax. The research focuses on system engineering feasibility:
- How effectively can Google Generative AI Embeddings paired with ChromaDB retrieve relevant conceptual textbook chunks?
- Can strict prompt constraints on Gemini-1.5-Pro enforce concise (3-sentence) responses that remain strictly grounded in uploaded course documentation?

---

## 5. Dataset / Educational Corpus

- **Corpus Type**: Computer science and artificial intelligence e-learning materials (specifically educational lecture notes and PDF textbooks covering complex machine learning architectures such as Generative Adversarial Networks — GANs).
- **Document Ingestion**: Parsing raw PDF textbooks into structured chapter segments.
- **Collection Scope**: Academic departmental reference documents at Dr N.G.P Arts and Science College.

### Source Evidence
- **PDF Page**: Pages 4–7 (pp. 367–370), Section 3 & Section 4.

---

## 6. Features & System Pipeline

### Ingestion Pipeline
- PDF text extraction and semantic chunking.
- Dense vector representations generated via `GoogleGenerativeAIEmbeddings`.
- Vector indexing in ChromaDB collections.

### Query & Generation Pipeline
- Natural language student queries converted into query vector embeddings.
- Cosine semantic similarity search over stored document vectors.
- Augmented context injection into Gemini-1.5-Pro prompt template.
- 3-sentence constrained text synthesis.

### Source Evidence
- **PDF Page**: Pages 4–5 (pp. 367–368), Figures 1, 2, 3, and 4.

---

## 7. Data Preprocessing

1. **PDF Text Extraction**: Extracting textual paragraphs from academic lecture notes and reference textbooks.
2. **Context Window Chunking**: Splitting continuous text into granular sections suitable for embedding models.
3. **Dense Embedding Vectorization**: Creating high-dimensional semantic vectors via `GoogleGenerativeAIEmbeddings`.
4. **Vector Storage**: Persisting generated vectors into ChromaDB collections to enable low-latency approximate nearest-neighbor retrieval.

### Source Evidence
- **PDF Page**: Page 4 (p. 367), Sections 3.2, 3.3, and 3.4.

---

## 8. Algorithms and Models

### 1. Vector Embedding Model
- **`GoogleGenerativeAIEmbeddings`**: Generates dense semantic representations capturing conceptual context across full sentences and paragraphs.

### 2. Vector Database
- **Chroma Vector Database (ChromaDB)**: Manages and indexes document embeddings, performing similarity search against incoming user queries.

### 3. Foundation Generative Model
- **Google Gemini-1.5-Pro**: Multi-modal foundation language model queried via API to synthesize answers.

### 4. Prompt Engineering System Instruction
- Employs a strict system constraint:
  > *"You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don’t know the answer, say that you don’t know. Keep the answer concise (maximum of 3 sentences)."*

### Source Evidence
- **PDF Page**: Pages 4–5 (pp. 367–368), Sections 3.3–3.5.

---

## 9. Architecture

The system architecture spans four distinct tiers (Figures 1, 4, 5):
1. **Frontend Client Layer**: Built with **React** and styled with **Bootstrap CSS**, featuring responsive chat bubbles, message input bars, and dynamic typing/processing indicators.
2. **API & Server Middleware**: **Python Flask** server handling HTTP POST requests, query routing, and API authentication.
3. **Retrieval Core**: **ChromaDB** storing vector embeddings generated by Google Generative AI Embeddings.
4. **Cloud Generative AI Engine**: **Google Gemini-1.5-Pro** executing constrained generation conditioned on top-$k$ retrieved chunks.

### Source Evidence
- **PDF Page**: Pages 4–6 (pp. 367–369), Figures 1, 4, 5, 6, and 7.

---

## 10. Methodology

1. **Document Loading & Embedding**: Course textbook PDFs are parsed and embedded into ChromaDB.
2. **Query Submission**: Student submits query (e.g., *"Working of GAN brief?"*).
3. **Query Embedding & Retrieval**: Query is embedded via Google Embeddings; ChromaDB retrieves semantically similar textbook chunks.
4. **Context Augmentation**: Retrieved context is injected into the 3-sentence constrained Gemini prompt.
5. **Answer Synthesis**: Gemini-1.5-Pro generates the answer.
6. **Delivery & Visual Verification**: Response is rendered in the React interface; authors compare generated answer against original textbook text.

### Source Evidence
- **PDF Page**: Pages 4–7 (pp. 367–370), Section 3 & Section 4.

---

## 11. Experimental Setup

- **Frontend**: React, Bootstrap CSS.
- **Backend**: Python, Flask web framework.
- **Vector DB**: ChromaDB.
- **Cloud Models**: `GoogleGenerativeAIEmbeddings`, `Gemini-1.5-Pro`.
- **Operating Environment**: Cloud-connected academic computing laboratory.

### Source Evidence
- **PDF Page**: Pages 5–7 (pp. 368–370).

---

## 12. Evaluation Metrics

Evaluated qualitatively through functional interface verification:
- **Factual Alignment**: Manual side-by-side comparison between generated response and PDF textbook source text (Figures 7 & 8).
- **Conciseness Compliance**: Verification that answers adhere to the maximum 3-sentence brevity constraint.
- **Interface Responsiveness**: Verification of query processing indicators and asynchronous API handling.

### Source Evidence
- **PDF Page**: Pages 6–8 (pp. 369–371), Figures 7 & 8.

---

## 13. Results

- **Factual Consistency**: In the benchmark test query (*"Working of GAN brief?"*), the system extracted the exact operational mechanics of Generative Adversarial Networks (Generator vs. Discriminator game) from the textbook PDF and synthesized a factually accurate, non-hallucinated summary.
- **Conciseness**: The 3-sentence prompt restriction successfully forced Gemini-1.5-Pro to eliminate conversational filler and deliver direct, highly digestible conceptual definitions.
- *Notice*: The authors did not report quantitative retrieval metrics (e.g., Hit Rate@k, MRR, ROUGE, or RAGAS scores) in this system implementation paper.

### Source Evidence
- **PDF Page**: Pages 6–8 (pp. 369–371), Figures 7 & 8, Section 4.

---

## 14. Baselines

- **Standalone Un-grounded LLM**: Direct query to generative models without retrieval (known to hallucinate or provide overly verbose, non-syllabus definitions).
- **Manual Textbook Search**: Students manually locating concepts across multi-hundred-page course PDFs.

### Source Evidence
- **PDF Page**: Page 1 (p. 364) & Page 7 (p. 370).

---

## 15. Ablation Study

Not reported.

---

## 16. Explainability

Source grounding: Explainability is achieved operationally because the generated answer's core assertions can be mapped directly to specific paragraphs in the ingested course PDF (demonstrated in Figure 8).

### Source Evidence
- **PDF Page**: Page 7 (p. 370), Figure 8.

---

## 17. Main Findings

1. Combining dense embeddings (Google Generative AI) with ChromaDB and Gemini-1.5-Pro provides a reliable, hallucination-resistant architecture for course Q&A.
2. Enforcing a strict 3-sentence brevity constraint prevents generative verbosity, making responses significantly more actionable for quick student revision.
3. Decoupling the user interface (React + Bootstrap) from the retrieval backend (Flask + ChromaDB) ensures modularity and easy integration into existing college portals.

### Source Evidence
- **PDF Page**: Pages 6–8 (pp. 369–371), Section 4 & Section 5 "Conclusion".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Computational Power & Connectivity**: Requires continuous high-bandwidth internet connectivity to query Google Cloud APIs (Gemini-1.5-Pro).
- **Cost Scaling**: Heavy multi-student usage incurs operational API usage costs.
- **Evaluation Subjectivity**: Relies on visual side-by-side inspection rather than automated benchmark scoring.

### 18.2 Research Interpretation
- Absence of automated quantitative retrieval benchmarks (RAGAS / BLEU / ROUGE).
- Does not incorporate multi-document re-ranking (Cross-Encoders) or hybrid keyword search.

---

## 19. Future Work

Explicitly proposed by authors:
1. Extending the chatbot to support multi-modal educational inputs (diagrams, handwritten mathematical equations, audio speech queries).
2. Incorporating localized, edge-deployable open-source LLMs to reduce cloud dependency.
3. Conducting structured user testing across entire student batches to measure learning gains.

### Source Evidence
- **PDF Page**: Page 8 (p. 371), Section 5 "Conclusion".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Contextual RAG Placement Assistant (Module 06)**.
- **Architectural Contribution**: Validates the integration of Google Gemini with ChromaDB and Flask for educational document Q&A.
- **Prompt Engineering Value**: The 3-sentence conciseness prompt provides an effective pattern for PRIE's quick interview preparation hints and policy summaries.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Google Gemini-1.5-Pro and ChromaDB stack | Methodology description | PDF pp. 4–5, Sections 3.3–3.5 | Architecture |
| Strict 3-sentence brevity prompt | Prompt template text | PDF p. 5, Section 3.5 | Methodology |
| React + Bootstrap frontend with Flask backend | UI and server stack | PDF p. 6, Section 4 | Experimental setup |
| Side-by-side verification against source PDF | Figures 7 & 8 comparison | PDF p. 7, Figs. 7 & 8 | Experimental result |
| Cloud API cost and connectivity limitation | Author discussion in conclusion | PDF p. 8, Section 5 | Author discussion |

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

**VERIFIED** (Primary PDF read, exact technical stack and prompt templates verified, author correction from legacy BibTeX documented).
