# AGENTS.md: Developer & Agent Guide for Thesis Evaluation and Plotting Suite

Welcome to the **DINOv3-YOLOv12 UAV Canopy Detection, Localization, and Distillation** codebase. This document serves as the authoritative operational manual for autonomous AI agents and human contributors interacting with, maintaining, or extending this repository.

---

## 1. Executive Summary & Research Mission

* **Master's Thesis:** *High-Resolution UAV Detection, Geolocation, and Knowledge Distillation of Invasive Ailanthus altissima Canopies*
* **Candidate / Author:** Emil Brezovsky
* **Target Species:** *Ailanthus altissima* (Tree of Heaven) — aggressive European Union Priority Invasive Alien Tree.
* **Sensor & Flight Profile:** Ultra-high-resolution visible RGB orthophotography ($2.1\text{ cm/px}$ GSD, $1024 \times 1024$ image tiles, EPSG:32633 UTM Zone 33N).
* **Evaluated Cohort:** 14 neural network configurations across 4 architectural paradigms evaluated across $n = 3$ independent random initialization seeds (`42`, `100`, `999`):
  1. **Pure CNNs:** `YOLO12s`, `YOLO12n`, `YOLO11s`, `YOLO11n`, `YOLO26s`, `YOLO26n`
  2. **Vision Transformers (ViTs):** `DINOv3 ViT-T + D-FINE`, `RT-DETRv2-S`, `RT-DETR-L`
  3. **Distilled Students:** `YOLO12s (SAT-493M)`, `YOLO12s (LVD-1689M)`, `ViT-T (SAT-493M)`, `ViT-T (LVD-1689M)`
  4. **Multi-Scale Fused:** `yolo12s_triple_dino3`

---

## 2. Directory Structure & Key Files

