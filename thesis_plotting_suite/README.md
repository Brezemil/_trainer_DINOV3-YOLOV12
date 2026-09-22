# Master's Thesis Plotting Suite & Interactive Evaluation Workspace

This folder provides a self-contained, publication-ready plotting environment for reproducing all figures from the Master's Thesis:
> **High-Resolution UAV Detection, Geolocation, and Knowledge Distillation of Invasive Ailanthus altissima Canopies**  
> *Author:* Emil Brezovsky  
> *Degree Program:* Master of Science in Geoinformatics & Remote Sensing

---

## 📁 Folder Structure

```text
thesis_plotting_suite/
├── pixi.toml                       # Dedicated Pixi environment (Python 3.11, JupyterLab, Matplotlib, Scipy, Seaborn)
├── README.md                       # Operational user guide
├── thesis_plotting_suite.ipynb     # Master interactive Jupyter Notebook with all figures & markdown analysis
├── generate_all_figures.py         # Headless CLI generator for batch rendering
├── data/                           # Self-contained data dependencies (Zero external path requirements)
│   ├── benchmark_metrics.json      # Verified quantitative metrics across 14 models & 3 random seeds
│   └── oi_curves_data.json         # 100-epoch training and validation loss curves & Overfitting Index (OI) stats
└── output_figures/                 # Generated 300 DPI publication figures
    ├── thesis_fig1_isolated_pareto_latency.png
    ├── thesis_fig2_isolated_dense_cluster_recall.png
    ├── thesis_fig2b_top_performers_dense_recall.png
    ├── thesis_fig3_isolated_overfitting_divergence.png
    ├── thesis_fig4_isolated_photogrammetric_centroid_error.png
    ├── thesis_fig4b_photogrammetric_raycasting_cdf.png
    ├── thesis_fig5_isolated_cross_seed_stability.png
    ├── thesis_fig6_isolated_distillation_domain_transfer.png
    ├── thesis_fig7_isolated_precision_recall_curves.png
    ├── thesis_fig8_isolated_scale_stratified_ap.png
    ├── thesis_fig8b_top_performers_scale_ap.png
    ├── thesis_fig9_isolated_hardware_batch_scaling.png
    ├── thesis_fig10_isolated_detection_error_breakdown.png
    └── thesis_fig11_isolated_radar_map50_map50_95.png
```

---

## 🚀 Quickstart with Pixi

The directory includes its own isolated `pixi.toml` environment with all necessary scientific dependencies (`jupyterlab`, `matplotlib`, `scipy`, `seaborn`, `pandas`, `opencv`).

### 1. Launch the Interactive Jupyter Notebook
```bash
cd thesis_plotting_suite
pixi run notebook
```
or launch JupyterLab:
```bash
pixi run jupyter
```
Open `thesis_plotting_suite.ipynb` in the browser to interactively inspect, re-plot, or adjust visual parameters for each figure.

### 2. Batch-Generate All Figures Headlessly
To generate all 13 figures in one pass from the terminal:
```bash
cd thesis_plotting_suite
pixi run plot-all
```
or run with standard Python:
```bash
python generate_all_figures.py
```
All outputs are automatically saved to `output_figures/` at 300 DPI.

---

## 📊 Summary of Evaluated Figures

| Figure ID | File Name | Key Finding |
| :---: | :--- | :--- |
| **Figure 1** | `thesis_fig1_isolated_pareto_latency.png` | `YOLO12s` establishes global Pareto apex ($49.91 \pm 0.75\%$) at $4.9\text{ ms}$ ($204.1\text{ FPS}$). Lower bar panel details parameter allocation ($18.0\text{M}$ trainable vs $257.0\text{M}$ frozen). |
| **Figure 2** | `thesis_fig2_isolated_dense_cluster_recall.png` | `DINOv3 ViT-T + D-FINE` sets benchmark record ($55.31 \pm 0.92\%$ AR@100), overcoming greedy NMS collapse via FDR probability modeling. |
| **Figure 2B** | `thesis_fig2b_top_performers_dense_recall.png` | Compares paradigm top performers: ViT-T + D-FINE ($55.31\%$), YOLO12s DINO ($52.04\%$), YOLO12s ($51.55\%$), ViT-T LVD ($51.20\%$), YOLO12s SAT ($49.80\%$). |
| **Figure 3** | `thesis_fig3_isolated_overfitting_divergence.png` | Empirical optimization dynamics over 100 epochs. DINOv3 exhibits zero memorization ($\text{OI} = 0.00$), while distillation regularizes YOLO12s OI by $-39.7\%$ to $-45.6\%$. |
| **Figure 4** | `thesis_fig4_isolated_photogrammetric_centroid_error.png` | `YOLO12s + DBSCAN` delivers $0.457 \pm 0.343\text{ m}$ mean error ($0.354\text{ m}$ median), satisfying the $< 1.0\text{ m}$ spray drone drift envelope ($94.8\%$ compliance). |
| **Figure 4B** | `thesis_fig4b_photogrammetric_raycasting_cdf.png` | Cumulative Distribution Function (CDF) of horizontal localization error: demonstrates $94.8\%$ sub-meter operational compliance for `YOLO12s + DBSCAN` vs. $64.3\%$ for raw direct raycasting. |
| **Figure 5** | `thesis_fig5_isolated_cross_seed_stability.png` | Cross-seed reproducibility: `YOLO12s` achieves $3.4\times$ tighter variance ($\sigma = 0.75\%$) than `YOLO11s` baseline ($\sigma = 2.53\%$). |
| **Figure 6** | `thesis_fig6_isolated_distillation_domain_transfer.png` | Pretraining inductive bias matching: CNN students align with satellite features ($+1.52\%$), while ViT students align with natural web features ($+0.86\%$). |
| **Figure 7** | `thesis_fig7_isolated_precision_recall_curves.png` | Multi-threshold trade-off: YOLO12s leads coarse reconnaissance ($\text{IoU}=0.50$), while D-FINE leads strict boundary actuation ($\text{IoU}=0.75$). |
| **Figure 8** | `thesis_fig8_isolated_scale_stratified_ap.png` | Scale sensitivity: D-FINE wins small saplings ($31.85\%$) and large groves ($62.10\%$). YOLO12s Area Attention wins medium solitary crowns ($53.15\%$). |
| **Figure 8B** | `thesis_fig8b_top_performers_scale_ap.png` | Scale sensitivity and precision across the 5 top paradigm performers. |
| **Figure 9** | `thesis_fig9_isolated_hardware_batch_scaling.png` | TensorRT FP16 batch scalability ($B \in \{1, 4, 8, 16\}$): `YOLO12s` throughput scales from $204 \to 328\text{ FPS}$. |
| **Figure 10** | `thesis_fig10_isolated_detection_error_breakdown.png` | Multi-class error breakdown: DINOv3 minimizes soil false alarms ($4.8\%$) and misses ($16.5\%$), while YOLO12s minimizes native tree confusion ($12.3\%$). |
| **Figure 11** | `thesis_fig11_isolated_radar_map50_map50_95.png` | Polar radar profiles across all 14 models with true 2D tangential perpendicular error caps ($d\theta = L/r$). |

---

## 🔬 Data Sources

- `benchmark_metrics.json`: Compiled from full-cohort test evaluation on $N_{\text{test}} = 510$ georeferenced orthophoto tiles ($1024 \times 1024$, $2.1\text{ cm/px}$ GSD; 7,035 ground-truth canopies) across seeds `42`, `100`, and `999`.
- `oi_curves_data.json`: Extracted per-epoch training and validation loss logs from WandB histories and YOLO run reports over 100 epochs.
