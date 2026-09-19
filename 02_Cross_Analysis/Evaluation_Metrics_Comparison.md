# Evaluation Metrics Comparison & Validation Standards

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/Evaluation_Metrics_Comparison.md`  
**Status**: Authoritative Evaluation Metrics Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. Multi-Disciplinary Metric Taxonomy

Evaluating artificial intelligence across education, recruitment, conversational speech, and psychometrics requires diverse validation metrics. Across the 44 verified papers, evaluation methodologies span five (5) distinct metric tiers:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            METRIC VALIDATION TAXONOMY                            │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Metric Category               │ Representative Metrics in Corpus                 │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Classification & Prediction│ Accuracy, Precision, Recall, Macro F1, AUC-ROC.  │
│ 2. Information Retrieval (IR) │ MRR@10, Precision@K, NDCG@10, Top-5 Match Acc.  │
│ 3. Natural Language & RAG     │ ROUGE-L, BLEU-4, RAG Triad (Faithfulness,       │
│                               │ Groundedness, Answer Relevancy).                 │
│ 4. Psychometrics & Pedagogy   │ Item Difficulty ($p$), Item Discrimination ($D$),│
│                               │ Bloom's Alignment %, TAM Path Coeffs ($\beta$),  │
│                               │ System Usability Scale (SUS), Anxiety Delta.     │
│ 5. Systems Engineering & ASR  │ Turn Latency (s), Word Error Rate (WER), FPS.    │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master Evaluation Metrics Benchmark Across Domains

The matrix below benchmarks evaluation metrics across the primary research domains, contrasting automated computational metrics with human ground-truth validations:

| Research Domain & Representative Papers | Primary Automated Metrics Used | Best Reported Metric Score | Human Validation Methodology | Human Correlation / Agreement | Key Metric Vulnerability / Blind Spot |
|:---|:---|:---|:---|:---|:---|
| **01_Employability** (P01, P06, P07, P09, P22, P24) | Accuracy, Precision, Recall, F1, AUC-ROC | **Stacking: 94.2% Acc, CatBoost: 93.6% Acc, AUC 0.92** | Historical institutional placement records | Ground-truth binary placement offer | Accuracy ignores class imbalance; lacks tracking of off-campus offers |
| **02_Prediction & LA** (P02, P05, P08, P10, P33, P44) | Multi-Horizon Acc, F1, AUC-ROC, Dropout Reduction | **TFT: 94.6% Acc, BiLSTM: 93.1% Acc, AUC 0.95** | End-of-term academic registrar records | Official student transcript records | Static metrics mask temporal dropouts; fails to capture personal emergencies |
| **03_XAI Frameworks** (P18, P19, P32, P34) | Shapley Attribution Fidelity, Counterfactual Validity | **DiCE Validity: 94.2%, Pearson r=0.91 advisor corr** | Senior faculty advisor & student review panels | High advisor agreement (r=0.91); 86.5% student agreement | Algorithmic fidelity does not guarantee student behavioral adoption (P32) |
| **04_ATS & Resume** (P11, P12, P17, P35, P36, P37, P42) | Entity F1, Semantic Cosine, MRR@10, Layout Acc | **LayoutLMv3 Entity F1: 0.948, ResuMatch MRR@10: 0.92**| Corporate IT recruiter ranking panels | Recruiter ranking correlation: r=0.81 (P11), r=0.88 (P17) | Lexical TF-IDF penalizes synonyms; SBERT alone misses exact hard criteria |
| **05_Mock Interview** (P03, P14, P15, P27, P28, P29, P30, P38)| Acoustic Acc, Emotion Acc, Turn Latency, WER | **Prosody Acc: 90.1%, IndusAI Code Eval: 88.5%** | Professional campus HR & technical panels | Expert panel correlation: rho=0.82 (P15), r=0.84 (P28) | High latency (>2.5s) destroys conversational flow; video sensitive to lighting |
| **06_RAG Educational** (P20, P21, P23, P40) | RAG Triad (Faithfulness, Relevancy), ROUGE-L | **Factual Precision: 92.8%, Faithfulness: 89.2%** | Course instructor syllabus ground truth | Expert factuality audit: <2.1% hallucination (P23) | ROUGE/BLEU penalizes valid paraphrasing; requires semantic RAG Triad (P20) |
| **07_Recommendation** (P13, P16, P35, P43) | Precision@10, NDCG@10, Graduation Delay Reduction | **MACO: -18% Delay, OPAC NDCG@10: 0.912** | Departmental academic committee review | 88.2% student path completion (P13) | Standard CF recommends prerequisite-invalid courses; requires DAG constraints |
| **09_Question Gen.** (P25, P26, P39) | Item Discrimination ($D$), Cognitive Depth % | **Validity: 91.5%, Discrimination: 0.88** | Subject Matter Expert (SME) peer review | 84.5% SME acceptance rate (P39) | LLMs generate plausible-looking distractors that are subtly ambiguous |
| **10_Digital Twin** (P41) | Simulation Offer Fidelity, Preparation Uplift | **Offer Fidelity: 91.4%, Prep Efficiency: +22%** | Multi-stakeholder validation (Recruiters+Mentors)| Real-world placement conversion: +18.5% | Requires continuous real-time multi-system data synchronization |

---

## 3. Critical Methodological Findings & Quality Gaps

### 3.1 The Flaw of Traditional NLP Metrics in Education (ROUGE / BLEU)
- `[CROSS-PAPER OBSERVATION]` In automated question generation and RAG tutoring (P20, P23, P26), researchers frequently relied on n-gram overlap metrics (BLEU, ROUGE).
- `[AUTHOR-STATED FACT]` Swacha & Gracel (P20) and Wang et al. (P25) proved that a response can have a low ROUGE score while being 100% pedagogically sound and factual (due to paraphrasing), or conversely, have a high ROUGE score while containing a subtle, catastrophic hallucination. The literature confirms that the **RAG Triad (Faithfulness, Groundedness, Answer Relevancy)** and human SME validation must supersede legacy n-gram metrics.

### 3.2 Accuracy Masking Minority-Class Failures in EDM
- `[CROSS-PAPER OBSERVATION]` In early placement and dropout studies (P01, P07, P33), authors frequently celebrated models achieving 85%–88% accuracy. However, in datasets where 80% of students naturally pass or get placed, a naive baseline predicting "Placed" for every single candidate automatically achieves 80% accuracy while failing to detect 100% of at-risk students.
- `[CROSS-PAPER OBSERVATION]` Modern empirical standards (P02, P08, P44) demand reporting **Minority-Class Recall**, **Macro F1-score**, and **Precision-Recall AUC (PR-AUC)** alongside ROC curves.

### 3.3 The Human Ground-Truth Gold Standard in Mock Interviews
- `[CROSS-PAPER OBSERVATION]` In automated mock interview evaluation (P03, P14, P15, P28, P29), purely algorithmic metrics (such as loss or classification accuracy on benchmark clips) are insufficient. Systems must validate their scoring rubrics by computing **Pearson ($r$) or Spearman ($\rho$) correlation coefficients against independent human recruiter panels**. The verified corpus sets the state-of-the-art correlation benchmark at $r \ge 0.82$ to $0.87$.

---

## 4. ScholarCamp / PRIE Unified Evaluation Protocol

ScholarCamp / PRIE implements an audited, multi-dimensional evaluation protocol across all ten subsystems:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             PRIE EVALUATION PROTOCOL                             │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ System Component         │ Mandatory Evaluation Standards & Thresholds           │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 1. Employability Predictor│ Macro-F1 $\ge 0.90$, PR-AUC $\ge 0.92$, 10-Fold CV;   │
│                          │ Zero reliance on unweighted accuracy alone.           │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 2. ATS Resume Screening  │ Mean Reciprocal Rank (MRR@10) $\ge 0.90$;             │
│                          │ Layout boundary tolerance on multi-column CVs $\ge 95%$.│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 3. Mock Interview Engine │ Conversational turn latency $\le 1.5\text{s}$;        │
│                          │ Human expert rubric correlation $r \ge 0.82$.         │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 4. Contextual RAG Tutor  │ Automated RAG Triad: Faithfulness $\ge 90\%$,         │
│                          │ Answer Relevancy $\ge 88\%$, Hallucination $\le 3\%$. │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 5. Adaptive Question Gen.│ Bloom's Taxonomy Alignment $\ge 88\%$; Item           │
│                          │ Discrimination Index ($D$) $\ge 0.80$ via psychometrics│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ 6. Explainability Engine │ Counterfactual validity $\ge 92\%$; Actionability     │
│                          │ score on intervenable student attributes $\ge 90\%$.  │
└──────────────────────────┴───────────────────────────────────────────────────────┘
```
