#!/usr/bin/env python3
"""
Full Evaluation, Export, and WandB Synchronization Pipeline
for YOLOv12s + DINOv3 ViT-B/16 Triple Integration Models.
"""

import os
import sys
import json
import shutil
from pathlib import Path
import numpy as np
import pandas as pd
import torch
import gc

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import wandb

# Ensure current directory is in path
CURRENT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(CURRENT_DIR))

from ultralytics import YOLO

DATASET_YAML = "C:/Users/emil_brezovsky/Documents/GitHub/_dataset_ail/dataset.yaml"
GT_VAL_PATH = r"C:\Users\emil_brezovsky\Documents\GitHub\_trainer_lightly\export\evaluation_results\coco_gt_val_8eddf691.json"
GT_TEST_PATH = r"C:\Users\emil_brezovsky\Documents\GitHub\_trainer_lightly\export\evaluation_results\coco_gt_test_f48b69af.json"

RUN_CONFIGS = [
    {
        "seed": 42,
        "run_dir": CURRENT_DIR / "_baseline" / "triple_dino3_vitb16_seed422",
        "wandb_id": "ovdgoz21",
        "sensible_name": "yolo12s_triple_dino3_vitb16_seed_42",
    },
    {
        "seed": 100,
        "run_dir": CURRENT_DIR / "_baseline" / "triple_dino3_vitb16_seed100",
        "wandb_id": "p96dlaj5",
        "sensible_name": "yolo12s_triple_dino3_vitb16_seed_100",
    },
    {
        "seed": 999,
        "run_dir": CURRENT_DIR / "_baseline" / "triple_dino3_vitb16_seed999",
        "wandb_id": "ftxj3r9n",
        "sensible_name": "yolo12s_triple_dino3_vitb16_seed_999",
    },
]

EXPORT_DIR = CURRENT_DIR / "export"
WEIGHTS_EXPORT_DIR = EXPORT_DIR / "weights"
EVAL_EXPORT_DIR = EXPORT_DIR / "evaluation_results"


def ensure_ground_truth():
    """Ensure ground truth JSON files exist in evaluation export directory."""
    EVAL_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    WEIGHTS_EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    dest_val = EVAL_EXPORT_DIR / Path(GT_VAL_PATH).name
    dest_test = EVAL_EXPORT_DIR / Path(GT_TEST_PATH).name

    if not dest_val.exists() and Path(GT_VAL_PATH).exists():
        shutil.copy(GT_VAL_PATH, dest_val)
        print(f"Copied GT Val to {dest_val}")
    if not dest_test.exists() and Path(GT_TEST_PATH).exists():
        shutil.copy(GT_TEST_PATH, dest_test)
        print(f"Copied GT Test to {dest_test}")

    return dest_val, dest_test


