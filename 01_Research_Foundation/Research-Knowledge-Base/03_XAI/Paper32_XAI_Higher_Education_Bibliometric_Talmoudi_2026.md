# Paper 32 — From Predictive Analytics to Explainable AI in Higher Education: A Bibliometric Mapping

## 1. Bibliographic Information

- **Paper ID**: Paper32
- **Full Title**: From Predictive Analytics to Explainable AI in Higher Education: A Bibliometric Mapping
- **Authors**: Ramzi Talmoudi and Jamel Choukir
- **Institution**: Department of Business Administration, College of Business, Imam Mohammad Ibn Saud Islamic University (IMSIU), Riyadh 13318, Kingdom of Saudi Arabia
- **Year**: May 2026
- **Venue**: Qubahan Academic Journal, Volume 6, No. 2, May 2026, pp. 437–461
- **DOI**: 10.48161/qaj.v6n2a2559
- **PDF filename**: `Paper32_viberg2025predictive.pdf` (Note: filename reflects legacy bibtex tag `viberg2025predictive`; authentic PDF confirms authors Ramzi Talmoudi and Jamel Choukir, Qubahan Academic Journal May 2026)
- **PDF path**: `Papers/PDFs/Paper32_viberg2025predictive.pdf`
- **Page count**: 25 pages (pp. 437–461)

---

## 2. Research Problem

Over the past three decades, higher education institutions have increasingly deployed Educational Data Mining (EDM) and machine learning models to predict student academic success and dropout risks. However, the dominant literature has relied almost exclusively on opaque, black-box classification algorithms. While achieving high benchmark accuracy, these systems face severe managerial bottlenecks: frontline academic advisors and educators suffer from algorithmic aversion and distrust, because unexplainable risk flags provide zero causal rationale or actionable guidance on how to remediate student deficiencies.

### Source Evidence
- **Page**: PDF pp. 1–2, 13–15 (pp. 437–438, 449–451)
- **Section**: Abstract, Section I — Introduction, and Section VI.2 — Trust, Algorithmic Aversion, and the XAI Mandate

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To execute a rigorous PRISMA 2020-compliant bibliometric analysis mapping the evolutionary structural trends of data-driven student success management over three decades (1996–2025).
2. To apply co-word analysis, co-citation mapping, and Louvain clustering to delineate the thematic architecture across basic, motor, niche, and emerging quadrants.
3. To trace the macro-level paradigm shift from black-box predictive modeling to Explainable Artificial Intelligence (XAI) and generative AI interventions.
4. To formulate socio-technical managerial implications for university leadership regarding ethical AI governance, data privacy, and human-in-the-loop decision empowerment.

### Source Evidence
- **Page**: PDF pp. 1, 3–4 (pp. 437, 439–440)
- **Section**: Abstract & Section I

---

## 4. Research Questions

The study investigates three core bibliometric and structural dimensions:
1. What are the macro-level publication volumes, geographic affiliations, and collaboration networks shaping AI-driven student success management?
2. How has the conceptual architecture evolved from early predictive modeling to modern transparent XAI frameworks?
3. What are the managerial and ethical prerequisites required for educational leaders to deploy trusted predictive learning analytics?

### Source Evidence
- **Page**: PDF pp. 2–4
- **Section**: Section I & Section III

---

## 5. Dataset / Survey Corpus

- **Indexing Source**: Web of Science (WoS) Core Collection indexes: Social Sciences Citation Index (SSCI), Arts & Humanities Citation Index (AHCI), and Emerging Sources Citation Index (ESCI).
- **Timeframe**: 30-year longitudinal window: **1996 to 2025**.
- **PRISMA 2020 Protocol (Figure 1)**:
  - Initial database records identified: **727**
  - Removed before screening (ineligible types): **48**
  - Records screened: **679** (198 excluded)
  - Full-text reports assessed for eligibility: **481** (455 articles, 25 reviews)
  - Excluded anomalies: **6**; non-English records excluded: **18**
  - **Final Included Studies**: **457 peer-reviewed English journal articles**
- **Reference Disambiguation**: 19,304 raw citations merged via Jaro-Winkler string distance into **19,029 unique normalized references**.
- **Thesaurus Harmonization**: 1,322 author keywords consolidated into **1,226 standardized semantic nodes** across target outcomes, contexts, algorithms, and strategic frontiers.

### Source Evidence
- **Page**: PDF pp. 6–8 (pp. 442–444)
- **Section**: Section III.2 & Figure 1 (PRISMA 2020 Flow Diagram)

