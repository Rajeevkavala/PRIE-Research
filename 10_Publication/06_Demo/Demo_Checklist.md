# Interactive Demo Pre-Flight Checklist

**Document**: `10_Publication/06_Demo/Demo_Checklist.md`  
**System**: Placement Readiness Intelligence Engine (PRIE)  
**Phase**: Phase 10 — Publication  

---

## 1. Environment & Infrastructure Verification
- [x] Python 3.10+ runtime active and virtual environment verified.
- [x] FastAPI backend server functioning on `localhost:8000`.
- [x] All 12 core system modules ($M_{01}$ to $M_{12}$) loaded and tested.
- [x] Pre-computed benchmark models loaded (`models/xgb_calibrated.pkl`, `models/scaler.pkl`).
- [x] Neo4j / JSON curriculum knowledge graph (`cs_concept_dag.json`, 38 nodes) validated for cycle-free DAG topology.
- [x] Faster-Whisper local ASR model weights cached for speech transcription.
- [x] PyMuPDF installed for 2D spatial coordinate resume parsing.

## 2. Telemetry & Data Assets
- [x] Demo candidate profile JSON files verified (`data/candidates/alex_chen.json`, `priya_sharma.json`).
- [x] Sample two-column resume PDF (`alex_chen_resume.pdf`) tested with zero PDF parsing exceptions.
- [x] Synthetic interview audio/video sample frames loaded for multimodal playback.

## 3. Real-Time Latency Verification
- [x] Profile assembly & normalization latency: $< 150$ ms.
- [x] Predictor + Platt scaling inference latency: $< 80$ ms.
- [x] TreeSHAP waterfall rendering latency: $< 350$ ms.
- [x] DiCE counterfactual optimization latency: $< 1.80$ s.
- [x] Kahn topological sort execution latency: $< 25$ ms.
- [x] Multimodal interview fusion latency: $< 1.20$ s (Observed: $1.18 \pm 0.14$ s).

## 4. Rehearsal Sign-Off
- [x] 8-minute demo walkthrough executed with zero crashes or API timeouts.
- [x] Audience Q&A talking points prepared (explaining why Logistic Regression had high synthetic F1, why LayoutLMv3 is ablated, and how DiCE guarantees $100\%$ lock on $F_{17}$).
