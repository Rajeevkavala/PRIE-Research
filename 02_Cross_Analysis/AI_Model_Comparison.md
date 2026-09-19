# AI Model Comparison & Foundation Architecture Taxonomy

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/AI_Model_Comparison.md`  
**Status**: Authoritative AI Model Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. AI Model Ecosystem & Categorization

Modern educational and recruitment intelligence systems heavily rely on pre-trained foundation models, transformer encoders, dense vector embeddings, and multimodal neural processors. Across the 44 verified primary research papers, AI models are classified into four (4) core technical tiers:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            AI MODEL FOUNDATION TIERS                             │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Model Tier                    │ Representative Models in Corpus                  │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Foundation LLMs (Cloud)    │ OpenAI GPT-3.5-Turbo, GPT-4, Anthropic Claude 3, │
│                               │ Google Gemini 1.5 Pro, Google Gemini 1.5 Flash.  │
│ 2. Open-Weights LLMs (Local)  │ Meta LLaMA-2-7B (LoRA), Meta LLaMA-3-8B-Instruct│
│                               │ (4-bit AWQ quantized), Mistral-7B-Instruct.      │
│ 3. Dense Embedding Models     │ Sentence-BERT (all-MiniLM-L6-v2, all-mpnet-base),│
│                               │ BAAI BGE-small, Doc2Vec (PV-DM), BERT-base-uncased│
│ 4. Speech & Vision Modalities │ OpenAI Whisper-v3, Wav2Vec 2.0, openSMILE toolkit│
│                               │ MediaPipe FaceMesh, LayoutLMv3, VGG-16, TrOCR.   │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Comprehensive Model Benchmarking Matrix

The matrix below benchmarks all major AI models documented across the corpus, evaluating operational runtime, input/output modality, parameter scale, task accuracy, and deployment constraints:

| Model / Architecture | Paper ID | Parameter Count / Size | Modality | Primary Task in Corpus | Empirical Performance Reported | Deployment Runtime & Constraints |
|:---|:---|:---|:---|:---|:---|:---|
| **GPT-3.5-Turbo** | P13, P26, P30 | ~175B (Proprietary API)| Text | Career pathing & mock interview Q&A| 88.2% path completion, SUS: 82.4 | Cloud REST API; ~1.8s latency; token cost |
| **GPT-4 (Chain-of-Thought)**| P25 | ~1.8T MoE (Proprietary) | Text / DAG | Pedagogical MCQ generation (CoT) | 91.5% validity, 0.88 discrimination | Cloud API; high cost ($0.03/1k); 4.2s latency |
| **Claude-3-Sonnet** | P28 | ~70B equiv (Proprietary)| Text / Code | Live coding interview & feedback | 88.5% code review accuracy | Cloud API; Docker sandboxed; 3.1s latency |
| **Gemini 1.5 Pro** | P23 | >1T MoE (Proprietary) | Multimodal | Contextual academic RAG assistant | 92.8% factual precision, ROUGE: 0.74| Cloud API; 2M token window; 2.2s latency |
| **Gemini 1.5 Flash** | P29 | Lightweight Multimodal | Audio / Text| Real-time WebRTC mock interview bot| Acoustic acc: 90.1%, latency <1.2s | Cloud WebRTC stream; sub-second response |
| **LLaMA-3-8B-Instruct** | P21 | 8 Billion (4-bit AWQ) | Text | Private offline campus tutoring RAG | Faithfulness: 89.2%, Relevancy: 86.4%| Local consumer GPU (RTX 4060, 5.8GB VRAM) |
| **LLaMA-2-7B (LoRA fine-tuned)**| P39| 7 Billion (LoRA rank=16)| Text | Bloom's cognitive taxonomy AQG | 88.6% cognitive depth alignment | Local server GPU (A10G, 16GB VRAM); fast |
| **SBERT (`all-MiniLM-L6-v2`)**| P12, P17 | 22.7 Million (384-dim) | Text | Resume-to-JD semantic bi-encoder | MRR@10: 0.92, Top-5 Acc: 89.4% | CPU / OnnxRuntime; <35ms inference |
| **Doc2Vec (PV-DM)** | P35 | Unsupervised (300-dim) | Paragraph Text| Implicit skill mining from projects | 86.7% recall on unstated tech skills | Fast CPU training; static vocabulary drift |
| **LayoutLMv3** | P42 | 133 Million (Base) | Vision + Text | Cognitive IDP for multi-column resume| Entity F1: 0.948, Layout Acc: 98.2% | GPU required (~1.5s/page); 32% error drop |
| **OpenAI Whisper-v3** | P03, P28, P29 | 1.55 Billion (Large) | Audio-to-Text | Real-time speech transcription | Word Error Rate (WER) < 4.2% | GPU / faster-whisper; 650ms audio chunk |
| **Wav2Vec 2.0** | P14 | 317 Million | Speech Audio | Phoneme duration & speech rate | Speech rate correlation r=0.78 | CPU/GPU inference; sensitive to accent |
| **openSMILE Toolkit** | P03, P29 | Feature Extractor (eGeMAPS)| Audio Signal | Pitch (F0), jitter, shimmer, voice dB| Feature set: 88 acoustic attributes | Pure C++ engine; real-time streaming (<15ms)|
| **MediaPipe FaceMesh** | P03, P14, P15 | Lightweight Vision CNN | Video Frames | 468 3D facial landmarks, eye contact| Landmark tracking: 89.2% eye accuracy| Browser WebAssembly / CPU; 60 FPS real-time |

---

## 3. Critical Model Trade-offs & Empirical Insights

### 3.1 Cloud Foundation Models vs Local Quantized LLMs
- `[CROSS-PAPER OBSERVATION]` **The Privacy & Cost Dilemma**: While cloud proprietary models (Gemini 1.5 in P23/P29, GPT-4 in P25) deliver state-of-the-art multi-step reasoning and vast context windows (up to 2M tokens), they introduce significant recurring API expenses and violate student data privacy mandates (such as POPIA in P02 or FERPA).
- `[AUTHOR-STATED FACT]` Nisanth et al. (P21) demonstrated that an **AWQ 4-bit quantized LLaMA-3-8B** executed locally on a single consumer-grade GPU (RTX 4060, 6GB VRAM) achieved **89.2% faithfulness** in course curriculum Q&A, completely eliminating external API bills and ensuring zero student query leakage.

### 3.2 Fine-Tuning (LoRA) vs Prompt Engineering (Chain-of-Thought)
- `[CROSS-PAPER OBSERVATION]` **AQG Efficiency**: For specialized educational tasks such as question generation, Wang et al. (P25) achieved 91.5% validity using zero-shot GPT-4 with structured Chain-of-Thought prompts and causal graph verification. However, each question required 4.2 seconds and $0.03 in API costs.
- `[AUTHOR-STATED FACT]` In contrast, Dousary et al. (P39) fine-tuned a **LLaMA-2-7B model using LoRA** on 8,000 Bloom's-tagged questions, achieving **88.6% cognitive depth alignment** while generating questions in under 450 milliseconds on local hardware with zero marginal cost.

### 3.3 Semantic Embeddings: Bi-Encoders vs Cross-Encoders (P17)
- `[AUTHOR-STATED FACT]` Solanki et al. (P17) proved that while Cross-Encoders achieve marginally higher Mean Reciprocal Rank (MRR@10: 0.93 vs 0.92), their quadratic compute complexity ($O(N \times M)$) makes them 4.2x slower than **SBERT Bi-Encoders** ($O(N + M)$). SBERT combined with BM25 sparse re-ranking via Reciprocal Rank Fusion (RRF) achieved near-identical precision (89.4%) with sub-50ms latency.

---

## 4. ScholarCamp / PRIE Multi-Tier AI Architecture

To maximize performance while minimizing latency and operational cloud costs, PRIE must deploy an intelligent multi-tiered AI routing architecture:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             PRIE TIERED AI ORCHESTRATION                         │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ Operational Tier         │ Assigned Models & Functional Roles                    │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Tier 1: Client Edge      │ MediaPipe (WebAssembly) for eye tracking & gaze;      │
│ (Browser / WebAssembly)  │ Web Audio API for audio capture and speech detection. │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Tier 2: Local Core       │ LayoutLMv3 for multi-column resume parsing (P42);     │
│ (Self-Hosted Microservices) SBERT all-MiniLM-L6-v2 for semantic match (P12, P17); │
│                          │ faster-whisper-large-v3 for low-latency ASR (P28);    │
│                          │ openSMILE for real-time acoustic prosody (P29);       │
│                          │ LLaMA-3-8B-Instruct (4-bit) for private RAG (P21).    │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Tier 3: Cloud Heavyweight│ Gemini 1.5 Flash (via WebRTC) for dynamic mock        │
│ (Selective Cloud Escalation) interview conversational generation (P29);          │
│                          │ GPT-4 / Gemini 1.5 Pro for deep causal syllabus RAG   │
│                          │ and multi-agent question verification (P23, P25).     │
└──────────────────────────┴───────────────────────────────────────────────────────┘
```