---

## 6. Features / Conceptual Taxonomy

The bibliometric mapping identifies core feature and thematic categories:
- **Predictive Target Variables**: Academic performance, student retention, dropout prediction, early warning flags, course completion.
- **Data Ingestion Sources**: Learning Management System (LMS) logs (Moodle, Blackboard), student information systems (SIS), clickstream interaction telemetry, psychometric surveys.
- **Methodological Dimensions**: Classical statistical regression, supervised machine learning (Random Forest, SVM, Decision Trees), deep neural networks, ensemble learning.
- **The Strategic Frontier**: Explainable AI (SHAP, LIME, counterfactuals), Generative AI (ChatGPT, LLMs), and algorithmic trust governance.

### Source Evidence
- **Page**: PDF pp. 6–8, 12–14 (pp. 442–444, 448–450)
- **Section**: Section III.3 & Section V.2

---

## 7. Data Preprocessing & Bibliometric Pipeline

The analysis pipeline utilized:
- **Software Tools**: R Statistical Computing Environment (v4.5.3) and `bibliometrix` R-package (v5.0) via the `biblioshiny` web interface.
- **Normalization Algorithms**:
  - *Jaro-Winkler matching*: Disambiguating 275 variant citation strings.
  - *Custom Thesaurus Cleansing*: Eliminating lexical fragmentation (e.g., merging "XAI", "explainable AI", and "explainability" into a single definitive node).
  - *Association Strength Metric*: Normalizing co-occurrence matrix weights to prevent bias from generic high-frequency terms.
- **Clustering & Mapping**:
  - *Louvain Community Detection*: Partitioning the keyword network into dense sub-communities ($n=250$ top words).
  - *Callon Centrality & Density*: Plotting clusters across the two-dimensional thematic matrix.

### Source Evidence
- **Page**: PDF pp. 6–8, 12–13 (pp. 442–444, 448–449)
- **Section**: Section III.3 & Section V.2

---

## 8. Algorithms and Models Reviewed in the Corpus

The bibliometric mapping synthesizes the historical adoption of ML/DL in higher education:
1. **Classical Early Warning Systems (EWS)**: Decision Trees (C4.5, CART), Logistic Regression, Naive Bayes, and Random Forest (Breiman 2001) dominated the 2000–2018 era.
2. **Class Imbalance Handlers**: Widespread adoption of SMOTE (Chawla et al. 2002) to handle low-frequency student dropout classes.
3. **Deep Learning**: Multi-layer perceptrons (MLP), LSTMs, and CNNs deployed on sequential clickstream data (2018–2022).
4. **Explainable AI (XAI)**: SHAP (Lundberg & Lee 2017) and LIME (Ribeiro et al. 2016) emerging as essential post-hoc interpretability layers (2022–2025).
5. **Generative AI**: LLMs and interactive dialogue agents emerging as frontline personal advising tools (2023–2025).

### Source Evidence
- **Page**: PDF pp. 11–14 (pp. 447–450)
- **Section**: Section V.1 & Figure 6 (Co-citation Network)

---

## 9. Conceptual Architecture

The paper establishes a **Socio-Technical Architecture for Educational Data Mining** (Section II):
- **Technical Layer**: Ingestion (LMS, SIS, behavioral telemetry) $\rightarrow$ Preprocessing & Feature Selection $\rightarrow$ Predictive Modeling (ML/DL) $\rightarrow$ Explainability Engine (SHAP/LIME feature attributions).
- **Human-in-the-Loop Management Layer**: Explainable Dashboard $\rightarrow$ Frontline Academic Advisors / Placement Officers $\rightarrow$ Tailored Intervention (advising, tutoring, psychological support) $\rightarrow$ Student Success Outcome.
- **Governance Envelope**: Data privacy standards (GDPR, FERPA), algorithmic transparency, and ethical bias monitoring.

### Source Evidence
- **Page**: PDF pp. 4–6, 15–18 (pp. 440–442, 451–454)
- **Section**: Section II & Section VI

---

## 10. Methodology

