"""
Generate 105 Publication-Grade Explainable AI (XAI) Attribution Heatmap Grids
for Top-Performing Canopy Detection Architectures across all Paradigms.

Layout:
- Panel 0: Ground Truth Tile (N = X Canopies, Emerald Green bounding boxes)
- Panel 1: YOLO12s (Pure CNN, Blue)
- Panel 2: DINOv3 ViT-T + D-FINE (Vision Transformer, Green)
- Panel 3: YOLO12s (SAT-493M) (Distilled CNN, Orange)
- Panel 4: DINOv3 ViT-T (LVD-1689M) (Distilled ViT, Red)
- Panel 5: YOLO12s (DINOv3) (Multi-Scale Fused, Purple)

Covers 105 diverse scenes with extensive representation of:
- Open Meadow & Grassland
- Dirt Tracks, Paths & Bare Soil
- Agricultural Field Margins & Boundary Clearings
- Native Background Stands (Zero Ailanthus)
- Solitary Crowns & Small Saplings
- Dense Clustered Stands
"""

import os
import sys
import json
import shutil
from pathlib import Path
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Ensure UTF-8 line buffering
sys.stdout.reconfigure(line_buffering=True)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Add current dir and DINOV3 repo to sys.path
THIS_DIR = Path(__file__).resolve().parent
DINO_REPO = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(DINO_REPO) not in sys.path:
    sys.path.insert(0, str(DINO_REPO))

# Import base components from generate_xai_heatmaps
from generate_xai_heatmaps import (
    SCENES as CANONICAL_24_SCENES,
    MODELS_META,
    generate_architectural_eigencam,
    load_predictions,
    STEM_TO_IMG_ID,
    LOADED_PREDS_CACHE,
    LOCAL_DIR as BASE_LOCAL_DIR,
    MIRROR_DIRS as BASE_MIRROR_DIRS,
)

# Output directories
XAI_OUTPUT_DINO = DINO_REPO / "thesis_evaluation" / "xai_scenes"
XAI_OUTPUT_PLOTTER = Path(r"C:\Users\emilb\Documents\GitHub\_trainer_pred_plotter\results\figures\xai_scenes")
XAI_OUTPUT_LIGHTLY = Path(r"C:\Users\emilb\Documents\GitHub\_trainer_lightly\thesis_evaluation\xai_scenes")
XAI_OUTPUT_DINO.mkdir(parents=True, exist_ok=True)
XAI_OUTPUT_PLOTTER.mkdir(parents=True, exist_ok=True)
XAI_OUTPUT_LIGHTLY.mkdir(parents=True, exist_ok=True)

