# Paper 43 — Transforming OPACs into Intelligent Discovery Systems: An AI-Powered, Knowledge Graph-Driven Smart OPAC for Digital Libraries

## 1. Bibliographic Information

- **Paper ID**: Paper43
- **Full Title**: Transforming OPACs into Intelligent Discovery Systems: An AI-Powered, Knowledge Graph-Driven Smart OPAC for Digital Libraries
- **Authors**: M. S. Rajeevan (1, *), B. Mini Devi (1)
  - *(1) Department of Library and Information Science, University of Kerala, Trivandrum, Kerala, India*
  - *Email: rajeevanms_2025@keralauniversity.ac.in*
- **Year**: 2026 (Preprint / Journal Submission incorporating late-2025/2026 benchmarks)
- **Venue**: Department of Library and Information Science, University of Kerala Research Monograph
- **DOI**: *Not explicitly reported / In press*
- **PDF filename**: `Paper43_knowledge2026transforming.pdf`
- **PDF path**: `Papers/PDFs/Paper43_knowledge2026transforming.pdf`
- **Page count**: 17 pages
- **Metadata Note / Discrepancy**: The PDF filename indicates `knowledge2026transforming`, but the actual printed authors on PDF p. 1 are M. S. Rajeevan and B. Mini Devi from University of Kerala, Trivandrum, India.

## 2. Research Problem

Conventional Online Public Access Catalogues (OPACs) in academic and digital libraries are increasingly obsolete in the face of exponential scholarly literature expansion. Traditional systems rely on rigid keyword matching, boolean queries (AND/OR/NOT), and static Dewey/LC classification schemes that fail to comprehend user intent, context, or semantic interconnections. Consequently, searches yield either catastrophic zero-hit queries or massive unranked lists of irrelevant records, precipitating severe information overload and negative user experiences.

### Source Evidence
- PDF p. 1–2, Abstract & Section 1 — Introduction.
- PDF p. 5, Section 3.4 — Performance Evaluation Strategy.

## 3. Research Objectives

1. Design and evaluate an architectural framework (**Smart OPAC**) transforming conventional library catalogs into intelligent discovery systems using Artificial Intelligence, semantic embeddings, and Knowledge Graph (KG) modeling.
2. Implement multi-source scholarly data orchestration integrating Europe PMC, OpenAlex, and Semantic Scholar.
3. Quantify retrieval latency ($ART_s$) and information overload reduction percentage ($Reduction\%$) across complex multidisciplinary queries.
4. Construct and visualize hierarchical thematic knowledge graphs demonstrating noise reduction and conceptual clustering.

### Source Evidence
- PDF p. 1, Abstract; PDF p. 5–6, Section 3 — Methodology.

## 4. Research Questions

- *Not explicitly reported in numbered academic RQ list.* The research is guided by core design objectives evaluating whether semantic filtering and knowledge graphs enhance precision, eliminate information overload, and reveal interdisciplinary connections over keyword search.

## 5. Dataset

The system ingests and processes scholarly records from three major public scientific repositories:
- **Corpus Data Sources**:
  - **Europe PMC**: Open-access biomedical and life sciences repository providing rich structured abstracts and standardized MeSH annotations.
  - **OpenAlex**: Global open scholarly graph containing metadata across 250M+ scientific publications.
  - **Semantic Scholar**: AI-powered scientific literature engine providing targeted semantic citation and paper search APIs.
- **Evaluation Sample**:
  - 110 total papers retrieved across 11 multi-source query batches:
    - Europe PMC: 50 papers retrieved across 5 query sets (PDF p. 6, Table 1).
    - OpenAlex: 50 papers retrieved across 5 query sets (PDF p. 6, Table 1).
    - Semantic Scholar: 10 papers retrieved across 1 selective query set (PDF p. 6, Table 1).
- **Test Query Suite**: Five representative Library and Information Science (LIS) research queries:
  1. *"Library Recommendation Systems"*
  2. *"Knowledge Graph in Digital Libraries"*
  3. *"AI in OPAC"*
  4. *"Semantic Search Libraries"*
  5. *"Information Retrieval LIS"*

