# Master Thesis Evaluation & Runs Database (`_thesis_eval`)

**Master's Thesis:** *High-Resolution UAV Detection, Geolocation, and Knowledge Distillation of Invasive Ailanthus altissima Canopies*  
**Author / Candidate:** Emil Brezovsky  
**Target Directory:** `C:\Users\emilb\My Drive\_thesis_eval`  
**Mirrors:**
- Local Repo: `C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\thesis_evaluation\`
- Cloud Backup: `C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D\`
- CLI Brain: `C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363\`

---

## 1. Directory Layout & Organization

The `_thesis_eval` directory is designed as the permanent, authoritative evaluation repository for the master's thesis. All benchmark tables, publication figures, per-epoch metric histories, and the master runs database are structured logically for direct programmatic consumption:

```text
_thesis_eval/
├── master_runs_database.csv              # Unified queryable pandas table (47 runs × 58 attributes)
├── master_runs_database.json             # Formatted JSON equivalent of the master database
├── README.md                             # This authoritative reference guide
│
├── benchmark_tables/                     # Core evaluation CSV tables
│   ├── model_comparison_overview.csv     # Unlabeled testset standard c=0.25 evaluation across 15 models
│   ├── model_comparison_optimal_f1.csv   # Unlabeled testset calibrated optimal c* evaluation
│   └── model_comparison_delta.csv        # Delta metrics (background FP reduction %, F1 gain)
│
├── figures/                              # 10 publication-ready 300 DPI figures
│   ├── fig1_prediction_counts_by_model.png                      # Total detections & positive/negative split at c=0.25
│   ├── fig1b_prediction_counts_optimal_f1.png                   # Total detections & split at optimal c*
│   ├── fig2_positive_vs_negative_detection_rates.png            # Detection rates per tile category at c=0.25
│   ├── fig2b_positive_vs_negative_detection_rates_optimal_f1.png# Detection rates per tile category at optimal c*
│   ├── fig3_conf025_vs_optimal_f1_false_alarm_reduction.png     # Calibrated false alarm reduction & F1 delta
│   ├── fig4_sample_overlay_dense_canopies.png                   # Spatial prediction overlay: Dense canopies (c=0.25)
│   ├── fig4b_sample_overlay_dense_canopies_optimal_f1.png        # Spatial prediction overlay: Dense canopies (c*)
│   ├── fig5_sample_overlay_solitary_canopy.png                  # Spatial prediction overlay: Solitary canopy
│   ├── fig6_sample_overlay_background_false_alarm.png           # Spatial prediction overlay: Background false alarm (c=0.25)
│   └── fig6b_sample_overlay_background_false_alarm_optimal_f1.png# Spatial prediction overlay: Background false alarm (c*)
│
└── metric_histories/                     # 109 per-epoch loss & validation trajectories (.csv)
    ├── yolo12s_seed_*_history.csv        # YOLO12s training/val loss & mAP curves
    ├── yolo12s_triple_dino3_*.csv        # Multi-scale Triple DINOv3 training curves
    ├── finetune_distill_*.csv            # Distillation finetuning histories
    ├── pretrain_distill_*.csv            # Distillation pretraining alignment histories
    ├── vitt16_*.csv                      # Vision Transformer D-FINE histories
    └── yolo11* / yolo26* / rtdetr*.csv   # Baseline CNN and DETR trajectories
