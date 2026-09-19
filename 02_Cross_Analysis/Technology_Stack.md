# Technology Stack Audit & Cross-System Infrastructure

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/Technology_Stack.md`  
**Status**: Authoritative Technology Stack Audit  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. Technology Ecosystem Overview

A critical assessment of the 44 verified primary research papers reveals an extensive landscape of programming languages, machine learning frameworks, databases, and deployment runtimes. This audit consolidates every technology documented across the corpus, categorizing them by layer:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            TECHNOLOGY STACK TAXONOMY                             │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Technology Layer              │ Documented Tools & Frameworks                    │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Programming Languages      │ Python 3.9–3.12, JavaScript / TypeScript, C++,   │
│                               │ R (Bibliometrix), SQL, Cypher (Graph Query).     │
│ 2. Frontend Frameworks        │ React.js, Next.js, Angular, Streamlit, Tailwind, │
│                               │ Monaco Code Editor, Cytoscape.js, Plotly.js.     │
│ 3. Backend & API Services     │ FastAPI, Express.js (Node.js), Flask, Django.    │
│ 4. ML & Deep Learning Core    │ PyTorch, TensorFlow, Scikit-Learn, CatBoost,     │
│                               │ XGBoost, LightGBM, Ray RLlib (Reinforcement Lrn).│
│ 5. NLP & LLM Orchestration    │ Hugging Face Transformers, Sentence-Transformers,│
│                               │ spaCy, LangChain, NLTK, AWQ Quantization, LoRA.  │
│ 6. Audio & Vision Processing  │ MediaPipe (Google), openSMILE (Audeering),       │
│                               │ OpenAI Whisper, OpenCV, PyMuPDF, LayoutLMv3.     │
│ 7. Databases & Vector Stores  │ Neo4j, ChromaDB, FAISS, PostgreSQL, MongoDB,     │
│                               │ TimescaleDB, Redis In-Memory Cache, MySQL.       │
│ 8. DevOps & Sandboxing        │ Docker, WebRTC, ONNX Runtime, Linux cgroups.     │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master Technology Audit Matrix Across Studies

The matrix below maps every key software component to its primary paper implementations, documenting its functional role and empirical performance in the literature:

| Technology Component | Category | Documented Paper Implementations | Primary Functional Role in Corpus | Literature-Supported Advantage / Benchmark |
|:---|:---|:---|:---|:---|
| **Python** | Language | P01–P10, P12, P14–P25, P28, P29, P31–P37, P39, P41–P44| Core ML, NLP, and backend engineering | Universal compatibility with PyTorch/HuggingFace |
| **TypeScript / JS**| Language | P04, P13, P28, P30, P38, P41 | Frontend UI & Node.js web services | Full-stack asynchronous responsiveness |
| **C++ / WebAssembly**| Runtime | P03, P14, P29 | Real-time audio prosody & client vision | Sub-15ms openSMILE prosody extraction (P29) |
| **FastAPI** | Backend | P13, P17, P21, P28, P29, P41, P42, P44 | High-concurrency asynchronous REST & WebSockets| Native async event loop, ASGI, OpenAPI docs |
| **Express / Node.js**| Backend | P30, P38 | Monolithic MERN stack backend APIs | Fast prototyping for JavaScript developers |
| **Flask** | Backend | P04, P37, P43 | Lightweight microservice REST wrappers | Minimalist routing; slower concurrency than FastAPI|
| **React.js / Next.js**| Frontend | P04, P13, P28, P30, P38, P41 | Interactive dashboards and candidate portals | Component reusability, virtual DOM, SSR speed |
| **Streamlit** | Frontend | P21, P36 | Rapid prototyping of AI/ML demo dashboards | Rapid deployment; limited multi-user concurrency |
| **PyTorch** | ML Core | P08, P10, P12, P17, P21, P28, P34, P39, P42, P43, P44| Deep neural networks, transformers, embeddings | Dynamic computation graphs, native Hugging Face |
| **Scikit-Learn** | ML Core | P01, P02, P04, P06, P07, P09, P18, P19, P22, P24, P31, P33| Classical ML, baseline classifiers, metrics | Robust cross-validation, preprocessing tools |
| **XGBoost** | Ensemble | P01, P02, P04, P06, P09, P18, P19 | Gradient boosting classification & regression | 91.2% accuracy in P02, robust handling of tabular|
| **CatBoost** | Ensemble | P01, P22 | Categorical gradient boosted decision trees | 93.6% accuracy in P22 without one-hot explosion |
| **LightGBM** | Ensemble | P05, P22 | Fast histogram-based gradient boosting | 6.8x faster training on 12k records in P05 |
| **Sentence-Transformers**| NLP | P12, P17, P38, P43 | Dense semantic text embedding generation | MRR@10: 0.92 with all-MiniLM-L6-v2 in P17 |
| **spaCy** | NLP | P04, P11, P12, P17, P36 | Named Entity Recognition (NER) and tokenizing | Fast C-optimized pipeline; 88.4% entity F1 in P12|
| **openSMILE** | Audio | P03, P29 | Acoustic prosody extraction (pitch, jitter) | Real-time C++ audio stream processing (P29) |
| **MediaPipe** | Vision | P03, P14, P15 | 3D facial landmarks, head pose, eye gaze | 60 FPS real-time tracking on CPU/WebAssembly |
| **OpenAI Whisper** | Audio | P03, P21, P28, P29 | Automatic Speech Recognition (ASR) | Low Word Error Rate (<4.2%) across accents |
| **LayoutLMv3** | Vision-Doc | P42 | Multimodal document processing for multi-column | 98.2% layout boundary tolerance on resumes (P42)|
| **Neo4j** | Graph DB | P13, P41, P43 | Knowledge graph representation and traversals | Native Cypher queries; 1,150-node twin in P41 |
| **ChromaDB / FAISS**| Vector DB | P20, P21, P23 | Dense vector similarity indexing for RAG | Sub-20ms nearest-neighbor retrieval (P21, P23) |
| **Docker** | DevOps | P28 | Sandboxed execution of untrusted candidate code | Prevents host OS compromise during live coding |
| **WebRTC** | Streaming | P29 | Low-latency audio streaming for conversational AI| Sub-1.2 second interactive interview turn lag |

---

## 3. Technology Stack Selection Critique & Literature Consensus

### 3.1 Backend Concurrency: FastAPI vs Flask / Django
- `[CROSS-PAPER OBSERVATION]` While early educational prototypes (P04, P37) utilized Flask, newer high-throughput and real-time systems (P17, P28, P29, P41, P44) uniformly adopt **FastAPI**.
- `[AGENT INTERPRETATION]` FastAPI’s native asynchronous Python event loop (ASGI via Uvicorn), tight Pydantic type validation, and native WebSocket/WebRTC support make it the undisputed industry standard for orchestrating multi-agent AI pipelines and concurrent student requests.

### 3.2 Vector Database Engine: ChromaDB vs FAISS vs Neo4j
- `[CROSS-PAPER OBSERVATION]` For localized educational RAG (P21), **ChromaDB** is favored because of its zero-configuration local on-disk SQLite/DuckDB persistence. For massive high-dimensional lecture transcript indexing (P23), **FAISS** provides GPU-accelerated inner-product similarity search.
- `[CROSS-PAPER OBSERVATION]` However, neither vector store can enforce hard hierarchical prerequisite constraints. Therefore, the literature converges on pairing **ChromaDB (for unstructured semantic text)** with **Neo4j (for structured curricular prerequisite DAGs)** (P13, P41).

---

## 4. ScholarCamp / PRIE Production Technology Stack

Based on verified empirical performance, stability, and licensing, ScholarCamp / PRIE adopts the following definitive technology stack:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            PRIE DEFINITIVE TECH STACK                            │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ Frontend (Client Layer)  │ Next.js 14 (App Router) + React 18 + TailwindCSS;     │
│                          │ MediaPipe WebAssembly (Client Video Tracking);        │
│                          │ Monaco Editor (Browser Coding Sandbox).               │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ API Gateway & Backend    │ Python 3.11 + FastAPI (ASGI / Uvicorn);               │
│                          │ WebSockets & WebRTC Streaming Gateways (aiortc).      │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Core AI / ML Engines     │ CatBoost & LightGBM (Employability Tabular ML);       │
│                          │ Temporal Fusion Transformer (PyTorch Forecasting);    │
│                          │ LayoutLMv3 + HuggingFace Transformers (ATS Parser);   │
│                          │ Sentence-Transformers (all-MiniLM-L6-v2);             │
│                          │ faster-whisper-v3 + openSMILE (Mock Interview);       │
│                          │ TreeSHAP + DiCE (XAI Diagnostic Engine).              │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Knowledge & Data Stores  │ Neo4j 5 Enterprise Community (Placement Digital Twin);│
│                          │ ChromaDB (Local Private Syllabus RAG);                │
│                          │ PostgreSQL 16 with TimescaleDB extension;             │
│                          │ Redis 7 (Pub/Sub & Caching).                          │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Security & Sandbox       │ Docker Engine (rootless containerized code sandbox).  │
└──────────────────────────┴───────────────────────────────────────────────────────┘
```