### Source Evidence
- PDF p. 6, Section 4.1 & Table 1; PDF p. 9–10, Section 4.4 & Figure 3.

## 6. Features

The system extracts and computes multi-tiered semantic features:
- **Textual & Bibliographic Metadata**: Article titles, author-provided keywords, structured abstracts, publication venues, and publication years.
- **Semantic Dense Embeddings**: 384-dimensional or 768-dimensional dense vector embeddings generated via pre-trained Transformer language models (Sentence-BERT / SBERT).
- **Extracted Keyword Entities**: Keyphrases extracted using KeyBERT representing core conceptual themes.
- **Graph Topology Features**: Entity nodes (authors, topics, methodologies, algorithms) and relational edges (thematic similarity, citation linkage, cross-disciplinary co-occurrence).

## 7. Data Preprocessing

The end-to-end Smart OPAC processing workflow follows five stages (PDF p. 5–6, Figure 1):
1. **Multi-Source Query Execution**: Dispatches user search terms in parallel to Europe PMC, OpenAlex, and Semantic Scholar REST APIs.
2. **Abstract & Metadata Parsing**: Ingests raw JSON/XML API responses, filtering null records and cleaning textual noise.
3. **Semantic Embedding Generation**: Passes extracted titles and abstracts through Sentence-BERT to generate dense contextual semantic vectors.
4. **KeyBERT Keyword & Theme Extraction**: Identifies candidate domain concepts and technical entities.
5. **Thematic Cosine Filtering & Graph Construction**: Filters candidate papers based on semantic similarity thresholds against user-specified target themes and maps surviving records into an interactive knowledge graph.

## 8. Algorithms and Models

- **Sentence-BERT (SBERT)**: Sentence-Transformers embedding framework used to map titles and abstracts into a shared semantic vector space (PDF p. 1–2, 5).
- **KeyBERT**: BERT-embeddings-based keyword extraction algorithm utilized for automated thematic indexing (PDF p. 5, 15).
- **Cosine Semantic Similarity Filtering**: Measures angle between user query vector and candidate paper vectors to filter out irrelevant or peripheral documents.
- **NetworkX / Graph Modeling**: Knowledge graph generation mapping interconnected themes, ontology networks, and conceptual clusters (PDF p. 10–13, Figures 4, 5, 6).

### Source Evidence
- PDF p. 1–2, Abstract & Introduction; PDF p. 5–6, Section 3.3–3.5 & Figure 1; PDF p. 10–13.

## 9. Architecture

The Smart OPAC architectural pipeline is structured into three functional tiers (PDF p. 5–6, Figure 1):
1. **Data Orchestration & Harvesting Tier**: Interfaces with external open APIs (Europe PMC, OpenAlex, Semantic Scholar) for concurrent multi-source retrieval.
2. **Semantic Transformation & Graph Core**: Executes SBERT vectorization, KeyBERT keyword extraction, cosine filtering, and graph topology generation.
3. **Interactive User Discovery Tier**: Replaces traditional flat OPAC lists with an exploratory UI providing semantic search, thematic faceted filtering, and visual Knowledge Graph navigation.
- **Architecture Diagram**: Figure 1 on PDF p. 6 illustrates the workflow of the semantic scholarly retrieval and filtering framework.

## 10. Methodology

1. **System Architecture Design**: Structuring an API-driven, embedding-powered discovery layer on top of catalog interfaces.
2. **Query Suite Formulation**: Selecting 5 representative, multi-disciplinary domain queries with varying degrees of semantic ambiguity.
3. **Empirical Benchmarking**: Measuring retrieval latency ($ART_s$) per source across execution logs.
4. **Information Overload Reduction Calculation**: Quantifying the ratio of filtered vs. raw retrieved documents.
5. **Iterative Graph Visualization**: Generating 3 sequential knowledge graph visualizations (unfiltered base graph $\rightarrow$ filtered themes $\rightarrow$ isolated deep semantic clusters) to demonstrate noise reduction.

## 11. Experimental Setup

- **Software Framework**: Python, SentenceTransformers (SBERT), KeyBERT, NetworkX, Matplotlib.
- **Target Repositories**: Europe PMC REST API, OpenAlex API, Semantic Scholar API.
- **Logging & Measurement**: System-level execution time logs recording query dispatch to final payload receipt.

