# Master Evaluation Compiler & Publication Figure Generator for testset_unlabeled_combined
# Compiles metrics, confusion statistics, comparison tables, and figures across 15 models
# Supports both Standard Confidence (c=0.25) and Calibrated Optimal F1 Confidence (c*) regimes

import os
import sys
import json
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

sys.stdout.reconfigure(line_buffering=True)

# Configuration
BASE_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"
IMAGES_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"
LABELS_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined\labels"

MIRROR_DIRS = [
    BASE_DIR,
    r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\thesis_evaluation",
    r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363",
]

# Publication Styling
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 10.5,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10.5,
    'axes.labelweight': 'bold',
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'legend.fontsize': 9.5,
    'figure.titlesize': 13.5,
    'figure.titleweight': 'bold',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.35,
    'grid.linestyle': '--'
})

MODEL_SPECS = [
    # 1. Pure CNN (Undistilled)
    {"id": "1_yolo12s_undistilled_seed42", "paradigm": "Pure CNN (Undistilled)", "arch": "YOLO12s", "seed": 42, "color": "#1f77b4", "opt_conf": 0.3283},
    {"id": "1_yolo12s_undistilled_seed100", "paradigm": "Pure CNN (Undistilled)", "arch": "YOLO12s", "seed": 100, "color": "#1f77b4", "opt_conf": 0.2482},
    {"id": "1_yolo12s_undistilled_seed999", "paradigm": "Pure CNN (Undistilled)", "arch": "YOLO12s", "seed": 999, "color": "#1f77b4", "opt_conf": 0.3013},
    
    # 2. Vision Transformer
    {"id": "2_vitt16_dfine_undistilled_seed42", "paradigm": "Vision Transformer", "arch": "ViT-T16 + D-FINE", "seed": 42, "color": "#2ca02c", "opt_conf": 0.5200},
    {"id": "2_vitt16_dfine_undistilled_seed100", "paradigm": "Vision Transformer", "arch": "ViT-T16 + D-FINE", "seed": 100, "color": "#2ca02c", "opt_conf": 0.5200},
    {"id": "2_vitt16_dfine_undistilled_seed999", "paradigm": "Vision Transformer", "arch": "ViT-T16 + D-FINE", "seed": 999, "color": "#2ca02c", "opt_conf": 0.5200},
    
    # 3. Distilled CNN
    {"id": "3_yolo12s_distilled_sat493m_seed42", "paradigm": "Distilled CNN", "arch": "YOLO12s (SAT-493M)", "seed": 42, "color": "#ff7f0e", "opt_conf": 0.2673},
    {"id": "3_yolo12s_distilled_sat493m_seed100", "paradigm": "Distilled CNN", "arch": "YOLO12s (SAT-493M)", "seed": 100, "color": "#ff7f0e", "opt_conf": 0.3493},
    {"id": "3_yolo12s_distilled_sat493m_seed999", "paradigm": "Distilled CNN", "arch": "YOLO12s (SAT-493M)", "seed": 999, "color": "#ff7f0e", "opt_conf": 0.2973},
    
    # 4. Distilled ViT
    {"id": "4_vitt16_distilled_lvd1689m_seed42", "paradigm": "Distilled ViT", "arch": "ViT-T16 (LVD-1689M)", "seed": 42, "color": "#d62728", "opt_conf": 0.5650},
    {"id": "4_vitt16_distilled_lvd1689m_seed100", "paradigm": "Distilled ViT", "arch": "ViT-T16 (LVD-1689M)", "seed": 100, "color": "#d62728", "opt_conf": 0.5600},
    {"id": "4_vitt16_distilled_lvd1689m_seed999", "paradigm": "Distilled ViT", "arch": "ViT-T16 (LVD-1689M)", "seed": 999, "color": "#d62728", "opt_conf": 0.5700},
    
    # 5. Multi-Scale Fused
    {"id": "5_yolo12s_triple_dino3_seed42", "paradigm": "Multi-Scale Fused", "arch": "YOLO12s Triple DINOv3", "seed": 42, "color": "#9467bd", "opt_conf": 0.2730},
    {"id": "5_yolo12s_triple_dino3_seed100", "paradigm": "Multi-Scale Fused", "arch": "YOLO12s Triple DINOv3", "seed": 100, "color": "#9467bd", "opt_conf": 0.2730},
    {"id": "5_yolo12s_triple_dino3_seed999", "paradigm": "Multi-Scale Fused", "arch": "YOLO12s Triple DINOv3", "seed": 999, "color": "#9467bd", "opt_conf": 0.3030},
]

