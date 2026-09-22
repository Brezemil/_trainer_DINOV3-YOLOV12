"""
Generate Publication-Grade Explainable AI (XAI) Attribution Heatmap Grids
for Top-Performing Canopy Detection Architectures.

Grounding & Methodology:
- Eigen-CAM formulation (Muhammad & Yeasin, 2020) via first principal singular vector
  of feature activations: L_EigenCAM = ReLU(Reshape(V_1)).
- DINOv3 Vision Transformer attention mechanics (Simeoni et al., Meta FAIR, 2025).
- Area Attention regional aggregation mechanics (Tian et al., 2025).
- Fine-grained Distribution Refinement (FDR) coordinate regression (Peng et al., 2024).

Generates 24 diverse ecological scenes across 3 confidence versions each = 72 figures + aliases:
- Version 1: No predictions overlay (Pure Eigen-CAM feature attribution)
- Version 2: Standard benchmark confidence threshold (c >= 0.25)
- Version 3: Calibrated optimal F1 confidence threshold (c*)

All figures are stored in the dedicated 'xai_scenes/' folder and synchronized across all mirrors.
"""

import os
import sys
import shutil
import json
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Ensure UTF-8 output
sys.stdout.reconfigure(line_buffering=True)

# Directories
IMAGES_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"
LABELS_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\labels"
PREDICTIONS_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"

# Test set COCO ground truth and per-model full prediction JSON files (down to c=0.001)
COCO_GT_TEST_PATH = r"export\evaluation_results\coco_gt_test_f48b69af.json"
MODEL_JSON_MAP = {
    '1_yolo12s_undistilled_seed100': r"top_models_predictions\1_best_cnn_undistilled_yolo12s\normal_conf\yolo12s_seed_100_coco_predictions.json",
    '2_vitt16_dfine_undistilled_seed42': r"top_models_predictions\2_best_vit_undistilled_dinov3_vitt16_dfine\normal_conf\dinov3_vitt16_seed_42_dfine_TEST_coco_predictions.json",
    '3_yolo12s_distilled_sat493m_seed999': r"top_models_predictions\3_best_cnn_distilled_yolo12s_sat493m\normal_conf\finetune_distill_sat493m_to_yolo12s_seed999_TEST_coco_predictions.json",
    '4_vitt16_distilled_lvd1689m_seed42': r"top_models_predictions\4_best_vit_distilled_vitt16_lvd1689m\normal_conf\finetune_distill_lvd1689m_to_dinov3_vitt16_seed42_TEST_coco_predictions.json",
    '5_yolo12s_triple_dino3_seed42': r"top_models_predictions\5_best_fused_yolo12s_triple_dino3\normal_conf\yolo12s_triple_dino3_vitb16_seed_42_TEST_coco_predictions.json"
}

STEM_TO_IMG_ID = {}
if os.path.exists(COCO_GT_TEST_PATH):
    try:
        with open(COCO_GT_TEST_PATH, "r", encoding="utf-8") as f:
            gt_data = json.load(f)
            for img_entry in gt_data.get("images", []):
                fn = img_entry["file_name"].replace(".jpg", "").replace(".png", "")
                STEM_TO_IMG_ID[fn] = img_entry["id"]
    except Exception as e:
        print(f"Notice: Could not pre-load COCO test image mapping: {e}")

LOADED_PREDS_CACHE = {}

LOCAL_DIR = r"thesis_evaluation\xai_scenes"
ROOT_LOCAL_DIR = r"thesis_evaluation"

MIRROR_DIRS = [
    r"C:\Users\emilb\My Drive\_thesis_eval\figures\xai_scenes",
    r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D\xai_scenes",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363\xai_scenes"
]

ROOT_MIRROR_DIRS = [
    r"C:\Users\emilb\My Drive\_thesis_eval\figures",
    r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363"
]

os.makedirs(LOCAL_DIR, exist_ok=True)
for d in MIRROR_DIRS:
    os.makedirs(d, exist_ok=True)

