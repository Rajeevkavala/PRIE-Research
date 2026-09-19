# Paper 40 — Utilizing Retrieval Augmented Generation (RAG)-Based Chatbots as an Innovative Learning Tool in Higher Education: A Case Study on the Use of Digital Learning Resources

## 1. Bibliographic Information

- **Paper ID**: Paper40
- **Full Title**: Utilizing Retrieval Augmented Generation (RAG)-Based Chatbots as an Innovative Learning Tool in Higher Education: A Case Study on the Use of Digital Learning Resources
- **Authors**: Yusza Reditya Murti (1), Dian Puteri Ramadhani (2), Herry Irawan (3)
  - *(1, 2, 3) School of Economics and Business, Universitas Telkom, Jawa Barat, Indonesia*
  - *Corresponding author: yuszaa@telkomuniversity.ac.id*
- **Year**: 2025 (Received 24 August 2025, Accepted 24 October 2025; Published in Vol. 4, No. 3, pp. 281–298)
- **Venue**: Indonesian Journal of Elearning and Multimedia (IJOEM), published by CV Media Inti Teknologi
- **DOI**: `https://doi.org/10.58723/ijoem.v4i3.510`
- **ISSN**: 2830-2885
- **PDF filename**: `Paper40_schmidt2025utilizing.pdf`
- **PDF path**: `Papers/PDFs/Paper40_schmidt2025utilizing.pdf`
- **Page count**: 18 pages
- **Metadata Note / Discrepancy**: The PDF filename indicates `schmidt2025utilizing`, but the actual printed authors on PDF p. 1 are Yusza Reditya Murti, Dian Puteri Ramadhani, and Herry Irawan from Telkom University, Indonesia. There is no author named Schmidt in the paper or references.

## 2. Research Problem

In higher education, digital learning resources are heavily fragmented across disparate platforms (Learning Management Systems, MOOCs, digital library repositories, and external e-books). This fragmentation forces students to expend excessive cognitive capacity navigating multiple portals, leading to digital information overload, reduced decision-making accuracy, and academic anxiety. Concurrently, standard Large Language Models (LLMs) suffer from hallucination and possess static, unverified knowledge bases that cannot reliably serve institutional curriculum needs.

### Source Evidence
- PDF p. 1–3, Abstract & Section A — Introduction.

## 3. Research Objectives

1. Design and develop a functional Retrieval-Augmented Generation (RAG) chatbot integrated with institutional Learning Management Systems (LMS) and learning repositories following the Design Science Research Methodology (DSRM).
2. Empirically assess undergraduate student acceptance using the Technology Acceptance Model (TAM) across Perceived Usefulness, Perceived Ease of Use, and Intention to Use.
3. Investigate faculty pedagogical perspectives, governance concerns, and source validation requirements through qualitative semi-structured inquiry.

### Source Evidence
- PDF p. 1, Abstract; PDF p. 3, Section B — Research Methods.

## 4. Research Questions

- *Not explicitly reported in itemized RQ format.* The study is organized around DSRM design objectives and TAM construct hypotheses examining user acceptance and pedagogical feasibility.

## 5. Dataset

The study incorporates two empirical evaluation cohorts:
- **Student TAM Cohort**:
  - **Sample Size**: 267 undergraduate students ($N = 267$).
  - **Sampling Strategy**: Convenience and purposive sampling of undergraduate students exposed to the RAG chatbot demonstration and system trials.
  - **Institution**: Telkom University (Bandung, Indonesia), with collaborative observation from UNIB, IAIN Madura, and UPI (PDF p. 7, 18).
  - **Instrument**: 10-item bilingual TAM survey (English and Indonesian) scored on a 5-point Likert scale (1 = Strongly Disagree to 5 = Strongly Agree) (PDF p. 7–8, Table 1).
- **Faculty Interview Cohort**:
  - **Sample Size**: 5 faculty members ($N = 5$).
  - **Representation**: Purposively selected across three universities representing STEM (engineering, computer science) and social sciences (management, business).
  - **Format**: 30–45 minute semi-structured interviews covering pedagogical value, integration, quality assurance, and faculty role (PDF p. 8).
- **Knowledge Base Corpus**:
  - Institutional learning materials: Lecturer slides, syllabi, course notes, LMS modules, MOOC transcripts, academic e-books, and curated external references across diverse disciplines (accounting, marketing, computer science/cybersecurity, microeconomics) (PDF p. 4, 8–9).