# Image & Label source directories (check E: then C:)
IMAGE_DIRS = [
    Path(r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"),
    Path(r"C:\Users\emilb\Documents\GitHub\_data\sliced_split_dataset\test\images"),
]
LABEL_DIRS = [
    Path(r"E:\Götterbaum\_export_data\testset_unlabeled_combined\labels"),
    Path(r"C:\Users\emilb\Documents\GitHub\_data\sliced_split_dataset\test\labels"),
]

INDEX_CSV = Path(r"C:\Users\emilb\Documents\GitHub\_trainer_pred_plotter\results\figures\test_prediction_slices\yolo12s\yolo12s_test_slice_evaluation_index.csv")


def find_image_path(stem: str) -> Path:
    for d in IMAGE_DIRS:
        p = d / f"{stem}.jpg"
        if p.exists():
            return p
        p_png = d / f"{stem}.png"
        if p_png.exists():
            return p_png
    raise FileNotFoundError(f"Image not found for stem: {stem}")


def find_label_path(stem: str) -> Path:
    for d in LABEL_DIRS:
        p = d / f"{stem}.txt"
        if p.exists():
            return p
    return None


def load_gt_boxes_robust(stem: str) -> list:
    lbl_p = find_label_path(stem)
    boxes = []
    if lbl_p and lbl_p.exists() and lbl_p.stat().st_size > 0:
        with open(lbl_p, "r", encoding="utf-8") as f:
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


def build_105_scenes():
    scenes = []
    existing_stems = set()

    # 1. First 24 canonical scenes
    for s in CANONICAL_24_SCENES:
        scenes.append({
            "num": s["num"],
            "id": s["id"],
            "stem": s["stem"],
            "name": s["name"],
            "category": "Canonical Thesis Benchmark",
        })
        existing_stems.add(s["stem"])

    # 2. Curate 81 new scenes from test set
    df = pd.read_csv(INDEX_CSV)
    records = []
    for _, row in df.iterrows():
        fn = row["slice_filename"]
        stem = fn.replace(".jpg", "")
        if stem in existing_stems:
            continue
        try:
            img_p = find_image_path(stem)
        except FileNotFoundError:
            continue

        img = cv2.imread(str(img_p))
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        b, g, r = img[:, :, 0].astype(float), img[:, :, 1].astype(float), img[:, :, 2].astype(float)
        exg = float(np.mean(2 * g - r - b))
        val = float(np.mean(gray))
        sat = float(np.mean(hsv[:, :, 1]))
        open_ratio = float(((hsv[:, :, 1] < 65) | (gray > 130)).mean())
        lap_var = float(cv2.Laplacian(gray, cv2.CV_64F).var())

        records.append({
            "stem": stem,
            "fn": fn,
            "gt_count": int(row["gt_count"]),
            "tp_count": int(row["tp_count"]),
            "is_tn": bool(row["is_tn_slice"]),
            "val": val,
            "sat": sat,
            "exg": exg,
            "open_ratio": open_ratio,
            "lap_var": lap_var,
        })

    used = set(existing_stems)

    # Category A: Open Meadow & Grassland (20 scenes)
    c_meadow = [r for r in records if r["is_tn"] and r["open_ratio"] > 0.60 and r["stem"] not in used]
    c_meadow.sort(key=lambda x: x["open_ratio"], reverse=True)
    sel_meadow = c_meadow[:20]
    for r in sel_meadow:
        r["cat_name"] = "Open Meadow & Grassland"
        used.add(r["stem"])

    # Category B: Dirt Tracks, Paths & Bare Soil (15 scenes)
    c_tracks = [r for r in records if r["is_tn"] and r["stem"] not in used]
    c_tracks.sort(key=lambda x: x["sat"])
    sel_tracks = c_tracks[:15]
    for r in sel_tracks:
        r["cat_name"] = "Dirt Tracks, Paths & Bare Soil"
        used.add(r["stem"])

    # Category C: Agricultural Field Margins (15 scenes)
    c_fields = [r for r in records if r["open_ratio"] > 0.40 and r["stem"] not in used]
    c_fields.sort(key=lambda x: x["open_ratio"], reverse=True)
    sel_fields = c_fields[:15]
    for r in sel_fields:
        r["cat_name"] = "Agricultural Field Margins & Boundary Clearings"
        used.add(r["stem"])

    # Category D: Native Background Stands (15 scenes)
    c_native = [r for r in records if r["is_tn"] and r["stem"] not in used]
    c_native.sort(key=lambda x: x["lap_var"], reverse=True)
    sel_native = c_native[:15]
    for r in sel_native:
        r["cat_name"] = "Native Background Stand (Zero Ailanthus)"
        used.add(r["stem"])

    # Category E: Solitary Crowns & Small Saplings (8 scenes)
    c_solitary = [r for r in records if r["gt_count"] == 1 and r["tp_count"] >= 1 and r["stem"] not in used]
    c_solitary.sort(key=lambda x: x["lap_var"], reverse=True)
    sel_solitary = c_solitary[:8]
    for r in sel_solitary:
        r["cat_name"] = "Solitary Crowns & Small Saplings"
        used.add(r["stem"])

    # Category F: Dense Clustered Stands (8 scenes)
    c_dense = [r for r in records if r["gt_count"] >= 2 and r["tp_count"] >= 1 and r["stem"] not in used]
    c_dense.sort(key=lambda x: (x["gt_count"], x["tp_count"]), reverse=True)
    sel_dense = c_dense[:8]
    for r in sel_dense:
        r["cat_name"] = "Dense Clustered Stands"
        used.add(r["stem"])

    new_cohort = sel_meadow + sel_tracks + sel_fields + sel_native + sel_solitary + sel_dense

    curr_num = 25
    for item in new_cohort:
        scenes.append({
            "num": curr_num,
            "id": f"scene{curr_num:02d}",
            "stem": item["stem"],
            "name": f"Scene {curr_num:02d}: {item['cat_name']}",
            "category": item["cat_name"],
        })
        curr_num += 1

    print(f"Total compiled scene suite: {len(scenes)} scenes.")
    return scenes


def render_scene_grid(scene_info, version_mode="conf_opt"):
    stem = scene_info["stem"]
    try:
        img_path = find_image_path(stem)
    except FileNotFoundError:
        print(f"Error: Target image {stem} not found.")
        return None

    img = Image.open(img_path).convert("RGB")
    img_np = np.array(img)
    gt_boxes = load_gt_boxes_robust(stem)

    fig, axes = plt.subplots(2, 3, figsize=(16.8, 12.0), dpi=300,
                             gridspec_kw={'hspace': 0.22, 'wspace': 0.08})
    axes = axes.flatten()

    has_subtitles = (version_mode != "no_pred")
    title_pad = 26 if has_subtitles else 13

    # Panel 0: Ground Truth Tile
    ax0 = axes[0]
    ax0.imshow(img_np)
    ax0.axis("off")
    ax0.set_title("Ground Truth", fontweight="bold", fontsize=15.0, color="#1b5e20", pad=title_pad)
    if has_subtitles:
        ax0.text(0.5, 1.02, f"N = {len(gt_boxes)} Canopies", transform=ax0.transAxes,
                 ha="center", va="bottom", fontsize=11.0, fontweight="bold", color="#1b5e20")

    for b in gt_boxes:
        rect = patches.Rectangle((b[0], b[1]), b[2], b[3], linewidth=2.4, edgecolor="#00e676",
                                 facecolor="none", linestyle="-")
        ax0.add_patch(rect)

    cmap = plt.get_cmap("turbo")

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
        ax.axis("off")

        if version_mode == "no_pred":
            active_preds = []
            badge_text = None
        elif version_mode == "conf001":
            active_preds = [p for p in all_preds if p["conf"] >= 0.01]
            badge_text = f"Predictions: N = {len(active_preds)} (c \u2265 0.01)"
        elif version_mode == "conf025":
            active_preds = [p for p in all_preds if p["conf"] >= 0.25]
            badge_text = f"Predictions: N = {len(active_preds)} (c \u2265 0.25)"
        elif version_mode == "conf_opt":
            active_preds = [p for p in all_preds if p["conf"] >= m_meta["opt_conf"]]
            badge_text = f"Predictions: N = {len(active_preds)} (c* \u2265 {m_meta['opt_conf']:.2f})"

        ax.set_title(m_meta["display_name"], fontweight="bold", fontsize=15.0, color=m_meta["color"], pad=title_pad)
        if badge_text is not None:
            ax.text(0.5, 1.02, badge_text, transform=ax.transAxes,
                    ha="center", va="bottom", fontsize=11.0, fontweight="bold", color="#334155")

        for p in active_preds:
            b = p["bbox"]
            conf = p["conf"]
            rect = patches.Rectangle((b[0], b[1]), b[2], b[3], linewidth=1.8, edgecolor=m_meta["color"],
                                     facecolor="none", linestyle="-")
            ax.add_patch(rect)
            ax.text(b[0] + 3, b[1] + 16, f"{conf:.2f}", color="white", fontsize=7.2, fontweight="bold",
                    bbox=dict(boxstyle="square,pad=0.15", facecolor=m_meta["color"], alpha=0.88, edgecolor="none"))

    plt.tight_layout()

    num_str = f"{scene_info['num']:02d}" if isinstance(scene_info['num'], int) else str(scene_info['num'])
    fname = f"xai_scene{num_str}_{version_mode}.png"
    out_dino = XAI_OUTPUT_DINO / fname
    out_plotter = XAI_OUTPUT_PLOTTER / fname
    out_lightly = XAI_OUTPUT_LIGHTLY / fname

    fig.savefig(str(out_dino), dpi=300, bbox_inches="tight", pad_inches=0.15)
    if XAI_OUTPUT_PLOTTER.exists():
        fig.savefig(str(out_plotter), dpi=300, bbox_inches="tight", pad_inches=0.15)
    if XAI_OUTPUT_LIGHTLY.exists():
        fig.savefig(str(out_lightly), dpi=300, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)

    # Also sync to mirror dirs if present
    for md in BASE_MIRROR_DIRS:
        if os.path.exists(md):
            try:
                shutil.copy2(str(out_dino), os.path.join(md, fname))
            except Exception:
                pass

    return fname


def main():
    print("=" * 80)
    print("EXPLAINABLE AI (XAI) TOP PARADIGMS GRID SUITE — 105 SCENES")
    print("=" * 80)

    scenes = build_105_scenes()
    manifest_rows = []

    print(f"\nRendering {len(scenes)} scenes in 6-panel paradigm comparison layout...")
    for s in scenes:
        fname = render_scene_grid(s, version_mode="conf_opt")
        if fname:
            gt_boxes = load_gt_boxes_robust(s["stem"])
            manifest_rows.append({
                "scene_num": s["num"],
                "scene_id": s["id"],
                "stem": s["stem"],
                "name": s["name"],
                "category": s["category"],
                "gt_count": len(gt_boxes),
                "filename": fname,
                "dino_path": str(XAI_OUTPUT_DINO / fname),
                "plotter_path": str(XAI_OUTPUT_PLOTTER / fname),
                "lightly_path": str(XAI_OUTPUT_LIGHTLY / fname),
            })
            if s["num"] % 10 == 0 or s["num"] == len(scenes):
                print(f"  Completed Scene {s['num']:02d}/{len(scenes)}: {s['name']}")

    manifest_df = pd.DataFrame(manifest_rows)
    manifest_csv = XAI_OUTPUT_PLOTTER / "xai_105_scenes_manifest.csv"
    manifest_df.to_csv(manifest_csv, index=False)
    manifest_df.to_csv(XAI_OUTPUT_DINO / "xai_105_scenes_manifest.csv", index=False)
    if XAI_OUTPUT_LIGHTLY.exists():
        manifest_df.to_csv(XAI_OUTPUT_LIGHTLY / "xai_105_scenes_manifest.csv", index=False)

    print("\n" + "=" * 80)
    print(f"ALL {len(scenes)} XAI SCENES SUCCESSFULLY GENERATED AT 300 DPI!")
    print(f"DINOv3-YOLOv12 Directory: {XAI_OUTPUT_DINO}")
    print(f"Pred Plotter Directory:  {XAI_OUTPUT_PLOTTER}")
    print(f"Lightly Directory:       {XAI_OUTPUT_LIGHTLY}")
    print(f"Manifest CSV:            {manifest_csv}")
    print("=" * 80)


if __name__ == "__main__":
    main()
