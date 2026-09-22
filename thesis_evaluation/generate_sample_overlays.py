# Visual Prediction Overlay Generator for Representative Testset Scenes
# Produces high-resolution 300 DPI multi-panel comparison figures showing Ground Truth vs Architecture Predictions
# Evaluates scenes under Standard Confidence (c=0.25) and Calibrated Optimal F1 (c=c*)

import os
import sys
import json
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

sys.stdout.reconfigure(line_buffering=True)

PREDICTIONS_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"
IMAGES_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"
LABELS_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\labels"
OUTPUT_DIR = os.path.join(PREDICTIONS_DIR, "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MIRROR_DIRS = [
    OUTPUT_DIR,
    r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\thesis_evaluation",
    r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363",
]

# Model definitions for side-by-side visual panels
MODELS_TO_SHOW = [
    {"id": "1_yolo12s_undistilled_seed100", "title": "Pure CNN (YOLO12s)", "color": "#1f77b4", "opt_conf": 0.2482},
    {"id": "2_vitt16_dfine_undistilled_seed42", "title": "ViT (DINOv3 ViT-T + D-FINE)", "color": "#2ca02c", "opt_conf": 0.5200},
    {"id": "3_yolo12s_distilled_sat493m_seed999", "title": "Distilled CNN (YOLO12s SAT-493M)", "color": "#ff7f0e", "opt_conf": 0.2973},
    {"id": "4_vitt16_distilled_lvd1689m_seed42", "title": "Distilled ViT (ViT-T LVD-1689M)", "color": "#d62728", "opt_conf": 0.5650},
    {"id": "5_yolo12s_triple_dino3_seed42", "title": "Multi-Scale Fused (Triple DINOv3)", "color": "#9467bd", "opt_conf": 0.2730},
]

