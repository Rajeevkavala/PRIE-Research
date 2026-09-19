# Algorithm Methodology: Mathematical Formulations, Objective Functions & Mechanics

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Algorithm_Methodology.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Algorithmic Formulation  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Algorithmic Scope & Grounding

This document establishes the exact mathematical formulations, loss functions, optimization objectives, and algorithmic steps for all models authorized by Phase 04 and Phase 05.

---

## 2. Gradient Boosted Decision Trees (XGBoost)

For static tabular placement prediction on the invariant 22-dimensional SPV tensor $\mathbf{x} \in \mathbb{R}^{22}$:

### 2.1 Regularized Objective Function
At boosting round $t$, XGBoost minimizes the second-order Taylor expansion of the regularized objective:
$$\mathcal{L}^{(t)} pprox \sum_{i=1}^N \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(\mathbf{x}_i) + rac{1}{2} h_i f_t^2(\mathbf{x}_i) ight] + \Omega(f_t)$$
where:
- $g_i = \partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$ is the first-order gradient.
- $h_i = \partial^2_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$ is the second-order Hessian.
- $l(y_i, \hat{y}_i)$ is binary logistic loss:
  $$l(y_i, \hat{y}_i) = -y_i \log(\hat{p}_i) - (1 - y_i) \log(1 - \hat{p}_i), \quad \hat{p}_i = rac{1}{1 + e^{-\hat{y}_i}}$$
- $\Omega(f_t)$ is the leaf complexity penalty:
  $$\Omega(f_t) = \gamma T + rac{1}{2} \lambda \sum_{j=1}^T w_j^2 + lpha \sum_{j=1}^T |w_j|$$

### 2.2 Optimal Leaf Weight & Split Criterion
For leaf $j$ containing instance set $I_j$, the optimal leaf weight $w_j^*$ is:
$$w_j^* = -rac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda}$$
The gain of splitting a leaf into left ($I_L$) and right ($I_R$) partitions is:
$$	ext{Gain} = rac{1}{2} \left[ rac{(\sum_{i \in I_L} g_i)^2}{\sum_{i \in I_L} h_i + \lambda} + rac{(\sum_{i \in I_R} g_i)^2}{\sum_{i \in I_R} h_i + \lambda} - rac{(\sum_{i \in I} g_i)^2}{\sum_{i \in I} h_i + \lambda} ight] - \gamma$$

---

## 3. Temporal Fusion Transformer (TFT)

For longitudinal multi-horizon placement sequence forecasting (`M06`, `EXP-3`):

### 3.1 Variable Selection Network (VSN)
At time step $t$, for candidate input feature vector $\mathbf{x}_t \in \mathbb{R}^D$:
$$\mathbf{v}_t = 	ext{Softmax}\Big( 	ext{GRN}_{v}(\mathbf{x}_t, \mathbf{c}) \Big) \in \mathbb{R}^D$$
$$	ilde{\mathbf{x}}_t = \sum_{j=1}^D v_t^{(j)} 	ext{GRN}_{j}\Big( x_t^{(j)}, \mathbf{c} \Big)$$
where $	ext{GRN}$ is the Gated Residual Network with GLU (Gated Linear Unit) activation and $\mathbf{c}$ is an external static context vector (student branch, baseline academic tier).

### 3.2 Quantile Loss Objective
TFT outputs multi-horizon predictions for quantiles $q \in \{0.1, 0.5, 0.9\}$ across future horizons $	au \in \{1, \dots, H\}$. The network is trained using the composite quantile loss:
$$\mathcal{L}_{	ext{TFT}} = rac{1}{N H} \sum_{i=1}^N \sum_{	au=1}^H \sum_{q \in \mathcal{Q}} 	ext{QL}_q\Big( y_{t+	au}^{(i)}, \hat{y}_{t+	au}^{(i)}(q) \Big)$$
$$	ext{QL}_q(y, \hat{y}) = \max\Big( q(y - \hat{y}), (1 - q)(\hat{y} - y) \Big)$$

