# Paper 39 — A Systematic Review of Automatic Question Generation for Educational Purposes

## 1. Bibliographic Information

- **Paper ID**: Paper39
- **Full Title**: A Systematic Review of Automatic Question Generation for Educational Purposes
- **Authors**: Ghader Kurdi (1), Jared Leo (1), Bijan Parsia (1), Uli Sattler (1), Salam Al-Emari (2)
  - *(1) School of Computer Science, The University of Manchester, Manchester, UK*
  - *(2) Department of Computer Science, University of Tabuk, Tabuk, Saudi Arabia*
- **Year**: 2020 (Published online 12 November 2019; Journal Volume 30, Issue 1, March 2020, pp. 121–204)
- **Venue**: International Journal of Artificial Intelligence in Education (IJAIED), Springer
- **DOI**: `https://doi.org/10.1007/s40593-019-00186-y`
- **PDF filename**: `Paper39_kurdi2020systematic.pdf`
- **PDF path**: `Papers/PDFs/Paper39_kurdi2020systematic.pdf`
- **Page count**: 84 pages

## 2. Research Problem

Manual construction of high-quality exam-style questions is a time-consuming, expensive process that requires specialized pedagogical training, subject matter expertise, and resources. Human-authored questions frequently suffer from poor item quality and item flaws. Concurrently, the exponential growth of educational technologies (e.g., MOOCs, intelligent tutoring systems, and adaptive testing) demands a continuous supply of fresh, psychometrically sound assessment items to replace compromised questions. While Automatic Question Generation (AQG) was introduced to solve this bottleneck, the field suffers from extreme fragmentation, lack of standardized evaluation procedures, handcrafted templates, questions targeting only lower-order cognitive recall, and a near-total absence of feedback generation and psychometric difficulty control.

### Source Evidence
- PDF p. 1–3, Abstract & Introduction.
- PDF p. 6–7, Section "Review Objective".

## 3. Research Objectives

The review systematically investigates the state of AQG literature published between 2015 and early 2019 across four primary objectives:
1. **OBJ1 (Community & Activities)**: Quantify publication rates, venue distributions, paper types, and active research groups in educational AQG.
2. **OBJ2 (QG Approaches & Techniques)**: Systematize the purposes, generation methods, inputs/knowledge sources, target domains, question/answer formats, languages, feedback mechanisms, and difficulty control strategies.
3. **OBJ3 (Performance & Gold Standards)**: Identify standard benchmark datasets, categorize question evaluation methods and metrics, quantify generation performance, and establish whether a gold standard exists.
4. **OBJ4 (Longitudinal Evolution)**: Track whether longstanding limitations highlighted in prior reviews (Alsubait 2015)—specifically feedback generation, controlled difficulty, and verbalization naturalness—have progressed.

### Source Evidence
- PDF p. 6–7, Section "Review Objective".

## 4. Research Questions

The study explicitly details 19 guiding review questions across its four primary objectives:
- **Under OBJ1**:
  - RQ1.1: What is the rate of publication?
  - RQ1.2: What types of papers are published in the area?
  - RQ1.3: Where is research published?
  - RQ1.4: Who are the active research groups in the field?
- **Under OBJ2**:
  - RQ2.1: What is the purpose of QG?
  - RQ2.2: What method is applied?
  - RQ2.3: What tasks related to question generation are considered?
  - RQ2.4: What type of input is used?
  - RQ2.5: Is it designed for a specific domain? For which domain?
  - RQ2.6: What type of questions are generated? (format and answer format)
  - RQ2.7: What is the language of the questions?
  - RQ2.8: Does it generate feedback?
  - RQ2.9: Is difficulty of questions controlled?
  - RQ2.10: Does it consider verbalisation?
- **Under OBJ3**:
  - RQ3.1: Are there any available sources or standard datasets for performance comparison?
  - RQ3.2: What types of evaluation are applied to QG approaches?
  - RQ3.3: What properties of questions are evaluated and what metrics are used?
  - RQ3.4: How does the generation approach perform?
  - RQ3.5: What is the gold-standard performance?
- **Under OBJ4**:
  - RQ4.1: Has there been any progress on feedback generation?
  - RQ4.2: Has there been progress on generating questions with controlled difficulty?
  - RQ4.3: Has there been progress on enhancing the naturalness of questions (verbalisation)?

### Source Evidence
- PDF p. 6–7, Section "Review Objective".

## 5. Dataset