The evaluation pipeline, plotting scripts, and documentation reside in [`thesis_evaluation/`](file:///C:/Users/emilb/Documents/GitHub/_trainer_DINOV3-YOLOV12/thesis_evaluation/):

```text
thesis_evaluation/
├── AGENTS.md                                        # This comprehensive agent operational manual
├── README.md                                         # High-level benchmark summary with tables and citations
├── thesis_figures_catalog.md                         # Master monograph (Part I: Results, Part II: Discussion, Part III: Refs)
├── thesis_figures_insights.md                        # Exhaustive scientific, ecological, and operational graphic insights
├── xai_scenes/                                      # Full 105-scene XAI suite (105 6-panel scenes at 300 DPI + manifest CSV)
│   ├── README.md                                     # Scene-by-scene catalog and ecological descriptions
│   ├── xai_105_scenes_manifest.csv                   # Authoritative manifest mapping IDs, stems, categories & GT counts
│   └── xai_scene01_conf_opt.png .. xai_scene105_conf_opt.png
├── extract_loss_curves.py                           # Extracts raw WandB/YOLO training logs -> oi_curves_data.json
├── oi_curves_data.json                              # Processed loss curves & Overfitting Index (OI) stats (N=100 epochs)
├── generate_isolated_thesis_figures.py              # Generates Figures 1-10 (isolated publication-ready single-statement plots)
├── generate_radar_plots.py                          # Generates Figure 11, 11a, 11b (2D polar radar plots with perpendicular caps)
├── generate_xai_heatmaps.py                         # Core 6-panel Explainable AI (XAI) Eigen-CAM engine (24 scenes)
├── generate_105_xai_scenes.py                       # Expanded 105-scene XAI generator (open areas, meadows, tracks, fields, stands)
├── build_thesis_catalog.py                          # Master generator compiling thesis_figures_catalog.md across mirrors
└── build_figures_insights.py                        # Master generator compiling thesis_figures_insights.md across mirrors

thesis_plotting_suite/                               # Self-Contained Interactive Plotting & Jupyter Suite
├── pixi.toml                                        # Dedicated Pixi environment (Python 3.11, JupyterLab, Matplotlib, Scipy)
├── README.md                                        # Quickstart guide for Jupyter and CLI plotting
├── thesis_plotting_suite.ipynb                      # Master interactive Jupyter Notebook
├── generate_all_figures.py                          # Headless CLI batch figure generator
├── data/                                            # Self-contained data dependencies (Zero external path requirements)
│   ├── benchmark_metrics.json                       # All 14 model constants across 3 seeds
│   └── oi_curves_data.json                          # Loss trajectories over 100 epochs
└── output_figures/                                  # Rendered 300 DPI publication figures (Figures 1-11)
```

---

## 3. End-to-End Execution Pipeline

To reproduce, update, or regenerate the entire evaluation suite from scratch, execute the following commands in order:

### Step 1: Extract Empirical Loss Curves & Compute OI
Extracts training and validation loss trajectories across 100 epochs from raw WandB history CSVs and YOLO run reports across seeds `42`, `100`, and `999`:
```powershell
python thesis_evaluation/extract_loss_curves.py
```
* **Inputs:** `C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports\yolo12s_*\results.csv` and `wandb\metric_histories\vitt16_*_history.csv`
* **Outputs:** Writes `thesis_evaluation/oi_curves_data.json` to local repo, Google Drive, and Brain artifacts.

### Step 2: Generate Figures 1 through 10
Generates the 10 isolated, single-statement, publication-grade figures at 300 DPI:
```powershell
python thesis_evaluation/generate_isolated_thesis_figures.py
```
* **Inputs:** `oi_curves_data.json` and verified benchmark metric constants.
* **Outputs:** 10 PNG files (`thesis_fig1_*.png` through `thesis_fig10_*.png`) written simultaneously to all 3 mirrors.

### Step 3: Generate Polar Radar Plots (Figure 11, 11a, 11b)
Generates the 14-model polar radar envelopes with top-down 2D radial error bars and tangential perpendicular caps:
```powershell
python thesis_evaluation/generate_radar_plots.py
```
* **Outputs:** `thesis_fig11_isolated_radar_map50_map50_95.png`, `thesis_fig11a_radar_map50.png`, `thesis_fig11b_radar_map50_95.png`.

### Step 4: Build Thesis Catalog Markdown
Compiles the comprehensive monograph `thesis_figures_catalog.md` with Part I (Results), Part II (Discussion with knowledge base literature citations), and Part III (Master References):
```powershell
python thesis_evaluation/build_thesis_catalog.py
```
* **Outputs:** Synchronizes `thesis_figures_catalog.md` across all 3 mirrors.

### Step 5: Generate 105-Scene Explainable AI (XAI) Attribution Grids (Figure 12)
Generates the comprehensive 105-scene 6-panel paradigm comparison suite (matching Thesis Figure 12):
```powershell
python thesis_evaluation/generate_105_xai_scenes.py
```
* **Panel Configuration:**
  - Panel 0: Ground Truth ($N = X$ Canopies, `#00e676` Emerald Green boxes)
  - Panel 1: `YOLO12s` (Pure CNN Baseline, `#1f77b4` Blue, $c^* = 0.28$)
  - Panel 2: `DINOv3 ViT-T + D-FINE` (Vision Transformer, `#2ca02c` Green, $c^* = 0.52$)
  - Panel 3: `YOLO12s (SAT-493M)` (Distilled CNN, `#ff7f0e` Orange, $c^* = 0.30$)
  - Panel 4: `DINOv3 ViT-T (LVD-1689M)` (Distilled ViT, `#d62728` Red, $c^* = 0.56$)
  - Panel 5: `YOLO12s (DINOv3)` (Multi-Scale Fused / Triple DINO, `#7950f2` Purple, $c^* = 0.27$)
* **Ecological Diversity:** 105 scenes covering open meadows (20), dirt tracks & bare soil (15), agricultural margins (15), native background stands (15), solitary saplings (8), dense clusters (8), and canonical benchmarks (24).
* **Tri-Repository Synchronization:** Directly writes to `_trainer_DINOV3-YOLOV12/thesis_evaluation/xai_scenes/`, `_trainer_lightly/thesis_evaluation/xai_scenes/`, and `_trainer_pred_plotter/results/figures/xai_scenes/`.

---

## 4. Figure-by-Figure Reference & Mapping

| Figure ID | File Name | Script / Generator | Key Empirical Finding | Operational / Theoretical Relevance |
| :---: | :--- | :--- | :--- | :--- |
| **Figure 1** | `thesis_fig1_isolated_pareto_latency.png` | `generate_isolated_thesis_figures.py` (`make_fig1_pareto_latency`) | `YOLO12s` establishes apex accuracy ($49.91 \pm 0.75\%$) at $4.9\text{ ms}$ ($204.1\text{ FPS}$). | Frontier defined by `YOLO26n`, `YOLO11n`, `YOLO12n`, `YOLO12s`. Monolithic ViT (`RT-DETR-L`) fails efficiency ($18.6\text{ ms}, 40.63\%$). |
| **Figure 2** | `thesis_fig2_isolated_dense_cluster_recall.png` | `generate_isolated_thesis_figures.py` (`make_fig2_dense_stand_recall`) | `DINOv3 ViT-T + D-FINE` sets benchmark record in cluster recall ($55.31 \pm 0.92\%$ AR@100). | Overcomes CNN greedy NMS collapse via Fine-grained Distribution Refinement (FDR) iterative coordinate modeling ($+3.76\%$ over `YOLO12s`). |
| **Figure 3** | `thesis_fig3_isolated_overfitting_divergence.png` | `generate_isolated_thesis_figures.py` (`make_fig3_overfitting_trajectories`) | DINOv3 shows zero memorization ($\text{OI} = 0.00 \pm 0.00$). Distillation compresses YOLO12s OI by $-39.7\%$ to $-45.6\%$. | Grounded in Vapnik (1998) statistical learning theory and modified Aburas (2023) Overfitting Index. |
| **Figure 4** | `thesis_fig4_isolated_photogrammetric_centroid_error.png` | `generate_isolated_thesis_figures.py` (`make_fig4_photogrammetric_error`) | `YOLO12s + DBSCAN` delivers $0.457 \pm 0.343\text{ m}$ mean error ($0.354\text{ m}$ median). | Satisfies operational $< 1.0\text{ m}$ threshold ($94.8\%$ compliance) for automated UAV herbicide spray actuation. |
| **Figure 5** | `thesis_fig5_isolated_cross_seed_stability.png` | `generate_isolated_thesis_figures.py` (`make_fig5_cross_seed_stability`) | `YOLO12s` achieves $3.4\times$ tighter variance ($\sigma = 0.75\%$) than `YOLO11s` ($\sigma = 2.53\%$). | Proves Area Attention architectural stability against random seed initialization and data shuffling order. |
| **Figure 6** | `thesis_fig6_isolated_distillation_domain_transfer.png` | `generate_isolated_thesis_figures.py` (`make_fig6_distillation_domain`) | CNN student prefers satellite teacher ($+1.52\%$). ViT student prefers web teacher ($+0.86\%$). | Establishes inductive-domain matching rule (satellite-CNN alignment vs. web-ViT token alignment). |
| **Figure 7** | `thesis_fig7_isolated_precision_recall_curves.png` | `generate_isolated_thesis_figures.py` (`make_fig7_precision_recall_curves`) | `YOLO12s` leads at $\text{IoU}=0.50$ ($F_1 = 0.514$). `DINOv3 ViT-T + D-FINE` leads at $\text{IoU}=0.75$ ($F_1 = 0.350$). | Demonstrates operational trade-off: coarse reconnaissance mapping vs. strict boundary actuation. |
| **Figure 8** | `thesis_fig8_isolated_scale_stratified_ap.png` | `generate_isolated_thesis_figures.py` (`make_fig8_scale_sensitivity`) | D-FINE wins small saplings ($31.85\%$) and large groves ($62.10\%$). YOLO12s wins medium solitary crowns ($53.15\%$). | Morphological growth habit dictates optimal receptive field and token resolution. |
| **Figure 9** | `thesis_fig9_isolated_hardware_batch_scaling.png` | `generate_isolated_thesis_figures.py` (`make_fig9_hardware_batch_scaling`) | `YOLO12s` throughput scales from $204 \to 328\text{ FPS}$ ($+60.7\%$). `YOLO12n` scales from $345 \to 645\text{ FPS}$. | Profiled on NVIDIA TensorRT FP16 across batch sizes $B \in \{1, 4, 8, 16\}$. |
| **Figure 10** | `thesis_fig10_isolated_detection_error_breakdown.png` | `generate_isolated_thesis_figures.py` (`make_fig10_error_breakdown`) | DINOv3 minimizes soil false alarms ($4.8\%$) and misses ($16.5\%$). YOLO12s minimizes native tree confusion ($12.3\%$). | Asymmetric ecological cost matrix: soil contamination vs. non-target kill (*Robinia*) vs. eradication failure. |
| **Figure 11** | `thesis_fig11_isolated_radar_map50_map50_95.png` | `generate_radar_plots.py` (`draw_combined_publication_figure`) | Maps all 14 models across mAP@50 and strict mAP(50-95) with $\pm 1\,\text{STD}$ confidence ribbons. | Strict 2D top-down polar geometry with perpendicular tangential error caps ($d\theta = L/r$). |

---

## 5. Theoretical Framework: Overfitting Index (OI) Formulation

Any agent modifying or reporting training dynamics must adhere strictly to the **Vapnik Statistical Learning Theory** formulation adopted for this thesis:

### 5.1. Statistical Learning Foundations
Under Vapnik’s framework [Vapnik 1998, pp. 17–28], training minimizes empirical risk ($R_{\text{emp}}$) over finite training instances. Overfitting occurs when a model memorizes idiosyncrasies of the training distribution (aerial forest tiles), driving $R_{\text{emp}} \to 0$ while true risk on unseen data ($R_{\text{val}}$) stagnates or diverges [Zhang et al., 2016].

### 5.2. Per-Epoch Generalization Gap
Object detection uses compound multi-task loss functions (bounding box regression, classification, distribution focal loss). The generalization gap is defined as:
$$d_{\text{Loss}}(e) = \max\left(0, \, \mathcal{L}_{\text{val}}(e) - \mathcal{L}_{\text{train}}(e)\right)$$
* **Role of $\max(0, \cdot)$:** Strong stochastic augmentations (Mosaic-4, MixUp, random perspective transforms) frequently elevate training loss above validation loss during early epochs ($R_{\text{val}} < R_{\text{emp}}$). The operator prevents transient negative gaps from corrupting the index [Aburas et al., 2023].

### 5.3. Modified Cumulative Overfitting Index
Because computing training-set mAP at every epoch is computationally prohibitive due to NMS candidate filtering [Redmon et al., 2016], accuracy delta is omitted. To penalize late-stage divergence over early stochastic jitter, epochs are weighted linearly:
$$\text{OI} = \sum_{e=1}^N e \cdot d_{\text{Loss}}(e) \quad (N = 100)$$

### 5.4. Architectural Loss Formulations & Incomparability Rule
**CRITICAL RULE FOR AGENTS:** Due to fundamentally different loss formulations, raw numerical OI values are **not directly comparable** across model families:
* **YOLO12s Family:** $\mathcal{L}_{\text{total}} = 0.5\,\mathcal{L}_{\text{BCE}} + 7.5\,\mathcal{L}_{\text{CIoU}} + 1.5\,\mathcal{L}_{\text{DFL}}$
* **DINOv3 / ViT-T Family:** $\mathcal{L}_{\text{total}} = 1.0\,\mathcal{L}_{\text{VFL}} + 2.5\,\mathcal{L}_{\text{GIoU}} + 5.0\,\mathcal{L}_{\text{bbox}}$

Comparisons are valid **only within each family** and between native vs. distilled variants:
* `YOLO12s` (Native): $\text{OI} = 3194.75 \pm 72.48$ (Baseline)
* `YOLO12s (SAT-493M)`: $\text{OI} = 1926.12 \pm 364.34$ (**$-39.7\%$** gap compression)
* `YOLO12s (LVD-1689M)`: $\text{OI} = 1737.61 \pm 985.84$ (**$-45.6\%$** gap compression)
* `DINOv3 ViT-T + D-FINE`: $\text{OI} = 0.00 \pm 0.00$ (Zero memorization; $R_{\text{val}} \le R_{\text{emp}}$ throughout)
* `ViT-T (LVD-1689M)`: $\text{OI} = 0.00 \pm 0.00$ (Zero memorization; fully preserved self-supervised invariance)
* `ViT-T (SAT-493M)`: $\text{OI} = 615.30 \pm 447.78$ (Minor late-epoch divergence)

---

## 6. Visualization & Styling Guardrails for Future Agents

When modifying existing plots or creating new figures, agents **MUST** obey the following design rules:

1. **Resolution & Typography:**
   * Global DPI must be `dpi=300`. Export with `bbox_inches='tight', pad_inches=0.18..0.25`.
   * Standard sans-serif fonts: `DejaVu Sans`, `Arial`, or `Helvetica`. Bold section/panel titles.
2. **Zero Callout Balloons / Speech Bubbles:**
   * **PROHIBITED:** Never draw speech bubbles, cartoon balloons, callout boxes, or narrative badges on plots.
   * **RULE:** Figures must contain only data lines, bars, markers, error bounds, and concise coordinate/threshold lines. Move explanatory text into GitHub-style `> [!NOTE]` callouts in the markdown documentation.
3. **No Qualitative Ranking Badges:**
   * **PROHIBITED:** Never insert subjective terms (`[Champion]`, `[Winner]`, `[Top]`, `[Lowest]`) on figure canvases, legends, tick labels, or markdown table headers.
   * **RULE:** Express performance superiority through bold numbers, error corridors, or objective textual discussion.
4. **Standardized Model Naming:**
   * Always use: `YOLO12s (SAT-493M)`, `YOLO12s (LVD-1689M)`, `ViT-T (SAT-493M)`, `ViT-T (LVD-1689M)`.
5. **Statistical Dispersion:**
   * Always report metric values with sample dispersion: $\text{Mean} \pm 1\,\text{STD}$.
6. **Polar Radar Plots:**
   * **PROHIBITED:** Do not use `marker='_'` for radial error caps (this renders Cartesian horizontal dashes that look skewed at $45^\circ$ angles).
   * **RULE:** Compute geometrically true tangential perpendicular arc segments normal to the radial spoke: $d\theta = L / r$.
7. **Zero Occlusion / Collision:**
   * Verify axis label padding (`labelpad=10`), subplots spacing (`top=0.88`, `bottom=0.14`), and bar height headroom (`ylim`).
   * For stacked bars (e.g., Fig 10), place the legend in 2 columns centered at `(0.50, 0.98)` with `ylim(0, 138)` to eliminate overlap with the tops of $100\%$ bars.

---

## 7. Multi-Mirror Synchronization Protocol

To guarantee reproducibility across development, backup, and conversational contexts, the following three directories must remain in **100% byte-for-byte synchronization**:

1. **Local Repository:** `C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\thesis_evaluation\`
2. **Google Drive Mirror:** `C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D\`
3. **Brain Artifact Workspace:** `C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363\`

Whenever a script generates or updates an artifact, the script itself should iterate over all mirror paths and write to each destination directly. Verify synchronization with the following check:

```powershell
python -c "
import os
dirs = [r'thesis_evaluation', r'C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D']
files = ['thesis_figures_catalog.md', 'thesis_fig3_isolated_overfitting_divergence.png', 'thesis_fig11_isolated_radar_map50_map50_95.png']
for f in files:
    s0 = os.path.getsize(os.path.join(dirs[0], f))
    s1 = os.path.getsize(os.path.join(dirs[1], f))
    print(f'{f}: {s0} vs {s1} -> {\"OK\" if s0==s1 else \"MISMATCH\"}')
"
```

---

## 8. Literature Citation Standards (Knowledge Base Integration)

When adding or revising discussion sections in `thesis_figures_catalog.md`, agents must ground all assertions in literature citations sourced from the central knowledge base located at:
`C:\Users\emilb\My Drive\Unterlagen_Studium\_MSc\____Master_Thesis_Work____\_Literature_Writing\central_knowledge_base`

Key canonical references:
* **Statistical Learning Theory & Overfitting:** Vapnik (1998), Zhang et al. (2016), Aburas et al. (2023).
* **Architecture:** Tian et al. (2025) [YOLOv12 Area Attention], Peng et al. (2024) [D-FINE FDR], Simeoni et al. (2025) [DINOv3], Redmon et al. (2016) [YOLO].
* **Remote Sensing & Ecology:** Kowarik & Säumel (2007) [*Ailanthus* biology], Naharki et al. (2023, 2024) [Drone detection of *Ailanthus*], Burkholder et al. (2011) [Leaf reflectance separability], Turner et al. (2014) [UAV direct georeferencing].
* **Field Robotics:** Zachariah et al. (2026) [MapForest], Soler et al. (2024) [Chemical eradication and spray drift], Ester et al. (1996) [DBSCAN spatial clustering].
