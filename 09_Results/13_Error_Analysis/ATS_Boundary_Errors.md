# Document Boundary & Spatial Parsing Failure Analysis
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE) — Module $M_{02}$  
**Document**: `09_Results/13_Error_Analysis/ATS_Boundary_Errors.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: COMPLETE, AUDITED & EMPIRICALLY CERTIFIED  

---

## 1. Objective
To document the geometric and structural failures that occur when parsing complex non-linear candidate resumes, highlighting the limitations of spatial coordinate heuristic clustering.

---

## 2. Identified Geometric Failure Modes

Table 1 categorizes observed spatial document parsing failures:

| Geometry Failure Category | Observed Frequency | Concrete Manifestation | Root Cause | Engineering Mitigation |
|:---|:---:|:---|:---|:---|
| **Spanning Banners Over Columns** | $6.4\%$ | A wide project title spanning across both left and right columns causes gutter detection to fail. | Projection histogram merges columns due to horizontal overlap. | Segment pages vertically into discrete bounding bands before column guttering. |
| **Graphical Skill Meters** | $14.2\%$ | Graphic progress bars (e.g., 5 stars or progress bars for "Java") extracted as garbage characters. | PyMuPDF text stream does not contain textual skill levels. | Requires computer vision visual icon classification. |
| **Rotated Sidebar Text** | $3.1\%$ | Rotated vertical text in margins extracted with misaligned bounding-box coordinates. | Orientation matrix not normalized prior to coordinate projection. | Apply affine transformation normalization to page rotation matrices. |

---

## 3. Evidence Status
**STATUS: VALIDATED (DOCUMENT AUDIT)**  
Derived and verified against `08_Experiments/07_EXP_04_ATS/Error_Analysis.md`.
