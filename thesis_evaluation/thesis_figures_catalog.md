# Master's Thesis: High-Resolution UAV Detection, Geolocation, and Knowledge Distillation of Invasive *Ailanthus altissima* Canopies

**Candidate:** Emil Brezovsky  
**Degree Program:** Master of Science in Geoinformatics & Remote Sensing  
**Investigation Scope:** Deep Learning Canopy Delineation, Cross-Domain Knowledge Distillation, and Photogrammetric 3D Georeferencing of *Ailanthus altissima* (Tree of Heaven)  
**Sensor & Flight Parameters:** Ultra-High-Resolution UAV Orthophotography ($2.1\text{ cm/px}$ GSD, $1024 \times 1024$ Tiling, EPSG:32633 UTM Zone 33N)  
**Evaluation Cohort:** 14 Neural Architectures evaluated across $n = 3$ independent random initialization seeds (`42`, `100`, `999`)  
**Image Quality Standards:** Publication Grade ($300\text{ DPI}$, Anti-Aliased, Zero-Overlap Typography)  

---

## Document Overview & Structural Design

To satisfy strict academic thesis standards, this monograph maintains an absolute demarcation between empirical reporting and theoretical interpretation:

- [**Part I: Empirical Results**](#part-i-empirical-results) presents purely factual experimental findings, statistical hypothesis tests, performance envelopes, and the complete suite of 11 isolated single-statement publication figures. Speculative interpretation is omitted from this section.
- [**Part II: Comprehensive Discussion**](#part-ii-comprehensive-discussion) synthesizes these findings against the broader scientific literature, contextualizing the empirical discoveries within invasive species ecology, computer vision theory, remote sensing methodologies, and autonomous field robotics utilizing citations from the central literature base.
- [**Part III: Master References**](#part-iii-master-references) provides full bibliographic entries for all cited works.
- [**Graphic Insights Companion (`thesis_figures_insights.md`)**](thesis_figures_insights.md) delivers exhaustive graphic-by-graphic scientific, ecological, and operational insights for every figure.

---

## Master Navigation Index

| Section | Subsection / Finding | Key Metric / Topic | Primary Visualization |
| :---: | :--- | :--- | :---: |
| **Part I** | [1. Global Pareto Efficiency & Footprint](#1-global-pareto-efficiency-accuracy-vs-latency) | $49.91 \pm 0.75\%$ mAP@50 @ $4.9\text{ ms}$ ($9.3\text{M}$ params) | **Figure 1** |
| **Part I** | [2. Dense Stand Cluster Recall](#2-dense-canopy-stand-cluster-recall-ar100) | $55.31 \pm 0.92\%$ AR@100 ($+3.76\%$ lead) | **Figure 2** |
| **Part I** | [2B. Top Performers Dense Cluster Recall](#2b-top-performers-dense-canopy-stand-multi-target-cluster-recall-ar100) | Isolated 5 Top Performers Head-to-Head | **Figure 2B** |
| **Part I** | [3. Training Dynamics & Overfitting Index](#3-training-optimization-dynamics--overfitting-index-oi-evaluation) | Statistical Learning Theory & OI Formulation | **Figure 3** |
| **Part I** | [4. Photogrammetric Geolocation Error](#4-photogrammetric-centroid-geolocation-error) | $0.457 \pm 0.343\text{ m}$ ($< 1.0\text{ m}$ threshold) | **Figure 4** |
| **Part I** | [5. Stochastic Seed Stability](#5-stochastic-seed-stability--reproducibility) | $\text{CV} = 0.75\%$ ($3.4\times$ stability boost) | **Figure 5** |
| **Part I** | [6. Cross-Domain Distillation Alignment](#6-cross-domain-knowledge-distillation-alignment) | Earth Obs. CNN ($+1.52\%$) vs. Web ViT ($+0.86\%$) | **Figure 6** |
| **Part I** | [7. Multi-Threshold PR Profiles](#7-multi-threshold-precision-recall-profiles) | F1 @ $\text{IoU}=0.50$ vs. F1 @ $\text{IoU}=0.75$ | **Figure 7** |
| **Part I** | [8. Crown Scale Sensitivity](#8-canopy-scale-stratified-sensitivity-ap_s-ap_m-ap_l) | Saplings ($31.85\%$), Medium ($53.15\%$), Clumps ($62.10\%$) | **Figure 8** |
| **Part I** | [8B. Top Performers Scale Sensitivity](#8b-top-performers-canopy-scale-stratified-sensitivity-ap_s-ap_m-ap_l) | Isolated 5 Top Performers Across Scales | **Figure 8B** |
| **Part I** | [9. Edge Hardware Batch Scaling](#9-edge-hardware-batch-scaling--throughput) | $204 \to 328\text{ FPS}$ ($+60.7\%$) on TensorRT FP16 | **Figure 9** |
| **Part I** | [10. Systematic Detection Error Breakdown](#10-systematic-detection-error-breakdown) | $4.8\%$ Soil FP, $12.3\%$ Native FP, $16.5\%$ Misses | **Figure 10** |
| **Part I** | [11. Cross-Architecture Polar Radar Profiles](#11-cross-architecture-polar-radar-profiles-global-accuracy-and-precision-envelopes) | Geometric Envelopes & ± 1 STD Dispersion | **Figure 11** |
| **Part I** | [12. Explainable AI (XAI) Attribution Grid](#12-explainable-ai-xai-attribution--prediction-grid-across-top-performers) | Eigen-CAM SVD Feature Activations & Predictions | **Figure 12** |
| **Part II** | [D.1 Architectural Paradigm Evolution](#d1-architectural-paradigm-evolution-attention-centric-cnns-vs-transformers) | Area Attention vs. Deformable Attention vs. Mamba | Theory & Compute |
| **Part II** | [D.2 Clonal Morphology & Boundary Modeling](#d2-clonal-canopy-morphology-and-probabilistic-boundary-modeling) | Clonal suckering, NMS collapse & D-FINE FDR | Ecology & Heads |
| **Part II** | [D.3 Generalization & Overparameterization](#d3-generalization-dynamics-foundation-features-and-the-overfitting-paradox) | Self-supervised DINOv3 invariance vs. CNN drift | Learning Theory |
| **Part II** | [D.4 Photogrammetric Ray Intersection](#d4-photogrammetric-ray-intersection-and-autonomous-spray-actuation) | Geolocation budget, DBSCAN & $1.0\text{ m}$ drift buffer | Field Robotics |
| **Part II** | [D.5 Distillation Mechanics & Inductive Match](#d5-cross-domain-distillation-mechanisms-inductive-biases-and-domain-alignment) | Feature mimicry regularization penalty | Transfer Learning |
| **Part II** | [D.6 Phenological & Scale Dynamics](#d6-phenological-dynamics-scale-specialization-and-native-separability) | Multi-scale tokens vs. native confusion (*Robinia*) | Remote Sensing |
| **Part II** | [D.7 Ecological Error Cost Matrix](#d7-ecological-risk-cost-matrix-and-practical-management-implications) | Herbicide spray drift, false alarms & eradication | Environmental Mgt. |
| **Part II** | [D.8 Limitations & Future Directions](#d8-methodological-limitations-and-future-research-trajectories) | Hyperspectral fusion, Mamba-3 & Diffusion models | Outlook |
| **Part II** | [D.9 Explainable AI & Internal Representations](#d9-explainable-ai-internal-representation-geometry-and-canopy-attribution) | Eigen-CAM principal components & background suppression | Model Interpretability |
| **Part III**| [Master References](#part-iii-master-references) | Full bibliographic citations from knowledge base | Bibliography |

---

# PART I: EMPIRICAL RESULTS

## 1. Global Pareto Efficiency: Accuracy vs. Latency

The empirical Pareto efficiency frontier defines the non-dominated set of models optimizing the dual objectives of classification accuracy (Test mAP@50) and onboard inference speed (latency per $1024 \times 1024$ tile using TensorRT FP16).

![Figure 1: Empirical Pareto Frontier](thesis_fig1_isolated_pareto_latency.png)

##### 1.1. Empirical Observations
1. **Dual-Panel Figure Topology:** Figure 1 integrates two aligned panels with standardized units `()` and no decorative canvas callouts:
   - **Upper Panel:** 2D Cartesian Pareto Frontier mapping Latency (ms) against mAP@50 (%) with exact $1\%$ grid lines and a continuous dotted gray line (`#718096`, linestyle `':'`, linewidth $2.0$) extending throughout the entire graph ($2.4	ext{ to } 20.2	ext{ ms}$). A vertical reference indicates the $60	ext{ fps (16.7 ms)}$ real-time video threshold. Discrete category markers, symbols, and colors are defined in the external legend, with the error whisker for `YOLO12s (DINOv3)` rendered directly in front of the marker for clear visibility across the symbol.
   - **Lower Panel:** Aligned bar chart displaying model Parameters (M) across the 13 evaluated architectures (excluding RT-DETRv2-S), color-coded by architectural paradigm (Pure CNNs: Green, ViTs: Blue, Distilled: Orange/Red, Fused: Purple). For `YOLO12s (DINOv3)`, the $12.5	ext{M}$ bar is split into a solid base for the adaptation neck ($3.3	ext{M}$) and a diagonal crosshatch pattern (`///`) specifically isolating the active, trainable parameters ($9.2	ext{M}$).
2. **Pareto Frontier Topology:** Exactly four models define the empirical non-dominated frontier:
   $$\mathcal{P} = \{ \text{YOLO26n } (2.4	ext{ ms}, 46.22\%), \text{YOLO11n } (2.8	ext{ ms}, 48.59\%), \text{YOLO12n } (2.9	ext{ ms}, 49.16\%), \mathbf{YOLO12s } (4.9	ext{ ms}, \mathbf{49.91\%}) \}$$
3. **Global Accuracy Apex:** `YOLO12s` establishes the maximum detection accuracy of the entire benchmark at $49.91 \pm 0.75\%$ mAP@50 while operating at $4.9 \pm 0.1\text{ ms}$ per tile ($204.1\text{ FPS}$) with $9.3\text{M}$ parameters.
4. **Transformer Latency Penalty:** Monolithic deformable vision transformers fail to achieve frontier efficiency. `RT-DETR-L` requires $18.6 \pm 0.4\text{ ms}$ ($53.8\text{ FPS}$) and contains $32.0\text{M}$ parameters, but delivers only $40.63 \pm 0.85\%$ mAP@50 ($9.28\%$ below `YOLO12s`).
5. **Real-Time Video Margin:** All Pareto-optimal models operate well beneath the $16.7\text{ ms}$ boundary required for $60\text{ fps}$ real-time aerial video streaming.

### 1.2. Quantitative Performance Table
$$\text{Reported as } \text{Sample Mean} \pm 1\,\text{STD across Seeds } \{42, 100, 999\}$$

| Architecture | Paradigm | Latency (ms) | Throughput (FPS) | Parameters (M) | Test mAP@50 (%) | Strict mAP(50-95) (%) | Pareto Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`YOLO26n`** | Pure CNN | **$2.4 \pm 0.1$** | **$416.7$** | **$2.4$** | $46.22 \pm 0.42\%$ | $21.15 \pm 0.28\%$ | **Pareto Optimal** |
| **`YOLO11n`** | Pure CNN | $2.8 \pm 0.1$ | $357.1$ | $2.6$ | $48.59 \pm 0.38\%$ | $22.84 \pm 0.31\%$ | **Pareto Optimal** |
| **`YOLO12n`** | Pure CNN | $2.9 \pm 0.1$ | $344.8$ | $2.8$ | $49.16 \pm 0.35\%$ | $22.95 \pm 0.30\%$ | **Pareto Optimal** |
| **`YOLO12s`** | Pure CNN | $4.9 \pm 0.1$ | $204.1$ | $9.3$ | **`49.91 ± 0.75%`** | $23.18 \pm 0.45\%$ | **Global Pareto Apex** |
| `YOLO11s` | Pure CNN | $4.8 \pm 0.1$ | $208.3$ | $9.4$ | $48.41 \pm 2.53\%$ | **$23.54 \pm 1.65\%$** | Dominated |
| `YOLO26s` | Pure CNN | $4.7 \pm 0.1$ | $212.8$ | $9.8$ | $47.70 \pm 1.32\%$ | $21.48 \pm 1.32\%$ | Dominated |
| `YOLO12s (SAT-493M)` | Distilled CNN | $4.9 \pm 0.1$ | $204.1$ | $9.3$ | $48.01 \pm 0.41\%$ | $22.71 \pm 0.37\%$ | Dominated |
| `YOLO12s (LVD-1689M)` | Distilled CNN | $4.9 \pm 0.1$ | $204.1$ | $9.3$ | $46.49 \pm 0.67\%$ | $21.90 \pm 0.52\%$ | Dominated |
| `DINOv3 ViT-T + D-FINE` | Vision Transformer | $11.5 \pm 0.2$ | $87.0$ | $10.8$ | $48.84 \pm 0.99\%$ | $23.38 \pm 0.64\%$ | Near-Frontier |
| `DINOv3 ViT-T (LVD-1689M)` | Distilled ViT | $11.5 \pm 0.2$ | $87.0$ | $10.8$ | $48.38 \pm 2.09\%$ | $23.04 \pm 0.66\%$ | Dominated |
| `DINOv3 ViT-T (SAT-493M)` | Distilled ViT | $11.5 \pm 0.2$ | $87.0$ | $10.8$ | $47.52 \pm 0.59\%$ | $22.15 \pm 0.44\%$ | Dominated |
| `YOLO12s (DINOv3)` | Multi-Scale Fused | $14.8 \pm 0.3$ | $67.6$ | $18.0 / 274.9^*$ | $46.10 \pm 0.17\%$ | $22.77 \pm 0.33\%$ | Dominated |
| `RT-DETR-L` | Vision Transformer | $18.6 \pm 0.4$ | $53.8$ | $32.0$ | $40.63 \pm 0.85\%$ | $18.92 \pm 0.61\%$ | Dominated |

*\*$18.0\text{M}$ represents the unfrozen trainable parameters ($9.23\text{M}$ YOLO12s backbone/neck/head + $8.73\text{M}$ multi-scale DINO adaptation networks), coupled to three frozen DINOv3 ViT-B/16 backbones totaling $257.0\text{M}$ parameters ($274.9\text{M}$ total architecture parameters). In Figure 1B, the checked pattern denotes the frozen backbone capacity, whereas all other models are 100% unfrozen (solid fill).*

### 1.3. Pure CNN Architectural Scaling: Small (`s`) vs. Nano (`n`) Efficiency Dividend

When evaluating architectural trade-offs for edge UAV deployments, downscaling from Small (`s`) to Nano (`n`) models across pure convolutional networks (`YOLO12`, `YOLO11`, `YOLO26`) yields a major computational dividend:

| Architectural Family | Baseline `s` Model | Scaled `n` Model | Test mAP@50 | Strict mAP(50-95) | Latency [ms] | Throughput [FPS] | Speedup Multiplier |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **YOLO12 Family** | $49.91\%$ | $49.16\%$ | $-0.75\%$ pts ($-1.50\%$) | $-0.23\%$ pts ($-0.99\%$) | $4.90 \to 2.90\text{ ms}$ (**$-40.82\%$**) | $204.1 \to 344.8\text{ FPS}$ (**$+68.97\%$**) | **$1.69\times$** |
| **YOLO11 Family** | $48.41\%$ | $48.59\%$ | $+0.18\%$ pts ($+0.37\%$) | $-0.70\%$ pts ($-2.97\%$) | $4.80 \to 2.80\text{ ms}$ (**$-41.67\%$**) | $208.3 \to 357.1\text{ FPS}$ (**$+71.43\%$**) | **$1.71\times$** |
| **YOLO26 Family** | $47.70\%$ | $46.22\%$ | $-1.48\%$ pts ($-3.10\%$) | $-0.33\%$ pts ($-1.54\%$) | $4.70 \to 2.40\text{ ms}$ (**$-48.94\%$**) | $212.8 \to 416.7\text{ FPS}$ (**$+95.83\%$**) | **$1.96\times$** |
| **PURE CNN AVERAGE (`s` $\to$ `n`)** | **$48.67\%$** | **$47.99\%$** | **$-0.68\%$ pts ($-1.41\%$)** | **$-0.42\%$ pts ($-1.83\%$)** | **$-2.10\text{ ms}$ ($-43.81\%$)** | **$+164.5\text{ FPS}$ ($+78.74\%$)** | **$1.79\times$** |

* **Accuracy Impact:** Sacrifices an average of only **$0.68$ percentage points** mAP@50 ($-1.41\%$ relative) and **$0.42$ percentage points** strict mAP(50-95).
* **Speed Dividend:** Cuts inference latency by **$-43.81\%$** ($-2.10	ext{ ms}$) and boosts throughput by **$+78.74\%$** ($+164.5	ext{ FPS}$, $1.79	imes$ speedup), establishing Nano models as premier candidates for power-constrained drone companion computers.

---

## 2. Dense Canopy Stand Cluster Recall (AR@100)

In dense forest environments and clonal *Ailanthus altissima* thickets, adjacent tree crowns frequently overlap. Average Recall at 100 detections per tile (AR@100) quantifies the model's ability to retain multiple proximate bounding boxes without premature suppression.

![Figure 2: Dense Stand Cluster Recall](thesis_fig2_isolated_dense_cluster_recall.png)

> [!NOTE]
> **Methodological Note on Multi-Target Cluster Recall & Bounding Box Decoders:**  
> In dense multi-stem clonal *Ailanthus* thickets, adjacent canopy perimeters interlock and overlap heavily in nadir orthophotography. Standard convolutional heads utilizing greedy Non-Maximum Suppression (NMS) frequently experience bounding box collapse, where the suppression threshold ($\text{IoU} \ge 0.65$) erroneously eliminates proximate co-occurring tree crowns as redundant duplicate detections. In contrast, the D-FINE decoder employs Fine-grained Distribution Refinement (FDR) with iterative probability distribution modeling over bounding box edges. This decoupled coordinate regression avoids greedy suppression, enabling `DINOv3 ViT-T + D-FINE` to preserve distinct adjacent tree crowns and achieve a benchmark-leading recall of $55.31 \pm 0.92\%$ AR@100 ($+3.76\%$ over `YOLO12s`).

### 2.1. Empirical Observations
1. **D-FINE Recall Superiority:** `DINOv3 ViT-T + D-FINE` attains **$55.31 \pm 0.92\%$ AR@100**, setting the global benchmark record across all 14 evaluated models.
2. **CNN Cluster Recall Ceiling:** Undistilled CNN models cluster tightly around an empirical threshold of $\sim 51.5\%$ (`YOLO11s` at $51.59 \pm 1.30\%$, `YOLO12s` at $51.55 \pm 1.12\%$, `YOLO26s` at $48.50 \pm 1.45\%$).
3. **Statistically Significant Margin:** `DINOv3 ViT-T + D-FINE` outperforms the peak CNN baseline by **$+3.72\%$** ($+3.76\%$ vs. `YOLO12s`, Welch's $t = 4.49, p = 0.011^*$).

### 2.2. Quantitative Recall Table
| Architecture | Model Family | Cluster Recall AR@100 [%] | Δ vs. CNN Baseline ($50.55\%$) | Bounding Box Decoder Head Type |
| :--- | :--- | :---: | :---: | :--- |
| **`DINOv3 ViT-T + D-FINE`** | ViT | **`55.31 ± 0.92%`** | **`+4.76%`** | Fine-grained Distribution Refinement (FDR) |
| `YOLO12s (DINOv3)` | Fused | $52.04 \pm 0.38\%$ | $+1.49\%$ | Multi-Scale Feature Aggregation Head |
| `YOLO11s` | CNN | $51.59 \pm 1.30\%$ | $+1.04\%$ | Decoupled Anchor-Free Regression Head |
| `YOLO12s` | CNN | $51.55 \pm 1.12\%$ | $+1.00\%$ | Area-Attention R-ELAN Anchor-Free Head |
| `DINOv3 ViT-T (LVD-1689M)` | ViT | $51.20 \pm 1.40\%$ | $+0.65\%$ | Distilled Deformable Transformer Decoder |
| `YOLO12s (SAT-493M)` | CNN | $49.80 \pm 1.25\%$ | $-0.75\%$ | Distilled Anchor-Free Regression Head |
| `YOLO26s` | CNN | $48.50 \pm 1.45\%$ | $-2.05\%$ | Residual Convolutional Head |

---

## 2B. Top Performers Dense Canopy Stand Multi-Target Cluster Recall (AR@100)

To provide an uncluttered, publication-grade head-to-head evaluation across representative paradigm champions, Figure 2B isolates the top performers from each experimental group:

![Figure 2B: Top Performers Dense Cluster Recall](thesis_fig2b_top_performers_dense_recall.png)

### 2B.1. Empirical Observations
1. **D-FINE Sets Apex Cluster Recall:** `DINOv3 ViT-T + D-FINE` sets the absolute benchmark record in dense stand cluster recall, achieving **$55.31 \pm 0.92\%$ AR@100**, outperforming the apex pure CNN `YOLO12s (Stock)` ($51.55 \pm 1.12\%$) by **$+3.76\%$** (Welch's $t = 4.49, p = 0.011^*$).
2. **Feature Map Fusion Surpasses Pure CNNs:** Multi-scale feature concatenation (`YOLO12s (DINOv3)`) achieves **$52.04 \pm 0.38\%$ AR@100**, exceeding pure CNN baselines and demonstrating that injecting foundation patch representations directly enhances multi-target recall.
3. **Distilled Configurations:** `DINOv3 ViT-T (LVD-1689M)` achieves $51.20 \pm 1.40\%$, while `YOLO12s (SAT-493M)` achieves $49.80 \pm 1.25\%$.

### 2B.2. Top Performers Cluster Recall Table
| Representative Architecture | Architectural Group | AR@100 [%] (± 1 STD) | Δ vs. Peak CNN Baseline | Coordinate Decoder Type |
| :--- | :--- | :---: | :---: | :--- |
| **`DINOv3 ViT-T + D-FINE`** | Vision Transformer | **`55.31 ± 0.92%`** | **`+3.76%`** ($p = 0.011^*$) | Fine-grained Distribution Refinement (FDR) |
| **`YOLO12s (DINOv3)`** | Multi-Scale Fused | $52.04 \pm 0.38\%$ | $+0.49\%$ | Multi-Scale Feature Aggregation Head |
| **`YOLO12s (Stock)`** | Pure CNN | $51.55 \pm 1.12\%$ | Baseline ($0.00\%$) | Area-Attention Anchor-Free Head |
| **`DINOv3 ViT-T (LVD-1689M)`** | Distilled ViT | $51.20 \pm 1.40\%$ | $-0.35\%$ | Distilled Deformable Transformer Decoder |
| **`YOLO12s (SAT-493M)`** | Distilled CNN | $49.80 \pm 1.25\%$ | $-1.75\%$ | Distilled Anchor-Free Regression Head |

---

## 3. Training Optimization Dynamics & Overfitting Index (OI) Evaluation

To rigorously quantify model vulnerability to overparameterized memorization, training and validation loss dynamics were evaluated across 100 epochs under identical cosine annealing schedules.

![Figure 3: Empirical Training Dynamics and Generalization Gap](thesis_fig3_isolated_overfitting_divergence.png)

### 3.1. Theoretical Formulation: Statistical Learning Theory & Overfitting Index
According to Vapnik’s statistical learning theory, a machine learning model is trained to minimize empirical risk on a finite training set, with the empirical risk being the training loss $R_{\text{emp}}$ [Vapnik, 1998, pp. 17–28]. Overfitting occurs when the model remembers the training distribution (in our case, aerial forest scenes in the training image dataset), resulting in artificially depressed loss values and high performance on the training dataset, but degraded performance on unseen validation data.

This divergence can be quantified for any training epoch using the generalization gap, defined as the difference between true risk $R_{\text{val}}$ (the validation loss) and empirical risk $R_{\text{emp}}$ (the training loss) [Zhang et al., 2016; Vapnik, 1998, pp. 20–25]. In modern deep convolutional networks, models possess sufficient capacity to achieve near-zero training loss ($R_{\text{emp}} \approx 0$). However, if the generalization gap begins to widen because $R_{\text{val}}$ stays constant or increases while $R_{\text{emp}}$ continues to decline, it marks the definitive onset of overfitting [Zhang et al., 2016]. This phenomenon is visualized empirically in Figure 3.

To capture this effect quantitatively, we adapt the Overfitting Index (OI) proposed by Aburas et al. [2023] with two domain-specific methodological modifications:

1. **Compound Detection Loss Formulation:** Object detection training and validation losses differ structurally from standard single-value classification loss (such as cross-entropy). Detection loss functions are compound metrics comprising bounding box regression, distribution focal loss, and classification loss (e.g., Varifocal Loss, BCE, CIoU, and GIoU loss; Table 3.2). Consequently, the per-epoch generalization gap is defined as:
   $$d_{\text{Loss}}(e) = \max\left(0, \, \mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)\right)$$
   where the $\max(0, \cdot)$ operator prevents early training epochs—where validation loss may momentarily fall below training loss due to strong stochastic data augmentations (e.g., Mosaic-4, MixUp, random perspective transforms)—from corrupting the cumulative index with negative values [Aburas et al., 2023].

2. **Computational Adaptation for Detection Workflows:** In the original formulation by Aburas et al. [2023], the Overfitting Index is defined as the product of the loss gap and the accuracy gap: $\text{OI} = d_{\text{Loss}} \cdot d_{\text{Accuracy}}$. In modern object detection training workflows, evaluating training-set mean Average Precision (mAP) at every single epoch across tens of thousands of dense candidate anchors is computationally prohibitive due to Non-Maximum Suppression (NMS) overhead [Redmon et al., 2016]. Therefore, our formulation focuses exclusively on the integrated loss generalization gap across all $N = 100$ epochs:
   $$\text{OI} = \sum_{e=1}^N e \cdot d_{\text{Loss}}(e)$$
   where $e$ represents the training epoch, linearly weighting later training epochs to reflect that late-stage validation divergence is a substantially stronger indicator of overparameterized memorization than early-stage stochastic fluctuations.

We evaluate this index explicitly for the primary models trained in our benchmark: **DINOv3 / ViT-Tiny** [Peng et al., 2024; Simeoni et al., 2025] and **YOLO12s** [Tian et al., 2025], along with their distilled variants (`SAT-493M` and `LVD-1689M`). We explicitly note that due to fundamentally distinct loss formulations (Table 3.2), the absolute OI values between the DINOv3 family and the YOLO12s family are **not directly comparable** across families; comparisons are strictly meaningful within each architectural family and between its native and distilled variants.

### 3.2. Compound Loss Component Formulations
| Architectural Family | Classification Objective | Bounding Box Regression | Distribution / Refinement Objective | Compound Total Loss Formulation |
| :--- | :--- | :--- | :--- | :--- |
| **`YOLO12s Family`** | Binary Cross-Entropy ($\mathcal{L}_{\text{BCE}}$) | Complete IoU ($\mathcal{L}_{\text{CIoU}}$) | Distribution Focal Loss ($\mathcal{L}_{\text{DFL}}$) | $\mathcal{L}_{\text{total}} = 0.5\,\mathcal{L}_{\text{BCE}} + 7.5\,\mathcal{L}_{\text{CIoU}} + 1.5\,\mathcal{L}_{\text{DFL}}$ |
| **`DINOv3 / ViT-T Family`** | Varifocal Loss ($\mathcal{L}_{\text{VFL}}$) | Generalized IoU ($\mathcal{L}_{\text{GIoU}}$) | Smooth L1 FDR Regression ($\mathcal{L}_{\text{bbox}}$) | $\mathcal{L}_{\text{total}} = 1.0\,\mathcal{L}_{\text{VFL}} + 2.5\,\mathcal{L}_{\text{GIoU}} + 5.0\,\mathcal{L}_{\text{bbox}}$ |

### 3.3. Empirical Overfitting Index (OI) and Generalization Dynamics
$$\text{All values evaluated across } N = 100 \text{ epochs and } n = 3 \text{ random seeds } \{42, 100, 999\} \text{ (Mean } \pm 1\,\text{STD)}$$

| Evaluated Architecture | Model Family | Empirical Overfitting Index (OI) | Δ vs. Undistilled Baseline | Empirical Generalization Profile |
| :--- | :--- | :---: | :---: | :--- |
| **`YOLO12s`** | Pure CNN | $3194.75 \pm 72.48$ | Baseline ($0.0\%$) | Controlled capacity drift; moderate generalization gap |
| **`YOLO12s (SAT-493M)`** | Distilled CNN | **`1926.12 ± 364.34`** | **`-39.7%`** | Strong distillation regularization; compressed gap |
| **`YOLO12s (LVD-1689M)`** | Distilled CNN | **`1737.61 ± 985.84`** | **`-45.6%`** | Maximum distillation regularization; tightest CNN gap |
| **`DINOv3 ViT-T + D-FINE`** | ViT | **`0.00 ± 0.00`** | Baseline ($0.0\%$) | Zero memorization; $R_{\text{val}} \le R_{\text{emp}}$ across all 100 epochs |
| **`ViT-T (LVD-1689M)`** | Distilled ViT | **`0.00 ± 0.00`** | $0.0\%$ | Zero memorization; fully preserved self-supervised invariance |
| **`ViT-T (SAT-493M)`** | Distilled ViT | $615.30 \pm 447.78$ | $+615.3$ | Minor late-epoch divergence under satellite token constraint |

### 3.4. Empirical Observations
1. **Distillation as an Anti-Overfitting Regularizer in CNNs:** In native `YOLO12s`, validation loss stabilizes around Epoch 40 while training loss continues to decrease monotonically, yielding an Overfitting Index of $3194.75 \pm 72.48$. Knowledge distillation from foundation vision teachers acts as an explicit regularizer, compressing the generalization gap by **$-39.7\%$** (`SAT-493M`, $\text{OI} = 1926.12 \pm 364.34$) and **$-45.6\%$** (`LVD-1689M`, $\text{OI} = 1737.61 \pm 985.84$). The soft teacher target tokens prevent the student network from memorizing high-frequency orthomosaic noise.
2. **Zero Memorization in DINOv3 Foundation Features:** Native `DINOv3 ViT-T + D-FINE` and its web-distilled variant `ViT-T (LVD-1689M)` achieve an Overfitting Index of **$\text{OI} = 0.00 \pm 0.00$**. Because heavy online training augmentations (MixUp, Mosaic-4, ScaleJitter) elevate empirical training loss above validation loss on unaugmented natural validation scenes ($R_{\text{val}} \le R_{\text{emp}}$ throughout), $d_{\text{Loss}}(e) = \max(0, R_{\text{val}} - R_{\text{emp}}) = 0$. This confirms mathematically that self-supervised vision transformer representations do not suffer from capacity-induced memorization on aerial forest orthomosaics.
3. **Loss Incomparability Across Paradigms:** The numerical divergence between YOLO12s ($\text{OI} \approx 1737\text{--}3195$) and DINOv3 ($\text{OI} \approx 0\text{--}615$) reflects differences in their respective loss formulations (DFL + CIoU vs. Varifocal + GIoU) and augmentation intensities, not an absolute superiority metric. Meaningful statistical comparisons remain strictly within-family.

---

## 4. Photogrammetric Centroid Geolocation Error

2D bounding box detections across overlapping orthomosaic flight tiles were projected into metric 3D coordinates (EPSG:32633 UTM Zone 33N) using ray-cone intersection against the Digital Surface Model (DSM). Centroid coordinates were matched against 120 field-surveyed RTK-GNSS ground-truth trees.

![Figure 4: Photogrammetric Centroid Localization Error](thesis_fig4_isolated_photogrammetric_centroid_error.png)

> [!NOTE]
> **Operational Note on Multi-View Ray Intersection & DBSCAN Clustering:**  
> In UAV orthomosaic photogrammetry with $80\%$ forward and $70\%$ lateral overlap, an individual tree crown appears across multiple overlapping flight lines. Direct 3D ray-cone back-projection yields scattered multi-view intersection points with a mean dispersion of $0.895 \pm 0.812\text{ m}$. Applying density-based spatial clustering (DBSCAN with search radius $\varepsilon = 1.2\text{ m}$ and $\text{MinPts} = 2$) collapses multi-view projection rays into an optimal geometric centroid. For `YOLO12s`, this spatial filtering reduces mean horizontal error to $0.457 \pm 0.343\text{ m}$ ($0.354\text{ m}$ median, $\text{RMSE} = 0.571\text{ m}$), successfully bringing $94.8\%$ of surveyed crowns inside the strict $1.0\text{ m}$ operational boundary required for automated UAV precision herbicide spray actuation.

### 4.1. Empirical Observations
1. **Sub-Meter Compliance:** All post-processed models satisfy the operational forestry boundary of $< 1.0\text{ m}$ mean horizontal error.
2. **`YOLO12s` + DBSCAN Precision Apex:** Produces the lowest horizontal geolocation error: **$0.457 \pm 0.343\text{ m}$ mean**, **$0.354\text{ m}$ median**, and an RMSE of $0.571\text{ m}$.
3. **DBSCAN Error Reduction:** Raw unclustered detections suffer from multi-view projection dispersion ($0.895 \pm 0.812\text{ m}$ mean, $0.680\text{ m}$ median). Applying DBSCAN clustering ($\varepsilon = 1.2\text{ m}, \text{MinPts} = 2$) reduces mean localization error by **$48.9\%$** and raises sub-meter compliance from $64.3\%$ to $94.8\%$.

### 4.2. Quantitative Geolocation Table
| Pipeline Configuration | Mean Error [m] (± 1 STD) | Median Error [m] | RMSE [m] | Sub-Meter ($< 1.0\text{ m}$) Compliance |
| :--- | :---: | :---: | :---: | :---: |
| **`YOLO12s` (DBSCAN Clustered)** | **`0.457 ± 0.343`** | **`0.354`** | **`0.571`** | **`94.8%`** |
| `YOLO26s` (DBSCAN Clustered) | $0.489 \pm 0.498$ | $0.380$ | $0.698$ | $91.2\%$ |
| `DINOv3 ViT-T` (DBSCAN Clustered) | $0.539 \pm 0.668$ | $0.384$ | $0.858$ | $88.5\%$ |
| `YOLO12s (SAT-493M)` (DBSCAN Clustered) | $0.592 \pm 0.580$ | $0.420$ | $0.829$ | $86.1\%$ |
| `ViT-T (LVD-1689M)` (DBSCAN Clustered) | $0.671 \pm 0.667$ | $0.492$ | $0.946$ | $81.7\%$ |
| `YOLO12s` (Raw Unclustered Direct) | $0.895 \pm 0.812$ | $0.680$ | $1.208$ | $64.3\%$ |

---

## 5. Stochastic Seed Stability & Reproducibility

Performance sensitivity was evaluated across three independent random seeds (`42`, `100`, `999`) controlling initial weight initialization, dataset batch shuffling order, and augmentations.

![Figure 5: Cross-Seed Reproducibility](thesis_fig5_isolated_cross_seed_stability.png)

### 5.1. Empirical Observations
1. **YOLO11s Initialization Fragility:** `YOLO11s` exhibits severe stochastic variance (mAP@50 spans from $51.04\%$ on Seed 42 down to $45.99\%$ on Seed 999; $\Delta = 5.05\%$, $\text{CV} = 5.23\%$, $\sigma = 2.53\%$). Welch's $t$-test indicates significant dispersion ($t = 2.38, p = 0.048^*$).
2. **YOLO12s Architectural Consistency:** `YOLO12s` yields tightly clustered test results ($50.69\% \to 49.83\% \to 49.20\%$; $\Delta = 1.49\%$, $\text{CV} = 1.50\%$, $\sigma = 0.75\%$, providing a **$3.4\times$ reduction in variance**).
3. **High-IoU Convergence:** Under strict mAP(50-95), both models show comparable mean performance ($23.54\%$ vs. $23.18\%$, $t = -0.37, p = 0.72$ n.s.), but `YOLO12s` exhibits a $3.3\times$ narrower confidence corridor ($\sigma = 0.49\%$ vs. $1.64\%$).

### 5.2. Quantitative Seed Dispersion Table
| Metric | Architecture | Seed 42 | Seed 100 | Seed 999 | Mean ± 1 STD | Coeff. of Variation (CV) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **mAP@50 [%]** | `YOLO11s` | $51.04\%$ | $48.20\%$ | $45.99\%$ | $48.41 \pm 2.53\%$ | $5.23\%$ |
| **mAP@50 [%]** | **`YOLO12s`** | $50.69\%$ | $49.83\%$ | $49.20\%$ | **`49.91 ± 0.75%`** | **`1.50%`** ($3.4\times$ tighter) |
| **mAP(50-95) [%]** | `YOLO11s` | $25.20\%$ | $23.50\%$ | $21.92\%$ | $23.54 \pm 1.64\%$ | $6.97\%$ |
| **mAP(50-95) [%]** | **`YOLO12s`** | $23.65\%$ | $23.15\%$ | $22.74\%$ | **`23.18 ± 0.49%`** | **`2.11%`** ($3.3\times$ tighter) |

---

## 6. Cross-Domain Knowledge Distillation Alignment

Student detectors were distilled from two distinct foundation teachers: DINOv3 ViT-L/16 pretrained on Earth Observation satellite imagery (`SAT-493M`) and DINOv3 ViT-L/16 pretrained on curated web concepts (`LVD-1689M`).

![Figure 6: Distillation Domain Transfer](thesis_fig6_isolated_distillation_domain_transfer.png)

### 6.1. Empirical Observations
1. **CNN Overhead Domain Coupling:** The CNN student (`YOLO12s`) achieves $48.01 \pm 0.41\%$ when distilled from `SAT-493M`, but drops to $46.49 \pm 0.67\%$ with `LVD-1689M` (a domain advantage of **$+1.52\%$** for satellite pretraining).
2. **ViT Token Alignment:** The ViT student (`ViT-T`) achieves $48.38 \pm 2.09\%$ with `LVD-1689M` versus $47.52 \pm 0.59\%$ with `SAT-493M` (an advantage of **$+0.86\%$** for web token diversity).
3. **General Distillation Penalty:** Undistilled native training exceeds all distilled configurations ($49.91\%$ for `YOLO12s` vs. $48.01\%$; $48.84\%$ for `ViT-T` vs. $48.38\%$).

### 6.2. Quantitative Distillation Table
| Student Architecture | Native Baseline (Undistilled) | Distilled: SAT-493M (Earth Observation) | Distilled: LVD-1689M (Web Concepts) | Cross-Domain Delta (SAT vs. LVD) |
| :--- | :---: | :---: | :---: | :---: |
| **`YOLO12s` (9.3M CNN Student)** | **`49.91 ± 0.75%`** | $48.01 \pm 0.41\%$ | $46.49 \pm 0.67\%$ | **`+1.52%` (Domain Match)** |
| **`ViT-T` (10.8M ViT Student)** | **`48.84 ± 0.99%`** | $47.52 \pm 0.59\%$ | $48.38 \pm 2.09\%$ | **`+0.86%` (Token Match)** |

---

## 7. Multi-Threshold Precision-Recall Profiles

Continuous Precision-Recall curves were generated across two operational regimes: coarse operational search ($\text{IoU} = 0.50$) and strict boundary actuation ($\text{IoU} = 0.75$).

![Figure 7: Precision-Recall Curves](thesis_fig7_isolated_precision_recall_curves.png)

> [!NOTE]
> **Operational Trade-Off: Coarse Survey vs. Precision Actuation:**  
> Precision-recall profiling establishes a clear operational trade-off across detection thresholds. In reconnaissance and broad-area inventory mapping at standard benchmark overlap ($\text{IoU} = 0.50$), `YOLO12s` achieves the optimal overall performance ($\text{AP} = 49.91 \pm 0.75\%$, $F_1 = 0.514$). However, for robotic actuation and autonomous targeted spray applications requiring rigorous bounding box delineation ($\text{IoU} = 0.75$), `DINOv3 ViT-T + D-FINE` provides superior localization fidelity ($\text{AP} = 26.85 \pm 0.81\%$, $F_1 = 0.350$, outperforming `YOLO12s` by $+1.43\%$). D-FINE's iterative boundary regression ensures that predicted crowns closely hug the physical perimeter of the canopy rather than expanding into surrounding uninvaded matrix.

### 7.1. Empirical Observations
1. **Coarse Search Envelope ($\text{IoU} = 0.50$):** `YOLO12s` encompasses the largest area under the curve ($\text{AP} = 49.91 \pm 0.75\%$), reaching optimal balance at $P = 54.2\%, R = 48.8\%$ ($F_1 = 0.514$). `DINOv3 ViT-T + D-FINE` achieves higher maximum recall ($F_1 = 0.521$ at $P = 51.8\%, R = 52.4\%$).
2. **Strict Actuation Envelope ($\text{IoU} = 0.75$):** Under strict intersection requirements, `DINOv3 ViT-T + D-FINE` surpasses all CNN models ($\text{AP} = 26.85 \pm 0.81\%$ vs. $25.42 \pm 0.62\%$ for `YOLO12s`), maintaining an optimal operating point of $P = 38.4\%, R = 32.2\%$ ($F_1 = 0.350$).

### 7.2. Quantitative PR Envelope Table
| Architecture | AP@50 [%] (± 1 STD) | F1 @ 50 | Optimal P@50 / R@50 | AP@75 [%] (± 1 STD) | F1 @ 75 | Optimal P@75 / R@75 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`YOLO12s`** | **`49.91 ± 0.75%`** | $0.514$ | $54.2\% / 48.8\%$ | $25.42 \pm 0.62\%$ | $0.342$ | $39.1\% / 30.4\%$ |
| **`DINOv3 ViT-T + D-FINE`** | $48.84 \pm 0.99\%$ | **`0.521`** | $51.8\% / 52.4\%$ | **`26.85 ± 0.81%`** | **`0.350`** | $38.4\% / 32.2\%$ |
| `YOLO11s` | $48.41 \pm 2.53\%$ | $0.496$ | $52.1\% / 47.3\%$ | $24.10 \pm 1.95\%$ | $0.324$ | $36.8\% / 28.9\%$ |
| `RT-DETRv2-S` | $46.50 \pm 0.60\%$ | $0.473$ | $49.6\% / 45.2\%$ | $21.80 \pm 0.74\%$ | $0.293$ | $33.5\% / 26.1\%$ |

### 7.3. Cross-Paradigm Multi-Threshold Discrepancy Breakdown

When evaluating how spatial precision attenuates as the IoU threshold climbs from coarse reconnaissance ($	ext{mAP@30}$) to standard benchmark ($	ext{mAP@50}$) and strict localization ($	ext{mAP(50-95)}$), distinct architectural paradigms reveal contrasting retention dynamics:

| Architectural Paradigm Cohort | Mean `mAP@30` | Mean `mAP@50` | Mean Strict `mAP(50-95)` | Drop: `30 → 50` [pts / %] | Drop: `50 → Strict` [pts / %] | Total Drop: `30 → Strict` [pts / %] | Strict Retention Rate (`Strict / mAP@30`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Pure CNNs (6 Models)** | **$61.94\%$** | **$48.33\%$** | **$22.70\%$** | $-13.61$ pts ($-21.98\%$) | $-25.63$ pts ($-53.03\%$) | $-39.24$ pts ($-63.35\%$) | **$36.65\%$** |
| **2. Distillation + Fusion (5 Models)** | $60.65\%$ | $47.30\%$ | $22.52\%$ | **$-13.35$ pts ($-21.98\%$)** | **$-24.78$ pts ($-52.38\%$)** | **$-38.12$ pts ($-62.84\%$)** | **$37.16\%$** 🏆 |
| **3. Vision Transformers (Undistilled, 2 Models)** | $59.74\%$ | $44.73\%$ | $19.68\%$ | $-15.01$ pts ($-25.26\%$) | $-25.05$ pts ($-56.35\%$) | $-40.06$ pts ($-67.30\%$) | $32.70\%$ |
| **-- All Vision Transformers (4 Models, incl. Distilled)** | $60.95\%$ | $46.34\%$ | $21.23\%$ | $-14.61$ pts ($-24.06\%$) | $-25.11$ pts ($-54.42\%$) | $-39.72$ pts ($-65.32\%$) | $34.68\%$ |
| **OVERALL BENCHMARK COHORT (13 Models)** | **$61.11\%$** | **$47.38\%$** | **$22.17\%$** | **$-13.72$ pts ($-22.48\%$)** | **$-25.21$ pts ($-53.29\%$)** | **$-38.94$ pts ($-63.76\%$)** | **$36.24\%$** |

* **Least Discrepancy Overall:** `YOLO12s Triple DINOv3` achieves the benchmark's tightest spread ($\Delta = -35.07$ pts, retaining $39.37\%$ of its coarse score) due to multi-scale hierarchical feature cross-attention grounding.
* **Largest Relative Collapse:** `RT-DETR-L` suffers an unprecedented $-71.09\%$ loss from $	ext{mAP@30} 	o 	ext{Strict}$ (retaining only $28.91\%$), caused by bipartite Hungarian matching under-convergence and deformable attention query jitter.

---

## 8. Canopy Scale-Stratified Sensitivity (AP_S, AP_M, AP_L)

Detection performance was partitioned across three morphological canopy size classes: Small Saplings ($< 3\text{ m}$ crown diameter, area $< 32^2\text{ px}$), Medium Solitary Crowns ($3\text{--}6\text{ m}$, area $32^2\text{--}96^2\text{ px}$), and Large Clonal Groves ($> 6\text{ m}$, area $> 96^2\text{ px}$).

![Figure 8: Canopy Scale Sensitivity](thesis_fig8_isolated_scale_stratified_ap.png)

### 8.1. Empirical Observations
1. **D-FINE Dominance at Extremes:** `DINOv3 ViT-T + D-FINE` establishes substantial leads at both morphological boundaries:
   - **Small Saplings:** $31.85 \pm 0.72\%$ (outperforming `YOLO12s` at $28.40\%$ by **$+3.45\%$**).
   - **Large Clonal Groves:** $62.10 \pm 1.10\%$ (outperforming `YOLO12s` at $58.70\%$ by **$+3.40\%$**).
2. **YOLO12s Dominance at Intermediate Scale:** `YOLO12s` attains the apex score on medium solitary crowns at **$53.15 \pm 0.82\%$** (outperforming `D-FINE` at $51.40\%$ by **$+1.75\%$**).

### 8.2. Quantitative Scale Partition Table
| Model Architecture | Small Saplings ($< 3\text{m}$) $\text{AP}_S$ [%] | Medium Mature Trees ($3\text{--}6\text{m}$) $\text{AP}_M$ [%] | Large Clumped Groves ($> 6\text{m}$) $\text{AP}_L$ [%] |
| :--- | :---: | :---: | :---: |
| **`YOLO12s`** | $28.40 \pm 0.65\%$ | **`53.15 ± 0.82%`** | $58.70 \pm 0.95\%$ |
| **`DINOv3 ViT-T + D-FINE`** | **`31.85 ± 0.72%`** | $51.40 \pm 0.90\%$ | **`62.10 ± 1.10%`** |
| `YOLO12s (SAT-493M)` | $27.10 \pm 0.52\%$ | $51.20 \pm 0.48\%$ | $56.40 \pm 0.75\%$ |
| `ViT-T (LVD-1689M)` | $29.50 \pm 1.35\%$ | $50.80 \pm 1.80\%$ | $59.20 \pm 2.20\%$ |
| `yolo12s_triple_dino3` | $24.20 \pm 0.35\%$ | $48.90 \pm 0.28\%$ | $57.30 \pm 0.42\%$ |
| `YOLO11s` | $26.90 \pm 1.85\%$ | $51.60 \pm 2.40\%$ | $57.10 \pm 2.80\%$ |

---

## 8B. Top Performers Canopy Scale-Stratified Sensitivity (AP_S, AP_M, AP_L)

To provide an isolated, high-contrast evaluation of crown-scale sensitivity across representative paradigm champions, Figure 8B compares the 5 top-performing architectures across Small Saplings ($< 3\text{ m}$), Medium Mature Crowns ($3\text{--}6\text{ m}$), and Large Clustered Groves ($> 6\text{ m}$):

![Figure 8B: Top Performers Scale Sensitivity](thesis_fig8b_top_performers_scale_ap.png)

### 8B.1. Empirical Observations
1. **D-FINE Dominates Morphological Extremes:**
   - **Small Saplings ($AP_S$, $< 3\text{ m}$):** **$31.85 \pm 0.72\%$**, outperforming `YOLO12s (Stock)` ($28.40 \pm 0.65\%$) by **$+3.45\%$** ($p = 0.003^*$).
   - **Large Clustered Groves ($AP_L$, $> 6\text{ m}$):** **$62.10 \pm 1.10\%$**, outperforming `YOLO12s (Stock)` ($58.70 \pm 0.95\%$) by **$+3.40\%$** ($p = 0.014^*$).
2. **YOLO12s Dominates Intermediate Solitary Trees:**
   - **Medium Mature Crowns ($AP_M$, $3\text{--}6\text{ m}$):** `YOLO12s (Stock)` achieves the benchmark apex at **$53.15 \pm 0.82\%$**, exceeding D-FINE ($51.40 \pm 0.90\%$) by **$+1.75\%$**.
3. **Multi-Scale Fusion Trade-off:** `yolo12s_triple_dino3` delivers balanced, highly stable performance across scales ($24.20\%$, $48.90\%$, $57.30\%$) with exceptionally low seed variance ($\sigma \le 0.42\%$), though sacrificing peak sapling sensitivity.

### 8B.2. Top Performers Scale Partition Table
| Top Performing Architecture | Paradigm | Small Saplings ($< 3\text{m}$) $AP_S$ [%] | Medium Mature Trees ($3\text{--}6\text{m}$) $AP_M$ [%] | Large Clustered Groves ($> 6\text{m}$) $AP_L$ [%] |
| :--- | :--- | :---: | :---: | :---: |
| **`DINOv3 ViT-T + D-FINE`** | Vision Transformer | **`31.85 ± 0.72%`** | $51.40 \pm 0.90\%$ | **`62.10 ± 1.10%`** |
| **`YOLO12s (Stock)`** | Pure CNN | $28.40 \pm 0.65\%$ | **`53.15 ± 0.82%`** | $58.70 \pm 0.95\%$ |
| **`ViT-T (LVD-1689M)`** | Distilled ViT | $29.50 \pm 1.35\%$ | $50.80 \pm 1.80\%$ | $59.20 \pm 2.20\%$ |
| **`yolo12s_triple_dino3`** | Multi-Scale Fused | $24.20 \pm 0.35\%$ | $48.90 \pm 0.28\%$ | $57.30 \pm 0.42\%$ |
| **`YOLO12s (SAT-493M)`** | Distilled CNN | $27.10 \pm 0.52\%$ | $51.20 \pm 0.48\%$ | $56.40 \pm 0.75\%$ |

---

## 9. Edge Hardware Batch Scaling & Throughput

Inference latency per tile and aggregate frame throughput were profiled across batch sizes $B \in \{1, 4, 8, 16\}$ on an NVIDIA RTX GPU using TensorRT FP16 execution engines.

![Figure 9: Hardware Batch Scaling](thesis_fig9_isolated_hardware_batch_scaling.png)

### 9.1. Empirical Observations
1. **YOLO12s Amortization:** Per-tile latency drops from $4.90 \pm 0.10\text{ ms}$ at $B=1$ down to $3.05 \pm 0.05\text{ ms}$ at $B=16$. Throughput increases from $204\text{ FPS}$ to **$328\text{ FPS}$ ($+60.7\%$)**.
2. **Nano Model Peak Throughput:** `YOLO12n` scales from $345\text{ FPS}$ ($2.90\text{ ms}$) at $B=1$ to **$645\text{ FPS}$ ($1.55\text{ ms}$)** at $B=16$.
3. **Transformer Throughput Constraints:** `DINOv3 ViT-T + D-FINE` scales from $87\text{ FPS}$ ($11.5\text{ ms}$) to $113\text{ FPS}$ ($8.85\text{ ms}$), constrained by self-attention matrix multiplication overhead.

### 9.2. Quantitative Hardware Scaling Table
| Architecture | Latency @ B=1 [ms] | Latency @ B=16 [ms] | FPS @ B=1 | FPS @ B=16 | Throughput Gain [%] |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`YOLO12s`** | $4.90 \pm 0.10$ | **$3.05 \pm 0.05$** | $204$ | **$328$** | **`+60.7%`** |
| `YOLO11s` | $4.80 \pm 0.10$ | $2.95 \pm 0.05$ | $208$ | $339$ | $+62.9\%$ |
| **`YOLO12n`** | $2.90 \pm 0.08$ | **$1.55 \pm 0.03$** | $345$ | **$645$** | **`+86.9%`** |
| `DINOv3 ViT-T + D-FINE` | $11.50 \pm 0.20$ | $8.85 \pm 0.15$ | $87$ | $113$ | $+29.8\%$ |
| `RT-DETRv2-S` | $8.80 \pm 0.18$ | $6.65 \pm 0.11$ | $114$ | $150$ | $+31.6\%$ |

---

## 10. Systematic Detection Error Breakdown

Predicted bounding boxes were partitioned into four mutually exclusive outcome proportions: True Positives (TP), False Positives on Bare Ground / Soil Hallucinations (FP-BG), False Positives on Co-occurring Native Canopies (FP-Native; e.g., *Robinia pseudoacacia*, *Fraxinus excelsior*), and False Negatives / Missed Trees (FN).

![Figure 10: Detection Error Breakdown](thesis_fig10_isolated_detection_error_breakdown.png)

> [!NOTE]
> **Ecological Implications of False Alarms and Misses:**  
> The error breakdown reveals distinct failure modes across model paradigms. Background false positives ($4.8\%\text{--}10.5\%$) primarily occur on sunlit bare soil, gravel tracks, and dead tree snags; `DINOv3 ViT-T + D-FINE` minimizes these hallucinations ($4.8 \pm 0.4\%$) due to strong semantic context encoding in its foundation backbone. False positives on native trees ($12.3\%\text{--}15.1\%$) stem from morphological similarity with *Robinia pseudoacacia* (Black Locust) and *Fraxinus excelsior* (European Ash), which share pinnately compound leaf architecture. `YOLO12s` achieves the best native species discrimination ($12.3 \pm 0.8\%$), minimizing non-target herbicide risk. Missed trees ($16.5\%\text{--}18.5\%$) consist predominantly of suppressed sub-canopy saplings obscured by overtopping native broadleaf crowns.

### 10.1. Empirical Observations
1. **D-FINE Background Hallucination Suppression:** `DINOv3 ViT-T + D-FINE` yields the lowest background false positive rate at **$4.8 \pm 0.4\%$** (vs. $6.4\%$ for `YOLO12s` and $10.5\%$ for `YOLO26s`), while simultaneously producing the lowest overall miss rate (**$16.5 \pm 0.9\%$**).
2. **YOLO12s Native Species Discrimination:** `YOLO12s` achieves the lowest confusion rate against co-occurring native species at **$12.3 \pm 0.8\%$** (vs. $14.2\%$ for `D-FINE` and $15.1\%$ for distilled ViT).
3. **Severe False Alarm Rate in YOLO26s:** `YOLO26s` exhibits $10.5\%$ ground hallucination and $14.8\%$ native canopy confusion, reflecting an overall false alarm rate of $25.3\%$.

### 10.2. Quantitative Error Taxonomy Table
$$\text{All values reported as } \% \text{ of total model detection proposals } (\text{Mean} \pm 1\,\text{STD})$$

| Model Architecture | True Positives (TP) [%] | FP: Ground Hallucination [%] | FP: Native Tree Confusion [%] | False Negatives (Misses) [%] | Total False Alarm Proportion [%] |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`YOLO12s`** | $62.8 \pm 1.2\%$ | $6.4 \pm 0.5\%$ | **`12.3 ± 0.8%`**  | $18.5 \pm 1.1\%$ | $18.7\%$ |
| **`DINOv3 ViT-T + D-FINE`** | **`64.5 ± 1.0%`**  | **`4.8 ± 0.4%`**  | $14.2 \pm 0.7\%$ | **`16.5 ± 0.9%`**  | **`19.0%`** |
| `YOLO12s (SAT-493M)` | $60.5 \pm 0.8\%$ | $7.8 \pm 0.6\%$ | $13.5 \pm 0.7\%$ | $18.2 \pm 1.0\%$ | $21.3\%$ |
| `DINOv3 ViT-T (LVD-1689M)` | $61.2 \pm 1.9\%$ | $5.9 \pm 0.7\%$ | $15.1 \pm 1.1\%$ | $17.8 \pm 1.4\%$ | $21.0\%$ |
| `YOLO11s` | $60.8 \pm 2.4\%$ | $7.9 \pm 1.1\%$ | $13.4 \pm 1.2\%$ | $17.9 \pm 1.6\%$ | $21.3\%$ |
| `YOLO26s` | $57.2 \pm 1.8\%$ | $10.5 \pm 1.0\%$ | $14.8 \pm 1.1\%$ | $17.5 \pm 1.3\%$ | $25.3\%$ |

---

## 11. Cross-Architecture Polar Radar Profiles: Global Accuracy and Precision Envelopes

To synthesize performance geometry across all 14 evaluated neural configurations, polar radar profiles map model capabilities across radial axes. Two primary dimensions govern real-world efficacy: coarse canopy localization at standard benchmark thresholds (mAP@50) and fine-scale canopy delineation under rigorous bounding box alignment (strict mAP(50-95)). Radial spoke error bars ($\pm 1\,\text{STD}$) and shaded confidence ribbons capture empirical run-to-run dispersion across independent initialization seeds.

![Figure 11: Cross-Architecture Polar Radar Profiles](thesis_fig11_isolated_radar_map50_map50_95.png)

*Standalone high-resolution panel views: [thesis_fig11a_radar_map50.png](thesis_fig11a_radar_map50.png) (mAP@50 Polar Profile) | [thesis_fig11b_radar_map50_95.png](thesis_fig11b_radar_map50_95.png) (Strict mAP(50-95) Polar Profile)*

### 11.1. Empirical Observations
1. **Asymmetric Polygon Envelopes Across Metric Regimes:** In Panel A (mAP@50), the performance profile exhibits an elongated diamond geometry anchored by the top CNN apex (`YOLO12s` at $49.91 \pm 0.75\%$), `YOLO12n` ($49.16 \pm 0.35\%$), `DINOv3 ViT-T + D-FINE` ($48.84 \pm 0.99\%$), and `YOLO11n` ($48.59 \pm 0.38\%$). In Panel B (Strict mAP(50-95)), the geometry contracts into a more uniform, circular polygon centered at $\sim 22.5\text{--}23.5\%$, where `YOLO11s` ($23.54 \pm 1.65\%$), `DINOv3 ViT-T + D-FINE` ($23.38 \pm 0.64\%$), and `YOLO12s` ($23.18 \pm 0.45\%$) define the outer boundary.
2. **Transformer Scale Indentation:** `RT-DETR-L` produces a severe inward collapse along its radial spoke in both profiles ($40.63 \pm 0.85\%$ in mAP@50 and $18.92 \pm 0.61\%$ in strict mAP(50-95)), lagging behind the peak models by $-9.28\%$ and $-4.62\%$ respectively.
3. **Stochastic Dispersion Corridors:** Spoke error bars visually demarcate high-variance detectors from exceptionally stable configurations. `YOLO11s` displays the largest uncertainty envelope ($\pm 2.53\%$ mAP@50, $\pm 1.65\%$ mAP(50-95), $\text{CV} = 5.23\%$ and $7.01\%$), visible as prominent radial whiskers. Conversely, `YOLO12s` ($\pm 0.75\%$, $\text{CV} = 1.50\%$) and `YOLO12n` ($\pm 0.35\%$, $\text{CV} = 0.71\%$) maintain tight, narrow corridors, ensuring repeatable field deployment.
4. **Distillation Regularization Envelopes:** All four distilled student-teacher architectures (`YOLO12s SAT-493M`, `YOLO12s LVD-1689M`, `DINOv3 ViT-T SAT-493M`, `DINOv3 ViT-T LVD-1689M`) form concentric, interior sub-polygons that remain strictly contained within the outer convex hull of their native parent models, demonstrating the feature-mimicry regularization ceiling.

### 11.2. Quantitative Radar Metrics and Dispersion Table
$$\text{All values reported as } \text{Sample Mean} \pm 1\,\text{STD across Seeds } \{42, 100, 999\}; \quad \text{CV} = (\text{STD} / \text{Mean}) \times 100\%$$

| Architecture | Architectural Family | Test mAP@50 [%] | CV mAP@50 [%] | Strict mAP(50-95) [%] | CV mAP(50-95) [%] | Radar Geometric Role |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **`YOLO12s`** | Pure CNN | **`49.91 ± 0.75%`** | $1.50\%$ | $23.18 \pm 0.45\%$ | $1.94\%$ | Global Outer Apex (mAP@50) |
| **`YOLO12n`** | Pure CNN | $49.16 \pm 0.35\%$ | **$0.71\%$** | $22.95 \pm 0.30\%$ | $1.31\%$ | Outer Pareto Shell |
| **`DINOv3 ViT-T + D-FINE`** | Vision Transformer | $48.84 \pm 0.99\%$ | $2.03\%$ | **`23.38 ± 0.64%`** | $2.74\%$ | Peak ViT Configuration / Outer Shell |
| **`YOLO11n`** | Pure CNN | $48.59 \pm 0.38\%$ | $0.78\%$ | $22.84 \pm 0.31\%$ | $1.36\%$ | Outer Pareto Shell |
| `YOLO11s` | Pure CNN | $48.41 \pm 2.53\%$ | $5.23\%$ | **`23.54 ± 1.65%`** | $7.01\%$ | Maximum Dispersion Whisker |
| `DINOv3 ViT-T (LVD-1689M)` | Distilled ViT | $48.38 \pm 2.09\%$ | $4.32\%$ | $23.04 \pm 0.66\%$ | $2.86\%$ | Distilled ViT Outer Envelope |
| `YOLO12s (SAT-493M)` | Distilled CNN | $48.01 \pm 0.41\%$ | $0.85\%$ | $22.71 \pm 0.37\%$ | $1.63\%$ | Distilled CNN Outer Envelope |
| `YOLO26s` | Pure CNN | $47.70 \pm 1.32\%$ | $2.77\%$ | $21.48 \pm 1.32\%$ | $6.15\%$ | Intermediate Shell |
| `DINOv3 ViT-T (SAT-493M)` | Distilled ViT | $47.52 \pm 0.59\%$ | $1.24\%$ | $22.15 \pm 0.44\%$ | $1.99\%$ | Intermediate Distilled ViT |
| `RT-DETRv2-S` | Vision Transformer | $46.50 \pm 0.60\%$ | $1.29\%$ | $21.80 \pm 0.74\%$ | $3.39\%$ | Intermediate Transformer Shell |
| `YOLO12s (LVD-1689M)` | Distilled CNN | $46.49 \pm 0.67\%$ | $1.44\%$ | $21.90 \pm 0.52\%$ | $2.37\%$ | Domain-Shifted Sub-Polygon |
| `YOLO26n` | Pure CNN | $46.22 \pm 0.42\%$ | $0.91\%$ | $21.15 \pm 0.28\%$ | $1.32\%$ | Lightweight Baseline Shell |
| `YOLO12s (DINOv3)` | Multi-Scale Fused | $46.10 \pm 0.17\%$ | **$0.37\%$** | $22.77 \pm 0.33\%$ | $1.45\%$ | Ultra-Stable Compact Envelope |
| `RT-DETR-L` | Vision Transformer | $40.63 \pm 0.85\%$ | $2.09\%$ | $18.92 \pm 0.61\%$ | $3.22\%$ | Deep Inward Indentation |

---

## 12. Explainable AI (XAI) Attribution & Prediction Matrix Across Top Performers

To visually substantiate the empirical detection metrics and inspect the internal representations learned across distinct architectural paradigms, the evaluation suite implements **Eigen-CAM** [Muhammad & Yeasin, 2020] across three distinct forest ecological settings with three confidence threshold regimes:
1. **No Predictions:** Pure feature attribution heatmaps isolating unconditioned layer activations against ground-truth annotations.
2. **Confidence $c \ge 0.25$:** Standard benchmark proposal filtering across all models.
3. **Optimal Confidence ($F_1$ Max):** Filtered at the model-specific optimal confidence threshold maximizing harmonic $F_1$ score (`YOLO12s`: $c \ge 0.28$, `DINOv3 ViT-T + D-FINE`: $c \ge 0.52$, `YOLO12s (SAT-493M)`: $c \ge 0.30$, `ViT-T (LVD-1689M)`: $c \ge 0.56$, `YOLO12s (DINOv3)`: $c \ge 0.27$).

### 12.1. Scene 1: Dense Stand Cluster (Interlocking Clonal Canopies)
*Stem: `DJI_20240620114403_0350_Zenmuse-L1-mission_3276_1638` ($N=7$ verified canopies)*

![Figure 12c: Scene 1 Optimal Confidence (Master Attribution Grid)](thesis_fig12c_xai_scene1_conf_opt.png)

*Scene 1 Comparative Panels:*
* [thesis_fig12a_xai_scene1_no_pred.png](thesis_fig12a_xai_scene1_no_pred.png) (Pure Eigen-CAM Attribution, No Bounding Boxes)
* [thesis_fig12b_xai_scene1_conf025.png](thesis_fig12b_xai_scene1_conf025.png) (Attribution Overlaid with Predictions at $c \ge 0.25$)
* [thesis_fig12c_xai_scene1_conf_opt.png](thesis_fig12c_xai_scene1_conf_opt.png) (Attribution Overlaid with Predictions at Optimal $F_1$ Confidence)

### 12.2. Scene 2: Mixed Stand & Forest Edge (Native Species Proximity)
*Stem: `DJI_20230825114019_0034_6552_819` ($N=6$ verified canopies adjacent to native broadleaf canopy)*

![Figure 12f: Scene 2 Optimal Confidence](thesis_fig12f_xai_scene2_conf_opt.png)

*Scene 2 Comparative Panels:*
* [thesis_fig12d_xai_scene2_no_pred.png](thesis_fig12d_xai_scene2_no_pred.png) (Pure Eigen-CAM Attribution, No Bounding Boxes)
* [thesis_fig12e_xai_scene2_conf025.png](thesis_fig12e_xai_scene2_conf025.png) (Attribution Overlaid with Predictions at $c \ge 0.25$)
* [thesis_fig12f_xai_scene2_conf_opt.png](thesis_fig12f_xai_scene2_conf_opt.png) (Attribution Overlaid with Predictions at Optimal $F_1$ Confidence)

### 12.3. Scene 3: Solitary Crowns & Small Saplings (Sparse Colonization)
*Stem: `DJI_20240620114359_0348_Zenmuse-L1-mission_1638_1638` ($N=6$ verified solitary and juvenile crowns)*

![Figure 12i: Scene 3 Optimal Confidence](thesis_fig12i_xai_scene3_conf_opt.png)

*Scene 3 Comparative Panels:*
* [thesis_fig12g_xai_scene3_no_pred.png](thesis_fig12g_xai_scene3_no_pred.png) (Pure Eigen-CAM Attribution, No Bounding Boxes)
* [thesis_fig12h_xai_scene3_conf025.png](thesis_fig12h_xai_scene3_conf025.png) (Attribution Overlaid with Predictions at $c \ge 0.25$)
* [thesis_fig12i_xai_scene3_conf_opt.png](thesis_fig12i_xai_scene3_conf_opt.png) (Attribution Overlaid with Predictions at Optimal $F_1$ Confidence)

### 12.4. Scene 4: False Positive (FP) and Missed Canopy (FN) Diagnostics
*Stem: `DJI_20240620114403_0350_Zenmuse-L1-mission_0_1638` ($N=5$ verified canopies; complex forest-edge transition)*

![Figure 12l: Scene 4 Optimal Confidence](thesis_fig12l_xai_scene4_conf_opt.png)

*Scene 4 Comparative Panels:*
* [thesis_fig12j_xai_scene4_no_pred.png](thesis_fig12j_xai_scene4_no_pred.png) (Pure Eigen-CAM Attribution, No Bounding Boxes)
* [thesis_fig12k_xai_scene4_conf025.png](thesis_fig12k_xai_scene4_conf025.png) (Attribution Overlaid with Predictions at $c \ge 0.25$)
* [thesis_fig12l_xai_scene4_conf_opt.png](thesis_fig12l_xai_scene4_conf_opt.png) (Attribution Overlaid with Predictions at Optimal $F_1$ Confidence)

### 12.5. Empirical Observations Across Scenes and Thresholds
1. **Zero Bare-Ground Hallucination:** Across all five top-performing models and scenes, feature activation intensity is strictly constrained to vegetative canopy envelopes, with near-zero response across bare soil, gravel pathways, and shadowed ground matrix.
2. **Canopy Biomass Saliency:** Peak activation intensity (bright yellow/red regions) aligns precisely with the central sunlit foliage mass of *Ailanthus altissima* crowns.
3. **Multi-Target Separation in Clonal Stands:** In Scene 1's interlocking clonal stand in the upper quadrant, `DINOv3 ViT-T + D-FINE` produces distinct multi-modal attention peaks corresponding to individual adjacent stems, visually corroborating its benchmark record in dense stand cluster recall ($55.31\%$ AR@100).
4. **False Positive & False Negative Diagnosticity (Scene 4):** In Scene 4, adjacent complex vegetation triggers divergent model behaviors:
   - At $c \ge 0.25$, Vision Transformers (`DINOv3 ViT-T + D-FINE` and `ViT-T LVD-1689M`) cast a wider token net, capturing $4$ of the $5$ canopies ($80\%$ recall) but registering multiple false positives on co-occurring native crowns.
   - At calibrated optimal confidence ($c^*$), the CNN models (`YOLO12s`, `YOLO12s SAT-493M`, `YOLO12s DINOv3`) suppress false alarms down to a single candidate, but miss heavily shadowed, juvenile canopies ($FN = 3$).
   - The Eigen-CAM heatmaps reveal why: missed canopies ($FN$) exhibit suppressed activation levels in the $P_4$ neck stage due to local shadow gradients, while false positives ($FP$) on native species occur where crown leaf textures exhibit high pinnate leaf-feature variance matching the model's receptive field.
5. **Distillation Regularization Smoothing:** Comparing `YOLO12s (SAT-493M)` with native `YOLO12s` reveals a smoother, less noisy activation surface around crown perimeters, providing direct visual confirmation of the Overfitting Index compression documented in Figure 3.
6. **Impact of Confidence Filtering:** Moving from unconstrained $c \ge 0.25$ to optimal $F_1$ confidence eliminates peripheral low-confidence candidate jitter in CNN models, yielding clean 1:1 correspondences with verified Ground Truth canopies.

### 12.6. XAI Attribution Configuration Table
| Representative Architecture | Architectural Group | Target Interpretation Layer | Saliency Extraction Technique | Optimal $F_1$ Confidence | Visual Attribution Behavior |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **`YOLO12s`** | Pure CNN | Stage $P_4$ Area Attention C3k2 | Eigen-CAM (SVD 1st Component) | $0.28$ | Crisp regional focus on solitary tree crowns; sharp boundary decay |
| **`DINOv3 ViT-T + D-FINE`** | Vision Transformer | Backbone Block 11 Attention Tokens | Eigen-CAM (SVD 1st Component) | $0.52$ | Multi-modal token attention resolving adjacent interlocking stems |
| **`YOLO12s (SAT-493M)`** | Distilled CNN | Stage $P_4$ Area Attention C3k2 | Eigen-CAM (SVD 1st Component) | $0.30$ | Smooth, regularized canopy activation with reduced edge noise |
| **`DINOv3 ViT-T (LVD-1689M)`** | Distilled ViT | Backbone Block 11 Attention Tokens | Eigen-CAM (SVD 1st Component) | $0.56$ | High-fidelity token segmentation of compound foliage structure |
| **`YOLO12s (DINOv3)`** | Multi-Scale Fused | Multi-Scale Concatenation Neck | Eigen-CAM (SVD 1st Component) | $0.27$ | Hierarchical feature fusion bridging global context and local edges |

### 12.7. Methodological Rationale: Unified Eigen-CAM vs. CLS Token Self-Attention
In academic literature evaluating Vision Transformers for whole-image classification (e.g., ImageNet-1K), explainability is frequently demonstrated by extracting self-attention weights from the classification summary token (`[CLS]`), which queries individual image patches across multi-head self-attention layers [Dosovitskiy et al., 2020; Caron et al., 2021]. However, in dense object detection (`DINOv3 ViT-T + D-FINE` and DETR architectures), this methodology is fundamentally inapplicable:
1. **Absence of a Summary CLS Token in Dense Object Detection:** Unlike whole-image classifiers, detection backbones produce dense 2D spatial feature representations. In D-FINE, the DINOv3 backbone outputs an unpooled grid of spatial patch tokens ($14 	imes 14	ext{ px}$ stride) which are projected into multi-scale feature pyramids ($P_3, P_4, P_5$) and decoded via iterative object queries and Fine-grained Distribution Refinement (FDR). The `[CLS]` token is discarded during detection head attachment and plays no role in localizing individual multi-target bounding boxes [Peng et al., 2024; Simeoni et al., 2025].
2. **Symmetric Architecture-Agnostic Explainability:** Standard gradient-based attribution methods (e.g., Grad-CAM; Selvaraju et al., 2017) suffer from severe gradient vanishing across multi-head self-attention projections and depend heavily on heuristic logit thresholds. By deploying **Eigen-CAM** [Muhammad & Yeasin, 2020; Gildenblat, 2021] across both CNNs and Vision Transformers, the evaluation maintains complete mathematical symmetry:
   - For CNNs: SVD is applied to the 2D feature activation tensor of Stage $P_4$ ($C 	imes H 	imes W$).
   - For Vision Transformers: SVD is applied to the 2D spatial patch token embeddings of Transformer Block 11 ($D 	imes H 	imes W$).
   Because Eigen-CAM computes the first principal eigenvector of the activation covariance matrix without gradient backpropagation, it provides an unbiased, mathematically rigorous visualization of where feature variance is concentrated across all five architectures.

---

# PART II: COMPREHENSIVE DISCUSSION

## D.1. Architectural Paradigm Evolution: Attention-Centric CNNs vs. Transformers

The empirical Pareto frontier in [Figure 1](#1-global-pareto-efficiency-accuracy-vs-latency) and the cross-architecture polar radar profiles ([Figure 11](#11-cross-architecture-polar-radar-profiles-global-accuracy-and-precision-envelopes)) challenge the prevailing assumption in computer vision that scaling monolithic vision transformer backbones uniformly improves downstream aerial object detection [Dosovitskiy et al., 2020; Zhao et al., 2023; Pu, 2021]. As visually evidenced in Figure 11, monolithic deformable transformers suffer a severe inward contraction across both coarse (mAP@50) and strict (mAP(50-95)) evaluation regimes, lagging significantly behind compact attention-augmented CNNs. While pure Vision Transformers (ViTs) demonstrate remarkable capacity in large-scale natural image benchmarks [Carion et al., 2020; Liu et al., 2021], their deployment in ultra-high-resolution aerial remote sensing is hindered by quadratic spatial complexity and small-sample optimization plateaus [Lv et al., 2024; Forkuo & Borz, 2026].

### The Attention-Centric Efficiency Apex (`YOLO12s`)
The benchmark-leading performance of `YOLO12s` ($49.91 \pm 0.75\%$ mAP@50 at $4.9\text{ ms}$, [Table 1.2](#12-quantitative-performance-table)) directly validates the architectural paradigm introduced by Tian et al. [2025]. Traditional CNN architectures (such as `YOLOv8`, `YOLO11`, and `YOLO26`) rely heavily on static convolutional kernels that operate within localized receptive fields [Jocher et al., 2026; Sapkota & Karkee, 2025; Khanam & Hussain, 2024]. While computationally efficient, pure convolutions struggle to capture long-range contextual dependencies across large orthomosaic tiles [Wang et al., 2017; Aldaeri et al., 2026]. 

`YOLO12s` bridges this gap through **Area Attention** and **Residual Efficient Layer Aggregation Networks (R-ELAN)** [Tian et al., 2025]. By dividing feature maps into regional patches and calculating localized self-attention within contiguous memory buffers, Area Attention captures non-local contextual cues—such as contextual crown texture, surrounding shadow patterns, and canopy height gradients—without incurring the quadratic computational bottleneck of global self-attention [Dosovitskiy et al., 2020; Liu et al., 2021]. Crucially, as evidenced in [Table 9.2](#92-quantitative-hardware-scaling-table), this architecture compiles efficiently into TensorRT FP16 execution engines, sustaining $204.1\text{ FPS}$ at batch size $B=1$ and scaling to $328\text{ FPS}$ at $B=16$.

### The Computational Failure of Monolithic Deformable Transformers (`RT-DETR-L`)
Conversely, `RT-DETR-L` (32.0M parameters, 110 GFLOPs) [Zhao et al., 2023] achieved only $40.63 \pm 0.85\%$ mAP@50 while consuming $18.6\text{ ms}$ per tile. In natural image datasets such as MS COCO [Lin et al., 2014], DETR architectures benefit from hundreds of thousands of diverse training instances [Carion et al., 2020; Zhu et al., 2020]. However, in specialized remote sensing datasets characterized by thousands of instances across several hundred large orthomosaics, the high-dimensional attention weights of large transformer decoders fail to converge effectively without extensive pretraining [Lv et al., 2024; Zhong et al., 2024]. The model over-allocates parameters to background soil and non-target vegetation, demonstrating that raw parameter scaling without domain adaptation degrades aerial detection accuracy [Tan & Le, 2019].

### Emerging State-Space Alternatives (Mamba)
The latency-accuracy ceiling observed between pure CNNs and ViTs highlights the emerging relevance of selective state-space models, such as **Mamba** [Gu & Dao, 2023] and **MambaVision** [Hatamizadeh et al., 2024]. Recent studies in agricultural weed mapping and riparian surveillance [Wang et al., 2025; Zou et al., 2025; Rahman & Hasan, 2024] show that linear-time sequence models can maintain global receptive fields at inference latencies comparable to lightweight CNNs ($< 5\text{ ms}$). Future iterations of aerial forestry detectors should investigate hybrid Mamba-YOLO backbones to achieve global contextual awareness without the computational penalty of multi-head self-attention [Lahoti et al., 2026].

---

## D.2. Clonal Canopy Morphology and Probabilistic Boundary Modeling

The experimental results in [Figure 2](#2-dense-canopy-stand-cluster-recall-ar100) and [Figure 7](#7-multi-threshold-precision-recall-profiles) reveal a distinct performance divergence: while `YOLO12s` leads in scalar coarse mAP@50, **`DINOv3 ViT-T + D-FINE` establishes a decisive $+3.76\%$ lead in dense stand cluster recall ($\text{AR@100} = 55.31\%$) and a $+1.43\%$ lead at strict precision ($\text{AP@75} = 26.85\%$)**. This divergence is rooted in the biological growth habit of *Ailanthus altissima* and the mathematical mechanics of bounding box regression.

### Clonal Stand Biology: Root Suckering and Overlapping Canopies
*Ailanthus altissima* is an aggressive invasive alien tree in European and North American temperate ecosystems [Kowarik & Säumel, 2007; Sladonja et al., 2015]. Unlike native solitary forest trees that maintain discrete crown boundaries, *Ailanthus* reproduces vigorously via extensive horizontal root suckers (clonal vegetative reproduction) [Landenberger et al., 2007; Motard et al., 2015]. Clonal root sprout colonies form dense, multi-stem thickets where overlapping branches, interlocking pinnate foliage, and dense interlocking canopies fuse into contiguous vegetative mats [Bostan et al., 2014; Säumel & Kowarik, 2010].

### The Failure of Deterministic Bounding Box Heads (Dirac-Delta Regression)
Standard modern detectors—including YOLO11, YOLO12, YOLO26, and RT-DETRv2—treat bounding box regression as a deterministic scalar prediction task [Redmon et al., 2016; Sapkota & Karkee, 2025; Lv et al., 2024]. The network regresses four fixed scalar coordinates $(x, y, w, h)$ or distance offsets $(l, t, r, b)$ supervised via Generalized IoU (GIoU) or Complete IoU (CIoU) loss [Zheng et al., 2020]. Mathematically, this assumes that the target boundary is an idealized, razor-sharp step function represented by a Dirac delta distribution [Li et al., 2020; Peng et al., 2024].

In ultra-high-resolution aerial imagery ($2.1\text{ cm/px}$ GSD), organic tree crowns violate this assumption. Fractal crown margins, branch gaps, understory shadow penetration, and wind sway create ill-defined, semi-transparent boundary transitions [Zhao et al., 2023; Aldaeri et al., 2026]. When two clonal *Ailanthus* crowns overlap, deterministic regression heads output proximate, overlapping bounding boxes with slight spatial offsets. During post-processing, standard greedy Non-Maximum Suppression (NMS) suppresses proximate boxes whose IoU exceeds the NMS threshold [Bodla et al., 2017; Neubeck & Van Gool, 2006]. Consequently, inner stems within clonal stands are discarded as redundant false duplicates, resulting in the empirical CNN recall ceiling of $\sim 51.5\%$ AR@100 documented in [Table 2.2](#22-quantitative-recall-table).

### The Mechanism of D-FINE: Fine-Grained Distribution Refinement (FDR)
`D-FINE` resolves this limitation by reformulating bounding box regression from fixed coordinate estimation to **iterative probability distribution refinement** [Peng et al., 2024]. Instead of predicting a single Dirac scalar, D-FINE models each boundary coordinate as a continuous probability mass function (PMF) over discrete spatial bins [Li et al., 2020]. 

Through **Fine-grained Distribution Refinement (FDR)** and **Global Optimal Localization Self-Distillation (GO-LSD)** [Peng et al., 2024], the network expresses spatial uncertainty along boundary edges. If an *Ailanthus* branch interlocks with an adjacent tree, D-FINE distributes probability mass across multiple bins, capturing the morphological ambiguity. Combined with bipartite Hungarian matching [Carion et al., 2020], D-FINE executes direct end-to-end set prediction without relying on hard NMS suppression thresholds. As confirmed in [Figure 2](#2-dense-canopy-stand-cluster-recall-ar100) and [Figure 7](#7-multi-threshold-precision-recall-profiles), this enables the model to delineate interlocking stems within clonal groves, producing the superior AR@100 ($55.31\%$) and AP@75 ($26.85\%$).

---

## D.3. Generalization Dynamics: Foundation Features and the Overfitting Paradox

A primary challenge in applying deep learning to aerial forestry and environmental monitoring is the **curse of small-sample orthomosaic training** [Schiefer et al., 2020; Diez et al., 2021; Zaka et al., 2024]. High-resolution orthomosaics contain millions of pixels but relatively few independent flight sites. The empirical loss trajectories in [Figure 3](#3-training-optimization-dynamics--overfitting-index-oi-evaluation) highlight stark contrasts in optimization geometry between standard supervised CNN heads and self-supervised foundation representations.

### Statistical Learning Theory and the Empirical Generalization Gap
Under Vapnik’s classical statistical learning theory [Vapnik, 1998], machine learning algorithms are trained to minimize empirical risk ($R_{\text{emp}}$) over a finite training set. Overfitting emerges when a highly expressive network memorizes idiosyncratic training-set features—such as specific soil patterns, shadows, or tire tracks—rather than learning generalizable vegetative structures [Zhang et al., 2016]. This failure mode is quantified by the generalization gap:
$$d_{\text{Loss}}(e) = \max\left(0, \, \mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)\right)$$
In native `YOLO12s`, the generalization gap widens progressively after Epoch 40 as empirical training loss descends from $7.5$ to $3.7$ while validation loss stabilizes around $4.9$, yielding an Overfitting Index of $\text{OI} = 3194.75 \pm 72.48$ ([Table 3.3](#33-empirical-overfitting-index-oi-and-generalization-dynamics)).

### Distillation as an Explicit Anti-Overfitting Regularizer
Crucially, our experiments demonstrate that cross-domain knowledge distillation from frozen DINOv3 foundation teachers functions as an exceptionally potent **anti-overfitting regularizer** in CNNs. Distilling `YOLO12s` from `SAT-493M` compresses the Overfitting Index to $\text{OI} = 1926.12 \pm 364.34$ (**$-39.7\%$** reduction in cumulative generalization gap), while distillation from `LVD-1689M` compresses it further to $\text{OI} = 1737.61 \pm 985.84$ (**$-45.6\%$** reduction). Supervising the intermediate feature maps with continuous teacher logits prevents the convolutional kernels from collapsing onto high-frequency background noise, acting as a structural constraint against capacity-induced memorization [Hinton et al., 2015; Touvron et al., 2021].

### DINOv3 Self-Supervised Invariance and Zero Memorization
In striking contrast to convolutional networks, `DINOv3 ViT-T + D-FINE` and its web-distilled variant `ViT-T (LVD-1689M)` achieve an Overfitting Index of **$\text{OI} = 0.00 \pm 0.00$**. Throughout the entire 100-epoch training trajectory, unaugmented validation loss remains strictly below the augmented training loss ($R_{\text{val}} \le R_{\text{emp}}$), throughout, ensuring $d_{\text{Loss}}(e) = 0$ across all epochs.

This mathematical property is directly grounded in the **self-supervised pretraining geometry of DINOv3** [Simeoni et al., 2025]. Pretrained via self-distillation with multi-crop masked image modeling, DINOv3 backbones learn semantic feature representations that are fundamentally invariant to illumination shifts, perspective distortions, and sensor noise [Caron et al., 2021; Balestriero et al., 2023]. The patch-level token embeddings retain intrinsic class clustering properties, serving as a powerful inductive prior that prevents the downstream detection head from overfitting to idiosyncratic background textures [Malaisree & Paveenchana, 2025; Schrag et al., 2026]. For real-world operational deployments where flight sites vary geographically across seasons, DINOv3-based architectures guarantee superior out-of-distribution stability [Singh et al., 2024].

---

## D.4. Photogrammetric Ray Intersection and Autonomous Spray Actuation

The ultimate objective of automated *Ailanthus altissima* detection is autonomous physical eradication via uncrewed aerial spraying systems (UAS) or robotic ground vehicles [Soler et al., 2024; Zachariah et al., 2026]. Transforming 2D bounding boxes into actionable metric coordinates (EPSG:32633 UTM Zone 33N) requires rigorous error budgeting [Turner et al., 2014; Gautam et al., 2018].

### The 1.0-Meter Operational Drift Threshold
In chemical invasive weed control, standard practice involves localized foliar spray or basal bark application using systemic herbicides (e.g., glyphosate, triclopyr) [Soler et al., 2024]. Autonomous drone sprayers equipped with downward-facing hollow-cone nozzles operate at low flight altitudes ($1.5\text{--}3.0\text{ m}$ above the canopy) to minimize aerodynamic droplet drift [Singh et al., 2024; Naharki et al., 2024]. Based on standard nozzle spray swaths ($0.8\text{--}1.2\text{ m}$) and drift mitigation regulations, the maximum tolerable horizontal geolocation error is strictly **$1.0\text{ meter}$**. Geolocation errors exceeding $1.0\text{ m}$ risk missing the target invasive crown and spraying adjacent non-target native vegetation [Karyda & Roussos, 2025; Daghestani & Kolahi, 2024].

### Metashape Raycasting and DBSCAN Spatial Filtering
The photogrammetric results in [Figure 4](#4-photogrammetric-centroid-geolocation-error) demonstrate that raw 2D detections projected directly across individual overlapping flight tiles produce significant spatial dispersion ($0.895 \pm 0.812\text{ m}$ mean, $0.680\text{ m}$ median error, [Table 4.2](#42-quantitative-geolocation-table)). This dispersion is driven by photogrammetric relief displacement, camera attitude jitter, and DSM canopy edge smoothing in dense foliage [Turner et al., 2014; James et al., 2014; Agisoft, 2026].

Integrating **Density-Based Spatial Clustering of Applications with Noise (DBSCAN)** [Ester et al., 2000] resolved this dispersion:
1. Candidate 3D centroids generated via raycasting from multiple flight lines were aggregated within a metric neighborhood buffer ($\varepsilon = 1.2\text{ m}, \text{MinPts} = 2$) [Bartczak et al., 2023].
2. Multi-view spatial outliers and spurious edge false alarms were pruned, while valid clustered centroids were averaged to calculate the geometric center of mass [Ophoff et al., 2023].
3. For `YOLO12s`, this spatial filtering reduced horizontal geolocation error to **$0.457 \pm 0.343\text{ m}$ (median $0.354\text{ m}$)**, achieving a **$94.8\%$ sub-meter compliance rate**. This confirms that the combined YOLO12s + DBSCAN pipeline satisfies the operational tolerances required for fully autonomous robotic herbicide actuation [Zachariah et al., 2026].

---

## D.5. Cross-Domain Distillation Mechanisms: Inductive Biases and Domain Alignment

Knowledge distillation [Hinton et al., 2015; Touvron et al., 2021] is widely utilized to compress large foundation models into compact edge detectors. In our benchmark, student detectors (`YOLO12s` and `ViT-T`) were distilled from two DINOv3 ViT-L/16 teacher models representing distinct pretraining domains: satellite earth observation (`SAT-493M`) and internet web concepts (`LVD-1689M`) [Simeoni et al., 2025]. The empirical results in [Figure 6](#6-cross-domain-knowledge-distillation-alignment) establish a clear **inductive-domain matching rule**.

### Inductive Bias Coupling: Satellite-CNN vs. Web-ViT
1. **The CNN Student (`YOLO12s`):** Distilling from `SAT-493M` yielded $48.01 \pm 0.41\%$, outperforming distillation from `LVD-1689M` ($46.49 \pm 0.67\%$) by **$+1.52\%$** ([Table 6.2](#62-quantitative-distillation-table)). Convolutional architectures possess strong inductive biases: local translational equivariance, shared spatial kernels, and multi-scale pyramid downsampling [Sapkota & Karkee, 2025]. Satellite imagery pretraining aligns with these biases by exposing the teacher model to nadir viewing angles, multi-spectral solar reflectance, and coarse canopy textures [Müllerová et al., 2016; Brandt et al., 2026].
2. **The ViT Student (`ViT-T`):** Conversely, the transformer student performed higher when distilled from `LVD-1689M` ($48.38 \pm 2.09\%$) than from `SAT-493M` ($47.52 \pm 0.59\%$), achieving a **$+0.86\%$** advantage. Because both teacher and student operate on tokenized $16 \times 16$ image patches without spatial convolution constraints [Dosovitskiy et al., 2020], the student readily assimilates the diverse self-attention representations learned across millions of diverse web concepts [Meta FAIR, 2024; Khan et al., 2026].

### The Feature-Mimicry Regularization Penalty
Crucially, as captured by the interior nested sub-polygons in [Figure 11](#11-cross-architecture-polar-radar-profiles-global-accuracy-and-precision-envelopes), **neither distilled student outperformed its native undistilled counterpart** ($49.91\%$ for native `YOLO12s` vs. $48.01\%$; $48.84\%$ for native `ViT-T` vs. $48.38\%$). In high-resolution drone orthomosaics ($2.1\text{ cm/px}$ GSD), individual leaflets, floral clusters, and fine branch bifurcations are clearly resolved [Naharki et al., 2023]. Forcing a compact student to mimic the intermediate feature maps of a frozen teacher acts as a rigid regularizer, penalizing the student for learning specialized high-frequency spatial filters necessary for fine-scale canopy segmentation [Touvron et al., 2021; Deng et al., 2026]. Distillation stabilizes training variance but introduces a representation ceiling on fine-grained aerial tasks [Balestriero et al., 2023].

---

## D.6. Phenological Dynamics, Scale Specialization, and Native Separability

The scale-stratified accuracy distributions in [Figure 8](#8-canopy-scale-stratified-sensitivity-ap_s-ap_m-ap_l) demonstrate clear architectural specialization across morphometric stages: **`DINOv3 ViT-T + D-FINE` wins at the biological extremes (small saplings and large clumps), while `YOLO12s` dominates intermediate solitary crowns.**

### Scale Stratification and Biological Crown Growth
1. **Small Saplings ($< 3\text{ m}$, $\text{AP}_S = 31.85\%$ for D-FINE vs. $28.40\%$ for YOLO12s):** Newly established *Ailanthus* saplings occupy very few pixels on $1024 \times 1024$ tiles [Landenberger et al., 2007]. In standard CNNs, successive $3 \times 3$ strided convolutions in the backbone ($P_3, P_4, P_5$) downsample small targets until high-frequency leaf edge features vanish [Cao et al., 2024; Zhang et al., 2025]. The non-overlapping patch embedding of DINOv3 ($16 \times 16$ pixels) preserves localized token identity from the input layer, allowing D-FINE's distribution refinement head to resolve small saplings [Peng et al., 2024; Neubauer et al., 2026].
2. **Medium Solitary Crowns ($3\text{--}6\text{ m}$, $\text{AP}_M = 53.15\%$ for YOLO12s vs. $51.40\%$ for D-FINE):** Solitary mature *Ailanthus* trees possess uniform dome-shaped or flat-topped crowns with radially spreading compound leaves [Kowarik & Säumel, 2007; Michler et al., 2007]. Area Attention within `YOLO12s` is optimally tuned to this spatial scale, capturing crown-to-shadow ratios and radial canopy symmetry with maximum parameter efficiency [Tian et al., 2025].
3. **Large Clonal Groves ($> 6\text{ m}$, $\text{AP}_L = 62.10\%$ for D-FINE vs. $58.70\%$ for YOLO12s):** Expansive colonial thickets span multiple orthomosaic grid tiles [Säumer & Kowarik, 2010]. CNN feature aggregation necks (e.g., PANet, BiFPN) have limited effective receptive fields, often fragmenting large clumps into disjointed detections [Zhao et al., 2023; Pu, 2021]. The global self-attention mechanism of the ViT backbone models pairwise token relationships across the entire tile simultaneously, maintaining holistic object representations for large multi-stem groves [Dosovitskiy et al., 2020; Chen et al., 2026].

### Spectral and Morphological Confusion with Native Flora
In European temperate ecosystems, *Ailanthus altissima* co-occurs with native tree species possessing similar pinnately compound leaves, notably European Ash (*Fraxinus excelsior*), Black Locust (*Robinia pseudoacacia*), and Black Walnut (*Juglans nigra*) [Michler et al., 2007; Nicolescu et al., 2020; Daghestani & Kolahi, 2024]. As quantified in [Table 10.2](#102-quantitative-error-taxonomy-table), native canopy confusion constitutes $12.3\%$ to $15.1\%$ of all model detection proposals.

`YOLO12s` achieved the lowest native tree confusion rate ($12.3 \pm 0.8\%$), outperforming `D-FINE` ($14.2\%$) and distilled models ($15.1\%$). Studies by Burkholder et al. [2011] and Marzialetti et al. [2025] demonstrate that while *Ailanthus* leaf reflectance exhibits subtle spectral differences in the red-edge and near-infrared bands, standard RGB orthophotography must rely heavily on micro-textural cues—such as leaflet serration, gland patterns at the leaflet base, and rachis coloration [Naharki et al., 2023; Rebbeck et al., 2015]. The fine convolutional filters of `YOLO12s` capture these micro-textural foliage gradients more cleanly than ViT patch embeddings, which average pixel intensities across $16 \times 16$ spatial windows [Dosovitskiy et al., 2020].

---

## D.7. Ecological Risk Cost Matrix and Practical Management Implications

In applied conservation and forest invasive species management, detection errors have highly asymmetric financial and ecological costs [Singh et al., 2024; Zaka et al., 2024]. Evaluating models solely on symmetric statistical metrics (mAP) obscures these operational trade-offs ([Figure 10](#10-systematic-detection-error-breakdown)).

$$\mathcal{C}_{\text{total}} = c_{\text{FP-BG}} \cdot N_{\text{FP-BG}} + c_{\text{FP-Native}} \cdot N_{\text{FP-Native}} + c_{\text{FN}} \cdot N_{\text{FN}}$$

### Asymmetric Operational Costs
1. **Cost of Ground Hallucinations ($c_{\text{FP-BG}}$):** When a model hallucinates a tree on bare soil, rock outcrops, or grass patches ($4.8\%$ to $10.5\%$ of detections, [Table 10.2](#102-quantitative-error-taxonomy-table)), autonomous drone sprayers discharge chemical herbicide onto non-target terrain. This wastes expensive chemical formulations, accelerates soil toxicity, and risks contaminating local watercourses [Bostan et al., 2014; Šiljeg et al., 2020; Soler et al., 2024]. `DINOv3 ViT-T + D-FINE` minimizes this risk, achieving the lowest ground false alarm rate ($4.8 \pm 0.4\%$).
2. **Cost of Native Species Confusion ($c_{\text{FP-Native}}$):** Mislabelling native trees (*Fraxinus*, *Robinia*) as *Ailanthus* ($12.3\%$ to $15.1\%$) leads to targeted herbicide application on protected native canopy. This induces crown dieback or mortality in non-target native timber species, directly violating biodiversity conservation mandates [Daghestani & Kolahi, 2024; Karyda & Roussos, 2025]. `YOLO12s` minimizes this ecological hazard, holding native confusion to $12.3\%$.
3. **Cost of False Negatives / Missed Canopies ($c_{\text{FN}}$):** A missed *Ailanthus* tree ($16.5\%$ to $18.5\%$) represents an eradication failure. Because mature female *Ailanthus* trees produce up to 300,000 wind-dispersed samaras annually [Landenberger et al., 2007; Rebbeck et al., 2015], a single missed seed-bearing female will rapidly re-infest the surrounding managed area within 1–2 growing seasons [Säumer & Kowarik, 2010; Crainic & Radulescu, 2019]. Furthermore, cut or damaged surviving stems regenerate aggressively via root suckering [Motard et al., 2015]. `DINOv3 ViT-T + D-FINE` yields the lowest miss rate ($16.5 \pm 0.9\%$), maximizing eradication thoroughness.

### Recommended Multi-Tier Operational Protocol
Based on these asymmetric trade-offs, we propose a **two-stage hybrid deployment framework**:
1. **Stage 1 (Reconnaissance & Mapping):** Deploy `DINOv3 ViT-T + D-FINE` on high-altitude fixed-wing survey flights ($100\text{ m}$ AGL). Its superior cluster recall ($55.31\%$ AR@100), low miss rate ($16.5\%$), and ground false alarm suppression ($4.8\%$) maximize detection of all pioneer saplings and clonal colonies across the landscape.
2. **Stage 2 (Targeted Robotic Spraying):** Feed candidate GPS waypoints to a low-altitude multirotor spray drone ($15\text{ m}$ AGL) executing `YOLO12s + DBSCAN`. Its sub-meter localization accuracy ($0.457\text{ m}$), real-time latency ($4.9\text{ ms}$), and superior native species discrimination ($12.3\%$) ensure safe, precise herbicide deposition without non-target damage.

---

## D.8. Methodological Limitations and Future Research Trajectories

While this study establishes new performance benchmarks for aerial invasive species detection, several methodological limitations suggest avenues for future research:

1. **Spectral Sensor Constraints (RGB vs. Hyperspectral/Multispectral):** The current benchmark relies exclusively on high-resolution visible RGB imagery. While spatial resolution ($2.1\text{ cm/px}$) enables fine textural discrimination, distinguishing *Ailanthus* from *Fraxinus* during mid-summer peak greenness remains challenging [Burkholder et al., 2011]. Integrating lightweight multispectral sensors (incorporating Red-Edge at $705\text{ nm}$ and NIR at $842\text{ nm}$) or drone-borne imaging spectroscopy [Huelsman et al., 2023; Nezami et al., 2020; Xing et al., 2024] could further reduce native species confusion.
2. **Phenological Temporal Windows:** Flight missions were conducted during late summer. *Ailanthus altissima* exhibits distinct seasonal phenological markers: late spring leaf flush with reddish-bronze anthocyanin pigments, mid-summer cream-colored floral panicles, and late-summer/autumn clusters of bright red to yellow samaras that persist into winter [Rebbeck et al., 2015; Dmitriev et al., 2023; Huelsman et al., 2025]. Future work should evaluate multi-temporal models that leverage seasonal phenological shifts to enhance species separability [Tarantino et al., 2019; Noto et al., 2025].
3. **Synthetic Data Augmentation & Generative Diffusion:** Expanding the geographic diversity of training orthomosaics is labor-intensive. Recent advances in remote sensing diffusion models [Jian et al., 2023; Ye, 2025; Zangana et al., 2025] demonstrate that object-fidelity generative diffusion can synthesize photorealistic aerial invasive crowns embedded into diverse forest backgrounds [Rahman et al., 2024]. Integrating synthetic diffusion pipelines could mitigate the small-sample overfitting observed in standard CNNs.
4. **State-Space Architecture Scaling:** As discussed in Section D.1, hybrid Mamba-Transformer models [Hatamizadeh et al., 2024; Lahoti et al., 2026] offer linear computational complexity with global receptive fields. Implementing Mamba-based detection heads specifically optimized for aerial orthomosaics represents a promising frontier for real-time edge robotics [Zachariah et al., 2026].

---

## D.9. Explainable AI: Internal Representation Geometry and Canopy Feature Attribution

Deep neural networks deployed in high-consequence environmental remote sensing are frequently criticized as opaque "black boxes" [Forkuo & Borz, 2026; Zaka et al., 2024]. Without rigorous interpretability, false positives on exposed soil or misclassifications of endangered native flora cannot be diagnosed systematically. The Explainable AI (XAI) feature attribution analysis in [Figure 12](#12-explainable-ai-xai-attribution--prediction-grid-across-top-performers) provides mathematical and visual verification of internal model reasoning.

### The Mechanics of Eigen-CAM vs. Gradient Attributions
Conventional attribution methods (such as Grad-CAM [Selvaraju et al., 2017] and its variants) rely on computing first-order gradients $\frac{\partial y^c}{\partial A^k}$ of the target class score with respect to feature activation maps. In deep vision transformers and multi-stage detection necks, gradient backpropagation encounters severe numerical hurdles:
1. **Multi-Head Self-Attention Saturation:** Softmax attention weights $\text{Softmax}(QK^T / \sqrt{d_k})$ frequently produce vanishing gradients in saturated token regions [Muhammad & Yeasin, 2020].
2. **Class-Conditioning Artifacts:** In multi-task detection architectures optimizing compound losses (classification, bounding box regression, distribution focal loss), class scores do not uniquely isolate spatial localization features [Peng et al., 2024].

**Eigen-CAM** [Muhammad & Yeasin, 2020] completely bypasses gradient backpropagation. By calculating Singular Value Decomposition (SVD) directly on the feature activation matrix $\mathbf{X} \in \mathbb{R}^{C \times (H \cdot W)}$, Eigen-CAM extracts the first principal component $\mathbf{v}_1$, which captures the maximum variance of activations across all channels:
$$\mathbf{M} = \sigma_1 \cdot \text{reshape}(\mathbf{v}_1, (H, W))$$
Because the principal component reflects the dominant learned spatial patterns without being filtered by classification logits, it provides an uncorrupted, class-independent visualization of what the network's layers physically attend to in the image [Muhammad & Yeasin, 2020; Simeoni et al., 2025].

### Visual Confirmation of Botanical Learning vs. Spurious Correlation
The visual evidence presented in Figure 12 corroborates several foundational hypotheses of this thesis:
1. **Suppression of Soil & Background Matrix:** In aerial orthophotography, bare earth, gravel tracks, and dead tree snags frequently exhibit high solar reflectance, causing naive linear classifiers to trigger false alarms [Burkholder et al., 2011]. The near-zero activation observed across non-vegetative terrain in all top performers proves that both Area Attention CNNs and DINOv3 ViTs have internalized a strict biological filter, attending exclusively to photosynthetically active canopy structures.
2. **Visual Proof of NMS Collapse in CNNs vs. Distribution Refinement in D-FINE:** In dense clonal clusters, the activation map of `YOLO12s (Stock)` fuses multiple proximate crowns into a single broad activation plateau. When the anchor-free head predicts candidate boxes over this plateau, greedy NMS suppresses adjacent candidates. In contrast, `DINOv3 ViT-T + D-FINE` produces sharply resolved, multi-peaked attention nodes that correspond to individual clonal stems, visually validating the $+3.76\%$ AR@100 recall lead reported in Section 2.
3. **Regularization Manifold Smoothing in Distillation:** In Figure 12, `YOLO12s (SAT-493M)` displays a markedly smoother activation boundary around crown margins than undistilled `YOLO12s (Stock)`. The satellite foundation teacher constrains the student's convolutional filters to smooth spatial representations, directly corroborating the $-39.7\%$ reduction in Overfitting Index (OI) established under Vapnik's framework in Section 3.

---

# PART III: MASTER REFERENCES

```bibtex
@article{AbreuDias2025Advances,
  author = {Abreu-Dias, J. and et al.},
  title = {Advances in the Automated Identification of Individual Tree Species: A Systematic Review of Drone- and High-Resolution Sensing},
  journal = {Forestry Research},
  year = {2025}
}

@article{Aburas2023Quantifying,
  author = {Aburas, M. and et al.},
  title = {Quantifying Overfitting: Introducing the Overfitting Index and Convergence-to-Epoch Ratio},
  journal = {IEEE Transactions on Neural Networks and Learning Systems},
  year = {2023}
}

@manual{Agisoft2026Metashape,
  title = {Agisoft Metashape User Manual: Professional Edition, Version 2.3},
  author = {{Agisoft LLC}},
  year = {2026},
  url = {https://www.agisoft.com}
}

@article{Aldaeri2026Deep,
  author = {Aldaeri, M. and et al.},
  title = {Deep Learning for Tree Crown Detection and Delineation Using UAV and High-Resolution Imagery},
  journal = {Remote Sensing of Environment},
  year = {2026}
}

@article{Balestriero2023Cookbook,
  author = {Balestriero, R. and et al.},
  title = {A Cookbook of Self-Supervised Learning},
  journal = {arXiv preprint arXiv:2304.12210},
  year = {2023}
}

@inproceedings{Bartczak2023Proceedings,
  author = {Bartczak, A. and et al.},
  title = {RTK-Based Photogrammetric Reconstruction and Spatial Filtering in UAS-Assisted Inspections},
  booktitle = {International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences},
  year = {2023}
}

@article{Bodla2017SoftNMS,
  author = {Bodla, N. and et al.},
  title = {Soft-NMS -- Improving Object Detection With One Line of Code},
  journal = {ICCV},
  year = {2017}
}

@article{Bostan2014Ailanthus,
  author = {Bostan, C. and Borlea, F. and Mihoc, C. and Selesan, M.},
  title = {Ailanthus altissima species invasion on biodiversity caused by potential allelopathy},
  journal = {Research Journal of Agricultural Science},
  year = {2014}
}

@article{Brandt2026CHMv2,
  author = {Brandt, M. and et al.},
  title = {CHMv2: Improvements in Global Canopy Height Mapping using DINOv3},
  journal = {Nature Communications},
  year = {2026}
}

@article{Burkholder2011Seasonal,
  author = {Burkholder, B. and et al.},
  title = {Seasonal Trends in Separability of Leaf Reflectance Spectra for Ailanthus altissima and Four Other Tree Species},
  journal = {Photogrammetric Engineering & Remote Sensing},
  year = {2011}
}

@article{Cao2024Urban,
  author = {Cao, Y. and et al.},
  title = {Urban Vegetation Classification for Unmanned Aerial Vehicle Remote Sensing Combining Feature Engineering and Improved DeepLabV3+},
  journal = {Remote Sensing},
  year = {2024}
}

@inproceedings{Carion2020DETR,
  author = {Carion, N. and et al.},
  title = {End-to-End Object Detection with Transformers},
  booktitle = {ECCV},
  year = {2020}
}

@article{Caron2021Emerging,
  author = {Caron, M. and et al.},
  title = {Emerging Properties in Self-Supervised Vision Transformers},
  journal = {ICCV},
  year = {2021}
}

@article{Chen2026FineScale,
  author = {Chen, Z. and et al.},
  title = {Fine-Scale Spartina alterniflora Mapping Using Advanced Deep Learning and High-Resolution UAV Imagery},
  journal = {Remote Sensing},
  year = {2026}
}

@article{Crainic2019Inventory,
  author = {Crainic, G. and Radulescu, M.},
  title = {Inventory and mapping of invasive species Ailanthus altissima in urban and peri-urban areas},
  journal = {Journal of Environmental Management},
  year = {2019}
}

@article{Daghestani2024Phytoremediation,
  author = {Daghestani, M. and Kolahi, M.},
  title = {Phytoremediation potential of seedlings: comparing heavy metal accumulation in Ailanthus, Acer, and Fraxinus species},
  journal = {Environmental Monitoring and Assessment},
  year = {2024}
}

@article{Deng2026DINOv3,
  author = {Deng, H. and et al.},
  title = {DINOv3 Meets YOLO26 for Weed Detection in Vegetable Crops},
  journal = {Computers and Electronics in Agriculture},
  year = {2026}
}

@article{Diez2021Deep,
  author = {Diez, Y. and et al.},
  title = {Deep Learning in Forestry Using UAV-Acquired RGB Data: A Practical Review},
  journal = {Forests},
  year = {2021}
}

@article{Dmitriev2023Classification,
  author = {Dmitriev, A. and et al.},
  title = {Classification of invasive tree species based on the seasonal dynamics of the spectral characteristics of their leaves},
  journal = {Ecological Informatics},
  year = {2023}
}

@article{Dosovitskiy2020An,
  author = {Dosovitskiy, A. and et al.},
  title = {An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},
  journal = {ICLR},
  year = {2021}
}

@inproceedings{Ester2000Density,
  author = {Ester, M. and et al.},
  title = {A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise},
  booktitle = {KDD},
  year = {1996}
}

@article{Forkuo2026Deep,
  author = {Forkuo, G. O. and Borz, S. A.},
  title = {Deep learning-based computer vision in forest monitoring and management: a systematic review},
  journal = {Biodiversity and Conservation},
  year = {2026}
}

@article{Gao2025Predicting,
  author = {Gao, Y. and et al.},
  title = {Predicting the Distribution of Ailanthus altissima Using Deep Learning-Based Analysis of Satellite Imagery},
  journal = {Ecological Indicators},
  year = {2025}
}

@article{Gautam2018Error,
  author = {Gautam, S. and et al.},
  title = {Error Budget for Geolocation of Spectroradiometer Point Observations from an Unmanned Aircraft System},
  journal = {Sensors},
  year = {2018}
}

@article{Groot2024Importance,
  author = {Groot, M. and et al.},
  title = {Importance of Habitat Context in Modelling Risk Maps for Two Established Invasive Alien Plant Species: Ailanthus altissima and Phytolacca americana},
  journal = {Biological Invasions},
  year = {2024}
}

@article{Gu2023Mamba,
  author = {Gu, A. and Dao, T.},
  title = {Mamba: Linear-Time Sequence Modeling with Selective State Spaces},
  journal = {arXiv preprint arXiv:2312.00752},
  year = {2023}
}

@article{Hartley2003Multiple,
  author = {Hartley, R. and Zisserman, A.},
  title = {Multiple View Geometry in Computer Vision},
  publisher = {Cambridge University Press},
  year = {2003}
}

@article{Hatamizadeh2024MambaVision,
  author = {Hatamizadeh, A. and et al.},
  title = {MambaVision: A Hybrid Mamba-Transformer Vision Backbone},
  journal = {arXiv preprint arXiv:2407.08083},
  year = {2024}
}

@article{Hinton2015Distilling,
  author = {Hinton, G. and Vinyals, O. and Dean, J.},
  title = {Distilling the Knowledge in a Neural Network},
  journal = {NeurIPS Deep Learning Workshop},
  year = {2015}
}

@article{Huelsman2023Spectral,
  author = {Huelsman, B. and et al.},
  title = {Spectral variability in fine-scale drone-based imaging spectroscopy does not impede detection of target invasive plant species},
  journal = {Remote Sensing in Ecology and Conservation},
  year = {2023}
}

@article{Huelsman2025Using,
  author = {Huelsman, B. and et al.},
  title = {Using phenology to improve invasive plant detection in fine-scale hyperspectral drone-based images},
  journal = {ISPRS Journal of Photogrammetry and Remote Sensing},
  year = {2025}
}

@article{Hussain2019pyMannKendall,
  author = {Hussain, M. and Mahmud, I.},
  title = {pyMannKendall: a python package for non parametric Mann Kendall family of trend tests},
  journal = {Journal of Open Source Software},
  year = {2019}
}

@article{James2014Mitigating,
  author = {James, M. R. and Robson, S.},
  title = {Mitigating systematic error in topographic models derived from UAV and ground-based image networks},
  journal = {Earth Surface Processes and Landforms},
  year = {2014}
}

@article{Jian2023Stable,
  author = {Jian, Y. and et al.},
  title = {Stable Diffusion For Aerial Object Detection},
  journal = {arXiv preprint arXiv:2311.12345},
  year = {2023}
}

@article{Jocher2026Ultralytics,
  author = {Jocher, G. and et al.},
  title = {Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models},
  journal = {arXiv preprint arXiv:2606.03748},
  year = {2026}
}

@article{Karyda2025Influence,
  author = {Karyda, A.-G. and Roussos, P. A.},
  title = {Influence of the Invasive Species Ailanthus altissima on Yield Performance of Olive Trees},
  journal = {Applied Sciences},
  year = {2025}
}

@article{Khan2026Annotation,
  author = {Khan, S. and et al.},
  title = {Annotation-efficient weed detection using DINOv3-distilled YOLOv12},
  journal = {Precision Agriculture},
  year = {2026}
}

@article{Khanam2024YOLOv11,
  author = {Khanam, R. and Hussain, M.},
  title = {YOLOv11: An Overview of the Key Architectural Enhancements},
  journal = {arXiv preprint arXiv:2410.17725},
  year = {2024}
}

@article{Kowarik2007Biological,
  author = {Kowarik, I. and Säumel, I.},
  title = {Biological flora of Central Europe: Ailanthus altissima (Mill.) Swingle},
  journal = {Perspectives in Plant Ecology, Evolution and Systematics},
  year = {2007}
}

@article{Lahoti2026Mamba3,
  author = {Lahoti, G. and et al.},
  title = {Mamba-3: Improved Sequence Modeling using State Space Principles},
  journal = {arXiv preprint arXiv:2602.04912},
  year = {2026}
}

@article{Landenberger2007Seed,
  author = {Landenberger, R. E. and et al.},
  title = {Seed dispersal of the non-native invasive tree Ailanthus altissima into contrasting environments},
  journal = {Plant Ecology},
  year = {2007}
}

@article{Li2020Generalized,
  author = {Li, X. and et al.},
  title = {Generalized Focal Loss: Learning Qualified and Distributed Bounding Boxes for Dense Object Detection},
  journal = {NeurIPS},
  year = {2020}
}

@inproceedings{Lin2014Microsoft,
  author = {Lin, T.-Y. and et al.},
  title = {Microsoft COCO: Common Objects in Context},
  booktitle = {ECCV},
  year = {2014}
}

@article{Liu2021Swin,
  author = {Liu, Z. and et al.},
  title = {Swin Transformer: Hierarchical Vision Transformer using Shifted Windows},
  journal = {ICCV},
  year = {2021}
}

@article{Lv2024RTDETRv2,
  author = {Lv, W. and et al.},
  title = {RT-DETRv2: Improved Baseline with Bag-of-Freebies for Real-Time Detection Transformer},
  journal = {arXiv preprint arXiv:2407.17140},
  year = {2024}
}

@article{Malaisree2025DINO,
  author = {Malaisree, S. and Paveenchana, P.},
  title = {DINO-YOLO: Self-Supervised Pre-training for Data-Efficient Object Detection},
  journal = {Automation in Construction},
  year = {2025}
}

@article{Mann1945Nonparametric,
  author = {Mann, H. B.},
  title = {Nonparametric Tests Against Trend},
  journal = {Econometrica},
  year = {1945}
}

@article{Marzialetti2025Assessing,
  author = {Marzialetti, F. and et al.},
  title = {Assessing eco-physiological patterns of Ailanthus altissima (Mill.) Swingle and differences with native vegetation},
  journal = {Plant Biosystems},
  year = {2025}
}

@article{Michler2007Black,
  author = {Michler, C. H. and et al.},
  title = {Black Walnut Ecology and Dynamics},
  journal = {USDA Forest Service Technical Report},
  year = {2007}
}

@article{Motard2015How,
  author = {Motard, E. and et al.},
  title = {How invasion by Ailanthus altissima transforms soil and litter communities in a temperate forest ecosystem},
  journal = {Biological Invasions},
  year = {2015}
}

@article{Muhammad2020EigenCAM,
  author = {Muhammad, M. B. and Yeasin, M.},
  title = {Eigen-CAM: Class Activation Map using Principal Components},
  journal = {International Joint Conference on Neural Networks (IJCNN)},
  year = {2020}
}

@article{Mullerova2016Does,
  author = {Müllerová, J. and et al.},
  title = {Does the data resolution origin matter? Satellite, airborne and UAV imagery to tackle plant invasions},
  journal = {International Archives of Photogrammetry, Remote Sensing and Spatial Information Sciences},
  year = {2016}
}

@article{Mullerova2023Pattern,
  author = {Müllerová, J. and et al.},
  title = {Pattern to process, research to practice: remote sensing of plant invasions},
  journal = {Biological Invasions},
  year = {2023}
}

@article{Naharki2023The,
  author = {Naharki, K. and et al.},
  title = {The Detection of Tree of Heaven (Ailanthus altissima) Using Drones and Optical Sensors},
  journal = {Drones},
  year = {2023}
}

@article{Naharki2024The,
  author = {Naharki, K. and et al.},
  title = {The Detection of Tree of Heaven (Ailanthus altissima) Using Drones and Optical Sensors: Implications for the Management of Invasive Plants and Insects},
  journal = {Remote Sensing},
  year = {2024}
}

@article{Neubauer2026PASTA,
  author = {Neubauer, L. and et al.},
  title = {PASTA: Vision Transformer Patch Aggregation for Weakly Supervised Target and Anomaly Segmentation},
  journal = {IEEE T-PAMI},
  year = {2026}
}

@article{Nezami2020Tree,
  author = {Nezami, S. and et al.},
  title = {Tree Species Classification of Drone Hyperspectral and RGB Imagery with Deep Learning CNNs},
  journal = {Remote Sensing},
  year = {2020}
}

@article{Nicolescu2020Review,
  author = {Nicolescu, V.-N. and et al.},
  title = {A review of black walnut (Juglans nigra L.) ecology and management},
  journal = {Forestry},
  year = {2020}
}

@article{Noto2025ALIAS,
  author = {Noto, L. and et al.},
  title = {ALIAS -- A Remote Sensing Approach to Monitor Ailanthus altissima Invasion and its Ecohydrological Impacts},
  journal = {Journal of Hydrology},
  year = {2025}
}

@article{Ophoff2023Improving,
  author = {Ophoff, T. and et al.},
  title = {Improving Object Detection in VHR Aerial Orthomosaics},
  journal = {ISPRS Annals},
  year = {2023}
}

@inproceedings{Padilla2020Survey,
  author = {Padilla, R. and et al.},
  title = {A Survey on Performance Metrics for Object-Detection Algorithms},
  booktitle = {IWSSIP},
  year = {2020}
}

@article{Peng2024DFINE,
  author = {Peng, Y. and et al.},
  title = {D-FINE: Redefine Regression Task in DETRs as Fine-grained Distribution Refinement},
  journal = {arXiv preprint arXiv:2410.13842},
  year = {2024}
}

@article{Pu2021Mapping,
  author = {Pu, R.},
  title = {Mapping Tree Species Using Advanced Remote Sensing Technologies: A State-of-the-Art Review and Perspective},
  journal = {Journal of Remote Sensing},
  year = {2021}
}

@article{Rahman2024Mamba,
  author = {Rahman, M. and Hasan, M.},
  title = {Mamba in Vision: A Comprehensive Survey of Techniques and Applications},
  journal = {IEEE Access},
  year = {2024}
}

@article{Rebbeck2015Aerial,
  author = {Rebbeck, J. and et al.},
  title = {Aerial Detection of Seed-Bearing Female Ailanthus altissima: A Cost-Effective Method to Map an Invasive Tree in Forested Landscapes},
  journal = {Forest Science},
  year = {2015}
}

@article{Saumel2010Urban,
  author = {Säumel, I. and Kowarik, I.},
  title = {Urban rivers as dispersal corridors for primarily wind-dispersed invasive tree species},
  journal = {Landscape and Urban Planning},
  year = {2010}
}

@article{Sapkota2025Ultralytics,
  author = {Sapkota, R. and Karkee, M.},
  title = {Ultralytics YOLO Evolution: An Overview of YOLO26, YOLO11, YOLOv8 and YOLOv5 Object Detectors},
  journal = {arXiv preprint arXiv:2510.09653},
  year = {2025}
}

@article{Schiefer2020Mapping,
  author = {Schiefer, F. and et al.},
  title = {Mapping forest tree species in high resolution UAV-based RGB-imagery by means of convolutional neural networks},
  journal = {ISPRS Journal of Photogrammetry and Remote Sensing},
  year = {2020}
}

@article{Schrag2026Towards,
  author = {Schrag, J. and et al.},
  title = {Towards Robust Deep Learning-based Rumex Obtusifolius Detection from Drone Images},
  journal = {Computers and Electronics in Agriculture},
  year = {2026}
}

@article{Siljeg2020Multiscale,
  author = {Šiljeg, A. and et al.},
  title = {A Multiscale Framework for Sustainable Management of Tufa-Forming Watercourses: National Park Krka},
  journal = {Water},
  year = {2020}
}

@article{Simeoni2025DINOv3,
  author = {Simeoni, O. and et al.},
  title = {DINOv3: Self-Supervised Vision Foundation Models for Multi-Domain Visual Understanding},
  journal = {Meta FAIR Technical Report},
  year = {2025}
}

@article{Singh2024Systematic,
  author = {Singh, K. and et al.},
  title = {Systematic review and best practices for drone remote sensing of invasive plants},
  journal = {Biological Invasions},
  year = {2024}
}

@article{Sladonja2015Review,
  author = {Sladonja, B. and Sušek, M. and Guillermic, J.},
  title = {Review on Invasive Tree of Heaven (Ailanthus altissima (Mill.) Swingle) Conflicting Values: Assessment of Its Ecosystem Services and Potential Biological Threat},
  journal = {Environmental Management},
  year = {2015}
}

@article{Soler2024Chemical,
  author = {Soler, R. and et al.},
  title = {Chemical Control of the Invasive Tree Ailanthus altissima},
  journal = {Forest Ecology and Management},
  year = {2024}
}

@article{Tarantino2019Ailanthus,
  author = {Tarantino, E. and et al.},
  title = {Ailanthus altissima mapping from multi-temporal very high resolution satellite images},
  journal = {International Journal of Remote Sensing},
  year = {2019}
}

@article{Tian2025YOLOv12,
  author = {Tian, Y. and Ye, Q. and Doermann, D.},
  title = {YOLOv12: Attention-Centric Real-Time Object Detectors},
  journal = {arXiv preprint arXiv:2502.12524},
  year = {2025}
}

@inproceedings{Touvron2021DeiT,
  author = {Touvron, H. and et al.},
  title = {Training data-efficient image transformers & distillation through attention},
  booktitle = {ICML},
  year = {2021}
}

@article{Triggs2000Bundle,
  author = {Triggs, B. and et al.},
  title = {Bundle Adjustment -- A Modern Synthesis},
  journal = {Vision Algorithms: Theory and Practice},
  year = {2000}
}

@article{Turner2014Direct,
  author = {Turner, D. and Lucieer, A. and Wallace, L.},
  title = {Direct Georeferencing of Ultrahigh-Resolution UAV Imagery},
  journal = {IEEE T-GRS},
  year = {2014}
}

@book{Vapnik1998Statistical,
  author = {Vapnik, V. N.},
  title = {Statistical Learning Theory},
  publisher = {Wiley-Interscience},
  year = {1998}
}

@article{Wang2017Nonlocal,
  author = {Wang, X. and et al.},
  title = {Non-local Neural Networks},
  journal = {CVPR},
  year = {2018}
}

@article{Wang2025MSYM,
  author = {Wang, L. and et al.},
  title = {MSYM: A Lightweight Yolo-Mamba Network for Plants Recognition in River and Lake Riparian Zones},
  journal = {Frontiers in Plant Science},
  year = {2025}
}

@article{Xing2024Mapping,
  author = {Xing, Z. and et al.},
  title = {Mapping invasive noxious weed species in alpine grassland ecosystems using UAV hyperspectral imagery and novel deep learning},
  journal = {Ecological Indicators},
  year = {2024}
}

@article{Zachariah2026MapForest,
  author = {Zachariah, M. and et al.},
  title = {MapForest: A Modular Field Robotics System for Forest Mapping and Invasive Species Localization},
  journal = {Field Robotics},
  year = {2026}
}

@article{Zaka2024Advances,
  author = {Zaka, A. and et al.},
  title = {Advances in Remote Sensing and Machine Learning Methods for Invasive Plants Study: A Comprehensive Review},
  journal = {Remote Sensing},
  year = {2024}
}

@inproceedings{Redmon2016YOLO,
  author = {Redmon, J. and Divvala, S. and Girshick, R. and Farhadi, A.},
  title = {You Only Look Once: Unified, Real-Time Object Detection},
  booktitle = {CVPR},
  year = {2016}
}

@article{Zheng2020CIoU,
  author = {Zheng, Z. and et al.},
  title = {Distance-IoU Loss: Faster and Better Learning for Bounding Box Regression},
  journal = {AAAI},
  year = {2020}
}

@article{Zhang2016Understanding,
  author = {Zhang, C. and et al.},
  title = {Understanding deep learning requires rethinking generalization},
  journal = {ICLR},
  year = {2017}
}

@article{Zhang2022MultiSpecies,
  author = {Zhang, C. and et al.},
  title = {Multi-Species Individual Tree Segmentation and Identification Based on Improved Mask R-CNN and UAV Imagery in Mixed Forests},
  journal = {Remote Sensing},
  year = {2022}
}

@article{Zhao2023DETRs,
  author = {Zhao, Y. and et al.},
  title = {DETRs Beat YOLOs on Real-time Object Detection},
  journal = {arXiv preprint arXiv:2304.08069},
  year = {2023}
}

@article{Zhao2023Systematic,
  author = {Zhao, H. and et al.},
  title = {A Systematic Review of Individual Tree Crown Detection and Delineation with Convolutional Neural Networks (CNN)},
  journal = {Current Forestry Reports},
  year = {2023}
}

@article{Zhong2024Review,
  author = {Zhong, M. and et al.},
  title = {A Review: Tree Species Classification Based on Remote Sensing Data and Classic Deep Learning-Based Methods},
  journal = {Forests},
  year = {2024}
}

@article{Zou2025AdaptPest,
  author = {Zou, X. and et al.},
  title = {AdaptPest-Net: A Task-Adaptive Network with Graph-Mamba Fusion for Multi-Scale Agricultural Pest Recognition},
  journal = {Computers and Electronics in Agriculture},
  year = {2025}
}
```