### Source Evidence
- PDF p. 1, Abstract; PDF p. 7–8, Section B — Research Methods (Participants and Table 1); PDF p. 18, Section E — Acknowledgment.

## 6. Features

Data elements and interaction features processed by the system:
- **Curricular Input Features**:
  - Syllabus topics, course competencies, slide text chunks, e-book sections, and faculty lecture transcripts.
- **Vector Embedding Features**:
  - Dense semantic embeddings generated across document chunks stored in a vector database.
- **Conversational & Query Features**:
  - Student natural language queries, multi-turn conversational history, topic labels (e.g., "BOK prodi akuntansi S-1", "Marketing plan", "Artikel tentang sqlmap", "Teori Permintaan dan Penawaran") (PDF p. 8–9, Figure 4).
- **Attribution Features**:
  - Explicit document source citations, page references, and clickable source links embedded in generated responses.

## 7. Data Preprocessing

The multi-stage RAG document processing pipeline follows a 6-step ingestion workflow (PDF p. 4, Figure 2 & Section B):
1. **Document Ingestion**: Collecting heterogeneous educational files (PDF, DOCX, PPTX, text).
2. **Text Extraction & Cleaning**: Removing formatting artifacts, boilerplate headers/footers, and non-informative text.
3. **Semantic Chunking**: Segmenting text into overlapping semantic passages to preserve localized context.
4. **Vector Embedding**: Transforming text chunks into high-dimensional dense vectors using a pre-trained embedding model.
5. **Vector Indexing & Storage**: Storing vector representations in an institutional vector database optimized for similarity search.
6. **Query-Context Retrieval**: Performing cosine/semantic similarity search on incoming student queries to extract the top-$k$ relevant contextual chunks for prompt augmentation.

## 8. Algorithms and Models

- **Large Language Model (LLM)**: Pre-trained foundation model acting as the Agent AI reasoning and synthesis engine (PDF p. 4, Figure 2).
- **Dense Vector Embedding Model**: Encodes educational texts and user queries into high-dimensional vector representations.
- **Retrieval Engine**: Vector database executing semantic similarity search (cosine similarity ranking) over institutional document vectors.
- **Prompt Synthesis Orchestrator**: Augments user prompts with retrieved context chunks and system guardrails instructing the LLM to ground answers strictly in retrieved evidence and cite sources.

### Source Evidence
- PDF p. 4, Section B, Figure 2 ("Conceptual Workflow for Chatbots"); PDF p. 8–10, Section C.1.

## 9. Architecture

The system implements an end-to-end RAG architecture integrated with educational infrastructure:
- **Chatbot User Interface**: Conversational frontend resembling modern messaging apps, featuring a left sidebar with multi-topic chat history and a primary interactive dialogue panel (PDF p. 8–9, Figure 4).
- **LMS & Institutional Gateway**: Connectors linking the RAG system to institutional LMS platforms (e.g., Moodle/Canvas) and digital libraries.
- **Agent AI / Orchestration Layer**: Manages prompt construction, enforces institutional guardrails, coordinates semantic search queries, and controls context windows.
- **Knowledge Vector Database**: Centralized searchable index storing embedded representations of verified institutional courseware.
- **Architecture Diagram**: Figure 2 (PDF p. 4) illustrates the conceptual RAG workflow; Figure 4 (PDF p. 9) illustrates the operational conversational UI.

## 10. Methodology

The study adheres to the **Design Science Research Methodology (DSRM)** (Peffers et al., 2007) across six structured stages:
1. **Problem Identification & Motivation**: Literature analysis of digital fragmentation and survey of student cognitive overload.
2. **Define Solution Objectives**: Establishing functional requirements for multi-source retrieval, factual grounding, and UI clarity.
3. **Design & Development**: Engineering the vector embedding pipeline, RAG orchestrator, and chatbot interface.
4. **Demonstration**: Deploying the operational prototype to simulate microeconomics, accounting, and computer science queries.
5. **Evaluation**: Dual-method empirical evaluation comprising a quantitative TAM survey ($N = 267$) and qualitative faculty interviews ($N = 5$).
6. **Communication**: Formal reporting of design principles, empirical findings, and governance recommendations.

## 11. Experimental Setup

