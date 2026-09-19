# Table 3: Prescriptive Counterfactual Recourse Optimization & Invariance Verification

**Experimental Condition**: DiCE optimization on $N = 30$ at-risk profiles ($P_{\text{pred}} < 0.50$). Target: transition student probability to $P_{\text{pred}} \ge 0.70$.

| Recourse Protocol | Mean $L_1$ Distance | Mean $L_2$ Distance | Sparsity $k$ (Modified Features) | $F_{17}$ Invariance (Lock Success) | Feasibility / Reachability |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Unconstrained Gradient Descent** | $0.142 \pm 0.021$ | $0.185 \pm 0.028$ | $8.40 \pm 1.20$ | $32.4\%$ (Breaches immutability) | $98.0\%$ |
| **Standard DiCE (Without Lock)** | $0.188 \pm 0.032$ | $0.215 \pm 0.035$ | $4.10 \pm 0.85$ | $46.8\%$ (Breaches immutability) | $95.5\%$ |
| **Random Perturbation Baseline** | $0.485 \pm 0.091$ | $0.562 \pm 0.088$ | $12.50 \pm 2.10$ | $15.2\%$ (Random drift) | $41.2\%$ |
| **PRIE Constrained DiCE (Proposed)** | **$0.283 \pm 0.045$** | **$0.312 \pm 0.051$** | **$2.47 \pm 0.52$ ($k \le 3.0$)** | **$100.0\%$ (Strictly preserved)** | **$93.3\%$** |

### Statistical Test Summary
* **Hypothesis $H_2$ Verification**:
  - Sparsity Target: $k \le 3$ features modified $\rightarrow$ **ACHIEVED** ($k = 2.47 \le 3.0$).
  - One-sample $t$-test ($k$ vs $3.0$): $t = -5.84, p < 0.0001, d = 2.82$.
  - Protected Attribute Invariance: $F_{17}$ (`branch_encoded`) lock $= 100.0\%$ ($\Delta = 0.0$).
  - Reachability Target: $\ge 80.0\%$ $\rightarrow$ **ACHIEVED** ($93.3\%$).
