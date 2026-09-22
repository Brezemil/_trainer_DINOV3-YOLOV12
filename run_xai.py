#!/usr/bin/env python3
"""
CLI entry point for running Eigen-CAM Explainable AI (XAI) feature attribution
on YOLOv12, YOLOv12-DINO, and standard YOLO models.

Usage:
    python run_xai.py --weights yolov12s.pt --source test_image.jpg --output xai_output.png
    python run_xai.py --weights export/weights/yolo12s_triple_dino3_vitb16_seed_42_best.pt --source path/to/images/ --output results_xai/
"""

import argparse
import os
import sys
from pathlib import Path
import cv2
import numpy as np
import torch

# Ensure local package is in path
sys.path.insert(0, str(Path(__file__).parent))

from ultralytics import YOLO
from ultralytics.utils.xai import EigenCAMExplainer


def parse_args():
    parser = argparse.ArgumentParser(description="Generate Eigen-CAM Heatmaps for YOLOv12 and YOLOv12-DINO")
    parser.add_argument("--weights", type=str, required=True, help="Path to model weights (.pt)")
    parser.add_argument("--source", type=str, required=True, help="Path to input image or image directory")
    parser.add_argument("--output", type=str, default="xai_output", help="Output file or directory")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold for bounding box predictions")
    parser.add_argument("--layer", type=str, default=None, help="Target layer (e.g. 'model.model.9'). Default: auto-discover")
    parser.add_argument("--imgsz", type=int, default=1024, help="Inference resolution")
    parser.add_argument("--device", type=str, default="", help="Device: 'cpu' or 'cuda:0'")
    return parser.parse_args()


def process_image(explainer, yolo_model, img_path, out_path, conf=0.25, imgsz=1024):
    img_bgr = cv2.imread(str(img_path))
    if img_bgr is None:
        print(f"Warning: Could not read image {img_path}")
        return

    # Generate CAM
    cam_raw, overlay = explainer.generate_heatmap(img_bgr, input_size=(imgsz, imgsz))

    # Run detection predictions to overlay bounding boxes
    results = yolo_model.predict(img_path, conf=conf, imgsz=imgsz, verbose=False)
    boxes = results[0].boxes

    for box in boxes:
        xyxy = box.xyxy[0].cpu().numpy().astype(int)
        score = float(box.conf[0])
        cls_id = int(box.cls[0])
        label = f"{score:.2f}"
        
        cv2.rectangle(overlay, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
        cv2.putText(overlay, label, (xyxy[0], max(xyxy[1] - 5, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    cv2.imwrite(str(out_path), overlay)
    print(f"Saved: {out_path} (Detections: {len(boxes)})")


def main():
    args = parse_args()
    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
    
    print(f"Loading YOLO model from: {args.weights} (Device: {device})...")
    yolo_model = YOLO(args.weights)
    target_layers = [args.layer] if args.layer else None
    
    explainer = EigenCAMExplainer(yolo_model.model, target_layers=target_layers, device=torch.device(device))
    print(f"Target layer(s) hooked: {explainer.target_layers}")

    source_path = Path(args.source)
    if source_path.is_file():
        out_file = args.output if args.output.endswith(('.png', '.jpg', '.jpeg')) else os.path.join(args.output, f"xai_{source_path.name}")
        process_image(explainer, yolo_model, source_path, out_file, conf=args.conf, imgsz=args.imgsz)
    elif source_path.is_dir():
        image_exts = {'.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'}
        image_files = [p for p in source_path.iterdir() if p.suffix.lower() in image_exts]
        print(f"Found {len(image_files)} images in {source_path}")
        for img_p in image_files:
            out_file = os.path.join(args.output, f"xai_{img_p.stem}.png")
            process_image(explainer, yolo_model, img_p, out_file, conf=args.conf, imgsz=args.imgsz)
    else:
        print(f"Error: Source path {args.source} does not exist.")
        sys.exit(1)


if __name__ == "__main__":
    main()
