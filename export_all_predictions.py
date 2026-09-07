#!/usr/bin/env python3
"""
Generate and organize all model predictions in both YOLO format (.txt)
and COCO format (.json), plus tabular predictions.csv, across all splits and seeds.
"""

import os
import json
import shutil
from pathlib import Path
import pandas as pd

CURRENT_DIR = Path(__file__).parent.resolve()
EXPORT_DIR = CURRENT_DIR / "export"
EVAL_RESULTS_DIR = EXPORT_DIR / "evaluation_results"
PRED_DIR = EXPORT_DIR / "predictions"
COCO_FORMAT_DIR = PRED_DIR / "coco_format"
YOLO_FORMAT_DIR = PRED_DIR / "yolo_format"

GT_TEST_PATH = EVAL_RESULTS_DIR / "coco_gt_test_f48b69af.json"
GT_VAL_PATH = EVAL_RESULTS_DIR / "coco_gt_val_8eddf691.json"


def load_gt_images(gt_path: Path):
    with open(gt_path, "r") as f:
        data = json.load(f)
    id_to_info = {}
    for img in data["images"]:
        id_to_info[img["id"]] = {
            "file_name": img["file_name"],
            "stem": Path(img["file_name"]).stem,
            "width": img.get("width", 1024),
            "height": img.get("height", 1024),
        }
    return id_to_info


def coco_to_yolo_and_csv(predictions: list, gt_info: dict, yolo_out_dir: Path, csv_out_path: Path = None, include_all_tiles: bool = True):
    yolo_out_dir.mkdir(parents=True, exist_ok=True)

    # Group predictions by image_id
    preds_by_img = {img_id: [] for img_id in gt_info.keys()}
    for p in predictions:
        img_id = p["image_id"]
        if img_id in preds_by_img:
            preds_by_img[img_id].append(p)

    csv_rows = []

    for img_id, img_data in gt_info.items():
        stem = img_data["stem"]
        filename = img_data["file_name"]
        w_img = img_data["width"]
        h_img = img_data["height"]
        img_preds = preds_by_img.get(img_id, [])

        txt_file = yolo_out_dir / f"{stem}.txt"

        if img_preds:
            lines = []
            for p in img_preds:
                # COCO bbox: [xmin, ymin, width, height]
                xmin, ymin, w, h = p["bbox"]
                score = p["score"]
                cat_id = p.get("category_id", 1)
                yolo_cls = cat_id - 1 if cat_id > 0 else 0

                # Normalized coordinates
                xc = (xmin + w / 2.0) / w_img
                yc = (ymin + h / 2.0) / h_img
                wn = w / w_img
                hn = h / h_img

                lines.append(f"{yolo_cls} {xc:.6f} {yc:.6f} {wn:.6f} {hn:.6f} {score:.6f}\n")

                if csv_out_path:
                    csv_rows.append({
                        "image_id": img_id,
                        "filename": filename,
                        "class_id": yolo_cls,
                        "class_name": "A. altissima",
                        "confidence": round(score, 6),
                        "xmin": round(xmin, 2),
                        "ymin": round(ymin, 2),
                        "xmax": round(xmin + w, 2),
                        "ymax": round(ymin + h, 2),
                    })

            with open(txt_file, "w") as f:
                f.writelines(lines)
        elif include_all_tiles:
            # Write empty label file for negative/background tile
            with open(txt_file, "w") as f:
                pass

    if csv_out_path and csv_rows:
        df = pd.DataFrame(csv_rows)
        df.to_csv(csv_out_path, index=False)


