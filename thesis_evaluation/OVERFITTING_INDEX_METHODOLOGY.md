# Overfitting Index (OI) Formal Methodology & Dual-Track Formulation

**Author:** Emil Brezovsky  
**Master's Thesis:** *High-Resolution UAV Detection, Geolocation, and Knowledge Distillation of Invasive Ailanthus altissima Canopies*  
**Scope:** Formal mathematical foundation, object detection adaptations, and empirical validation of the Overfitting Index (OI).

---

## 1. Theoretical Foundations: Vapnik Statistical Learning Theory

Under Vapnik's classical Statistical Learning Theory [Vapnik 1998, pp. 17–28], supervised learning algorithm optimization corresponds to empirical risk minimization (R_emp) over a finite observed training sample S = {(x_i, y_i)}:
R_{\text{emp}}(\mathbf{w}) = \frac{1}{M} \sum_{i=1}^M \mathcal{L}(f(x_i; \mathbf{w}), y_i)

The true operational risk on unseen samples from the broader distribution P(x, y) is the expected risk, empirically approximated via an independent validation partition:
R_{\text{val}}(\mathbf{w}) = \frac{1}{M_{\text{val}}} \sum_{j=1}^{M_{\text{val}}} \mathcal{L}(f(x_j; \mathbf{w}), y_j)

### 1.1. Definition of Overfitting & The Generalization Gap
A model begins to overfit when empirical risk continues to decrease (R_emp -> 0) while true risk stagnates or diverges (R_val > R_emp) [Zhang et al., 2016]. The per-epoch generalization gap is defined as:
d_{\text{Loss}}(e) = \max\left(0, \, \mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)\right)

* **Rectification Operator max(0, *):** Strong stochastic augmentations (Mosaic-4, MixUp, random affine transforms) frequently elevate training loss above validation loss during early and intermediate epochs (R_val < R_emp). The rectification operator ensures transient negative gaps do not cancel out real divergence [Aburas et al., 2023].

---

## 2. The Aburas et al. (2023) Overfitting Index

In image classification, Aburas et al. (2023) unified loss divergence and accuracy decay into a single scalar Overfitting Index:
\text{OI}_{\text{classical}} = \sum_{e=1}^N e \cdot \mathbb{I}_{(\mathcal{L}_{\text{val}} > \mathcal{L}_{\text{train}})} \left[ (\mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)) + \max\left(0, \, \text{Acc}_{\text{train}}(e) - \text{Acc}_{\text{val}}(e)\right) \right]

* **Linear Epoch Weighting (e *):** Early epochs exhibit stochastic gradient jitter that does not signify structural memorization. Linear weighting heavily penalizes persistent late-stage divergence over early warmup noise.

---

## 3. The Object Detection Dilemma: Why Training mAP Is Unlogged

In image classification, evaluating training accuracy requires trivial logit argmax operations during the training forward pass. In deep learning object detection (YOLOv12, D-FINE, RT-DETR), computing detection accuracy (mAP) requires:
1. Decoding tens of thousands of candidate anchor boxes per image.
2. Running iterative Non-Maximum Suppression (NMS) or bipartite Hungarian matching.
3. Calculating IoU overlap matrices across 10 evaluation thresholds (IoU in [0.50, 0.95]).

Running full mAP evaluation on the training split at every epoch increases training time by 3x to 5x. Consequently, standard detection frameworks (Ultralytics YOLO, Lightly-Train, MMDetection, RT-DETR) only evaluate mAP on the validation split (metrics/mAP50(B)). Hence, training mAP does not exist in raw epoch histories.

---

## 4. The Dual-Track Methodology

To provide complete scientific rigor for the Master's thesis, we establish a **Dual-Track Evaluation Architecture**:

`
                              +----------------------------------------+
                              |     Training Logs (Epoch e = 1..N)     |
                              +-------------------+--------------------+
                                                  |
                       +--------------------------+--------------------------+
                       v                                                     v
        +-----------------------------+                       +-----------------------------+
        |   Track A: Pure Vapnik OI   |                       |  Track B: Compound Aburas OI|
        |  (Loss Generalization Gap)  |                       |  (Loss Gap + Cls Acc Proxy) |
        +--------------+--------------+                       +--------------+--------------+
                       |                                                     |
                       v                                                     v
        OI_Vapnik = sum(e * max(0, dL))                       OI_Compound = sum(e * [dL + dAcc])
`

### Track A: Pure Vapnik Generalization Index (Loss-Based)
Grounded directly in Vapnik's Empirical Risk formulation without requiring proxy assumptions:
\text{OI}_{\text{Vapnik}} = \sum_{e=1}^N e \cdot \max\left(0, \, \mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)\right)

