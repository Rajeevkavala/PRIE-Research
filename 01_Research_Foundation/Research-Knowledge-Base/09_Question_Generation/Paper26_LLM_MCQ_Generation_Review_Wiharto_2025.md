# Paper 26 — Transformer and Large Language Models for Automatic Multiple-Choice Question Generation: A Systematic Literature Review

## 1. Bibliographic Information

- **Paper ID**: Paper26
- **Full Title**: Transformer and Large Language Models for Automatic Multiple-Choice Question Generation: A Systematic Literature Review
- **Authors**: Halim Wildan Awalurahman, Rizal Fathoni Aji, and Indra Budi
- **Institution**: Faculty of Computer Science, Universitas Indonesia, Depok 16424, Indonesia
- **Year**: 2025 (Received 16 June 2025, Accepted 10 July 2025, Published 18 July 2025)
- **Venue**: IEEE Access (Volume 13, pp. 127100–127112)
- **DOI**: 10.1109/ACCESS.2025.3590423
- **PDF filename**: `Paper26_fernandez2025automated.pdf` (Note: filename reflects legacy bibtex tag `fernandez2025automated`; authentic PDF confirms Halim Wildan Awalurahman et al., Universitas Indonesia, IEEE Access 2025)
- **PDF path**: `Papers/PDFs/Paper26_fernandez2025automated.pdf`
- **Page count**: 13 pages (pp. 127100–127112)

---

## 2. Research Problem

Developing multiple-choice questions (MCQs) manually demands extensive instructional time, domain expertise, and effort. While Automatic Multiple-Choice Question Generation (MCQG) using Transformers and Large Language Models (LLMs) has proliferated rapidly, existing literature reviews have not systematically analyzed the specific architectures, fine-tuning regimes, prompt engineering strategies (zero-shot, few-shot, CoT, RAG), distractor generation mechanisms, and evaluation paradigms (automatic overlap vs manual expert rubrics) uniquely tailored to the MCQ format.

### Source Evidence
- **Page**: PDF p. 1 (p. 127100)
- **Section**: Abstract & Section I — Introduction

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To conduct a rigorous Systematic Literature Review (SLR) on Automatic Multiple-Choice Question Generation using Transformer and Large Language Models following the Kitchenham framework.
2. To synthesize a comprehensive taxonomy of existing architectures (multi-task pipelines vs end-to-end single-task models) and deployment paradigms (fine-tuning vs prompt engineering).
3. To evaluate how learning objectives, Bloom's taxonomy, and pedagogical components are integrated into prompt design.
4. To analyze automatic, manual, and mixed evaluation strategies and identify critical research gaps and future directions.

### Source Evidence
- **Page**: PDF pp. 1–3 (pp. 127100–127102)
- **Section**: Section I & Section III — Methods

---

## 4. Research Questions

The paper explicitly formulates two research questions:
- **RQ1**: *What are the methods in existing research?* (Explores architectures, fine-tuning, prompting strategies, and component pipelines for question and distractor generation).
- **RQ2**: *What are the evaluation metrics that have been used in existing research?* (Analyzes automated metrics, manual expert review rubrics, and mixed evaluation approaches).

### Source Evidence
- **Page**: PDF p. 3 (p. 127102)
- **Section**: Section III.A — Planning

---

## 5. Dataset (SLR Corpus & Benchmarks)

### SLR Search & Selection Corpus
- **Framework**: Kitchenham systematic literature review methodology (Planning, Conducting, Reporting).
- **Search Query**: `"Multiple-choice questions generation" AND ("Transformer" OR "Large Language Models")`.
- **Databases Queried**: 4 scientific databases: ACM Digital Library, IEEE Xplore, ScienceDirect, Scopus.
- **Inclusion / Quality Criteria**: 7 quality assessment questions (QA1–QA7 scored 0, 0.5, 1.0; inclusion threshold: score $> 4$ and QA2 score $= 1$).
- **Primary Studies Selected**: **28 primary studies** published between 2021 and 2024 (1 in 2021, 6 in 2022, 4 in 2023, 17 in 2024; 19 conference papers, 9 journal articles).

