# Interview Methodology: Conversational Turn Cadence, Paralinguistic Telemetry & Sandbox Execution

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Interview_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Mock Interview Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Resolving the Latency Bottleneck in AI Mock Interviews (`RG5`)

Prior automated mock interview systems suffer from debilitating conversational turnaround latency ($>2.8$ to $4.2$ seconds) caused by sequential round-trip cloud API calls (`Paper03`, `Paper14`, `Paper15`, `Paper28`). This breaks conversational immersion, induces student stress, and destroys interview validity.

PRIE achieves a **sub-1.5s voice-to-voice latency budget** (`DD-005`, `EXP-2`) by restructuring the interview engine into a localized, streaming micro-pipeline:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    SUB-1.5s VOICE-TO-VOICE LATENCY BUDGET                       │
├────────────────────────────┬──────────────┬─────────────────────────────────────┤
│ Pipeline Stage             │ Budget (ms)  │ Technical Optimization              │
├────────────────────────────┼──────────────┼─────────────────────────────────────┤
│ Speech Activity End Detect │  150 ms      │ Client-side Silero VAD trailing edge│
│ Audio Chunk Ingress & STT  │  350 ms      │ Local Chunked Whisper (TensorRT-LLM)│
│ LLM First Token Generation │  450 ms      │ Quantized Llama-3-8B via vLLM       │
│ TTS First Chunk Synthesis  │  250 ms      │ FastTTS streaming audio synthesis   │
│ WebRTC Audio Buffer Ingress│  150 ms      │ Jitter buffer pre-buffering         │
├────────────────────────────┼──────────────┼─────────────────────────────────────┤
│ TOTAL TURNAROUND LATENCY   │ 1,350 ms     │ SUB-1.5 SECONDS (TARGET SATISFIED)  │
└────────────────────────────┴──────────────┴─────────────────────────────────────┘
```

---

## 2. Multimodal Interview Feature Extraction

Telemetry captured during technical mock interview sessions is strictly decomposed across five orthogonal feature dimensions:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       ORTHOGONAL INTERVIEW TELEMETRY                            │
├───────────────────┬─────────────────────────────────────────────────────────────┤
│ Modality          │ Extracted Paralinguistic / Behavioral Features              │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Acoustic / Speech │ Fundamental frequency (F0) pitch contour, jitter, shimmer,  │
│                   │ speech rate (syllables/sec), pause duration distribution    │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Linguistic        │ Technical vocabulary density, filler word ratio ("um","ah"),│
│                   │ STAR framework adherence, semantic question relevance       │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Visual / Kinematic│ Gaze fixation stability (% on-screen), head orientation     │
│                   │ entropy (pitch/yaw variance), facial action units (blink)   │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Technical Code    │ Live unit test pass rate, memory efficiency, cyclomatic     │
│                   │ complexity, algorithm time complexity Big-O                 │
├───────────────────┼─────────────────────────────────────────────────────────────┤
│ Temporal Flow     │ Turn-taking response latency, interruption frequency        │
└───────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 3. Isolated Ephemeral Docker Sandboxing (`DD-006`)

During technical coding rounds, student programming submissions are executed inside ephemeral micro-containers:
- **Rootless Execution**: Micro-containers run as non-root unprivileged users (`UID 10001`).
- **Resource Constraints**: Strict limits enforced via Linux cgroups: `--cpus 1.0`, `--memory 256m`, `--pids-limit 64`.
- **Network Isolation**: Complete network disconnection (`--network none`).
- **Execution Timeout**: Hard 5.0-second SIGKILL timeout preventing infinite loops.
