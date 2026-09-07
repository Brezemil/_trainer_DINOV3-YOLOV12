# 🤖 AGENT DIRECTIVES: Integrating Exported YOLOv12s-Triple-DINOv3 Weights for Inference & Benchmark Testing

This guide is written for an AI coding assistant, autonomous agent, or developer operating on another machine. It provides complete operational rules, architectural specifications, critical framework gotchas, and self-contained Python recipes to integrate, test, and benchmark the exported model weights.

---

## 1. Executive Package Manifest

```
export/
├── AGENTS.md                                                    <-- This operational guide
├── f1_confidence_optimization_analysis.md                       <-- Comprehensive scientific thesis artifact
├── artifacts/                                                   <-- Thesis analysis artifacts & reports
│   └── f1_confidence_optimization_analysis.md
├── weights/                                                     <-- Full 300-epoch trained model checkpoints
│   ├── yolo12s_triple_dino3_vitb16_seed_42_best.pt              <-- Seed 42 Best Validation Checkpoint (550.9 MB)
│   ├── yolo12s_triple_dino3_vitb16_seed_42_last.pt              <-- Seed 42 Final Epoch Checkpoint (550.9 MB)
│   ├── yolo12s_triple_dino3_vitb16_seed_100_best.pt             <-- Seed 100 Best Validation Checkpoint (550.9 MB)
│   ├── yolo12s_triple_dino3_vitb16_seed_100_last.pt             <-- Seed 100 Final Epoch Checkpoint (550.9 MB)
│   ├── yolo12s_triple_dino3_vitb16_seed_999_best.pt             <-- Seed 999 Best Validation Checkpoint (550.9 MB)
│   └── yolo12s_triple_dino3_vitb16_seed_999_last.pt             <-- Seed 999 Final Epoch Checkpoint (550.9 MB)
├── evaluation_results/                                          <-- Ground-truth Hold-Out Test & Val COCO Benchmarks
│   ├── benchmark_statistical_report.json                        <-- 3-Seed Mean ± Std summary JSON (Standard COCO evaluation)
│   ├── evaluation_summary.csv                                   <-- Detailed metrics table across all runs
│   ├── optimal_f1_statistical_report.json                       <-- 3-Seed Mean ± Std summary JSON (Calibrated Optimal F1 point)
│   ├── optimal_f1_evaluation_summary.csv                        <-- Calibrated Optimal F1 metrics table across all runs
│   ├── coco_gt_val_8eddf691.json                                <-- Validation ground truth COCO annotations (N=510)
│   ├── coco_gt_test_f48b69af.json                               <-- Hold-out test ground truth COCO annotations (N=510)
│   ├── yolo12s_triple_dino3_vitb16_seed_*_VAL_coco_predictions.json
│   ├── yolo12s_triple_dino3_vitb16_seed_*_VAL_coco_metrics.json
│   ├── yolo12s_triple_dino3_vitb16_seed_*_TEST_coco_predictions.json
│   ├── yolo12s_triple_dino3_vitb16_seed_*_TEST_coco_metrics.json
│   ├── yolo12s_triple_dino3_vitb16_seed_*_opt_f1_TEST_coco_predictions.json
│   └── yolo12s_triple_dino3_vitb16_seed_*_opt_f1_TEST_coco_metrics.json
├── predictions/                                                 <-- Multi-Format Predictions (COCO JSON, YOLO TXT, Tabular CSV)
│   ├── coco_format/                                             <-- COCO format detection JSONs (mapped to GT test & val image IDs)
│   │   ├── yolo12s_triple_dino3_vitb16_seed_*_opt_f1_TEST_coco_predictions.json (Seeds 42, 100, 999)
│   │   ├── yolo12s_triple_dino3_vitb16_seed_*_TEST_coco_predictions.json        (Seeds 42, 100, 999)
│   │   └── yolo12s_triple_dino3_vitb16_seed_*_VAL_coco_predictions.json         (Seeds 42, 100, 999)
│   ├── yolo_format/                                             <-- Normalized YOLO format txt bounding boxes [class x y w conf]
│   │   ├── yolo12s_triple_dino3_vitb16_seed_*_opt_f1/             (Seeds 42, 100, 999, 510 tiles each)
│   │   ├── yolo12s_triple_dino3_vitb16_seed_*_test/               (Seeds 42, 100, 999, 510 tiles each)
│   │   └── yolo12s_triple_dino3_vitb16_seed_*_val/                (Seeds 42, 100, 999, 510 tiles each)
│   ├── yolo12s_triple_dino3_vitb16_seed_42/                     <-- Standard model bundle: coco_predictions.json, predictions.csv, yolo_labels/
│   ├── yolo12s_triple_dino3_vitb16_seed_100/                    <-- Standard model bundle: coco_predictions.json, predictions.csv, yolo_labels/
│   └── yolo12s_triple_dino3_vitb16_seed_999/                    <-- Standard model bundle: coco_predictions.json, predictions.csv, yolo_labels/
├── training_artifacts/                                          <-- Training Curves, Confusion Matrices, Loss CSVs
│   ├── seed_42/                                                 <-- F1_curve, PR_curve, results.png, results.csv (with train & val loss), args.yaml
│   ├── seed_100/                                                <-- F1_curve, PR_curve, results.png, results.csv (with train & val loss), args.yaml
│   └── seed_999/                                                <-- F1_curve, PR_curve, results.png, results.csv (with train & val loss), args.yaml
└── wandb_logs/                                                  <-- Full Telemetry, Output Logs, and 300-Epoch History
    ├── wandb_runs_overview.json                                 <-- Master index of all runs with URLs & summary metrics (including train & val loss)
    ├── runs_summary.csv                                         <-- Consolidated tabular metrics (train/val loss, mAP, precision, recall, hyperparameters)
    ├── runs_summary.json                                        <-- JSON version of runs summary table
    ├── metric_histories/                                        <-- Standardized cross-project metric history CSVs
    │   ├── yolo12s_triple_dino3_vitb16_seed_42_ovdgoz21_history.csv
    │   ├── yolo12s_triple_dino3_vitb16_seed_100_p96dlaj5_history.csv
    │   └── yolo12s_triple_dino3_vitb16_seed_999_ftxj3r9n_history.csv
    ├── seed_42_ovdgoz21/                                        <-- wandb_history.csv/.json, output.log, config.yaml, .wandb binary, media/
    ├── seed_100_p96dlaj5/                                       <-- wandb_history.csv/.json, output.log, config.yaml, .wandb binary, media/
    ├── seed_999_ftxj3r9n/                                       <-- wandb_history.csv/.json, output.log, config.yaml, .wandb binary, media/
    └── aborted_test_runs/                                       <-- Archived local aborted test launches with run configs and logs
```

