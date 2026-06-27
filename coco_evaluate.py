#!/usr/bin/env python3
"""
coco_evaluate.py - Strict COCO Evaluation Module for YOLOv12 + DINOv3 models.

This script parses the dataset config, generates a COCO ground truth JSON file,
matches model predictions to the ground truth integer IDs, runs strict COCOeval
from pycocotools, saves the metrics to a JSON file, and performs GPU memory cleanup.
"""

import argparse
import json
import sys
import os
import hashlib
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import torch
import yaml
from PIL import Image

try:
    from pycocotools.coco import COCO
    from pycocotools.cocoeval import COCOeval
except ImportError:
    print("[ERROR] pycocotools is required for COCO evaluation. Please install it or use the Pixi environment.")
    sys.exit(1)

from ultralytics import YOLO


def generate_coco_ground_truth(data_yaml, split="val", output_dir="results", fraction=None):
    """
    Parse dataset YAML, scan target split, and build/save a valid COCO format JSON.
    """
    print(f"[INFO] Generating COCO ground truth for split: {split}")

    with open(data_yaml, "r") as f:
        yaml_data = yaml.safe_load(f)

    yaml_dir = Path(data_yaml).parent
    dataset_root = yaml_data.get("path", "")
    if dataset_root:
        dataset_path = Path(dataset_root)
        if not dataset_path.is_absolute():
            dataset_path = yaml_dir / dataset_path
    else:
        dataset_path = yaml_dir

    split_dir_name = yaml_data.get(split)
    if not split_dir_name:
        raise ValueError(f"Split '{split}' not defined in dataset config: {data_yaml}")

    img_dir = dataset_path / split_dir_name
    if not img_dir.exists():
        raise FileNotFoundError(f"Image directory does not exist: {img_dir}")

    # Standard labels folder replacement (images -> labels)
    if "images" in img_dir.parts:
        parts = list(img_dir.parts)
        idx = parts.index("images")
        parts[idx] = "labels"
        lbl_dir = Path(*parts)
    else:
        lbl_dir = img_dir.parent / "labels" / img_dir.name

    print(f"   Image folder: {img_dir}")
    print(f"   Label folder: {lbl_dir}")

    # Save path for the GT JSON with path hash isolation to prevent split contamination
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    full_split_path = os.path.abspath(img_dir)
    path_hash = hashlib.md5(full_split_path.encode("utf-8")).hexdigest()[:8]

    if fraction is not None:
        gt_json_path = output_dir_path / f"coco_gt_{split}_{path_hash}_frac_{fraction}.json"
    else:
        gt_json_path = output_dir_path / f"coco_gt_{split}_{path_hash}.json"

    # Find image files
    img_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}
    img_files = sorted([f for f in img_dir.iterdir() if f.suffix.lower() in img_extensions])

    if not img_files:
        raise FileNotFoundError(f"No images found in split directory: {img_dir}")

    # Handle smoketest fraction
    if fraction is not None:
        import random

        random.seed(42)  # Deterministic seed for reproducible evaluation
        k = max(1, int(len(img_files) * fraction))
        img_files = sorted(random.sample(img_files, k))
        print(f"   [SMOKETEST] Fraction {fraction} applied. Evaluating on {len(img_files)} images.")

    if gt_json_path.exists():
        print(f"   [INFO] COCO ground truth file already exists at: {gt_json_path} (Skipping generation)")
        return gt_json_path, img_dir, img_files

    # Get categories mapping
    names = yaml_data.get("names", {})
    categories = []
    if isinstance(names, dict):
        for cid, name in names.items():
            categories.append({"id": int(cid), "name": str(name), "supercategory": "none"})
    elif isinstance(names, list):
        for cid, name in enumerate(names):
            categories.append({"id": cid, "name": str(name), "supercategory": "none"})
    else:
        raise ValueError("Invalid format for 'names' in dataset YAML.")

    print(f"   Building COCO structure for {len(img_files)} images...")

    images_list = []
    annotations = []
    ann_id_counter = 1

    for img_idx, img_file in enumerate(img_files, 1):
        try:
            with Image.open(img_file) as img:
                w, h = img.size
        except Exception as e:
            print(f"   [WARNING] Could not open image {img_file.name}: {e}")
            continue

        images_list.append({"id": img_idx, "file_name": img_file.name, "width": w, "height": h})

        # Match label file
        lbl_file = lbl_dir / f"{img_file.stem}.txt"
        if lbl_file.exists():
            with open(lbl_file, "r") as lf:
                lines = lf.readlines()

            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    class_id = int(parts[0])
                    # YOLO: x_center, y_center, width, height (normalized)
                    x_c, y_c, box_w, box_h = map(float, parts[1:5])

                    # Convert to absolute COCO format: [x_min, y_min, width, height]
                    w_abs = box_w * w
                    h_abs = box_h * h
                    x_min = (x_c - box_w / 2) * w
                    y_min = (y_c - box_h / 2) * h

                    annotations.append(
                        {
                            "id": ann_id_counter,
                            "image_id": img_idx,
                            "category_id": class_id,
                            "bbox": [x_min, y_min, w_abs, h_abs],
                            "area": w_abs * h_abs,
                            "iscrowd": 0,
                        }
                    )
                    ann_id_counter += 1

    coco_gt = {
        "info": {"description": f"COCO Ground Truth generated from {data_yaml}", "version": "1.0", "year": 2026},
        "licenses": [],
        "categories": categories,
        "images": images_list,
        "annotations": annotations,
    }

    with open(gt_json_path, "w") as f:
        json.dump(coco_gt, f, indent=2)

    print(f"   [SUCCESS] Saved ground truth COCO JSON to: {gt_json_path}")
    print(f"   Total Annotations: {len(annotations)}")
    return gt_json_path, img_dir, img_files


