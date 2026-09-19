# EXP-03 Modality Ablation & Fusion Analysis
- **Audio Alone (Librosa Prosody)**: Mean Score $= 74.3 \pm 7.8$, Variance $= 60.84$
- **Video Alone (OpenCV Gaze & Stability)**: Mean Score $= 77.9 \pm 6.9$, Variance $= 47.61$
- **Speech Alone (Whisper Lexical & WPM)**: Mean Score $= 75.8 \pm 8.9$, Variance $= 79.21$
- **Late Multimodal Fusion (Proposed M05)**: Mean Score $= 76.0 \pm 4.2$, Variance $= 17.64$
- **Empirical Variance Reduction**: **$77.98\% \pm 3.99\%$** over highest unimodal variance ($p = 0.0022$).
- **Conclusion**: Late Multimodal Fusion effectively dampens transient unimodal sensor noise.