## 12. Evaluation Metrics

- **Average Retrieval Time per Source ($ART_s$)**:
  $$ART_s = \frac{1}{n} \sum_{i=1}^{n} t_i$$
  where $t_i$ is retrieval time for query $i$ in seconds (PDF p. 5, Section 3.4).
- **Information Overload Reduction Percentage ($Reduction\%$):**
  $$Reduction(\%) = \left(1 - \frac{P_{\text{filtered}}}{P_{\text{retrieved}}}\right) \times 100$$
  where $P_{\text{filtered}}$ is the count of items retained after semantic filtering and $P_{\text{retrieved}}$ is total initial retrieved records (PDF p. 5, Section 3.4).
- **Thematic Graph Structural Clarity**: Qualitative visual assessment of modular subgraphs and noise elimination across Figures 4, 5, and 6.

## 13. Results

### Retrieval Performance Across Scholarly Sources (Table 1, PDF p. 6):
- **Semantic Scholar**: Average retrieval time = **1.124 seconds** (fastest response; 10 papers retrieved across 1 query).
- **Europe PMC**: Average retrieval time = **1.318 seconds** (highly efficient; 50 papers retrieved across 5 queries).
- **OpenAlex**: Average retrieval time = **3.646 seconds** (highest latency; 50 papers retrieved across 5 queries).

### Information Overload Reduction by Query & Source (PDF p. 9–10, Figure 3):
- **High Complexity Queries**:
  - *"AI in OPAC"*: Achieved approximately **90% reduction** in irrelevant literature in Europe PMC.
  - *"Information Retrieval LIS"*: Achieved approximately **90% reduction** in Europe PMC.
- **Moderate Complexity Queries**:
  - *"Library Recommendation Systems"*: Achieved **$> 70\%$ reduction** in Europe PMC (vs. 0% in OpenAlex).
  - *"Knowledge Graph in Digital Libraries"*: Achieved **$> 60\%$ reduction** in Europe PMC (vs. 10% in OpenAlex).
- **Low Complexity Queries**:
  - *"Semantic Search Libraries"*: 0% reduction in Semantic Scholar due to restrictive upstream API filtering.
- **Key Insight**: Europe PMC achieved the strongest semantic discrimination due to standardized MeSH annotations and rich structured abstracts, proving that repository metadata quality directly governs downstream semantic filtering efficiency.

### Knowledge Graph Discovery Visualizations (PDF p. 10–13, Figures 4–6):
- **Knowledge Graph 1 (Unfiltered Theme Space, Figure 4)**: Captures wide, noisy interdisciplinary connections (digital humanities, oncology intelligence, ontology networks).
- **Knowledge Graph 2 (Filtered Semantic Themes, Figure 5)**: Filters network noise, revealing clean thematic boundaries (adaptive semantic benchmarking, data management, digital humanities).
- **Knowledge Graph 3 (Deep Semantic Subgraphs, Figure 6)**: Isolates tightly interconnected technical clusters (information innovation, networks ontology, retrieval frameworks, semantic retrieval).

## 14. Baselines

- Traditional keyword-based OPAC systems using exact string matching and Boolean queries, and unfiltered multi-source API search results without semantic embedding layers.

## 15. Ablation Study

- Progressively evaluated three stages of knowledge graph refinement (unfiltered baseline vs. thematic filtered vs. cluster isolated), demonstrating progressive elimination of cross-domain noise.

## 16. Explainability

- **Visual Graph Topology as Explainability**: By visualizing nodes (concepts) and edges (thematic relationships), users can immediately understand *why* a document was retrieved or recommended, moving beyond the "black-box" list paradigm of conventional search engines (PDF p. 10–13).

## 17. Main Findings

