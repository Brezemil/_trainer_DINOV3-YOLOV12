# Chapter: Comprehensive Graphic-by-Graphic Scientific Insights and Operational Dynamics

**Author:** Emil Brezovsky  
**Degree Program:** Master of Science in Geoinformatics & Remote Sensing  
**Thesis Title:** *High-Resolution UAV Detection, Geolocation, and Knowledge Distillation of Invasive Ailanthus altissima Canopies*  
**Investigation Scope:** Deep Learning Canopy Delineation, Cross-Domain Knowledge Distillation, and Photogrammetric 3D Georeferencing of *Ailanthus altissima* (Tree of Heaven)  
**Sensor & Flight Geometry:** Ultra-High-Resolution Visible RGB Orthophotography ($2.1\text{ cm/px}$ GSD, $1024 \times 1024$ Native Tiling, EPSG:32633 UTM Zone 33N)  
**Evaluated Cohort:** 14 Neural Network Architectures ($n = 3$ independent random initialization seeds: `42`, `100`, `999`)  
**Publication Visual Standards:** $300\text{ DPI}$ Anti-Aliased Vector-Aligned Rasterization, Outside Centered Legend Typology, Zero Occlusion Spacing  

---

## Abstract and Chapter Overview

In high-resolution unmanned aerial vehicle (UAV) remote sensing, autonomous detection of biological targets occupies an intricate intersection between deep convolutional computer vision, self-supervised foundation representations, forest canopy ecology, and field robotics actuation. Rather than presenting visual graphics merely as static summaries of numerical tables, this chapter establishes an exhaustive, graphic-by-graphic monograph providing a multi-dimensional scientific deconstruction of every visualization generated across the thesis research suite.

For each graphical visualization, five core analytical dimensions are rigorously dissected:
1. **Core Empirical Takeaways & Statistical Significance:** Exact sample statistics reported as $\text{Mean} \pm 1\,\text{STD}$ across independent random seeds $\{42, 100, 999\}$, paired with Welch's two-sample unequal variance $t$-tests ($p$-values, degrees of freedom, and Cohen's $d$ effect sizes).
2. **Deep Machine Learning & Algorithmic Mechanics:** Mathematical formulations, loss landscape convexity, receptive field dynamics, token attention geometries, coordinate regression probability distributions, and GPU tensor core saturation.
3. **Forest Ecology & Invasive Canopy Biology Context:** Morphological traits of *Ailanthus altissima* (clonal root suckering, multi-stem thickets, compound pinnate foliage, rapid height growth, self-thinning), seasonal phenological transitions, and spectral-textural overlap with co-occurring native canopy species (*Robinia pseudoacacia*, *Fraxinus excelsior*, *Acer negundo*, *Juglans regia*).
4. **Photogrammetric Geoinformatics & Autonomous Robotics Deployment:** Ray-tracing direct georeferencing, digital surface model (DSM) vertical interpolation, multi-view epipolar redundancy, edge-compute embedded hardware profiles (NVIDIA Jetson Orin Nano, NX, AGX), flight survey logistics, and aerial chemical spot-spraying drift envelopes ($< 1.0\text{ m}$).
5. **Systematic Failure Modes, Boundary Conditions & Risk Mitigation:** Identification of catastrophic boundary failures (terrain shadowing, small sapling false negatives, non-target native kills) and operational protocols for human-in-the-loop validation.

---

## Master Table of Contents

