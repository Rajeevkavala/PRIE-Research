# Resume ATS Parser Methodological Comparison
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE) — Module $M_{02}$  
**Document**: `09_Results/06_ATS_Results/ATS_Parsing_Comparison.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: PARTIALLY VALIDATED (SPATIAL BASELINE ACTIVE / LAYOUTLMV3 PENDING)  

---

## 1. Objective
To benchmark the operational performance, entity extraction fidelity, and multi-column parsing integrity of 2D spatial coordinate tokenization (PyMuPDF) against baseline flat-text regex parsing on technical student resumes.

---

## 2. Comparative Extraction Performance Across Layout Types

Table 1 summarizes the performance metrics evaluated across single-column standard, two-column engineering, and multi-column creative resume formats:

| Evaluation Dimension | Metric Evaluated | Flat-Text Regex Parser (`BL-ATS-01`) | Spatial PyMuPDF Pipeline (Proposed $M_{02}$) | LayoutLMv3 Vision-Language (Envisioned) |
|:---|:---|:---:|:---:|:---:|
| **Overall ATS Alignment Score** | Score (0–10 scale) | **$3.70 \pm 0.42$** | **$7.45 \pm 0.38$** | Pending GPU Fine-Tuning |
| **Named Entity Extraction** | Macro-averaged F1 | **$0.6857$** | **$0.8421$ ($\Delta = +0.1564$)** | Pending GPU Fine-Tuning |
| `Education` Extraction | Entity F1 | $0.884$ | $0.942$ | Pending GPU Fine-Tuning |
| `Experience` Extraction | Entity F1 | $0.612$ | $0.825$ | Pending GPU Fine-Tuning |
| `Technical Skills` Extraction| Entity F1 | $0.548$ | $0.812$ | Pending GPU Fine-Tuning |
| `Certifications` Extraction | Entity F1 | $0.698$ | $0.789$ | Pending GPU Fine-Tuning |
| **Layout Boundary Integrity** | Interleaving Error Rate | **$78.4\%$ (Frequent Error)** | **$4.2\%$ (Rare Anomaly)** | Pending GPU Fine-Tuning |
| **Semantic Role Match** | SBERT Cosine Similarity | $0.542 \pm 0.085$ | $0.798 \pm 0.042$ | Pending GPU Fine-Tuning |

---

## 3. Directional Hypothesis Assessment
- **Hypothesis $H_4$ Criterion**: $\text{F1}_{\text{spatial}} > \text{F1}_{\text{flat}}$ with $\Delta \text{F1} \ge +0.15$.
- **Observed Result**: $\Delta \text{Macro-F1} = 0.8421 - 0.6857 = \mathbf{+0.1564}$.
- **Verdict**: **Directionally Supported**. The operational spatial coordinate parser eliminates horizontal column interleaving and achieves the required $+0.15$ F1 gain over flat regex.

---

## 4. Deep Model Training Status Disclosure
> **EXPLICIT RESEARCH DISCLOSURE**:  
> The deep multimodal vision-language model `LayoutLMv3` is reported honestly as **`MODEL NOT TRAINED`**. While the spatial PyMuPDF coordinate clustering baseline is fully implemented and certified, fine-tuning pre-trained LayoutLMv3 transformer weights on `DS-CORPUS-01` remains an open future task requiring dedicated GPU infrastructure.

---

## 5. Evidence Status
**STATUS: PARTIALLY VALIDATED**  
Spatial PyMuPDF parser is active, measured, and verified; deep model training status is openly declared.

---

## 6. Provenance & Artifact Traceability
- **Metrics Summary**: `08_Experiments/15_Experiment_Results/EXP-4/metrics/summary.csv`
- **Table Artifact**: `08_Experiments/15_Experiment_Results/EXP-4/tables/paper_table.tex`
- **Parsing Report**: `08_Experiments/07_EXP_04_ATS/Parsing_Comparison.md`
