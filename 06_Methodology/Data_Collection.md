# Data Collection: Multimodal Telemetry Ingestion, Modality Protocols & Quality Controls

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Data_Collection.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Data Collection Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Multimodal Data Ingress Taxonomy

PRIE collects and harmonizes telemetry across eight distinct institutional and behavioral channels. Each channel enforces strict data isolation, format validation, and automated quality gating before feature extraction:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           MULTIMODAL INGRESS TOPOLOGY                           │
├──────┬──────────────────────┬──────────────────────┬────────────────────────────┤
│ Chan │ Channel Description  │ Ingress Format       │ Primary Validation Rule    │
├──────┼──────────────────────┼──────────────────────┼────────────────────────────┤
│ C01  │ Academic Transcripts │ JSON via SIS API     │ CGPA in [0.0, 10.0]        │
│ C02  │ Code Sandboxes       │ Stdout/Stderr JSON   │ Exit code, timeout < 5.0s  │
│ C03  │ Resume Documents     │ PDF / DOCX Stream    │ Size < 10MB, parseable text│
│ C04  │ Technical JDs        │ Plain Text / Markdown│ Token length in [50, 2000] │
│ C05  │ Mock Interview Audio │ 16 kHz Mono PCM WAV  │ SNR >= 12 dB, VAD active   │
│ C06  │ Mock Interview Video │ JSON Landmark Stream │ 30 FPS, 468 FaceMesh points│
│ C07  │ Formative Quizzes    │ Interaction Log JSON │ Score in [0, 100], time > 0│
│ C08  │ Platform Telemetry   │ W3C Event Stream     │ Valid UUID, monotonic time │
└──────┴──────────────────────┴──────────────────────┴────────────────────────────┘
```

---

## 2. Granular Modality Ingestion Protocols

### Channel C01: Academic Data Ingestion (SIS)
- **Source**: University Student Information System (SIS) / ERP database.
- **Protocol**: Nightly automated sync via OAuth2-secured REST API endpoints.
- **Payload**: Cumulative Grade Point Average (`cgpa`), individual core subject marks (DSA, OS, DBMS, Networks), semester registration status.
- **Quality Control**: Schema validation rejects non-numeric grades; out-of-range scores trigger an administrative warning; missing subject records default to an explicit observation mask ($m_i = 0$).

### Channel C02: Live Programming & Coding Assessment Telemetry
- **Source**: Diagnostic Assessment (`M03`) and Mock Interview Sandboxes (`M05`).
- **Protocol**: Student code submissions are encapsulated into stateless JSON execution envelopes and submitted to ephemeral Docker execution workers (`DD-006`).
- **Payload**: Test suite execution matrix (pass/fail count), execution wall-clock time (ms), peak memory consumption (MB), static cyclomatic complexity, code syntax AST.
- **Quality Control**: Sandboxes enforce a hard 5-second wall time; network sockets are disabled (`--network none`); non-zero memory leaks trigger graceful container termination.

### Channel C03: Resume Document Ingestion
- **Source**: Student document upload interface in ScholarCamp.
- **Protocol**: HTTPS multipart/form-data upload.
- **Payload**: Raw PDF or DOCX file stream.
- **Quality Control**: Maximum file size limit enforced (10 MB); file header bytes verified (`%PDF-`); corrupted PDF streams trigger user upload warnings with repair suggestions; documents rendered to 300 DPI images for LayoutLMv3 processing.

### Channel C04: Corporate Job Description (JD) Ingestion
- **Source**: Campus placement cell administrative portal or corporate recruiter ingestion pipeline.
- **Protocol**: Direct text ingress, automated web scraper on corporate partner portals, or plain-text markdown ingestion.
- **Payload**: Cleaned job title, role category, mandatory technical skills, preferred qualifications, experience requirements.
- **Quality Control**: Role complexity scoring engine normalizes requirements against the standardized O*NET / ESCO job taxonomy.

### Channel C05: Mock Interview Audio Stream Ingestion
- **Source**: Interactive browser mock interview interface (`M05`).
- **Protocol**: WebRTC audio track streaming into an Audio Worklet processor.
- **Payload**: 16 kHz, 16-bit mono PCM audio chunks streamed in 200ms increments.
- **Quality Control**: Client-side Silero Voice Activity Detector (VAD) drops silent frames; Signal-to-Noise Ratio (SNR) calculated; clipping thresholds flag audio distortion.
- **Privacy Rule**: **Raw audio waveforms are discarded immediately after Whisper transcription. Zero persistent raw voice recordings are retained (`DD-011`).**

### Channel C06: Mock Interview Vision Landmark Ingestion
- **Source**: Client browser video stream.
- **Protocol**: Browser-side execution via WebAssembly (Wasm) compiled MediaPipe FaceMesh (`DD-005`).
- **Payload**: Compact JSON telemetry packets transmitting 468 normalized 3D facial coordinate landmarks $[x, y, z]$ at 30 FPS.
- **Quality Control**: Face detection confidence threshold $\ge 0.85$; head pose angles computed (pitch, yaw, roll); missing frame intervals logged.
- **Privacy Rule**: **Video frames never leave the client browser. No raw video is transmitted across the network or stored on servers (`DD-005`, `DD-011`).**

### Channel C07: Formative Assessment & Quizzing Telemetry
- **Source**: Adaptive Quizzing Engine (`M03`) and Causal AQG (`M10`).
- **Protocol**: Real-time event dispatch upon question submission.
- **Payload**: Question UUID, student response option, correct option, response latency (seconds), hint requests count.
- **Quality Control**: Submissions completed under 2.0 seconds trigger bot/guess flags; session state verified via HMAC signatures.

### Channel C08: Learning Activity & Interaction Clickstreams
- **Source**: ScholarCamp Learning Management System.
- **Protocol**: Asynchronous event batching via high-throughput Kafka / Redis pub-sub queues.
- **Payload**: Timestamp, session UUID, event category (`login`, `resource_view`, `video_play`, `roadmap_milestone_check`).
- **Quality Control**: Monotonically increasing timestamps verified; duplicated event IDs pruned via Redis bloom filters.