### Datasets Analyzed Across Primary Studies
- **Reading Comprehension & QA Corpora**: SQuAD (most frequent across training/testing), RACE, DG-RACE, EQG-RACE, BoolQ, CLOTH, Cosmos QA, ScienceQA.
- **Domain-Specific Corpora**: Lecture notes, OpenStax textbooks, e-books.

### Source Evidence
- **Page**: PDF pp. 3–5 (pp. 127102–127104)
- **Section**: Section III.B (Conducting), Section IV.A (Overview, Figure 1, Figure 2)

---

## 6. Features / Input Information

The primary studies structure MCQ inputs across distinct informational components (Table 8):
1. **Context / Source Text**: Reading passage, textbook excerpt, lecture slide, or code snippet.
2. **Target Answer / Key**: Specific named entity, concept, or phrase designated as the correct option.
3. **Learning Objective / Bloom's Taxonomy Level**: Pedagogical target (e.g., Remember, Understand, Apply, Analyze).
4. **Distractor Constraints**: Part-of-speech, semantic similarity bounds, or domain ontology classes.
5. **Audience / Grade Level**: Target educational proficiency level.

### Source Evidence
- **Page**: PDF pp. 6–10 (pp. 127105–127109)
- **Section**: Section IV.B, Table 3, Table 8

---

## 7. Data Preprocessing

Reported preprocessing pipelines across the reviewed studies:
- **Key Selection / Candidate Extraction**: Named Entity Recognition (NER), TF-IDF keyword extraction, or heuristic phrase chunking to extract key answers before question generation.
- **Tokenization & Formatting**: Converting input context and target keys into structured prompt templates or sequence-to-sequence format (`context: <text> answer: <key>`).
- **Semantic Filtering**: Candidate distractor filtering using cosine similarity thresholds (e.g., Word2Vec/Sense2Vec embeddings) to ensure plausibility while avoiding duplicate correct answers.

### Source Evidence
- **Page**: PDF pp. 6–8 (pp. 127105–127107)
- **Section**: Section IV.B

---

## 8. Algorithms and Models

The review establishes an authoritative taxonomy dividing MCQG into two foundational architectural paradigms:

### Paradigm 1: Multi-Task Pipeline (Separate QG and DG)
- **Question Generation (QG)**: Smaller fine-tuned sequence-to-sequence Transformer models (T5, mT5, Pegasus, BART).
- **Distractor Generation (DG)**:
  - *Transformer-Lexical*: Combines Transformer QG with lexical semantic models for distractors (Sense2Vec, Word2Vec, WordNet). The most common configuration is **T5-Sense2Vec** (5 studies).
  - *Transformer-Transformer*: Uses fine-tuned Transformers for both QG and DG (e.g., T5 + T5, BERT + T5).
- **Deployment**: Primarily requires fine-tuning on labeled QA datasets (SQuAD, RACE).

### Paradigm 2: Single-Task End-to-End Generation
- **Models**: Large Language Models (LLMs) generating stem, correct answer, and distractors simultaneously in a single prompt (GPT-3.5/GPT-4, Google Gemini, LLaMA, Mistral, Qwen).
- **Prompting Strategies**:
  - *Zero-Shot*: Direct instruction prompting (most common).
  - *Few-Shot*: In-context demonstration examples.
  - *Chain-of-Thought (CoT)*: Step-by-step reasoning prompts.
  - *Retrieval-Augmented Generation (RAG)*: External document context retrieval prior to prompting.

### Source Evidence
- **Page**: PDF pp. 5–8, 10 (pp. 127104–127107, 127109)
- **Section**: Section IV.B, Table 2, Table 3, Table 7

---

## 9. Architecture

