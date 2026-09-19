# Paper 35 — Implicit Skills Extraction Using Document Embedding and Its Use in Job Recommendation

## 1. Bibliographic Information

- **Paper ID**: Paper35
- **Full Title**: Implicit Skills Extraction Using Document Embedding and Its Use in Job Recommendation
- **Authors**: Akshay Gugnani (IBM Research - AI) and Hemant Misra (Applied Research, Swiggy, India)
- **Institution**: IBM Research - AI, India; Applied Research, Swiggy, India
- **Year**: 2020
- **Venue**: Proceedings of the Thirty-Second Innovative Applications of Artificial Intelligence Conference (IAAI-20 / AAAI-20), pp. 13186–13193
- **DOI**: Available via AAAI Publications (https://ojs.aaai.org/index.php/AAAI/article/view/7037)
- **PDF filename**: `Paper35_qin2020implicit.pdf` (Note: filename reflects legacy bibtex tag `qin2020implicit`; authentic primary PDF confirms authors Akshay Gugnani and Hemant Misra, IBM Research & Swiggy, AAAI/IAAI-20)
- **PDF path**: `Papers/PDFs/Paper35_qin2020implicit.pdf`
- **Page count**: 8 pages (pp. 13186–13193)

---

## 2. Research Problem

Automated job recommender systems match unstructured candidate curricula vitae (CVs/resumes) against job descriptions (JDs). However, standard keyword-matching ATS engines rely solely on **explicit skills** directly stated in the text. In real hiring pipelines, recruiters frequently omit foundational, adjacent, or contextual prerequisites (e.g., a "Python Data Scientist" JD might omit basic "SQL" or "Git", assuming they are self-evident). Relying exclusively on explicit string matching results in severe false-negative mismatches and sub-optimal job recommendations.

### Source Evidence
- **Page**: PDF p. 1 (p. 13186)
- **Section**: Abstract & Section 1 — Introduction

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To propose an industrial-scale ensemble NLP skill extraction architecture combining commercial entity extractors, Part-of-Speech (PoS) grammars, and ontology dictionaries.
2. To introduce the concept and algorithmic formalization of **Implicit Skills Extraction**: inferring unstated but contextually necessary competencies by projecting JDs into a semantic document embedding space.
3. To train a **Doc2Vec** model over a massive corpus of **1.1 million real-world JDs** to capture domain-level semantic affinities.
4. To formalize a bipartite graph matching framework calculating a weighted **Affinity Score** between candidate skills and job requirements.
5. To empirically demonstrate that augmenting explicit matching with implicit skill inferences significantly boosts recommendation accuracy (A@K) and Mean Reciprocal Rank (MRR).

### Source Evidence
- **Page**: PDF pp. 1–3 (pp. 13186–13188)
- **Section**: Abstract, Section 1, and Section 4

---

## 4. Research Questions

- *Not explicitly reported* (The paper is structured as an applied AI system and empirical benchmarking study in AAAI/IAAI rather than numbered hypotheses).

---

## 5. Dataset

The study uses four distinct datasets across training and evaluation:
1. **Unsupervised Semantic Pretraining Corpus**: **1.1 Million Job Descriptions (JDs)** crawled from the web across multiple industries, job families, and geographies to train the domain-wide Doc2Vec model.
2. **Skill Extraction Ground-Truth Benchmark**: An industrial-scale corpus of resumes and JDs evaluated against manual human annotations from 2 domain hiring experts.
3. **Small-Scale Recommendation Benchmark (Maheshwary & Misra 2018)**: **25 candidate profiles** matched against a curated pool of **100 JDs**.
4. **Large-Scale Recommendation Benchmark**: **200 candidate profiles** matched against **10,000 JDs**.

### Source Evidence
- **Page**: PDF pp. 1, 3, 7 (pp. 13186, 13188, 13192)
- **Section**: Abstract, Section 3 (Data Sources), Section 5 (Results)

---

## 6. Features / Entity Representations

The framework extracts and operates on:
- **Explicit Skills**: Direct technical and functional skills extracted from text (e.g., Java, React, PyTorch, Linear Algebra).
- **Implicit Skills**: Contextually inferred competencies absent from the target JD but present across semantically neighboring JDs within the Doc2Vec latent manifold.
- **Syntactic / PoS Patterns**: Noun-phrase chunks, verb-noun dependencies, and capitalized entity tokens.
- **Word2Vec (W2V) Dense Embeddings**: 300-dimensional semantic skill vectors.
- **Document Metadata**: Role titles, industry categories, years of experience, and geographic constraints.

### Source Evidence
- **Page**: PDF pp. 2–5, 7
- **Section**: Section 3, Section 4, Table 4

---

## 7. Data Preprocessing

1. **Text Normalization**: Removing formatting markup, standardizing casing, stripping non-alphanumeric punctuation.
2. **Ensemble Skill Extraction**:
   - *IBM Watson NLU*: Extracting high-level concepts, named entities, and semantic keywords.
   - *Stanford PoS Tagger*: Filtering candidate tokens through rule-based grammatical patterns (e.g., `(Noun)+`, `(Adjective)*(Noun)+`).
   - *O\*NET Dictionary Expansion*: Validating and standardizing extracted terms against the standardized U.S. Department of Labor O\*NET occupational taxonomy.
3. **Document Embedding Transformation**: Vectorizing JDs via a Distributed Memory Doc2Vec model ($d=300$).

### Source Evidence
- **Page**: PDF pp. 3–5 (pp. 13188–13190)
- **Section**: Section 3 & Section 4.1

---

## 8. Algorithms and Models

The paper integrates four distinct algorithmic components:
1. **Skill Extraction Ensemble**: Tri-partite architecture (Watson NLU + PoS Pattern Matcher + O\*NET Taxonomy Matcher). Yields Precision = 0.78, Recall = 0.88, F1 $> 0.83$, Accuracy $> 0.90$ against expert human annotators.
2. **Implicit Skill Mining Engine**:
   - Projects target JD into Doc2Vec semantic space.
   - Computes cosine distance to retrieve top-$k$ most similar JDs from the 1.1M corpus.
   - Extracts candidate skills present in neighbors but absent in target JD.
   - Weights candidate skills via TF-IDF relevance and co-occurrence frequency to filter noise.
3. **Bipartite Graph Matching**: Constructs a bipartite graph between candidate CV skills and JD (explicit + implicit) skills; executes both greedy maximal matching and maximum bipartite matching to compute bidirectional coverage.
4. **Affinity Scoring Function**:
   $$Y = \frac{\omega_1 E_1 + \omega_2 E_2 + \omega_3 E_3}{\omega_1 + \omega_2 + \omega_3}$$
   where:
   - $E_1$: Cosine similarity between Word2Vec skill embeddings ($\omega_1 = 0.5$).
   - $E_2$: Normalized corpus document frequency ($\omega_2 = 0.2$).
   - $E_3$: Explicit/Implicit boosting score ($\omega_3 = 0.3$; $E_3 = 1.0$ for explicit skills, $E_3 = 0.5$ for implicit skills).
   - The final **Affinity Score** is the average edge weight across all bipartite matches ($[0, 1]$).

### Source Evidence
- **Page**: PDF pp. 1, 4–7 (pp. 13186, 13189–13192)
- **Section**: Section 4 (Subsections 1, 2, 3), Table 4, Equation (2)

---

## 9. Architecture

The system implements a multi-stage offline/online workflow:
- **Offline Stage**: `1.1M Web JDs` $\rightarrow$ `Doc2Vec Pretraining` $\rightarrow$ `Semantic Projection Index`.
- **Online Ingestion**: `Candidate CV` + `Target JD Pool` $\rightarrow$ `Ensemble Skill Extractor (Watson + PoS + O*NET)` $\rightarrow$ `Explicit Skill Sets`.
- **Implicit Expansion**: `Target JD Vector` $\rightarrow$ `Doc2Vec Nearest Neighbor Query` $\rightarrow$ `Latent Skill Aggregator` $\rightarrow$ `Weighted Implicit Skills`.
- **Recommendation Engine**: `Bipartite Skill Graph` $\rightarrow$ `Edge Weight Calculator (Eq 2)` $\rightarrow$ `Affinity Score Ranking` $\rightarrow$ `Top-10 Recommended JDs`.

### Source Evidence
- **Page**: PDF pp. 4–7
- **Figures / Text**: Section 4 & Section 5

---

## 10. Methodology

1. **Extraction Validation**: Benchmarking the ensemble skill extractor against two human recruitment experts on real-world resumes.
2. **Semantic Space Construction**: Training Doc2Vec on 1.1M documents to model implicit skill relationships.
3. **Implicit Inference Validation**: Testing candidate skill expansion using neighbor frequency thresholds.
4. **Comparative Recommendation Trials**:
   - Trial A: 25 candidates vs 100 JDs (evaluating baseline without implicit skills vs proposed system with implicit skills).
   - Trial B: 200 candidates vs 10,000 JDs (evaluating scalability and generalization).
5. **Expert Evaluation**: Two independent corporate hiring managers reviewed top-10 recommended postings to rate relevance.

### Source Evidence
- **Page**: PDF pp. 6–8
- **Section**: Section 4 & Section 5

---

## 11. Experimental Setup

- **Doc2Vec Hyperparameters**: 300 dimensions, window size 5, minimum count 5, negative sampling.
- **Word2Vec Embeddings**: 300-dimensional pretrained word vectors.
- **Edge Weight Weights**: $\omega_1 = 0.5$ (W2V cosine similarity), $\omega_2 = 0.2$ (frequency), $\omega_3 = 0.3$ (explicit/implicit boost).

### Source Evidence
- **Page**: PDF pp. 4–7
- **Section**: Section 4 & Table 4

---

## 12. Evaluation Metrics

1. **Accuracy at K (A@K)**: Proportion of recommendations in the top-$K$ containing a hiring-manager-approved job match (evaluated at $K=1, 3, 5$).
2. **Mean Reciprocal Rank (MRR)**: Average reciprocal rank of the first relevant recommended job.
3. **Skill Extraction Precision & Recall**: Precision (0.78), Recall (0.88), F1-Score ($>0.83$), and Accuracy ($>0.90$).

### Source Evidence
- **Page**: PDF pp. 1, 7–8 (pp. 13186, 13192–13193)
- **Section**: Abstract & Section 5 (Tables 5 & 6)

---

## 13. Results

### Small-Scale Benchmark (25 Candidates / 100 JDs, Table 5)
- **A@1 (First Recommendation Accuracy)**:
  - Without Implicit Skills: **0.68**
  - With Implicit Skills: **0.88** (**+29.4% improvement in MRR**)
- **A@3**: Increased from **0.76** to **0.96**.
- **A@5**: Increased from **0.88** to **1.00** (a perfect relevant match achieved within top-5 recommendations for every candidate).
- **Outperforming Siamese Network Baseline**: Outperformed the Siamese neural network baseline of Maheshwary & Misra (2018) by **+6.67%** on the exact same dataset.

### Large-Scale Benchmark (200 Candidates / 10,000 JDs, Table 6)
- **A@1**: **0.84**
- **A@3**: **0.95**
- **A@5**: **0.98**
- **Generalizability Confirmation**: Proved that the implicit skill inference mechanism maintains high precision ($A@5 = 0.98$) even when scaling candidate pools by 8x and job pools by 100x.

### Source Evidence
- **Page**: PDF pp. 1, 7–8 (pp. 13186, 13192–13193)
- **Section**: Abstract, Section 5, Tables 5 and 6

---

## 14. Baselines

1. **Explicit-Only Matching Baseline**: The same system running bipartite graph matching without the Doc2Vec implicit skill expansion module (A@1 = 0.68).
2. **Maheshwary & Misra (2018)**: Siamese Deep Neural Network architecture for CV-JD matching evaluated on the same 25-candidate dataset.

### Source Evidence
- **Page**: PDF pp. 7–8
- **Section**: Section 5 & Table 5

---

## 15. Ablation Study

- **Ablation of Implicit Skill Inference (Table 5)**: Directly ablated the implicit skill module:
  - Excluding implicit skills caused A@1 to plunge from **0.88 down to 0.68** (-22.7% drop in top-1 match precision).
  - This proves that implicit skills capture essential contextual competencies that human recruiters expect but frequently omit from written postings.

### Source Evidence
- **Page**: PDF pp. 7–8
- **Section**: Section 5 & Table 5

---

## 16. Explainability

- **Bipartite Graph Traceability**: Unlike end-to-end black-box matching networks (e.g., Siamese CNNs/BERT matching), Gugnani & Misra's bipartite graph matching provides 100% transparent matching rationales:
  - Every match is explicitly decomposed into specific matching skills with their corresponding Word2Vec semantic affinity score and explicit/implicit weight.
  - Candidates and recruiters can inspect exactly *which* skills drove the recommendation.

### Source Evidence
- **Page**: PDF pp. 6–7
- **Section**: Section 4.3 (Equation 2)

---

## 17. Main Findings

1. Job postings frequently suffer from incomplete specification, omitting foundational competencies that domain experts consider implicit.
2. Training Doc2Vec embeddings on massive unlabelled job corpora (1.1M JDs) allows unsupervised mining of implicit skills via semantic neighborhood projection.
3. Factoring implicit skills into candidate-job matching produces dramatic accuracy improvements (+29.4% MRR boost; A@5 reaching 1.00 on 25 candidates and 0.98 on 200 candidates).
4. Bipartite graph matching provides an interpretable alternative to opaque Siamese networks while outperforming them by +6.67%.

### Source Evidence
- **Page**: PDF pp. 7–8
- **Section**: Sections 5 & 6

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Corpus Availability**: Absence of public, standardized large-scale open-source benchmarks for job recommendation, forcing reliance on proprietary internal datasets.
2. **Static Implicit Weighting**: Implicit boosting was fixed at a constant weight ($\omega_3 = 0.3$, $E_3 = 0.5$) rather than being learned dynamically per job role.
3. **Unidirectional Match**: Evaluated job recommendation for candidates; did not symmetrically model reciprocal candidate ranking for recruiters.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The study utilized Word2Vec and Doc2Vec (state-of-the-art at IAAI-20); modern transformer embeddings (Sentence-BERT, modern LLM embeddings) would capture deeper contextual semantics without requiring separate lexical taggers.

### Source Evidence
- **Page**: PDF pp. 7–8
- **Section**: Section 5 & Section 6

---

## 19. Future Work

Explicitly proposed by the authors (Section 6, PDF p. 8):
1. Generating ranked recommendations across multi-year career path trajectories that optimally utilize accumulated skills.
2. Constructing a dynamic **Skill Graph** to infer a candidate's professional growth relative to industry peers.
3. Utilizing skill graphs to automatically infer **Skill-Gaps** and calculate the training cost/time required to acquire missing skills.
4. Comparing organizations based on the professional skill growth trajectories of their employees.

### Source Evidence
- **Page**: PDF p. 8 (p. 13193)
- **Section**: Section 6 — Conclusions and Future Work

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper is foundational for PRIE's **Skill Gap Analyzer** and **Career Recommendation Engine**:
1. **Resolving the Implicit Skill Gap in Student Resumes**: Engineering students often omit basic skills (e.g., writing "Built an e-commerce app with React" but omitting "HTML/CSS" or "JavaScript"). Gugnani & Misra's Doc2Vec neighborhood projection provides the exact algorithmic blueprint for PRIE to infer implicit competencies.
2. **Bipartite Affinity Scoring for PRIE**: PRIE can adopt Equation (2)'s exact weighted formula ($\omega_1 = 0.5$ semantic, $\omega_2 = 0.2$ frequency, $\omega_3 = 0.3$ explicit/implicit boost) to score candidate readiness against target company job descriptions transparently.
3. **Skill-Gap and Career Path Synthesis**: Gugnani & Misra's proposed future work—calculating skill-gaps and recommending targeted learning paths to bridge them—is precisely what ScholarCamp operationalizes in its automated learning pathway module.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **Core Research Scope** | "job recommender system to match resumes to job descriptions... introduces the concept of extracting implicit skills... Doc2Vec model trained on 1.1 Million JDs." | PDF p. 1, Abstract | Direct statement |
| **Extraction Performance** | Ensemble NLP yielded Precision = 0.78, Recall = 0.88, F1 > 0.83, Accuracy > 0.90 against human experts. | PDF pp. 1, 8, Abstract & Section 6 | Quantitative benchmark |
| **A@K Results (25 Candidates)** | A@1 increased from 0.68 to 0.88 (+29.4% MRR boost); A@5 reached 1.00 (Table 5). | PDF pp. 1, 7, Abstract & Table 5 | Experimental result |
| **A@K Results (200 Candidates)** | A@1 = 0.84, A@3 = 0.95, A@5 = 0.98 across 10,000 JDs (Table 6). | PDF p. 8, Table 6 | Experimental result |
| **Siamese Network Benchmark** | Outperformed Siamese network baseline of Maheshwary & Misra (2018) by +6.67%. | PDF p. 7, Section 5 | Comparative result |
| **Author Future Scope** | Career path options, skill graphs for professional growth, and skill-gap inference with acquisition cost analysis. | PDF p. 8, Section 6 | Author future work |

---

## 22. Verification Checklist

- [x] PDF read (`Paper35_qin2020implicit.pdf`, 8 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (Doc2Vec on 1.1M JDs, ensemble skill extractor, bipartite graph match)
- [x] Datasets verified (1.1M JDs, 25 CVs/100 JDs, 200 CVs/10,000 JDs)
- [x] Features verified (Explicit vs implicit skills, W2V embeddings, frequency scores)
- [x] Algorithms verified (Doc2Vec, Word2Vec, IBM Watson NLU, PoS chunking, Equation 2 Affinity Score)
- [x] Architecture inspected (Offline pretraining + online bipartite matching pipeline)
- [x] Experiments inspected (Tables 5 & 6; A@1, A@3, A@5 benchmarks)
- [x] Results verified (A@1: 0.68 -> 0.88, A@5: 1.00, +29.4% MRR, +6.67% over Siamese net)
- [x] Limitations verified (No public large benchmark, static implicit weights, unidirectional)
- [x] Future work verified (Skill graphs, skill-gap analysis, training cost modeling)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; AAAI/IAAI-20 paper by Akshay Gugnani & Hemant Misra, 1.1M JD Doc2Vec model, Equation 2 Affinity Scoring formula, and Tables 5 & 6 numerical results verified directly from source text; legacy filename discrepancy documented).