### Track B: Compound Overfitting Index with Classification Accuracy Proxy
Whenever validation loss exceeds training loss (L_val(e) > L_train(e)), we incorporate the classification accuracy divergence:
d_{\text{Compound}}(e) = \begin{cases} (\mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)) + \max\left(0, \, \text{Acc}_{\text{train}}^{\text{proxy}}(e) - \text{Acc}_{\text{val}}^{\text{proxy}}(e)\right), & \text{if } \mathcal{L}_{\text{val}}(e) > \mathcal{L}_{\text{train}}(e) \\ 0, & \text{otherwise} \end{cases}
\text{OI}_{\text{Compound}} = \sum_{e=1}^N e \cdot d_{\text{Compound}}(e)

---

## 5. Mathematical Derivation of the Classification Accuracy Proxy

Both YOLO and DINO/DETR architectures log the dedicated classification loss component at every epoch:
* **YOLOv12 Head:** Binary Cross-Entropy (BCE) loss: L_BCE(p, y) = - [y * log(p) + (1-y) * log(1-p)].
* **DINOv3 / D-FINE Head:** Varifocal Loss (VFL): L_VFL(p, q) = - q * [q * log(p) + (1-q) * log(1-p)].

For foreground canopy proposals (y = 1), the mean classification loss over positive targets is:
\overline{\mathcal{L}}_{\text{cls}} = - \frac{1}{K} \sum_{k=1}^K \log(p_k) = - \log\left( \prod_{k=1}^K p_k^{1/K} \right) = - \log(\tilde{p}_{\text{geom}})
where p_geom is the geometric mean confidence assigned to true targets.

Inverting this fundamental relation yields the exact geometric confidence on the positive class:
\tilde{p}_{\text{geom}} = \exp\left( - \overline{\mathcal{L}}_{\text{cls}} \right) \in (0, 1]

Under likelihood theory, exp(-L_cls) behaves as a bounded, monotonic proxy for classification correctness:
* L_cls -> 0 ==> Acc_proxy -> 1.0 (100% confidence).
* L_cls -> infinity ==> Acc_proxy -> 0.0 (complete misclassification).

We formally define:
\text{Acc}_{\text{proxy}}(e) = \exp\left(-\mathcal{L}_{\text{cls}}(e)\right)

---

## 6. Empirical Benchmark Results Across Cohort

Evaluated across independent initialization seeds (n = 3: 42, 100, 999) across each model's complete training horizon:

| Model Architecture | Epochs (N) | Track A: Vapnik OI | Track B: Compound OI | Accuracy Delta Impact (+dAcc) | Reduction vs. Native Baseline |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **YOLO12s (Native)** | 154-166 | **17,041.20 +/- 2,017.12** | **18,549.38 +/- 2,211.74** | +1,508.18 | *Baseline (100%)* |
| **YOLO12s (SAT-493M)** | 77-86 | **1,926.12 +/- 446.22** | **2,087.98 +/- 481.45** | +161.86 | **-88.7%** |
| **YOLO12s (LVD-1689M)** | 71-90 | **1,737.61 +/- 1,207.41** | **1,879.91 +/- 1,314.85** | +142.30 | **-89.9%** |
| **YOLO12s Triple DINOv3** | 300 | **965.25 +/- 252.11** | **977.58 +/- 266.03** | +12.33 | **-94.7%** |
| **DINOv3 ViT-T (Stock)** | 100 | **0.00 +/- 0.00** | **0.00 +/- 0.00** | +0.00 | *Zero Gap* |
| **ViT-T (LVD-1689M)** | 100 | **0.00 +/- 0.00** | **0.00 +/- 0.00** | +0.00 | *Zero Gap* |
| **ViT-T (SAT-493M)** | 100 | **615.30 +/- 548.42** | **960.80 +/- 847.90** | +345.50 | *Late Divergence* |

---

## 7. Conclusions & Findings

1. **Perfect Correlation Between Tracks:** Both Track A (Pure Vapnik) and Track B (Compound Aburas) reach identical architectural conclusions:
   * Knowledge distillation compresses YOLO12s cumulative overfitting by **-88.7% to -89.9%**.
   * Multi-scale frozen foundation integration (YOLO12s Triple DINOv3) compresses cumulative overfitting by **-94.3% to -94.7%**, adding only +12.3 accuracy delta units across 300 epochs.
2. **Scientific Integrity:** By presenting both formulations in parallel, the thesis demonstrates complete transparency regarding the NMS logging constraints of modern object detectors while providing a mathematically rigorous proxy validated under likelihood theory.
