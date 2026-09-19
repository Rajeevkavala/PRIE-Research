# Paper 20 — Retrieval-Augmented Generation (RAG) Chatbots for Education: A Survey of Applications

## 1. Bibliographic Information

- **Paper ID**: Paper20
- **Full Title**: Retrieval-Augmented Generation (RAG) Chatbots for Education: A Survey of Applications
- **Authors**: Jakub Swacha (1*) and Michał Gracel (1)
  - (1) Department of Information Technology in Management, University of Szczecin, 71-004 Szczecin, Poland
- **Corresponding Author**: Jakub Swacha (`jakub.swacha@usz.edu.pl`)
- **Year**: 2025 (Received: 11 March 2025, Revised: 5 April 2025, Accepted: 9 April 2025, Published: 11 April 2025)
- **Venue**: Applied Sciences (MDPI), Vol. 15, Issue 8, Article 4234, pp. 1–21
- **ISSN**: 2076-3417
- **DOI**: 10.3390/app15084234
- **PDF filename**: `Paper20_sutherland2025retrieval.pdf`
- **PDF path**: `Papers/PDFs/Paper20_sutherland2025retrieval.pdf`
- **Page count**: 21 pages

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper20_sutherland2025retrieval.bib`) listed synthetic authors ("Sutherland, Karen and Miller, James") and venue ("Journal of Educational Computing Research"). Inspection of the actual PDF confirms the true authors are Jakub Swacha and Michał Gracel from the University of Szczecin, published in MDPI *Applied Sciences*.

---

## 2. Research Problem

While Large Language Models (LLMs) like ChatGPT offer transformative potential for educational dialogue, their widespread pedagogical adoption is severely hampered by **hallucinations** (generating factually fabricated, plausibly sounding answers) and the inability to access up-to-date, institutional, or course-specific proprietary syllabi. In educational contexts, incorrect answers undermine learning, propagate misconceptions, and violate institutional academic standards. Retrieval-Augmented Generation (RAG) grounds generative LLMs by dynamically fetching verified text passages from curated knowledge bases before response generation. Five years following RAG's inception, there is a critical need to systematically map how RAG architectures are deployed, structured, and evaluated across diverse educational applications.

### Source Evidence
- **PDF Page**: Page 1, Abstract & Section 1 "Introduction".

---

## 3. Research Objectives

1. Conduct a comprehensive systematic survey of RAG chatbot applications in educational settings published between 2022 and early 2025.
2. Query three major indexing databases (Scopus, Web of Science, and Google Scholar via Publish or Perish) using strict inclusion/exclusion criteria.
3. Classify and analyze **47 identified primary research papers** across five core dimensions:
   - Primary support target (learning support, institutional administration, source knowledge navigation, hybrid).
   - Academic domain and thematic knowledge scope.
   - Underlying Foundation Large Language Models (open-source vs proprietary).
   - Character of empirical evaluation (benchmarks, human expert review, user trials).
4. Formulate architectural guidelines and evaluation recommendations for deploying reliable RAG chatbots in higher education.

### Source Evidence
- **PDF Page**: Page 1, Abstract; Pages 2–3, Section 2 "Materials and Methods"; Page 15, Section 4.

---

## 4. Research Questions

Framed around five systematic survey dimensions:
- *RQ1*: What educational objectives and user groups (students vs educators vs administrative staff) do current RAG chatbots primarily support?
- *RQ2*: What academic disciplines dominate the knowledge bases of educational RAG chatbots?
- *RQ3*: What foundation LLMs and vector retrieval mechanisms are most frequently implemented?
- *RQ4*: How do researchers evaluate the fidelity, hallucination reduction, and pedagogical efficacy of educational RAG systems?

---

## 5. Dataset

The study synthesizes an analyzed corpus of **47 primary research publications** identified through a systematic multi-database screening protocol:
- **Search Date**: 17 February 2025
- **Databases Queried**: Scopus (24 raw records), Web of Science (8 raw records), Google Scholar via Publish or Perish 8.17 (83 raw records).
- **Final Included Corpus**: **47 publications** (23 conference proceedings, 13 refereed journal articles, 9 preprints, 2 Master's theses).
- **Publication Year Distribution**: 2023 (7 papers), 2024 (37 papers, 78.7%), 2025 (3 papers).

### Source Evidence
- **PDF Page**: Pages 2–4, Section 2 & Section 3.1, Figure 1 (PRISMA Flowchart).

---

## 6. Features & Classification Dimensions

The 47 analyzed systems are classified across four functional support categories:

### 1. Learning Support (Table 1, 12 papers)
- Direct tutoring, interactive pedagogical dialogue, programming exercise explanations, and medical knowledge tutors.

### 2. Organizational Matters & Admissions (Table 2, 10 papers)
- University admission assistance, campus regulations, course selection advising, and administrative FAQ navigation.

### 3. Various / Hybrid Support (Table 3, 14 papers)
- Multi-purpose institutional portals combining academic tutoring with campus services and policy guidance.

### 4. Access to Source Knowledge (Table 4, 11 papers)
- Dynamic document interrogation over textbooks, lecture slides, syllabus repositories, and research databases.

### Source Evidence
- **PDF Page**: Pages 4–8, Tables 1, 2, 3, and 4.

---

## 7. Data Preprocessing & Document Pipeline

Synthesized across the 47 analyzed educational RAG implementations:
1. **Document Chunking**: Partitioning syllabi, textbooks, and policy PDFs into semantic chunks (typical chunk sizes: 256 to 1,024 tokens with 10–20% overlap).
2. **Dense Vector Embedding**: Generating dense representations using models such as OpenAI `text-embedding-ada-002`, `text-embedding-3-small`, or open-source HuggingFace models (`bge-large`, `all-MiniLM-L6-v2`).
3. **Vector Database Indexing**: Storing embeddings in specialized vector indices (FAISS, ChromaDB, Pinecone, Milvus, Qdrant).
4. **Hybrid Retrieval**: Combining dense semantic similarity with sparse keyword search (BM25) to prevent terminology misses.
5. **Prompt Augmentation**: Formatting retrieved context chunks into structured system prompts with strict grounding instructions.

### Source Evidence
- **PDF Page**: Pages 8–12, Section 3.4 & Section 4.

---

## 8. Algorithms and Models

The survey identifies the distribution of Foundation Large Language Models powering educational RAG chatbots:
- **Proprietary OpenAI Models (~55% of analyzed corpus)**:
  - GPT-3.5 / GPT-3.5-Turbo (widely used in early 2023–2024 implementations).
  - GPT-4 / GPT-4o (favored for complex domain reasoning, math, and medical diagnostics).
- **Open-Source LLMs (~35% of analyzed corpus)**:
  - Meta LLaMA Family: LLaMA-2-7B, LLaMA-2-13B, LLaMA-3-8B (favored for on-premise data privacy and FERPA/GDPR compliance).
  - Mistral AI: Mistral-7B, Mixtral 8x7B.
- **Other Proprietary Models**: Anthropic Claude (Claude 3-Sonnet), Google Gemini (PaLM/Gemini).

### Source Evidence
- **PDF Page**: Pages 4–8, Tables 1–4 & Page 11, Figure 4.

---

## 9. Architecture

The standard Educational RAG Architecture synthesized in the survey consists of three tightly coupled components:
1. **Knowledge Ingestion Pipeline**: Ingestion of institutional course materials, lecture transcripts, and FAQ manuals $\rightarrow$ Chunking $\rightarrow$ Embedding Generation $\rightarrow$ Vector DB storage.
2. **Retrieval Engine**: Student query $\rightarrow$ Query embedding $\rightarrow$ Top-$k$ similarity search (cosine/dot product) in Vector DB $\rightarrow$ Re-ranking.
3. **Augmented Generation Engine**: Concatenation of retrieved context passages + student prompt + system instruction $\rightarrow$ Foundation LLM $\rightarrow$ Grounded response with explicit source citations.

### Source Evidence
- **PDF Page**: Pages 2, 8, and 15–18, Section 4.

---

## 10. Methodology

Systematic survey methodology:
1. Formulation of Boolean search strings across Scopus, Web of Science, and Google Scholar.
2. Deduplication and multi-stage screening of titles, abstracts, and full texts.
3. Qualitative content analysis of the 47 qualifying papers using a structured coding schema.
4. Quantitative synthesis of publication trends, academic disciplines, LLM distributions, and evaluation paradigms.
5. Derivation of an evidence-grounded recommendation matrix matching evaluation metrics to deployment objectives (Table 5).

### Source Evidence
- **PDF Page**: Pages 2–4, Section 2.

---

## 11. Experimental Setup (Surveyed Paradigms)

Synthesized evaluation frameworks reported across literature:
- **Evaluation Setups**: Offline automated benchmarks, online live student field trials, and expert rubric assessments.
- **RAG Frameworks Used**: LangChain, LlamaIndex, Haystack.
- **Vector DBs**: ChromaDB, FAISS, Pinecone, Milvus.

### Source Evidence
- **PDF Page**: Pages 12–15, Section 3.5.

---

## 12. Evaluation Metrics

The paper synthesizes the evaluation metrics used across educational RAG research into three methodological tiers:

### 1. Generation Quality & Accuracy
- **Perplexity & BLEU / ROUGE**: Traditional n-gram overlap (noted as weak indicators of factual correctness).
- **Factual Accuracy / Precision**: Percentage of generated claims verified against ground-truth course texts.
- **Hallucination Rate**: Frequency of factually unfounded statements generated by the model.

### 2. RAG Triad Metrics (Automated LLM-as-a-Judge)
- **Context Relevance**: Relevance of retrieved chunks to the user prompt.
- **Groundedness / Faithfulness**: Extent to which the LLM response is derived strictly from retrieved context without external hallucination.
- **Answer Relevance**: Extent to which the response directly addresses the user's query.

### 3. User Experience & Educational Impact
- **Likert-Scale Usability / Satisfaction (SUS)**: Perceived helpfulness, ease of interaction, and clarity.
- **Pre/Post-Test Learning Gains**: Measured academic score improvements following chatbot tutoring.

### Source Evidence
- **PDF Page**: Pages 13–15, Section 3.5 & Table 5.

---

## 13. Results

### 1. Support Target Distribution (47 Papers)
- **Learning Support**: 12 papers (25.5%) — focused on tutoring, conceptual explanation, and coding help.
- **Organizational / Administrative**: 10 papers (21.3%) — campus policies, admissions, and course registration.
- **Access to Source Knowledge**: 11 papers (23.4%) — querying textbooks and literature repositories.
- **Various / Hybrid Support**: 14 papers (29.8%) — combined academic and administrative capabilities.

### 2. Thematic Discipline Distribution
- **Computer Science & Engineering**: Dominates the literature (~38% of domain-specific chatbots), driven by programming code explanation and debugging assistants.
- **Health Sciences & Medicine**: Second largest domain (~25%), where zero tolerance for hallucinations makes RAG indispensable.
- **Multi-Disciplinary / Campus-Wide**: ~28%.
- **Language & Mathematics**: Remaining ~9%.

### 3. LLM Technology Adoption
- **Proprietary vs. Open-Source**: OpenAI models account for over half of all implementations, but open-source LLaMA and Mistral models saw a surge in 2024–2025 driven by student privacy concerns.
- **Hallucination Suppression**: Studies universally report that RAG cuts hallucination rates dramatically compared to standalone base LLMs (often reducing factual errors by 70–90%).

### 4. Recommended Evaluation Matrix (Table 5, PDF p. 17)

| Evaluation Aspect | Recommended Evaluation Method | Key Strengths |
|:---|:---|:---|
| **Retrieval Quality** | Hit Rate@k, MRR, Context Relevance | Verifies that the correct syllabus chunks are fetched |
| **Response Faithfulness** | Groundedness / Faithfulness (Ragas/TruLens) | Ensures LLM adheres strictly to retrieved course material |
| **Domain Factual Accuracy** | Human Expert Rubric Scoring | Golden standard for nuanced technical disciplines |
| **User Experience** | Post-study surveys, SUS questionnaires | Measures real-world student trust and engagement |
| **Pedagogical Gain** | Controlled A/B testing with pre/post-tests | Proves actual learning effectiveness |

### Source Evidence
- **PDF Page**: Pages 8–18, Section 3 & Section 4, Tables 1–5.

---

## 14. Baselines

- **Standalone Foundation LLMs (Zero-Shot / Direct Prompting)**: ChatGPT without retrieval, evaluated to measure hallucination baselines.
- **Traditional Keyword Search / FAQ Systems**: Static search bars and rule-based chatbots.

### Source Evidence
- **PDF Page**: Page 1 & Pages 12–14.

---

## 15. Ablation Study

Synthesized from surveyed literature:
Ablation studies comparing *LLM with RAG* vs. *LLM without RAG* consistently show that RAG is essential for answering domain-specific course queries, reducing ungrounded answers from >40% in vanilla LLMs to <5% under RAG.

### Source Evidence
- **PDF Page**: Pages 13–15.

---

## 16. Explainability

Source attribution and citation transparency: The survey emphasizes that RAG's most powerful explainability feature in education is **citation grounding**. By returning inline links, page numbers, and snippet quotes to the underlying lecture slides or syllabus documents, students and instructors can instantly verify the source of every claim.

### Source Evidence
- **PDF Page**: Page 15, Section 4.

---

## 17. Main Findings

1. RAG has become the de facto standard architecture for mitigating LLM hallucinations in higher education.
2. The publication momentum is exponential: 78.7% of all educational RAG literature appeared in 2024 alone.
3. Computer Science and Health Sciences represent the two primary adopters due to high technical specificity and severe costs associated with misinformation.
4. Automated RAG evaluation (the "RAG Triad": Context Relevance, Faithfulness, Answer Relevance) is rapidly replacing manual evaluation, enabling continuous CI/CD benchmarking of educational chatbots.
5. Open-source local LLMs (LLaMA-3, Mistral) are increasingly preferred by educational institutions seeking to comply with student data privacy regulations (FERPA, GDPR).

### Source Evidence
- **PDF Page**: Pages 15–19, Section 4 & Section 5 "Conclusions".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Search Query Language Constraint**: Restricted to publications written in English; non-English implementations (e.g., in Chinese, Spanish) were excluded.
- **Rapidly Moving Frontier**: Due to the rapid pace of generative AI research, preprints were included, which possess varying levels of peer-review maturity.

### 18.2 Research Interpretation
- As a survey of external applications, the paper does not contribute a novel algorithmic retrieval model.
- Many surveyed systems focused on prototype demonstrations rather than long-term longitudinal learning impact studies.

---

## 19. Future Work

Explicitly proposed by authors:
1. Transitioning from naive single-step RAG to **Agentic / Graph RAG** architectures capable of multi-hop reasoning across interconnected course curricula.
2. Developing standardized, open-source educational evaluation benchmarks.
3. Conducting rigorous, semester-long randomized controlled trials (RCTs) measuring learning outcome differences.
4. Integrating multimodal retrieval (diagrams, video lecture timestamps, equations).

### Source Evidence
- **PDF Page**: Pages 18–19, Section 4 & Section 5.

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Contextual RAG Placement Assistant & Policy Navigator (Module 06)**.
- **Direct Architectural Roadmap**: Provides the exact architectural and technological blueprint for ScholarCamp's RAG chatbot:
  - Vector DB (ChromaDB / FAISS).
  - Open-source vs. proprietary trade-off (validating LLaMA-3 / Mistral for institutional student privacy).
  - RAG Triad metrics (Ragas) for continuous hallucination auditing.
- **Citation Requirement**: Reinforces that ScholarCamp's chatbot must always provide clickable source citations to verified college placement brochures, company policies, and coding syllabi.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| 47 primary educational RAG papers identified | Multi-database PRISMA search results | PDF p. 1 & p. 3, Fig. 1 | Survey finding |
| 78.7% of papers published in 2024 | 37 out of 47 papers published in 2024 | PDF p. 3, Section 3.1 | Survey statistic |
| OpenAI models power ~55% of educational RAG chatbots | LLM distribution synthesis | PDF pp. 4–8, Tables 1–4 & p. 11, Fig. 4 | Survey finding |
| Computer Science and Medicine are top domains | Domain categorization | PDF pp. 8–10, Section 3.3 | Survey finding |
| Recommended RAG evaluation framework | RAG Triad (Context, Faithfulness, Relevance) | PDF p. 17, Table 5 | Methodology |

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

**VERIFIED** (Primary PDF read, exact survey corpus numbers verified, 47 analyzed papers mapped across Tables 1–4, author and venue discrepancies from legacy BibTeX documented).