- **Evaluation Design**: Post-demonstration empirical assessment.
- **Student Cohort**: $N = 267$ undergraduate students from Indonesian universities.
- **Survey Scale**: 5-point Likert scale (1 = Strongly Disagree, 2 = Disagree, 3 = Neutral, 4 = Agree, 5 = Strongly Agree).
- **Constructs Evaluated**: Perceived Usefulness (PU, 3 items), Perceived Ease of Use (PEU, 3 items), and Intention to Use (ITU, 4 items) (Table 1, PDF p. 7–8).
- **Categorization Criteria**: Mean scores categorized as Low ($< 3.0$), Moderately High ($3.0 \le \text{Score} < 4.0$), and High ($\ge 4.0$).
- **Qualitative Protocol**: 30–45 minute semi-structured interviews with 5 faculty members across three institutions.

## 12. Evaluation Metrics

- **Technology Acceptance Model (TAM) Construct Means**:
  - Perceived Usefulness (PU) mean score.
  - Perceived Ease of Use (PEU) mean score.
  - Intention to Use (ITU) mean score.
  - Overall TAM mean score.
- **Item-Level Descriptive Means**: PU1–PU3, PEU1–PEU3, ITU1–ITU4.
- **Qualitative Thematic Codes**: Pedagogical value, curriculum integration, quality assurance / verification responsibility, faculty positioning.

## 13. Results

### Quantitative TAM Findings ($N = 267$, PDF p. 11–12, Tables 2 & 3):
- **Overall TAM Acceptance**: Overall mean score of **4.097** out of 5.0, categorized as **"High"** acceptance.
- **Construct Breakdown (Table 2)**:
  - **Perceived Usefulness (PU)**: **4.138** (High) — highest scoring construct.
  - **Perceived Ease of Use (PEU)**: **4.023** (High).
  - **Intention to Use (ITU)**: **4.129** (High).
- **Item-Level Highlights (Table 3)**:
  - Highest single item: **ITU4** ("I will recommend the Academic Chatbot application to friends or colleagues") = **4.251** (High).
  - Second highest item: **PU3** ("Helps me find academic information quickly") = **4.213** (High).
  - Third highest item: **ITU3** ("Plan to regularly use the chatbot") = **4.194** (High).
  - PU2 (Meets learning needs): **4.133**; PU1 (Helps complete tasks and understand materials): **4.068**.
  - PEU1 (Easy to use in learning): **4.103**; PEU2 (Easy to use for tasks): **4.072**.
  - Lowest single item: **PEU3** ("Interaction with the chatbot is clear and easy to understand") = **3.894** ("Moderately High") — indicates occasional ambiguity or cognitive effort in interpreting generated synthesized responses.

### Qualitative Faculty Interview Findings ($N = 5$, PDF p. 12–15):
- Faculty unanimously affirmed the 24/7 learning support and remediation potential of RAG chatbots.
- Highlighted critical pedagogical risks: student over-reliance on synthesized summaries discouraging deep reading of primary source literature.
- Emphasized the necessity of explicit institutional quality assurance: faculty-verified knowledge ingestion, automated source links, and disciplinary boundary guardrails.

## 14. Baselines

- Traditional fragmented digital learning environments (manual keyword searching across unintegrated LMS, MOOC portals, and library catalogs) and standard, ungrounded commercial LLMs prone to hallucination.

## 15. Ablation Study

- *Not reported.* The study evaluated the end-to-end RAG system rather than comparing dense vs. sparse retrieval or alternative vector chunking strategies.

## 16. Explainability

- **Transparent Source Attribution**: A core architectural feature of the RAG system is explicit grounding and citation: every generated paragraph provides direct attribution to specific courseware documents, slide titles, or textbook sections, enabling users to verify factual assertions (PDF p. 4, 8–10).

## 17. Main Findings

1. RAG-based chatbots successfully mitigate information fragmentation and hallucination by grounding responses in verified courseware and providing verifiable source citations.
2. Students demonstrate high acceptance (TAM mean = 4.097), prioritizing functional usefulness (PU = 4.138) and rapid retrieval (PU3 = 4.213) over interface novelty.
3. Students exhibit strong intention to recommend the tool to peers (ITU4 = 4.251), reflecting high perceived utility.
4. Interaction clarity (PEU3 = 3.894) represents the primary friction point, suggesting that lengthy or densely synthesized academic responses require better visual structuring.
5. Faculty support RAG integration for remediation but demand institutional governance frameworks and UI mechanisms that compel students to consult primary texts rather than rely solely on generated summaries.

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Demonstration-Based Evaluation**: Evaluation occurred post-demonstration rather than tracking longitudinal, semester-long usage in credit-bearing courses (PDF p. 15, 17).
- **Geographic & Cultural Sample**: Student sample ($N = 267$) drawn exclusively from Indonesian higher education institutions, limiting direct cross-cultural generalizability (PDF p. 17).
- **Lack of Statistical Model Validation**: Evaluated via descriptive means; did not perform Structural Equation Modeling (PLS-SEM) or confirmatory factor analysis on TAM constructs (PDF p. 17).
- **Small Faculty Cohort**: Faculty inquiry limited to 5 participants ($N = 5$) across three institutions (PDF p. 8, 17).
- **Absence of Algorithmic Benchmarks**: Did not benchmark retrieval precision (Hit@$k$, MRR) or generation faithfulness (RAGAS) against alternative RAG pipelines (PDF p. 17).