1. Semantic embedding layers and Knowledge Graph representations successfully modernize traditional catalog systems, reducing information overload by up to 90% on conceptually complex queries.
2. Metadata richness governs semantic filtering performance: repositories with structured abstracts and standardized taxonomies (Europe PMC) yield significantly higher discrimination than broad, shallow graphs.
3. Multi-source API orchestration balances comprehensive indexing (OpenAlex, Europe PMC) with low latency (Semantic Scholar: 1.124s, Europe PMC: 1.318s).
4. Graph-based discovery enables exploratory and serendipitous learning, revealing non-obvious cross-domain links that keyword indexing misses completely.

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Limited Evaluation Scale**: Evaluated across a restricted set of 5 test queries and 110 retrieved papers (PDF p. 14, Section 6).
- **Absence of User Usability Testing**: No human-centered usability evaluation (e.g., SUS or TAM) was conducted with librarians or students (PDF p. 14).
- **Static Knowledge Graphs**: Knowledge graphs were generated offline post-retrieval rather than dynamically updated in real-time streaming pipelines (PDF p. 15).

### 18.2 Research Interpretation
- **Target Domain Scope**: While focused on digital libraries, the architectural principles of multi-source semantic filtering and knowledge graph visualization apply directly to automated career discovery and curriculum recommendation.

## 19. Future Work

Explicitly proposed by the authors (PDF p. 14–15, Section 6):
1. Expanding coverage to additional open scholarly repositories and institutional digital repositories.
2. Implementing user interaction analytics, student search session tracking, and personalized recommendation based on user profiles.
3. Deploying dynamic real-time knowledge graph updates and automated ontology learning.

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Direct Application to PRIE Recommendation & Skill Discovery**: Rajeevan & Mini Devi provides the exact algorithmic blueprint for ScholarCamp's Recommendation and Learning Analytics engine (`07_Recommendation/`).
- **Overcoming Keyword Search in Job & Course Discovery**: Students searching for career tracks face the exact same "information overload" as OPAC users. Using SBERT embeddings and Knowledge Graphs allows ScholarCamp to recommend learning resources, certifications, and job openings based on deep semantic match rather than crude keyword overlap.
- **Thematic Noise Reduction**: The paper's finding that semantic filtering reduces irrelevancy by up to 90% provides empirical justification for incorporating SBERT-based cosine filtering before presenting skill gap remediation roadmaps to students.

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|---|---|---|---|
| Fastest retrieval latency | Semantic Scholar (1.124s) and Europe PMC (1.318s) achieved lowest latency | PDF p. 6, Table 1 | Experimental result |
| Maximum overload reduction | "AI in OPAC" and "Information Retrieval LIS" achieved ~90% reduction | PDF p. 9–10, Section 4.4 | Experimental result |
| Metadata impact on filtering | Rich structured abstracts in Europe PMC enable superior discrimination over OpenAlex | PDF p. 9–10, Section 4.4 | Author discussion |
| Knowledge graph noise reduction | Progressive filtering across Figures 4–6 isolates core semantic clusters | PDF p. 10–13, Figures 4, 5, 6 | Experimental result |
| Limitations | Evaluation limited to 5 queries; lacks human usability testing | PDF p. 14, Section 6 | Author discussion |

## 22. Verification Checklist

- [x] PDF read (17-page research article inspected)
- [x] Introduction inspected
- [x] Related work inspected (Semantic search & digital libraries)
- [x] Methodology inspected (5-stage semantic retrieval and filtering pipeline)
- [x] Dataset verified (Europe PMC, OpenAlex, Semantic Scholar; 110 papers, 5 queries)
- [x] Features verified (Titles, structured abstracts, SBERT embeddings, KeyBERT entities)
- [x] Algorithms verified (Sentence-BERT, KeyBERT, Cosine Similarity, Knowledge Graph)
- [x] Architecture inspected (Figure 1: Multi-source workflow)
- [x] Experiments inspected (Log-based retrieval latency and overload reduction formulas)
- [x] Results verified (Exact latency: 1.124s, 1.318s, 3.646s; ~90% reduction)
- [x] Limitations verified (Limited queries, lack of user testing, static graphs)
- [x] Future work verified (Dynamic KGs, personalization, expanded repositories)
- [x] Evidence locations recorded

## 23. Verification Status

**VERIFIED**
*(Empirical information science and knowledge graph study verified directly from source PDF with exact latency numbers, mathematical formulas, and multi-source reduction percentages.)*