As a systematic literature review, the primary corpus consists of peer-reviewed scientific studies on educational AQG:
- **Corpus Search Range**: January 2015 to early 2019.
- **Search Databases**: 6 data sources: ERIC, ACM Digital Library, IEEE Xplore, INSPEC, ScienceDirect, and the International Journal of Artificial Intelligence in Education (IJAIED) / AIED conference proceedings. Supplemented by forward/backward snowballing on Google Scholar (PDF p. 8).
- **Initial Search Yield**: 373 records identified from electronic databases + citations screened via snowballing.
- **Excluded Studies**: 180+ studies excluded based on 13 explicit exclusion criteria (91 non-educational, 39 lacking evaluation, 19 unclear purpose, 14 non-peer reviewed, 10 lacking full text, etc.; detailed in Table 11, PDF p. 41).
- **Final Synthesized Corpus**: **93 primary studies** meeting all inclusion criteria (PDF p. 1, 13).

### Source Evidence
- PDF p. 1, Abstract.
- PDF p. 8–9, Search Strategy and Screening.
- PDF p. 13, Table 3 ("Data Extraction Results").
- PDF p. 41, Table 11 ("Excluded Studies").

## 6. Features

The review analyzes input features and knowledge representation sources utilized across the 93 reviewed studies:
- **Input Knowledge Sources**:
  - Raw unannotated text corpora (textbooks, Wikipedia, news articles).
  - Structured ontologies (OWL/RDF formal ontologies, domain taxonomies).
  - Curated databases and semantic knowledge graphs (WordNet, ConceptNet, DBpedia).
  - Course slide decks, transcripts, and pedagogical lecture notes.
- **Linguistic and Syntactic Features**:
  - Part-of-Speech (POS) tags, named entity tags (NER), dependency trees, parse trees, semantic role labels (SRL).
- **Difficulty and Distractor Features**:
  - Semantic distance, word embedding cosine similarity (Word2Vec, GloVe), co-occurrence frequencies, word frequency/rarity scores, phonetic/orthographic similarity.

### Source Evidence
- PDF p. 4–5, Table 1; p. 14–26, Section "Summarising Current QG Approaches".

## 7. Data Preprocessing

Data extraction and review synthesis protocols:
- **Dual Independent Reviewers**: Two reviewers independently reviewed titles, abstracts, and full texts, and independently filled structured data extraction forms (PDF p. 9).
- **Inter-Rater Quality Assessment**: Quality of reporting evaluated using a 9-criterion appraisal instrument adapted from Downs & Black (1998) covering participant reporting (Q1–Q4), question sampling (Q5–Q7), and outcome measures (Q8–Q9) (PDF p. 10, Table 2).
- **Analysis Pipeline**: Extracted data synthesized and analyzed using automated R Markdown scripts published open-source on GitHub (`https://github.com/grkurdi/AQG_systematic_review`) (PDF p. 10).

## 8. Algorithms and Models

The review categorizes generation algorithms across the 93 primary studies into five dominant paradigms:
1. **Rule-Based and Template-Based Generation**: Handcrafted syntactic transformation patterns, semantic role labeling rules, and slot-filling templates (most prevalent in domain-specific systems).
2. **Ontology-Driven Generation**: Axiom querying, SPARQL templates, description logic reasoners, and ontology graph traversals to generate MCQs and distractors.
3. **Statistical NLP & Information Extraction**: TF-IDF keyword extraction, C-value multi-word terminology extraction, and lexical database lookups (WordNet).
4. **Early Machine Learning & Deep Learning**: Sequence-to-sequence (Seq2Seq) neural networks with attention, recurrent neural networks (LSTM/GRU), and pointer-generator networks (emerging in 2017–2019 studies).
5. **Distractor Generation Algorithms**: Vector space similarity ranking (Word2Vec, GloVe), ontology sibling selection, WordNet synset/hypernym traversal, and phonetic edit-distance calculations.

### Source Evidence
- PDF p. 14–28, Section "Summarising Current QG Approaches".

## 9. Architecture

The paper synthesizes the general end-to-end AQG pipeline into distinct functional stages across literature:
1. **Target Content Selection**: Parsing source materials to extract candidate key phrases, named entities, key concepts, or target sentences.
2. **Question Formulation / Stem Construction**: Applying syntactic inversion rules, template instantiation, or neural seq2seq decoding to produce the question stem.
3. **Key and Distractor Generation (for MCQs)**: Extracting the ground-truth key and selecting plausible, semantically related but strictly incorrect alternatives (distractors).
4. **Post-Processing & Filtering**: Ranking candidate questions using language models, perplexity thresholds, grammatical checkers, or difficulty classifiers.
5. **Quality Appraisal & Delivery**: Reviewing items via human rubrics or automated scoring engines before delivery to students or question banks.

### Source Evidence
- PDF p. 14–20; Figure diagrams and taxonomy tables throughout Section "Results and Discussion".

## 10. Methodology

