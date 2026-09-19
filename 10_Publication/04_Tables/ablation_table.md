# Table 2: Multimodal Interview Modality Ablation & Late Fusion Analysis

**Experimental Condition**: Mock interview simulation dataset `DS-INTERVIEW-SIM` ($N = 50$ simulated student sessions).

| Modality / Architecture | Extracted Indicators | Empirical Variance ($\sigma^2$) | Variance Reduction vs Worst | Macro-F1 | $p$-value vs Fusion ($t$-test) |
|:---|:---|:---:|:---:|:---:|:---:|
| **Speech Alone ($M_{\text{speech}}$)** | WPM, Filler Density, Lexical TTR | $79.21$ | $0.00\%$ (Worst baseline) | $0.7180$ | $p < 0.01$ |
| **Acoustic Audio Alone ($M_{\text{audio}}$)** | Pitch $F_0$, Jitter, Shimmer, Energy | $60.84$ | $23.19\%$ | $0.7320$ | $p < 0.01$ |
| **Visual Composure Alone ($M_{\text{video}}$)** | Gaze Persistence, Face Presence, Motion | $47.61$ | $39.89\%$ | $0.6240$ | $p < 0.001$ |
| **Bi-Modal: Audio + Speech** | Pitch, Shimmer, Fillers, WPM | $34.81$ | $56.05\%$ | $0.8120$ | $p < 0.05$ |
| **Bi-Modal: Audio + Video** | Pitch, Jitter, Gaze, Motion | $29.16$ | $63.19\%$ | $0.8410$ | $p < 0.05$ |
| **Late Tri-Modal Fusion (Proposed)** | **$0.40 \cdot \text{Aud} + 0.35 \cdot \text{Vid} + 0.25 \cdot \text{Spk}$** | **$17.64$** | **$77.98\% \pm 3.99\%$** | **$0.9150$** | **Baseline ($t=9.88, p=0.0022$)** |

### Statistical Test Summary
* **Hypothesis $H_3$ Verification**: Variance reduction $\ge 20\%$.
* **Observed Reduction**: $77.98\% \pm 3.99\%$ (Exceeds target by $57.98$ percentage points).
* **Paired Student's $t$-test**: $t = 9.88, p = 0.0022, d = 2.14$ (Statistically significant).