The paper synthesizes a conceptual pipeline representing the two pathways:
- **Multi-Stage Modular Architecture**:
  - `Input Passage` $\rightarrow$ `Key Selection` $\rightarrow$ `Transformer QG (Stem Generation)` $\rightarrow$ `Lexical / Transformer DG (Distractor Generation)` $\rightarrow$ `Filtering / Assembly` $\rightarrow$ `Final MCQ`.
- **End-to-End LLM Architecture**:
  - `Context + Learning Objective + Instructions + Few-Shot Examples` $\rightarrow$ `LLM (Direct Generation)` $\rightarrow$ `Complete MCQ (Stem + Key + 3 Distractors + Explanation)`.

### Source Evidence
- **Page**: PDF pp. 5–7 (pp. 127104–127106)
- **Section**: Section IV.B & Table 2

---

## 10. Methodology

1. **Systematic Protocol Definition**: Formulated research scope and quality assessment criteria following Kitchenham guidelines.
2. **Corpus Identification**: Queried ACM DL, IEEE Xplore, ScienceDirect, and Scopus, yielding raw candidate pools.
3. **Screening & Quality Scoring**: Applied 7 quality questions (QA1 to QA7), filtering down to 28 qualifying primary studies.
4. **Data Extraction & Categorization**: Coded each paper for model type, task structure (multi-task vs single-task), deployment regime (fine-tuning vs prompting), datasets, and evaluation metrics.
5. **Synthesis & Comparative Analysis**: Contrastive analysis of linguistic scope, distractor granularity (word-level vs sentence-level), pedagogical integration, and evaluation rigor.

### Source Evidence
- **Page**: PDF pp. 3–5 (pp. 127102–127104)
- **Section**: Section III

---

## 11. Experimental Setup

- **Corpus Demographics**: 28 primary studies (2021: 1, 2022: 6, 2023: 4, 2024: 17; Conferences: 19, Journals: 9).
- **Hardware / Resource Findings**: The authors report that fine-tuning requires substantial domain training data, while prompting LLMs requires significant server GPU memory or reliance on commercial cloud APIs.

### Source Evidence
- **Page**: PDF pp. 4–5, 10
- **Section**: Section IV.A, Section V.A

---

## 12. Evaluation Metrics

The review identifies three broad evaluation categories across the 28 primary studies (Table 4):
- **Automatic Only**: 7 studies (25.0%)
- **Manual (Human) Only**: 12 studies (42.9%)
- **Mixed (Automatic + Manual)**: 9 studies (32.1%)

### Automated Metrics (Table 5)
- **N-Gram Overlap**: BLEU (BLEU-1, 2, 3, 4), ROUGE (ROUGE-1, ROUGE-2, ROUGE-L), METEOR.
- **Classification / Matching**: Precision, Recall, F1-Score, Exact Match (EM).
- **Embedding / Semantic**: BERTScore.

### Manual / Expert Metrics (Table 6)
- **Linguistic Quality**: Fluency, Grammaticality, Clarity, Readability.
- **Pedagogical Quality**: Relevance to context, Answerability, Question Difficulty.
- **Distractor Quality**: Distractor Plausibility, Non-ambiguity, Avoidance of Item Writing Flaws (IWF), Docimological Analysis.

### Emerging Semi-Automated Metrics
- **LLM-as-a-Judge / Item Response Theory (IRT)**: Using secondary LLMs to simulate student responses to estimate question difficulty and discrimination parameters.

### Source Evidence
- **Page**: PDF pp. 7–9, 11 (pp. 127105–127108, 127110)
- **Section**: Section IV.C, Section V.B, Tables 4, 5, 6

---

## 13. Results

### Corpus Synthesis Results
1. **Dominant Architecture**: Rapid shift from modular Transformer-Lexical pipelines (2021–2022) to end-to-end LLM prompting (2023–2024).
2. **Language Bias**: 100% of reviewed fine-tuned Transformer-Sense2Vec pipelines operated exclusively in **English**; multilingual MCQG remains largely unexplored.
3. **Distractor Granularity**: Transformer-Lexical models (Sense2Vec, Word2Vec) are strictly restricted to word- or phrase-level distractors; only LLMs reliably generate plausible sentence-length distractors for complex reasoning questions.
4. **Evaluation Discrepancy**: Automated word-overlap metrics (BLEU, ROUGE) correlate poorly with true pedagogical quality and distractor plausibility, explaining why 75% of primary studies incorporate manual expert evaluations.
5. **Prompting Sophistication**: Despite the popularity of LLMs, the vast majority of studies relied solely on standard zero-shot prompting; advanced prompting (Chain-of-Thought, RAG, and Few-Shot) remains underutilized in MCQG literature.

