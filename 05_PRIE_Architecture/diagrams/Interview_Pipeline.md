# PRIE Architecture: Mock Interview Pipeline

## 1. Overview and Purpose
This document presents the detailed architectural pipeline diagram for the **PRIE Interactive Mock Interview & Behavioral Intelligence Engine (M05)**.

The interview system implements a privacy-first, low-latency conversational architecture specified in [`Mock_Interview_Architecture.md`](file:///d:/4-1%20AD/All%20College%20Docs%20and%20ppts/Documentations/PDR/PRIE-Research/05_PRIE_Architecture/Mock_Interview_Architecture.md). It achieves a sub-1.5s total conversational response loop (`DD-005`) through streaming audio processing, zero-server-video client-side WebAssembly computer vision (`DD-011`), and an isolated gVisor container sandbox for technical code execution. The pipeline directly computes and updates four invariant SPV features: `F14: mock_interview_score`, `F15: speech_rate_wpm`, `F16: pause_filler_ratio`, and `F17: visual_confidence_index`.

---

## 2. Mermaid Mock Interview Pipeline Diagram

```mermaid
flowchart TD
    %% Styling
    classDef clientEnv fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,color:#01579b;
    classDef audioEngine fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#e65100;
    classDef visionEngine fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    classDef dialogueEngine fill:#ede7f6,stroke:#7b1fa2,stroke-width:2px,color:#4a148c;
    classDef codeSandbox fill:#fbe9e7,stroke:#d84315,stroke-width:2px,color:#bf360c;
    classDef spvSink fill:#fce4ec,stroke:#c2185b,stroke-width:3px,color:#880e4f;

    %% Client Ingress Environment
    subgraph CLIENT_BROWSER ["Client Browser Sandbox (WebAssembly & WebAudio)"]
        MIC_CAPTURE["WebAudio API<br/>(Opus 16kHz Stream)"]:::clientEnv
        CAM_CAPTURE["HTML5 Video Stream<br/>(Local Canvas Camera Feed)"]:::clientEnv
        WASM_VISION["MediaPipe WebAssembly Engine<br/>- FaceMesh 468 Landmarks<br/>- Iris & Gaze Tracking<br/>- Head Pose (Pitch, Yaw, Roll)"]:::clientEnv
        CODE_EDITOR["Monaco Code Editor<br/>(Live Algorithmic Coding)"]:::clientEnv
        AUDIO_PLAYER["WebAudio AudioBuffer Source<br/>(Streaming AI Speech Playback)"]:::clientEnv
    end

    %% Network Transport Layer
    subgraph NETWORK_GW ["Duplex WebSocket Ingress (TLS 1.3)"]
        WSS_SOCKET["Duplex WebSocket Session Gateway<br/>(Binary Audio Chunks, Landmark JSON, Control Signals)"]:::network
    end

    %% Conversational Audio & Linguistic Track (Sub-1.5s SLA)
    subgraph AUDIO_PIPELINE ["Streaming Audio & Dialogue Pipeline (Backend Core)"]
        VAD_STAGE["Silero VAD Engine<br/>(Speech Boundary Detection ~150ms)"]:::audioEngine
        WHISPER_STAGE["Streaming Chunk Whisper STT<br/>(Incremental Verbatim Transcripts ~250ms)"]:::audioEngine
        LINGUISTIC_EVAL["Linguistic & Fluency Analyzer<br/>- Words Per Minute (WPM)<br/>- Filler Word Ratio ('um', 'ah', 'like')<br/>- Semantic Relevance to Question"]:::audioEngine
        VLLM_ENGINE["Local vLLM Engine (Qwen2.5-7B-Instruct)<br/>(Contextual Interviewer Persona ~320ms TTFT)"]:::dialogueEngine
        TTS_ENGINE["FastTTS Neural Synthesizer<br/>(Streaming PCM Chunks ~280ms)"]:::audioEngine
    end

    %% Visual Demeanor Track (Privacy-Preserving Edge Compute)
    subgraph VISION_PIPELINE ["Kinematic Demeanor Analysis (Zero Raw Video)"]
        GAZE_ANALYZER["Gaze & Eye-Contact Detector<br/>(Percentage On-Screen Focus)"]:::visionEngine
        BLINK_ANALYZER["Blink Rate & Stress Estimator<br/>(Blinks/min vs Baseline)"]:::visionEngine
        HEAD_ANALYZER["Head Stability & Nodding Classifier<br/>(Nodding Affirmation vs Restlessness)"]:::visionEngine
        VIS_SYNTHESIS["Visual Confidence Index Synthesizer<br/>$$F17 = w_g C_{\text{gaze}} + w_b C_{\text{blink}} + w_h C_{\text{pose}}$$"]:::visionEngine
    end

    %% Technical Coding Sandbox Track
    subgraph SANDBOX_TRACK ["Isolated Code Execution Sandbox"]
        GVISOR_CONTAINER["gVisor PTRACE Sandboxed Daemon<br/>- No Host Root Privilege<br/>- Network Disabled<br/>- CPU Cgroups: 1 Core, 512MB RAM<br/>- Timeout: 3.0s Hard Limit"]:::codeSandbox
        VERDICT_EVAL["Automated Testcase Runner<br/>(Syntax, Memory, Edge Cases, Big-O Complexity)"]:::codeSandbox
    end

    %% Final Synthesis and SPV Ingress
    subgraph SYNTHESIS_SPV ["Synthesis & SPV Feature Sink (M01)"]
        INTERVIEW_SCORER["Overall Mock Performance Synthesizer<br/>(Technical Accuracy + Fluency + Demeanor)"]:::spvSink
        SPV_TARGET["<b>Updated SPV Features:</b><br/>- F14: mock_interview_score [0.0, 100.0]<br/>- F15: speech_rate_wpm [50.0, 250.0]<br/>- F16: pause_filler_ratio [0.0, 0.5]<br/>- F17: visual_confidence_index [0.0, 1.0]"]:::spvSink
    end

    %% Connections: Client to Network
    MIC_CAPTURE -->|"Opus Audio Chunks (200ms)"| WSS_SOCKET
    CAM_CAPTURE --> WASM_VISION
    WASM_VISION -->|"Kinematic Vectors Only (30 Hz)"| WSS_SOCKET
    CODE_EDITOR -->|"POST: Code Submission"| WSS_SOCKET

    %% Connections: Audio Track
    WSS_SOCKET --> VAD_STAGE
    VAD_STAGE -->|"Speech Detected"| WHISPER_STAGE
    WHISPER_STAGE --> LINGUISTIC_EVAL
    WHISPER_STAGE --> VLLM_ENGINE
    VLLM_ENGINE --> TTS_ENGINE
    TTS_ENGINE -->|"Streaming Audio Response (<1.5s Total)"| WSS_SOCKET
    WSS_SOCKET --> AUDIO_PLAYER

    %% Connections: Vision Track
    WSS_SOCKET --> GAZE_ANALYZER
    WSS_SOCKET --> BLINK_ANALYZER
    WSS_SOCKET --> HEAD_ANALYZER
    GAZE_ANALYZER --> VIS_SYNTHESIS
    BLINK_ANALYZER --> VIS_SYNTHESIS
    HEAD_ANALYZER --> VIS_SYNTHESIS

    %% Connections: Code Track
    WSS_SOCKET --> GVISOR_CONTAINER
    GVISOR_CONTAINER --> VERDICT_EVAL

    %% Connections: Scoring & SPV
    LINGUISTIC_EVAL --> INTERVIEW_SCORER
    VIS_SYNTHESIS --> INTERVIEW_SCORER
    VERDICT_EVAL --> INTERVIEW_SCORER
    VLLM_ENGINE --> INTERVIEW_SCORER

    INTERVIEW_SCORER --> SPV_TARGET
```

---

## 3. Conversational Latency Breakdown and Privacy Boundaries

### A. Sub-1.5s Voice Loop Latency Audit (DD-005)

$$\text{Latency}_{\text{total}} = T_{\text{VAD}} + T_{\text{Whisper}} + T_{\text{vLLM (TTFT)}} + T_{\text{FastTTS}} + T_{\text{Transport}} \approx 1,120\text{ ms} < 1,500\text{ ms}$$

| Component | Responsible Subsystem | Latency Allocation | Operational Mode |
| :--- | :--- | :--- | :--- |
| **VAD Trailing Silence** | Silero VAD | $150\text{ ms}$ | Buffers 200ms audio chunks |
| **Speech-to-Text** | Whisper Small.en (CTranslate2) | $250\text{ ms}$ | Chunk-based streaming beam search |
| **LLM Reasoning (TTFT)** | Qwen2.5-7B-Instruct (vLLM) | $320\text{ ms}$ | PagedAttention, KV-cache warmed |
| **Audio Synthesis** | FastTTS Neural Engine | $280\text{ ms}$ | First chunk emitted at 50 tokens |
| **Network & Playback** | WebSocket / AudioContext | $120\text{ ms}$ | Opus codec, jitter buffer 50ms |

### B. Client-Side Vision Privacy Isolation (DD-011)
- **Zero Video Transmission**: Webcam pixel frames never leave the client browser execution context.
- **Landmark Coordinates Only**: The client transmits only dimensionless floating-point kinematic vectors ($\approx 4\text{ KB/s}$).
- **GDPR / FERPA Compliance**: Eliminates biometric facial image storage risks entirely.
