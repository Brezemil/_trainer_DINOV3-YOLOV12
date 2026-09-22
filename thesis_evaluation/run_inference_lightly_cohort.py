# Master Batch Inference for Lightly Models Cohort (YOLO12s Stock, YOLO12s SAT, ViT-T16 Stock, ViT-T16 LVD)
# Target Dataset: E:\Götterbaum\_export_data\testset_unlabeled_combined
# Output Destination: E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions

import os
import sys
import time
import json
import glob
import gc
from PIL import Image
import torch

sys.stdout.reconfigure(line_buffering=True)

LIGHTLY_REPO = r"C:\Users\emilb\Documents\GitHub\_trainer_lightly"
if LIGHTLY_REPO not in sys.path:
    sys.path.insert(0, LIGHTLY_REPO)

from eval_utils import safe_load_model
from ultralytics import YOLO

IMAGES_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"
OUTPUT_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"
CONF_THRESHOLD = 0.25

MODELS = [
    # 1. Undistilled YOLO12s
    {
        "id": "1_yolo12s_undistilled_seed42",
        "name": "YOLO12s (Seed 42)",
        "category": "Pure CNN",
        "framework": "yolo",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\yolo12s_stock_seed42_best.pt",
    },
    {
        "id": "1_yolo12s_undistilled_seed100",
        "name": "YOLO12s (Seed 100)",
        "category": "Pure CNN",
        "framework": "yolo",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\yolo12s_stock_seed100_best.pt",
    },
    {
        "id": "1_yolo12s_undistilled_seed999",
        "name": "YOLO12s (Seed 999)",
        "category": "Pure CNN",
        "framework": "yolo",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\yolo12s_stock_seed999_best.pt",
    },
    # 2. Undistilled ViT-T16 (DINOv3 ViT-T + D-FINE)
    {
        "id": "2_vitt16_dfine_undistilled_seed42",
        "name": "ViT-T16 + D-FINE (Seed 42)",
        "category": "Vision Transformer",
        "framework": "vit",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\vitt16_stock_seed42_best.pt",
    },
    {
        "id": "2_vitt16_dfine_undistilled_seed100",
        "name": "ViT-T16 + D-FINE (Seed 100)",
        "category": "Vision Transformer",
        "framework": "vit",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\vitt16_stock_seed100_best.pt",
    },
    {
        "id": "2_vitt16_dfine_undistilled_seed999",
        "name": "ViT-T16 + D-FINE (Seed 999)",
        "category": "Vision Transformer",
        "framework": "vit",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\vitt16_stock_seed999_best.pt",
    },
    # 3. Distilled YOLO12s (SAT-493M Teacher)
    {
        "id": "3_yolo12s_distilled_sat493m_seed42",
        "name": "YOLO12s SAT-493M (Seed 42)",
        "category": "Distilled CNN",
        "framework": "yolo",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\yolo12s_sat493m_seed42_best.pt",
    },
    {
        "id": "3_yolo12s_distilled_sat493m_seed100",
        "name": "YOLO12s SAT-493M (Seed 100)",
        "category": "Distilled CNN",
        "framework": "yolo",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\yolo12s_sat493m_seed100_best.pt",
    },
    {
        "id": "3_yolo12s_distilled_sat493m_seed999",
        "name": "YOLO12s SAT-493M (Seed 999)",
        "category": "Distilled CNN",
        "framework": "yolo",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\yolo12s_sat493m_seed999_best.pt",
    },
    # 4. Distilled ViT-T16 (LVD-1689M Teacher)
    {
        "id": "4_vitt16_distilled_lvd1689m_seed42",
        "name": "ViT-T16 LVD-1689M (Seed 42)",
        "category": "Distilled ViT",
        "framework": "vit",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\vitt16_lvd1689m_seed42_best.pt",
    },
    {
        "id": "4_vitt16_distilled_lvd1689m_seed100",
        "name": "ViT-T16 LVD-1689M (Seed 100)",
        "category": "Distilled ViT",
        "framework": "vit",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\vitt16_lvd1689m_seed100_best.pt",
    },
    {
        "id": "4_vitt16_distilled_lvd1689m_seed999",
        "name": "ViT-T16 LVD-1689M (Seed 999)",
        "category": "Distilled ViT",
        "framework": "vit",
        "path": r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\vitt16_lvd1689m_seed999_best.pt",
    },
]