### 18.2 Research Interpretation
- **Model Specification Details Omitted**: Specific foundational LLM (e.g., GPT-4o, LLaMA-3) and embedding model dimensions are not explicitly documented in the text, focusing instead on system-level DSRM workflows.

## 19. Future Work

1. Conducting longitudinal field studies measuring actual usage behavior and empirical academic performance impacts over full academic semesters (PDF p. 17).
2. Performing rigorous psychometric and structural equation modeling (PLS-SEM) to validate TAM causal paths (PDF p. 17).
3. Expanding faculty acceptance studies across broader institutional samples and academic disciplines (PDF p. 17).
4. Implementing institutional governance, automated source-checking protocols, and pedagogical guardrails preventing superficial summary dependence (PDF p. 17).

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Direct Blueprint for ScholarCamp Knowledge Engine**: Murti et al. provides empirical and architectural validation for deploying RAG chatbots over institutional courseware and placement training syllabi.
- **Validating Usefulness over Ease of Use**: Demonstrates that university students value retrieval accuracy and task completion (PU = 4.138) more than superficial gamification or ease of use (PEU = 4.023).
- **Source Citation Safeguard**: Confirms that transparent source linking is essential for educational credibility, aligning with ScholarCamp's requirement that AI recommendations link directly back to verified curriculum modules.
- **Pedagogical Guardrail Design**: Informs ScholarCamp's UI design: rather than providing terminal answers that bypass student effort, the chatbot must provide guided explanations with prompts nudging students toward active problem solving.

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|---|---|---|---|
| Overall student TAM acceptance | Overall mean score of 4.097 across N=267 students | PDF p. 1, Abstract; p. 11, Table 2 | Experimental result |
| Highest evaluated construct | Perceived Usefulness (PU) mean score of 4.138 | PDF p. 11, Table 2 | Experimental result |
| Highest rated individual item | ITU4 (Peer recommendation willingness) mean score of 4.251 | PDF p. 12, Table 3 | Experimental result |
| Information retrieval efficiency | PU3 (Helps find academic info quickly) mean score of 4.213 | PDF p. 12, Table 3 | Experimental result |
| Interaction clarity friction | PEU3 (Interaction clarity) received lowest score at 3.894 (Moderately High) | PDF p. 12, Table 3 | Experimental result |
| Faculty pedagogical concerns | Faculty highlight risks of summary over-reliance and demand verified QA pipelines | PDF p. 12–15, Section C.1.3 | Author discussion |

## 22. Verification Checklist

- [x] PDF read (18-page research article inspected)
- [x] Introduction inspected (Information fragmentation in HE)
- [x] Related work inspected (LMS, TAM, RAG literature)
- [x] Methodology inspected (DSRM 6-phase framework)
- [x] Dataset verified (N=267 undergraduate students, N=5 faculty members)
- [x] Features verified (LMS courseware chunks, dense embeddings, multi-turn queries)
- [x] Algorithms verified (RAG pipeline, semantic similarity vector retrieval)
- [x] Architecture inspected (Figures 1, 2, and 4)
- [x] Experiments inspected (TAM survey with 10 bilingual items)
- [x] Results verified (Exact mean scores: 4.097, 4.138, 4.023, 4.129, item table)
- [x] Limitations verified (Demonstration-based, lack of SEM, Indonesian sample)
- [x] Future work verified (Longitudinal studies, SEM validation, faculty governance)
- [x] Evidence locations recorded

## 23. Verification Status

**VERIFIED**
*(Empirical DSRM and TAM study in IJOEM verified directly from source PDF with exact quantitative survey statistics and qualitative interview themes.)*
