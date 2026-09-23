# Phase 10: Citation-Claim Verification Matrix

**Project**: ScholarCamp  
**Core System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `10_Publication/PHASE_10_CITATION_CLAIM_MATRIX.md`  
**Date**: September 19, 2026  
**Status**: COMPLETE & VERIFIED  

---

## 1. Master Citation-to-Claim Mapping Matrix

This matrix links every literature citation appearing in the reconstructed conference paper to the primary cited paper ID, formal citation key, specific claim made in the manuscript, exact page/section location within the cited source paper, the target paper section, and verification status:

| Claim ID | Paper ID | Citation Key & Authors | Claim in Reconstructed Manuscript | Cited Source & Evidence Location | Manuscript Section | Status |
|:---:|:---:|:---|:---|:---|:---:|:---:|
| **CIT-01** | `Paper01` | `\cite{b1}`: Olipas (2024) | Machine learning and explainable AI for student career readiness; technical and problem-solving skills outweigh cumulative GPA in predicting placement outcomes. | `Paper01_olipas2024predicting.pdf`, Section 3.2, Table 2 | §I, §II-A, §VI-B | **VERIFIED** |
| **CIT-02** | `Paper02` | `\cite{b2}`: Van Wyk & Du Plessis (2025) | AI-driven learning analytics in higher education; necessity of longitudinal engagement tracking over static semester-end records. | `Paper02_vanwyk2025engagement.pdf`, Section 4.1, Table 2 | §I, §II-B | **VERIFIED** |
| **CIT-03** | `Paper03` | `\cite{b3}`: Sharma & Gupta (2025) | Integrated placement preparation platforms (Preplyte); observing that disconnected standalone tools cause student attrition and preparation fragmentation. | `Paper03_sharma2025preplyte.pdf`, Section 1.2, Section 3.1 | §I, §II-A | **VERIFIED** |
| **CIT-04** | `Paper04` | `\cite{b4}`: Patel & Nair (2024) | Predictive analysis of placement success; identifying practical skill deficits and interview communication anxiety as dual gating factors. | `Paper04_patel2024ai.pdf`, Section 2.4, Table 3 | §I, §II-A, §VI-B | **VERIFIED** |
| **CIT-05** | `Paper05` | `\cite{b5}`: Chen & Hwang (2024) | Bibliometric review of AI in education; establishing that algorithmic explainability and fairness represent critical prerequisites for institutional adoption. | `Paper05_chen2024artificial.pdf`, Section 3.4, pp. 128–132 | §I, §II-B | **VERIFIED** |
| **CIT-06** | `Paper06` | `\cite{b6}`: Senthil & Kumar (2021) | Survey of employability prediction; observing that conventional models operate as retrospective post-hoc classifiers in final semesters. | `Paper06_senthil2021employability.pdf`, Section 2.1, pp. 6218–6220 | §I, §II-A | **VERIFIED** |
| **CIT-07** | `Paper09` | `\cite{b7}`: Casuat & Festijo (2021) | Employability classification using machine learning; achieving 84.5%–89.2% accuracy on institutional cohorts while noting class imbalance challenges. | `Paper09_casuat2021predicting.pdf`, Section 4.2, Table 4 | §I, §II-A, §VI-B | **VERIFIED** |
| **CIT-08** | `Paper10` | `\cite{b8}`: Rao & Swamy (2022) | Comparative benchmark of student performance prediction; demonstrating tree ensemble superiority on structured tabular academic records. | `Paper10_rao2022student.pdf`, Section 3.2, Table 2 | §I, §II-A, §VI-B | **VERIFIED** |
| **CIT-09** | `Paper11` | `\cite{b9}`: Academic Consortium (2025) | Automated resume parsing and candidate information extraction using natural language processing techniques. | `Paper11_consortium2025resume.pdf`, Section 3.1, pp. 48–50 | §II-D | **VERIFIED** |
| **CIT-10** | `Paper12` | `\cite{b10}`: Roy & Bhattacharya (2024) | Contextual resume parsing; identifying that multi-column visual layouts suffer severe text stream interleaving under 1D scrapers. | `Paper12_roy2024resume.pdf`, Section 4.2, pp. 105–108 | §II-D, §VI-E | **VERIFIED** |
| **CIT-11** | `Paper13` | `\cite{b11}`: Zhang et al. (2023) | Career-gAIde: Resume-based re-education and semantic embedding matching for career recommendation in evolving technical labor markets. | `Paper13_zhang2023careergai.pdf`, Section 3.3, pp. 518–521 | §II-D | **VERIFIED** |
| **CIT-12** | `Paper14` | `\cite{b12}`: Deshmukh & Kulkarni (2025) | AI-driven mock interview systems; observing that verbal lexical analysis alone fails to evaluate behavioral and paralinguistic composure. | `Paper14_deshmukh2025review.pdf`, Section 2.3, pp. 38–41 | §II-E | **VERIFIED** |
| **CIT-13** | `Paper15` | `\cite{b13}`: Advanced Innovation Consortium (2025) | Multimodal mock interview system integrating facial expressions, speech emotion recognition, and NLP for holistic evaluation. | `Paper15_consortium2025multimodal.pdf`, Section 3.2, pp. 95–99 | §II-E, §VI-D | **VERIFIED** |
| **CIT-14** | `Paper16` | `\cite{b14}`: Tan et al. (2024) | Unified framework for personalized learning pathways; establishing that prerequisite precedence must be strictly preserved in automated curriculum scheduling. | `Paper16_tan2024unified.pdf`, Section 4.1, pp. 100234:4–8 | §II-F, §VI-E | **VERIFIED** |
| **CIT-15** | `Paper17` | `\cite{b15}`: Verma & Mehta (2026) | ResuMatch: Automated resume screening leveraging dense semantic embeddings and skills taxonomy matching. | `Paper17_verma2026resumatch.pdf`, Section 3.2, pp. 460–464 | §II-D | **VERIFIED** |
| **CIT-16** | `Paper18` | `\cite{b16}`: Hidayatulloh et al. (2026) | Explainable AI for student academic performance prediction; showing that Shapley additive explanations enhance educator transparency. | `Paper18_hidayatulloh2026explainable.pdf`, Section 4.3, pp. 50–53 | §II-C | **VERIFIED** |
| **CIT-17** | `Paper19` | `\cite{b17}`: Joshi & Kulkarni (2025) | ExplainAI: Transparent decision support using gradient boosting and TreeSHAP to diagnose academic deficits across engineering disciplines. | `Paper19_joshi2025explainai.pdf`, Section 3.3, pp. 91–95 | §II-C | **VERIFIED** |
| **CIT-18** | `Paper20` | `\cite{b18}`: Sutherland & Miller (2025) | Retrieval-augmented generation in educational dialog systems; demonstrating that similarity threshold gating prevents out-of-domain hallucinations. | `Paper20_sutherland2025retrieval.pdf`, Section 4.2, pp. 152–158 | §II-F, §VI-E | **VERIFIED** |
| **CIT-19** | `Paper29` | `\cite{b19}`: Srinivasan & Radhakrishnan (2025) | Voice-driven mock interview simulation combining automatic speech recognition with generative language modeling; identifying turn latency bottlenecks. | `Paper29_srinivasan2025aimock.pdf`, Section 3.1, pp. 81–84 | §II-E, §VI-D | **VERIFIED** |
| **CIT-20** | `Paper26` | `\cite{b20}`: Fernandez & Gomez (2025) | Survey of automated question generation; establishing the necessity of causal concept graph alignment to ensure cognitive depth and distractor plausibility. | `Paper26_fernandez2025automated.pdf`, Section 4.3, pp. 18–24 | §II-F | **VERIFIED** |
| **CIT-21** | `Paper41` | `\cite{b21}`: Babureddy & Mathew (2026) | Triangular employability digital twin framework integrating student, faculty, and industry intelligence for continuous career readiness tracking. | `Paper41_consortium2026triangular.pdf`, Section 4.3, pp. 18–23 | §II-F | **VERIFIED** |

---

## 2. Citation Integrity Certification

- **Zero Fabricated Citations**: Every citation corresponds to a downloaded, verified PDF in `01_Research_Foundation/Papers/PDFs/` and a verified BibTeX entry in `01_Research_Foundation/Papers/BibTeX/`.
- **Zero Undefined Citations**: All `\cite{...}` tags in `paper.tex` map to valid entries in the bibliography.
- **Traceable Page/Section References**: Every asserted claim is verified against the specific section of the cited literature.
