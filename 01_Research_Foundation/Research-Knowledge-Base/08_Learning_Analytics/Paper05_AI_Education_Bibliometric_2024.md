# Paper 05 — Artificial intelligence in education: a bibliometric analysis of emerging trends

## 1. Bibliographic Information

- **Paper ID**: Paper05
- **Full Title**: Artificial intelligence in education: a bibliometric analysis of emerging trends
- **Authors**: Lim Seong Pek, Nahdatul Akma Ahmad, Faiz Zulkifli, Fatin Syamilah Che Yob, Usman Ependi, Geoffrey Rhoel C. Cruz
- **Affiliation**: Faculty of Education and Liberal Arts, INTI International University, Nilai, Malaysia; School of Education, Universiti Utara Malaysia; Department of Informatics, Universitas Bina Darma, Indonesia; Mapúa University, Manila, Philippines
- **Year**: 2026 (Published February 2026; cataloged under 2024 in earlier bib)
- **Venue**: International Journal of Evaluation and Research in Education (IJERE)
- **Volume / Issue / Pages**: Vol. 15, No. 1, February 2026, pp. 649–659
- **ISSN / DOI**: ISSN: 2252-8822, DOI: [10.11591/ijere.v15i1.34428](https://doi.org/10.11591/ijere.v15i1.34428)
- **PDF filename**: `Paper05_chen2024artificial.pdf`
- **PDF path**: `01_Research_Foundation/Papers/PDFs/Paper05_chen2024artificial.pdf`
- **Page count**: 11 pages

---

## 2. Research Problem

Despite the exponential growth of Artificial Intelligence in Education (AIEd) applications—ranging from adaptive tutoring and automated grading to predictive learning analytics and generative AI assistants—scholarly literature remains fragmented across disparate disciplines (computer science, pedagogy, medical training, ethics). Consequently, educators, developers, and policymakers lack a systematic, bibliometric mapping of the intellectual structure, emerging thematic clusters, foundational citation networks, and ethical challenges characterizing modern AIEd.

### Source Evidence
- **Page**: PDF p. 649–650 (PDF pp. 1–2)
- **Section**: Section 1 (Introduction)

---

## 3. Research Objectives

The authors explicitly define two bibliometric research objectives:
1. Analyze macro-level intellectual structures and historical research clusters in AIEd through co-citation analysis of foundational literature.
2. Identify emerging keyword trends, thematic shifts (e.g., toward Generative AI and personalized learning), and research gaps through term co-occurrence network analysis.

### Source Evidence
- **Page**: PDF p. 650 (PDF p. 2)
- **Section**: Section 1 (Introduction)

---

## 4. Research Questions

Not explicitly framed as numbered research questions; operationalized directly through the two stated bibliometric objectives:
- Objective 1: Co-citation analysis across foundational literature (2015–2024).
- Objective 2: Keyword co-occurrence analysis tracking thematic transitions.

---

## 5. Dataset

- **Dataset name**: Web of Science (WoS) AIEd Bibliometric Corpus (2015–2024)
- **Database source**: Clarivate Web of Science (Core Collection)
- **Search Query**: `(TI="artificial intelligence" OR TI="AI") AND TI="educat*"`
- **Initial search yield**: 3,017 documents retrieved
- **Screening & Eligibility**: Filtered to English-language peer-reviewed journal articles published between 2015 and 2024, yielding 946 relevant candidate articles
- **Final core corpus analyzed**: 291 seminal articles selected for comprehensive network analysis based on citation thresholds and thematic alignment
- **Total citations analyzed**: 5,246 total citations (5,001 citations excluding author self-citations; 3,525 unique citing articles)
- **Citation impact**: Average citations per article = 18.03; Corpus H-index = 42
- **Data Availability**: Derived from public Web of Science indexed records

### Source Evidence
- **Page**: PDF p. 650–651 (PDF pp. 2–3)
- **Section**: Section 2 (Method), Figure 1 (PRISMA Flowchart)

---

## 6. Features & Analytical Dimensions

In place of tabular student features, the bibliometric study maps bibliometric metadata dimensions:
- **Bibliographic Identifiers**: Document title, publication year, journal source, author affiliations, national origins.
- **Citation Metrics**: Total global citations, normalized local citations, co-citation links, H-index.
- **Textual Keywords**: Author keywords and Keyword Plus terms.
- **Co-Citation Thresholds**: Minimum citation threshold of 60 citations for co-citation cluster inclusion.
- **Co-Occurrence Thresholds**: Minimum keyword occurrence frequency of 5.

### Source Evidence
- **Page**: PDF p. 651 (PDF p. 3)
- **Section**: Section 2 (Method)

---

## 7. Data Preprocessing

- **PRISMA Protocol Filtering**: Applied multi-stage filtering from 3,017 raw WoS records to 946 eligible journal articles.
- **Full-Text Manual Review**: Checked 946 articles for subject relevance and methodological appropriateness.
- **Deduplication & Self-Citation Removal**: Automated removal of duplicate index entries and author self-citations.
- **Fractional Counting**: Used fractional counting in VOSviewer (v1.6.20) rather than full counting to ensure balanced weighting of multi-authored and interdisciplinary works.

### Source Evidence
- **Page**: PDF p. 651 (PDF p. 3)
- **Section**: Section 2 (Method), Figure 1

---

## 8. Algorithms and Models

- **Bibliometric Mapping Software**: VOSviewer (version 1.6.20).
- **Network Construction Algorithms**:
  - VOS (Visualization of Similarities) clustering technique for co-citation and keyword co-occurrence maps.
  - Normalized citation weight association strength normalization.
- **Co-Citation Clustering**: Identified 5 distinct intellectual clusters (Table 1).
- **Co-Occurrence Thematic Clustering**: Grouped high-frequency keywords into 4 emerging research themes (Table 2).

### Source Evidence
- **Page**: PDF p. 651–653 (PDF pp. 3–5)
- **Section**: Section 2, Section 3.1, Section 3.2

---

## 9. Architecture

The research pipeline comprises four sequential phases:
1. **Search & Identification**: WoS query formulation and raw record retrieval ($N = 3,017$).
2. **PRISMA-Guided Screening**: Inclusion/exclusion filtering, language restriction, peer-review validation ($n = 946$).
3. **Core Corpus Selection**: Threshold filtering for high-impact analysis ($n = 291$, H-index = 42).
4. **VOSviewer Analytics & Synthesis**: Dual co-citation and co-occurrence network extraction, cluster labeling, and policy translation.

### Source Evidence
- **Page**: PDF p. 651 (PDF p. 3)
- **Figure**: Figure 1 (PRISMA Flowchart)

---

## 10. Methodology

1. Formulate boolean search string targeting title occurrences of AI and Education in Web of Science.
2. Filter documents according to temporal window (2015–2024) and document type (journal articles only).
3. Export complete bibliographic and citation data.
4. Execute co-citation analysis in VOSviewer (min citation threshold = 60) to identify foundational intellectual roots.
5. Execute keyword co-occurrence analysis (min occurrence = 5) to map the evolution from early adaptive tutors to generative LLMs.
6. Perform qualitative thematic synthesis of identified clusters and extract policy implications.

### Source Evidence
- **Page**: PDF p. 650–652 (PDF pp. 2–4)
- **Section**: Section 2, Section 3

---

## 11. Experimental Setup

- **Database**: Clarivate Web of Science (WoS Core Collection).
- **Software**: VOSviewer 1.6.20.
- **Counting Mode**: Fractional counting.
- **Thresholds**: Co-citation citation count $\ge 60$; keyword occurrence count $\ge 5$.

### Source Evidence
- **Page**: PDF p. 651 (PDF p. 3)
- **Section**: Section 2 (Method)

---

## 12. Evaluation Metrics

- Total Publications ($N = 291$)
- Total Citation Count ($TC = 5,246$; $5,001$ without self-citations)
- Average Citations Per Paper ($18.03$)
- Corpus H-Index ($H = 42$)
- Total Link Strength (TLS) in VOSviewer network graphs
- Cluster Modularity & Co-occurrence Frequency

### Source Evidence
- **Page**: PDF p. 651–654 (PDF pp. 3–6)
- **Section**: Section 2, Table 1, Table 2

---

## 13. Results

### 13.1 Co-Citation Clusters (Table 1, PDF p. 652):
1. **Cluster 1 (Red - Conceptual Frameworks & Theoretical Foundations)**: Foundational theoretical paradigms of intelligent tutoring systems, learner modeling, and educational data mining (key authors: Zawacki-Richter, Roll, Holmes).
2. **Cluster 2 (Green - Ethical Governance & Bias)**: AI ethics, privacy safeguards, algorithmic transparency, and responsible AI policy.
3. **Cluster 3 (Blue - Generative AI & Large Language Models)**: Emerging post-2022 explosion of ChatGPT, automated writing feedback, and prompt engineering in education.
4. **Cluster 4 (Yellow - Systematic Reviews & Meta-Analyses)**: Meta-syntheses examining learning analytics efficacy and student retention.
5. **Cluster 5 (Purple - Medical & Clinical Education)**: Simulation-based training, diagnostic tutoring, and clinical reasoning in healthcare education.

### 13.2 Emerging Keyword Trends (Section 3.2, PDF p. 653–654):
- Shift from traditional "expert systems" and "machine learning" toward "ChatGPT", "large language models", "generative AI", "AI literacy", and "personalized learning".
- Sharp post-2022 pivot toward ethical governance, academic integrity, and bias mitigation.

### Source Evidence
- **Page**: PDF p. 651–655 (PDF pp. 3–7)
- **Tables & Figures**: Table 1, Table 2, Figure 2, Figure 3

---

## 14. Baselines

Not applicable (bibliometric mapping study; benchmarks historical AIEd trends from 2015 against modern 2024 developments).

---

## 15. Ablation Study

Not applicable.

---

## 16. Explainability

Explainability is discussed as a critical emergent cluster (Cluster 2) in AIEd literature:
- Emphasizes that high-stakes educational decisions (grading, placement, admissions) cannot rely on black-box algorithms.
- Synthesizes literature calling for transparent learner models, interpretable dashboards, and student data privacy protections.

### Source Evidence
- **Page**: PDF p. 654–655 (PDF pp. 6–7)
- **Section**: Section 3.1, Section 4 (Discussion)

---

## 17. Main Findings

1. **Exponential Rise Post-2022**: The AIEd landscape experienced a massive inflection point following the introduction of generative AI (ChatGPT), which rapidly shifted research from niche adaptive systems to mainstream educational policy and academic integrity debates.
2. **Emergence of AI Literacy as a Core Construct**: Research increasingly emphasizes that preparing students and faculty with "AI Literacy" (understanding AI capabilities, limitations, and ethics) is as important as deploying AI tools.
3. **The Global Resource Divide**: Research disproportionately addresses well-funded institutional contexts; there is a critical scarcity of empirical research investigating how AI tools perform in high-class-size, low-bandwidth, and multilingual settings.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Single Database Scope**: Literature search was conducted exclusively within Clarivate Web of Science; relevant publications indexed exclusively in Scopus, IEEE Xplore, or arXiv were omitted.
- **Title-Field Restriction**: Search syntax was constrained to the title field (`TI=`), which ensured high thematic precision but may have excluded relevant papers mentioning AIEd terms only in abstracts or keywords.
- **English Language Limitation**: Non-English studies were excluded, potentially creating regional and language selection bias.

### 18.2 Research Interpretation
- *Research team interpretation*: The paper provides a high-level quantitative overview of publication trends and citation clusters, but does not benchmark specific algorithm implementations or compare empirical model accuracies.

---

## 19. Future Work

Explicitly proposed by the authors:
1. Conduct multi-database bibliometric reviews combining Web of Science, Scopus, and IEEE Xplore.
2. Investigate longitudinal studies evaluating the long-term impact of generative AI tutors on student cognitive retention and critical thinking.
3. Develop multidisciplinary frameworks examining digital equity and accessible AI for resource-limited educational communities.

### Source Evidence
- **Page**: PDF p. 655 (PDF p. 7)
- **Section**: Section 4 (Discussion), Future Directions

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Relevant PRIE Module**: Overall ecosystem positioning, `08_Learning_Analytics`, and `06_RAG`.
- **Bibliometric Justification**: Directly substantiates ScholarCamp's dual focus on Generative AI (LLMs for interview practice and question generation) alongside strict ethical transparency, explainable AI, and skill gap remediation.
- **Curricular Grounding**: Confirms that AI Literacy and explainable decision support are globally recognized research priorities in higher education.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Corpus Size & Impact | 291 core papers analyzed; 5,246 citations; H-index = 42 | PDF p. 651, Section 2 | Experimental result |
| Identification Protocol | 3,017 initial WoS records narrowed to 946 eligible journal articles | PDF p. 651, Fig 1 | Methodology |
| 5 Co-Citation Clusters | Conceptual Foundations, Ethics/Policy, Generative AI, Reviews, Medical | PDF p. 652, Table 1 | Table |
| Search Syntax Specification | `(TI="artificial intelligence" OR TI="AI") AND TI="educat*"` | PDF p. 651, Section 2 | Methodology |
| Post-2022 Generative AI Pivot | Cluster 3 (ChatGPT, LLMs) emerged as fastest-growing research axis | PDF p. 653, Section 3.1 | Author discussion |
| Limitation: Single Database | Analysis limited to Web of Science, omitting non-WoS literature | PDF p. 655, Section 4 | Author discussion |

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

**VERIFIED** (Fully verified from primary PDF source: `Paper05_chen2024artificial.pdf`, 11 pages).
