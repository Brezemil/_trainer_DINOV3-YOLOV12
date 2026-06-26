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

    # Save path for the GT JSON
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)
    if fraction is not None:
        gt_json_path = output_dir_path / f"coco_gt_{split}_frac_{fraction}.json"
    else:
        gt_json_path = output_dir_path / f"coco_gt_{split}.json"

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
    model_path, data_yaml, split="val", run_name=None, imgsz=640, device="0", output_dir="results", fraction=None
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

    print(f"[INFO] Running inference on {split} images...")
    # Use list of sampled filepaths if fraction is specified to save time (smoketest)
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

    # 3. Match prediction boxes to GT integer IDs
    predictions = []
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
            # xyxy coordinate format: x_min, y_min, x_max, y_max
            xyxy = box.xyxy[0].tolist()
            w_box = xyxy[2] - xyxy[0]
            h_box = xyxy[3] - xyxy[1]

            predictions.append(
                {"image_id": img_id, "category_id": cls_id, "bbox": [xyxy[0], xyxy[1], w_box, h_box], "score": score}
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

        # Save standard COCO evaluation stats
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

    # 5. Clear GPU Cache
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
    )
