# Video Processing Methodology: Client-Side WebAssembly MediaPipe, Landmark Kinematics & Privacy

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Video_Processing_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Video Processing Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Zero-Trust Biometric Privacy Architecture (`DD-005`, `DD-011`)

> [!CAUTION]
> **STRICT PRIVACY ENFORCEMENT: ZERO VIDEO TRANSMISSION**  
> Under no circumstances does PRIE record, stream, or store raw video frames from candidate webcams.  
> Video processing is executed entirely within the candidate's browser via WebAssembly-compiled MediaPipe FaceMesh. Only anonymized coordinate landmarks and geometric kinematic summaries are transmitted.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      CLIENT-SIDE BROWSER EXECUTION BOUNDARY                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  [Candidate Webcam Video Stream] (Local MediaStream API)                        │
│                           │                                                     │
│                           ▼                                                     │
│  [MediaPipe FaceMesh Wasm Worker] (Local 30 FPS inference)                      │
│                           │                                                     │
│                           ▼                                                     │
│  [468 Normalized 3D Facial Landmarks] [x_i, y_i, z_i]                          │
│                           │                                                     │
│                           ▼                                                     │
│  [Kinematic Coordinate Derivation]                                              │
│  • Head pose angles: Pitch, Yaw, Roll                                           │
│  • Gaze stability vector: theta_gaze                                            │
│  • Blink rate: Eye Aspect Ratio (EAR)                                           │
├───────────────────────────┼─────────────────────────────────────────────────────┤
│ NETWORK TRANSMISSION ONLY │ Compact JSON Telemetry Packet (No Raw Video)        │
└───────────────────────────┴─────────────────────────────────────────────────────┘
```

---

## 2. Geometric Landmark Kinematics

### 2.1 Eye Aspect Ratio (EAR) for Blink Detection
Eye Aspect Ratio tracks alertness and excessive blinking disfluency:
$$\text{EAR} = \frac{\|p_2 - p_6\|_2 + \|p_3 - p_5\|_2}{2 \|p_1 - p_4\|_2}$$
where $p_1, \dots, p_6$ are standard 2D eye boundary landmark points. A blink event is registered when $\text{EAR} < 0.20$ for 2 to 4 consecutive frames.

### 2.2 Head Pose Orientation (Pitch, Yaw, Roll)
Derived using the Perspective-n-Point (PnP) algorithm mapped to a 3D canonical facial model using nose tip, chin, eye corners, and mouth corners. High variance in yaw indicates candidate distraction from the screen.

### 2.3 Epistemological Guardrail
Visual kinematics are used exclusively to evaluate communicative composure and screen presence. **PRIE strictly prohibits inferring personality traits, honesty, or cognitive intelligence from facial geometry.**