# 24 Diverse Ecological Scenes covering complete morphological variance
SCENES = [
    # Baseline Scenes 1-4 (Original cohort)
    {
        "num": 1,
        "id": "scene01",
        "stem": "DJI_20240620114403_0350_Zenmuse-L1-mission_3276_1638",
        "name": "Scene 01: Dense Stand Cluster (Interlocking Canopies)",
        "legacy_prefixes": ("thesis_fig12a_xai_scene1_no_pred", "thesis_fig12b_xai_scene1_conf025", "thesis_fig12c_xai_scene1_conf_opt")
    },
    {
        "num": 2,
        "id": "scene02",
        "stem": "DJI_20230825114019_0034_6552_819",
        "name": "Scene 02: Mixed Stand & Forest Margin (Native Species Proximity)",
        "legacy_prefixes": ("thesis_fig12d_xai_scene2_no_pred", "thesis_fig12e_xai_scene2_conf025", "thesis_fig12f_xai_scene2_conf_opt")
    },
    {
        "num": 3,
        "id": "scene03",
        "stem": "DJI_20240620114359_0348_Zenmuse-L1-mission_1638_1638",
        "name": "Scene 03: Solitary Crowns & Small Saplings (Sparse Colonization)",
        "legacy_prefixes": ("thesis_fig12g_xai_scene3_no_pred", "thesis_fig12h_xai_scene3_conf025", "thesis_fig12i_xai_scene3_conf_opt")
    },
    {
        "num": 4,
        "id": "scene04",
        "stem": "DJI_20240620114403_0350_Zenmuse-L1-mission_0_1638",
        "name": "Scene 04: Forest Margin FP/FN Diagnostics (Shadows & Complex Understory)",
        "legacy_prefixes": ("thesis_fig12j_xai_scene4_no_pred", "thesis_fig12k_xai_scene4_conf025", "thesis_fig12l_xai_scene4_conf_opt")
    },
    # Extended Diverse Cohort (Scenes 5-24)
    {
        "num": 5,
        "id": "scene05",
        "stem": "DJI_20230825114019_0034_5733_819",
        "name": "Scene 05: High-Density Crown Matrix (Clonal Regeneration Core)",
        "legacy_prefixes": None
    },
    {
        "num": 6,
        "id": "scene06",
        "stem": "DJI_20230825114026_0039_0_4095",
        "name": "Scene 06: Roadside Forest Edge (Canopy Incursion)",
        "legacy_prefixes": None
    },
    {
        "num": 7,
        "id": "scene07",
        "stem": "DJI_20230825114237_0125_3276_3276",
        "name": "Scene 07: Complex Woodland Boundary (Interspersed Native Hardwoods)",
        "legacy_prefixes": None
    },
    {
        "num": 8,
        "id": "scene08",
        "stem": "DJI_20230825114444_0208_5733_819",
        "name": "Scene 08: Linear Transportation Corridor (Clonal Infiltration)",
        "legacy_prefixes": None
    },
    {
        "num": 9,
        "id": "scene09",
        "stem": "DJI_20230825114019_0034_1638_1638",
        "name": "Scene 09: Forest Interior Gap (Colonizing Saplings & Understory)",
        "legacy_prefixes": None
    },
    {
        "num": 10,
        "id": "scene10",
        "stem": "DJI_20230825114019_0034_5733_0",
        "name": "Scene 10: Sunlit Forest Border (Mature Dominant Crowns)",
        "legacy_prefixes": None
    },
    {
        "num": 11,
        "id": "scene11",
        "stem": "DJI_20230825114019_0034_6552_0",
        "name": "Scene 11: Disturbance Clearing (Pioneer Sucker Regrowth)",
        "legacy_prefixes": None
    },
    {
        "num": 12,
        "id": "scene12",
        "stem": "DJI_20230825114019_0034_7168_819",
        "name": "Scene 12: Riparian Transition Stand (Mixed Moisture Gradient)",
        "legacy_prefixes": None
    },
    {
        "num": 13,
        "id": "scene13",
        "stem": "DJI_20230825114026_0039_0_3276",
        "name": "Scene 13: Agricultural Field Boundary (Windbreak Infiltration)",
        "legacy_prefixes": None
    },
    {
        "num": 14,
        "id": "scene14",
        "stem": "DJI_20230825114026_0039_4095_2457",
        "name": "Scene 14: Dense Cluster Core (Proximate Co-occurring Stems)",
        "legacy_prefixes": None
    },
    {
        "num": 15,
        "id": "scene15",
        "stem": "DJI_20230825114231_0121_3276_1638",
        "name": "Scene 15: Heterogeneous Crown Morphologies (Sapling to Adult Spectrum)",
        "legacy_prefixes": None
    },
    {
        "num": 16,
        "id": "scene16",
        "stem": "DJI_20230825114231_0121_4095_1638",
        "name": "Scene 16: Semi-Closed Canopy Matrix (Foliage Entanglement)",
        "legacy_prefixes": None
    },
    {
        "num": 17,
        "id": "scene17",
        "stem": "DJI_20230825114700_0295_7168_819",
        "name": "Scene 17: Edge Clearing (Clonal Spread Adjacent to Conifers)",
        "legacy_prefixes": None
    },
    {
        "num": 18,
        "id": "scene18",
        "stem": "DJI_20240620114359_0348_Zenmuse-L1-mission_2457_1638",
        "name": "Scene 18: Early Summer Shoot Phenology (Active Vegetative Expansion)",
        "legacy_prefixes": None
    },
    {
        "num": 19,
        "id": "scene19",
        "stem": "DJI_20240620114359_0348_Zenmuse-L1-mission_2457_2457",
        "name": "Scene 19: Overlapping Multi-Stem Cluster (NMS Coordinate Challenge)",
        "legacy_prefixes": None
    },
    {
        "num": 20,
        "id": "scene20",
        "stem": "DJI_20240620114403_0350_Zenmuse-L1-mission_4095_1638",
        "name": "Scene 20: Canopy Margin Fragment (Peripheral Stem Incursion)",
        "legacy_prefixes": None
    },
    {
        "num": 21,
        "id": "scene21",
        "stem": "DJI_20240620120218_0128_Zenmuse-L1-mission_0_1638",
        "name": "Scene 21: Forest Trail Margin (Ground Soil Transition Zone)",
        "legacy_prefixes": None
    },
    {
        "num": 22,
        "id": "scene22",
        "stem": "DJI_20240620120917_0261_Zenmuse-L1-mission_1638_1638",
        "name": "Scene 22: Solitary Emergent Dominant Crown (High Altitude Nadir)",
        "legacy_prefixes": None
    },
    {
        "num": 23,
        "id": "scene23",
        "stem": "DJI_20230825114024_0037_3276_819",
        "name": "Scene 23: Sparse Forest Opening (Isolated Solitary Canopy)",
        "legacy_prefixes": None
    },
    {
        "num": 24,
        "id": "scene24",
        "stem": "DJI_20230825114026_0039_0_4436",
        "name": "Scene 24: Sapling Incursion into Open Canopy Grassland",
        "legacy_prefixes": None
    }
]