---

## 4. Multimodal Spatial Transformer (LayoutLMv3)

For 2D document intelligence on multi-column resumes (`M02`, `EXP-1`):

### 4.1 Input Embedding Fusion
For text word token $w_i$ located at normalized page coordinates $[x_0, y_0, x_1, y_1]$:
$$\mathbf{z}_i = \mathbf{e}_{	ext{text}}(w_i) + \mathbf{e}_{	ext{1D}}(i) + \mathbf{e}_{	ext{2D}}(x_0, y_0, x_1, y_1) + \mathbf{v}_{	ext{patch}}(i)$$
where:
- $\mathbf{e}_{	ext{text}}$ is WordPiece token embedding.
- $\mathbf{e}_{	ext{1D}}$ is standard 1D sequential position embedding.
- $\mathbf{e}_{	ext{2D}}$ projects normalized bounding box coordinates into hidden dimension $d$:
  $$\mathbf{e}_{	ext{2D}} = \mathbf{W}_{x0} x_0 + \mathbf{W}_{y0} y_0 + \mathbf{W}_{x1} x_1 + \mathbf{W}_{y1} y_1 + \mathbf{W}_w (x_1 - x_0) + \mathbf{W}_h (y_1 - y_0)$$
- $\mathbf{v}_{	ext{patch}}$ is linear projection of the aligned visual document image patch.

### 4.2 Spatial Self-Attention
Spatial attention modifies the standard transformer attention matrix by adding a spatial bias matrix $\mathbf{B}_{	ext{spatial}}$ encoding horizontal and vertical distance between word pairs:
$$\mathbf{A}_{i, j} = 	ext{Softmax}\left( rac{\mathbf{q}_i \mathbf{k}_j^T}{\sqrt{d_k}} + \mathbf{B}_{	ext{spatial}}(i, j) ight)$$

---

## 5. Explainable AI Mechanics (TreeSHAP & DiCE)

### 5.1 TreeSHAP Polynomial-Time Feature Attribution
For tree ensemble $f(\mathbf{x})$, TreeSHAP computes exact Shapley values $\phi_i$ by tracking conditional expectations $E[f(\mathbf{x}) | \mathbf{x}_S]$ across leaf nodes in $O(T L D^2)$ time:
$$\phi_i(f, \mathbf{x}) = \sum_{S \subseteq \mathcal{F} \setminus \{i\}} rac{|S|! (|\mathcal{F}| - |S| - 1)!}{|\mathcal{F}|!} \Big( E[f(\mathbf{x}) | \mathbf{x}_{S \cup \{i\}}] - E[f(\mathbf{x}) | \mathbf{x}_S] \Big)$$

### 5.2 DiCE Diverse Counterfactual Optimization
DiCE computes feasible counterfactual profile $\mathbf{c}^*$ for unready student $\mathbf{x}$ by solving the constrained optimization problem:
$$\mathbf{c}^* = rg\min_{\mathbf{c}} 	ext{dist}(\mathbf{x}, \mathbf{c}) + \lambda_1 \Big( f(\mathbf{c}) - y^* \Big)^2 - \lambda_2 	ext{Diversity}(\mathbf{c}_1, \dots, \mathbf{c}_k)$$
$$	ext{subject to: } \mathbf{c}_{	ext{immutable}} = \mathbf{x}_{	ext{immutable}} \quad (	ext{CGPA, Branch, Gender locked})$$
where distance is the normalized $L_1$ student intervention effort:
$$	ext{dist}(\mathbf{x}, \mathbf{c}) = \sum_{i \in 	ext{mutable}} rac{|x_i - c_i|}{	ext{MAD}_i}$$
and $	ext{MAD}_i$ is the Median Absolute Deviation of feature $i$ across the training cohort.