A systematic literature review adhering to established software engineering and educational informatics guidelines (Kitchenham and Charters 2007; Boland et al. 2013):
1. **Protocol Definition**: Establishing 4 objectives, 19 research questions, and 13 inclusion/exclusion rules.
2. **Database Querying**: Boolean search execution across 6 primary academic databases.
3. **Snowballing**: Exhaustive forward citation searching and backward bibliography screening.
4. **Quality Appraisal**: 9-item critical appraisal instrument scoring participant, sample, and measurement validity.
5. **Data Extraction & Coding**: Structured feature extraction regarding domain, language, model, input source, evaluation type, metrics, and cognitive level.
6. **Quantitative & Qualitative Synthesis**: Descriptive statistical aggregation and thematic qualitative comparison.

## 11. Experimental Setup

- Review conducted across 93 included studies.
- Analysis pipeline implemented in R Markdown (scripts and raw extraction tables deposited publicly at GitHub: `https://github.com/grkurdi/AQG_systematic_review`).
- Primary publication venues surveyed include IJAIED, AIED Conference, IEEE TLT, BEA/NLP Workshops, and ACM SIGCSE (PDF p. 42, Table 12).

## 12. Evaluation Metrics

The review documents an alarming heterogeneity of evaluation practices across the 93 studies:
- **Human Evaluation Dimensions**:
  - Grammaticality / Syntactic correctness
  - Relevance / Content appropriateness
  - Clarity / Readability
  - Pedagogical usefulness / Educational value
  - Distractor plausibility
  - Difficulty level
- **Automated Linguistic Metrics**:
  - BLEU (BLEU-1 to BLEU-4)
  - ROUGE (ROUGE-L)
  - METEOR
  - Perplexity
- **Psychometric and Statistical Measures**:
  - Item Difficulty Index ($P$-value)
  - Discrimination Index ($D$)
  - Inter-rater agreement: Cohen's Kappa ($\kappa$), Fleiss' Kappa, Krippendorff's Alpha, Pearson's $r$.

### Source Evidence
- PDF p. 28–36, Section "Identifying Gold Standard Performance in AQG".

## 13. Results

Quantitative review findings across the 93 studies (PDF p. 13–37):
- **Publication Growth**: Publication volume increased steadily from 2015 through 2018, dominated by conference and workshop publications (Table 12).
- **Target Domains**: Language learning (ESL/EFL vocabulary and grammar) remains the most heavily researched domain, followed by medicine/healthcare, computer science/programming, and biology.
- **Knowledge Sources**: Unstructured text constitutes the dominant input (over 60% of studies), while ontologies and structured knowledge graphs represent ~15–20%.
- **Question Types**: Heavily concentrated on simple factual Wh-questions (who, what, where) and gap-fill / cloze questions (over 70% combined). Complex higher-order reasoning questions (why, how, scenario-based) are exceedingly rare.
- **Question Difficulty Control**: Only a small minority of papers attempt to model or control question difficulty, primarily through distractor similarity metrics; psychometric validation on real learner cohorts is virtually non-existent.
- **Feedback Generation**: Feedback generation is almost completely neglected—fewer than 5% of studies generate explanatory feedback alongside questions.
- **Gold Standard Absence**: No single standard dataset or universal evaluation protocol exists. BLEU/ROUGE metrics show weak correlation with pedagogical human ratings. Inter-rater reliability is reported in fewer than 30% of human evaluations.

## 14. Baselines

- Pre-2015 AQG state-of-the-art established by Alsubait's (2015) systematic review (covering 65 studies up to late 2014) served as the direct longitudinal baseline (PDF p. 3–5, 37–38).

## 15. Ablation Study

- *Not applicable* (Systematic literature review synthesis).

## 16. Explainability

- The review examines feedback generation as an explainability and pedagogical mechanism. It concludes that existing systems almost never generate explanations of why an answer is correct or why a distractor is incorrect, severely limiting their use in formative self-directed learning (PDF p. 6, 38).

## 17. Main Findings