```

---

## 2. Master Database Column Dictionary (58 Attributes)

`master_runs_database.csv` aggregates data across 47 training runs from both `_trainer_lightly` and `_trainer_DINOV3-YOLOV12`. Every attribute is explicitly typed and documented below:

| Column Name | Type | Description |
| :--- | :---: | :--- |
| `run_id` | string | Unique Weights & Biases (WandB) run identifier (e.g. `9d6dvly1`, `ovdgoz21`). |
| `run_name` | string | Canonical run name used during training execution. |
| `canonical_model` | string | Standardized thesis model label (e.g. `YOLO12s`, `DINOv3 ViT-T + D-FINE`, `YOLO12s Triple DINOv3`). |
| `arch_family` | string | High-level architectural paradigm: `Pure CNN`, `Vision Transformer`, `Distilled Student`, `Multi-Scale Fused`. |
| `model_variant` | string | Specific model variant name in repository logs. |
| `seed` | int | Random seed for weight initialization and batch shuffling (`42`, `100`, `999`). |
| `epochs` | int | Total scheduled training epochs ($100$, $150$, or $300$). |
| `batch_size` | int | Mini-batch size used during training ($4$, $8$, or $16$). |
| `imgsz` | int | Training and inference image resolution in pixels ($1024 \times 1024$). |
| `lr0` | float | Initial learning rate $\eta_0$ ($0.01$ for SGD, $0.0001$ for AdamW). |
| `lrf` | float | Final learning rate ratio $\eta_f / \eta_0$ (cosine annealing schedule). |
| `optimizer` | string | Optimization algorithm (`SGD`, `AdamW`, `auto`). |
| `is_distilled` | bool | Boolean flag indicating whether feature-based knowledge distillation was applied. |
| `teacher_model` | string | Teacher network: `DINOv3 SAT-493M`, `DINOv3 LVD-1689M`, or `None`. |
| `backbone` | string | Underlying feature extraction backbone (e.g. `AreaAttention`, `DINOv3 ViT-T`, `YOLO12s + DINOv3 ViT-B/16`). |
| `detection_head` | string | Prediction head: `Decoupled Head`, `D-FINE FDR Head`, `Multi-Scale Decoupled Head`. |
| `params_m` | float | Parameter count in millions ($2.3\text{ M}$ to $95.8\text{ M}$). |
| `latency_ms` | float | Hardware latency on NVIDIA TensorRT FP16 ($1024 \times 1024$, batch 1) in milliseconds. |
| `fps` | float | Inference throughput in Frames Per Second ($\text{FPS} = 1000 / \text{latency}$). |
| `train_loss_min` | float | Minimum training loss observed during the run. |
| `train_loss_final` | float | Final training loss at the last epoch ($R_{\text{emp}}$). |
| `val_loss_min` | float | Minimum validation loss observed during training ($R_{\text{val}}$). |
| `val_loss_final` | float | Final validation loss at the last epoch. |
| `wandb_best_mAP50` | float | Best validation mAP@50 recorded in WandB telemetry. |
| `wandb_best_mAP50_95`| float | Best validation mAP(50-95) recorded in WandB telemetry. |
| `test_coco_AP` | float | Strict COCO test set mAP(50-95) ($N=1024$ test images). |
| `test_coco_AP50` | float | Strict COCO test set mAP@50. |
| `test_coco_AP75` | float | Strict COCO test set mAP@75 (strict localization accuracy). |
| `test_coco_AP30` | float | Strict COCO test set mAP@30 (coarse canopy detection). |
| `test_coco_AP40` | float | Strict COCO test set mAP@40. |
| `test_coco_AP_small` | float | COCO test set AP for small crowns ($\text{area} < 32^2\text{ px}$). |
| `test_coco_AP_medium`| float | COCO test set AP for medium crowns ($32^2 \le \text{area} < 96^2\text{ px}$). |
| `test_coco_AP_large` | float | COCO test set AP for large crowns ($\text{area} \ge 96^2\text{ px}$). |
| `test_coco_AR_max1` | float | Average Recall with at most 1 detection per image. |
| `test_coco_AR_max10` | float | Average Recall with at most 10 detections per image. |
| `test_coco_AR_max100`| float | Average Recall with at most 100 detections per image (Dense Stand Recall). |
| `test_coco_AR_small` | float | Average Recall for small crowns. |
| `test_coco_AR_medium`| float | Average Recall for medium crowns. |
| `test_coco_AR_large` | float | Average Recall for large crowns. |
| `unlabeled_c025_detections` | int | Total canopy predictions on combined unlabeled testset at default confidence $c=0.25$. |
| `unlabeled_c025_tp` | int | True positive detections inside known positive tiles at $c=0.25$. |
| `unlabeled_c025_fp_bg` | int | False positive detections inside background negative tiles at $c=0.25$. |
| `unlabeled_c025_recall` | float | Empirical recall on positive tiles at $c=0.25$. |
| `unlabeled_c025_precision` | float | Empirical precision across all tiles at $c=0.25$. |
| `unlabeled_c025_f1` | float | Harmonic mean $F_1$ score at $c=0.25$. |
| `unlabeled_c025_fa_density_per_1k` | float | False alarm density per 1,000 background negative tiles at $c=0.25$. |
| `optimal_conf_threshold` | float | Calibrated optimal confidence threshold $c^*$ maximizing $F_1$ score. |
| `unlabeled_opt_detections` | int | Total canopy predictions on combined unlabeled testset at optimal $c^*$. |
| `unlabeled_opt_tp` | int | True positive detections inside positive tiles at optimal $c^*$. |
| `unlabeled_opt_fp_bg` | int | False positive detections inside background negative tiles at optimal $c^*$. |
| `unlabeled_opt_recall` | float | Empirical recall at optimal $c^*$. |
| `unlabeled_opt_precision` | float | Empirical precision at optimal $c^*$. |
| `unlabeled_opt_f1` | float | Peak $F_1$ score at optimal $c^*$. |
| `unlabeled_opt_fa_density_per_1k` | float | Calibrated false alarm density per 1,000 background tiles at optimal $c^*$. |
| `unlabeled_fp_reduction_pct` | float | Percentage reduction in background false alarms: $\frac{\text{FP}_{0.25} - \text{FP}_{c^*}}{\text{FP}_{0.25}} \times 100$. |
| `unlabeled_f1_gain` | float | Absolute gain in $F_1$ score: $F_1(c^*) - F_1(0.25)$. |
| `history_csv` | string | Full path to the per-epoch metric history CSV file. |
| `weight_file` | string | Model checkpoint weight filename. |

---

## 3. Quick-Start Python Recipes

### 3.1. Loading the Database
```python
import pandas as pd
import numpy as np