---

## 2. Model Architecture & Specifications

| Parameter | Value / Description |
| :--- | :--- |
| **Model Architecture** | `YOLOv12s-triple-dino3-vitb16` |
| **Object Detection Backbone** | YOLOv12s (Area-Attention, FlashAttention/SDPA support) |
| **Vision Foundation Backbone** | Meta DINOv3 ViT-B/16 (`facebook/dinov3-vitb16-pretrain`, 768 dim, patch size 16) |
| **Integration Paradigm** | **Triple Scale Fusion (`triple`)** — DINOv3 ViT features are projected and fused into the multi-scale feature pyramid at P3 (128×128), P4 (64×64), and P5 (32×32) before the neck and detection head |
| **Total Model Parameters** | 274,915,805 (~275M parameters) |
| **Total Layers** | 1,116 layers |
| **Input Resolution** | 1024×1024 pixels |
| **Target Dataset** | *Ailanthus altissima* aerial canopy detection benchmark |
| **Class Label** | `0: A. altissima` |
| **Training Duration** | 300 epochs per seed (SGD optimizer, imgsz 1024, batch 4) |

---

## 3. Ground-Truth Verification Matrix (Hold-Out Benchmark)

Use these hold-out test set ($N=510$ tiles, 1024×1024) and validation set ($N=510$ tiles) metrics to verify that your inference and evaluation environment reproduces the exact benchmark results:

### Hold-Out Test Set Benchmark ($N=510$)

