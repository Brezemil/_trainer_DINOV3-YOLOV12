#!/usr/bin/env python3
"""
Optimal F1-Confidence Evaluation & Multi-Format Prediction Export Pipeline
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

CURRENT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(CURRENT_DIR))

from ultralytics import YOLO

DATASET_YAML = "C:/Users/emil_brezovsky/Documents/GitHub/_dataset_ail/dataset.yaml"
GT_TEST_PATH = CURRENT_DIR / "export" / "evaluation_results" / "coco_gt_test_f48b69af.json"

RUN_CONFIGS = [
    {
        "seed": 42,
        "weights_path": CURRENT_DIR / "export" / "weights" / "yolo12s_triple_dino3_vitb16_seed_42_best.pt",
        "run_name": "yolo12s_triple_dino3_vitb16_seed_42",
        "opt_conf": 0.2730,
        "val_f1_max": 0.6110,
        "val_p_at_opt": 0.6680,
        "val_r_at_opt": 0.5620,
    },
    {
        "seed": 100,
        "weights_path": CURRENT_DIR / "export" / "weights" / "yolo12s_triple_dino3_vitb16_seed_100_best.pt",
        "run_name": "yolo12s_triple_dino3_vitb16_seed_100",
        "opt_conf": 0.2730,
        "val_f1_max": 0.6050,
        "val_p_at_opt": 0.6670,
        "val_r_at_opt": 0.5530,
    },
    {
        "seed": 999,
        "weights_path": CURRENT_DIR / "export" / "weights" / "yolo12s_triple_dino3_vitb16_seed_999_best.pt",
        "run_name": "yolo12s_triple_dino3_vitb16_seed_999",
        "opt_conf": 0.3030,
        "val_f1_max": 0.6060,
        "val_p_at_opt": 0.6890,
        "val_r_at_opt": 0.5400,
    },
]

EXPORT_DIR = CURRENT_DIR / "export"
EVAL_EXPORT_DIR = EXPORT_DIR / "evaluation_results"
PRED_EXPORT_DIR = EXPORT_DIR / "predictions"
YOLO_LABELS_DIR = PRED_EXPORT_DIR / "yolo_format"
COCO_JSON_DIR = PRED_EXPORT_DIR / "coco_format"


def compute_point_metrics_at_iou50(coco_gt: COCO, mapped_preds: list, iou_thresh: float = 0.5):
    """
    Computes exact point metrics (TP, FP, FN, Precision, Recall, F1)
    for detections at a fixed IoU threshold.
    """
    # Group GT by image_id
    gt_by_img = {}
    for ann in coco_gt.dataset["annotations"]:
        img_id = ann["image_id"]
        if img_id not in gt_by_img:
            gt_by_img[img_id] = []
        gt_by_img[img_id].append(ann["bbox"])  # [x, y, w, h]

    # Group Preds by image_id, sorted by score descending
    preds_by_img = {}
    for p in mapped_preds:
        img_id = p["image_id"]
        if img_id not in preds_by_img:
            preds_by_img[img_id] = []
        preds_by_img[img_id].append(p)

    for img_id in preds_by_img:
        preds_by_img[img_id].sort(key=lambda x: x["score"], reverse=True)

    tp_total = 0
    fp_total = 0
    fn_total = 0
    total_gt = len(coco_gt.dataset["annotations"])

    for img_id, gt_boxes in gt_by_img.items():
        matched_gt = [False] * len(gt_boxes)
        pred_list = preds_by_img.get(img_id, [])

        for pred in pred_list:
            pb = pred["bbox"]  # [px, py, pw, ph]
            best_iou = 0.0
            best_gt_idx = -1

            for g_idx, gb in enumerate(gt_boxes):
                if matched_gt[g_idx]:
                    continue
                # Calculate IoU
                x1 = max(pb[0], gb[0])
                y1 = max(pb[1], gb[1])
                x2 = min(pb[0] + pb[2], gb[0] + gb[2])
                y2 = min(pb[1] + pb[3], gb[1] + gb[3])

                inter_w = max(0.0, x2 - x1)
                inter_h = max(0.0, y2 - y1)
                inter_area = inter_w * inter_h

                p_area = pb[2] * pb[3]
                g_area = gb[2] * gb[3]
                union_area = p_area + g_area - inter_area

                iou = inter_area / union_area if union_area > 0 else 0.0
                if iou > best_iou:
                    best_iou = iou
                    best_gt_idx = g_idx

            if best_iou >= iou_thresh and best_gt_idx >= 0:
                tp_total += 1
                matched_gt[best_gt_idx] = True
            else:
                fp_total += 1

        fn_total += matched_gt.count(False)

    # Any images in preds that have no GT
    for img_id, pred_list in preds_by_img.items():
        if img_id not in gt_by_img:
            fp_total += len(pred_list)

    precision = tp_total / (tp_total + fp_total) if (tp_total + fp_total) > 0 else 0.0
    recall = tp_total / total_gt if total_gt > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "true_positives": tp_total,
        "false_positives": fp_total,
        "false_negatives": fn_total,
        "ground_truth_count": total_gt,
        "predictions_count": len(mapped_preds),
        "point_precision": float(precision),
        "point_recall": float(recall),
        "point_f1_score": float(f1),
    }


def evaluate_optimal_run(cfg: dict, gt_test_path: Path):
    seed = cfg["seed"]
    weights_path = cfg["weights_path"]
    run_name = cfg["run_name"]
    opt_conf = cfg["opt_conf"]

    print("\n" + "=" * 80)
    print(f"EVALUATING {run_name} AT OPTIMAL F1 CONFIDENCE = {opt_conf}")
    print("=" * 80)

    # 1. Run Ultralytics val on test set with conf=opt_conf
    temp_project = CURRENT_DIR / "temp_opt_eval"
    temp_name = f"{run_name}_opt_f1"

    model = YOLO(str(weights_path))
    val_results = model.val(
        data=DATASET_YAML,
        split="test",
        conf=opt_conf,
        save_json=True,
        save_txt=True,
        save_conf=True,
        batch=4,
        imgsz=1024,
        device=0,
        project=str(temp_project),
        name=temp_name,
        exist_ok=True,
        plots=False,
    )

    temp_run_dir = temp_project / temp_name

    # 2. Export YOLO format predictions (.txt)
    yolo_dest_dir = YOLO_LABELS_DIR / f"{run_name}_opt_f1"
    yolo_dest_dir.mkdir(parents=True, exist_ok=True)

    src_labels_dir = temp_run_dir / "labels"
    txt_count = 0
    if src_labels_dir.exists():
        for txt_file in src_labels_dir.glob("*.txt"):
            shutil.copy(txt_file, yolo_dest_dir / txt_file.name)
            txt_count += 1
    print(f"  Exported {txt_count} YOLO format label files to {yolo_dest_dir.relative_to(CURRENT_DIR)}")

    # 3. Process COCO format predictions (.json)
    pred_src_file = temp_run_dir / "predictions.json"
    raw_preds = []
    if pred_src_file.exists():
        with open(pred_src_file, "r") as f:
            raw_preds = json.load(f)

    with open(gt_test_path, "r") as f:
        gt_data = json.load(f)
    name_to_id = {Path(img["file_name"]).stem: img["id"] for img in gt_data["images"]}

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

    # Save to both predictions/coco_format and evaluation_results
    coco_json_dest = COCO_JSON_DIR / f"{run_name}_opt_f1_TEST_coco_predictions.json"
    eval_json_dest = EVAL_EXPORT_DIR / f"{run_name}_opt_f1_TEST_coco_predictions.json"
    with open(coco_json_dest, "w") as f:
        json.dump(mapped_preds, f, indent=4)
    with open(eval_json_dest, "w") as f:
        json.dump(mapped_preds, f, indent=4)
    print(f"  Exported {len(mapped_preds)} detections in COCO JSON format to {coco_json_dest.relative_to(CURRENT_DIR)}")

    # 4. Run pycocotools COCOeval
    coco_gt = COCO(str(gt_test_path))
    if len(mapped_preds) == 0:
        stats = [0.0] * 12
        ap30, ap40 = 0.0, 0.0
    else:
        coco_dt = coco_gt.loadRes(str(eval_json_dest))
        coco_eval = COCOeval(coco_gt, coco_dt, iouType="bbox")
        coco_eval.evaluate()
        coco_eval.accumulate()
        coco_eval.summarize()
        stats = list(coco_eval.stats)

        coco_eval_custom = COCOeval(coco_gt, coco_dt, iouType="bbox")
        coco_eval_custom.params.iouThrs = np.array([0.3, 0.4])
        coco_eval_custom.evaluate()
        coco_eval_custom.accumulate()
        precision = coco_eval_custom.eval["precision"]
        s_30 = precision[0, :, :, 0, 2]
        s_40 = precision[1, :, :, 0, 2]
        ap30 = float(np.mean(s_30[s_30 > -1])) if len(s_30[s_30 > -1]) > 0 else 0.0
        ap40 = float(np.mean(s_40[s_40 > -1])) if len(s_40[s_40 > -1]) > 0 else 0.0

    # 5. Compute exact Point Metrics at IoU 0.50 operating point
    point_stats = compute_point_metrics_at_iou50(coco_gt, mapped_preds, iou_thresh=0.5)

    metrics_payload = {
        "model_variant": str(weights_path.name),
        "run_name": f"{run_name}_opt_f1_TEST",
        "split": "test",
        "operating_point": {
            "optimal_confidence_threshold": opt_conf,
            "validation_max_f1": cfg["val_f1_max"],
            "validation_precision_at_opt": cfg["val_p_at_opt"],
            "validation_recall_at_opt": cfg["val_r_at_opt"],
        },
        "test_point_metrics_iou50": point_stats,
        "coco_metrics": {
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
        "ultralytics_metrics_at_conf": {
            "precision": float(val_results.box.mp),
            "recall": float(val_results.box.mr),
            "f1": float(2 * val_results.box.mp * val_results.box.mr / (val_results.box.mp + val_results.box.mr))
            if (val_results.box.mp + val_results.box.mr) > 0 else 0.0,
            "mAP50": float(val_results.box.map50),
            "mAP75": float(val_results.box.map75),
            "mAP50-95": float(val_results.box.map),
        },
    }

    metrics_dest_file = EVAL_EXPORT_DIR / f"{run_name}_opt_f1_TEST_coco_metrics.json"
    with open(metrics_dest_file, "w") as f:
        json.dump(metrics_payload, f, indent=4)
    print(f"  Strict COCO metrics saved to {metrics_dest_file.relative_to(CURRENT_DIR)}")

    # Cleanup temp
    try:
        shutil.rmtree(temp_project)
    except Exception as e:
        print(f"  Temp cleanup note: {e}")

    return metrics_payload


def main():
    print("=" * 80)
    print("STARTING OPTIMAL F1 INFERENCE & EVALUATION PIPELINE")
    print("=" * 80)

    EVAL_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    YOLO_LABELS_DIR.mkdir(parents=True, exist_ok=True)
    COCO_JSON_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    for cfg in RUN_CONFIGS:
        res = evaluate_optimal_run(cfg, GT_TEST_PATH)
        results.append(res)
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

    # Generate Summary CSV
    summary_rows = []
    for r in results:
        cm = r["coco_metrics"]
        pm = r["test_point_metrics_iou50"]
        op = r["operating_point"]
        summary_rows.append({
            "model_variant": r["model_variant"],
            "optimal_conf_threshold": op["optimal_confidence_threshold"],
            "val_f1_max": op["validation_max_f1"],
            "test_point_precision": pm["point_precision"],
            "test_point_recall": pm["point_recall"],
            "test_point_f1": pm["point_f1_score"],
            "test_true_positives": pm["true_positives"],
            "test_false_positives": pm["false_positives"],
            "test_false_negatives": pm["false_negatives"],
            "test_coco_AP": cm["AP"],
            "test_coco_AP50": cm["AP50"],
            "test_coco_AP75": cm["AP75"],
            "test_coco_AP30": cm["AP30"],
            "test_coco_AP40": cm["AP40"],
            "test_coco_AR100": cm["AR_max100"],
        })

    df = pd.DataFrame(summary_rows)
    csv_path = EVAL_EXPORT_DIR / "optimal_f1_evaluation_summary.csv"
    df.to_csv(csv_path, index=False)
    print(f"\nSaved optimal F1 evaluation summary CSV to {csv_path.relative_to(CURRENT_DIR)}")

    # Statistical Report
    p_scores = [r["test_point_metrics_iou50"]["point_precision"] for r in results]
    r_scores = [r["test_point_metrics_iou50"]["point_recall"] for r in results]
    f1_scores = [r["test_point_metrics_iou50"]["point_f1_score"] for r in results]
    ap50_scores = [r["coco_metrics"]["AP50"] for r in results]
    ap_scores = [r["coco_metrics"]["AP"] for r in results]
    ap75_scores = [r["coco_metrics"]["AP75"] for r in results]
    ap30_scores = [r["coco_metrics"]["AP30"] for r in results]
    ap40_scores = [r["coco_metrics"]["AP40"] for r in results]

    stats = {
        "title": "YOLOv12s-Triple-DINOv3 Optimal F1 Operating Point Benchmark Analysis",
        "description": "Evaluation of 3-seed models at calibrated optimal confidence thresholds from validation F1 curves",
        "seeds": [c["seed"] for c in RUN_CONFIGS],
        "metrics_summary": {
            "test_precision_mean": float(np.mean(p_scores)),
            "test_precision_std": float(np.std(p_scores)),
            "test_recall_mean": float(np.mean(r_scores)),
            "test_recall_std": float(np.std(r_scores)),
            "test_f1_mean": float(np.mean(f1_scores)),
            "test_f1_std": float(np.std(f1_scores)),
            "test_mAP50_mean": float(np.mean(ap50_scores)),
            "test_mAP50_std": float(np.std(ap50_scores)),
            "test_mAP50_95_mean": float(np.mean(ap_scores)),
            "test_mAP50_95_std": float(np.std(ap_scores)),
            "test_mAP75_mean": float(np.mean(ap75_scores)),
            "test_mAP75_std": float(np.std(ap75_scores)),
            "test_mAP30_mean": float(np.mean(ap30_scores)),
            "test_mAP30_std": float(np.std(ap30_scores)),
            "test_mAP40_mean": float(np.mean(ap40_scores)),
            "test_mAP40_std": float(np.std(ap40_scores)),
        },
        "individual_runs": results,
    }

    stats_path = EVAL_EXPORT_DIR / "optimal_f1_statistical_report.json"
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=4)
    print(f"Saved optimal F1 statistical report to {stats_path.relative_to(CURRENT_DIR)}")

    print("\n" + "=" * 80)
    print("FINAL OPTIMAL F1 OPERATING POINT SUMMARY")
    print("=" * 80)
    print(f"Precision @ IoU 0.50:   {np.mean(p_scores)*100:.2f}% ± {np.std(p_scores)*100:.2f}%")
    print(f"Recall @ IoU 0.50:      {np.mean(r_scores)*100:.2f}% ± {np.std(r_scores)*100:.2f}%")
    print(f"F1-Score @ IoU 0.50:    {np.mean(f1_scores)*100:.2f}% ± {np.std(f1_scores)*100:.2f}%")
    print(f"COCO mAP@0.50:          {np.mean(ap50_scores)*100:.2f}% ± {np.std(ap50_scores)*100:.2f}%")
    print(f"COCO mAP@0.50:0.95:     {np.mean(ap_scores)*100:.2f}% ± {np.std(ap_scores)*100:.2f}%")
    print("=" * 80)


if __name__ == "__main__":
    main()