def main():
    print("=" * 80)
    print("EXPORTING ALL PREDICTIONS IN BOTH YOLO (.txt) AND COCO (.json) FORMATS")
    print("=" * 80)

    COCO_FORMAT_DIR.mkdir(parents=True, exist_ok=True)
    YOLO_FORMAT_DIR.mkdir(parents=True, exist_ok=True)

    test_gt_info = load_gt_images(GT_TEST_PATH)
    val_gt_info = load_gt_images(GT_VAL_PATH)

    print(f"Loaded {len(test_gt_info)} test images and {len(val_gt_info)} val images ground truth.")

    SEEDS = [42, 100, 999]

    # Process all combinations
    # 1. Optimal F1 Hold-out Test predictions
    # 2. Standard Swept Test predictions
    # 3. Standard Swept Validation predictions

    for seed in SEEDS:
        run_name = f"yolo12s_triple_dino3_vitb16_seed_{seed}"
        print(f"\nProcessing {run_name}...")

        # 1. OPTIMAL F1 TEST PREDICTIONS
        opt_src = EVAL_RESULTS_DIR / f"{run_name}_opt_f1_TEST_coco_predictions.json"
        if opt_src.exists():
            with open(opt_src, "r") as f:
                opt_preds = json.load(f)

            # Ensure in coco_format/
            coco_dest = COCO_FORMAT_DIR / opt_src.name
            shutil.copy2(opt_src, coco_dest)
            print(f"  [COCO] Copied {opt_src.name} -> {coco_dest.relative_to(EXPORT_DIR)} ({len(opt_preds)} detections)")

            # Save in yolo_format/yolo12s_triple_dino3_vitb16_seed_<seed>_opt_f1/
            yolo_opt_dir = YOLO_FORMAT_DIR / f"{run_name}_opt_f1"
            coco_to_yolo_and_csv(opt_preds, test_gt_info, yolo_opt_dir, include_all_tiles=True)
            print(f"  [YOLO] Saved 510 YOLO format .txt files -> {yolo_opt_dir.relative_to(EXPORT_DIR)}")

            # Standard Model Bundle directory: export/predictions/<run_name>/
            model_bundle_dir = PRED_DIR / run_name
            model_bundle_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(opt_src, model_bundle_dir / "coco_predictions.json")
            csv_dest = model_bundle_dir / "predictions.csv"
            yolo_labels_dest = model_bundle_dir / "yolo_labels"
            coco_to_yolo_and_csv(opt_preds, test_gt_info, yolo_labels_dest, csv_out_path=csv_dest, include_all_tiles=True)
            print(f"  [Bundle] Created {model_bundle_dir.relative_to(EXPORT_DIR)} with coco_predictions.json, predictions.csv, yolo_labels/")

        # 2. STANDARD TEST PREDICTIONS (conf=0.001)
        test_src = EVAL_RESULTS_DIR / f"{run_name}_TEST_coco_predictions.json"
        if test_src.exists():
            with open(test_src, "r") as f:
                test_preds = json.load(f)

            # Ensure in coco_format/
            coco_dest = COCO_FORMAT_DIR / test_src.name
            shutil.copy2(test_src, coco_dest)
            print(f"  [COCO] Copied {test_src.name} -> {coco_dest.relative_to(EXPORT_DIR)} ({len(test_preds)} detections)")

            # Save in yolo_format/yolo12s_triple_dino3_vitb16_seed_<seed>_test/
            yolo_test_dir = YOLO_FORMAT_DIR / f"{run_name}_test"
            coco_to_yolo_and_csv(test_preds, test_gt_info, yolo_test_dir, include_all_tiles=True)
            print(f"  [YOLO] Saved 510 YOLO format .txt files -> {yolo_test_dir.relative_to(EXPORT_DIR)}")

        # 3. STANDARD VAL PREDICTIONS (conf=0.001)
        val_src = EVAL_RESULTS_DIR / f"{run_name}_VAL_coco_predictions.json"
        if val_src.exists():
            with open(val_src, "r") as f:
                val_preds = json.load(f)

            # Ensure in coco_format/
            coco_dest = COCO_FORMAT_DIR / val_src.name
            shutil.copy2(val_src, coco_dest)
            print(f"  [COCO] Copied {val_src.name} -> {coco_dest.relative_to(EXPORT_DIR)} ({len(val_preds)} detections)")

            # Save in yolo_format/yolo12s_triple_dino3_vitb16_seed_<seed>_val/
            yolo_val_dir = YOLO_FORMAT_DIR / f"{run_name}_val"
            coco_to_yolo_and_csv(val_preds, val_gt_info, yolo_val_dir, include_all_tiles=True)
            print(f"  [YOLO] Saved 510 YOLO format .txt files -> {yolo_val_dir.relative_to(EXPORT_DIR)}")

    print("\n" + "=" * 80)
    print("ALL PREDICTIONS EXPORTED AND ORGANIZED IN YOLO AND COCO FORMATS!")
    print("=" * 80)


if __name__ == "__main__":
    main()