### Source Evidence
- **Page**: PDF pp. 6–11 (pp. 127105–127110)
- **Section**: Section IV & Section V

---

## 14. Baselines

The review evaluates baselines utilized across the 28 primary studies:
- Conventional rule-based question generators (Syntactic pattern matchers).
- Vanilla Sequence-to-Sequence models (LSTM, GRU, standard Seq2Seq).
- Non-fine-tuned zero-shot LLM baselines against fine-tuned smaller Transformers.

### Source Evidence
- **Page**: PDF pp. 6–8
- **Section**: Section IV.B

---

## 15. Ablation Study

- *Not applicable* (Systematic literature review methodology; paper provides comparative breakdowns of model components across Table 2, Table 3, and Table 7).

---

## 16. Explainability

- The review highlights that neither fine-tuned Transformers nor standard zero-shot LLMs inherently provide explanation traces for why specific distractors are incorrect.
- Studies utilizing Chain-of-Thought (CoT) prompting represent an emerging direction by generating rationales and explanations alongside the answer key.

### Source Evidence
- **Page**: PDF pp. 6, 11
- **Section**: Section IV.B & Section V.D

---

## 17. Main Findings

1. **Architectural Transition**: Automatic MCQG has branched into two distinct paradigms: (a) modular pipelines pairing fine-tuned sequence-to-sequence Transformers (e.g., T5) with lexical distance algorithms (Sense2Vec/WordNet) for short factoid distractors, and (b) end-to-end LLM prompting for complex, narrative-level questions.
2. **Pedagogical Deficit**: Most existing studies treat question generation as pure text-to-text reading comprehension (e.g., SQuAD/RACE) without anchoring questions to formal pedagogical frameworks like Bloom's Taxonomy or explicit course learning objectives.
3. **The Evaluation Bottleneck**: Automatic n-gram overlap metrics (BLEU/ROUGE) are fundamentally inadequate for evaluating distractor quality, driving a heavy reliance on manual expert review (42.9% manual, 32.1% mixed).
4. **Underutilization of CoT and RAG**: Grounded generation via RAG and step-by-step reasoning via CoT are rarely combined in current MCQ literature.

### Source Evidence
- **Page**: PDF pp. 9–12
- **Section**: Section V & Section VI

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Quality Assessment Subjectivity**: Quality criteria QA1–QA7 and scoring thresholds were defined and executed by the authors, introducing potential subjective bias.
2. **Scope Restriction**: The review strictly limited its scope to Transformer and Large Language Models, excluding non-transformer neural networks, statistical classifiers, and rule-based systems.
3. **Lack of Unified Benchmark Testing**: The review synthesizes published claims across disparate datasets and metrics rather than executing direct empirical comparisons on a single standardized benchmark.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The search query string (`"Multiple-choice questions generation"`) might have omitted studies that phrased the task as "distractor generation", "multiple-choice test creation", or "item generation" without the exact hyphenated string.

### Source Evidence
- **Page**: PDF p. 11 (p. 127110)
- **Section**: Section V.C — Limitation

---

## 19. Future Work