def load_ground_truth():
    gt_map = {}
    label_files = glob.glob(os.path.join(LABELS_DIR, "*.txt"))
    for lf in label_files:
        stem = os.path.splitext(os.path.basename(lf))[0]
        boxes = []
        if os.path.getsize(lf) > 0:
            with open(lf, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 5:
                        cls_id = int(parts[0])
                        xc, yc, w, h = map(float, parts[1:5])
                        boxes.append({"cls": cls_id, "xc": xc, "yc": yc, "w": w, "h": h})
        gt_map[stem] = boxes
    return gt_map

def compute_iou(box1, box2):
    b1_x1, b1_y1, b1_x2, b1_y2 = box1
    b2_x1, b2_y1, b2_x2, b2_y2 = box2
    inter_x1 = max(b1_x1, b2_x1)
    inter_y1 = max(b1_y1, b2_y1)
    inter_x2 = min(b1_x2, b2_x2)
    inter_y2 = min(b1_y2, b2_y2)
    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
    b1_area = (b1_x2 - b1_x1) * (b1_y2 - b1_y1)
    b2_area = (b2_x2 - b2_x1) * (b2_y2 - b2_y1)
    union_area = b1_area + b2_area - inter_area
    return inter_area / union_area if union_area > 0 else 0.0

def evaluate_predictions_from_json(gt_map, json_path, model_spec, conf_mode="standard", conf_val=0.25):
    if not os.path.exists(json_path):
        return None
        
    with open(json_path, "r", encoding="utf-8") as f:
        preds = json.load(f)
        
    preds_by_img = {}
    scores = []
    for p in preds:
        stem = os.path.splitext(p["file_name"])[0]
        preds_by_img.setdefault(stem, []).append(p)
        scores.append(p["score"])
        
    total_preds = len(preds)
    imgs_with_preds = len(preds_by_img)
    mean_score = float(np.mean(scores)) if scores else 0.0
    
    tp = 0
    fp_pos = 0
    fp_bg = 0
    fn = 0
    
    total_gt_boxes = 0
    fg_images_count = sum(1 for b in gt_map.values() if len(b) > 0)
    bg_images_count = len(gt_map) - fg_images_count
    
    preds_on_fg = 0
    preds_on_bg = 0
    
    for stem, gt_boxes in gt_map.items():
        total_gt_boxes += len(gt_boxes)
        img_preds = preds_by_img.get(stem, [])
        is_fg = len(gt_boxes) > 0
        
        if is_fg:
            preds_on_fg += len(img_preds)
        else:
            preds_on_bg += len(img_preds)
            fp_bg += len(img_preds)
            continue
            
        gt_xyxy = []
        for g in gt_boxes:
            xmin = (g["xc"] - g["w"] / 2.0) * 1024.0
            ymin = (g["yc"] - g["h"] / 2.0) * 1024.0
            xmax = (g["xc"] + g["w"] / 2.0) * 1024.0
            ymax = (g["yc"] + g["h"] / 2.0) * 1024.0
            gt_xyxy.append([xmin, ymin, xmax, ymax])
            
        sorted_preds = sorted(img_preds, key=lambda x: x["score"], reverse=True)
        matched_gt = set()
        
        for p in sorted_preds:
            px, py, pw, ph = p["bbox"]
            p_xyxy = [px, py, px + pw, py + ph]
            
            best_iou = 0.0
            best_gt_idx = -1
            for g_idx, g_box in enumerate(gt_xyxy):
                if g_idx in matched_gt:
                    continue
                iou = compute_iou(p_xyxy, g_box)
                if iou > best_iou:
                    best_iou = iou
                    best_gt_idx = g_idx
                    
            if best_iou >= 0.50 and best_gt_idx != -1:
                tp += 1
                matched_gt.add(best_gt_idx)
            else:
                fp_pos += 1
                
        fn += (len(gt_boxes) - len(matched_gt))
        
    precision = tp / (tp + fp_pos + fp_bg) if (tp + fp_pos + fp_bg) > 0 else 0.0
    fg_precision = tp / (tp + fp_pos) if (tp + fp_pos) > 0 else 0.0
    recall = tp / total_gt_boxes if total_gt_boxes > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    fg_f1 = 2 * fg_precision * recall / (fg_precision + recall) if (fg_precision + recall) > 0 else 0.0
    false_alarm_rate_per_img = preds_on_bg / bg_images_count if bg_images_count > 0 else 0.0
    bg_images_with_fp = sum(1 for stem in preds_by_img if len(gt_map.get(stem, [])) == 0)
    
    return {
        "id": model_spec["id"],
        "paradigm": model_spec["paradigm"],
        "arch": model_spec["arch"],
        "seed": model_spec["seed"],
        "conf_mode": conf_mode,
        "conf_threshold": conf_val,
        "total_detections": total_preds,
        "images_with_detections": imgs_with_preds,
        "mean_confidence": round(mean_score, 4),
        "true_positives": tp,
        "false_positives_fg": fp_pos,
        "false_positives_bg": fp_bg,
        "false_negatives": fn,
        "total_gt_trees": total_gt_boxes,
        "recall": round(recall, 4),
        "precision_overall": round(precision, 4),
        "precision_fg_only": round(fg_precision, 4),
        "f1_overall": round(f1, 4),
        "f1_fg_only": round(fg_f1, 4),
        "false_alarm_rate_per_bg_tile": round(false_alarm_rate_per_img, 4),
        "bg_images_with_fp": bg_images_with_fp,
        "bg_tiles_fp_pct": round(bg_images_with_fp / bg_images_count * 100.0, 2) if bg_images_count > 0 else 0.0,
        "total_bg_images": bg_images_count,
        "total_fg_images": fg_images_count,
    }

def save_fig_all(fig, filename):
    for d in MIRROR_DIRS:
        target = os.path.join(d, filename)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        fig.savefig(target, dpi=300, bbox_inches='tight', pad_inches=0.18)
    print(f"Saved {filename} across all mirrors.", flush=True)
    plt.close(fig)

def plot_counts_breakdown(df, filename, title_suffix=""):
    fig, ax = plt.subplots(figsize=(10, 6))
    archs = ["YOLO12s", "ViT-T16 + D-FINE", "YOLO12s (SAT-493M)", "ViT-T16 (LVD-1689M)", "YOLO12s Triple DINOv3"]
    
    means_total = []
    stds_total = []
    means_tp = []
    means_fp_bg = []
    
    for arch in archs:
        sub = df[df["arch"] == arch]
        if len(sub) == 0:
            means_total.append(0); stds_total.append(0); means_tp.append(0); means_fp_bg.append(0)
            continue
        means_total.append(sub["total_detections"].mean())
        stds_total.append(sub["total_detections"].std() if len(sub) > 1 else 0)
        means_tp.append(sub["true_positives"].mean())
        means_fp_bg.append(sub["false_positives_bg"].mean())
        
    x = np.arange(len(archs))
    width = 0.55
    
    ax.bar(x, means_tp, width, label='True Positives (Verified Trees)', color='#2ca02c', alpha=0.9, edgecolor='black', linewidth=0.8)
    ax.bar(x, means_fp_bg, width, bottom=means_tp, label='Background False Alarms (Negative Slices)', color='#d62728', alpha=0.85, edgecolor='black', linewidth=0.8)
    ax.errorbar(x, means_total, yerr=stds_total, fmt='none', ecolor='black', elinewidth=1.8, capsize=5, capthick=1.5, zorder=5)
    
    ax.set_ylabel('Total Predicted Bounding Boxes (N=4,721 Slices)', fontweight='bold')
    ax.set_title(f'Detection Count & False Discovery Breakdown {title_suffix}', fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(archs, rotation=15, ha='right', fontweight='bold')
    ax.legend(loc='upper right', frameon=True)
    
    for i, (m_tot, s_tot, m_tp, m_fp) in enumerate(zip(means_total, stds_total, means_tp, means_fp_bg)):
        if m_tot > 0:
            ax.text(i, m_tot + (s_tot if s_tot > 0 else 5) + 12, f"{m_tot:.0f} ± {s_tot:.1f}\n(TP: {m_tp:.0f})", ha='center', va='bottom', fontsize=8.5, fontweight='bold')
        
    max_val = max(means_total) if means_total and max(means_total) > 0 else 100
    ax.set_ylim(0, max_val * 1.25)
    save_fig_all(fig, filename)

def plot_tradeoff(df, filename, title_suffix=""):
    fig, ax = plt.subplots(figsize=(8.5, 6))
    archs = ["YOLO12s", "ViT-T16 + D-FINE", "YOLO12s (SAT-493M)", "ViT-T16 (LVD-1689M)", "YOLO12s Triple DINOv3"]
    colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
    
    for idx, row in df.iterrows():
        if row["arch"] in archs:
            c = colors[archs.index(row["arch"])]
            ax.scatter(row["false_alarm_rate_per_bg_tile"] * 1000, row["recall"] * 100, 
                       color=c, s=110, edgecolors='black', linewidth=1.1, zorder=4, alpha=0.85)
        
    for arch, color in zip(archs, colors):
        sub = df[df["arch"] == arch]
        if len(sub) == 0:
            continue
        m_x = sub["false_alarm_rate_per_bg_tile"].mean() * 1000
        s_x = sub["false_alarm_rate_per_bg_tile"].std() * 1000 if len(sub) > 1 else 0
        m_y = sub["recall"].mean() * 100
        s_y = sub["recall"].std() * 100 if len(sub) > 1 else 0
        
        ax.errorbar(m_x, m_y, xerr=s_x, yerr=s_y, fmt='D', color=color, ecolor=color,
                    markersize=10, elinewidth=2, capsize=4, capthick=1.5, zorder=5, label=arch)
        ax.annotate(arch, (m_x, m_y), textcoords="offset points", xytext=(8, 5), fontweight='bold', fontsize=9)
        
    ax.set_xlabel('False Alarm Density (FP Triggers per 1,000 Empty Background Tiles)', fontweight='bold')
    ax.set_ylabel('Ground Truth Tree Recall (%) [IoU = 0.50]', fontweight='bold')
    ax.set_title(f'Operational Tradeoff: Tree Recall vs. False Alarm Density {title_suffix}', fontweight='bold', pad=12)
    ax.legend(loc='lower right', frameon=True)
    save_fig_all(fig, filename)

def plot_comparison_fa_reduction(df_norm, df_opt, filename):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    archs = ["YOLO12s", "ViT-T16 + D-FINE", "YOLO12s (SAT-493M)", "ViT-T16 (LVD-1689M)", "YOLO12s Triple DINOv3"]
    x = np.arange(len(archs))
    width = 0.35
    
    # Left Panel: Background False Alarms
    fp_norm_m, fp_norm_s = [], []
    fp_opt_m, fp_opt_s = [], []
    
    # Right Panel: Overall F1 Score
    f1_norm_m, f1_norm_s = [], []
    f1_opt_m, f1_opt_s = [], []
    
    for arch in archs:
        s_norm = df_norm[df_norm["arch"] == arch]
        s_opt = df_opt[df_opt["arch"] == arch]
        
        fp_norm_m.append(s_norm["false_positives_bg"].mean() if len(s_norm) > 0 else 0)
        fp_norm_s.append(s_norm["false_positives_bg"].std() if len(s_norm) > 1 else 0)
        fp_opt_m.append(s_opt["false_positives_bg"].mean() if len(s_opt) > 0 else 0)
        fp_opt_s.append(s_opt["false_positives_bg"].std() if len(s_opt) > 1 else 0)
        
        f1_norm_m.append(s_norm["f1_overall"].mean() * 100 if len(s_norm) > 0 else 0)
        f1_norm_s.append(s_norm["f1_overall"].std() * 100 if len(s_norm) > 1 else 0)
        f1_opt_m.append(s_opt["f1_overall"].mean() * 100 if len(s_opt) > 0 else 0)
        f1_opt_s.append(s_opt["f1_overall"].std() * 100 if len(s_opt) > 1 else 0)
        
    rects1 = ax1.bar(x - width/2, fp_norm_m, width, yerr=fp_norm_s, label='Standard (c = 0.25)', color='#e74c3c', alpha=0.85, capsize=4, edgecolor='black')
    rects2 = ax1.bar(x + width/2, fp_opt_m, width, yerr=fp_opt_s, label='Calibrated Optimal F1 (c = c*)', color='#2ecc71', alpha=0.85, capsize=4, edgecolor='black')
    ax1.set_ylabel('Background False Alarms (N=4,576 Empty Tiles)', fontweight='bold')
    ax1.set_title('(A) Suppression of Empty Background False Alarms', fontweight='bold', pad=10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(archs, rotation=18, ha='right', fontweight='bold')
    ax1.legend(loc='upper right')
    
    for i, (n_m, o_m) in enumerate(zip(fp_norm_m, fp_opt_m)):
        if n_m > 0 and o_m < n_m:
            drop = (n_m - o_m) / n_m * 100.0
            ax1.text(i, max(n_m, o_m) * 1.05, f"-{drop:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#27ae60')
            
    ax2.bar(x - width/2, f1_norm_m, width, yerr=f1_norm_s, label='Standard (c = 0.25)', color='#3498db', alpha=0.85, capsize=4, edgecolor='black')
    ax2.bar(x + width/2, f1_opt_m, width, yerr=f1_opt_s, label='Calibrated Optimal F1 (c = c*)', color='#9b59b6', alpha=0.85, capsize=4, edgecolor='black')
    ax2.set_ylabel('Overall F1 Score (%) [IoU = 0.50]', fontweight='bold')
    ax2.set_title('(B) Precision-Calibrated F1 Score Comparison', fontweight='bold', pad=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(archs, rotation=18, ha='right', fontweight='bold')
    ax2.legend(loc='upper right')
    
    plt.suptitle('Operational Impact of Optimal F1 Confidence Threshold Calibration (c = 0.25 vs. c*)', fontsize=13, fontweight='bold', y=0.98)
    save_fig_all(fig, filename)

def main():
    print("======================================================================", flush=True)
    print("Master Benchmark Compiler: Combined Testset Dual-Confidence Evaluation", flush=True)
    print("======================================================================", flush=True)
    
    gt_map = load_ground_truth()
    print(f"Loaded ground truth for {len(gt_map)} images.", flush=True)
    fg_count = sum(1 for b in gt_map.values() if len(b) > 0)
    total_trees = sum(len(b) for b in gt_map.values())
    print(f"  Foreground images: {fg_count}, Total tree canopies: {total_trees}", flush=True)
    print(f"  Empty background images: {len(gt_map) - fg_count}", flush=True)
    
    # 1. Standard Confidence (c=0.25)
    print("\n--- Evaluating Standard Confidence (c = 0.25) ---", flush=True)
    results_norm = []
    for spec in MODEL_SPECS:
        json_path = os.path.join(BASE_DIR, "predictions_json", f"{spec['id']}.json")
        res = evaluate_predictions_from_json(gt_map, json_path, spec, conf_mode="standard", conf_val=0.25)
        if res:
            results_norm.append(res)
            
    df_norm = pd.DataFrame(results_norm)
    if len(df_norm) > 0:
        csv_norm = os.path.join(BASE_DIR, "summary_tables", "model_comparison_overview.csv")
        os.makedirs(os.path.dirname(csv_norm), exist_ok=True)
        df_norm.to_csv(csv_norm, index=False)
        print(f"Saved standard conf CSV: {csv_norm} ({len(df_norm)} models)", flush=True)
        
        plot_counts_breakdown(df_norm, os.path.join("figures", "fig1_prediction_counts_by_model.png"), "(Standard c = 0.25)")
        plot_tradeoff(df_norm, os.path.join("figures", "fig2_positive_vs_negative_detection_rates.png"), "(Standard c = 0.25)")
        
    # 2. Optimal F1 Confidence (c=c*)
    print("\n--- Evaluating Calibrated Optimal F1 Confidence (c = c*) ---", flush=True)
    results_opt = []
    for spec in MODEL_SPECS:
        json_path = os.path.join(BASE_DIR, "optimal_f1_conf", "predictions_json", f"{spec['id']}.json")
        res = evaluate_predictions_from_json(gt_map, json_path, spec, conf_mode="optimal_f1", conf_val=spec["opt_conf"])
        if res:
            results_opt.append(res)
            
    df_opt = pd.DataFrame(results_opt)
    if len(df_opt) > 0:
        csv_opt = os.path.join(BASE_DIR, "summary_tables", "model_comparison_optimal_f1.csv")
        os.makedirs(os.path.dirname(csv_opt), exist_ok=True)
        df_opt.to_csv(csv_opt, index=False)
        print(f"Saved optimal conf CSV: {csv_opt} ({len(df_opt)} models)", flush=True)
        
        plot_counts_breakdown(df_opt, os.path.join("figures", "fig1b_prediction_counts_optimal_f1.png"), "(Calibrated Optimal F1 c*)")
        plot_tradeoff(df_opt, os.path.join("figures", "fig2b_positive_vs_negative_detection_rates_optimal_f1.png"), "(Calibrated Optimal F1 c*)")
        
    # 3. Delta Analysis (if both exist)
    if len(df_norm) > 0 and len(df_opt) > 0:
        print("\n--- Computing Delta Comparison (c=0.25 vs c=c*) ---", flush=True)
        common_ids = set(df_norm["id"]).intersection(set(df_opt["id"]))
        deltas = []
        for mid in common_ids:
            r_n = df_norm[df_norm["id"] == mid].iloc[0]
            r_o = df_opt[df_opt["id"] == mid].iloc[0]
            
            fp_drop = r_n["false_positives_bg"] - r_o["false_positives_bg"]
            fp_drop_pct = (fp_drop / r_n["false_positives_bg"] * 100.0) if r_n["false_positives_bg"] > 0 else 0.0
            
            deltas.append({
                "id": mid,
                "paradigm": r_n["paradigm"],
                "arch": r_n["arch"],
                "seed": r_n["seed"],
                "opt_conf": r_o["conf_threshold"],
                "fp_bg_standard": r_n["false_positives_bg"],
                "fp_bg_optimal": r_o["false_positives_bg"],
                "fp_bg_reduction": fp_drop,
                "fp_bg_reduction_pct": round(fp_drop_pct, 2),
                "tp_standard": r_n["true_positives"],
                "tp_optimal": r_o["true_positives"],
                "recall_standard": r_n["recall"],
                "recall_optimal": r_o["recall"],
                "precision_standard": r_n["precision_overall"],
                "precision_optimal": r_o["precision_overall"],
                "f1_standard": r_n["f1_overall"],
                "f1_optimal": r_o["f1_overall"],
                "f1_gain": round(r_o["f1_overall"] - r_n["f1_overall"], 4),
            })
        df_delta = pd.DataFrame(deltas)
        csv_delta = os.path.join(BASE_DIR, "summary_tables", "model_comparison_delta.csv")
        df_delta.to_csv(csv_delta, index=False)
        print(f"Saved delta comparison CSV: {csv_delta}", flush=True)
        
        plot_comparison_fa_reduction(df_norm, df_opt, os.path.join("figures", "fig3_conf025_vs_optimal_f1_false_alarm_reduction.png"))

    print("\n======================================================================", flush=True)
    print("Master Evaluation Compilation Completed Successfully!", flush=True)
    print("======================================================================", flush=True)

if __name__ == "__main__":
    main()