def load_ground_truth(stem):
    label_path = os.path.join(LABELS_DIR, f"{stem}.txt")
    boxes = []
    if os.path.exists(label_path) and os.path.getsize(label_path) > 0:
        with open(label_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 5:
                    cls_id = int(parts[0])
                    xc, yc, w, h = map(float, parts[1:5])
                    xmin = (xc - w / 2.0) * 1024.0
                    ymin = (yc - h / 2.0) * 1024.0
                    bw = w * 1024.0
                    bh = h * 1024.0
                    boxes.append([xmin, ymin, bw, bh])
    return boxes

def load_model_preds(model_id, stem, mode="standard"):
    if mode == "standard":
        txt_path = os.path.join(PREDICTIONS_DIR, "predictions_yolo", model_id, f"{stem}.txt")
    else:
        txt_path = os.path.join(PREDICTIONS_DIR, "optimal_f1_conf", "predictions_yolo", model_id, f"{stem}.txt")
        
    boxes = []
    if os.path.exists(txt_path) and os.path.getsize(txt_path) > 0:
        with open(txt_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 6:
                    cls_id = int(parts[0])
                    xc, yc, w, h, conf = map(float, parts[1:6])
                    xmin = (xc - w / 2.0) * 1024.0
                    ymin = (yc - h / 2.0) * 1024.0
                    bw = w * 1024.0
                    bh = h * 1024.0
                    boxes.append({"bbox": [xmin, ymin, bw, bh], "conf": conf})
    return boxes

def render_comparison_figure(stem, figure_filename, scene_description, mode="standard"):
    img_path = os.path.join(IMAGES_DIR, f"{stem}.jpg")
    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        return
        
    img = Image.open(img_path).convert("RGB")
    gt_boxes = load_ground_truth(stem)
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 11), dpi=300)
    axes = axes.flatten()
    
    # Panel 0: Ground Truth
    ax0 = axes[0]
    ax0.imshow(img)
    gt_title = f"Ground Truth (N={len(gt_boxes)} Verified Canopies)" if len(gt_boxes) > 0 else "Ground Truth (N=0, Negative Background Tile)"
    ax0.set_title(gt_title, fontweight='bold', fontsize=11, color='#1b5e20')
    ax0.axis('off')
    for b in gt_boxes:
        rect = patches.Rectangle((b[0], b[1]), b[2], b[3], linewidth=2.2, edgecolor='#00e676', facecolor='none', linestyle='-')
        ax0.add_patch(rect)
        
    # Panels 1 to 5: Models
    for i, m_info in enumerate(MODELS_TO_SHOW, 1):
        ax = axes[i]
        ax.imshow(img)
        preds = load_model_preds(m_info["id"], stem, mode=mode)
        
        conf_str = f"c={m_info['opt_conf']:.3f}" if mode == "optimal_f1" else "c=0.25"
        ax.set_title(f"{m_info['title']}\n[{conf_str}] (N={len(preds)} Detections)", fontweight='bold', fontsize=10.5, color=m_info["color"])
        ax.axis('off')
        
        for p in preds:
            b = p["bbox"]
            conf = p["conf"]
            rect = patches.Rectangle((b[0], b[1]), b[2], b[3], linewidth=2.0, edgecolor=m_info["color"], facecolor='none', linestyle='-')
            ax.add_patch(rect)
            ax.text(b[0] + 3, b[1] + 16, f"{conf:.2f}", color='white', fontsize=7.5, fontweight='bold',
                    bbox=dict(boxstyle='square,pad=0.15', facecolor=m_info["color"], alpha=0.85, edgecolor='none'))
                    
    regime_str = "Standard Confidence (c=0.25)" if mode == "standard" else "Calibrated Optimal F1 Confidence (c=c*)"
    plt.suptitle(f"Multi-Architecture Canopy Detections: {scene_description} [{regime_str}]\nImage: {stem}.jpg (1024×1024 px, GSD 2.1 cm)", 
                 fontsize=13, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    for d in MIRROR_DIRS:
        target = os.path.join(d, figure_filename)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        fig.savefig(target, dpi=300, bbox_inches='tight', pad_inches=0.15)
    print(f"Saved {figure_filename} across all mirrors.", flush=True)
    plt.close(fig)

def main():
    print("Generating Visual Comparison Figures...", flush=True)
    
    # Standard Confidence Visual Overlays (c=0.25)
    dense_stem = "DJI_20240620114403_0350_Zenmuse-L1-mission_3276_1638"
    render_comparison_figure(dense_stem, "fig4_sample_overlay_dense_canopies.png", "Dense Forest Stand Multi-Target Cluster", mode="standard")
    
    solitary_stem = "DJI_20230825114019_0034_0_1638"
    render_comparison_figure(solitary_stem, "fig5_sample_overlay_solitary_canopy.png", "Isolated Solitary Canopy on Forest Margin", mode="standard")
    
    bg_stem = "DJI_20230825114015_0031_0_0"
    render_comparison_figure(bg_stem, "fig6_sample_overlay_background_false_alarm.png", "Negative Background Terrain (False Alarm Audit)", mode="standard")
    
    # Check if optimal F1 preds exist, and render them too
    opt_check = os.path.join(PREDICTIONS_DIR, "optimal_f1_conf", "predictions_yolo", "2_vitt16_dfine_undistilled_seed42")
    if os.path.exists(opt_check) and len(glob.glob(os.path.join(opt_check, "*.txt"))) > 100:
        render_comparison_figure(dense_stem, "fig4b_sample_overlay_dense_canopies_optimal_f1.png", "Dense Forest Stand Multi-Target Cluster", mode="optimal_f1")
        render_comparison_figure(bg_stem, "fig6b_sample_overlay_background_false_alarm_optimal_f1.png", "Negative Background Terrain (False Alarm Suppression)", mode="optimal_f1")
        
    print("Visual comparison figures generation completed!", flush=True)

if __name__ == "__main__":
    main()