def run_evaluation(
    model_path,
    data_yaml,
    split="val",
    run_name=None,
    imgsz=640,
    device="0",
    output_dir="results",
    fraction=None,
    sahi_enabled=False,
    sahi_slice_height=512,
    sahi_slice_width=512,
    sahi_overlap_height_ratio=0.2,
    sahi_overlap_width_ratio=0.2,
    sahi_postprocess_match_threshold=0.5,
):
    """
    Run evaluation, map predictions, execute COCOeval, and save results.
    """
    # Setup paths and names
    if run_name is None:
        run_name = Path(model_path).stem

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Generate COCO Ground Truth JSON
    gt_json_path, img_dir, img_files = generate_coco_ground_truth(data_yaml, split, output_dir, fraction)

    # Load GT mappings to build the ID index
    with open(gt_json_path, "r") as f:
        gt_data = json.load(f)

    filename_to_id = {img["file_name"]: img["id"] for img in gt_data["images"]}

    # 2. Load Model and Predict
    print(f"[INFO] Loading model checkpoint: {model_path}")
    model = YOLO(model_path)

    predictions = []

    if sahi_enabled:
        print(f"[INFO] Running SAHI sliced inference on {len(img_files)} images...")
        try:
            from sahi.predict import get_sliced_prediction
            from sahi import AutoDetectionModel
        except ImportError:
            print(
                "[ERROR] sahi library is required for SAHI evaluation. Please install it or use the Pixi environment."
            )
            sys.exit(1)

        sahi_device = device
        if isinstance(sahi_device, int):
            sahi_device = f"cuda:{sahi_device}"
        elif isinstance(sahi_device, str):
            if sahi_device.isdigit():
                sahi_device = f"cuda:{sahi_device}"

        sahi_model_type = "rtdetr" if "rtdetr" in str(model_path).lower() else "ultralytics"
        sahi_model = AutoDetectionModel.from_pretrained(
            model_type=sahi_model_type,
            model=model,
            model_path=str(model_path),
            confidence_threshold=0.001,  # Low threshold for standard COCO PR curves
            device=sahi_device,
        )

        for img_file in img_files:
            img_name = img_file.name
            if img_name not in filename_to_id:
                continue
            img_id = filename_to_id[img_name]

            try:
                result = get_sliced_prediction(
                    str(img_file),
                    sahi_model,
                    slice_height=sahi_slice_height,
                    slice_width=sahi_slice_width,
                    overlap_height_ratio=sahi_overlap_height_ratio,
                    overlap_width_ratio=sahi_overlap_width_ratio,
                    perform_standard_pred=True,
                    postprocess_type="GREEDYNMM",
                    postprocess_match_metric="IOS",
                    postprocess_match_threshold=sahi_postprocess_match_threshold,
                    verbose=0,
                )

                for obj_pred in result.object_prediction_list:
                    bbox = obj_pred.bbox.to_coco_bbox()
                    cls = obj_pred.category.id
                    score = obj_pred.score.value

                    predictions.append(
                        {"image_id": img_id, "category_id": int(cls), "bbox": bbox, "score": float(score)}
                    )
            except Exception as e:
                print(f"   [WARNING] Error SAHI predicting on {img_file.name}: {e}")
                continue
    else:
        print(f"[INFO] Running standard inference on {split} images...")
        predict_source = [str(f) for f in img_files]
        results = model.predict(
            source=predict_source,
            conf=0.001,  # Standard low threshold for COCO PR curves
            iou=0.6,
            imgsz=imgsz,
            device=device,
            verbose=False,
            stream=True,  # Stream mode to optimize memory
        )

        # Match prediction boxes to GT integer IDs
        for result in results:
            img_name = Path(result.path).name
            if img_name not in filename_to_id:
                continue
            img_id = filename_to_id[img_name]

            boxes = result.boxes
            if boxes is None or len(boxes) == 0:
                continue

            for box in boxes:
                cls_id = int(box.cls[0].item())
                score = float(box.conf[0].item())
                xyxy = box.xyxy[0].tolist()
                w_box = xyxy[2] - xyxy[0]
                h_box = xyxy[3] - xyxy[1]

                predictions.append(
                    {
                        "image_id": img_id,
                        "category_id": cls_id,
                        "bbox": [xyxy[0], xyxy[1], w_box, h_box],
                        "score": score,
                    }
                )

    dt_json_path = output_path / f"{run_name}_predictions.json"
    with open(dt_json_path, "w") as f:
        json.dump(predictions, f)

    print(f"   Mapped {len(predictions)} prediction instances.")

    # 4. Strict COCO evaluation via pycocotools
    if len(predictions) == 0:
        print("[WARNING] No predictions made. Setting all metrics to 0.")
        metrics = {
            "mAP_50_95": 0.0,
            "mAP_50": 0.0,
            "mAP_75": 0.0,
            "AP_small": 0.0,
            "AP_medium": 0.0,
            "AP_large": 0.0,
            "AR_1": 0.0,
            "AR_10": 0.0,
            "AR_100": 0.0,
            "AR_small": 0.0,
            "AR_medium": 0.0,
            "AR_large": 0.0,
        }
    else:
        print("[INFO] Running pycocotools COCOeval...")
        coco_gt = COCO(str(gt_json_path))
        coco_dt = coco_gt.loadRes(str(dt_json_path))

        coco_eval = COCOeval(coco_gt, coco_dt, iouType="bbox")
        coco_eval.evaluate()
        coco_eval.accumulate()
        coco_eval.summarize()

        stats = coco_eval.stats.tolist()
        metrics = {
            "mAP_50_95": stats[0],
            "mAP_50": stats[1],
            "mAP_75": stats[2],
            "AP_small": stats[3],
            "AP_medium": stats[4],
            "AP_large": stats[5],
            "AR_1": stats[6],
            "AR_10": stats[7],
            "AR_100": stats[8],
            "AR_small": stats[9],
            "AR_medium": stats[10],
            "AR_large": stats[11],
        }

    # Clean up predictions JSON file to free disk space
    if dt_json_path.exists():
        dt_json_path.unlink()

    # Save metrics dict to destination file
    metrics_json_path = output_path / f"{run_name}_coco_metrics.json"
    with open(metrics_json_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"[SUCCESS] Saved metrics to: {metrics_json_path}")

    # 5. Log strict metrics to Weights & Biases
    try:
        import wandb
        from config import BenchmarkConfig

        cfg = BenchmarkConfig()

        # Connect to W&B API to log/update summary metrics
        print(f"[INFO] Connecting to W&B API to log strict metrics to: {run_name}")
        api = wandb.Api()
        runs = api.runs(f"{cfg.wandb_entity}/{cfg.wandb_project}")
        target_run = None
        for r in runs:
            if r.name == run_name:
                target_run = r
                break

        if target_run is not None:
            print(f"[INFO] Found active/finished run {run_name} (ID: {target_run.id}). Updating W&B summary...")
            for k, v in metrics.items():
                target_run.summary[f"metrics/{k}"] = v
            target_run.update()
            print("[SUCCESS] Successfully logged evaluation metrics to W&B via public API.")
        else:
            print(f"[WARNING] Run name '{run_name}' not found on W&B. Initializing a standalone evaluation logger...")
            run = wandb.init(
                project=cfg.wandb_project, entity=cfg.wandb_entity, name=run_name, job_type="evaluation", resume="allow"
            )
            wandb.log({f"metrics/{k}": v for k, v in metrics.items()})
            run.finish()
            print("[SUCCESS] Logged metrics to new/resumed standalone W&B run.")
    except Exception as exc:
        print(f"[WARNING] Failed to log strict metrics to W&B: {exc}")

    # 6. Clear GPU Cache
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        print("[INFO] Cleared GPU memory cache.")

    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Strict COCO Evaluation Module for YOLOv12-DINO3")
    parser.add_argument("--model", type=str, required=True, help="Path to model checkpoint (.pt file)")
    parser.add_argument("--data", type=str, required=True, help="Path to dataset YAML file (e.g., DOTAv1.yaml)")
    parser.add_argument("--split", type=str, default="val", help="Dataset split to evaluate (default: val)")
    parser.add_argument("--name", type=str, default=None, help="Output metrics prefix run name")
    parser.add_argument("--imgsz", type=int, default=640, help="Image size for inference (default: 640)")
    parser.add_argument("--device", type=str, default="0", help="CUDA device or 'cpu' (default: 0)")
    parser.add_argument("--output-dir", type=str, default="results", help="Directory to save evaluation files")
    parser.add_argument(
        "--fraction", type=float, default=None, help="Fraction of dataset split to evaluate (smoketest)"
    )

    # SAHI parameters
    parser.add_argument("--sahi", action="store_true", help="Enable Sliced Aided Hyper Inference (SAHI) evaluation")
    parser.add_argument("--slice-height", type=int, default=512, help="SAHI slice height")
    parser.add_argument("--slice-width", type=int, default=512, help="SAHI slice width")
    parser.add_argument("--overlap-height-ratio", type=float, default=0.2, help="SAHI overlap height ratio")
    parser.add_argument("--overlap-width-ratio", type=float, default=0.2, help="SAHI overlap width ratio")
    parser.add_argument("--postprocess-match-threshold", type=float, default=0.5, help="SAHI NMS match threshold")

    args = parser.parse_args()

    run_evaluation(
        model_path=args.model,
        data_yaml=args.data,
        split=args.split,
        run_name=args.name,
        imgsz=args.imgsz,
        device=args.device,
        output_dir=args.output_dir,
        fraction=args.fraction,
        sahi_enabled=args.sahi,
        sahi_slice_height=args.slice_height,
        sahi_slice_width=args.slice_width,
        sahi_overlap_height_ratio=args.overlap_height_ratio,
        sahi_overlap_width_ratio=args.overlap_width_ratio,
        sahi_postprocess_match_threshold=args.postprocess_match_threshold,
    )
