# Script to generate calibrated Optimal F1 (c*) prediction files from standard predictions (where c* >= 0.25)
# Generates both structured JSON and individual YOLO-format .txt files (4,721 files per model)

import os
import sys
import json
import glob

sys.stdout.reconfigure(line_buffering=True)

PREDICTIONS_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"
IMAGES_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"
OPT_DIR = os.path.join(PREDICTIONS_DIR, "optimal_f1_conf")

OPTIMAL_CONFS = {
    "1_yolo12s_undistilled_seed42": 0.3283,
    "1_yolo12s_undistilled_seed100": 0.2482,
    "1_yolo12s_undistilled_seed999": 0.3013,
    "2_vitt16_dfine_undistilled_seed42": 0.5200,
    "2_vitt16_dfine_undistilled_seed100": 0.5200,
    "2_vitt16_dfine_undistilled_seed999": 0.5200,
    "3_yolo12s_distilled_sat493m_seed42": 0.2673,
    "3_yolo12s_distilled_sat493m_seed100": 0.3493,
    "3_yolo12s_distilled_sat493m_seed999": 0.2973,
    "4_vitt16_distilled_lvd1689m_seed42": 0.5650,
    "4_vitt16_distilled_lvd1689m_seed100": 0.5600,
    "4_vitt16_distilled_lvd1689m_seed999": 0.5700,
    "5_yolo12s_triple_dino3_seed42": 0.2730,
    "5_yolo12s_triple_dino3_seed100": 0.2730,
    "5_yolo12s_triple_dino3_seed999": 0.3030,
}

def process_model(model_id, opt_conf, all_stems):
    norm_json = os.path.join(PREDICTIONS_DIR, "predictions_json", f"{model_id}.json")
    if not os.path.exists(norm_json) or os.path.getsize(norm_json) < 100:
        return False
        
    out_yolo_dir = os.path.join(OPT_DIR, "predictions_yolo", model_id)
    out_json_path = os.path.join(OPT_DIR, "predictions_json", f"{model_id}.json")
    
    # Check if already processed
    if os.path.exists(out_json_path) and os.path.getsize(out_json_path) > 100:
        existing = len(glob.glob(os.path.join(out_yolo_dir, "*.txt")))
        if existing >= 4721:
            print(f"[{model_id}] Already generated optimal F1 predictions ({existing} txts). Skipping.", flush=True)
            return True

    os.makedirs(out_yolo_dir, exist_ok=True)
    os.makedirs(os.path.dirname(out_json_path), exist_ok=True)

    print(f"[{model_id}] Filtering predictions at c* = {opt_conf:.4f}...", flush=True)
    with open(norm_json, "r", encoding="utf-8") as f:
        preds = json.load(f)

    opt_preds = [p for p in preds if p["score"] >= opt_conf]
    print(f"  Total boxes: {len(preds)} -> {len(opt_preds)} (filtered {len(preds) - len(opt_preds)} low-conf boxes)", flush=True)

    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(opt_preds, f, indent=2)

    # Group by stem for yolo txt
    by_stem = {}
    for p in opt_preds:
        stem = os.path.splitext(p["file_name"])[0]
        by_stem.setdefault(stem, []).append(p)

    for stem in all_stems:
        tp = os.path.join(out_yolo_dir, f"{stem}.txt")
        boxes = by_stem.get(stem, [])
        lines = []
        for b in boxes:
            cls_id = b["category_id"]
            xmin, ymin, w, h = b["bbox"]
            xc = (xmin + w / 2.0) / 1024.0
            yc = (ymin + h / 2.0) / 1024.0
            wn = w / 1024.0
            hn = h / 1024.0
            conf = b["score"]
            lines.append(f"{cls_id} {xc:.6f} {yc:.6f} {wn:.6f} {hn:.6f} {conf:.5f}")

        with open(tp, "w", encoding="utf-8") as f:
            if lines:
                f.write("\n".join(lines) + "\n")

    print(f"  Wrote {len(all_stems)} YOLO txt files to {out_yolo_dir}", flush=True)
    return True

def main():
    print("======================================================================", flush=True)
    print("Generating Optimal F1 Predictions (c = c*) from Available Inference", flush=True)
    print("======================================================================", flush=True)

    all_img_paths = sorted(glob.glob(os.path.join(IMAGES_DIR, "*.jpg")))
    all_stems = [os.path.splitext(os.path.basename(p))[0] for p in all_img_paths]
    print(f"Found {len(all_stems)} total test images.", flush=True)

    processed = 0
    for model_id, opt_conf in OPTIMAL_CONFS.items():
        if process_model(model_id, opt_conf, all_stems):
            processed += 1

    print(f"\nCompleted {processed}/{len(OPTIMAL_CONFS)} models.", flush=True)

if __name__ == "__main__":
    main()