Explicitly outlined in Section V.D:
1. **Multilingual and Cross-Lingual MCQG**: Developing lexical distractor generators (e.g., FastText) and exploring cross-lingual prompt-output configurations for non-English contexts.
2. **Bloom's Taxonomy and Learning Objective Alignment**: Grounding fine-tuning and prompting datasets explicitly in cognitive complexity levels (Bloom's Taxonomy) rather than surface reading comprehension.
3. **Advanced Prompting Paradigms**: Systematic exploration of Few-Shot, Chain-of-Thought (CoT), and Retrieval-Augmented Generation (RAG) for multi-step reasoning questions.
4. **Automated Quality Evaluation using NLP / LLMs**: Developing reliable automated surrogates for human expert review, such as Item Writing Flaws (IWF) classifiers and LLM-based Item Response Theory (IRT) student simulations.

### Source Evidence
- **Page**: PDF pp. 11–12 (pp. 127110–127111)
- **Section**: Section V.D — Future Works

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This systematic review directly informs the architectural design and research positioning of PRIE's **Adaptive Question Generation (AQG)** module:
1. **Hybrid Architecture Selection**: The review validates PRIE's choice of LLM prompting over brittle T5-Sense2Vec pipelines. Placement readiness assessments require multi-sentence scenario questions and realistic coding distractors, which lexical models cannot generate.
2. **Closing the Identified SLR Gaps**:
   - *Gap identified by Awalurahman et al.*: "Few studies utilizing learning components such as learning objective, limited use of chain-of-thought, retrieval augmented generation."
   - *PRIE Solution*: PRIE directly implements **RAG-grounded, Bloom-indexed Chain-of-Thought question generation**, targeting precisely the three deficiencies highlighted in the SLR.
3. **Automated Distractor Evaluation**: PRIE can adopt the Item Writing Flaws (IWF) rule-based tagging and LLM-as-a-judge rubrics identified in the review to evaluate generated technical assessment items automatically.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **SLR Scope & Primary Studies** | "We obtained 28 primary studies... published from 2021 to 2024 (19 conferences, 9 journals)." | PDF pp. 1, 4–5, Sections I & IV.A | Direct statement / Corpus count |
| **Two Methodological Paradigms** | Multi-task pipeline (separate QG and DG using fine-tuned T5/Sense2Vec) vs single-task end-to-end (LLMs using prompting). | PDF pp. 5–7, Section IV.B & Table 2 | Taxonomy / Methodology |
| **Most Used Lexical Pair** | "The most used method in the Transformer-Lexical based approach was T5-Sense2Vec." | PDF p. 6, Section IV.B | Corpus statistic |
| **Evaluation Method Distribution** | Manual only: 12 studies (42.9%), Mixed: 9 studies (32.1%), Automatic only: 7 studies (25.0%). | PDF p. 7, Table 4 | Table / Quantitative count |
| **Identified Literature Gaps** | "studies are still primarily in English, with few studies utilizing learning components such as learning objective, limited use of chain-of-thought, retrieval augmented generation." | PDF p. 1, Abstract | Author finding / Gap |
| **Author Limitations** | Subjective QA criteria, exclusion of non-transformer methods, absence of unified empirical benchmark across models. | PDF p. 11, Section V.C | Author limitation |

---

## 22. Verification Checklist

- [x] PDF read (`Paper26_fernandez2025automated.pdf`, 13 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (Kitchenham SLR framework, 4 databases, QA1–QA7)
- [x] Dataset verified (28 primary studies, SQuAD, RACE, DG-RACE)
- [x] Features verified (Context, key answer, learning objectives, distractor constraints)
- [x] Algorithms verified (T5, Pegasus, Sense2Vec, WordNet, GPT, Gemini, LLaMA)
- [x] Architecture inspected (Multi-task pipeline vs Single-task end-to-end prompting)
- [x] Experiments inspected (Evaluation breakdowns across Tables 4, 5, 6, 7, 8)
- [x] Results verified (28 studies breakdown: 42.9% manual, 32.1% mixed, 25.0% automatic)
- [x] Limitations verified (Subjectivity of QA, lack of unified benchmark)
- [x] Future work verified (Multilingual, Bloom alignment, CoT, RAG, automated metrics)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact Kitchenham SLR protocol, 28 primary studies synthesis, architectural taxonomy from Table 2, evaluation breakdown from Table 4, and future research gaps verified directly from source text).
