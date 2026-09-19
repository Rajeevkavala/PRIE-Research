# Preprocessing Methodology: Multimodal Transformation, Imputation & Outlier Governance

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Preprocessing.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Preprocessing Protocol  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Multimodal Preprocessing Architecture

Multimodal data in PRIE originates from heterogeneous structures: tabular databases, raw PDF text streams, bounding boxes, audio waveforms, video landmarks, and high-frequency clickstreams. Preprocessing applies standardized, mathematically sound transformations while enforcing strict test-set isolation:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       MULTIMODAL PREPROCESSING PIPELINE                         │
├───────────────────┬──────────────────────────────────┬──────────────────────────┤
│ Modality          │ Preprocessing Operations         │ Output Representation    │
├───────────────────┼──────────────────────────────────┼──────────────────────────┤
│ Academic Tabular  │ MICE Imputation → Tukey Clipping │ Normalized float         │
│                   │ → RobustScaler → MinMax [0, 1]   │ in domain [0.0, 1.0]     │
├───────────────────┼──────────────────────────────────┼──────────────────────────┤
│ Resume Text & PDF │ Tesseract OCR → LayoutLMv3 Token │ 512-token sequence with  │
│                   │ Bounding Box Scaling [0, 1000]   │ 2D coordinates [x0,y0..] │
├───────────────────┼──────────────────────────────────┼──────────────────────────┤
│ Audio Streams     │ 16kHz Mono Resampling → Silero   │ 80-channel Log-Mel       │
│                   │ VAD Speech Chunking (200ms)      │ Spectrograms + Text      │
├───────────────────┼──────────────────────────────────┼──────────────────────────┤
│ Video Landmarks   │ Wasm MediaPipe 468 3D landmarks  │ Kinematic eye/head pose  │
│                   │ → Temporal moving median filter  │ displacement vectors     │
├───────────────────┼──────────────────────────────────┼──────────────────────────┤
│ Clickstream Logs  │ Event deduplication → Session    │ Weekly engagement rollups│
│                   │ Windowing → Shannon Entropy      │ & consistency scores     │
└───────────────────┴──────────────────────────────────┴──────────────────────────┘
```

---

## 2. Tabular Data Preprocessing Procedures

### 2.1 Outlier Detection & Tukey Clipping
Extreme feature entries (e.g., erroneous test attempt entries or abnormal logging spikes) are detected using Tukey's Interquartile Range (IQR) fence:
$$	ext{IQR} = Q_3 - Q_1$$
$$	ext{Lower Bound} = \max\Big( 	ext{Domain Min}, Q_1 - 1.5 	imes 	ext{IQR} \Big)$$
$$	ext{Upper Bound} = \min\Big( 	ext{Domain Max}, Q_3 + 1.5 	imes 	ext{IQR} \Big)$$
Values falling outside bounds are clipped (winsorized) to the boundary thresholds rather than dropped, preserving statistical sample size.

### 2.2 Missing Value Imputation via MICE
Missing entries are imputed via Multivariate Imputation by Chained Equations (MICE) using Bayesian Ridge regression estimators:
1. For each feature with missingness $f_j$, a linear regression model is trained on observed data using all other features $f_{-j}$ as predictors:
   $$f_j = \mathbf{w}^T f_{-j} + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2)$$
2. Missing entries are imputed by sampling from the predictive posterior distribution.
3. The procedure iterates across features until convergence (10 cycles).
4. **Leakage Protection**: Imputation regression parameters are fitted exclusively on the Training fold and stored. Validation and test instances are imputed by applying the pre-fitted estimators.

### 2.3 Feature Scaling & Normalization
To handle skewed academic score distributions without distortion:
1. **RobustScaler**: Centers features by subtracting the median and divides by the interquartile range:
   $$x_{	ext{robust}} = rac{x - 	ext{median}(x)}{Q_3(x) - Q_1(x)}$$
2. **Min-Max Scaling**: Binds the final feature to the canonical interval $[0.0, 1.0]$:
   $$	ilde{x} = rac{x_{	ext{robust}} - \min(x_{	ext{robust}})}{\max(x_{	ext{robust}}) - \min(x_{	ext{robust}})}$$

---

## 3. Unstructured Modality Preprocessing

### 3.1 Document & Resume Layout Preprocessing
1. **PDF Rendering**: PDF pages are converted into 300 DPI RGB bitmap images using `pdf2image`.
2. **Bounding Box Extraction**: Tesseract OCR extracts bounding box coordinates $[x_{	ext{min}}, y_{	ext{min}}, x_{	ext{max}}, y_{	ext{max}}]$ for every recognized word token.
3. **Coordinate Normalization**: Coordinates are rescaled to the standard $[0, 1000]$ integer grid required by LayoutLMv3:
   $$x_{	ext{norm}} = 	ext{round}\left( rac{x}{W_{	ext{page}}} 	imes 1000 ight), \quad y_{	ext{norm}} = 	ext{round}\left( rac{y}{H_{	ext{page}}} 	imes 1000 ight)$$
4. **Token Truncation & Chunking**: Documents exceeding 512 tokens are segmented using a sliding window with a 64-token overlap.

### 3.2 Conversational Audio Preprocessing
1. **Sample Rate Standardization**: Audio streams are downmixed to single-channel (mono) and resampled to 16,000 Hz using Polyphase filtering.
2. **Voice Activity Detection (VAD)**: Silero VAD filters out acoustic silence, fan hum, and room reverb, preserving only voiced frames with speech probability $P(	ext{speech}) > 0.5$.
3. **Acoustic Feature Extraction**: 80-channel log-mel filterbank energies are computed with a 25ms window length and 10ms hop length for Whisper acoustic encoder consumption.

### 3.3 Video Landmark Preprocessing
1. **Browser-Side Wasm Extraction**: MediaPipe FaceMesh runs locally at 30 FPS, emitting 468 landmark coordinates $[x_i, y_i, z_i]$.
2. **Temporal Smoothing**: A 5-frame moving median filter attenuates high-frequency webcam sensor jitter.
3. **Head Pose & Eye Gaze Kinematics**: Roll, pitch, and yaw angles are derived from facial plane normal vectors; horizontal and vertical gaze vectors are calculated relative to eye-corner landmarks.