# Load master database from Drive or local mirror
db_path = r"C:\Users\emilb\My Drive\_thesis_eval\master_runs_database.csv"
df = pd.read_csv(db_path)

print(f"Loaded database: {df.shape[0]} runs, {df.shape[1]} columns")
```

### 3.2. Computing Aggregated Benchmark Statistics ($\text{Mean} \pm \text{STD}$)
```python
# Filter to primary evaluated thesis models with valid test results
primary_models = [
    'YOLO12s', 'YOLO12n', 'YOLO11s', 'YOLO11n', 'YOLO26s', 'YOLO26n',
    'RT-DETR-L', 'DINOv3 ViT-T + D-FINE',
    'YOLO12s (SAT-493M)', 'YOLO12s (LVD-1689M)',
    'ViT-T (SAT-493M)', 'ViT-T (LVD-1689M)',
    'YOLO12s Triple DINOv3'
]

sub = df[df['canonical_model'].isin(primary_models)]

summary = sub.groupby('canonical_model').agg({
    'params_m': 'first',
    'latency_ms': 'first',
    'fps': 'first',
    'test_coco_AP50': ['mean', 'std'],
    'test_coco_AP': ['mean', 'std'],
    'test_coco_AR_max100': ['mean', 'std'],
    'unlabeled_opt_f1': ['mean', 'std'],
    'unlabeled_fp_reduction_pct': ['mean', 'std']
}).reset_index()

print(summary.to_string())
```

### 3.3. Extracting the Latency-Accuracy Pareto Frontier
```python
# Compute Pareto points (optimizing test_coco_AP50 and minimizing latency_ms)
pareto_candidates = sub.groupby('canonical_model').agg({
    'latency_ms': 'mean',
    'test_coco_AP50': 'mean'
}).reset_index()

pareto_points = []
for idx, row in pareto_candidates.iterrows():
    is_pareto = True
    for other_idx, other in pareto_candidates.iterrows():
        if (other['latency_ms'] <= row['latency_ms'] and 
            other['test_coco_AP50'] > row['test_coco_AP50']):
            is_pareto = False
            break
    if is_pareto:
        pareto_points.append(row)

pareto_df = pd.DataFrame(pareto_points).sort_values('latency_ms')
print("Empirical Pareto Frontier Models:")
print(pareto_df.to_string(index=False))
```

### 3.4. Inspecting Per-Epoch Loss Trajectories
```python
# Select a run and load its metric history CSV
run = df[df['run_name'] == 'yolo12s_seed_42'].iloc[0]
history_file = run['history_csv']

if pd.notna(history_file):
    hist_df = pd.read_csv(history_file)
    print(f"Loaded {len(hist_df)} epochs of training telemetry for {run['canonical_model']}")
    print(hist_df[['_step', 'train/loss', 'val/loss']].head())
```

---

## 4. Maintenance and Extension Protocol

To update the database when new training runs, evaluation checkpoints, or test metrics are produced:
1. Ensure all training logs (`results.csv` or WandB history) and evaluation files (`*_coco_metrics.json`) reside in their canonical directories.
2. Run the master compilation pipeline:
   ```powershell
   python thesis_evaluation/build_master_eval_db.py
   ```
3. The script automatically rebuilds `master_runs_database.csv` and `master_runs_database.json` and synchronizes them across all 4 mirrors:
   - `C:\Users\emilb\My Drive\_thesis_eval\`
   - `thesis_evaluation\`
   - `C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D\`
   - Antigravity Brain Workspace
