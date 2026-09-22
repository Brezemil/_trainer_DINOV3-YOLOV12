# Master Batch Inference for Triple DINO YOLO12s Models (Seeds 42, 100, 999)
# Target Dataset: E:\Götterbaum\_export_data\testset_unlabeled_combined
# Output Destination: E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions

import os
import sys
import time
import json
import glob
import gc
import torch

sys.stdout.reconfigure(line_buffering=True)
from ultralytics import YOLO

IMAGES_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"
OUTPUT_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"
CONF_THRESHOLD = 0.25

MODELS = [
    {
        "id": "5_yolo12s_triple_dino3_seed42",
        "name": "YOLO12s Triple DINOv3 (Seed 42)",
        "category": "Multi-Scale Fused",
        "path": r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\weights\yolo12s_triple_dino3_vitb16_seed_42_best.pt",
    },
    {
        "id": "5_yolo12s_triple_dino3_seed100",
        "name": "YOLO12s Triple DINOv3 (Seed 100)",
        "category": "Multi-Scale Fused",
        "path": r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\weights\yolo12s_triple_dino3_vitb16_seed_100_best.pt",
    },
    {
        "id": "5_yolo12s_triple_dino3_seed999",
        "name": "YOLO12s Triple DINOv3 (Seed 999)",
        "category": "Multi-Scale Fused",
        "path": r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\weights\yolo12s_triple_dino3_vitb16_seed_999_best.pt",
    },
]

def run_triple_dino(cfg, image_paths, yolo_dir, json_path):
    print(f"\n[START] Processing Triple DINO model: {cfg['name']} ({cfg['id']})", flush=True)
    t_start = time.time()
    model = YOLO(cfg['path'])
    all_preds = []
    total_detections = 0
    imgs_with_detections = 0
    total_imgs = len(image_paths)

    # Use IMAGES_DIR string as source to prevent autocast_list memory thrashing
    for idx, res in enumerate(model.predict(source=IMAGES_DIR, batch=4, imgsz=1024, half=True, conf=CONF_THRESHOLD, device=0, stream=True, verbose=False), 1):
        img_name = os.path.basename(res.path)
        img_stem = os.path.splitext(img_name)[0]
        txt_path = os.path.join(yolo_dir, f"{img_stem}.txt")

        boxes = res.boxes
        txt_lines = []
        if boxes is not None and len(boxes) > 0:
            imgs_with_detections += 1
            for b in boxes:
                xywhn = b.xywhn[0].cpu().tolist()
                conf = float(b.conf[0].cpu())
                cls_id = int(b.cls[0].cpu())

                txt_lines.append(f"{cls_id} {xywhn[0]:.6f} {xywhn[1]:.6f} {xywhn[2]:.6f} {xywhn[3]:.6f} {conf:.5f}")

                xyxy = b.xyxy[0].cpu().tolist()
                xmin, ymin, xmax, ymax = xyxy
                all_preds.append({
                    "image_id": idx,
                    "file_name": img_name,
                    "category_id": cls_id,
                    "category_name": "Ailanthus altissima",
                    "bbox": [round(xmin, 2), round(ymin, 2), round(xmax - xmin, 2), round(ymax - ymin, 2)],
                    "score": round(conf, 5)
                })
                total_detections += 1

        with open(txt_path, "w", encoding="utf-8") as f:
            if txt_lines:
                f.write("\n".join(txt_lines) + "\n")

        if idx % 250 == 0 or idx == total_imgs:
            fps = idx / (time.time() - t_start)
            eta_s = (total_imgs - idx) / fps if fps > 0 else 0
            print(f"  [{cfg['id']}] {idx}/{total_imgs} ({idx/total_imgs*100:.1f}%) - {total_detections} boxes found ({fps:.1f} FPS, ETA: {eta_s:.0f}s)", flush=True)

    # Ensure all 4,721 files exist
    for p in image_paths:
        stem = os.path.splitext(os.path.basename(p))[0]
        tp = os.path.join(yolo_dir, f"{stem}.txt")
        if not os.path.exists(tp):
            open(tp, "w").close()

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_preds, f, indent=2)

    dt = time.time() - t_start
    print(f"[DONE] {cfg['id']} finished in {dt:.1f}s. Boxes: {total_detections}, Positive images: {imgs_with_detections}/{total_imgs} ({total_imgs/dt:.1f} FPS)", flush=True)

    del model
    torch.cuda.empty_cache()
    gc.collect()

def main():
    print("======================================================================", flush=True)
    print("Master Batch Inference: Triple DINO Models (3 Seeds)", flush=True)
    print(f"Images Directory: {IMAGES_DIR}", flush=True)
    print(f"Output Directory: {OUTPUT_DIR}", flush=True)
    print(f"Confidence Threshold: {CONF_THRESHOLD}", flush=True)
    print("======================================================================", flush=True)

    image_paths = sorted(glob.glob(os.path.join(IMAGES_DIR, "*.jpg")))
    print(f"Found {len(image_paths)} total test images.", flush=True)
    assert len(image_paths) == 4721, f"Expected 4,721 images, found {len(image_paths)}"

    yolo_base = os.path.join(OUTPUT_DIR, "predictions_yolo")
    json_base = os.path.join(OUTPUT_DIR, "predictions_json")
    os.makedirs(yolo_base, exist_ok=True)
    os.makedirs(json_base, exist_ok=True)

    for idx, cfg in enumerate(MODELS, 1):
        print(f"\n>>> [{idx}/{len(MODELS)}] Checking Model: {cfg['id']}", flush=True)
        yolo_dir = os.path.join(yolo_base, cfg["id"])
        json_path = os.path.join(json_base, f"{cfg['id']}.json")
        os.makedirs(yolo_dir, exist_ok=True)

        # Check if already completed
        if os.path.exists(json_path) and os.path.getsize(json_path) > 100:
            existing_txts = len(glob.glob(os.path.join(yolo_dir, "*.txt")))
            if existing_txts >= 4721:
                print(f"  >> Already completed ({existing_txts} txt files and valid json). Skipping.", flush=True)
                continue

        run_triple_dino(cfg, image_paths, yolo_dir, json_path)

    print("\n======================================================================", flush=True)
    print("All 3 Triple DINO Models Inference Completed Successfully!", flush=True)
    print("======================================================================", flush=True)

if __name__ == "__main__":
    main()
