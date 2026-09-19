# Resume Processing Methodology: Document Ingestion, Bounding Box Extraction & Robust Section Segmentation

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Resume_Processing_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Resume Processing Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Document Ingestion & Image Standardization

Resumes arrive as heterogeneous, frequently non-conformant PDF or DOCX binary streams. The ingestion pipeline enforces a robust normalization sequence:

1. **Format Validation**: File magic headers are checked (`%PDF-`). DOCX files are converted to standardized PDFs via headless LibreOffice in an isolated sandbox.
2. **Page Rendering**: PDF pages are rendered into lossless RGB images at 300 DPI (yielding typical dimensions of $2480 \times 3508$ pixels for A4).
3. **Deskewing & Contrast Enhancement**: OpenCV Hough transform detects page tilt angles ($\theta > 1.5^\circ$); affine rotations deskew pages prior to OCR.

---

## 2. Bounding Box Extraction & Coordinate Geometry

Tesseract 5 OCR processes the rendered page images to extract word-level tokens along with their visual bounding box rectangles $[x_{\text{min}}, y_{\text{min}}, x_{\text{max}}, y_{\text{max}}]$.

Coordinates are projected onto the standard integer grid $[0, 1000] \times [0, 1000]$:
$$x_0 = \text{round}\left( \frac{x_{\text{min}}}{W} \times 1000 \right), \quad y_0 = \text{round}\left( \frac{y_{\text{min}}}{H} \times 1000 \right)$$
$$x_1 = \text{round}\left( \frac{x_{\text{max}}}{W} \times 1000 \right), \quad y_1 = \text{round}\left( \frac{y_{\text{max}}}{H} \times 1000 \right)$$

---

## 3. Heuristic Section Detection & Block Grouping

To assist the downstream transformer and handle documents exceeding 512 tokens:
1. **Header Identification**: Regex patterns identify standard section header text (e.g., `EDUCATION`, `TECHNICAL SKILLS`, `PROJECTS`, `WORK EXPERIENCE`).
2. **Spatial Block Clustering**: Words sharing vertical bounding box overlaps are clustered into cohesive visual paragraphs using connected component analysis.
3. **Malformed Document Fallback**: If PDF stream extraction reveals corrupted fonts or scanned raster images without a text layer, the pipeline automatically switches to full OCR engine fallback with image contrast normalization.