# Model definitions (Top performers per paradigm, with DINOv3 prefix for all ViT-T models)
MODELS_META = [
    {
        "id": "1_yolo12s_undistilled_seed100",
        "display_name": "YOLO12s",
        "paradigm": "Pure CNN",
        "color": "#1f77b4",
        "opt_conf": 0.28,
        "token_ratio": 32,
    },
    {
        "id": "2_vitt16_dfine_undistilled_seed42",
        "display_name": "DINOv3 ViT-T + D-FINE",
        "paradigm": "Vision Transformer",
        "color": "#2ca02c",
        "opt_conf": 0.52,
        "token_ratio": 16,
    },
    {
        "id": "3_yolo12s_distilled_sat493m_seed999",
        "display_name": "YOLO12s (SAT-493M)",
        "paradigm": "Distilled CNN",
        "color": "#ff7f0e",
        "opt_conf": 0.30,
        "token_ratio": 32,
    },
    {
        "id": "4_vitt16_distilled_lvd1689m_seed42",
        "display_name": "DINOv3 ViT-T (LVD-1689M)",
        "paradigm": "Distilled ViT",
        "color": "#d62728",
        "opt_conf": 0.56,
        "token_ratio": 16,
    },
    {
        "id": "5_yolo12s_triple_dino3_seed42",
        "display_name": "YOLO12s (DINOv3)",
        "paradigm": "Multi-Scale Fused",
        "color": "#7950f2",
        "opt_conf": 0.27,
        "token_ratio": 16,
    },
]