1. **Protocol Formulation**: Defined WoS search strings and PRISMA screening boundaries.
2. **Bibliographic Extraction**: Retrieved 457 qualifying articles across SSCI/AHCI/ESCI.
3. **Reference & Keyword Cleansing**: Applied Jaro-Winkler disambiguation and a custom educational data mining thesaurus.
4. **Network Science Mapping**: Calculated co-authorship collaboration networks, journal productivity distributions (Bradford's Law), and co-citation topologies.
5. **Thematic Evolution Analysis**: Generated Callon centrality/density quadrant maps tracing diachronic shifts across sub-periods.

### Source Evidence
- **Page**: PDF pp. 6–9
- **Section**: Section III

---

## 11. Experimental Setup

- **Software Stack**: R v4.5.3, Bibliometrix v5.0, Biblioshiny GUI.
- **Corpus Demographics**: 457 articles; 25% international co-authorship collaboration rate; China and United States universities produced the highest publication volumes; *Applied Sciences* emerged as the leading publishing venue.

### Source Evidence
- **Page**: PDF pp. 1, 9–11 (pp. 437, 445–447)
- **Section**: Abstract & Section IV (Descriptive Bibliometrics)

---

## 12. Evaluation Metrics

- **Callon Centrality**: Measures the intensity of external links from a thematic cluster to other parts of the network (relevance / structural importance).
- **Callon Density**: Measures the internal strength and development maturity of edges within a thematic cluster.
- **Stability Index**: Evaluates longitudinal persistence of keyword clusters across consecutive time slices.
- **Modularity Score**: Evaluates cluster partitioning quality in the Louvain community detection algorithm.

### Source Evidence
- **Page**: PDF pp. 7–8, 12–13
- **Section**: Section III.3 & Section V.2

---

## 13. Results

### Thematic Map Quadrant Distribution (Figure 7 & Section V.2)
1. **Basic Themes (High Centrality, Low Density)**: Early Warning Systems (EWS), Predictive Modeling, Dropout Prediction. These form the indispensable structural bedrock of educational data mining.
2. **Motor Themes (High Centrality, High Density)**: Generative Artificial Intelligence (ChatGPT) and Psychological Constructs (self-efficacy, academic motivation). These are currently driving rapid field expansion.
3. **Emerging Themes (Low Centrality, High Dynamic Growth)**: **Explainable Artificial Intelligence (XAI)**. While emerging over the 30-year baseline, XAI has transitioned into a foundational, highly active priority for the 2024–2025 window.
4. **Co-Citation Fusion (Figure 6)**: The intellectual base merges foundational educational retention theories (e.g., Vincent Tinto's student integration model) directly with machine learning algorithms (Random Forest, SMOTE).

### Managerial Findings (Section VI)
- **Resolution of Algorithmic Aversion**: Advisors reject predictive scores when delivered as raw numerical probabilities; providing SHAP waterfall plots and feature contribution rankings dissolves faculty resistance.
- **Economic ROI**: Early detection of at-risk students translates directly into institutional financial sustainability by preventing student attrition.

### Source Evidence
- **Page**: PDF pp. 11–16 (pp. 447–452)
- **Section**: Section V & Section VI

---

## 14. Baselines

- Standard historical bibliometric studies that treated educational data mining as pure predictive modeling without accounting for the recent emergence of XAI and Generative AI.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section I

---

## 15. Ablation Study

- *Not applicable* (Bibliometric mapping and science visualization methodology).

---

## 16. Explainability

- **Central Focus of the Study**: The entire paper investigates the paradigm shift toward Explainable AI (XAI) in higher education:
  - Demonstrates that post-hoc interpretability (SHAP, LIME) is not merely a technical luxury, but a mandatory socio-technical requirement for user trust, ethical compliance, and institutional adoption.

### Source Evidence
- **Page**: PDF pp. 1, 14–17 (pp. 437, 450–453)
- **Section**: Title, Abstract, Section VI.2

---

## 17. Main Findings

1. Higher education research has decisively concluded that **prediction accuracy alone is insufficient**; opaque algorithms create friction with educators and violate ethical accountability.
2. The field has evolved through three distinct eras: (1) abstract sociological retention models (1990s), (2) opaque black-box machine learning optimization (2010s), and (3) transparent, Explainable Student Success Management (2020s).
3. The future of educational intelligence lies in pairing predictive algorithms with XAI for causal diagnosis, and leveraging Generative AI for personalized student dialogue.

### Source Evidence
- **Page**: PDF pp. 15–19 (pp. 451–455)
- **Section**: Section VI & Section VII

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Single Database Limitation**: Restricted to the Web of Science Core Collection, potentially omitting studies indexed solely in Scopus, IEEE Xplore, or Google Scholar.
2. **Peer-Reviewed Journal Restriction**: Excluded conference proceedings (which represent a substantial portion of computer science literature) to ensure standardized metadata.
3. **Language Bias**: Excluded 18 non-English publications, creating an Anglo-centric and international English journal focus.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: Because the WoS query emphasized general student academic performance and retention in higher education, specialized enterprise recruitment and placement-specific AI papers might be under-represented relative to broad undergraduate academic success studies.

### Source Evidence
- **Page**: PDF pp. 6–7 (pp. 442–443)
- **Section**: Section III.2

---

## 19. Future Work

Explicitly proposed by the authors:
1. Conducting multi-database cross-comparisons including Scopus and IEEE Xplore conference proceedings.
2. Investigating empirical educator behavioral responses to XAI interfaces in live university advising workflows.
3. Developing standardized ethical AI governance frameworks specifically tailored to generative AI in higher education.

### Source Evidence
- **Page**: PDF pp. 18–19 (pp. 454–455)
- **Section**: Section VII — Conclusion

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides macro-level scholarly justification for PRIE's core architectural thesis:
1. **Validation of PRIE's XAI Pillar**: PRIE's placement readiness engine is built on the explicit philosophy that predicting whether a student will get placed is useless unless the engine explains *why* (via SHAP/LIME) and identifies *what skills to improve*. Talmoudi & Choukir prove that the global higher education literature has formally identified this exact mandate.
2. **Mitigating Placement Officer Aversion**: ScholarCamp's institutional dashboard must provide college placement coordinators with transparent feature importance visualizers rather than opaque risk scores, directly aligning with Talmoudi & Choukir's socio-technical advising guidelines.
3. **Synthesis of EWS + XAI + GenAI**: Talmoudi & Choukir conclude that optimal systems unite Early Warning (Predictive), Transparent Explanation (XAI), and Interactive Dialogue (GenAI). This is the exact triumvirate instantiated in PRIE (Prediction + SHAP + Mock Interview Copilot).

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **Core Research Scope** | "A PRISMA-based bibliometric analysis of 457 articles... retrieved from Web of Science Core Collection (1996-2025)... using R bibliometrix." | PDF p. 1, Abstract | Direct statement / Scope |
| **Citation & Keyword Cleaning** | 19,304 citations merged into 19,029 unique references via Jaro-Winkler; 1,322 keywords consolidated to 1,226 via custom thesaurus. | PDF pp. 6–7, Section III.3 | Methodology / Quantitative |
| **Thematic Map Findings** | EWS and Predictive Modeling are Basic Themes; Generative AI and psychological constructs are Motor Themes; XAI is an Emerging Theme. | PDF p. 1, Abstract & pp. 12–14, Section V.2 | Bibliometric result |
| **International Collaboration** | "network analysis indicates an international collaboration rate of 25%." | PDF p. 1, Abstract & p. 11, Section V.1 | Bibliometric result |
| **The Algorithmic Aversion Mandate** | Frontline academic advisors resist black-box predictions; transparent XAI explanations are required to bridge digital predictions and human advising. | PDF pp. 14–16, Section VI.2 | Author finding / Discussion |
| **Stated Study Limitations** | Single database (WoS Core Collection), exclusion of conference proceedings, and exclusion of 18 non-English documents. | PDF pp. 6–7, Section III.2 | Author limitation |

---

## 22. Verification Checklist

- [x] PDF read (`Paper32_viberg2025predictive.pdf`, 25 pages)
- [x] Introduction inspected
- [x] Related work / socio-technical architecture inspected
- [x] Methodology inspected (PRISMA 2020, R bibliometrix 5.0, Jaro-Winkler disambiguation)
- [x] Corpus verified (457 articles from Web of Science Core Collection, 1996–2025)
- [x] Features verified (Predictive targets, LMS clickstream logs, ML/DL algorithms, XAI, GenAI)
- [x] Algorithms verified (Louvain community clustering, Callon centrality and density, Association Strength)
- [x] Architecture inspected (Socio-technical EDM pipeline, Figure 1 PRISMA flowchart)
- [x] Thematic analysis verified (Basic, Motor, Niche, Emerging quadrants)
- [x] Results verified (Shift from black-box to XAI, 25% international collaboration, resolution of algorithmic aversion)
- [x] Limitations verified (WoS-only, exclusion of proceedings, English language restriction)
- [x] Future work verified (Cross-database mapping, live advisor trials, generative AI governance)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact 457-article PRISMA protocol from Section III.2, Jaro-Winkler normalization from Section III.3, Louvain thematic mapping from Section V.2, and managerial XAI implications from Section VI verified directly from source text; legacy filename discrepancy documented).