def evaluate_split(model: YOLO, split: str, gt_path: Path, run_name: str):
    """
    Run YOLO validation with save_json=True and compute pycocotools COCO evaluation
    including custom AP30 and AP40 metrics.
    """
    print(f"\n[{run_name}] Running validation on split '{split}'...")
    temp_project = CURRENT_DIR / "temp_eval"
    temp_name = f"val_{run_name}_{split}"

    # 1. Run Ultralytics validation to get predictions
    val_results = model.val(
        data=DATASET_YAML,
        split=split,
        save_json=True,
        batch=4,
        imgsz=1024,
        device=0,
        project=str(temp_project),
        name=temp_name,
        exist_ok=True,
        plots=False,
    )

    pred_src_file = temp_project / temp_name / "predictions.json"
    if not pred_src_file.exists():
        raise FileNotFoundError(f"predictions.json not found at {pred_src_file}")

    with open(pred_src_file, "r") as f:
        raw_preds = json.load(f)

    # 2. Load Ground Truth mapping
    with open(gt_path, "r") as f:
        gt_data = json.load(f)
    name_to_id = {Path(img["file_name"]).stem: img["id"] for img in gt_data["images"]}

    # 3. Map predictions to GT image IDs
    mapped_preds = []
    unmapped = 0
    for p in raw_preds:
        stem = Path(p["image_id"]).stem
        if stem in name_to_id:
            mapped_preds.append({
                "image_id": name_to_id[stem],
                "category_id": p["category_id"],
                "bbox": p["bbox"],
                "score": p["score"],
            })
        else:
            unmapped += 1

    if unmapped > 0:
        print(f"  Warning: {unmapped} predictions unmapped to GT.")

    # Save mapped predictions
    pred_dest_file = EVAL_EXPORT_DIR / f"{run_name}_{split.upper()}_coco_predictions.json"
    with open(pred_dest_file, "w") as f:
        json.dump(mapped_preds, f, indent=4)
    print(f"  Saved {len(mapped_preds)} predictions to {pred_dest_file.name}")

    # 4. Run pycocotools COCOeval
    coco_gt = COCO(str(gt_path))
    if len(mapped_preds) == 0:
        stats = [0.0] * 12
        ap30, ap40 = 0.0, 0.0
    else:
        coco_dt = coco_gt.loadRes(str(pred_dest_file))
        coco_eval = COCOeval(coco_gt, coco_dt, iouType="bbox")
        coco_eval.evaluate()
        coco_eval.accumulate()
        coco_eval.summarize()
        stats = list(coco_eval.stats)

        # Custom IoU 0.30 and 0.40
        coco_eval_custom = COCOeval(coco_gt, coco_dt, iouType="bbox")
        coco_eval_custom.params.iouThrs = np.array([0.3, 0.4])
        coco_eval_custom.evaluate()
        coco_eval_custom.accumulate()
        precision = coco_eval_custom.eval["precision"]
        s_30 = precision[0, :, :, 0, 2]
        s_40 = precision[1, :, :, 0, 2]
        ap30 = float(np.mean(s_30[s_30 > -1])) if len(s_30[s_30 > -1]) > 0 else 0.0
        ap40 = float(np.mean(s_40[s_40 > -1])) if len(s_40[s_40 > -1]) > 0 else 0.0

    metrics_payload = {
        "model_variant": str(model.ckpt_path) if hasattr(model, "ckpt_path") else run_name,
        "run_name": f"{run_name}_{split.upper()}",
        "split": split,
        "metrics": {
            "AP": stats[0],
            "AP50": stats[1],
            "AP75": stats[2],
            "AP30": ap30,
            "AP40": ap40,
            "AP_small": stats[3],
            "AP_medium": stats[4],
            "AP_large": stats[5],
            "AR_max1": stats[6],
            "AR_max10": stats[7],
            "AR_max100": stats[8],
            "AR_small": stats[9],
            "AR_medium": stats[10],
            "AR_large": stats[11],
        },
        "ultralytics_metrics": {
            "mAP50": float(val_results.box.map50),
            "mAP75": float(val_results.box.map75),
            "mAP50-95": float(val_results.box.map),
            "precision": float(val_results.box.mp),
            "recall": float(val_results.box.mr),
        },
    }

    metrics_dest_file = EVAL_EXPORT_DIR / f"{run_name}_{split.upper()}_coco_metrics.json"
    with open(metrics_dest_file, "w") as f:
        json.dump(metrics_payload, f, indent=4)
    print(f"  Strict COCO metrics saved to {metrics_dest_file.name}")

    # Cleanup temp directory
    try:
        shutil.rmtree(temp_project / temp_name)
    except Exception as e:
        print(f"  Cleanup note: {e}")

    return metrics_payload


def sync_wandb(run_id: str, sensible_name: str, test_metrics: dict, val_metrics: dict):
    """Update WandB run name, tags, and summary metrics."""
    api = wandb.Api()
    run = api.run(f"brezo-boku-vienna/_baseline/{run_id}")
    old_name = run.name
    print(f"\n[WandB Sync] Updating run {run_id}: '{old_name}' -> '{sensible_name}'")

    run.name = sensible_name
    run.tags = ["yolo12s", "dino3", "triple", "vitb16", "completed", "evaluated_coco"]

    # Update summary with hold-out test metrics (primary benchmark comparison)
    t_m = test_metrics["metrics"]
    for k, v in t_m.items():
        run.summary[f"metrics/{k}"] = v
    run.summary["metrics/mAP50(B)"] = t_m["AP50"]
    run.summary["metrics/mAP50-95(B)"] = t_m["AP"]

    # Also log validation metrics under val_metrics/
    v_m = val_metrics["metrics"]
    for k, v in v_m.items():
        run.summary[f"val_coco_metrics/{k}"] = v

    run.update()
    print(f"  WandB run {run_id} updated successfully!")