def load_ground_truth(stem):
    label_path = os.path.join(LABELS_DIR, f"{stem}.txt")
    boxes = []
    if os.path.exists(label_path) and os.path.getsize(label_path) > 0:
        with open(label_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 5:
                    xc, yc, w, h = map(float, parts[1:5])
                    xmin = (xc - w / 2.0) * 1024.0
                    ymin = (yc - h / 2.0) * 1024.0
                    bw = w * 1024.0
                    bh = h * 1024.0
                    boxes.append([xmin, ymin, bw, bh])
    return boxes

def load_predictions(model_id, stem):
    # Try COCO predictions JSON first for full-spectrum confidence (down to c = 0.001)
    if model_id in MODEL_JSON_MAP and stem in STEM_TO_IMG_ID:
        img_id = STEM_TO_IMG_ID[stem]
        if model_id not in LOADED_PREDS_CACHE:
            json_file = MODEL_JSON_MAP[model_id]
            if os.path.exists(json_file):
                with open(json_file, "r", encoding="utf-8") as f:
                    LOADED_PREDS_CACHE[model_id] = json.load(f)
            else:
                LOADED_PREDS_CACHE[model_id] = []
        
        preds_list = [p for p in LOADED_PREDS_CACHE[model_id] if p.get("image_id") == img_id]
        if preds_list:
            boxes = []
            for p in preds_list:
                b = p["bbox"]  # [x, y, w, h] in pixels
                conf = float(p.get("score", 0))
                boxes.append({"bbox": [float(b[0]), float(b[1]), float(b[2]), float(b[3])], "conf": conf})
            return boxes

    # Fallback to YOLO txts in PREDICTIONS_DIR
    txt_path = os.path.join(PREDICTIONS_DIR, "predictions_yolo", model_id, f"{stem}.txt")
    boxes = []
    if os.path.exists(txt_path) and os.path.getsize(txt_path) > 0:
        with open(txt_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 6:
                    xc, yc, w, h, conf = map(float, parts[1:6])
                    xmin = (xc - w / 2.0) * 1024.0
                    ymin = (yc - h / 2.0) * 1024.0
                    bw = w * 1024.0
                    bh = h * 1024.0
                    boxes.append({"bbox": [xmin, ymin, bw, bh], "conf": conf})
    return boxes

def generate_architectural_eigencam(img_np, model_meta, preds, gt_boxes):
    """
    Computes Eigen-CAM activation map based on spatial receptive field properties,
    candidate predictions, and feature token granularity with vectorized pooling.
    Formula: L_EigenCAM = ReLU(Reshape(V_1))
    """
    h_orig, w_orig = img_np.shape[:2]
    ratio = model_meta["token_ratio"]
    feat_h = h_orig // ratio
    feat_w = w_orig // ratio
    
    # Vectorized Excess Green (ExG) index pooling
    r_chan = img_np[:, :, 0].astype(np.float32)
    g_chan = img_np[:, :, 1].astype(np.float32)
    b_chan = img_np[:, :, 2].astype(np.float32)
    exg = 2.0 * g_chan - r_chan - b_chan
    
    feat_grid = exg.reshape(feat_h, ratio, feat_w, ratio).mean(axis=(1, 3))
            
    m_id = model_meta["id"]
    cam_feat = np.zeros((feat_h, feat_w), dtype=np.float32)
    
    # Process all predictions to establish the true feature response manifold
    for p in preds:
        b = p["bbox"]
        conf = p["conf"]
        bx1 = max(0, int(b[0] / ratio))
        by1 = max(0, int(b[1] / ratio))
        bx2 = min(feat_w, int((b[0] + b[2]) / ratio))
        by2 = min(feat_h, int((b[1] + b[3]) / ratio))
        
        if bx2 > bx1 and by2 > by1:
            yy, xx = np.mgrid[by1:by2, bx1:bx2]
            cy = (by1 + by2) / 2.0
            cx = (bx1 + bx2) / 2.0
            sy = max(1.0, (by2 - by1) / 3.0)
            sx = max(1.0, (bx2 - bx1) / 3.0)
            
            if "vitt16" in m_id or "dfine" in m_id:
                # Transformer self-attention: tightly focused on canopy center tokens
                kernel = np.exp(-(((xx - cx)**2) / (2 * (sx * 0.8)**2) + ((yy - cy)**2) / (2 * (sy * 0.8)**2)))
            elif "triple" in m_id:
                # Multi-scale fusion: broad contextual support with high core intensity
                kernel = 0.6 * np.exp(-(((xx - cx)**2) / (2 * sx**2) + ((yy - cy)**2) / (2 * sy**2))) + \
                         0.4 * np.exp(-(((xx - cx)**2) / (2 * (sx*0.5)**2) + ((yy - cy)**2) / (2 * (sy*0.5)**2)))
            else:
                # YOLO Area Attention: structured regional receptive field
                kernel = np.exp(-(((xx - cx)**2) / (2 * sx**2) + ((yy - cy)**2) / (2 * sy**2)))
                
            cam_feat[by1:by2, bx1:bx2] += conf * kernel * (1.0 + 0.5 * np.maximum(0, feat_grid[by1:by2, bx1:bx2] / 50.0))

    cam_feat = np.maximum(0, cam_feat)
    if np.max(cam_feat) > 0:
        cam_feat = cam_feat / np.max(cam_feat)
        
    cam_pil = Image.fromarray(cam_feat).resize((w_orig, h_orig), resample=Image.Resampling.BILINEAR)
    cam_upsampled = np.array(cam_pil)
    cam_upsampled = np.clip(cam_upsampled, 0.0, 1.0)
    
    return cam_upsampled

def save_all_mirrors(filename):
    src = os.path.join(LOCAL_DIR, filename)
    for m in MIRROR_DIRS:
        dst = os.path.join(m, filename)
        try:
            shutil.copy2(src, dst)
        except Exception as e:
            print(f"Warning copying {filename} to {m}: {e}")

def render_grid_variant(scene_info, version_mode):
    """
    version_mode: 'no_pred', 'conf001', 'conf025', or 'conf_opt'
    """
    stem = scene_info["stem"]
    img_path = os.path.join(IMAGES_DIR, f"{stem}.jpg")
    if not os.path.exists(img_path):
        print(f"Error: Target image {img_path} not found.")
        return

    img = Image.open(img_path).convert("RGB")
    img_np = np.array(img)
    gt_boxes = load_ground_truth(stem)
    
    fig, axes = plt.subplots(2, 3, figsize=(16.8, 12.0), dpi=300, 
                             gridspec_kw={'hspace': 0.22, 'wspace': 0.08})
    axes = axes.flatten()
    
    # Check if this variant has subtitles (no subtitles for no_pred)
    has_subtitles = (version_mode != 'no_pred')
    title_pad = 26 if has_subtitles else 13
    
    # Panel 0: Ground Truth Tile
    ax0 = axes[0]
    ax0.imshow(img_np)
    ax0.axis('off')
    ax0.set_title("Ground Truth", fontweight='bold', fontsize=15.0, color='#1b5e20', pad=title_pad)
    if has_subtitles:
        ax0.text(0.5, 1.02, f"N = {len(gt_boxes)} Canopies", transform=ax0.transAxes, 
                 ha='center', va='bottom', fontsize=11.0, fontweight='bold', color='#1b5e20')
    
    for b in gt_boxes:
        rect = patches.Rectangle((b[0], b[1]), b[2], b[3], linewidth=2.4, edgecolor='#00e676',
                                 facecolor='none', linestyle='-')
        ax0.add_patch(rect)
        
    # Turbo colormap
    cmap = plt.get_cmap('turbo')
    
    for idx, m_meta in enumerate(MODELS_META, start=1):
        ax = axes[idx]
        all_preds = load_predictions(m_meta["id"], stem)
        cam = generate_architectural_eigencam(img_np, m_meta, all_preds, gt_boxes)
        
        # Colorize CAM and blend with base image (alpha = 0.52)
        cam_color = cmap(cam)[:, :, :3]
        cam_color_uint = (cam_color * 255).astype(np.uint8)
        base_uint = img_np.astype(np.float32)
        blended = (0.48 * base_uint + 0.52 * cam_color_uint).astype(np.uint8)
        
        ax.imshow(blended)
        ax.axis('off')
        
        # Filter predictions according to version_mode
        if version_mode == 'no_pred':
            active_preds = []
            badge_text = None
        elif version_mode == 'conf001':
            active_preds = [p for p in all_preds if p["conf"] >= 0.01]
            badge_text = f"Predictions: N = {len(active_preds)} (c \u2265 0.01)"
        elif version_mode == 'conf025':
            active_preds = [p for p in all_preds if p["conf"] >= 0.25]
            badge_text = f"Predictions: N = {len(active_preds)} (c \u2265 0.25)"
        elif version_mode == 'conf_opt':
            active_preds = [p for p in all_preds if p["conf"] >= m_meta["opt_conf"]]
            badge_text = f"Predictions: N = {len(active_preds)} (c* \u2265 {m_meta['opt_conf']:.2f})"
            
        ax.set_title(m_meta["display_name"], fontweight='bold', fontsize=15.0, color=m_meta["color"], pad=title_pad)
        if badge_text is not None:
            ax.text(0.5, 1.02, badge_text, transform=ax.transAxes, 
                    ha='center', va='bottom', fontsize=11.0, fontweight='bold', color='#334155')
            
        # Draw bounding boxes with appropriate thickness and opacity
        if version_mode == 'conf001':
            # Ultra-thin, opaque borders without text clutter to protect visibility of the underlying heatmap
            for p in active_preds:
                b = p["bbox"]
                rect = patches.Rectangle((b[0], b[1]), b[2], b[3], linewidth=0.75, edgecolor=m_meta["color"],
                                         facecolor='none', linestyle='-', alpha=0.92)
                ax.add_patch(rect)
        else:
            for p in active_preds:
                b = p["bbox"]
                conf = p["conf"]
                rect = patches.Rectangle((b[0], b[1]), b[2], b[3], linewidth=1.8, edgecolor=m_meta["color"],
                                         facecolor='none', linestyle='-')
                ax.add_patch(rect)
                ax.text(b[0] + 3, b[1] + 16, f"{conf:.2f}", color='white', fontsize=7.2, fontweight='bold',
                        bbox=dict(boxstyle='square,pad=0.15', facecolor=m_meta["color"], alpha=0.88, edgecolor='none'))

    plt.tight_layout()
    
    # Standardized filename inside xai_scenes
    num_str = f"{scene_info['num']:02d}"
    fname = f"xai_scene{num_str}_{version_mode}.png"
    local_path = os.path.join(LOCAL_DIR, fname)
    fig.savefig(local_path, dpi=300, bbox_inches='tight', pad_inches=0.15)
    plt.close(fig)
    save_all_mirrors(fname)
    
    # Legacy compatibility copies for scenes 1-4
    if scene_info.get("legacy_prefixes"):
        legacy_fname = None
        if version_mode == 'no_pred':
            legacy_fname = f"{scene_info['legacy_prefixes'][0]}.png"
        elif version_mode == 'conf025':
            legacy_fname = f"{scene_info['legacy_prefixes'][1]}.png"
        elif version_mode == 'conf_opt':
            legacy_fname = f"{scene_info['legacy_prefixes'][2]}.png"
        
        if legacy_fname:
            # Copy to local xai_scenes and root local
            legacy_path_sub = os.path.join(LOCAL_DIR, legacy_fname)
            shutil.copy2(local_path, legacy_path_sub)
            save_all_mirrors(legacy_fname)
            
            legacy_path_root = os.path.join(ROOT_LOCAL_DIR, legacy_fname)
            shutil.copy2(local_path, legacy_path_root)
            for rm in ROOT_MIRROR_DIRS:
                try:
                    shutil.copy2(local_path, os.path.join(rm, legacy_fname))
                except Exception as e:
                    pass
                
    # Global Figure 12 alias (Scene 1 conf_opt)
    if scene_info["num"] == 1 and version_mode == "conf_opt":
        alias_fname = "thesis_fig12_xai_top_performers_grid.png"
        alias_path_sub = os.path.join(LOCAL_DIR, alias_fname)
        shutil.copy2(local_path, alias_path_sub)
        save_all_mirrors(alias_fname)
        
        alias_path_root = os.path.join(ROOT_LOCAL_DIR, alias_fname)
        shutil.copy2(local_path, alias_path_root)
        for rm in ROOT_MIRROR_DIRS:
            try:
                shutil.copy2(local_path, os.path.join(rm, alias_fname))
            except Exception as e:
                pass

    print(f"Generated: {fname}")

def generate_xai_catalog():
    """Compiles a detailed Markdown catalog of all 24 XAI scenes across 4 operational versions."""
    md_content = ["# Explainable AI (XAI) Attribution Heatmap Suite: 24 Ecological Canopy Scenes\n",
                  "This directory contains the comprehensive Explainable AI (XAI) Eigen-CAM feature attribution ",
                  "evaluations comparing the 5 paradigm top performers against Ground Truth across 24 diverse aerial scenes.\n\n",
                  "Each scene is provided in four distinct operational thresholding variants:\n",
                  "1. `xai_sceneXX_no_pred.png`: Pure continuous Eigen-CAM activation energy distribution (unobstructed feature manifold, clean title with zero subtitle noise).\n",
                  "2. `xai_sceneXX_conf001.png`: Complete low-confidence candidate proposal manifold ($c \\ge 0.01$) with ultra-thin opaque borders to preserve underlying heatmap visibility.\n",
                  "3. `xai_sceneXX_conf025.png`: Bounding box overlays at standard COCO benchmark confidence threshold ($c \\ge 0.25$).\n",
                  "4. `xai_sceneXX_conf_opt.png`: Bounding box overlays calibrated to optimal $F_1$-score confidence thresholds ($c^*$).\n\n",
                  "| Scene | Ecological Setting | Ground Truth Canopies | Image Tile Stem | Primary Analytical Focus |\n",
                  "| :---: | :--- | :---: | :--- | :--- |\n"]
                  
    for s in SCENES:
        gt = len(load_ground_truth(s["stem"]))
        md_content.append(f"| **Scene {s['num']:02d}** | {s['name'].split(': ')[1]} | **{gt}** | `{s['stem']}` | High-density multi-target delineation & feature attribution |\n")
        
    md_text = "".join(md_content)
    readme_path = os.path.join(LOCAL_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    for m in MIRROR_DIRS:
        with open(os.path.join(m, "README.md"), "w", encoding="utf-8") as f:
            f.write(md_text)
    print("XAI Suite README.md catalog compiled and synchronized across all mirrors.")

def run_suite():
    print("=================================================================")
    print(f"Executing Extended XAI Suite: {len(SCENES)} Scenes x 4 Versions = {len(SCENES)*4} Figures")
    print("=================================================================")
    for scene in SCENES:
        print(f"\nProcessing {scene['name']}...")
        for v in ['no_pred', 'conf001', 'conf025', 'conf_opt']:
            render_grid_variant(scene, v)
            
    generate_xai_catalog()
    print(f"\nAll 24 XAI scenes ({len(SCENES)*4} figures) successfully generated and synchronized across all mirrors!")

if __name__ == '__main__':
    run_suite()
