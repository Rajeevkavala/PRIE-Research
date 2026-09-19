# Technology Stack Architecture: Scientific Requirements vs Engineering Implementations

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Technology_Stack_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Technology Stack Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & Epistemological Taxonomy

A fundamental requirement of the Phase 05 Master Directive (Section 34 & 44) is the strict demarcation between:
1. **RESEARCH REQUIREMENT (Scientific Core)**: A mathematical, algorithmic, or representational requirement dictated by literature findings (`Paper01`–`Paper44`), validated research gaps (`RG1`–`RG8`), or pre-experimental protocols (`EXP-1`–`EXP-6`).
2. **ENGINEERING IMPLEMENTATION CHOICE (Substrate)**: A software framework, runtime container, database, or network protocol selected for latency, cost, developer productivity, or operational stability.

Under no circumstances may engineering convenience masquerade as scientific justification.

---

## 2. Comprehensive Technology Stack Evaluation Matrix

| Subsystem Component | Selected Technology | Evaluated Alternatives | Scientific Rationale (Research Requirement) | Engineering Rationale (Implementation Choice) | Linked Pre-Experiment | Epistemological Classification |
|:---|:---|:---|:---|:---|:---:|:---:|
| **Tabular Placement Predictor** | **XGBoost (GBDT)** | Random Forest, CatBoost, LightGBM, TabNet | Proven dominance on tabular student cohorts ($N < 5,000$) (**P01, P04, P18**); resists overfitting. | Sub-5ms CPU inference via ONNX Runtime; low memory footprint ($<25$MB). | `EXP-3` | `RESEARCH REQUIREMENT` |
| **Longitudinal Sequence Model** | **Temporal Fusion Transformer (TFT)** | LSTM with Attention, GRU, ARIMA | Captures variable multi-horizon dependencies and student learning velocity (**P44**). | Direct quantile loss forecasting ($\text{P}_{10}, \text{P}_{50}, \text{P}_{90}$); temporal self-attention maps. | `EXP-3` | `RESEARCH REQUIREMENT` |
| **Document Intelligence Parser** | **LayoutLMv3** | Tesseract Flat OCR, SpaCy NER, PyPDF2 | Resolves multi-column layout destruction; 2D spatial coordinates ($[x_0, y_0, x_1, y_1]$) (**P17, P42**). | Unified multimodal vision-language transformer; ONNX FP16 acceleration. | `EXP-1` | `RESEARCH REQUIREMENT` |
| **Dense Semantic Embeddings** | **Sentence-BERT (`all-MiniLM-L6-v2`)** | TF-IDF, BM25, OpenAI `text-embedding-3-small` | 20%+ higher semantic recall than sparse keyword matching (**P13, P35, P36**). | Sub-20ms bi-encoder inference; 384d compact vectors pre-indexable in vector store. | `EXP-1` | `RESEARCH REQUIREMENT` |
| **Speech-to-Text Transcription**| **Whisper ASR (Chunked)** | Vosk, Kaldi, Google Cloud Speech API | Robustness against non-native accented Indian English speech (**P29**: $\text{WER} = 6.2\%$). | Lightweight local streaming inference via `whisper.cpp`; sub-250ms chunk turnaround. | `EXP-2` | `RESEARCH REQUIREMENT` |
| **Client Vision Perception** | **MediaPipe FaceMesh** | OpenFace, DeepFace, Server OpenCV | Non-verbal composure tracking (blink rate, gaze stability) (**P15, P30**). | Runs entirely in client browser WebAssembly (30 FPS); **Zero raw video transmitted to server (`DD-011`)**. | `EXP-2` | `RESEARCH REQUIREMENT` |
| **Descriptive Attribution** | **TreeSHAP** | KernelSHAP, LIME, Permutation Importance | Theoretical game-theoretic axioms (Efficiency, Symmetry, Additivity) (**P18, P22, P34**). | Polynomial-time evaluation $O(T L D^2)$; execution time $<15$ms on CPU. | `EXP-4` | `RESEARCH REQUIREMENT` |
| **Prescriptive Recourse** | **DiCE (Counterfactuals)**| Alibi, Heuristic Grids, Unconstrained GD | Resolves the "Descriptive-to-Prescriptive Chasm" (`RG3`); locks immutable features (**P18, P19**). | Loss minimization balancing $L_1$ proximity and $L_0$ sparsity; enforced feasibility. | `EXP-4` | `RESEARCH REQUIREMENT` |
| **Vector Store & Retrieval** | **ChromaDB** | FAISS, Pinecone, Milvus, Weaviate | Native dense vector indexing for two-stage curriculum RAG (`DD-007`). | Embedded in-process / lightweight container; zero recurring cloud API subscription costs. | `EXP-1` | `ENGINEERING CHOICE` |
| **Concept Graph Traversal** | **NetworkX / Graph Lib**| Neo4j, ArangoDB, Gremlin Server | Evaluates topological shortest path ($A^*$) on prerequisite DAG (`DD-008`). | In-memory graph search executes in $<10$ms; avoids heavy graph database daemon overhead. | `EXP-4` | `ENGINEERING CHOICE` |
| **Ephemeral Code Sandbox** | **Docker Engine API** | Judge0 Cloud, Firejail, gVisor, in-process `exec` | Prevents server compromise while validating live unit test pass rates (`DD-006`, **P28**). | Native Linux cgroup isolation; `--net=none`; strict 128MB RAM and 5.0s timeout limits. | `EXP-2` | `ENGINEERING CHOICE` |
| **Relational Database** | **PostgreSQL 16** | MySQL, MariaDB, Oracle | Strict ACID compliance for official student transcripts and historical SPV snapshots. | Robust JSONB support for semi-structured entities; mature connection pooling (PgBouncer). | None | `ENGINEERING CHOICE` |
| **Time-Series Telemetry** | **TimescaleDB Extension** | InfluxDB, Prometheus, MongoDB | Longitudinal clickstream and habit cadence tracking (`M11`, **P02, P44**). | Automatic hyper-table chunking by week; continuous aggregates SQL support. | `EXP-3` | `ENGINEERING CHOICE` |
| **Caching & Message Broker** | **Redis 7.x** | RabbitMQ, Apache Kafka, Memcached | Decoupled asynchronous task offloading and low-latency session caching. | Sub-millisecond latency; dual role as task queue broker and distributed memory cache. | None | `ENGINEERING CHOICE` |
| **API Framework & Gateway** | **FastAPI (Python 3.10)** | Django, Flask, Express.js, Spring Boot | Asynchronous event loop native support; OpenAPI 3.1 automatic schema generation. | High-performance ASGI runtime (Uvicorn); native Pydantic data validation contracts. | None | `ENGINEERING CHOICE` |
| **Differential Privacy** | **Custom Python DP Proxy** | Diffprivlib, OpenDP | Enforces Laplace mechanism ($\epsilon \le 1.0$) on recruiter cohort analytics (`DD-011`). | Transparent middleware proxy intercepting aggregate queries before response serialization. | `EXP-6` | `RESEARCH REQUIREMENT` |

---

## 3. Technology Governance & Licensing Verification

All selected software libraries, runtimes, and models are compatible with open academic research and institutional deployment:
- **Permissive Open-Source Licenses**: PostgreSQL (PostgreSQL License), Redis (BSD-3), FastAPI (MIT), ChromaDB (Apache 2.0), Docker Community Edition (Apache 2.0).
- **Machine Learning Weights**:
  - `LayoutLMv3`: HuggingFace open research weights (CC-BY-NC-SA / MIT research license).
  - `Sentence-BERT (all-MiniLM-L6-v2)`: Apache 2.0 open commercial/research weights.
  - `Whisper-Small`: MIT License.
  - `Llama-3-8B-Instruct`: Meta Llama 3 Community License (Permitted for educational/research use).
  - `MediaPipe`: Apache 2.0 License.

**Integrity Verification**: Zero proprietary cloud-vendor lock-in APIs (e.g., Azure Document Intelligence, AWS Rekognition, proprietary closed-source LLMs) are required for the primary research baseline, guaranteeing complete experimental reproducibility across academic institutions.
