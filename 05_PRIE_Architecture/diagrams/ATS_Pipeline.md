# PRIE Architecture: ATS Resume Pipeline

## 1. Overview and Purpose
This document provides the architectural pipeline diagram for the **PRIE Applicant Tracking System (ATS) & Resume Intelligence Engine (M06)**. 

The pipeline bridges document vision and natural language processing by combining **LayoutLMv3** (2D spatial visual-document parsing) with **Sentence-BERT** (dense semantic vector matching against target Job Descriptions), strictly enforcing the algorithms and boundaries defined in [`ATS_Architecture.md`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/ATS_Architecture.md). The engine outputs three foundational features into the Student Profile Vector: `F11: ats_resume_score`, `F12: resume_quantified_bullets_ratio`, and `F13: technical_skills_match_ratio`.

---

## 2. Mermaid ATS Resume Pipeline Diagram

```mermaid
flowchart TD
    %% Styling
    classDef inputPdf fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b;
    classDef spatialDoc fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#e65100;
    classDef nlpModel fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    classDef vectorMath fill:#ede7f6,stroke:#7b1fa2,stroke-width:2px,color:#4a148c;
    classDef scoreStage fill:#fce4ec,stroke:#c2185b,stroke-width:3px,color:#880e4f;
    classDef outputFeedback fill:#eceff1,stroke:#455a64,stroke-width:2px,color:#263238;

    %% Ingress Sources
    subgraph INGRESS ["Ingress Documents"]
        DOC_RESUME["Student Resume Document<br/>(PDF / DOCX Format)"]:::inputPdf
        DOC_JD["Target Job Description (JD)<br/>(Role Requirements & Hard Skills)"]:::inputPdf
    end

    %% Document Preprocessing & Spatial Layout Extraction
    subgraph STAGE_SPATIAL ["Stage 1: Spatial Layout & Bounding Box Extraction"]
        PDF_PARSER["PyMuPDF & Tesseract OCR<br/>(Text Stream + Bounding Boxes [x0, y0, x1, y1])"]:::spatialDoc
        LAYOUTLM_MODEL["LayoutLMv3 Multimodal Tokenizer<br/>- 2D Positional Embeddings<br/>- Visual Patch Encodings<br/>- Text Token Sequence"]:::spatialDoc
        LAYOUT_ENTITIES["Structured Document Entities<br/>- Header / Contact Block<br/>- Education Hierarchy<br/>- Work Experience & Projects<br/>- Technical Skills Sub-blocks"]:::spatialDoc
    end

    %% Semantic Encoding & Vector Representation
    subgraph STAGE_SEMANTIC ["Stage 2: Dense Semantic Encoding (Sentence-BERT)"]
        SBERT_MODEL["Sentence-BERT Model (`all-mpnet-base-v2`)<br/>(Mean-Pooled Dense Representation)"]:::nlpModel
        EMB_RESUME["Resume Semantic Vector<br/>$$\mathbf{e}_{\text{res}} \in \mathbb{R}^{768}$$"]:::nlpModel
        EMB_JD["Job Description Semantic Vector<br/>$$\mathbf{e}_{\text{jd}} \in \mathbb{R}^{768}$$"]:::nlpModel
    end

    %% Quantitative & Heuristic Auditing
    subgraph STAGE_AUDIT ["Stage 3: Quantified Impact & Rule-Based Heuristics"]
        REGEX_QUANT["Regex & Spacy Numeric Matcher<br/>(Detects %, $, ms, scale metrics in bullet points)"]:::vectorMath
        SKILL_TAXONOMY["Curated Technical Taxonomy Matcher<br/>(ESCO / O*NET CS Concepts & Frameworks)"]:::vectorMath
        FORMAT_CHECK["Spatial Formatting Penalizer<br/>(Detects unreadable tables, multi-column clashes)"]:::vectorMath
    end

    %% Multi-factor Scoring Engine
    subgraph STAGE_SCORING ["Stage 4: Multi-Factor ATS Scoring Synthesis"]
        SIM_COSINE["Dense Semantic Similarity<br/>$$S_{\text{dense}} = \cos(\mathbf{e}_{\text{res}}, \mathbf{e}_{\text{jd}})$$"]:::scoreStage
        RECALL_EXACT["Hard Skill Exact Match Recall<br/>$$R_{\text{skills}} = |K_{\text{res}} \cap K_{\text{jd}}| / |K_{\text{jd}}|$$"]:::scoreStage
        RATIO_QUANT["Quantified Bullet Points Ratio<br/>$$Q_{\text{ratio}} = B_{\text{quant}} / B_{\text{total}}$$"]:::scoreStage
        FINAL_SYNTHESIS["Multi-Criteria Synthesis Function<br/>$$S_{\text{ATS}} = \alpha S_{\text{dense}} + \beta R_{\text{skills}} - \gamma P_{\text{format}}$$"]:::scoreStage
    end

    %% Outputs & Feedbacks
    subgraph STAGE_OUTPUT ["Stage 5: Output Artifacts & SPV Mutations"]
        SPV_UPDATES["<b>SPV Invariant Feature Updates (M01)</b><br/>- F11: ats_resume_score [0.0, 100.0]<br/>- F12: resume_quantified_bullets_ratio [0.0, 1.0]<br/>- F13: technical_skills_match_ratio [0.0, 1.0]"]:::outputFeedback
        FEEDBACK_JSON["<b>Actionable Student Remediation Report</b><br/>- Missing Hard Keywords (e.g., Kafka, Docker)<br/>- Weak Action Verb Flags (e.g., 'Helped', 'Worked on')<br/>- Unquantified Experience Bullets Identified<br/>- Layout Parser Degradation Warnings"]:::outputFeedback
    end

    %% Connections
    DOC_RESUME --> PDF_PARSER
    PDF_PARSER --> LAYOUTLM_MODEL
    LAYOUTLM_MODEL --> LAYOUT_ENTITIES

    LAYOUT_ENTITIES --> SBERT_MODEL
    DOC_JD --> SBERT_MODEL
    SBERT_MODEL --> EMB_RESUME
    SBERT_MODEL --> EMB_JD

    LAYOUT_ENTITIES --> REGEX_QUANT
    LAYOUT_ENTITIES --> SKILL_TAXONOMY
    LAYOUT_ENTITIES --> FORMAT_CHECK
    DOC_JD --> SKILL_TAXONOMY

    EMB_RESUME --> SIM_COSINE
    EMB_JD --> SIM_COSINE
    SKILL_TAXONOMY --> RECALL_EXACT
    REGEX_QUANT --> RATIO_QUANT

    SIM_COSINE --> FINAL_SYNTHESIS
    RECALL_EXACT --> FINAL_SYNTHESIS
    RATIO_QUANT --> FINAL_SYNTHESIS
    FORMAT_CHECK --> FINAL_SYNTHESIS

    FINAL_SYNTHESIS --> SPV_UPDATES
    FINAL_SYNTHESIS --> FEEDBACK_JSON
    REGEX_QUANT --> FEEDBACK_JSON
    SKILL_TAXONOMY --> FEEDBACK_JSON
```

---

## 3. Operational Guarantees and Thresholds

| Pipeline Step | Module / Library | SLA / Target | Validation Constraint |
| :--- | :--- | :--- | :--- |
| **Document Ingestion** | PyMuPDF / Tesseract | $< 2.0\text{ s}$ per 2-page PDF | File size capped at $10\text{ MB}$; password-protected PDFs rejected |
| **Visual Bounding Boxes** | LayoutLMv3 Tokenizer | $< 4.0\text{ s}$ (GPU/CPU worker) | Bounding boxes normalized to $[0, 1000]$ coordinate space |
| **Dense Semantic Vector** | S-BERT `all-mpnet-base-v2` | $< 800\text{ ms}$ | Vector dimension invariant at $\mathbb{R}^{768}$; unit L2 normalized |
| **Quantified Bullets** | spaCy Cardinal/Percent Extractor | $< 300\text{ ms}$ | Strict regex: requires number + action verb + noun object |
| **ATS Composite Score** | Weighted Synthesis | $< 100\text{ ms}$ | Bounds strictly mapped to $[0.0, 100.0]$ |
| **Downstream Mutation** | M01 Profile Vector Sync | Asynchronous queue | Atomically updates $F11, F12, F13$ within database transaction |