| Model Run | Seed | mAP@0.50 | mAP@0.50:0.95 | mAP@0.75 | mAP@0.30 | mAP@0.40 | AR@100 | WandB Run ID |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `yolo12s_triple_dino3_vitb16_seed_42` | 42 | **46.16%** | **23.08%** | 20.22% | 58.05% | 52.27% | 52.93% | [`ovdgoz21`](https://wandb.ai/brezo-boku-vienna/_baseline/runs/ovdgoz21) |
| `yolo12s_triple_dino3_vitb16_seed_100` | 100 | 45.86% | 22.32% | 19.39% | 57.52% | 51.90% | 51.53% | [`p96dlaj5`](https://wandb.ai/brezo-boku-vienna/_baseline/runs/p96dlaj5) |
| `yolo12s_triple_dino3_vitb16_seed_999` | 999 | 46.27% | 22.92% | **20.13%** | 57.95% | 52.81% | 51.65% | [`ftxj3r9n`](https://wandb.ai/brezo-boku-vienna/_baseline/runs/ftxj3r9n) |
| **3-Seed Mean ± Std** | — | **46.10% ± 0.17%** | **22.77% ± 0.33%** | **19.91% ± 0.37%** | **57.84% ± 0.23%** | **52.33% ± 0.37%** | **52.04% ± 0.64%** | — |

### Validation Set Benchmark ($N=510$)

| Model Run | Seed | mAP@0.50 | mAP@0.50:0.95 | mAP@0.75 | mAP@0.30 | mAP@0.40 | AR@100 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `yolo12s_triple_dino3_vitb16_seed_42` | 42 | 59.26% | 31.65% | 29.88% | 65.93% | 62.07% | 57.60% |
| `yolo12s_triple_dino3_vitb16_seed_100` | 100 | 56.51% | 29.69% | 27.36% | 62.74% | 60.27% | 55.21% |
| `yolo12s_triple_dino3_vitb16_seed_999` | 999 | 57.71% | 31.28% | 29.14% | 63.07% | 60.58% | 58.58% |
| **3-Seed Mean ± Std** | — | **57.83% ± 1.13%** | **30.87% ± 0.85%** | **28.79% ± 1.06%** | **63.91% ± 1.43%** | **60.97% ± 0.79%** | **57.13% ± 1.41%** |

### Training and Validation Loss Benchmarks (300 Epochs)

Both individual component losses (`box_loss`, `cls_loss`, `dfl_loss`) and total losses (`train/loss`, `val/loss`) are logged for all 300 epochs in `wandb_history.csv`, `wandb_history.json`, `metric_histories/`, and `results.csv`:

| Model Run | Seed | Final Train Loss | Final Val Loss | Best Val Loss (Epoch) | Final Train Breakdown (box / cls / dfl) | Final Val Breakdown (box / cls / dfl) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `yolo12s_triple_dino3_vitb16_seed_42` | 42 | **4.4131** | **4.7384** | 4.6750 (Ep. 268) | 1.3436 / 1.5331 / 1.5365 | 1.4460 / 1.5422 / 1.7502 |
| `yolo12s_triple_dino3_vitb16_seed_100` | 100 | **4.3924** | **4.9049** | 4.6288 (Ep. 243) | 1.3298 / 1.5406 / 1.5219 | 1.4854 / 1.6218 / 1.7977 |
| `yolo12s_triple_dino3_vitb16_seed_999` | 999 | **4.3755** | **4.7872** | 4.6833 (Ep. 258) | 1.3369 / 1.5152 / 1.5233 | 1.4696 / 1.5416 / 1.7760 |
| **3-Seed Mean ± Std** | — | **4.3937 ± 0.0188** | **4.8102 ± 0.0856** | **4.6624 ± 0.0294** | **1.3368 / 1.5296 / 1.5272** | **1.4670 / 1.5685 / 1.7746** |

---

## 4. Critical Framework Gotchas & Implementation Directives

> [!IMPORTANT]
> **1. Custom Ultralytics Fork Installation Requirement**
> The model architecture (`YOLOv12s-triple-dino3-vitb16`) introduces custom DINOv3 feature injection layers (`TripleDINO`, `DINOv3`) and Area Attention blocks inside `ultralytics/nn/modules`.
> If you load the `.pt` weights in a vanilla `pip install ultralytics` environment without this fork, it will fail with `ModuleNotFoundError` or `KeyError` on custom module types.
> **Fix**: In the destination repository, install this repository's codebase in editable mode:
> ```bash
> git clone https://github.com/Brezemil/_trainer_DINOV3-YOLOV12.git
> cd _trainer_DINOV3-YOLOV12
> pip install -e .
> ```

> [!CAUTION]
> **2. PyTorch 2.6+ Default `weights_only=True` Gotcha**
> In PyTorch 2.6+, `torch.load()` changed its default argument `weights_only` from `False` to `True`. Checkpoints containing Ultralytics `DetectionModel` objects will fail with:
> `_pickle.UnpicklingError: Weights only load failed ... Unsupported global: GLOBAL ultralytics.nn.tasks.DetectionModel`
> **Fix**: Always use the Ultralytics high-level API `from ultralytics import YOLO; model = YOLO("path/to/weights.pt")`, or if calling `torch.load` manually, explicitly pass:
> `torch.load("path/to/weights.pt", weights_only=False, map_location=device)`

> [!NOTE]
> **3. FlashAttention vs. SDPA Fallback**
> If your destination machine has an RTX 40-series, 50-series, or data center GPU, but does not have compiled `flash_attn` wheels installed, the codebase automatically falls back to PyTorch's native `F.scaled_dot_product_attention` without error and with identical numerical accuracy.

> [!TIP]
> **4. VRAM & Batch Sizing Recommendations**
> - **16 GB VRAM** (e.g. RTX 4080 / RTX 5080): Use `batch=4` at `imgsz=1024` for inference/validation. Peak VRAM usage is ~9.5 GB.
> - **24 GB VRAM** (e.g. RTX 3090 / RTX 4090 / A10G): Use `batch=8` or `batch=16` at `imgsz=1024`.
> - **8–12 GB VRAM**: Use `batch=1` or `batch=2` with `half=True` (FP16 inference).

---

## 5. Self-Contained Ready-to-Run Python Recipes

### Recipe 1: Single Image Inference & Visualization

```python
#!/usr/bin/env python3
"""Run single-image inference with exported YOLOv12s-Triple-DINOv3 weights."""

from pathlib import Path
from ultralytics import YOLO

# 1. Path to exported weights
WEIGHTS_PATH = "export/weights/yolo12s_triple_dino3_vitb16_seed_42_best.pt"
IMAGE_PATH = "test_image.jpg"

# 2. Load model
model = YOLO(WEIGHTS_PATH)

# 3. Predict with recommended confidence and IoU thresholds
results = model.predict(
    source=IMAGE_PATH,
    conf=0.25,        # Confidence threshold
    iou=0.7,          # NMS IoU threshold
    imgsz=1024,       # Mandatory input size for optimal DINOv3 alignment
    device=0,         # '0' for CUDA GPU, or 'cpu'
    save=True,        # Save annotated image
    save_txt=True,    # Save YOLO format bounding box annotations
    project="inference_output",
    name="single_test",
    exist_ok=True,
)

# 4. Print detections
for box in results[0].boxes:
    cls_id = int(box.cls[0].item())
    cls_name = model.names[cls_id]
    conf = float(box.conf[0].item())
    xyxy = box.xyxy[0].tolist()
    print(f"Detected: {cls_name} (conf={conf:.3f}) at [{xyxy[0]:.1f}, {xyxy[1]:.1f}, {xyxy[2]:.1f}, {xyxy[3]:.1f}]")
```

---

### Recipe 2: Directory Batch Inference & COCO Predictions JSON Export

```python
#!/usr/bin/env python3
"""Run directory batch inference and export predictions in COCO JSON format."""

import json
from pathlib import Path
from ultralytics import YOLO

WEIGHTS_PATH = "export/weights/yolo12s_triple_dino3_vitb16_seed_42_best.pt"
IMAGES_DIR = "path/to/test/images"
OUTPUT_JSON = "batch_predictions_coco.json"

model = YOLO(WEIGHTS_PATH)

# Run batch prediction
results = model.predict(
    source=IMAGES_DIR,
    conf=0.001,       # Low threshold for evaluation / mAP calculation
    iou=0.7,
    imgsz=1024,
    device=0,
    batch=4,
    stream=True,      # Stream generator for memory efficiency
)

coco_predictions = []
for res in results:
    img_stem = Path(res.path).stem
    for box in res.boxes:
        cls_id = int(box.cls[0].item())
        score = float(box.conf[0].item())
        # Convert xyxy to COCO format [xmin, ymin, width, height]
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        w = x2 - x1
        h = y2 - y1

        coco_predictions.append({
            "image_id": img_stem,
            "category_id": cls_id + 1,  # 1-indexed for COCO format
            "bbox": [round(x1, 3), round(y1, 3), round(w, 3), round(h, 3)],
            "score": round(score, 5),
        })

with open(OUTPUT_JSON, "w") as f:
    json.dump(coco_predictions, f, indent=4)

print(f"Exported {len(coco_predictions)} detections to {OUTPUT_JSON}")
```

---

### Recipe 3: Formal COCO Evaluation with pycocotools (Including AP30/AP40)

```python
#!/usr/bin/env python3
"""
Formal COCO Evaluation Pipeline using pycocotools.
Computes standard COCO metrics (AP, AP50, AP75, AP_medium, AP_large, AR_max100)
and custom aerial metrics (AP30, AP40).
"""

import json
import numpy as np
from pathlib import Path
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from ultralytics import YOLO

WEIGHTS_PATH = "export/weights/yolo12s_triple_dino3_vitb16_seed_42_best.pt"
DATASET_YAML = "path/to/dataset.yaml"
GT_JSON_PATH = "export/evaluation_results/coco_gt_test_f48b69af.json"
SPLIT = "test"  # 'val' or 'test'

# 1. Run Ultralytics validation with save_json=True
model = YOLO(WEIGHTS_PATH)
val_results = model.val(
    data=DATASET_YAML,
    split=SPLIT,
    save_json=True,
    batch=4,
    imgsz=1024,
    device=0,
    project="temp_eval",
    name="run_eval",
    exist_ok=True,
    plots=False,
)

# 2. Load ground truth image name mapping
with open(GT_JSON_PATH, "r") as f:
    gt_data = json.load(f)
name_to_id = {Path(img["file_name"]).stem: img["id"] for img in gt_data["images"]}

# 3. Load and remap predictions
pred_file = Path("temp_eval/run_eval/predictions.json")
with open(pred_file, "r") as f:
    raw_preds = json.load(f)

mapped_preds = []
for p in raw_preds:
    stem = Path(p["image_id"]).stem
    if stem in name_to_id:
        mapped_preds.append({
            "image_id": name_to_id[stem],
            "category_id": p["category_id"],
            "bbox": p["bbox"],
            "score": p["score"],
        })

mapped_pred_file = Path("mapped_predictions.json")
with open(mapped_pred_file, "w") as f:
    json.dump(mapped_preds, f)

# 4. Standard COCO evaluation
coco_gt = COCO(GT_JSON_PATH)
coco_dt = coco_gt.loadRes(str(mapped_pred_file))

coco_eval = COCOeval(coco_gt, coco_dt, iouType="bbox")
coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()
stats = list(coco_eval.stats)

# 5. Custom IoU=0.30 and 0.40 evaluation
coco_eval_custom = COCOeval(coco_gt, coco_dt, iouType="bbox")
coco_eval_custom.params.iouThrs = np.array([0.3, 0.4])
coco_eval_custom.evaluate()
coco_eval_custom.accumulate()
precision = coco_eval_custom.eval["precision"]
s_30 = precision[0, :, :, 0, 2]
s_40 = precision[1, :, :, 0, 2]
ap30 = float(np.mean(s_30[s_30 > -1])) if len(s_30[s_30 > -1]) > 0 else 0.0
ap40 = float(np.mean(s_40[s_40 > -1])) if len(s_40[s_40 > -1]) > 0 else 0.0

print("\n" + "=" * 50)
print(f" COCO EVALUATION RESULTS SUMMARY ({SPLIT.upper()})")
print("=" * 50)
print(f" mAP (50-95):   {stats[0]:.4f}")
print(f" mAP@0.50:      {stats[1]:.4f}")
print(f" mAP@0.75:      {stats[2]:.4f}")
print(f" mAP@0.30:      {ap30:.4f}")
print(f" mAP@0.40:      {ap40:.4f}")
print(f" AR@100:        {stats[8]:.4f}")
print("=" * 50)
```

---

## 6. Weights & Biases (W&B) Run Mapping

All completed runs have been synchronized to the central benchmark project:
**W&B Project**: [https://wandb.ai/brezo-boku-vienna/_baseline?nw=nwuserbrezo](https://wandb.ai/brezo-boku-vienna/_baseline?nw=nwuserbrezo)

| Local Run Directory | Sensible W&B Run Name | W&B Run ID | Status | Checkpoint File |
| :--- | :--- | :--- | :--- | :--- |
| `_baseline/triple_dino3_vitb16_seed422` | `yolo12s_triple_dino3_vitb16_seed_42` | [`ovdgoz21`](https://wandb.ai/brezo-boku-vienna/_baseline/runs/ovdgoz21) | Finished (300 ep) | `export/weights/yolo12s_triple_dino3_vitb16_seed_42_best.pt` |
| `_baseline/triple_dino3_vitb16_seed100` | `yolo12s_triple_dino3_vitb16_seed_100` | [`p96dlaj5`](https://wandb.ai/brezo-boku-vienna/_baseline/runs/p96dlaj5) | Finished (300 ep) | `export/weights/yolo12s_triple_dino3_vitb16_seed_100_best.pt` |
| `_baseline/triple_dino3_vitb16_seed999` | `yolo12s_triple_dino3_vitb16_seed_999` | [`ftxj3r9n`](https://wandb.ai/brezo-boku-vienna/_baseline/runs/ftxj3r9n) | Finished (300 ep) | `export/weights/yolo12s_triple_dino3_vitb16_seed_999_best.pt` |

---

## 7. Calibrated Optimal F1 Operating Point Benchmark

For operational field deployment, raw mAP (which integrates over the entire $[0, 1]$ confidence interval at $conf=0.001$) does not indicate the single decision threshold that balances False Positives and False Negatives.
The optimal operating point was determined on the independent **Validation F1-Confidence Curve** ($\approx 0.273 - 0.303$) and evaluated on the hold-out test set ($N=510$).

### Hold-Out Test Set Results at Optimal Confidence Threshold ($conf \in [0.273, 0.303]$)

| Seed | Opt Conf ($\tau^*$) | Val F1 (max) | Test Precision | Test Recall | Test F1 @ IoU 0.50 | TP | FP | FN | Test COCO AP50 | Test COCO AP |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **42** | 0.2730 | 0.6110 | 62.43% | 36.63% | **46.17%** | 211 | 127 | 365 | 30.45% | 16.39% |
| **100** | 0.2730 | 0.6050 | 59.55% | 36.81% | **45.49%** | 212 | 144 | 364 | 30.31% | 15.77% |
| **999** | 0.3030 | 0.6060 | 61.20% | 38.89% | **47.56%** | 224 | 142 | 352 | 31.86% | 16.85% |
| **Mean ± Std** | — | **0.607 ± 0.003** | **61.06% ± 1.18%** | **37.44% ± 1.03%** | **46.41% ± 0.86%** | 215.7 | 137.7 | 360.3 | **30.87% ± 0.70%** | **16.34% ± 0.44%** |

### Recipe 4: Running Calibrated Optimal F1 Inference

```python
#!/usr/bin/env python3
"""Run inference using the calibrated optimal F1 confidence threshold."""

from ultralytics import YOLO

# Recommended calibrated confidence: conf=0.28 (mean optimal across seeds)
WEIGHTS_PATH = "export/weights/yolo12s_triple_dino3_vitb16_seed_42_best.pt"
model = YOLO(WEIGHTS_PATH)

results = model.predict(
    source="path/to/aerial/images",
    conf=0.28,        # Calibrated optimal F1 threshold
    iou=0.5,         # NMS IoU threshold
    imgsz=1024,
    device=0,
    save=True,
    save_txt=True,   # Saves YOLO format [cls x y w conf]
    save_conf=True,
)
```