def main():
    print("=" * 80)
    print("STARTING FULL EVALUATION, EXPORT, AND WANDB SYNC PIPELINE")
    print("=" * 80)

    dest_val_gt, dest_test_gt = ensure_ground_truth()

    all_results = []

    for cfg in RUN_CONFIGS:
        seed = cfg["seed"]
        run_dir = cfg["run_dir"]
        wandb_id = cfg["wandb_id"]
        sensible_name = cfg["sensible_name"]

        best_pt = run_dir / "weights" / "best.pt"
        last_pt = run_dir / "weights" / "last.pt"

        if not best_pt.exists():
            print(f"ERROR: {best_pt} not found!")
            continue

        # 1. Export weights
        exported_best = WEIGHTS_EXPORT_DIR / f"{sensible_name}_best.pt"
        exported_last = WEIGHTS_EXPORT_DIR / f"{sensible_name}_last.pt"

        if not exported_best.exists():
            print(f"\nExporting {best_pt.name} -> {exported_best.name}...")
            shutil.copy(best_pt, exported_best)
        else:
            print(f"\n{exported_best.name} already exported.")

        if last_pt.exists() and not exported_last.exists():
            print(f"Exporting {last_pt.name} -> {exported_last.name}...")
            shutil.copy(last_pt, exported_last)

        # 2. Load model
        print(f"Loading YOLO model from {exported_best}...")
        model = YOLO(str(exported_best))

        # 3. Evaluate on VAL split
        val_metrics = evaluate_split(model, "val", dest_val_gt, sensible_name)

        # 4. Evaluate on TEST split
        test_metrics = evaluate_split(model, "test", dest_test_gt, sensible_name)

        # 5. Sync to WandB
        sync_wandb(wandb_id, sensible_name, test_metrics, val_metrics)

        all_results.append({
            "seed": seed,
            "name": sensible_name,
            "wandb_id": wandb_id,
            "val_metrics": val_metrics,
            "test_metrics": test_metrics,
        })

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

    # 6. Generate Statistical Benchmark Summary
    print("\n" + "=" * 80)
    print("GENERATING STATISTICAL SUMMARY")
    print("=" * 80)

    summary_rows = []
    for r in all_results:
        tm = r["test_metrics"]["metrics"]
        vm = r["val_metrics"]["metrics"]
        summary_rows.append({
            "model": r["name"],
            "seed": r["seed"],
            "wandb_id": r["wandb_id"],
            "test_mAP50-95": tm["AP"],
            "test_mAP50": tm["AP50"],
            "test_mAP75": tm["AP75"],
            "test_mAP30": tm["AP30"],
            "test_mAP40": tm["AP40"],
            "test_AR_max100": tm["AR_max100"],
            "val_mAP50-95": vm["AP"],
            "val_mAP50": vm["AP50"],
            "val_mAP75": vm["AP75"],
            "val_mAP30": vm["AP30"],
            "val_mAP40": vm["AP40"],
            "val_AR_max100": vm["AR_max100"],
        })

    df = pd.DataFrame(summary_rows)
    csv_path = EVAL_EXPORT_DIR / "evaluation_summary.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved evaluation summary CSV to {csv_path}")

    # Compute mean and std across 3 seeds
    test_aps = [r["test_metrics"]["metrics"]["AP"] for r in all_results]
    test_ap50s = [r["test_metrics"]["metrics"]["AP50"] for r in all_results]
    test_ap75s = [r["test_metrics"]["metrics"]["AP75"] for r in all_results]
    test_ap30s = [r["test_metrics"]["metrics"]["AP30"] for r in all_results]
    test_ap40s = [r["test_metrics"]["metrics"]["AP40"] for r in all_results]
    test_ar100s = [r["test_metrics"]["metrics"]["AR_max100"] for r in all_results]

    val_aps = [r["val_metrics"]["metrics"]["AP"] for r in all_results]
    val_ap50s = [r["val_metrics"]["metrics"]["AP50"] for r in all_results]
    val_ap75s = [r["val_metrics"]["metrics"]["AP75"] for r in all_results]
    val_ap30s = [r["val_metrics"]["metrics"]["AP30"] for r in all_results]
    val_ap40s = [r["val_metrics"]["metrics"]["AP40"] for r in all_results]

    stats_report = {
        "model_architecture": "yolo12s_triple_dino3_vitb16",
        "backbone": "YOLOv12s + Meta DINOv3 ViT-B/16 (Triple Scale P3/P4/P5)",
        "dataset": "Ailanthus altissima aerial benchmark (510 val, 510 test, 1024x1024)",
        "num_runs": len(all_results),
        "seeds": [r["seed"] for r in all_results],
        "test_holdout_metrics": {
            "mAP50_mean": float(np.mean(test_ap50s)),
            "mAP50_std": float(np.std(test_ap50s)),
            "mAP50_95_mean": float(np.mean(test_aps)),
            "mAP50_95_std": float(np.std(test_aps)),
            "mAP75_mean": float(np.mean(test_ap75s)),
            "mAP75_std": float(np.std(test_ap75s)),
            "mAP30_mean": float(np.mean(test_ap30s)),
            "mAP30_std": float(np.std(test_ap30s)),
            "mAP40_mean": float(np.mean(test_ap40s)),
            "mAP40_std": float(np.std(test_ap40s)),
            "AR_max100_mean": float(np.mean(test_ar100s)),
            "AR_max100_std": float(np.std(test_ar100s)),
        },
        "validation_metrics": {
            "mAP50_mean": float(np.mean(val_ap50s)),
            "mAP50_std": float(np.std(val_ap50s)),
            "mAP50_95_mean": float(np.mean(val_aps)),
            "mAP50_95_std": float(np.std(val_aps)),
            "mAP75_mean": float(np.mean(val_ap75s)),
            "mAP75_std": float(np.std(val_ap75s)),
            "mAP30_mean": float(np.mean(val_ap30s)),
            "mAP30_std": float(np.std(val_ap30s)),
            "mAP40_mean": float(np.mean(val_ap40s)),
            "mAP40_std": float(np.std(val_ap40s)),
        },
        "individual_runs": all_results,
    }

    report_path = EVAL_EXPORT_DIR / "benchmark_statistical_report.json"
    with open(report_path, "w") as f:
        json.dump(stats_report, f, indent=4)
    print(f"Saved statistical report JSON to {report_path}")

    # Print summary table
    print("\n" + "=" * 80)
    print("FINAL BENCHMARK RESULTS MATRIX")
    print("=" * 80)
    print(f"Hold-out Test Set (N=510):")
    print(f"  mAP@0.50:      {np.mean(test_ap50s)*100:.2f}% ± {np.std(test_ap50s)*100:.2f}%")
    print(f"  mAP@0.50:0.95: {np.mean(test_aps)*100:.2f}% ± {np.std(test_aps)*100:.2f}%")
    print(f"  mAP@0.75:      {np.mean(test_ap75s)*100:.2f}% ± {np.std(test_ap75s)*100:.2f}%")
    print(f"  mAP@0.30:      {np.mean(test_ap30s)*100:.2f}% ± {np.std(test_ap30s)*100:.2f}%")
    print(f"  mAP@0.40:      {np.mean(test_ap40s)*100:.2f}% ± {np.std(test_ap40s)*100:.2f}%")
    print(f"  AR@100:        {np.mean(test_ar100s)*100:.2f}% ± {np.std(test_ar100s)*100:.2f}%")
    print("=" * 80)
    print("Pipeline completed successfully!")


if __name__ == "__main__":
    main()