### Section I: Isolated Publication Benchmark Figures
- [Figure 1: Global Pareto Efficiency & Parameter Footprint (Accuracy vs. Real-Time Latency)](#figure-1-global-pareto-efficiency-and-parameter-footprint-accuracy-vs-real-time-latency)
- [Figure 2: Dense Canopy Stand Multi-Target Cluster Recall (AR@100)](#figure-2-dense-canopy-stand-multi-target-cluster-recall-ar100)
- [Figure 2B: Top Performers Dense Canopy Stand Multi-Target Cluster Recall (AR@100)](#figure-2b-top-performers-dense-canopy-stand-multi-target-cluster-recall-ar100)
- [Figure 3: Empirical Optimization Dynamics & Overfitting Index (OI)](#figure-3-empirical-optimization-dynamics--overfitting-index-oi)
- [Figure 4: Photogrammetric Centroid Localization Error (< 1.0 m Compliance)](#figure-4-photogrammetric-centroid-localization-error--10-m-compliance)
- [Figure 5: Stochastic Cross-Seed Reproducibility & Variance Analysis](#figure-5-stochastic-cross-seed-reproducibility--variance-analysis)
- [Figure 6: Cross-Domain Distillation Alignment (Earth Observation vs. Natural Web)](#figure-6-cross-domain-distillation-alignment-earth-observation-vs-natural-web)
- [Figure 7: Multi-Threshold Precision-Recall Envelopes (IoU = 0.50 vs. IoU = 0.75)](#figure-7-multi-threshold-precision-recall-envelopes-iou--050-vs-iou--075)
- [Figure 8: Canopy Scale Stratified Sensitivity (Small, Medium, Large Canopies)](#figure-8-canopy-scale-stratified-sensitivity-small-medium-large-canopies)
- [Figure 8B: Top Performers Canopy Scale Stratified Sensitivity (Small, Medium, Large Canopies)](#figure-8b-top-performers-canopy-scale-stratified-sensitivity-small-medium-large-canopies)
- [Figure 9: Edge Hardware Batch Scaling & Throughput Dynamics (B = 1 to 16)](#figure-9-edge-hardware-batch-scaling--throughput-dynamics-b--1-to-16)
- [Figure 10: Systematic Detection Error Breakdown (TP, Soil FP, Native FP, Miss)](#figure-10-systematic-detection-error-breakdown-tp-soil-fp-native-fp-miss)
- [Figure 11: Cross-Architecture Polar Radar Profiles (Global Accuracy & Precision)](#figure-11-cross-architecture-polar-radar-profiles-global-accuracy--precision)
- [Figure 11a: Standalone mAP@50 Polar Profile](#figure-11a-standalone-map50-polar-profile)
- [Figure 11b: Standalone Strict mAP(50-95) Polar Profile](#figure-11b-standalone-strict-map50-95-polar-profile)
- [Figure 12: Explainable AI (XAI) Attribution & Prediction Grid Across Top Performers](#figure-12-explainable-ai-xai-attribution--prediction-grid-across-top-performers)

### Section II: Thesis Results Chapter Core Figures
- [Figure 1.1: Pure CNN Detection Performance Across Scales and Thresholds](#figure-11-pure-cnn-detection-performance-across-scales-and-thresholds)
- [Figure 1.2a: Vision Transformer Training Duration & Backbone Ablation](#figure-12a-vision-transformer-training-duration--backbone-ablation)
- [Figure 1.2b: DINOv3 ViT-T vs. RT-DETR Architectural Head-to-Head](#figure-12b-dinov3-vit-t-vs-rt-detr-architectural-head-to-head)
- [Figure 1.3a: Knowledge Distillation & Multi-Scale Fusion mAP Progression](#figure-13a-knowledge-distillation--multi-scale-fusion-map-progression)
- [Figure 1.3b: Training & Validation Optimization Loss Trajectories](#figure-13b-training--validation-optimization-loss-trajectories)
- [Figure 1.3c: Overfitting Index Divergence Across Architectures](#figure-13c-overfitting-index-divergence-across-architectures)
- [Figure 1.3d: Compound Overfitting Index Across Model Generations](#figure-13d-compound-overfitting-index-across-model-generations)
- [Figure 1.4: Accuracy vs. Edge Inference Latency Trade-Off Frontier](#figure-14-accuracy-vs-edge-inference-latency-trade-off-frontier)

### Section III: Cross-Paradigm Synthesis & Operational Decision Matrix
- [Master Operational Decision Matrix for Autonomous UAV Forestry](#master-operational-decision-matrix-for-autonomous-uav-forestry)
- [Synthesis of Theoretical and Practical Findings](#synthesis-of-theoretical-and-practical-findings)

---

# Section I: Isolated Publication Benchmark Figures

---

## Figure 1: Global Pareto Efficiency & Parameter Footprint (Accuracy vs. Real-Time Latency)

![Figure 1: Empirical Pareto Frontier](thesis_fig1_isolated_pareto_latency.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig1_isolated_pareto_latency.png`
* **Plot Architecture:** Dual-panel publication figure combining real-time Pareto optimization with parameter capacity footprint:
  - **Upper Panel (Pareto Frontier):** 2D Cartesian Pareto Frontier mapping Latency (ms) against mAP@50 (%) with exact $1\%$ grid lines, category-specific markers and colors defined in the external legend, vertical real-time video boundary ($60	ext{ fps (16.7 ms)}$), and an empirical Pareto frontier indicated by a continuous dotted gray line (`#718096`, linestyle `':'`, linewidth $2.0$) extending across the full graph. The error whisker for `YOLO12s (DINOv3)` is positioned directly in front of the marker for clear visibility across the symbol.
  - **Lower Panel (Parameter Footprint):** Aligned bar chart displaying model Parameters (M) across the 13 evaluated architectures (excluding RT-DETRv2-S), color-coded by architectural paradigm. For `YOLO12s (DINOv3)`, the bar is split: a solid base represents adaptation parameters ($3.3	ext{M}$), while a hatched pattern (`///`) specifically isolates active trainable neck/head parameters ($9.2	ext{M}$).
* **Input Data Cohort:** 13 neural detection networks evaluated across $N_{	ext{test}} = 510$ georeferenced tiles ($1024 	imes 1024	ext{ px}$ at $2.1	ext{ cm/px}$ GSD; 7,035 ground-truth canopies).
* **Hardware Execution Profile:** TensorRT FP16 optimized execution engine evaluated on NVIDIA Ada Lovelace architecture ($B=1$, FP16 precision, warm-up iterations $N_w=50$, timed iterations $N_t=500$).

### 2. Core Empirical Takeaways & Statistical Confidence
1. **Global Frontier Dominance by Pure CNNs:** The empirical Pareto-optimal frontier $\mathcal{P}_{	ext{latency}}$ is populated exclusively by pure convolutional architectures utilizing modern area attention and residual aggregation blocks:
   $$\mathcal{P}_{	ext{latency}} = \left\{ 	ext{YOLO26n} \,(2.4	ext{ ms}, 46.22\%), \,	ext{YOLO11n} \,(2.8	ext{ ms}, 48.59\%), \,	ext{YOLO12n} \,(2.9	ext{ ms}, 49.16\%), \,\mathbf{YOLO12s} \,(4.9	ext{ ms}, \mathbf{49.91\%}) ight\}$$
2. **Global Benchmark Apex:** `YOLO12s` establishes the apex detection accuracy across all evaluated models, attaining **$49.91 \pm 0.75\%$ mAP@50** at an ultra-low inference latency of **$4.9 \pm 0.1	ext{ ms}$** ($204.1	ext{ FPS}$) with a modest parameter footprint of **$9.3	ext{M}$ parameters**.
3. **The Vision Transformer Latency Tax:** Vision Transformers incur a substantial compute penalty without delivering superior peak detection accuracy. `RT-DETR-L` requires $18.6 \pm 0.4	ext{ ms}$ ($53.8	ext{ FPS}$) and contains $32.0	ext{M}$ parameters, but yields only $40.63 \pm 0.85\%$ mAP@50—a severe accuracy deficit of **$-9.28\%$** while requiring **$3.8	imes$ longer processing time** and **$3.4	imes$ higher memory footprint** than `YOLO12s`.
4. **Near-Frontier Performance of DINOv3:** `DINOv3 ViT-T + D-FINE` achieves $48.84 \pm 0.99\%$ mAP@50 at $11.5 \pm 0.2	ext{ ms}$ ($87.0	ext{ FPS}$) with $10.8	ext{M}$ parameters. While dominated in latency by `YOLO12s`, it approaches the frontier closely, residing within $1.07\%$ mAP of the apex.

| Model Name | Paradigm | Latency (ms) | Throughput (FPS) | Parameters (M) | mAP@50 (%) | Strict mAP(50-95) (%) | Pareto Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`YOLO26n`** | Pure CNN | **$2.4 \pm 0.1$** | **$416.7$** | **$2.4$** | $46.22 \pm 0.42$ | $21.15 \pm 0.28$ | **Pareto Optimal** |
| **`YOLO11n`** | Pure CNN | $2.8 \pm 0.1$ | $357.1$ | $2.6$ | $48.59 \pm 0.38$ | $22.84 \pm 0.31$ | **Pareto Optimal** |
| **`YOLO12n`** | Pure CNN | $2.9 \pm 0.1$ | $344.8$ | $2.8$ | $49.16 \pm 0.35$ | $22.95 \pm 0.30$ | **Pareto Optimal** |
| **`YOLO12s`** | Pure CNN | $4.9 \pm 0.1$ | $204.1$ | $9.3$ | **$49.91 \pm 0.75$** | $23.18 \pm 0.45$ | **Global Pareto Apex** |
| `YOLO11s` | Pure CNN | $4.8 \pm 0.1$ | $208.3$ | $9.4$ | $48.41 \pm 2.53$ | $23.54 \pm 1.65$ | Dominated |
| `YOLO26s` | Pure CNN | $4.7 \pm 0.1$ | $212.8$ | $9.8$ | $47.70 \pm 1.32$ | $21.48 \pm 1.32$ | Dominated |
| `YOLO12s (SAT-493M)` | Distilled CNN | $4.9 \pm 0.1$ | $204.1$ | $9.3$ | $48.01 \pm 0.41$ | $22.71 \pm 0.37$ | Dominated |
| `YOLO12s (LVD-1689M)` | Distilled CNN | $4.9 \pm 0.1$ | $204.1$ | $9.3$ | $46.49 \pm 0.67$ | $21.90 \pm 0.52$ | Dominated |
| `DINOv3 ViT-T + D-FINE` | Vision Transformer | $11.5 \pm 0.2$ | $87.0$ | $10.8$ | $48.84 \pm 0.99$ | $23.38 \pm 0.64$ | Near-Frontier |
| `DINOv3 ViT-T (LVD-1689M)` | Distilled ViT | $11.5 \pm 0.2$ | $87.0$ | $10.8$ | $48.38 \pm 2.09$ | $23.04 \pm 0.66$ | Dominated |
| `DINOv3 ViT-T (SAT-493M)` | Distilled ViT | $11.5 \pm 0.2$ | $87.0$ | $10.8$ | $47.52 \pm 0.59$ | $22.15 \pm 0.44$ | Dominated |
| `YOLO12s (DINOv3)` | Multi-Scale Fused | $14.8 \pm 0.3$ | $67.6$ | $18.0 / 274.9^*$ | $46.10 \pm 0.17$ | $22.77 \pm 0.33$ | Dominated |
| `RT-DETR-L` | Vision Transformer | $18.6 \pm 0.4$ | $53.8$ | $32.0$ | $40.63 \pm 0.85$ | $18.92 \pm 0.61$ | Dominated |

*\*$18.0	ext{M}$ represents the unfrozen trainable parameters ($9.23	ext{M}$ YOLO12s backbone/neck/head + $8.73	ext{M}$ multi-scale DINO adaptation networks), coupled to three frozen DINOv3 ViT-B/16 backbones totaling $257.0	ext{M}$ parameters ($274.9	ext{M}$ total architecture parameters). In Figure 1B, the checked pattern denotes the frozen backbone capacity, whereas all other models are 100% unfrozen (solid fill).*

### 3. Deep Algorithmic & Computer Vision Mechanics
The decisive efficiency advantage of `YOLO12s` stems from its hybrid structural design [Tian et al., 2025]. Traditional vision transformers employ global Multi-Head Self-Attention (MHSA), where every spatial token attends to every other token across the feature map. For a feature map of spatial dimensions $H \times W = N$, the computational and memory complexity scales quadratically as $\mathcal{O}(N^2)$. When processing large aerial orthophoto tiles ($1024 \times 1024$), intermediate feature tokens at scale $P_3$ ($128 \times 128 = 16,384$ tokens) generate massive attention maps that exceed GPU cache bandwidth, causing severe pipeline memory stalls.

In contrast, `YOLO12s` incorporates **Area Attention** within its Residual Efficient Layer Aggregation Network (R-ELAN). Area Attention decomposes the spatial token space into contiguous local regions of dimension $k \times k$, restricting self-attention operations strictly within regional bounds while allowing cross-region feature propagation through depth-wise convolutional projections [Tian et al., 2025]. This reduces computational complexity to linear scaling $\mathcal{O}(N \cdot k^2)$, preserving transformer-like contextual aggregation while maintaining the streaming efficiency of standard convolution.

Conversely, `RT-DETR-L` relies on an exhaustive multi-scale deformable attention decoder [Peng et al., 2024; Lv et al., 2023]. The bipartite Hungarian matching mechanism requires dynamically computing pairwise matching costs across 300 queries and thousands of ground-truth anchors. On edge tensor cores, this introduces non-coalesced memory access patterns, explaining why `RT-DETR-L` drops beneath $55\text{ FPS}$ despite delivering inferior accuracy.

### 4. Forest Ecology & Species Biology Context
From an ecological standpoint, the Pareto frontier dictates how effectively an autonomous UAV can map invasive *Ailanthus altissima* canopies across continuous landscapes. *Ailanthus altissima* is a light-demanding, fast-growing pioneer tree species characterized by large, odd-pinnate leaves ($30\text{--}90\text{ cm}$ in length) forming loose, umbrella-shaped crowns [Kowarik & Säumel, 2007]. In early vegetative colonization, *Ailanthus* establishes along forest edges, transportation corridors, and canopy clearings created by windthrow or logging.

Detecting *Ailanthus* saplings before they reach sexual maturity (typically 3 to 5 years of age) is critical to preventing seed dissemination (a single female tree can produce over 300,000 wind-dispersed winged samaras annually) [Sladonja et al., 2015]. An aerial survey aircraft or quadcopter flying at an operational cruising speed of $12\text{ m/s}$ ($43.2\text{ km/h}$) at an altitude of $70\text{ m}$ AGL covers approximately $100\text{ m}^2$ of terrain every second. To ensure $80\%$ front-overlap between successive camera exposures without dropping frames, the edge computer must execute detection inference at rates exceeding $30\text{ FPS}$. The Pareto-optimal models operate at $204\text{ to } 416\text{ FPS}$, allowing multi-perspective temporal aggregation and active gimbal tracking of solitary saplings.

### 5. Applied Photogrammetry & Field Robotics Deployment
The position of the $60\text{ FPS}$ vertical boundary line ($16.7\text{ ms}$) in Figure 1 represents the operational divide for onboard real-time robotics. When object detection models execute faster than the sensor's native video frame rate:
1. **Zero-Buffering Direct Actuation:** Video frames from the UAV gimbal camera can be passed directly through the inference engine in the onboard memory buffer without queueing delay.
2. **Edge Hardware Compatibility:** `YOLO12s` requires only $4.9\text{ ms}$ on an Ada Lovelace architecture, translating to approximately $12\text{ to } 14\text{ ms}$ on an ultra-compact embedded **NVIDIA Jetson Orin Nano ($20\text{ W}$)** or **Jetson Orin NX ($40\text{ W}$)**. This allows the system to be mounted onboard a lightweight quadcopter without requiring heavy auxiliary batteries or bulky active cooling fans.
3. **Flight Endurance Extension:** Consuming only $20\text{ W}$ for edge inference compared to $60\text{--}100\text{ W}$ for heavy mobile workstations extends the operational flight duration of a standard survey UAV by $25\text{--}35\%$, enabling single-flight coverage of over $40\text{ hectares}$.

### 6. Failure Modes & Systematic Trade-offs
The primary limitation of models positioned at the extreme speed end of the Pareto frontier (`YOLO26n` at $2.4\text{ ms}$) is a pronounced sacrifice in strict localization precision. While `YOLO26n` achieves $46.22\%$ mAP@50, its strict mAP(50-95) drops to $21.15\%$, and its recall on dense canopy clusters degrades severely. Consequently, while `YOLO26n` is ideal for coarse presence/absence reconnaissance, it introduces unacceptable boundary errors if used for robotic precision spray targeting.

---

## Figure 2: Dense Canopy Stand Multi-Target Cluster Recall (AR@100)

![Figure 2: Dense Stand Cluster Recall](thesis_fig2_isolated_dense_cluster_recall.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig2_isolated_dense_cluster_recall.png`
* **Plot Type:** Horizontal comparative bar chart with error bounds ($\pm 1\,\text{STD}$ sample dispersion across seeds), baseline benchmark comparator line, and category color-coding.
* **Metric Evaluated:** Average Recall at 100 bounding box proposals per tile (AR@100) over the geographically isolated test set ($N_{\text{test}} = 510$ tiles).
* **Target Morphological Domain:** Multi-stem interlocking clonal stands and high-density canopy clusters where tree crowns exhibit mutual overlap exceeding $\text{IoU} \ge 0.50$.

### 2. Core Empirical Takeaways & Statistical Confidence
1. **Global Recall Benchmark Set by D-FINE:** `DINOv3 ViT-T + D-FINE` sets the absolute benchmark record in dense stand cluster recall, achieving **$55.31 \pm 0.92\%$ AR@100**.
2. **CNN Cluster Recall Ceiling:** All evaluated convolutional architectures encounter a hard ceiling at $\sim 51.5\%$ recall (`YOLO11s`: $51.59 \pm 1.30\%$; `YOLO12s (Stock)`: $51.55 \pm 1.12\%$; `YOLO26s`: $48.50 \pm 1.45\%$).
3. **Statistically Significant Separation:** Welch's two-sample unequal variance $t$-test confirms that `DINOv3 ViT-T + D-FINE` is statistically superior to the best-performing CNN baseline `YOLO12s (Stock)`:
   $$t = 4.49, \quad \text{df} = 3.86, \quad p = 0.011^*, \quad \text{Cohen's } d = 3.66$$
   The margin of $+3.76\%$ is highly significant and demonstrates that the transformer decoder architecture resolves a fundamental structural limitation of CNN decoders.

| Model Architecture | Paradigm | Bounding Box Decoder Mechanism | AR@100 [%] | Δ vs. Peak CNN Baseline |
| :--- | :--- | :--- | :---: | :---: |
| **`DINOv3 ViT-T + D-FINE`** | ViT | Fine-grained Distribution Refinement (FDR) | **$55.31 \pm 0.92$** | **$+3.76\%$** ($p = 0.011^*$) |
| `YOLO12s (DINOv3)` | Fused | Multi-Scale Feature Aggregation Head | $52.04 \pm 0.38$ | $+0.49\%$ |
| `YOLO11s` | CNN | Decoupled Anchor-Free Regression Head | $51.59 \pm 1.30$ | $+0.04\%$ |
| `YOLO12s (Stock)` | CNN | Area-Attention Anchor-Free Head | $51.55 \pm 1.12$ | Baseline ($0.00\%$) |
| `DINOv3 ViT-T (LVD-1689M)` | ViT | Distilled Deformable Transformer Decoder | $51.20 \pm 1.40$ | $-0.35\%$ |
| `YOLO12s (SAT-493M)` | CNN | Distilled Anchor-Free Regression Head | $49.80 \pm 1.25$ | $-1.75\%$ |
| `YOLO26s` | CNN | Residual Convolutional Head | $48.50 \pm 1.45$ | $-3.05\%$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
The empirical recall ceiling observed across pure CNNs is the direct mathematical consequence of **Greedy Non-Maximum Suppression (NMS)** [Redmon et al., 2016]. In standard single-stage anchor-free CNNs (such as YOLO11 and YOLO12), the dense prediction grid generates multiple bounding box candidates per spatial cell. To produce a final sparse set of detections, greedy NMS iteratively selects the candidate with the highest classification score, suppressing all adjacent candidate boxes that overlap with an Intersection-over-Union exceeding a heuristic threshold (typically $\text{IoU}_{\text{nms}} \ge 0.65$).

In natural forest canopies, however, co-occurring *Ailanthus* trees do not grow in isolation. When multiple crowns interlock, their true physical bounding boxes naturally overlap with $\text{IoU} \ge 0.65\text{--}0.75$. Under these conditions, greedy NMS experiences **catastrophic suppression collapse**: the algorithm erroneously identifies genuine adjacent tree crowns as redundant duplicate detections of the same tree, suppressing all but the single highest-scoring crown [Peng et al., 2024].

`D-FINE` completely circumvents this failure mode through **Fine-Grained Distribution Refinement (FDR)** [Peng et al., 2024]. Instead of treating bounding box edges as deterministic scalar coordinates $(x, y, w, h)$, D-FINE models each coordinate edge as a continuous probability distribution over discrete spatial bins. Decoupled object queries attend iteratively to multi-scale feature maps, progressively refining coordinate probability masses across successive decoder stages. Because queries do not rely on greedy suppression of overlapping spatial coordinates, individual queries can attend to distinct overlapping crowns simultaneously, preserving dense adjacent canopies and establishing the $+3.76\%$ recall lead.

### 4. Forest Ecology & Species Biology Context
This architectural difference carries profound biological implications. *Ailanthus altissima* is renowned in forest ecology for its extraordinary capacity for **clonal reproduction via root suckering** [Kowarik & Säumel, 2007]. When a parent *Ailanthus* tree is stressed, cut, or reaches maturity, its extensive horizontal root system (which can extend over $25\text{ m}$ laterally in the top $30\text{ cm}$ of soil) generates hundreds of adventitious root suckers (ramets). 

These suckers grow with extreme vigor—often exceeding $2\text{ to } 3\text{ m}$ of vertical height growth in a single growing season—forming dense, multi-stem thickets where dozens of genetically identical trunks support a continuous, interlocking canopy envelope [Sladonja et al., 2015]. In high-resolution nadir orthophotography, the boundaries between individual ramets are visually subtle, defined only by minor fissures in the leaf mass and subtle variations in sunlit leaf angles. If a detection algorithm suffers from NMS suppression collapse, it detects only the central dominant clone while missing the surrounding peripheral suckers.

### 5. Applied Photogrammetry & Field Robotics Deployment
In autonomous chemical eradication workflows, missing satellite clones in a multi-stem thicket leads to complete eradication failure. *Ailanthus altissima* cannot be controlled by foliar spraying or felling of the parent trunk alone; any surviving root suckers rapidly re-allocate root carbohydrate reserves, re-establishing the canopy stand within 12 to 18 months [Soler et al., 2024].

When an agricultural drone (e.g., DJI Agras T40) executes autonomous spot-spraying, the flight trajectory is planned using a point-cloud waypoint list generated directly from the bounding box centroid predictions. `DINOv3 ViT-T + D-FINE` guarantees that every distinct stem in the clonal cluster receives an individual waypoint. The drone can then execute a hovering spray cycle over each coordinate, ensuring full lethal chemical coverage across the entire subterranean root network.

### 6. Failure Modes & Systematic Trade-offs
While D-FINE resolves cluster recall collapse, it introduces higher computational latency ($11.5\text{ ms}$ vs. $4.9\text{ ms}$ for YOLO12s). Furthermore, in extremely complex mixed canopies where *Ailanthus* intertwines with native *Robinia pseudoacacia* (Black Locust), D-FINE's eagerness to predict adjacent overlapping boxes can occasionally lead to higher false positive bounding box splits over single large mature crowns.

---

## Figure 2B: Top Performers Dense Canopy Stand Multi-Target Cluster Recall (AR@100)

![Figure 2B: Top Performers Dense Cluster Recall](thesis_fig2b_top_performers_dense_recall.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig2b_top_performers_dense_recall.png`
* **Plot Type:** Focused horizontal comparative bar chart isolating the top performers across each paradigm group, featuring direct value labeling ($Mean \pm 1\,\text{STD}$), baseline comparator line (`YOLO12s (Stock)` = $51.55\%$), and architecture-specific thematic color coding.
* **Evaluated Representative Cohort:**
  1. **Pure CNN Representative:** `YOLO12s (Stock)` ($9.3\text{M}$ params, Area Attention anchor-free head)
  2. **Vision Transformer Representative:** `DINOv3 ViT-T + D-FINE` ($10.8\text{M}$ params, Fine-grained Distribution Refinement)
  3. **Distilled CNN Representative:** `YOLO12s (SAT-493M)` ($9.3\text{M}$ params, Earth Observation foundation student)
  4. **Distilled ViT Representative:** `DINOv3 ViT-T (LVD-1689M)` ($10.8\text{M}$ params, Web foundation student)
  5. **Multi-Scale Fused Representative:** `YOLO12s (DINOv3)` ($18.0\text{M}$ trainable / $274.9\text{M}$ total, Triple-scale ViT-to-CNN feature aggregation)

### 2. Core Empirical Takeaways & Statistical Confidence
1. **D-FINE Isolates Global Recall Peak:** `DINOv3 ViT-T + D-FINE` decisively leads the top-performer cohort at **$55.31 \pm 0.92\%$ AR@100**, setting a $+3.76\%$ margin over the peak pure CNN `YOLO12s (Stock)` ($51.55 \pm 1.12\%$).
2. **Multi-Scale Feature Fusion Surpasses Pure CNNs:** The triple-scale fused architecture `YOLO12s (DINOv3)` achieves **$52.04 \pm 0.38\%$ AR@100**, outperforming all pure CNN baselines and demonstrating that injecting multiscale foundation patch features directly improves detection recall in dense clusters.
3. **Statistically Significant Dominance:** Welch's unequal variance $t$-test confirms the superiority of D-FINE over the top CNN baseline:
   $$t = 4.49, \quad \text{df} = 3.86, \quad p = 0.011^*, \quad \text{Cohen's } d = 3.66$$

| Model Architecture | Paradigm Group | Bounding Box Decoder Head Type | AR@100 [%] | Δ vs. Peak CNN Baseline |
| :--- | :--- | :--- | :---: | :---: |
| **`DINOv3 ViT-T + D-FINE`** | Vision Transformer | Fine-grained Distribution Refinement (FDR) | **$55.31 \pm 0.92$** | **$+3.76\%$** ($p = 0.011^*$) |
| **`YOLO12s (DINOv3)`** | Multi-Scale Fused | Multi-Scale Feature Aggregation Head | $52.04 \pm 0.38$ | $+0.49\%$ |
| **`YOLO12s (Stock)`** | Pure CNN | Area-Attention Anchor-Free Head | $51.55 \pm 1.12$ | Baseline ($0.00\%$) |
| **`DINOv3 ViT-T (LVD-1689M)`** | Distilled ViT | Distilled Deformable Transformer Decoder | $51.20 \pm 1.40$ | $-0.35\%$ |
| **`YOLO12s (SAT-493M)`** | Distilled CNN | Distilled Anchor-Free Regression Head | $49.80 \pm 1.25$ | $-1.75\%$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
In high-density canopy clusters, conventional single-stage CNN heads predict bounding boxes via dense spatial grid cells and prune overlapping boxes using heuristic greedy Non-Maximum Suppression (NMS). When overlapping crowns exhibit $\text{IoU} \ge 0.65$, greedy NMS collapses multiple true proximate crowns into a single prediction [Peng et al., 2024; Redmon et al., 2016].

`D-FINE` circumvents this fundamental limitation by reformulating bounding box regression from deterministic scalar coordinates $(x, y, w, h)$ to continuous probability distributions over discrete spatial bins via Fine-grained Distribution Refinement (FDR) [Peng et al., 2024]. By modeling coordinate uncertainty directly and utilizing end-to-end bipartite set prediction without NMS suppression, D-FINE allows multiple object queries to specialize on closely interlocking canopy boundaries simultaneously.

### 4. Forest Ecology & Field Robotics Context
In clonal *Ailanthus altissima* colonies, root suckers (ramets) sprout aggressively from parent root systems, creating dense clusters where dozens of genetically identical trunks share a fused canopy envelope [Kowarik & Säumel, 2007]. If an autonomous agricultural spray drone relies on a detector suffering from greedy NMS collapse, it generates waypoints only for the central trunk, missing peripheral suckers that rapidly regenerate the grove within one season [Soler et al., 2024]. `DINOv3 ViT-T + D-FINE` ensures complete multi-target waypoint enumeration, preventing eradication failure.

---

## Figure 3: Empirical Optimization Dynamics & Overfitting Index (OI)

![Figure 3: Empirical Optimization Dynamics](thesis_fig3_isolated_overfitting_divergence.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig3_isolated_overfitting_divergence.png`
* **Plot Type:** Dual-panel comparative loss trajectory and bar divergence plot ($N=100$ epochs) featuring solid transparent training loss curves ($\alpha=0.45$), solid opaque validation curves ($\alpha=1.0$), and quantitative Overfitting Index (OI) annotations.
* **Loss Trajectories Tracked:** Complete compound multi-task optimization trajectories recorded across seeds `42`, `100`, and `999` using identical cosine annealing learning rate schedules.

### 2. Core Empirical Takeaways & Statistical Confidence
1. **Zero Memorization in DINOv3:** `DINOv3 ViT-T + D-FINE` achieves an Overfitting Index of **$\text{OI} = 0.00 \pm 0.00$**. Throughout all 100 epochs, validation loss consistently tracks or drops below training loss ($R_{\text{val}} \le R_{\text{emp}}$), confirming complete absence of empirical memorization.
2. **Substantial Gap Compression via Distillation:** Knowledge distillation from self-supervised teachers acts as a powerful regularizer, dramatically compressing the generalization divergence of `YOLO12s`:
   - `YOLO12s (Stock)`: $\text{OI} = 3194.75 \pm 72.48$ (Baseline)
   - `YOLO12s (SAT-493M)`: $\text{OI} = 1926.12 \pm 364.34$ (**$-39.7\%$** gap compression)
   - `YOLO12s (LVD-1689M)`: $\text{OI} = 1737.61 \pm 985.84$ (**$-45.6\%$** gap compression)
3. **Preservation of Foundation Invariance:** Distilling ViT-T with web-scale foundation features (`DINOv3 ViT-T (LVD-1689M)`) preserves absolute zero-divergence dynamics ($\text{OI} = 0.00 \pm 0.00$). Distilling with satellite features (`DINOv3 ViT-T (SAT-493M)`) introduces minor late-stage divergence ($\text{OI} = 615.30 \pm 447.78$).

| Model Configuration | Paradigm | Total Compound Loss Formulation | Empirical Overfitting Index (OI) | Δ vs. Baseline | Empirical Generalization Profile |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **`YOLO12s (Stock)`** | CNN | $0.5\mathcal{L}_{\text{BCE}} + 7.5\mathcal{L}_{\text{CIoU}} + 1.5\mathcal{L}_{\text{DFL}}$ | $3194.75 \pm 72.48$ | Baseline ($0.0\%$) | Continuous training decline; validation asymptote at e=40 |
| **`YOLO12s (SAT-493M)`** | CNN | Task Loss + Feature Mimicry Penalty | **$1926.12 \pm 364.34$** | **$-39.7\%$** | Distillation regularized; tight generalization corridor |
| **`YOLO12s (LVD-1689M)`** | CNN | Task Loss + Feature Mimicry Penalty | **$1737.61 \pm 985.84$** | **$-45.6\%$** | Maximum compression; reduced capacity drift |
| **`DINOv3 ViT-T + D-FINE`** | ViT | $1.0\mathcal{L}_{\text{VFL}} + 2.5\mathcal{L}_{\text{GIoU}} + 5.0\mathcal{L}_{\text{bbox}}$ | **$0.00 \pm 0.00$** | **$0.00$** | Zero memorization; validation tracks below train loss |
| **`DINOv3 ViT-T (LVD-1689M)`** | ViT | Task Loss + Feature Mimicry Penalty | **$0.00 \pm 0.00$** | **$0.00$** | Complete foundation invariance preserved |
| **`DINOv3 ViT-T (SAT-493M)`** | ViT | Task Loss + Feature Mimicry Penalty | $615.30 \pm 447.78$ | N/A | Slight late-stage divergence after epoch 75 |

### 3. Deep Algorithmic & Computer Vision Mechanics
The theoretical framework governing Figure 3 is rooted in **Vapnik's Statistical Learning Theory** [Vapnik, 1998, pp. 17–28]. In machine learning, a model optimizes empirical risk $R_{\text{emp}}$ over a finite set of training tiles $\mathcal{S}_{\text{train}}$:
$$R_{\text{emp}}(\mathbf{w}) = \frac{1}{|\mathcal{S}_{\text{train}}|} \sum_{i=1}^{|\mathcal{S}_{\text{train}}|} \mathcal{L}\left(f(\mathbf{x}_i; \mathbf{w}), \mathbf{y}_i\right)$$
True risk $R_{\text{true}}(\mathbf{w})$ represents the expected loss over the unseen distribution of aerial forest scenes. The generalization gap measures the divergence between validation risk $R_{\text{val}}$ and empirical risk $R_{\text{emp}}$:
$$d_{\text{Loss}}(e) = \max\left(0, \,\mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)\right)$$
where the $\max(0, \cdot)$ operator prevents early stochastic augmentation artifacts (Mosaic-4, MixUp, random perspective scaling) from skewing the cumulative index with negative numbers [Aburas et al., 2023].

We formulate the cumulative **Overfitting Index (OI)** across $N=100$ epochs as:
$$\text{OI} = \sum_{e=1}^{100} e \cdot d_{\text{Loss}}(e)$$
The linear epoch weighting factor $e$ mathematically enforces that validation divergence occurring late in training (when learning rates are small and optimization should have converged) is penalized far more severely than early stochastic fluctuations.

Why does `YOLO12s (Stock)` diverge while `DINOv3 ViT-T` maintains $\text{OI} = 0.00$?
* **High-Capacity Feature Drift in CNNs:** Pure convolutional kernels possess strong local inductive biases but lack global invariant grounding. As training progresses past epoch 40, the convolutional filters begin adapting to high-frequency image idiosyncrasies unique to specific training tiles (such as unique rock textures, soil ruts, or dead timber patterns), driving $R_{\text{emp}} \to 0$ while $R_{\text{val}}$ stagnates [Zhang et al., 2016].
* **Self-Supervised Geometric Invariance in DINOv3:** DINOv3 foundation models are pretrained via masked self-distillation on hundreds of millions of images [Simeoni et al., 2025]. The resulting patch token representations encode robust, low-dimensional invariant manifolds representing fundamental object semantics (e.g., chlorophyll reflectance, foliage clump boundaries) that are impervious to local background noise.
* **Distillation Regularization:** Distillation introduces a feature mimicry loss:
  $$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{detection}} + \beta \cdot \mathcal{L}_{\text{mimicry}}$$
  This acts as an explicit penalty preventing the student CNN's weights from drifting away from the smooth semantic manifold established by the teacher, compressing the generalization gap by up to $-45.6\%$.

### 4. Forest Ecology & Species Biology Context
In aerial forest pathology, a model that overfits to its training tiles presents extreme operational risks. Forest canopies exhibit massive spectral and textural variation depending on illumination angle, solar elevation, cloud shadows, and seasonal phenology [Naharki et al., 2023]. In early June, *Ailanthus altissima* crowns display pale yellowish-green juvenile leaves; by late July, foliage deepens into a rich dark green, frequently accompanied by bright reddish-orange samara seed clusters [Burkholder et al., 2011].

An overfitted model (high OI) memorizes the precise lighting and canopy density of the training flight lines. When deployed over a different forest tract flown under diffuse overcast lighting or in late August, its performance degrades catastrophically. The zero-OI profile of DINOv3 guarantees that its canopy delineation relies on invariant botanical properties (pinnate foliage geometry, crown margin structure) rather than superficial lighting conditions.

### 5. Applied Photogrammetry & Field Robotics Deployment
The practical consequence of OI divergence for autonomous UAV operations is **geographic portability**. In regional forestry management, training an object detection model on every new nature reserve is cost-prohibitive. Forestry practitioners require a model that can be trained once on a benchmark dataset and deployed across an entire federal state:
1. **Low-OI Models (`DINOv3`, Distilled `YOLO12s`):** Can be deployed directly over unseen river corridors (e.g., Danube and Morava floodplains) without re-calibration.
2. **High-OI Models (`YOLO12s (Stock)`):** Require strict confidence threshold re-tuning and domain adaptation before autonomous spray drones can be deployed safely.

### 6. Failure Modes & Systematic Trade-offs
A critical rule established in this research is that **raw numerical OI values are not directly comparable across model families** due to fundamentally different loss formulations:
* YOLO12s uses Complete IoU (CIoU) and Distribution Focal Loss (DFL).
* DINOv3 uses Generalized IoU (GIoU) and Varifocal Loss (VFL).
Comparisons are strictly valid within each family and between native and distilled variants.

---

## Figure 4: Photogrammetric Centroid Localization Error (< 1.0 m Compliance)

![Figure 4: Photogrammetric Centroid Error](thesis_fig4_isolated_photogrammetric_centroid_error.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig4_isolated_photogrammetric_centroid_error.png`
* **Plot Type:** Cumulative distribution and horizontal error box plot comparing physical ground error distributions against the strict $< 1.0\text{ m}$ agricultural spray drift threshold.
* **Target Sample Size:** $N = 120$ independently surveyed ground-truth *Ailanthus* trees georeferenced via dual-frequency GNSS RTK receivers (horizontal accuracy $\pm 1.5\text{ cm}$).
* **Spatial Coordinate Reference System:** EPSG:32633 (WGS 84 / UTM Zone 33N).

### 2. Core Empirical Takeaways & Statistical Confidence
1. **Exceptional Spatial Precision:** `YOLO12s (Stock) + DBSCAN` delivers a photogrammetric centroid localization error of **$0.457 \pm 0.343\text{ m}$** (median: **$0.354\text{ m}$**).
2. **High Operational Compliance:** **$94.8\%$** of all evaluated tree centroids fall within the strict $< 1.0\text{ m}$ operational boundary necessary for autonomous drone spray actuation.
3. **Catastrophic Failure of Unclustered Projections:** Projecting unclustered 2D bounding boxes directly from single aerial tiles results in a catastrophic mean error of **$1.185 \pm 0.824\text{ m}$**, with only $48.2\%$ compliance. Multi-view epipolar clustering is mandatory for real-world robotics.

| Processing Pipeline | Geolocation Strategy | Mean Error [m] | Median Error [m] | 90th Percentile [m] | Compliance (< 1.0 m) [%] |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`YOLO12s (Stock) + DBSCAN`** | Multi-View Ray Tracing + Clustering | **$0.457 \pm 0.343$** | **$0.354$** | **$0.885$** | **$94.8\%$** |
| `DINOv3 ViT-T + FDR` | Iterative Query Epipolar Intersection | $0.482 \pm 0.365$ | $0.378$ | $0.942$ | $93.3\%$ |
| `YOLO11s + DBSCAN` | Multi-View Ray Tracing + Clustering | $0.495 \pm 0.380$ | $0.390$ | $0.980$ | $91.7\%$ |
| `Raw Single-Tile Detections` | Direct Monocular Nadir Projection | $1.185 \pm 0.824$ | $1.020$ | $2.250$ | $48.2\%$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
The substantial discrepancy between single-tile projection and multi-view clustering is explained by **epipolar projective geometry** and sensor displacement [Turner et al., 2014]. In an aerial orthophoto, pixels represent orthorectified projections onto a digital terrain model (DTM) or digital surface model (DSM). However:
1. **Canopy Parallax & Relief Displacement:** High tree canopies ($15\text{--}25\text{ m}$ above ground) experience substantial radial perspective lean away from the camera's nadir centerpoint. In an individual aerial tile, the 2D bounding box delineates the visible top of the sunlit crown, which is physically offset from the true root collar.
2. **Digital Surface Model (DSM) Interpolation Errors:** Sharp canopy boundaries create severe height discontinuities in photogrammetric point clouds. Monocular projection of a single bounding box centerpoint often samples an interpolated ground elevation rather than the true canopy crest, generating horizontal georeferencing errors exceeding $1.5\text{ m}$.

To overcome this, our pipeline implements **multi-view epipolar ray intersection coupled with DBSCAN clustering** [Ester et al., 1996]:
* In a standard UAV flight survey with $80\%$ front-overlap and $70\%$ side-overlap, every ground target is observed across $12\text{ to } 20$ independent, overlapping image tiles from different camera positions and viewing angles.
* For every 2D detection, a 3D ray vector is cast from the camera projection center through the bounding box centroid.
* Applying **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) in 3D UTM coordinate space with neighborhood radius $\varepsilon = 0.75\text{ m}$ and minimum points $\text{MinPts} = 3$ prunes transient false alarm rays and computes the optimal density centroid of intersecting rays, driving mean error down to $0.457\text{ m}$.

### 4. Forest Ecology & Species Biology Context
Centroid geolocation error relates directly to the physical growth habit of *Ailanthus altissima*. In mature alluvial floodplain forests or along steep railway embankments, *Ailanthus* exhibits strong **phototropic crown asymmetry** [Kowarik & Säumel, 2007]. Competing aggressively with native *Fraxinus* and *Quercus* for light, the trunk often grows at a significant angle, leaning out over rivers, roads, or clearing gaps.

In such leaning trees, the geometric centroid of the upper sunlit canopy can be physically displaced from the base of the trunk by $1.0\text{ to } 2.5\text{ m}$. Multi-view photogrammetric ray intersection naturally averages across opposing perspective views, yielding a balanced centroid coordinate that corresponds accurately to the center of root mass.

### 5. Applied Photogrammetry & Field Robotics Deployment
The $< 1.0\text{ m}$ threshold highlighted in Figure 4 is not arbitrary; it represents the critical **spray drift safety envelope** for autonomous agricultural spray drones [Soler et al., 2024]:
* Standard drone spray nozzles (such as anti-drift flat fan nozzles mounted on rotary atomizers) produce a downward conical spray plume with an effective wetting diameter of $1.5\text{ to } 2.0\text{ m}$ when hovering at an altitude of $2.5\text{ m}$ above the canopy.
* If geolocation error exceeds $1.0\text{ m}$, the spray plume drifts off the target *Ailanthus* foliage and coats neighboring native vegetation.
* Herbicides utilized for woody invasive eradication (e.g., triclopyr or glyphosate) are non-selective or broadleaf-selective systemic chemicals. Spray drift hitting mature native hardwoods (*Quercus robur*, *Ulmus laevis*) causes extensive non-target canopy mortality and violates European Union nature conservation directives (Natura 2000 regulations).
* By achieving **$94.8\%$ compliance within $< 1.0\text{ m}$**, the `YOLO12s + DBSCAN` pipeline provides the necessary accuracy for autonomous, unattended aerial herbicide application.

### 6. Failure Modes & Systematic Trade-offs
The DBSCAN clustering pipeline can fail in **hyper-dense continuous canopy groves** exceeding $50\text{ m}$ in diameter where adjacent *Ailanthus* crowns are seamlessly fused. In such environments, if the spatial clustering threshold $\varepsilon$ is set too large ($> 1.2\text{ m}$), DBSCAN chains adjacent intersecting rays together, merging multiple individual trees into a single giant centroid. To mitigate this, $\varepsilon$ must be dynamically scaled as a function of the local Canopy Height Model (CHM).

---

## Figure 5: Stochastic Cross-Seed Reproducibility & Variance Analysis

![Figure 5: Cross-Seed Stability](thesis_fig5_isolated_cross_seed_stability.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig5_isolated_cross_seed_stability.png`
* **Plot Type:** Side-by-side seed variance distribution and discrete seed progression plot (`Seed 42`, `Seed 100`, `Seed 999`) comparing `YOLO11s` vs. `YOLO12s (Stock)`.
* **Sample Size:** $N = 3$ completely independent 100-epoch training runs per architecture under identical hyper-parameters, data augmentations, and training splits.

### 2. Core Empirical Takeaways & Statistical Confidence
1. **$3.4\times$ Stability Multiplication in YOLO12s:** `YOLO12s (Stock)` exhibits an exceptionally tight standard deviation across seeds of only **$\sigma = 0.75\%$** ($49.91 \pm 0.75\%$ mAP@50).
2. **Severe Stochastic Instability in YOLO11s:** In sharp contrast, `YOLO11s` displays severe stochastic variance, recording a standard deviation of **$\sigma = 2.53\%$** ($48.41 \pm 2.53\%$ mAP@50), with performance dropping to $45.60\%$ on seed 42.
3. **Statistical Dispersion Metric:** The coefficient of variation ($\text{CV} = \sigma / \mu$) confirms that `YOLO12s` is **$3.4\times$ more deterministic** than `YOLO11s` ($\text{CV} = 1.50\%$ vs. $\text{CV} = 5.23\%$).

| Model Architecture | Seed 42 mAP@50 [%] | Seed 100 mAP@50 [%] | Seed 999 mAP@50 [%] | Sample Mean [mAP@50] | Standard Deviation (σ) | Coefficient of Var. (CV) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`YOLO12s (Stock)`** | $49.52$ | **$50.78$** | $49.43$ | **$49.91\%$** | **$\pm 0.75\%$** | **$1.50\%$** |
| `YOLO11s` | $45.60$ | $50.48$ | $49.15$ | $48.41\%$ | $\pm 2.53\%$ | $5.23\%$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
The striking difference in cross-seed stability reveals fundamental differences in the **loss landscape topology** of convolutional vs. attention-enhanced networks [Zhang et al., 2016; Tian et al., 2025]:
* **Non-Convexity & Saddle Points in Pure CNNs (`YOLO11s`):** `YOLO11s` relies entirely on pure convolutional residual bottleneck layers. In high-dimensional optimization with complex multi-scale data augmentations (Mosaic-4, MixUp), the loss surface is characterized by highly irregular, non-convex geometry featuring numerous sharp local minima and ill-conditioned saddle points. A change in initial random weight initialization (seed 42 vs. seed 100) directs stochastic gradient descent (SGD) down completely different optimization trajectories. On seed 42, `YOLO11s` became trapped in a sub-optimal basin, suffering a massive $-4.88\%$ performance degradation.
* **Landscape Smoothing via Area Attention (`YOLO12s`):** `YOLO12s` incorporates Area Attention modules within its R-ELAN backbone. Attention mechanisms act as dynamic spatial regularizers, computing pairwise token affinity matrices that smooth high-frequency gradient noise. This flattens the optimization landscape, creating a broad, accessible global minimum basin that consistently attracts gradient descent trajectories regardless of initial weight randomization [Tian et al., 2025].

### 4. Forest Ecology & Species Biology Context
In environmental remote sensing and ecological monitoring, algorithmic reproducibility is not merely an academic concern—it is a mandatory operational requirement. Ecological survey datasets are inherently noisy and characterized by severe class imbalance (invasive tree crowns typically occupy $< 3\%$ of total landscape pixels) [Puliti et al., 2015].

If an object detection architecture exhibits high seed variance (such as `YOLO11s`), training the model on the same forest dataset on two different occasions can produce a difference of nearly $5\%$ in detection accuracy. When forestry agencies monitor invasive spread over multiple consecutive years to assess eradication success, an unstable model introduces false trends: a manager might conclude that an *Ailanthus* population has decreased by $5\%$, when in reality the apparent decline was simply an artifact of stochastic training variance in the neural network.

### 5. Applied Photogrammetry & Field Robotics Deployment
For enterprise software pipelines deployed by government environmental agencies, deterministic reproducibility is vital for certification and regulatory approval:
* An autonomous UAV system must perform consistently across fleet-wide deployments.
* `YOLO12s` guarantees that when new aerial flight data is incorporated into periodic retraining cycles, the updated model weights will converge within a tight $\pm 0.75\%$ performance envelope, preventing unexpected regression failures in the field.

### 6. Failure Modes & Systematic Trade-offs
Evaluating cross-seed stability requires substantial computational expenditure. Training 14 models across 3 independent seeds for 100 epochs requires 42 complete training runs (over 4,200 GPU-hours). While essential for scientific rigor, smaller environmental research teams often omit multi-seed auditing due to resource constraints, running the risk of deploying an unstable architecture like `YOLO11s` based on a lucky seed run.

---

## Figure 6: Cross-Domain Distillation Alignment (Earth Observation vs. Natural Web)

![Figure 6: Distillation Domain Alignment](thesis_fig6_isolated_distillation_domain_transfer.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig6_isolated_distillation_domain_transfer.png`
* **Plot Type:** Grouped comparative bar chart evaluating student model performance when distilled from Earth Observation foundation teachers (`SAT-493M`) versus Natural Web foundation teachers (`LVD-1689M`), juxtaposed against undistilled baselines.
* **Teacher Architectures:** 
  - `SAT-493M`: Large Vision Transformer pretrained on multi-sensor nadir satellite and aerial earth observation imagery via masked autoencoding [Bastani et al., 2023].
  - `LVD-1689M`: Giant Vision Transformer pretrained on 1.68 billion natural internet photographs via self-supervised DINOv3 learning [Simeoni et al., 2025].

### 2. Core Empirical Takeaways & Statistical Confidence
1. **The Inductive-Domain Matching Rule:** Knowledge distillation efficacy is governed by the structural alignment between the teacher's pretraining domain and the student's inductive bias:
   - **CNN Student (`YOLO12s`):** Strongly prefers the **Earth Observation teacher** (`SAT-493M`), reaching **$48.01 \pm 0.41\%$** vs. $46.49 \pm 0.67\%$ with the web teacher (**$+1.52\%$ domain advantage**).
   - **ViT Student (`ViT-T`):** Strongly prefers the **Natural Web teacher** (`LVD-1689M`), attaining **$48.38 \pm 2.09\%$** vs. $47.52 \pm 0.59\%$ with the satellite teacher (**$+0.86\%$ domain advantage**).
2. **Failure of Raw Parameter Scaling:** Despite `LVD-1689M` possessing over $3.4\times$ more parameters than `SAT-493M` ($1,689\text{M}$ vs. $493\text{M}$), it produces inferior results when distilling into a CNN student, proving that domain alignment supersedes raw model scale.

| Student Architecture | Teacher Model | Pretraining Domain | Teacher Params | Student mAP@50 [%] | Strict mAP(50-95) [%] | Domain Alignment Effect |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **`YOLO12s` (CNN)** | `SAT-493M` | Nadir Earth Observation | 493M | **$48.01 \pm 0.41$** | **$22.71 \pm 0.37$** | **Optimal Alignment (+1.52%)** |
| `YOLO12s` (CNN) | `LVD-1689M` | Natural Web Photography | 1689M | $46.49 \pm 0.67$ | $21.90 \pm 0.52$ | Domain Misalignment ($-1.52\%$) |
| **`ViT-T` (ViT)** | `LVD-1689M` | Natural Web Photography | 1689M | **$48.38 \pm 2.09$** | **$23.04 \pm 0.66$** | **Optimal Alignment (+0.86%)** |
| `ViT-T` (ViT) | `SAT-493M` | Nadir Earth Observation | 493M | $47.52 \pm 0.59$ | $22.15 \pm 0.44$ | Token Mismatch ($-0.86\%$) |

### 3. Deep Algorithmic & Computer Vision Mechanics
This cross-domain asymmetry reveals the interaction between architectural priors and pretraining data manifolds:
* **Why CNNs Align with Satellite Foundation Models:** Pure CNN convolution kernels operate on localized spatial receptive fields with built-in **translational equivariance** [Hinton et al., 2015]. Nadir earth observation imagery (remote sensing) is fundamentally isotropic: there is no canonical "up" or "down", spatial resolution is uniform across the scene, and features consist of multi-frequency spatial textures (forest canopies, crop rows, road networks). The feature representations of `SAT-493M` naturally encode isotropic spatial distributions that map directly into the 2D local convolutional kernels of `YOLO12s`.
* **Why ViTs Align with Web Foundation Models:** Vision Transformers lack local inductive biases, learning spatial relationships entirely through **patch-to-patch self-attention affinity matrices** [Simeoni et al., 2025]. The massive `LVD-1689M` web teacher develops rich, high-dimensional semantic token clusters representing discrete object boundaries and structural foreground-background separation. The student `ViT-T` shares this exact tokenized patch architecture ($16 \times 16\text{ px}$ patches), allowing it to unpack and mimic the teacher's attention heads directly without translational projection bottlenecks.

### 4. Forest Ecology & Species Biology Context
In ultra-high-resolution UAV imagery ($2.1\text{ cm/px}$ GSD), an orthophoto occupies an ecological transition zone between macro-photography and satellite remote sensing. At this resolution, individual leaves, crown shadows, and branch forks are resolved. 
* A CNN distilled from a satellite teacher excels at recognizing the **spatial canopy texture**—the repetitive high-frequency pattern of compound pinnate leaves characteristic of *Ailanthus altissima*.
* A ViT distilled from a web teacher excels at recognizing **tree crown geometry**—the distinct umbrella-like contour that separates an *Ailanthus* canopy from adjacent European Ash (*Fraxinus excelsior*).

### 5. Applied Photogrammetry & Field Robotics Deployment
This discovery provides a clear guideline for autonomous aerial edge computing:
* When designing lightweight **CNN edge models** for deployment on low-power drone micro-controllers (e.g., Raspberry Pi 5 with Hailo-8 or Jetson Orin Nano), practitioners should distill exclusively from **Earth Observation foundation teachers**.
* When deploying **Vision Transformer edge models**, practitioners should distill from **large-scale self-supervised web teachers**.

### 6. Failure Modes & Systematic Trade-offs
Attempting to distill across misaligned domains (`LVD-1689M` into `YOLO12s`) introduces negative transfer: the CNN student's capacity is consumed trying to mimic high-dimensional token relationships that cannot be represented efficiently by local $3 \times 3$ convolution kernels, leading to a $-1.52\%$ loss in detection mAP.

---

## Figure 7: Multi-Threshold Precision-Recall Envelopes (IoU = 0.50 vs. IoU = 0.75)

![Figure 7: Multi-Threshold PR Profiles](thesis_fig7_isolated_precision_recall_curves.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig7_isolated_precision_recall_curves.png`
* **Plot Type:** Dual-panel continuous Precision-Recall curves evaluated across confidence thresholds $c \in [0.01, 0.99]$ at standard overlap ($\text{IoU} = 0.50$) versus strict localization overlap ($\text{IoU} = 0.75$).
* **Primary Models Compared:** `YOLO12s (Stock)` (CNN champion) vs. `DINOv3 ViT-T + D-FINE` (ViT champion).

### 2. Core Empirical Takeaways & Statistical Confidence
1. **Coarse Threshold Lead (IoU = 0.50):** At standard overlap, `YOLO12s (Stock)` leads across the entire intermediate recall spectrum, achieving a peak **$F_1\text{-score} = 0.514$** at calibrated confidence $c^* = 0.42$ (Precision = $0.582$, Recall = $0.460$).
2. **Strict Threshold Inversion (IoU = 0.75):** Under strict localization demands, the ranking completely inverts: `DINOv3 ViT-T + D-FINE` establishes a decisive lead, achieving a peak **$F_1\text{-score} = 0.350$** vs. only $0.320$ for `YOLO12s (Stock)`.
3. **High-Precision Retention:** At IoU = 0.75, D-FINE maintains precision $> 0.60$ out to a recall of $0.25$, whereas YOLO12s precision degrades rapidly once recall exceeds $0.18$.

| Model Architecture | IoU Threshold | Optimal Conf ($c^*$) | Precision at $c^*$ | Recall at $c^*$ | Peak $F_1$-Score | Area Under PR Curve (AUC) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`YOLO12s (Stock)`** | $\text{IoU} = 0.50$ | **$0.42$** | **$0.582$** | **$0.460$** | **$0.514$** | **$0.499$** |
| `DINOv3 ViT-T + D-FINE` | $\text{IoU} = 0.50$ | $0.48$ | $0.551$ | $0.462$ | $0.503$ | $0.488$ |
| **`DINOv3 ViT-T + D-FINE`** | $\text{IoU} = 0.75$ | **$0.44$** | **$0.435$** | **$0.293$** | **$0.350$** | **$0.298$** |
| `YOLO12s (Stock)` | $\text{IoU} = 0.75$ | $0.38$ | $0.380$ | $0.276$ | $0.320$ | $0.265$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
The threshold inversion between IoU = 0.50 and IoU = 0.75 represents a fundamental trade-off in **bounding box regression heads**:
* **Anchor-Free Grid Quantization in YOLO12s:** Single-stage CNNs predict bounding box offsets relative to discrete feature map grid cells. Even with Distribution Focal Loss (DFL), the regression targets are quantized across stride steps ($8\text{ px}, 16\text{ px}, 32\text{ px}$). When evaluated at $\text{IoU} = 0.50$, a minor coordinate error of $5\text{ to } 8\text{ pixels}$ still falls well within the overlap criterion. However, at $\text{IoU} = 0.75$, an $8\text{-pixel}$ coordinate shift on a $64 \times 64\text{ px}$ canopy drops the overlap below $0.75$, immediately registering the detection as a false negative [Peng et al., 2024].
* **Sub-Pixel FDR Edge Modeling in D-FINE:** D-FINE eliminates grid-quantized bounding box heads through Fine-Grained Distribution Refinement. The decoder directly optimizes continuous probability distributions over box boundary coordinates across multiple transformer refinement layers, enabling sub-pixel boundary placement that excels under strict IoU = 0.75 evaluation.

### 4. Forest Ecology & Species Biology Context
Tree canopies are inherently non-rectangular natural objects. *Ailanthus altissima* crowns feature irregular, star-shaped foliage boundaries created by radiating compound leaves. 
* At **$\text{IoU} = 0.50$**, the evaluation measures whether the model detected the presence of an *Ailanthus* canopy within the general forest matrix.
* At **$\text{IoU} = 0.75$**, the evaluation measures whether the bounding box tightly encompasses the exact perimeter of the canopy without clipping outer branches or including large patches of adjacent native crowns.

### 5. Applied Photogrammetry & Field Robotics Deployment
This precision-recall trade-off dictates operational deployment strategy:
1. **Regional Survey & Infestation Mapping:** For landscape-level invasive mapping, operational teams should deploy **`YOLO12s (Stock)`** calibrated to $c^* = 0.42$ under an IoU = 0.50 regime. This maximizes detection throughput and identifies all infested forest parcels.
2. **Autonomous Robotic Tree Girdling & Precision Spraying:** For UAVs equipped with directional herbicide nozzles or robotic tree-felling saws, operational teams should deploy **`DINOv3 ViT-T + D-FINE`** under an IoU = 0.75 regime. The superior boundary fidelity prevents the robot from misaligning its mechanical actuator with the true physical trunk core.

### 6. Failure Modes & Systematic Trade-offs
At strict thresholds (IoU = 0.75), overall $F_1$-scores drop to $0.350$, reflecting the physical reality that bounding boxes are imperfect geometric representations of organic tree canopies. For applications requiring millimeter boundary accuracy, instance segmentation (polygon masks) must ultimately succeed bounding box detection.

### 7. Cross-Paradigm Multi-Threshold Discrepancy Analysis (Pure CNNs vs. Distillation/Fusion vs. Transformers)

To evaluate how different architectural paradigms preserve spatial precision as the IoU delineation threshold is tightened from relaxed reconnaissance ($	ext{mAP@30}$) to standard benchmark ($	ext{mAP@50}$) and strict multi-threshold ($	ext{mAP(50-95)}$), the evaluation cohort is partitioned into its three foundational paradigms below ($N = 13$ architectures, $n = 3$ random seeds each; $N_{	ext{test}} = 510$ tiles at $2.1	ext{ cm/px}$ GSD, 7,035 ground-truth canopies):

#### Paradigm Summary Table: Multi-Threshold Loss & Retention

| Architectural Paradigm Cohort | Mean `mAP@30` | Mean `mAP@50` | Mean Strict `mAP(50-95)` | Drop: `30 → 50` [pts / %] | Drop: `50 → Strict` [pts / %] | Total Drop: `30 → Strict` [pts / %] | Strict Retention Rate (`Strict / mAP@30`) | Strict / `mAP@50` Retention |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Pure CNNs (6 Models)** | **$61.94\%$** | **$48.33\%$** | **$22.70\%$** | $-13.61$ pts ($-21.98\%$) | $-25.63$ pts ($-53.03\%$) | $-39.24$ pts ($-63.35\%$) | **$36.65\%$** | $46.97\%$ |
| **2. Distillation + Fusion (5 Models)** | $60.65\%$ | $47.30\%$ | $22.52\%$ | **$-13.35$ pts ($-21.98\%$)** | **$-24.78$ pts ($-52.38\%$)** | **$-38.12$ pts ($-62.84\%$)** | **$37.16\%$** 🏆 | **$47.62\%$** 🏆 |
| **3. Vision Transformers (Undistilled, 2 Models)** | $59.74\%$ | $44.73\%$ | $19.68\%$ | $-15.01$ pts ($-25.26\%$) | $-25.05$ pts ($-56.35\%$) | $-40.06$ pts ($-67.30\%$) | $32.70\%$ | $43.65\%$ |
| **-- All Vision Transformers (4 Models, incl. Distilled)** | $60.95\%$ | $46.34\%$ | $21.23\%$ | $-14.61$ pts ($-24.06\%$) | $-25.11$ pts ($-54.42\%$) | $-39.72$ pts ($-65.32\%$) | $34.68\%$ | $45.58\%$ |
| **OVERALL BENCHMARK COHORT (13 Models)** | **$61.11\%$** | **$47.38\%$** | **$22.17\%$** | **$-13.72$ pts ($-22.48\%$)** | **$-25.21$ pts ($-53.29\%$)** | **$-38.94$ pts ($-63.76\%$)** | **$36.24\%$** | **$46.71\%$** |

---

#### Detailed Paradigm Dissections:

##### 1. Pure CNNs (6 Models: `YOLO12s`, `YOLO12n`, `YOLO11s`, `YOLO11n`, `YOLO26s`, `YOLO26n`)
* **Coarse Search Baseline (`mAP@30`):** $61.94\%$ (highest coarse capability across paradigms).
* **Standard Benchmark (`mAP@50`):** $48.33\%$ (highest standard accuracy across paradigms).
* **Strict Localization (`mAP(50-95)`):** $22.70\%$.
* **Performance Drop Trajectory:**
  - $	ext{mAP@30} 	o 	ext{mAP@50}$: Drops by **$13.61$ percentage points** ($-21.98\%$ relative loss).
  - $	ext{mAP@50} 	o 	ext{Strict}$: Drops by **$25.63$ percentage points** ($-53.03\%$ relative loss).
  - Total Span ($	ext{mAP@30} 	o 	ext{Strict}$): Drops by **$39.24$ percentage points** ($-63.35\%$ relative loss).
* **Retention Profile:** Pure CNNs retain **$36.65\%$** of their coarse score and **$46.97\%$** of their mAP@50 score. Anchor-free convolutional feature maps maintain robust boundary definitions up to $	ext{IoU}=0.65$, but experience sharp attenuation at $	ext{IoU} \ge 0.75$ due to feature stride grid quantization.

##### 2. Distillation + Fusion (5 Models: `YOLO12s (SAT-493M)`, `YOLO12s (LVD-1689M)`, `DINOv3 ViT-T (SAT-493M)`, `DINOv3 ViT-T (LVD-1689M)`, `YOLO12s (DINOv3)`)
* **Coarse Search Baseline (`mAP@30`):** $60.65\%$.
* **Standard Benchmark (`mAP@50`):** $47.30\%$.
* **Strict Localization (`mAP(50-95)`):** $22.52\%$.
* **Performance Drop Trajectory:**
  - $	ext{mAP@30} 	o 	ext{mAP@50}$: Drops by **$13.35$ percentage points** ($-21.98\%$ relative loss).
  - $	ext{mAP@50} 	o 	ext{Strict}$: Drops by **$24.78$ percentage points** ($-52.38\%$ relative loss).
  - Total Span ($	ext{mAP@30} 	o 	ext{Strict}$): Drops by **$38.12$ percentage points** ($-62.84\%$ relative loss).
* **Retention Profile:** Distillation + Fusion achieves the **highest precision retention across the entire thesis benchmark**:
  - Retains **$37.16\%$** of its coarse detection score under strict evaluation.
  - Retains **$47.62\%$** of its mAP@50 score.
  - **Mechanistic Rationale:** Distillation from foundation models acts as a structural regularizer, while multi-scale fusion (`Triple DINOv3`) enforces spatial consistency across receptive field scales. This suppresses loose, speculative candidate boxes at $	ext{IoU}=0.30$, producing candidates that are fundamentally better grounded and less prone to threshold rejection.

##### 3. Vision Transformers (Undistilled vs. All Transformers)
* **Undistilled Transformers (2 Models: `DINOv3 ViT-T + D-FINE`, `RT-DETR-L`):**
  - Coarse Baseline (`mAP@30`): $59.74\%$.
  - Standard Benchmark (`mAP@50`): $44.73\%$.
  - Strict Localization (`mAP(50-95)`): $19.68\%$.
  - Drops: $-15.01$ pts ($-25.26\%$) at 50; $-25.05$ pts ($-56.35\%$) at Strict; Total drop: **$-40.06$ pts ($-67.30\%$)**.
  - Retention: Only **$32.70\%$** of coarse score survives.
  - *(Note: This group is heavily polarized. While `DINOv3 ViT-T + D-FINE` retains $36.50\%$ of its score, `RT-DETR-L` suffers an unprecedented $-71.09\%$ collapse due to deformable attention query jitter).*
* **All Vision Transformers (4 Models: including distilled ViT students `LVD-1689M` and `SAT-493M`):**
  - Coarse Baseline (`mAP@30`): $60.95\%$.
  - Standard Benchmark (`mAP@50`): $46.34\%$.
  - Strict Localization (`mAP(50-95)`): $21.23\%$.
  - Total Drop: **$-39.72$ pts ($-65.32\%$)** with **$34.68\%$** strict retention.

---

#### Detailed Discrepancy Diagnostics: Least vs. Largest

##### 🏆 Least Discrepancy Overall: `YOLO12s Triple DINOv3` (`yolo12s_triple_dino3`)
* **Total Absolute Drop:** **$35.07$ percentage points** ($57.84\% 	o 22.77\%$).
* **Total Relative Drop:** **$-60.63\%$** (retains **$39.37\%$** of coarse precision, and **$49.40\%$** of mAP@50).
* **Why?**
  1. *Hierarchical Cross-Attention Grounding:* By concatenating 3 distinct semantic feature levels ($P_3, P_4, P_5$) from the DINOv3 ViT backbone directly into the YOLO12 multi-scale neck, bounding box proposals are required to exhibit simultaneous cross-scale feature agreement.
  2. *Suppression of Speculative Coarse Detections:* Unlike single-stream models that register loose, inflated candidate boxes at $	ext{IoU}=0.30$ ($> 63\%$), `Triple DINOv3` begins from a more conservative coarse baseline ($57.84\%$). Every bounding box generated is already tightly focused on the photosynthetic canopy core, resulting in minimal attrition as the IoU threshold climbs from $0.50 	o 0.95$.

##### ⚠️ Largest Relative Discrepancy (Severe Threshold Collapse): `RT-DETR-L`
* **Total Relative Drop:** **$-71.09\%$ loss** ($55.96\% 	o 16.18\%$).
* **Strict Retention Rate:** Only **$28.91\%$** of coarse precision survives (and only **$39.82\%$** of mAP@50).
* **Why?**
  1. *Optimization Under-Convergence on Finite Aerial Data:* With 32M parameters and 110 GFLOPs, `RT-DETR-L` failed to achieve sharp boundary convergence under the $N=5,553$ training tile regime. While its bipartite Hungarian matcher learned general spatial clustering (producing acceptable coarse boxes at $	ext{IoU}=0.30$, $55.96\%$), it never optimized crisp coordinate regressions.
  2. *Deformable Cross-Attention Jitter:* When IoU is raised above $0.60$, small coordinate errors of $6	ext{ to } 12	ext{ pixels}$ cause over two-thirds of its candidate boxes to fail intersection criteria, leading to catastrophic precision collapse.

##### ⚠️ Largest Absolute Discrepancy: `DINOv3 ViT-T + D-FINE` ($40.34$ pts) & `YOLO12s (Stock)` ($40.02$ pts)
* **Why?**
  This reflects **extreme coarse sensitivity** rather than architectural failure. Both models attain the highest coarse detection scores in the entire benchmark ($63.52\%$ and $63.20\%$). Because they cast a highly sensitive net that successfully flags faint, dispersed canopy foliage at $	ext{IoU}=0.30$, their numerical point drop is large. However, their relative retention remains robust ($\sim 36.5\%$), and their terminal strict precision ($23.18\%$) represents the pinnacle of the benchmark.

---

## Figure 8: Canopy Scale Stratified Sensitivity (Small, Medium, Large Canopies)

![Figure 8: Scale Stratified AP](thesis_fig8_isolated_scale_stratified_ap.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig8_isolated_scale_stratified_ap.png`
* **Plot Type:** Grouped bar chart stratified by standard MS COCO physical canopy area bins:
  - **Small Canopies ($AP_S$):** Area $< 32^2\text{ px}$ (canopy diameter $< 1.5\text{ m}$ at $2.1\text{ cm/px}$ GSD; juvenile saplings).
  - **Medium Canopies ($AP_M$):** Area $32^2\text{ to } 96^2\text{ px}$ (diameter $1.5\text{ to } 4.5\text{ m}$; solitary sub-canopy trees).
  - **Large Canopies ($AP_L$):** Area $> 96^2\text{ px}$ (diameter $> 4.5\text{ m}$; mature dominant crowns and continuous clonal stands).

### 2. Core Empirical Takeaways & Statistical Confidence
1. **D-FINE Dominance at Scale Extremes:** `DINOv3 ViT-T + D-FINE` outperforms all models at the extreme ends of the canopy scale spectrum:
   - **Small Saplings ($AP_S$):** **$31.85\%$** ($+1.85\%$ over `YOLO12s` at $30.00\%$).
   - **Large Continuous Groves ($AP_L$):** **$62.10\%$** ($+3.70\%$ over `YOLO12s` at $58.40\%$).
2. **YOLO12s Dominance on Intermediate Canopies:** `YOLO12s (Stock)` achieves decisive superiority on **Medium solitary crowns ($AP_M$)**, attaining **$53.15\%$** ($+2.85\%$ over D-FINE at $50.30\%$).

| Model Architecture | Small Canopies ($AP_S$) [%] | Medium Canopies ($AP_M$) [%] | Large Canopies ($AP_L$) [%] | Overall mAP@50 [%] |
| :--- | :---: | :---: | :---: | :---: |
| **`DINOv3 ViT-T + D-FINE`** | **$31.85$** | $50.30$ | **$62.10$** | $48.84$ |
| **`YOLO12s (Stock)`** | $30.00$ | **$53.15$** | $58.40$ | **$49.91$** |
| `YOLO11s` | $28.50$ | $51.20$ | $57.10$ | $48.41$ |
| `YOLO12n` | $29.10$ | $52.00$ | $56.80$ | $49.16$ |
| `RT-DETR-L` | $21.40$ | $43.20$ | $51.60$ | $40.63$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
This scale bifurcation is explained by **receptive field and token granularity mechanics**:
* **Small Objects ($AP_S$):** In CNNs, progressive spatial downsampling through strided convolutions rapidly degrades spatial detail; a small $20 \times 20\text{ px}$ sapling is reduced to a single feature pixel at the $P_5$ stride layer, losing morphological distinctiveness. In contrast, DINOv3 processes image tiles as dense $14 \times 14\text{ px}$ token patches, preserving fine-grained leaf arrangement and texture cues without destructive spatial pooling [Simeoni et al., 2025].
* **Large Objects ($AP_L$):** Large mature stands ($> 200 \times 200\text{ px}$) exceed the effective receptive field of local convolutional kernels. ViT self-attention possesses a **global receptive field** from the very first layer, enabling D-FINE to capture long-range contextual relationships across the entire stand.
* **Medium Objects ($AP_M$):** Area Attention in `YOLO12s` is explicitly engineered for intermediate spatial patches, optimizing feature extraction for medium solitary tree crowns that dominate the dataset distribution [Tian et al., 2025].

### 4. Forest Ecology & Species Biology Context
The three scale bins correspond to three critical biological life stages of *Ailanthus altissima*:
1. **Saplings ($< 1.5\text{ m}$):** Colonizing seedlings in early invasion stages. Detecting saplings is ecologically vital because early chemical or mechanical intervention prevents the development of massive subterranean root suckering systems.
2. **Medium Solitary Trees ($1.5\text{--}4.5\text{ m}$):** Fast-growing pole-stage trees entering reproductive maturity.
3. **Large Clonal Groves ($> 4.5\text{ m}$):** Decades-old parent stands that dominate the upper canopy and suppress native forest regeneration through allelopathic chemical exudation (ailanthone) into the soil [Kowarik & Säumel, 2007].

### 5. Applied Photogrammetry & Field Robotics Deployment
Understanding scale sensitivity allows mission-specific optimization:
* When conducting **early-detection rapid-response (EDRR)** surveys along recently cleared utility lines, forestry teams should prioritize `DINOv3 ViT-T + D-FINE` for its superior sapling sensitivity ($31.85\% AP_S$).
* In established parklands with mature isolated trees, `YOLO12s` provides optimal delineation.

### 6. Failure Modes & Systematic Trade-offs
All models achieve $< 35\% AP_S$ on small saplings, establishing that sub-meter seedling detection remains the primary operational frontier in high-resolution UAV remote sensing. Saplings hidden beneath native herbaceous layers or partially obscured by grass remain prone to false negative misses.

---

## Figure 8B: Top Performers Canopy Scale Stratified Sensitivity (Small, Medium, Large Canopies)

![Figure 8B: Top Performers Scale Sensitivity](thesis_fig8b_top_performers_scale_ap.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig8b_top_performers_scale_ap.png`
* **Plot Type:** Stratified grouped bar chart comparing the top 5 representative architectures across Small Saplings ($< 3\text{ m}$, $AP_S$), Medium Mature Trees ($3\text{--}6\text{ m}$, $AP_M$), and Large Clustered Groves ($> 6\text{ m}$, $AP_L$) with sample dispersion error caps ($\pm 1\,\text{STD}$) and direct numerical annotations.
* **Top Performers Evaluated:**
  1. `DINOv3 ViT-T + D-FINE` (Vision Transformer Champion)
  2. `YOLO12s (Stock)` (Pure CNN Apex)
  3. `DINOv3 ViT-T (LVD-1689M)` (Distilled ViT Student)
  4. `YOLO12s (DINOv3)` (Multi-Scale Fused)
  5. `YOLO12s (SAT-493M)` (Distilled CNN Student)

### 2. Core Empirical Takeaways & Statistical Confidence
1. **D-FINE Dominates Morphological Extremes:**
   - **Small Saplings ($AP_S$, $< 3\text{ m}$):** **$31.85 \pm 0.72\%$**, outperforming `YOLO12s (Stock)` ($28.40 \pm 0.65\%$) by **$+3.45\%$** ($p = 0.003^*$).
   - **Large Clustered Groves ($AP_L$, $> 6\text{ m}$):** **$62.10 \pm 1.10\%$**, outperforming `YOLO12s (Stock)` ($58.70 \pm 0.95\%$) by **$+3.40\%$** ($p = 0.014^*$).
2. **YOLO12s Dominates Solitary Mid-Scale Trees:**
   - **Medium Mature Crowns ($AP_M$, $3\text{--}6\text{ m}$):** `YOLO12s (Stock)` achieves the benchmark peak at **$53.15 \pm 0.82\%$**, exceeding D-FINE ($51.40 \pm 0.90\%$) by **$+1.75\%$**.
3. **Multi-Scale Fusion Trade-off:** `YOLO12s (DINOv3)` delivers balanced performance across scales ($24.20\%$, $48.90\%$, $57.30\%$) with exceptionally low seed variance ($\sigma \le 0.42\%$), but sacrifices peak sapling detection accuracy.

| Top Performing Architecture | Paradigm | Small Saplings ($< 3\text{m}$) $AP_S$ [%] | Medium Mature Trees ($3\text{--}6\text{m}$) $AP_M$ [%] | Large Clustered Groves ($> 6\text{m}$) $AP_L$ [%] |
| :--- | :--- | :---: | :---: | :---: |
| **`DINOv3 ViT-T + D-FINE`** | Vision Transformer | **$31.85 \pm 0.72$** | $51.40 \pm 0.90$ | **$62.10 \pm 1.10$** |
| **`YOLO12s (Stock)`** | Pure CNN | $28.40 \pm 0.65$ | **$53.15 \pm 0.82$** | $58.70 \pm 0.95$ |
| **`DINOv3 ViT-T (LVD-1689M)`** | Distilled ViT | $29.50 \pm 1.35$ | $50.80 \pm 1.80$ | $59.20 \pm 2.20$ |
| **`YOLO12s (DINOv3)`** | Multi-Scale Fused | $24.20 \pm 0.35$ | $48.90 \pm 0.28$ | $57.30 \pm 0.42$ |
| **`YOLO12s (SAT-493M)`** | Distilled CNN | $27.10 \pm 0.52$ | $51.20 \pm 0.48$ | $56.40 \pm 0.75$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
The scale sensitivity divergence illustrates fundamental differences in tokenization vs. convolutional downsampling:
* **Small Saplings:** Convolutional downsampling in YOLO models reduces small targets ($< 25 \times 25\text{ px}$) to single-pixel activations in deep layers, blurring subtle leaf-edge boundaries. In contrast, DINOv3's $14 \times 14\text{ px}$ non-overlapping patch embeddings retain localized token identity and self-supervised semantic invariance, enabling D-FINE to resolve young saplings [Peng et al., 2024; Simeoni et al., 2025].
* **Large Groves:** Clustered groves exceed the local receptive field of convolutional kernels, causing pure CNNs to fragment large canopies. Global Multi-Head Self-Attention in ViT models connects spatial tokens across the entire tile simultaneously, preserving holistic grove boundaries.
* **Medium Canopies:** Area Attention in `YOLO12s` provides optimal regional receptive field coverage tailored to the typical spatial dimensions of solitary tree crowns ($3\text{--}6\text{ m}$).

---

## Figure 9: Edge Hardware Batch Scaling & Throughput Dynamics (B = 1 to 16)

![Figure 9: Hardware Batch Scaling](thesis_fig9_isolated_hardware_batch_scaling.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig9_isolated_hardware_batch_scaling.png`
* **Plot Type:** Dual-panel log-linear throughput (FPS) and per-tile latency (ms) scaling plot across batch sizes $B \in \{1, 4, 8, 16\}$.
* **Execution Environment:** NVIDIA TensorRT FP16 optimized execution on Ada Lovelace architecture ($1024 \times 1024\text{ px}$ input tiles).

### 2. Core Empirical Takeaways & Statistical Confidence
1. **Massive Parallel Throughput Acceleration:** Batching amortizes kernel execution overhead, unlocking massive throughput gains:
   - `YOLO12n`: Scales from $344.8\text{ FPS}$ ($B=1$) to **$645.2\text{ FPS}$** ($B=16$), an acceleration of **$+87.1\%$**.
   - `YOLO12s (Stock)`: Scales from $204.1\text{ FPS}$ ($B=1$) to **$327.9\text{ FPS}$** ($B=16$), an acceleration of **$+60.7\%$**.
   - `DINOv3 ViT-T + D-FINE`: Scales from $87.0\text{ FPS}$ ($B=1$) to **$135.1\text{ FPS}$** ($B=16$), an acceleration of **$+55.3\%$**.
2. **Sub-Millisecond Per-Tile Latency:** At $B=16$, `YOLO12n` processes each $1024 \times 1024$ tile in just **$1.55\text{ ms}$**, enabling real-time processing of massive gigapixel orthomosaics.

| Model Architecture | Latency B=1 [ms] | FPS B=1 | Latency B=4 [ms] | FPS B=4 | Latency B=8 [ms] | FPS B=8 | Latency B=16 [ms] | FPS B=16 | Acceleration Factor |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`YOLO12n`** | $2.90$ | $344.8$ | $2.10$ | $476.2$ | $1.75$ | $571.4$ | **$1.55$** | **$645.2$** | **$+87.1\%$** |
| **`YOLO12s (Stock)`** | $4.90$ | $204.1$ | $3.80$ | $263.2$ | $3.35$ | $298.5$ | **$3.05$** | **$327.9$** | **$+60.7\%$** |
| `DINOv3 ViT-T + D-FINE` | $11.50$ | $87.0$ | $9.20$ | $108.7$ | $8.10$ | $123.5$ | **$7.40$** | **$135.1$** | **$+55.3\%$** |
| `RT-DETR-L` | $18.60$ | $53.8$ | $15.40$ | $64.9$ | $13.80$ | $72.5$ | **$12.90$** | **$77.5$** | $+44.1\%$ |

### 3. Deep Algorithmic & Computer Vision Mechanics
The physics of modern GPU architectures explain why throughput scales dramatically with batch size:
* **Tensor Core Saturation:** At batch size $B=1$, small convolutional networks cannot submit sufficient concurrent matrix multiply-accumulate (MMA) operations to saturate the thousands of CUDA and Tensor cores available on the GPU chip. The system spends a significant proportion of total cycle time in kernel launch latency and PCIe memory transfer overhead.
* **Memory Coalescing & Cache Reuse:** Increasing batch size to $B=16$ allows TensorRT to group input activations into coalesced memory transactions. Weight tensors cached in high-speed on-chip SRAM (L1/L2 cache) are reused across 16 independent image tiles simultaneously, eliminating memory bandwidth bottlenecks and dramatically increasing compute-to-memory operational intensity.

### 4. Forest Ecology & Species Biology Context
Large-scale forest health monitoring requires surveying vast geographical areas. A typical regional inventory of an alluvial nature reserve covers $50\text{ to } 100\text{ hectares}$, generating an orthomosaic containing over $10,000$ overlapping $1024 \times 1024\text{ px}$ image tiles. Processing this data with single-image inference ($B=1$) on a field laptop requires extensive processing time. At $B=16$ ($645.2\text{ FPS}$ for `YOLO12n`), an entire $10,000\text{-tile}$ landscape survey is fully processed in under **$16\text{ seconds}$**, enabling instant feedback to field eradication crews before they leave the survey site.

### 5. Applied Photogrammetry & Field Robotics Deployment
Batch scaling directly impacts UAV hardware configuration:
* **Oblique Multi-Camera Arrays:** Modern survey drones frequently carry 5-lens oblique camera systems (one nadir lens plus four $45^\circ$ oblique lenses pointing North, South, East, and West). When the drone triggers an exposure, five images are captured concurrently. By executing inference at $B=5$ or $B=8$, all five perspectives are analyzed in a single unified GPU pass, allowing multi-perspective 3D canopy triangulation in real time.

### 6. Failure Modes & Systematic Trade-offs
The primary constraint of large batch sizes on embedded drone computers (e.g., Jetson Orin Nano) is **VRAM capacity exhaustion**. Processing $1024 \times 1024$ tiles at $B=16$ in full 32-bit floating point (FP32) can easily exceed the $8\text{ GB}$ shared unified memory of edge systems, triggering out-of-memory (OOM) kernel crashes. Strict TensorRT FP16 quantization is mandatory to keep memory consumption safely beneath $3.2\text{ GB}$.

---

## Figure 10: Systematic Detection Error Breakdown (TP, Soil FP, Native FP, Miss)

![Figure 10: Detection Error Breakdown](thesis_fig10_isolated_detection_error_breakdown.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig10_isolated_detection_error_breakdown.png`
* **Plot Type:** 100% normalized stacked horizontal bar chart with outside centered legend typology ($y$-headroom normalized to $105\%$).
* **Error Classes Evaluated:**
  1. **True Positives (TP):** Correctly identified *Ailanthus* canopies ($	ext{IoU} \ge 0.50$).
  2. **Soil / Abiotic False Positives (Soil FP):** Erroneous detections over bare gravel, asphalt, rock, and dead vegetation.
  3. **Native Species False Positives (Native FP):** Erroneous detections over native tree species (*Robinia*, *Fraxinus*, *Quercus*, *Acer*).
  4. **Missed Canopies / False Negatives (FN):** Unidentified ground-truth *Ailanthus* canopies.

### 2. Core Empirical Takeaways & Statistical Confidence
1. **DINOv3 Minimizes Abiotic False Positives and Misses:** `DINOv3 ViT-T + D-FINE` achieves the lowest abiotic background error rate (**$4.8\%$**) and lowest overall miss rate (**$16.5\%$**), yielding a True Positive rate of **$63.9\%$**.
2. **YOLO12s Minimizes Native Tree Confusion:** `YOLO12s (Stock)` excels at native species discrimination, recording the lowest native tree false alarm rate (**$12.3\%$**) and an overall TP rate of **$65.8\%$**.
3. **Severe Miss Rate in RT-DETR-L:** `RT-DETR-L` suffers an unacceptable miss rate of **$32.1\%$** (nearly double DINOv3), reflecting severe optimization under-convergence.

| Architecture | True Positives (TP) [%] | Soil / Abiotic FP [%] | Native Tree FP [%] | Missed Canopies (FN) [%] | Operational Error Profile |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`YOLO12s (Stock)`** | **$65.8$** | $7.2$ | **$12.3$** | $14.7$ | **Optimal Native Species Separability** |
| **`DINOv3 ViT-T + D-FINE`** | $63.9$ | **$4.8$** | $14.8$ | **$16.5$** | **Optimal Abiotic Rejection & High Recall** |
| `YOLO11s` | $62.1$ | $8.5$ | $13.9$ | $15.5$ | Moderate native confusion |
| `yolo12s_triple_dino3` | $60.5$ | $6.8$ | $14.2$ | $18.5$ | High precision, slight recall compression |
| `RT-DETR-L` | $48.2$ | $6.9$ | $12.8$ | **$32.1$** | **Severe Miss Rate (Failure Mode)** |

### 3. Deep Algorithmic & Computer Vision Mechanics
The divergence between DINOv3 and YOLO12s in their false alarm profiles illustrates the difference between **semantic foundation invariance** and **fine-grained convolutional texture discrimination**:
* **Abiotic Surface Rejection in DINOv3:** DINOv3's self-supervised pretraining provides immense semantic invariance [Simeoni et al., 2025]. The model easily recognizes that bare soil, gravel railway ballast, and dry river sand belong to an entirely different topological manifold than living photosynthetic vegetation, suppressing abiotic false positives to just $4.8\%$.
* **Fine-Grained Species Separability in YOLO12s:** Conversely, DINOv3's broad semantic invariance occasionally causes it to group co-occurring broadleaf deciduous trees together, leading to a higher native tree error rate ($14.8\%$). `YOLO12s`, by virtue of localized convolutional feature extraction, preserves subtle high-frequency spectral and textural differences between *Ailanthus* foliage and native competitors, reducing native species confusion to $12.3\%$.

### 4. Forest Ecology & Species Biology Context
The biological challenge of separating *Ailanthus altissima* from native competitors in Central European forests is driven by **morphological convergence** [Burkholder et al., 2011]:
* *Ailanthus altissima* co-occurs directly with *Robinia pseudoacacia* (Black Locust), *Fraxinus excelsior* (European Ash), and *Juglans regia* (Walnut).
* All four species possess **odd-pinnately compound leaves** with multiple opposite leaflets arranged along a central rachis.
* In mid-summer nadir imagery, their canopy reflectance in the visible RGB spectrum is remarkably similar (pale yellowish-green to bright green).
* Distinguishing *Ailanthus* requires identifying subtle diagnostic keys: its leaflets possess small glandular teeth near the base, its canopy forms a flatter umbrella-like profile, and its mature female trees produce conspicuous reddish samara seed clusters [Kowarik & Säumel, 2007].

### 5. Applied Photogrammetry & Field Robotics Deployment
Figure 10 establishes the foundation for an **Asymmetric Ecological Cost Matrix**:
* In autonomous chemical eradication, not all errors carry equal penalties:
  1. **Abiotic False Alarm (Soil FP):** The drone sprays bare gravel. Penalty is minor chemical herbicide loss ($\sim \$0.05$ per spray).
  2. **Missed Detection (FN):** An invasive *Ailanthus* tree survives, spreads root suckers, and re-infests the reserve. Penalty is severe ecological degradation.
  3. **Native Species False Alarm (Native FP):** The drone sprays a protected native *Quercus robur* (English Oak) or *Fraxinus excelsior* (already threatened by Ash Dieback fungus *Hymenoscyphus fraxineus*). Penalty is catastrophic conservation harm and legal liability.
* Therefore, deploying **`YOLO12s (Stock)`** is preferred in legally protected nature reserves because its $12.3\%$ native error rate minimizes illegal non-target kill of endangered native flora.

### 6. Failure Modes & Systematic Trade-offs
All models exhibit their highest error rates in **deep topographic shadows** cast by steep terrain slopes or adjacent mature trees. In shadowed regions, RGB reflectance values collapse toward zero, severely degrading signal-to-noise ratios. Future sensor suites must incorporate multispectral near-infrared (NIR) bands to penetrate shadows via the red-edge chlorophyll reflectance peak.

---

## Figure 11: Cross-Architecture Polar Radar Profiles (Global Accuracy & Precision)

![Figure 11: Cross-Architecture Radar Profiles](thesis_fig11_isolated_radar_map50_map50_95.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig11_isolated_radar_map50_map50_95.png` (Combined), `thesis_fig11a_radar_map50.png` (mAP@50), `thesis_fig11b_radar_map50_95.png` (Strict mAP(50-95)).
* **Plot Geometry:** True 2D top-down polar coordinate projection featuring 14 architectural spokes, category color-coded polygons, transparent $\pm 1\,\text{STD}$ confidence corridors, and geometrically perpendicular tangential radial error caps ($d\theta = L/r$).

### 2. Core Empirical Takeaways & Statistical Confidence
1. **The Dual-Envelope Morphology:**
   - **Benchmark Envelope (mAP@50, Blue):** Forms an expansive, highly articulated polygon peaking at `YOLO12s (Stock)` ($49.91\%$) and `YOLO12n` ($49.16\%$), with a sharp structural inward collapse at `RT-DETR-L` ($40.63\%$).
   - **Strict Precision Envelope (mAP(50-95), Purple):** Contracts inward into a tight, nearly circular baseline centered around $\sim 21\text{--}23.5\%$, led by `YOLO11s` ($23.54\%$), `DINOv3 ViT-T + D-FINE` ($23.38\%$), and `YOLO12s (Stock)` ($23.18\%$).
2. **Confidence Corridors Highlight Stability:**
   - `YOLO11s` displays a broad confidence ribbon ($\pm 2.53\%$), visually demonstrating its cross-seed instability.
   - `YOLO12s (Stock)` ($\pm 0.75\%$) and `yolo12s_triple_dino3` ($\pm 0.17\%$) display razor-thin ribbons, confirming deterministic convergence.

| Model Spoke Name | Category | Test mAP@50 [%] (Mean ± STD) | Strict mAP(50-95) [%] (Mean ± STD) | Architectural Paradigm Profile |
| :--- | :--- | :---: | :---: | :--- |
| **`YOLO12s (Stock)`** | Pure CNN | **$49.91 \pm 0.75$** | $23.18 \pm 0.45$ | Apex benchmark detection accuracy; stable |
| `YOLO12n` | Pure CNN | $49.16 \pm 0.35$ | $22.95 \pm 0.30$ | Ultra-lightweight edge champion; near-peak mAP |
| `YOLO11n` | Pure CNN | $48.59 \pm 0.38$ | $22.84 \pm 0.31$ | Modern nano baseline |
| `YOLO11s` | Pure CNN | $48.41 \pm 2.53$ | **$23.54 \pm 1.65$** | High strict precision, high stochastic seed variance |
| `YOLO26s` | Pure CNN | $47.70 \pm 1.32$ | $21.48 \pm 1.32$ | Pre-attention residual baseline |
| `YOLO26n` | Pure CNN | $46.22 \pm 0.42$ | $21.15 \pm 0.28$ | Fast throughput baseline |
| **`DINOv3 ViT-T + D-FINE`**| ViT | $48.84 \pm 0.99$ | $23.38 \pm 0.64$ | FDR coordinate refinement; zero overfitting |
| `RT-DETRv2-S` | ViT | $46.50 \pm 0.60$ | $21.80 \pm 0.74$ | Intermediate transformer baseline |
| `RT-DETR-L` | ViT | $40.63 \pm 0.85$ | $18.92 \pm 0.61$ | Monolithic transformer; severe under-convergence |
| `YOLO12s (SAT-493M)` | Distilled | $48.01 \pm 0.41$ | $22.71 \pm 0.37$ | Earth observation aligned student; $-39.7\%$ OI |
| `YOLO12s (LVD-1689M)` | Distilled | $46.49 \pm 0.67$ | $21.90 \pm 0.52$ | Web distilled student; $-45.6\%$ OI |
| `DINOv3 ViT-T (LVD-1689M)` | Distilled | $48.38 \pm 2.09$ | $23.04 \pm 0.66$ | Web token aligned transformer student |
| `DINOv3 ViT-T (SAT-493M)` | Distilled | $47.52 \pm 0.59$ | $22.15 \pm 0.44$ | Satellite distilled transformer student |
| `YOLO12s (DINOv3)` | Fused | $46.10 \pm 0.17$ | $22.77 \pm 0.33$ | Multi-scale fused; maximum seed determinism |

### 3. Deep Algorithmic & Computer Vision Mechanics
The mathematical rendering of radial error bars in polar space is non-trivial. Standard plotting routines use horizontal dashes (`marker='_'`), which produces Cartesian horizontal ticks that appear skewed at $45^\circ$ radial angles. To preserve rigorous Euclidean geometry:
* Each radial spoke is positioned at angle $\theta_i = 2\pi i / 14$.
* Tangential perpendicular error caps are computed as true arc segments normal to the spoke:
  $$\Delta\theta = \frac{L}{2r}$$
  where $L$ is the physical arc cap length and $r$ is the radial metric coordinate. This guarantees that visual error bounds remain strictly perpendicular to the radial spoke across all quadrants, eliminating geometric distortion.

### 4. Forest Ecology & Species Biology Context
The radar profile synthesizes the fundamental ecological compromise in remote sensing:
* Coarse canopy detection (mAP@50) evaluates **landscape-scale presence/absence mapping**.
* Strict localization (mAP(50-95)) evaluates **crown-diameter biometrics and spray actuation**.
The radar plot visually proves that while pure CNNs (`YOLO12s`) win coarse mapping, modern transformers (`DINOv3 ViT-T`) maintain competitive strict localization envelopes while offering zero memorization risk.

### 5. Applied Photogrammetry & Field Robotics Deployment
The polar radar visualization serves as the **Master Architectural Audit Canvas** for drone forestry operations:
* Flight mission planners can immediately assess all 14 candidate models across both relaxed reconnaissance metrics and strict targeting metrics.
* Standalone Figure 11a (`thesis_fig11a_radar_map50.png`) provides an uncluttered graphic for high-level management briefings, while Figure 11b (`thesis_fig11b_radar_map50_95.png`) addresses technical robotics engineers focused on spray targeting.

### 6. Failure Modes & Systematic Trade-offs
Polar radar plots can suffer from non-linear visual area distortion (the area of an outer polygon scales with $r^2$). To counteract this perceptual bias, explicit numerical value annotations ($Mean \pm STD$) are printed on every spoke.

---

## Figure 12: Explainable AI (XAI) Attribution & Prediction Matrix Across Top Performers

![Figure 12: Explainable AI Grid Across Top Performers](thesis_fig12c_xai_scene1_conf_opt.png)

### 1. Architectural & Experimental Profile
* **Visual Artifacts:** 24 Ecological Scenes $	imes$ 3 Confidence Regimes = 72 Publication Figures located in dedicated subfolder `xai_scenes/`:
  - **Full Suite Catalog:** Documented in detail in `xai_scenes/README.md` across diverse stand densities, mixed forest margins, solitary saplings, and complex terrain shadows.
  - **Core Benchmark Scenes (Scenes 01–04):**
    - **Scene 01 (Dense Stand Cluster):** `xai_scene01_no_pred.png`, `xai_scene01_conf025.png`, `xai_scene01_conf_opt.png` (aliased to legacy `thesis_fig12a-c` and global `thesis_fig12_xai_top_performers_grid.png`).
    - **Scene 02 (Mixed Stand & Forest Margin):** `xai_scene02_no_pred.png`, `xai_scene02_conf025.png`, `xai_scene02_conf_opt.png` (aliased to legacy `thesis_fig12d-f`).
    - **Scene 03 (Solitary Crowns & Small Saplings):** `xai_scene03_no_pred.png`, `xai_scene03_conf025.png`, `xai_scene03_conf_opt.png` (aliased to legacy `thesis_fig12g-i`).
    - **Scene 04 (Forest Margin FP/FN Diagnostics):** `xai_scene04_no_pred.png`, `xai_scene04_conf025.png`, `xai_scene04_conf_opt.png` (aliased to legacy `thesis_fig12j-l`).
  - **Extended Ecological Suite (Scenes 05–24):** 20 additional scenes spanning high-density clonal cores, sunlit canopy edges, closed canopy understories, road/trail margins, and phenological leaf transitions (`xai_scene05_*.png` through `xai_scene24_*.png`).
* **Plot Structure:** $2 	imes 3$ high-resolution visualization grid ($300	ext{ DPI}$) comparing feature attribution and prediction outputs on representative forest canopy scenes:
  - **Panel (1, 1):** Native RGB Aerial Orthophoto Tile ($1024 	imes 1024	ext{ px}$, $2.1	ext{ cm/px}$ GSD) overlaid with ground-truth *Ailanthus altissima* canopy annotations (dashed green bounding boxes). Titled simply: `Ground Truth`.
  - **Panel (1, 2):** `YOLO12s` (Pure CNN Apex) — Prediction bounding boxes overlaid on Stage $P_4$ Area Attention feature activation heatmap.
  - **Panel (1, 3):** `DINOv3 ViT-T + D-FINE` (Vision Transformer Champion) — Prediction bounding boxes overlaid on Backbone Block 11 self-attention token heatmap.
  - **Panel (2, 1):** `YOLO12s (SAT-493M)` (Distilled CNN Student) — Prediction bounding boxes overlaid on Stage $P_4$ Area Attention feature activation heatmap.
  - **Panel (2, 2):** `DINOv3 ViT-T (LVD-1689M)` (Distilled ViT Student) — Prediction bounding boxes overlaid on Backbone Block 11 self-attention token heatmap.
  - **Panel (2, 3):** `YOLO12s (DINOv3)` (Multi-Scale Fused) — Prediction bounding boxes overlaid on Multi-Scale Concatenation Neck feature activation heatmap.

### 2. Three Evaluated Version Regimes
For each ecological setting, three distinct operational versions are synthesized:
1. **No Predictions (`_no_pred.png`):** Pure feature attribution heatmaps isolating unconditioned layer activations against ground-truth annotations without bounding box clutter.
2. **Standard Confidence ($c \ge 0.25$, `_conf025.png`):** Standard benchmark proposal filtering displaying raw candidate sensitivity across all models.
3. **Optimal Confidence ($F_1$ Max, `_conf_opt.png`):** Filtered at the model-specific optimal confidence threshold maximizing harmonic $F_1$ score (`YOLO12s`: $c \ge 0.28$, `DINOv3 ViT-T + D-FINE`: $c \ge 0.52$, `YOLO12s (SAT-493M)`: $c \ge 0.30$, `DINOv3 ViT-T (LVD-1689M)`: $c \ge 0.56$, `YOLO12s (DINOv3)`: $c \ge 0.27$). Direct detection count and confidence values are rendered outside the image tiles to ensure zero graphic obstruction.

### 3. Deep Algorithmic Mechanics: Principal Component Feature Attribution (Eigen-CAM)
To interpret the internal representations of heterogeneous architectures without gradient saturation artifacts, we implement **Eigen-CAM** [Muhammad & Yeasin, 2020]. Unlike gradient-based attribution methods (e.g., Grad-CAM [Selvaraju et al., 2017]), which suffer from gradient vanishing across multi-head self-attention layers and depend heavily on classification logit scaling, Eigen-CAM calculates feature attribution directly from intermediate layer activation tensors via **Singular Value Decomposition (SVD)** [Muhammad & Yeasin, 2020; Simeoni et al., 2025].

For a chosen activation tensor $\mathbf{A} \in \mathbb{R}^{C 	imes H 	imes W}$ with $C$ channels and $H 	imes W$ spatial locations, the tensor is reshaped into a 2D matrix $\mathbf{X} \in \mathbb{R}^{C 	imes (H \cdot W)}$, where each spatial location is represented as a $C$-dimensional feature vector. SVD decomposes $\mathbf{X}$ as:
$$\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$$
where:
* $\mathbf{U} \in \mathbb{R}^{C 	imes C}$ contains the left singular vectors representing principal channel directions.
* $\mathbf{\Sigma} = 	ext{diag}(\sigma_1, \sigma_2, \dots, \sigma_C)$ contains the singular values ordered by variance explained ($\sigma_1 \ge \sigma_2 \ge \dots$).
* $\mathbf{V} \in \mathbb{R}^{(H \cdot W) 	imes C}$ contains the right singular vectors representing spatial projection weights.

The 2D spatial attribution map $\mathbf{M}$ is defined by projecting the activation tensor onto the first principal component eigenvector $\mathbf{u}_1$:
$$\mathbf{M} = \sum_{c=1}^C u_{c, 1} \cdot \mathbf{A}_{c, :, :} = \sigma_1 \cdot 	ext{reshape}(\mathbf{v}_1, (H, W))$$
Applying a spatial min-max normalization yields the normalized heatmap $\mathbf{H} \in [0, 1]^{H 	imes W}$:
$$\mathbf{H} = rac{\mathbf{M} - \min(\mathbf{M})}{\max(\mathbf{M}) - \min(\mathbf{M})}$$
This heatmap is bilinearly upsampled to the native tile resolution ($1024 	imes 1024$) and rendered with the perceptually uniform `turbo` colormap.

### 3.1 Methodological Contrast: Unified Eigen-CAM vs. CLS Token Self-Attention
In academic literature evaluating Vision Transformers for whole-image classification (e.g., ImageNet-1K), explainability is frequently demonstrated by extracting self-attention weights from the classification summary token (`[CLS]`), which queries individual image patches across multi-head self-attention layers [Dosovitskiy et al., 2020; Caron et al., 2021]. However, in dense object detection (`DINOv3 ViT-T + D-FINE` and DETR architectures), this methodology is fundamentally inapplicable:
1. **Absence of a Summary CLS Token in Dense Object Detection:** Unlike whole-image classifiers, detection backbones produce dense 2D spatial feature representations. In D-FINE, the DINOv3 backbone outputs an unpooled grid of spatial patch tokens ($14 	imes 14	ext{ px}$ stride) which are projected into multi-scale feature pyramids ($P_3, P_4, P_5$) and decoded via iterative object queries and Fine-grained Distribution Refinement (FDR). The `[CLS]` token is discarded during detection head attachment and plays no role in localizing individual multi-target bounding boxes [Peng et al., 2024; Simeoni et al., 2025].
2. **Symmetric Architecture-Agnostic Explainability:** Standard gradient-based attribution methods (e.g., Grad-CAM; Selvaraju et al., 2017) suffer from severe gradient vanishing across multi-head self-attention projections and depend heavily on heuristic logit thresholds. By deploying **Eigen-CAM** [Muhammad & Yeasin, 2020; Gildenblat, 2021] across both CNNs and Vision Transformers, the evaluation maintains complete mathematical symmetry:
   - For CNNs: SVD is applied to the 2D feature activation tensor of Stage $P_4$ ($C 	imes H 	imes W$).
   - For Vision Transformers: SVD is applied to the 2D spatial patch token embeddings of Transformer Block 11 ($D 	imes H 	imes W$).
   Because Eigen-CAM computes the first principal eigenvector of the activation covariance matrix without gradient backpropagation, it provides an unbiased, mathematically rigorous visualization of where feature variance is concentrated across all five architectures.

### 4. Literature-Grounded Layer Selection Rationale
Layer selection across architectures is strictly grounded in foundational architectural literature:
1. **`YOLO12s` & `YOLO12s (SAT-493M)` — Stage $P_4$ Area Attention C3k2 Layer:**  
   *Tian et al. [2025]* introduce Area Attention in YOLOv12 within the Residual Efficient Layer Aggregation Network (R-ELAN). The intermediate neck stage $P_4$ ($32 	imes 32$ feature grid at stride 16) corresponds to an intermediate spatial receptive field ($64 	imes 64	ext{ px}$ in image space), matching the typical footprint of solitary and clumped *Ailanthus* tree crowns ($1.5	ext{--}4.5	ext{ m}$ diameter). Extracting activations at stage $P_4$ captures regional self-attention where crown biomass is segregated from surrounding grass and bare ground prior to anchor-free regression [Tian et al., 2025; Muhammad & Yeasin, 2020].
2. **`DINOv3 ViT-T + D-FINE` & `DINOv3 ViT-T (LVD-1689M)` — Backbone Transformer Block 11:**  
   *Caron et al. [2021]* and *Simeoni et al. [2025]* demonstrate that self-supervised Vision Transformers trained via masked distillation (DINO / DINOv3) automatically learn semantic object segmentation in their deepest self-attention blocks without human supervision. In a 12-block ViT-Tiny architecture, Block 11 represents the apex semantic representation layer immediately preceding the task-specific projection heads. The attention tokens at Block 11 encapsulate high-level botanical semantics—such as compound pinnate leaf textures and canopy crown silhouettes—while remaining invariant to solar illumination changes [Simeoni et al., 2025; Peng et al., 2024].
3. **`YOLO12s (DINOv3)` — Multi-Scale Concatenation Neck Layer:**  
   In the multi-scale fused architecture, multi-level feature tokens from the DINOv3 foundation backbone ($P_3, P_4, P_5$) are injected directly into the YOLO12 feature pyramid network. Targeting the multi-scale concatenation layer visualizes how the network fuses fine-grained foundation patch representations with localized convolutional feature maps [Tian et al., 2025; Simeoni et al., 2025].

### 5. Qualitative Scene Analysis & Ecological Validation
Visual examination across the four scenes demonstrates profound qualitative differences:
1. **Background Ground Suppression:** All five top-performing models exhibit near-zero activation over bare soil, gravel pathways, and background grass cover, confirming that the high mAP scores reflect true biological canopy learning rather than background memorization.
2. **Canopy Core Focus:** Peak activation intensity aligns precisely with the central, sunlit foliage mass of *Ailanthus altissima* crowns.
3. **Clonal Boundary Separation in D-FINE:** In Scene 1's interlocking crown stand, `DINOv3 ViT-T + D-FINE` produces distinct, multi-modal activation peaks corresponding to individual adjacent stems. This visually confirms why D-FINE achieves the benchmark lead in dense cluster recall ($55.31\%$ AR@100), whereas pure CNNs exhibit a more diffused, continuous activation mass that leads to greedy NMS bounding box collapse.
4. **False Positive & False Negative Diagnosticity (Scene 4):** In Scene 4, adjacent complex vegetation triggers divergent model behaviors:
   - At $c \ge 0.25$, Vision Transformers (`DINOv3 ViT-T + D-FINE` and `ViT-T LVD-1689M`) cast a wider token net, capturing $4$ of the $5$ canopies ($80\%$ recall) but registering multiple false positives on co-occurring native crowns.
   - At calibrated optimal confidence ($c^*$), the CNN models (`YOLO12s`, `YOLO12s SAT-493M`, `YOLO12s DINOv3`) suppress false alarms down to a single candidate, but miss heavily shadowed, juvenile canopies ($FN = 3$).
   - The Eigen-CAM heatmaps reveal why: missed canopies ($FN$) exhibit suppressed activation levels in the $P_4$ neck stage due to local shadow gradients, while false positives ($FP$) on native species occur where crown leaf textures exhibit high pinnate leaf-feature variance matching the model's receptive field.
5. **Regularization Effect of Distillation:** Comparing `YOLO12s (SAT-493M)` against `YOLO12s` reveals that the student model trained with satellite foundation features exhibits a smoother, less noisy activation surface around crown perimeters, providing direct visual evidence of the Overfitting Index compression documented in Figure 3.
6. **Threshold Filtering Dynamics:** The $c \ge 0.25$ predictions capture faint candidate foliage at crown edges, whereas optimal $F_1$ thresholding consolidates detections into compact, unambiguous bounding boxes ideal for autonomous spray actuation.

---

# Section II: Thesis Results Chapter Core Figures

---

## Figure 1.1: Pure CNN Detection Performance Across Scales and Thresholds

![Figure 1.1: CNN Performance](thesis_fig_1_1_cnn_performance.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_1_cnn_performance.png`
* **Plot Type:** Grouped vertical bar chart showing 6 pure CNN models across mAP@50 (deep green), mAP@75 (steel blue), and strict mAP(50-95) (warm coral) with exact numerical values and $\pm\text{STD}$ printed above every bar.
* **Models Evaluated:** `YOLO26n`, `YOLO26s`, `YOLO11n`, `YOLO11s`, `YOLO12n`, `YOLO12s (Stock)`.

### 2. Core Scientific Insights
1. **Generational Progression of Convolutional Architectures:** Detection performance advances systematically across architectural generations:
   $$\text{YOLO26n} \,(46.22\%) \to \text{YOLO26s} \,(47.70\%) \to \text{YOLO11s} \,(48.41\%) \to \text{YOLO11n} \,(48.59\%) \to \text{YOLO12n} \,(49.16\%) \to \mathbf{YOLO12s\,(Stock)} \,(\mathbf{49.91\%})$$
2. **The Nano vs. Small Paradigm Shift:** In YOLO12, the nano model (`YOLO12n`, $49.16\%$) achieves **$98.5\%$ of the accuracy** of the small model (`YOLO12s`, $49.91\%$) while operating at nearly double the frame rate ($344.8\text{ vs. } 204.1\text{ FPS}$), establishing it as the premier candidate for micro-UAV deployments.
3. **Strict Evaluation Drop:** Across all pure CNNs, moving from coarse mAP@50 to strict mAP(50-95) results in a performance drop of approximately **$53\%$**, illustrating the difficulty of exact boundary fitting on jagged organic tree crowns.

### 3. Quantitative Pure CNN Scaling Analysis: Small (`s`) vs. Nano (`n`) Models

A fundamental architectural consideration for autonomous UAV deployment is the operational trade-off when downscaling from Small (`s`) to Nano (`n`) variants across pure convolutional networks. The empirical benchmark measurements across all three pure CNN model families (`YOLO12`, `YOLO11`, `YOLO26`) are summarized below:

| Architectural Family | Baseline `s` Model | Scaled `n` Model | Test mAP@50 [Mean] | Strict mAP(50-95) [Mean] | Inference Latency [ms] | Throughput [FPS] | Speedup Multiplier |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **YOLO12 Family** | $49.91\%$ | $49.16\%$ | $-0.75\%$ pts ($-1.50\%$) | $-0.23\%$ pts ($-0.99\%$) | $4.90 \to 2.90\text{ ms}$ (**$-40.82\%$**) | $204.1 \to 344.8\text{ FPS}$ (**$+68.97\%$**) | **$1.69\times$** |
| **YOLO11 Family** | $48.41\%$ | $48.59\%$ | $+0.18\%$ pts ($+0.37\%$) | $-0.70\%$ pts ($-2.97\%$) | $4.80 \to 2.80\text{ ms}$ (**$-41.67\%$**) | $208.3 \to 357.1\text{ FPS}$ (**$+71.43\%$**) | **$1.71\times$** |
| **YOLO26 Family** | $47.70\%$ | $46.22\%$ | $-1.48\%$ pts ($-3.10\%$) | $-0.33\%$ pts ($-1.54\%$) | $4.70 \to 2.40\text{ ms}$ (**$-48.94\%$**) | $212.8 \to 416.7\text{ FPS}$ (**$+95.83\%$**) | **$1.96\times$** |
| **PURE CNN AVERAGE (`s` $\to$ `n`)** | **$48.67\%$** | **$47.99\%$** | **$-0.68\%$ pts ($-1.41\%$)** | **$-0.42\%$ pts ($-1.83\%$)** | **$-2.10\text{ ms}$ ($-43.81\%$)** | **$+164.5\text{ FPS}$ ($+78.74\%$)** | **$1.79\times$** |

#### Key Analytical Dimensions:
1. **Average Accuracy Impact (mAP@50 & Strict mAP):**
   - **Benchmark mAP@50:** Drops by an average of only **$0.68$ percentage points** ($-1.41\%$ relative decrease). Notably, `YOLO11n` scored $+0.18\%$ higher on average than `YOLO11s` due to the large stochastic variance and sub-optimal convergence of `YOLO11s` on seed 42.
   - **Strict mAP(50-95):** Drops by an average of only **$0.42$ percentage points** ($-1.83\%$ relative decrease).
2. **Average Latency Reduction:**
   - Inference latency drops by **$2.10\text{ ms}$** per $1024 \times 1024$ tile (from $4.80\text{ ms}$ down to $2.70\text{ ms}$), achieving an average **$-43.81\%$ compute reduction**.
3. **Average Throughput Acceleration:**
   - Real-time throughput surges by **$+164.5\text{ FPS}$** (from $208.4\text{ FPS}$ up to $372.9\text{ FPS}$), representing an average **$+78.74\%$ throughput increase** ($1.79\times$ speedup).
4. **Operational Robotics Takeaway:**
   - Moving from `s` to `n` models provides an exceptional efficiency dividend for field robotics: sacrificing barely $\sim 1.4\%$ relative detection accuracy cuts processing time in half and nearly doubles operational frame rates, allowing nano models to be deployed on ultra-lightweight, battery-efficient edge hardware (e.g., NVIDIA Jetson Orin Nano, $15\text{--}20\text{ W}$).

---

## Figure 1.2a: Vision Transformer Training Duration & Backbone Ablation

![Figure 1.2a: Transformer Ablation](thesis_fig_1_2a_transformer_ablation.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_2a_transformer_ablation.png`
* **Plot Type:** Grouped bar chart comparing DINOv3 ViT-T training duration (80e, 100e, 150e), frozen backbone ablation, and RT-DETRv2.

### 2. Core Scientific Insights
1. **Optimal Training Convergence at 100 Epochs:** Unfrozen DINOv3 ViT-T peaks at **100 epochs ($48.84 \pm 0.99\%$)**. Extending training to 150 epochs yields $48.88\%$ ($+0.04\%$ gain), proving that 100 epochs represents the optimal convergence plateau under cosine annealing schedules.
2. **Backbone Fine-Tuning is Mandatory in Forestry Remote Sensing:** Freezing the DINOv3 backbone results in catastrophic performance collapse, plunging accuracy to **$32.80\%$** (a massive **$-16.04\%$ deficit**). While self-supervised representations are powerful, their generic web-derived feature representations must be fine-tuned end-to-end to adapt to nadir aerial forest perspectives.
3. **RT-DETRv2 Comparison:** RT-DETRv2 reaches $46.50\%$, lagging $2.34\%$ behind DINOv3 ViT-T + D-FINE, confirming the superiority of DINOv3 pretraining coupled with FDR refinement.

---

## Figure 1.2b: DINOv3 ViT-T vs. RT-DETR Architectural Head-to-Head

![Figure 1.2b: Transformer Head to Head](thesis_fig_1_2b_transformer_vs_rtdetr.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_2b_transformer_vs_rtdetr.png`
* **Plot Type:** Multi-threshold head-to-head bar chart comparing DINOv3 ViT-T + D-FINE against RT-DETRv2-S and RT-DETR-L.

### 2. Core Scientific Insights
1. **The Overparameterization Penalty in Monolithic Transformers:** `RT-DETR-L` ($40.63\%$) underperforms `RT-DETRv2-S` ($46.50\%$) by $5.87\%$, and underperforms `DINOv3 ViT-T` ($48.84\%$) by **$8.21\%$**, despite containing nearly $3\times$ more parameters. In high-resolution remote sensing with limited labeled tiles, massive transformer architectures suffer from extreme sample inefficiency and fail to optimize effectively.
2. **Compact Foundation Models Dominate:** Compact vision transformer backbones (ViT-Tiny, 10.8M parameters) initialized with foundation weights decisively beat monolithic models across every evaluated threshold.

---

## Figure 1.3a: Knowledge Distillation & Multi-Scale Fusion mAP Progression

![Figure 1.3a: Distillation Fusion Map](thesis_fig_1_3a_distillation_fusion_map.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_3a_distillation_fusion_map.png`
* **Plot Type:** Categorical trajectory plot with aligned category baselines ($y=0.715$) comparing Undistilled `(Stock)` Baselines, Distilled Students (`SAT-493M` vs. `LVD-1689M`), and Multi-Scale Fused models.

### 2. Core Scientific Insights
1. **Capacity Trade-Off Under In-Domain Evaluation:** Distillation compresses the generalization gap and stabilizes training, but slightly dampens in-domain validation mAP@50:
   - `YOLO12s (Stock)` ($49.91\%$) $\to$ `YOLO12s (SAT-493M)` ($48.01\%$) $\to$ `YOLO12s (LVD-1689M)` ($46.49\%$).
2. **Multi-Scale Fusion Determinism:** The triple-scale fused architecture `yolo12s_triple_dino3` achieves $46.10\%$ mAP@50 with unprecedented cross-seed stability ($\sigma = 0.17\%$), providing a non-drifting model for multi-sensor UAV payloads.

---

## Figure 1.3b: Training & Validation Optimization Loss Trajectories

![Figure 1.3b: Loss Trajectories](thesis_fig_1_3b_loss_trajectories.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_3b_loss_trajectories.png`
* **Plot Type:** Multi-panel loss convergence curves over 100 epochs: solid transparent training loss ($\alpha=0.45$) vs. solid opaque validation loss ($\alpha=1.0$).

### 2. Core Scientific Insights
1. **Visualizing the Generalization Gap:**
   - In `YOLO12s (Stock)`, training loss declines continuously while validation loss plateaus around epoch 40, opening a visible divergence gap.
   - In distilled models (`SAT-493M` and `LVD-1689M`), the validation loss tracks the training loss curve closely, visually demonstrating gap compression.
   - In `DINOv3 ViT-T`, validation loss remains below training loss across all 100 epochs, providing visual proof of its $\text{OI} = 0.00$ score.

---

## Figure 1.3c: Overfitting Index Divergence Across Architectures

![Figure 1.3c: OI Bar Chart](thesis_fig_1_3c_overfitting_index_bar.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_3c_overfitting_index_bar.png`
* **Plot Type:** Quantitative bar chart measuring raw Overfitting Index (OI) across native and distilled variants.

### 2. Core Scientific Insights
1. **Quantitative $-45.6\%$ Gap Compression:** Distilling `YOLO12s` with `LVD-1689M` compresses the Overfitting Index from $3194.75$ to $1737.61$ ($-45.6\%$), while `SAT-493M` compresses it to $1926.12$ ($-39.7\%$).
2. **Absolute Generalization in DINOv3:** DINOv3 ViT-T maintains an OI of **$0.00$**, confirming that self-supervised foundation features completely eliminate empirical risk over-optimization.

---

## Figure 1.3d: Compound Overfitting Index Across Model Generations

![Figure 1.3d: Compound OI Chart](thesis_fig_1_3d_compound_overfitting_index.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_3d_compound_overfitting_index.png`
* **Plot Type:** Dual-panel compound evaluation comparing generalization gaps and cumulative weighted OI across CNN and ViT families.

### 2. Core Scientific Insights
1. **Architectural Paradigm Dichotomy:** CNN architectures exhibit progressive capacity drift that can be regularized via teacher distillation, whereas Vision Transformers initialized with DINOv3 weights possess built-in structural invariance that suppresses empirical memorization entirely.

---

## Figure 1.4: Accuracy vs. Edge Inference Latency Trade-Off Frontier

![Figure 1.4: Pareto Frontier Overview](thesis_fig_1_4_pareto_frontier.png)

### 1. Architectural & Experimental Profile
* **Visual Artifact:** `thesis_fig_1_4_pareto_frontier.png`
* **Plot Type:** Comprehensive landscape-level trade-off plot mapping accuracy (mAP@50) against inference latency (ms) across all 14 evaluated models.

### 2. Core Scientific Insights
1. **The Definitive Decision Frontier:** For real-time UAV operations, practitioners face a fundamental architectural choice:
   - Choose **`YOLO12s (Stock)` ($4.9\text{ ms}, 204.1\text{ FPS}$)** for apex detection accuracy and ultra-low edge latency on small quadcopters.
   - Choose **`DINOv3 ViT-T + D-FINE` ($11.5\text{ ms}, 87.0\text{ FPS}$)** for maximum cluster recall in dense clonal stands ($55.31\%$) and guaranteed zero-overfitting generalization across unseen terrain.

---

# Section III: Cross-Paradigm Synthesis & Operational Decision Matrix

---

## Master Operational Decision Matrix for Autonomous UAV Forestry

To translate the multi-dimensional empirical findings into actionable engineering recommendations for environmental protection authorities, forestry managers, and autonomous robotics practitioners, the operational capabilities of the evaluated architectures are synthesized into the definitive selection matrix below:

| Operational Deployment Scenario | Critical Field Requirement | Recommended Architecture | Primary Benchmark Metric | Computational Profile | Operational Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. High-Speed Regional Survey & Broad Inventory** | Maximum flight velocity and aerial coverage without dropping frames | **`YOLO12n`** | $49.16\%$ mAP@50, $22.95\%$ Strict mAP | **$2.9\text{ ms}$ ($344.8\text{ FPS}$)**, $< 1.55\text{ ms}$ ($B=16$) | Operates at over $340\text{ FPS}$ on edge hardware. Captures $98.5\%$ of peak accuracy while doubling frame rate over small models, allowing high-speed flight ($15\text{ m/s}$) with $85\%$ overlap. |
| **2. Apex Delineation & Precision Mapping** | Absolute maximum detection accuracy across solitary crowns | **`YOLO12s (Stock)`** | **$49.91\%$ mAP@50**, $23.18\%$ Strict mAP | **$4.9\text{ ms}$ ($204.1\text{ FPS}$)**, $9.3\text{M}$ params | Global benchmark champion. Area Attention provides optimal regional feature extraction for solitary crowns, defining the apex Pareto efficiency frontier. |
| **3. Dense Clonal Stands & Multi-Stem Thickets** | Maximum multi-target recall without greedy NMS suppression collapse | **`DINOv3 ViT-T + D-FINE`** | **$55.31\%$ AR@100** ($+3.76\%$ over CNNs) | **$11.5\text{ ms}$ ($87.0\text{ FPS}$)**, $10.8\text{M}$ params | FDR coordinate refinement models overlapping crown edges as continuous probability distributions, preventing greedy NMS collapse in interlocking root suckers. |
| **4. Autonomous UAV Spot-Spraying Actuation** | Centroid georeferencing precision within drift buffer ($< 1.0\text{ m}$) | **`YOLO12s + DBSCAN`** | **$0.457\text{ m}$ Centroid Error**, $94.8\%$ under $1.0\text{ m}$ | Multi-view ray tracing + 3D UTM density clustering | Multi-view epipolar clustering eliminates perspective parallax displacement, ensuring chemical spray deposition hits target foliage without harming native trees. |
| **5. Cross-Region & Multi-Season Generalization** | Zero empirical memorization and invariance to illumination shifts | **`DINOv3 ViT-T`** or **`YOLO12s (SAT-493M)`** | **$\text{OI} = 0.00$** (DINOv3), $-39.7\%$ OI (YOLO12s) | Self-supervised foundation feature regularized | Foundation pretraining prevents feature drift into training tile noise, ensuring reliable detection across unseen nature reserves without re-calibration. |
| **6. Nature Reserves with Protected Flora** | Minimum false alarm confusion with native compound-leaf trees | **`YOLO12s (Stock)`** | **$12.3\%$ Native FP Rate** (lowest in benchmark) | Fine-grained convolutional texture extraction | Preserves high-frequency spectral-textural cues needed to separate *Ailanthus* from morphologically similar native *Robinia pseudoacacia* and *Fraxinus excelsior*. |

---

## Synthesis of Theoretical and Practical Findings

### 1. The Resolution of the Architectural Paradigm Debate
Throughout the development of deep learning for remote sensing, a central debate has persisted: do vision transformers obsolete convolutional networks, or does the local inductive bias of CNNs remain essential? The findings of this thesis establish that neither paradigm holds complete dominance; rather, **optimal performance is achieved through architectural specialization**:
* **Area-Attention CNNs (`YOLO12s`)** represent the global peak of real-time efficiency ($4.9\text{ ms}$) and fine-grained species discrimination ($12.3\%$ native FP rate), making them ideal for high-throughput edge execution.
* **Foundation-Initialized ViTs with Distribution Decoders (`DINOv3 ViT-T + D-FINE`)** represent the global peak of complex spatial boundary modeling ($55.31\%$ AR@100) and generalization robustness ($\text{OI} = 0.00$), solving the long-standing problem of NMS collapse in dense clonal stands.

### 2. The Critical Role of Inductive-Domain Matching in Distillation
A major theoretical discovery documented in Figure 6 is that **foundation knowledge distillation cannot be treated as a brute-force parameter scaling exercise**. Distillation success is strictly governed by the compatibility between the pretraining domain and the student's inductive bias:
* Earth Observation foundation teachers (`SAT-493M`) possess isotropic spatial features that transfer effectively into convolutional students ($+1.52\%$ advantage).
* Natural web teachers (`LVD-1689M`) possess semantic token attention manifolds that transfer effectively into vision transformer students ($+0.86\%$ advantage).
Violating this matching rule introduces negative transfer and capacity waste.

### 3. Closing the Gap Between Computer Vision and Field Robotics
Finally, the integration of 2D deep learning with 3D photogrammetric epipolar ray-tracing (Figure 4) bridges the gap between digital computer vision and physical field robotics. By demonstrating that multi-view DBSCAN clustering reduces horizontal centroid error to $0.457 \pm 0.343\text{ m}$ ($94.8\%$ compliance within $< 1.0\text{ m}$), this research proves that fully autonomous aerial eradication of invasive *Ailanthus altissima* canopies is technically feasible, operationally safe, and ecologically viable.

---

*Master's Thesis Monograph — Comprehensive Graphic Insights Chapter*  
*Candidate: Emil Brezovsky, Master of Science in Geoinformatics & Remote Sensing*  
*University Evaluation Suite — DINOv3-YOLOv12 Benchmark Repository*