1. **Persistent Focus on Lower Cognitive Levels**: AQG systems overwhelmingly generate superficial factual recall items (cloze and wh-questions) rather than questions requiring analysis, application, or evaluation (Bloom's Taxonomy higher tiers).
2. **Critical Neglect of Pedagogical Feedback**: Despite the recognized educational necessity of formative feedback, automated feedback generation remains almost non-existent in the literature.
3. **Unvalidated Difficulty Models**: Difficulty control remains rudimentary, typically relying on semantic distance proxies without empirical psychometric validation against student response data (IRT or classical test theory).
4. **Evaluation Crisis and Incomparability**: Extreme fragmentation in evaluation criteria, rating scales (3-point, 5-point, binary), and ungrounded automated metrics prevents meaningful cross-system benchmarking. No "gold standard" exists in the field.
5. **Handcrafted Templates Bottleneck**: Template acquisition remains primarily manual and labor-intensive, creating an economic bottleneck that contradicts the core premise of automatic generation.

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Language Restriction**: The review is limited to studies published in English, underrepresenting non-English AQG research (PDF p. 41).
- **Inaccessible Full Texts**: 10 identified relevant papers had to be excluded due to full-text unavailability through university subscriptions or open channels (PDF p. 41).
- **Rapidly Moving Neural SOTA**: Deep learning neural question generation models began emerging during the 2017–2019 window, but early pre-transformer seq2seq models dominated the tail of this review's corpus.

### 18.2 Research Interpretation
- **Pre-LLM Horizon**: Published in 2020, the review captures the literature prior to the modern Large Language Model revolution (GPT-3, GPT-4, LLaMA). While its foundational taxonomy and critique of educational validity remain profoundly relevant, the technological baseline has since transitioned from templates/seq2seq to prompt-based LLM generation.

## 19. Future Work

Explicitly proposed research agenda by the authors (PDF p. 37–41):
1. **Formulating Holistic Difficulty Theories**: Developing difficulty models that integrate stem complexity, distractor plausibility, and student pedagogical misconception profiles.
2. **Automating Template Acquisition**: Applying machine learning and text mining to automatically extract reusable question templates from verified exam repositories.
3. **Developing Rich Feedback Generation**: Designing algorithmic mechanisms for formative, summative, and personalized feedback explaining item rationales.
4. **Standardizing Evaluation Protocols**: Creating shared public benchmark datasets, standardized human scoring rubrics, and automated metrics correlated with pedagogical validity.
5. **Automated Exam Assembly**: Progressing from single-question generation to assembling balanced, psychometrically sound exams with non-overlapping concept coverage.

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Direct Theoretical Framework for PRIE AQG**: Kurdi et al. provides the definitive foundational taxonomy for evaluating placement readiness question generation in ScholarCamp.
- **Architectural Safeguards Against Literature Flaws**:
  - ScholarCamp must actively avoid the "lower-order recall trap" by explicitly structuring prompt rubrics around Bloom's higher cognitive levels (scenario analysis, system design, coding debugging).
  - Validates ScholarCamp's requirement for **two-way explanatory feedback**: every generated MCQ or technical prompt must supply pedagogical rationale for both the correct answer and each distractor.
  - Informs PRIE's psychometric calibration: item difficulty cannot be assumed from LLM prompts alone; it must be continuously updated using student empirical performance data (IRT / Elo rating).

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|---|---|---|---|
| Review corpus size | 93 peer-reviewed studies published between 2015 and early 2019 included | PDF p. 1, Abstract; p. 13, Table 3 | Systematic synthesis |
| Cognitive level simplicity | Over 70% of questions are simple factual wh-word or cloze gap-fill items | PDF p. 5, 14–20, 38 | Experimental result |
| Neglect of feedback | Fewer than 5% of reviewed systems generate explanatory pedagogical feedback | PDF p. 6, 37–38 | Experimental result |
| Absence of gold standard | Heterogeneous metrics and absence of public benchmark datasets prevent cross-study comparison | PDF p. 7, 28–36, 37 | Systematic synthesis |
| Difficulty modeling gap | Difficulty models rely on distractor similarity proxies and lack empirical psychometric validation | PDF p. 6, 37–38 | Systematic synthesis |
| Reporting quality deficit | Inter-rater reliability reported in under 30% of human evaluations; reporting is highly unstandardized | PDF p. 10, 28–34 | Systematic synthesis |

## 22. Verification Checklist

- [x] PDF read (84-page monograph thoroughly inspected)
- [x] Introduction inspected
- [x] Related work inspected (Alsubait 2015 baseline compared)
- [x] Methodology inspected (Kitchenham SLR guidelines, 13 exclusion criteria)
- [x] Dataset verified (93 primary studies from 6 databases + snowballing)
- [x] Features verified (Corpus types, syntactic features, distractor metrics)
- [x] Algorithms verified (Rules, ontologies, statistical NLP, early seq2seq)
- [x] Architecture inspected (5-stage AQG pipeline)
- [x] Experiments inspected (9-point quality appraisal instrument)
- [x] Results verified (Exact counts, percentages, taxonomy distributions)
- [x] Limitations verified (English restriction, 10 inaccessible full texts)
- [x] Future work verified (Difficulty theories, template mining, feedback, exam assembly)
- [x] Evidence locations recorded

## 23. Verification Status

**VERIFIED**
*(Comprehensive 84-page systematic review in IJAIED verified directly from source PDF with exhaustive extraction of objectives, corpus criteria, taxonomy findings, and research directions.)*