def run_yolo(cfg, image_paths, yolo_dir, json_path):
    print(f"\n[START] Processing YOLO model: {cfg['name']} ({cfg['id']})", flush=True)
    t_start = time.time()
    model = YOLO(cfg['path'])
    all_preds = []
    total_detections = 0
    imgs_with_detections = 0
    total_imgs = len(image_paths)

    # Use IMAGES_DIR string as source to prevent autocast_list memory loading
    for idx, res in enumerate(model.predict(source=IMAGES_DIR, batch=16, imgsz=1024, half=True, conf=CONF_THRESHOLD, device=0, stream=True, verbose=False), 1):
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

        if idx % 500 == 0 or idx == total_imgs:
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

def run_vit(cfg, image_paths, yolo_dir, json_path):
    print(f"\n[START] Processing ViT model: {cfg['name']} ({cfg['id']})", flush=True)
    t_start = time.time()
    model = safe_load_model(cfg['path'], device=0)
    if model.training or not model.postprocessor.deploy_mode:
        model.deploy()

    all_preds = []
    total_detections = 0
    imgs_with_detections = 0
    batch_size = 4
    total_imgs = len(image_paths)

    for i in range(0, total_imgs, batch_size):
        batch_paths = image_paths[i:i + batch_size]
        xs = []
        metas = []
        for p in batch_paths:
            x, meta = model.preprocess_image(p)
            xs.append(x)
            metas.append(meta)

        x_batch = torch.stack(xs)
        batch_input = model.preprocess_batch(x_batch)
        with torch.no_grad():
            raw = model.forward_backend(batch_input)
            batch_preds = model.postprocess(raw, metas, threshold=CONF_THRESHOLD)

        for p, res in zip(batch_paths, batch_preds):
            img_name = os.path.basename(p)
            img_stem = os.path.splitext(img_name)[0]
            txt_path = os.path.join(yolo_dir, f"{img_stem}.txt")

            boxes = res.get("bboxes")
            scores = res.get("scores")
            labels = res.get("labels")

            txt_lines = []
            if boxes is not None and len(boxes) > 0:
                imgs_with_detections += 1
                for box, score, label in zip(boxes.cpu().numpy(), scores.cpu().numpy(), labels.cpu().numpy()):
                    xmin, ymin, xmax, ymax = map(float, box)
                    w = xmax - xmin
                    h = ymax - ymin
                    xc = (xmin + xmax) / 2.0 / 1024.0
                    yc = (ymin + ymax) / 2.0 / 1024.0
                    wn = w / 1024.0
                    hn = h / 1024.0
                    cls_id = int(label)
                    conf = float(score)

                    txt_lines.append(f"{cls_id} {xc:.6f} {yc:.6f} {wn:.6f} {hn:.6f} {conf:.5f}")

                    all_preds.append({
                        "image_id": len(all_preds) + 1,
                        "file_name": img_name,
                        "category_id": cls_id,
                        "category_name": "Ailanthus altissima",
                        "bbox": [round(xmin, 2), round(ymin, 2), round(w, 2), round(h, 2)],
                        "score": round(conf, 5)
                    })
                    total_detections += 1

            with open(txt_path, "w", encoding="utf-8") as f:
                if txt_lines:
                    f.write("\n".join(txt_lines) + "\n")

        curr_count = min(i + batch_size, total_imgs)
        if curr_count % 500 < batch_size or curr_count == total_imgs:
            fps = curr_count / (time.time() - t_start)
            eta_s = (total_imgs - curr_count) / fps if fps > 0 else 0
            print(f"  [{cfg['id']}] {curr_count}/{total_imgs} ({curr_count/total_imgs*100:.1f}%) - {total_detections} boxes found ({fps:.1f} FPS, ETA: {eta_s:.0f}s)", flush=True)

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
    print("Master Batch Inference: Lightly Models Cohort (12 Models)", flush=True)
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

        if cfg["framework"] == "yolo":
            run_yolo(cfg, image_paths, yolo_dir, json_path)
        elif cfg["framework"] == "vit":
            run_vit(cfg, image_paths, yolo_dir, json_path)

    print("\n======================================================================", flush=True)
    print("All 12 Lightly Models Inference Completed Successfully!", flush=True)
    print("======================================================================", flush=True)

if __name__ == "__main__":
    main()
