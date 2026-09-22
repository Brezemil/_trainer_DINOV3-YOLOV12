"""
Thesis Results Figure Generator (Sections 1.1, 1.2, 1.3, and 1.4)
===================================================================
Generates publication-ready figures at 300 DPI:
- Fig 1.1:  CNN Performance Compared (mAP30, 40, 50, 50-95 with STD + latency/param annotations)
- Fig 1.2a: Transformer Architecture Ablation (Frozen vs. Unfrozen vs. Epochs vs. Heads at Seed 100)
- Fig 1.2b: Monolithic DETR vs. Modern Lightweight ViT (RT-DETR-L vs. DINOv3 ViT-T + D-FINE)
- Fig 1.3a: Distillation & Multi-Scale Feature Map Fusion Performance (mAP across teachers)
- Fig 1.3b: Empirical Optimization Loss Dynamics (Side-by-side with STD shadow ribbons)
- Fig 1.3c: Overfitting Index (OI) Comparison across architectural paradigms
- Fig 1.4:  Top Performers Hardware Pareto Frontier (Latency vs. mAP50, Parameter Bubbles & Trainable Cake Wedges)

All percentage axes feature:
- Numbers at 10% markings
- Intermediate tick markings at 5%
- Minor tick markings at 2.5%
- Multi-level background grid for maximum cartographic readability
"""

import os
import json
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator, FuncFormatter
import matplotlib.ticker as ticker
from matplotlib.patches import Wedge, Circle

# Configure Seaborn & Matplotlib for Modern Publication Quality
sns.set_theme(style="whitegrid", font_scale=1.0)
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['grid.color'] = '#e0e0e0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

# Target Directories
OUTPUT_DIRS = [
    r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\thesis_evaluation",
    r"C:\Users\emilb\My Drive\_thesis_eval\figures",
    r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363"
]

def save_plot_to_all(fig, filename):
    for out_dir in OUTPUT_DIRS:
        os.makedirs(out_dir, exist_ok=True)
        dest = os.path.join(out_dir, filename)
        fig.savefig(dest, dpi=300, bbox_inches='tight', pad_inches=0.18)
    print(f"Saved: {filename} to all mirrors.")

def apply_hierarchical_percentage_grid(ax, axis='y', vmin=0.0, vmax=0.70):
    """
    Configures an axis with:
    - Numbers at 10% (0.10)
    - Tick marks at 5% (0.05) with dashed semi-major grid
    - Smaller tick marks at 2.5% (0.025) with dotted minor grid
    """
    if axis == 'y':
        ax.set_ylim(vmin, vmax)
        ax.yaxis.set_major_locator(MultipleLocator(0.10))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{int(round(v * 100))}%"))
        ax.yaxis.set_minor_locator(MultipleLocator(0.025))
        
        ax.tick_params(axis='y', which='major', length=7.0, width=1.2, direction='out', color='#333333')
        ax.tick_params(axis='y', which='minor', length=3.5, width=0.7, direction='out', color='#777777')
        
        # 10% Major Solid Grid
        ax.grid(which='major', axis='y', color='#c8c8c8', linestyle='-', linewidth=0.75, alpha=0.55, zorder=0)
        
        # 5% Semi-major Dashed Grid Lines & Custom Intermediate Ticks
        for v in np.arange(vmin + 0.05, vmax + 0.001, 0.10):
            ax.plot([-0.015, 0], [v, v], transform=ax.get_yaxis_transform(), clip_on=False, color='#444444', lw=1.0)
            ax.axhline(v, color='#d8d8d8', linestyle='--', linewidth=0.60, alpha=0.50, zorder=0)
            
        # 2.5% Minor Dotted Grid Lines
        for v in np.arange(vmin + 0.025, vmax + 0.001, 0.05):
            ax.axhline(v, color='#e8e8e8', linestyle=':', linewidth=0.45, alpha=0.45, zorder=0)
            
    elif axis == 'x':
        ax.set_xlim(vmin, vmax)
        ax.xaxis.set_major_locator(MultipleLocator(0.10))
        ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{int(round(v * 100))}%"))
        ax.xaxis.set_minor_locator(MultipleLocator(0.025))
        
        ax.tick_params(axis='x', which='major', length=7.0, width=1.2, direction='out', color='#333333')
        ax.tick_params(axis='x', which='minor', length=3.5, width=0.7, direction='out', color='#777777')
        
        ax.grid(which='major', axis='x', color='#c8c8c8', linestyle='-', linewidth=0.75, alpha=0.55, zorder=0)
        for v in np.arange(vmin + 0.05, vmax + 0.001, 0.10):
            ax.axvline(v, color='#d8d8d8', linestyle='--', linewidth=0.60, alpha=0.50, zorder=0)
        for v in np.arange(vmin + 0.025, vmax + 0.001, 0.05):
            ax.axvline(v, color='#e8e8e8', linestyle=':', linewidth=0.45, alpha=0.45, zorder=0)

# Seaborn-derived modern palette for Multi-Threshold Evaluation (mAP30, mAP50, mAP50-95)
# Using refined, harmonious deep/muted tones (Deep Slate Blue, Soft Emerald Teal, Rich Warm Coral)
METRIC_COLORS = {
    'mAP30': '#4c72b0',      # Seaborn Deep Blue
    'mAP50': '#55a868',      # Seaborn Soft Forest / Emerald Green
    'mAP50-95': '#dd8452'    # Seaborn Warm Coral / Amber
}

# ==============================================================================
# 1.1. CNN Performance Compared
# ==============================================================================
def make_fig_1_1_cnn_performance(df_master):
    print("Generating Figure 1.1: CNN Performance Compared...")
    
    cnn_models = ['YOLO26n', 'YOLO26s', 'YOLO12n', 'YOLO12s', 'YOLO11n', 'YOLO11s']
    
    # Extract Means and STDs across seeds
    stats = {}
    for m in cnn_models:
        sub = df_master[df_master['canonical_model'] == m]
        stats[m] = {
            'params': sub['params_m'].iloc[0],
            'lat': sub['latency_ms'].iloc[0],
            'fps': sub['fps'].iloc[0],
            'mAP30_m': sub['test_coco_AP30'].mean(),
            'mAP30_s': sub['test_coco_AP30'].std(),
            'mAP50_m': sub['test_coco_AP50'].mean(),
            'mAP50_s': sub['test_coco_AP50'].std(),
            'mAP50_95_m': sub['test_coco_AP'].mean(),
            'mAP50_95_s': sub['test_coco_AP'].std(),
        }

    fig, ax = plt.subplots(figsize=(9.8, 5.4))
    
    x = np.arange(len(cnn_models))
    width = 0.22
    offsets = [-1.0 * width, 0.0, 1.0 * width]
    metrics = ['mAP30', 'mAP50', 'mAP50-95']
    labels = ['mAP@0.30', 'mAP@0.50', 'mAP@0.50:0.95']
    
    for i, (met, lab) in enumerate(zip(metrics, labels)):
        means = [stats[m][f"{met.replace('-', '_')}_m"] for m in cnn_models]
        stds = [stats[m][f"{met.replace('-', '_')}_s"] for m in cnn_models]
        
        bars = ax.bar(x + offsets[i], means, width, yerr=stds, capsize=3.2,
                      label=lab, color=METRIC_COLORS[met], edgecolor='#111111', lw=0.8,
                      error_kw=dict(ecolor='#222222', lw=1.1, capthick=1.1), zorder=3)
        
        # Add numbers above every bar in crisp black with +/- STD
        for bar, val, s in zip(bars, means, stds):
            bar_center_x = bar.get_x() + bar.get_width() / 2.0
            text_x = bar_center_x + width * 0.12  # Subtle offset to the right to avoid error cap clash
            text_y = bar.get_height() + s + 0.012
            ax.text(text_x, text_y, f"{val*100:.1f}\n±{s*100:.1f}",
                    ha='center', va='bottom', fontsize=6.8, fontweight='bold', color='#111111', zorder=5)

    apply_hierarchical_percentage_grid(ax, axis='y', vmin=0.0, vmax=0.76)
    
    ax.set_xticks(x)
    xtick_labels = [
        f"{m}\n({stats[m]['params']:.1f}M params)\n{stats[m]['lat']:.1f} ms · {stats[m]['fps']:.0f} FPS"
        for m in cnn_models
    ]
    ax.set_xticklabels(xtick_labels, fontsize=9.5, fontweight='semibold')
    
    ax.set_ylabel("Mean Average Precision (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title("CNN Architecture Benchmark Comparison across Multi-Scale IoU Thresholds\n"
                 "Evaluated across Random Initialization Seeds (n = 3, Mean ± 1 STD)", fontsize=12.0, fontweight='bold', pad=32)
    
    # Legend moved outside above plot canvas (horizontal, compact)
    ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cccccc', framealpha=0.95,
              fontsize=9.2, ncol=3, loc='lower center', bbox_to_anchor=(0.5, 1.01))
    
    plt.tight_layout()
    save_plot_to_all(fig, "thesis_fig_1_1_cnn_performance.png")
    plt.close(fig)

# ==============================================================================
# 1.2a. Transformer Performance Compared (Ablation: Model & Epochs)
# ==============================================================================
def make_fig_1_2a_transformer_ablation():
    print("Generating Figure 1.2a: Transformer Architecture Ablation...")
    
    # Authoritative ablation conditions: clean model name and trained epochs only
    # Order: 80e -> 100e -> 150e (longer run) -> Frozen 100e -> RT-DETRv2 (100e)
    # (Unfrozen is standard baseline, only mark Frozen explicitly)
    conditions = [
        "ViT-T + D-FINE\n(80 Epochs)",
        "ViT-T + D-FINE\n(100 Epochs)",
        "ViT-T + D-FINE\n(150 Epochs)",
        "ViT-T + D-FINE\nFrozen (100 Epochs)",
        "ViT-T + RT-DETRv2\n(100 Epochs)"
    ]
    
    # Values at Seed 100
    map50_vals = [0.391800, 0.482421, 0.414234, 0.384873, 0.420117]
    map50_95_vals = [0.183200, 0.227571, 0.212639, 0.183400, 0.193824]
    
    fig, ax = plt.subplots(figsize=(9.4, 5.2))
    
    x = np.arange(len(conditions))
    width = 0.28
    
    bars1 = ax.bar(x - width/2, map50_vals, width, label='mAP@0.50', color=METRIC_COLORS['mAP50'], edgecolor='#111111', lw=0.9, zorder=3)
    bars2 = ax.bar(x + width/2, map50_95_vals, width, label='mAP@0.50:0.95', color=METRIC_COLORS['mAP50-95'], edgecolor='#111111', lw=0.9, zorder=3)
    
    # Bar value labels above every bar in crisp black
    for b, val in zip(bars1, map50_vals):
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.010, f"{val*100:.1f}%", ha='center', va='bottom', fontsize=8.6, fontweight='bold', color='#111111')
    for b, val in zip(bars2, map50_95_vals):
        ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.010, f"{val*100:.1f}%", ha='center', va='bottom', fontsize=8.6, fontweight='bold', color='#111111')

    apply_hierarchical_percentage_grid(ax, axis='y', vmin=0.0, vmax=0.62)
    
    ax.set_xticks(x)
    ax.set_xticklabels(conditions, fontsize=9.2, fontweight='semibold')
    ax.set_ylabel("Mean Average Precision (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title("Vision Transformer Representation Ablation: Adaptation Dynamics & Detection Heads\n"
                 "Unified Seed Initialization (Seed 100, Identical Shuffling Order)", fontsize=12.0, fontweight='bold', pad=32)

    # Legend moved outside above plot canvas (horizontal, compact)
    ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cccccc', framealpha=0.95,
              fontsize=9.2, ncol=2, loc='lower center', bbox_to_anchor=(0.5, 1.01))
    
    plt.tight_layout()
    save_plot_to_all(fig, "thesis_fig_1_2a_transformer_ablation.png")
    plt.close(fig)

# ==============================================================================
# 1.2b. Transformer Performance Compared (RT-DETR-L vs. DINOv3 ViT-T + D-FINE)
# ==============================================================================
def make_fig_1_2b_transformer_vs_rtdetr(df_master):
    print("Generating Figure 1.2b: RT-DETR-L vs. DINOv3 ViT-T + D-FINE...")
    
    trans_models = ['RT-DETR-L', 'DINOv3 ViT-T + D-FINE']
    
    stats = {}
    for m in trans_models:
        sub = df_master[df_master['canonical_model'] == m]
        stats[m] = {
            'params': sub['params_m'].iloc[0],
            'lat': sub['latency_ms'].iloc[0],
            'fps': sub['fps'].iloc[0],
            'mAP30_m': sub['test_coco_AP30'].mean(),
            'mAP30_s': sub['test_coco_AP30'].std(),
            'mAP50_m': sub['test_coco_AP50'].mean(),
            'mAP50_s': sub['test_coco_AP50'].std(),
            'mAP50_95_m': sub['test_coco_AP'].mean(),
            'mAP50_95_s': sub['test_coco_AP'].std(),
        }

    fig, ax = plt.subplots(figsize=(8.5, 5.0))
    
    x = np.arange(len(trans_models))
    width = 0.22
    offsets = [-1.0 * width, 0.0, 1.0 * width]
    metrics = ['mAP30', 'mAP50', 'mAP50-95']
    labels = ['mAP@0.30', 'mAP@0.50', 'mAP@0.50:0.95']
    
    for i, (met, lab) in enumerate(zip(metrics, labels)):
        means = [stats[m][f"{met.replace('-', '_')}_m"] for m in trans_models]
        stds = [stats[m][f"{met.replace('-', '_')}_s"] for m in trans_models]
        
        bars = ax.bar(x + offsets[i], means, width, yerr=stds, capsize=3.5,
                      label=lab, color=METRIC_COLORS[met], edgecolor='#111111', lw=0.9,
                      error_kw=dict(ecolor='#222222', lw=1.1, capthick=1.1), zorder=3)
        
        for bar, val, s in zip(bars, means, stds):
            bar_center_x = bar.get_x() + bar.get_width() / 2.0
            text_x = bar_center_x + width * 0.12
            text_y = bar.get_height() + s + 0.012
            ax.text(text_x, text_y, f"{val*100:.1f}\n±{s*100:.1f}",
                    ha='center', va='bottom', fontsize=7.2, fontweight='bold', color='#111111', zorder=5)

    apply_hierarchical_percentage_grid(ax, axis='y', vmin=0.0, vmax=0.76)
    
    ax.set_xticks(x)
    xtick_labels = [
        f"{m}\n({stats[m]['params']:.1f}M params · {stats[m]['lat']:.1f} ms · {stats[m]['fps']:.0f} FPS)"
        for m in trans_models
    ]
    ax.set_xticklabels(xtick_labels, fontsize=10, fontweight='semibold')
    
    ax.set_ylabel("Mean Average Precision (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title("Monolithic Detection Transformer vs. Lightweight Foundation ViT\n"
                 "RT-DETR-L vs. DINOv3 ViT-T + D-FINE (Mean ± 1 STD, n = 3)", fontsize=12.0, fontweight='bold', pad=32)
    
    # Legend moved outside above plot canvas (horizontal, compact)
    ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cccccc', framealpha=0.95,
              fontsize=9.2, ncol=3, loc='lower center', bbox_to_anchor=(0.5, 1.01))
    
    plt.tight_layout()
    save_plot_to_all(fig, "thesis_fig_1_2b_transformer_vs_rtdetr.png")
    plt.close(fig)

# ==============================================================================
# 1.3a. Distillation and Feature Map Fusion Performance Impacts
# ==============================================================================
def make_fig_1_3a_distillation_fusion_map(df_master):
    print("Generating Figure 1.3a: Distillation and Feature Map Fusion Performance...")
    
    models = [
        'YOLO12s', 'YOLO12s (SAT-493M)', 'YOLO12s (LVD-1689M)',
        'DINOv3 ViT-T + D-FINE', 'ViT-T (SAT-493M)', 'ViT-T (LVD-1689M)',
        'YOLO12s Triple DINOv3'
    ]
    
    stats = {}
    for m in models:
        sub = df_master[df_master['canonical_model'] == m]
        stats[m] = {
            'mAP30_m': sub['test_coco_AP30'].mean(),
            'mAP30_s': sub['test_coco_AP30'].std(),
            'mAP50_m': sub['test_coco_AP50'].mean(),
            'mAP50_s': sub['test_coco_AP50'].std(),
            'mAP50_95_m': sub['test_coco_AP'].mean(),
            'mAP50_95_s': sub['test_coco_AP'].std(),
        }

    fig, ax = plt.subplots(figsize=(10.0, 5.2))
    
    x = np.arange(len(models))
    width = 0.22
    offsets = [-1.0 * width, 0.0, 1.0 * width]
    metrics = ['mAP30', 'mAP50', 'mAP50-95']
    labels = ['mAP@0.30', 'mAP@0.50', 'mAP@0.50:0.95']
    
    for i, (met, lab) in enumerate(zip(metrics, labels)):
        means = [stats[m][f"{met.replace('-', '_')}_m"] for m in models]
        stds = [stats[m][f"{met.replace('-', '_')}_s"] for m in models]
        
        bars = ax.bar(x + offsets[i], means, width, yerr=stds, capsize=3.2,
                      label=lab, color=METRIC_COLORS[met], edgecolor='#111111', lw=0.8,
                      error_kw=dict(ecolor='#222222', lw=1.1, capthick=1.1), zorder=3)
        
        for bar, val, s in zip(bars, means, stds):
            bar_center_x = bar.get_x() + bar.get_width() / 2.0
            text_x = bar_center_x + width * 0.12
            text_y = bar.get_height() + s + 0.012
            ax.text(text_x, text_y, f"{val*100:.1f}\n±{s*100:.1f}",
                    ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#111111', zorder=5)

    apply_hierarchical_percentage_grid(ax, axis='y', vmin=0.0, vmax=0.76)
    
    ax.set_xticks(x)
    clean_labels = [
        "YOLO12s\n(Stock)",
        "YOLO12s\n(SAT-493M)",
        "YOLO12s\n(LVD-1689M)",
        "ViT-T\n(Stock)",
        "ViT-T\n(SAT-493M)",
        "ViT-T\n(LVD-1689M)",
        "YOLO12s\nTriple DINOv3"
    ]
    ax.set_xticklabels(clean_labels, fontsize=8.8, fontweight='semibold')
    
    # Demarcation lines between paradigms
    ax.axvline(2.5, color='#aaaaaa', linestyle='--', lw=1.2, alpha=0.7)
    ax.axvline(5.5, color='#aaaaaa', linestyle='--', lw=1.2, alpha=0.7)
    
    # All 3 paradigm titles aligned on the exact same vertical level (y = 0.715)
    ax.text(1.0, 0.715, "CNN Students", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#4c72b0')
    ax.text(4.0, 0.715, "ViT Students", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#c44e52')
    ax.text(6.0, 0.715, "Multi-Scale Fused", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#8172b3')

    ax.set_ylabel("Mean Average Precision (%)", fontsize=10.5, fontweight='bold', labelpad=10)
    ax.set_title("Cross-Domain Knowledge Distillation & Multi-Scale Feature Map Fusion Impacts\n"
                 "Comparison of Earth Observation (SAT-493M) vs. Natural Web Images (LVD-1689M) across Seeds (Mean ± 1 STD)",
                 fontsize=11.5, fontweight='bold', pad=32)
    
    # Place legend cleanly outside the plot canvas centered above the axis
    ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cccccc', framealpha=0.95,
              fontsize=9.2, ncol=3, loc='lower center', bbox_to_anchor=(0.5, 1.01))
    
    plt.tight_layout()
    save_plot_to_all(fig, "thesis_fig_1_3a_distillation_fusion_map.png")
    plt.close(fig)

# ==============================================================================
# ==============================================================================
# 1.3b. Empirical Optimization Loss Dynamics (Side-by-Side Plots with STD Ribbons)
# ==============================================================================
def make_fig_1_3b_loss_trajectories():
    print("Generating Figure 1.3b: Empirical Optimization Loss Dynamics (Full Window)...")
    
    with open(r"thesis_evaluation/oi_curves_data.json", 'r') as f:
        oi_data = json.load(f)

    base_lightly = r"C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports"
    hist_dir = r"C:\Users\emilb\My Drive\_thesis_eval\metric_histories"

    def load_full_yolo_curves(file_list):
        curves_tr = []
        curves_va = []
        max_len = max(len(pd.read_csv(f)) for f in file_list)
        epochs = np.arange(1, max_len + 1)
        for f in file_list:
            df = pd.read_csv(f)
            df.columns = [c.strip() for c in df.columns]
            tr = (df['train/box_loss'] + df['train/cls_loss'] + df['train/dfl_loss']).values
            va = (df['val/box_loss'] + df['val/cls_loss'] + df['val/dfl_loss']).values
            tr_pad = np.full(max_len, np.nan)
            va_pad = np.full(max_len, np.nan)
            tr_pad[:len(tr)] = tr
            va_pad[:len(va)] = va
            curves_tr.append(tr_pad)
            curves_va.append(va_pad)
        tr_m = np.nanmean(curves_tr, axis=0)
        tr_s = np.nanstd(curves_tr, axis=0)
        va_m = np.nanmean(curves_va, axis=0)
        va_s = np.nanstd(curves_va, axis=0)
        return epochs, tr_m, tr_s, va_m, va_s

    fig, (ax_vit, ax_yolo) = plt.subplots(1, 2, figsize=(10.5, 5.4), sharey=False)

    # ------------------ PANEL A: ViT Family (100 Epochs) ------------------
    # Using harmonious Seaborn color palette: Forest Green, Deep Blue, Warm Coral
    vit_models = [
        ('DINOv3 ViT-T + D-FINE', '#55a868', 'Stock'),
        ('ViT-T (SAT-493M)', '#4c72b0', 'SAT-493M'),
        ('ViT-T (LVD-1689M)', '#dd8452', 'LVD-1689M')
    ]
    
    val_handles_vit, tr_handles_vit = [], []
    for mod_key, col, lab in vit_models:
        d = oi_data[mod_key]
        ep = d['epochs']
        tr_m = np.array(d['train_mean'])
        va_m = np.array(d['val_mean'])
        
        # Validation: solid, opaque line (prominent)
        h_v, = ax_vit.plot(ep, va_m, color=col, lw=2.2, linestyle='-', alpha=1.0, label=f"{lab} (Val)")
        # Training: solid, semi-transparent line
        h_t, = ax_vit.plot(ep, tr_m, color=col, lw=1.5, linestyle='-', alpha=0.45, label=f"{lab} (Train)")
        val_handles_vit.append(h_v)
        tr_handles_vit.append(h_t)

    ax_vit.set_xlim(1, 100)
    ax_vit.set_ylim(1.4, 3.8)
    ax_vit.set_xlabel("Training Epoch (N = 100)", fontsize=10.5, fontweight='bold')
    ax_vit.set_ylabel("DINOv3 Compound Loss\n(1.0 VFL + 2.5 GIoU + 5.0 BBox)", fontsize=10.5, fontweight='bold', labelpad=8)
    ax_vit.set_title("(A) Vision Transformer Optimization Dynamics\n"
                     "Pretraining & Adaptation Trajectories (Mean)", fontsize=10.5, fontweight='bold', pad=44)
    ax_vit.grid(True, linestyle='--', color='#e0e0e0', alpha=0.7)
    
    # Legend placed outside above subplot A, ordered horizontally: Row 1 Val, Row 2 Train
    ordered_vit_handles = val_handles_vit + tr_handles_vit
    ax_vit.legend(handles=ordered_vit_handles, frameon=True, facecolor='#ffffff', edgecolor='#cccccc',
                  framealpha=0.95, fontsize=7.6, loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=3)

    # ------------------ PANEL B: YOLO Family Across Full Training Horizons ------------------
    # Palette: Charcoal Stock, Deep Blue SAT, Warm Coral LVD, Soft Purple Triple DINO
    yolo_configs = [
        ('Stock', '#2b2b2b', [os.path.join(base_lightly, f'yolo12s_seed_{s}', 'results.csv') for s in [42, 100, 999]]),
        ('SAT-493M', '#4c72b0', [os.path.join(base_lightly, f'yolo12s_sat493m_seed{s}', 'results.csv') for s in [42, 100, 999]]),
        ('LVD-1689M', '#dd8452', [os.path.join(base_lightly, f'yolo12s_lvd1689m_seed{s}', 'results.csv') for s in [42, 100, 999]]),
        ('Triple DINO', '#8172b3', [glob.glob(os.path.join(hist_dir, f'*triple_dino3*seed_{s}*.csv'))[0] for s in [42, 100, 999]])
    ]

    val_handles_yolo, tr_handles_yolo = [], []
    for lab, col, flist in yolo_configs:
        ep, tr_m, tr_s, va_m, va_s = load_full_yolo_curves(flist)
        # Validation: solid, opaque line
        h_v, = ax_yolo.plot(ep, va_m, color=col, lw=2.2, linestyle='-', alpha=1.0, label=f"{lab} (Val)")
        # Training: solid, semi-transparent line
        h_t, = ax_yolo.plot(ep, tr_m, color=col, lw=1.5, linestyle='-', alpha=0.45, label=f"{lab} (Train)")
        val_handles_yolo.append(h_v)
        tr_handles_yolo.append(h_t)

    ax_yolo.set_xlim(1, 305)
    ax_yolo.set_ylim(2.0, 17.5)
    ax_yolo.set_xlabel("Training Epoch (Full Horizon: 71 - 300 Epochs)", fontsize=10.5, fontweight='bold')
    ax_yolo.set_ylabel("YOLO12 Compound Loss\n(0.5 BCE + 7.5 CIoU + 1.5 DFL)", fontsize=10.5, fontweight='bold', labelpad=8)
    ax_yolo.set_title("(B) CNN & Feature Fusion Optimization Dynamics\n"
                      "Convergence & Distillation Trajectories (Mean)", fontsize=10.5, fontweight='bold', pad=44)
    ax_yolo.grid(True, linestyle='--', color='#e0e0e0', alpha=0.7)
    
    # Legend placed outside above subplot B, ordered horizontally: Row 1 Val, Row 2 Train
    ordered_yolo_handles = val_handles_yolo + tr_handles_yolo
    ax_yolo.legend(handles=ordered_yolo_handles, frameon=True, facecolor='#ffffff', edgecolor='#cccccc',
                   framealpha=0.95, fontsize=7.2, loc='lower center', bbox_to_anchor=(0.5, 1.01), ncol=4)

    plt.tight_layout()
    save_plot_to_all(fig, "thesis_fig_1_3b_loss_trajectories.png")
    plt.close(fig)

# ==============================================================================
# 1.3c. Overfitting Index (OI) Comparison Bar Chart (Full Training Window)
# ==============================================================================
def make_fig_1_3c_overfitting_index():
    print("Generating Figure 1.3c: Overfitting Index Comparison (Full Training Window)...")
    
    fig, (ax_yolo, ax_vit) = plt.subplots(1, 2, figsize=(9.8, 4.8), gridspec_kw={'width_ratios': [4, 3]})

    # YOLO Family (Full Training Window)
    yolo_labels = ["YOLO12s\n(Stock)", "YOLO12s\n(SAT-493M)", "YOLO12s\n(LVD-1689M)", "YOLO12s\nTriple DINOv3"]
    yolo_means = [17041.20, 1926.12, 1737.61, 965.25]
    yolo_stds = [2017.12, 446.22, 1207.41, 252.11]
    yolo_colors = ['#4c72b0', '#55a868', '#dd8452', '#8172b3']

    x_yolo = np.arange(len(yolo_labels))
    b_yolo = ax_yolo.bar(x_yolo, yolo_means, yerr=yolo_stds, capsize=4.5,
                         color=yolo_colors, edgecolor='#222222', lw=0.9, width=0.55, zorder=3)
    
    # Numbers atop bars with STD
    for b, m, s in zip(b_yolo, yolo_means, yolo_stds):
        ax_yolo.text(b.get_x() + b.get_width()/2.0, m + s + 500, f"{m:,.0f}\n±{s:,.0f}",
                     ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')

    ax_yolo.set_ylim(0, 22000)
    ax_yolo.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x/1000)}k" if x > 0 else "0"))
    ax_yolo.set_xticks(x_yolo)
    ax_yolo.set_xticklabels(yolo_labels, fontsize=9.5, fontweight='semibold')
    ax_yolo.set_ylabel("Cumulative Overfitting Index (OI)", fontsize=11, fontweight='bold', labelpad=8)
    ax_yolo.set_title("YOLO12 Family Overfitting Index\nOI = Σ e · max(0, L_val - L_train)", fontsize=11.5, fontweight='bold', pad=10)
    ax_yolo.grid(True, axis='y', linestyle='--', color='#e0e0e0', alpha=0.7, zorder=0)

    # ViT Family (Full Window)
    vit_labels = ["ViT-T\n(Stock)", "ViT-T\n(LVD-1689M)", "ViT-T\n(SAT-493M)"]
    vit_means = [0.0, 0.0, 615.30]
    vit_stds = [0.0, 0.0, 548.42]
    vit_colors = ['#55a868', '#dd8452', '#4c72b0']

    x_vit = np.arange(len(vit_labels))
    b_vit = ax_vit.bar(x_vit, vit_means, yerr=vit_stds, capsize=4.5,
                       color=vit_colors, edgecolor='#222222', lw=0.9, width=0.55, zorder=3)
    
    ax_vit.text(0, 30, "0.0\n±0.0", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')
    ax_vit.text(1, 30, "0.0\n±0.0", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')
    ax_vit.text(2, vit_means[2] + vit_stds[2] + 40, f"{vit_means[2]:.0f}\n±{vit_stds[2]:.0f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')

    ax_vit.set_ylim(0, 1500)
    ax_vit.set_xticks(x_vit)
    ax_vit.set_xticklabels(vit_labels, fontsize=9.5, fontweight='semibold')
    ax_vit.set_ylabel("Cumulative Overfitting Index (OI)", fontsize=11, fontweight='bold', labelpad=8)
    ax_vit.set_title("ViT-T Family Overfitting Index\n(Non-comparable across loss formulas)", fontsize=11.5, fontweight='bold', pad=10)
    ax_vit.grid(True, axis='y', linestyle='--', color='#e0e0e0', alpha=0.7, zorder=0)

    fig.suptitle("Empirical Generalization Gap & Overfitting Index Across Architectural Paradigms (Vapnik Formulation)",
                 fontsize=12.5, fontweight='bold', y=1.02)
    plt.tight_layout()
    save_plot_to_all(fig, "thesis_fig_1_3c_overfitting_index_bar.png")
    plt.close(fig)

# ==============================================================================
# 1.3d. Compound Overfitting Index (Loss Gap + Classification Accuracy Proxy)
# ==============================================================================
def make_fig_1_3d_compound_overfitting_index():
    print("Generating Figure 1.3d: Compound Overfitting Index (Loss Gap + Accuracy Proxy)...")
    
    fig, (ax_yolo, ax_vit) = plt.subplots(1, 2, figsize=(9.8, 5.0), gridspec_kw={'width_ratios': [4, 3]})

    # YOLO Family
    yolo_labels = ["YOLO12s\n(Stock)", "YOLO12s\n(SAT-493M)", "YOLO12s\n(LVD-1689M)", "YOLO12s\nTriple DINOv3"]
    yolo_loss = np.array([17041.20, 1926.12, 1737.61, 965.25])
    yolo_acc = np.array([1508.18, 161.86, 142.30, 12.33])
    yolo_total = yolo_loss + yolo_acc
    yolo_total_stds = [2211.74, 481.45, 1314.85, 266.03]
    yolo_colors = ['#4c72b0', '#55a868', '#dd8452', '#8172b3']

    x_yolo = np.arange(len(yolo_labels))
    w = 0.52

    # Stacked Bars: Base = Loss Gap, Top = Accuracy Proxy Gap
    b_loss = ax_yolo.bar(x_yolo, yolo_loss, width=w, color=yolo_colors, edgecolor='#222222', lw=0.9, zorder=3,
                         label="Loss Generalization Gap (dL)")
    b_acc = ax_yolo.bar(x_yolo, yolo_acc, bottom=yolo_loss, width=w, color='#eedd88', edgecolor='#222222', lw=0.9,
                        hatch='///', zorder=3, label="Accuracy Proxy Gap (dAcc)")
    # Total error bars
    ax_yolo.errorbar(x_yolo, yolo_total, yerr=yolo_total_stds, fmt='none', ecolor='#222222', elinewidth=1.2,
                     capsize=4.5, capthick=1.2, zorder=4)

    # Numbers atop bars
    for i, (tot, std_v) in enumerate(zip(yolo_total, yolo_total_stds)):
        ax_yolo.text(i, tot + std_v + 500, f"{tot:,.0f}\n±{std_v:,.0f}",
                     ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')

    ax_yolo.set_ylim(0, 26000)
    ax_yolo.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x/1000)}k" if x > 0 else "0"))
    ax_yolo.set_xticks(x_yolo)
    ax_yolo.set_xticklabels(yolo_labels, fontsize=9.5, fontweight='semibold')
    ax_yolo.set_ylabel("Compound Overfitting Index (OI)", fontsize=11, fontweight='bold', labelpad=8)
    ax_yolo.set_title("YOLO12 Family Compound OI\nStacked Loss Gap + Accuracy Proxy Gap", fontsize=11.5, fontweight='bold', pad=10)
    ax_yolo.grid(True, axis='y', linestyle='--', color='#e0e0e0', alpha=0.7, zorder=0)

    # ViT Family
    vit_labels = ["ViT-T\n(Stock)", "ViT-T\n(LVD-1689M)", "ViT-T\n(SAT-493M)"]
    vit_loss = np.array([0.0, 0.0, 615.30])
    vit_acc = np.array([0.0, 0.0, 345.50])
    vit_total = vit_loss + vit_acc
    vit_total_stds = [0.0, 0.0, 847.90]
    vit_colors = ['#55a868', '#dd8452', '#4c72b0']

    x_vit = np.arange(len(vit_labels))
    ax_vit.bar(x_vit, vit_loss, width=w, color=vit_colors, edgecolor='#222222', lw=0.9, zorder=3)
    ax_vit.bar(x_vit, vit_acc, bottom=vit_loss, width=w, color='#eedd88', edgecolor='#222222', lw=0.9,
               hatch='///', zorder=3)
    ax_vit.errorbar(x_vit, vit_total, yerr=vit_total_stds, fmt='none', ecolor='#222222', elinewidth=1.2,
                    capsize=4.5, capthick=1.2, zorder=4)

    ax_vit.text(0, 40, "0.0\n±0.0", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')
    ax_vit.text(1, 40, "0.0\n±0.0", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')
    ax_vit.text(2, vit_total[2] + vit_total_stds[2] + 40, f"{vit_total[2]:.0f}\n±{vit_total_stds[2]:.0f}",
                ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#111111')

    ax_vit.set_ylim(0, 2400)
    ax_vit.set_xticks(x_vit)
    ax_vit.set_xticklabels(vit_labels, fontsize=9.5, fontweight='semibold')
    ax_vit.set_ylabel("Compound Overfitting Index (OI)", fontsize=11, fontweight='bold', labelpad=8)
    ax_vit.set_title("ViT-T Family Compound OI\n(Non-comparable across loss formulas)", fontsize=11.5, fontweight='bold', pad=10)
    ax_vit.grid(True, axis='y', linestyle='--', color='#e0e0e0', alpha=0.7, zorder=0)

    # Shared unified legend placed outside centered above both panels (horizontal)
    fig.legend(handles=[b_loss, b_acc], labels=["Loss Generalization Gap (dL)", "Accuracy Proxy Gap (dAcc)"],
               loc='lower center', bbox_to_anchor=(0.5, 0.90), ncol=2, frameon=True,
               facecolor='#ffffff', edgecolor='#cccccc', framealpha=0.95, fontsize=9.0)

    fig.suptitle("Dual-Track Evaluation: Compound Overfitting Index with Classification Accuracy Proxy (Aburas-Extended)",
                 fontsize=12.0, fontweight='bold', y=0.99)
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    save_plot_to_all(fig, "thesis_fig_1_3d_compound_overfitting_index.png")
    plt.close(fig)

# ==============================================================================
# 1.4. Top Performers Hardware Pareto Frontier (Bubble & Trainable Cake Wedges)
# ==============================================================================
def make_fig_1_4_pareto_frontier(df_master):
    print("Generating Figure 1.4: Hardware Pareto Frontier with Parameter Cake Wedges...")
    
    # Selected 13 primary evaluated models
    models_to_plot = [
        ('YOLO26n', 'Baseline CNN', '#4c72b0', 2.3, 2.3, 2.4, 416.7),
        ('YOLO26s', 'Baseline CNN', '#4c72b0', 7.2, 7.2, 4.2, 238.1),
        ('YOLO11n', 'Baseline CNN', '#4c72b0', 2.6, 2.6, 2.8, 357.1),
        ('YOLO11s', 'Baseline CNN', '#4c72b0', 9.4, 9.4, 5.1, 196.1),
        ('YOLO12n', 'Baseline CNN', '#4c72b0', 2.6, 2.6, 2.9, 344.8),
        ('YOLO12s', 'Baseline CNN', '#4c72b0', 9.3, 9.3, 4.9, 204.1),
        ('RT-DETR-L', 'Baseline Transformer', '#55a868', 32.0, 32.0, 18.6, 53.8),
        ('DINOv3 ViT-T + D-FINE', 'Baseline Transformer', '#55a868', 10.8, 10.8, 11.5, 87.0),
        ('YOLO12s (SAT-493M)', 'Distilled Student', '#dd8452', 9.3, 9.3, 4.9, 204.1),
        ('YOLO12s (LVD-1689M)', 'Distilled Student', '#dd8452', 9.3, 9.3, 4.9, 204.1),
        ('ViT-T (SAT-493M)', 'Distilled Student', '#dd8452', 10.8, 10.8, 11.5, 87.0),
        ('ViT-T (LVD-1689M)', 'Distilled Student', '#dd8452', 10.8, 10.8, 11.5, 87.0),
        ('YOLO12s Triple DINOv3', 'Multi-Scale Feature Fusion', '#8172b3', 95.8, 9.8, 14.8, 67.6) # 9.8M trainable
    ]
    
    fig, ax = plt.subplots(figsize=(10.0, 6.0))
    
    # Collect coordinates
    pts = []
    for mod_name, fam, fam_col, total_p, train_p, lat, fps in models_to_plot:
        sub = df_master[df_master['canonical_model'] == mod_name]
        ap50_m = sub['test_coco_AP50'].mean()
        ap50_s = sub['test_coco_AP50'].std()
        pts.append({
            'name': mod_name,
            'fam': fam,
            'col': fam_col,
            'total_p': total_p,
            'train_p': train_p,
            'lat': lat,
            'fps': fps,
            'ap50_m': ap50_m,
            'ap50_s': ap50_s
        })
    
    pts_df = pd.DataFrame(pts)

    # Set Axes limits
    ax.set_xlim(1.0, 20.5)
    apply_hierarchical_percentage_grid(ax, axis='y', vmin=0.35, vmax=0.54)
    
    ax.set_xlabel("Inference Latency (ms) [NVIDIA TensorRT FP16, Batch=1, 1024×1024]", fontsize=11, fontweight='bold', labelpad=8)
    ax.set_ylabel("Mean Average Precision (%)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title("Empirical Hardware Pareto Frontier & Architectural Footprint\n"
                 "Latency vs. Canopy Detection Accuracy across Model Families with Parameter Cake Slices",
                 fontsize=12.0, fontweight='bold', pad=38)

    # Draw Empirical Stepped Pareto Frontier line
    pareto_line_x = [2.4, 2.8, 2.9, 4.9, 20.0]
    pareto_line_y = [0.4622, 0.4859, 0.4916, 0.4991, 0.4991]
    ax.step(pareto_line_x, pareto_line_y, where='post', color='#2b2b2b', linestyle='--', lw=1.8, alpha=0.75,
            label='Empirical Pareto Frontier', zorder=2)

    # First pass: Draw display-space pie bubbles centered at each model coordinate
    fig.canvas.draw() # Force coordinate calculation
    for _, row in pts_df.iterrows():
        x, y = row['lat'], row['ap50_m']
        tot_p, tr_p = row['total_p'], row['train_p']
        col = row['col']
        
        # Radius in points proportional to square root of parameters
        r_pts = 7.0 + np.sqrt(tot_p / 100.0) * 26.0
        frac = tr_p / tot_p
        
        disp_pt = ax.transData.transform((x, y))
        
        # Background circle in neutral soft gray (represents total parameter footprint)
        w_bg = Wedge(disp_pt, r_pts, 0, 360, facecolor='#eaeaea', edgecolor='#666666', linewidth=0.9, alpha=0.75)
        # Trainable cake segment in family color
        w_tr = Wedge(disp_pt, r_pts, 0, 360 * frac, facecolor=col, edgecolor='#222222', linewidth=0.9, alpha=0.85)
        
        w_bg.set_transform(None)
        w_tr.set_transform(None)
        ax.add_patch(w_bg)
        ax.add_patch(w_tr)

    # Second pass: Draw error bars and labels
    for _, row in pts_df.iterrows():
        x, y = row['lat'], row['ap50_m']
        y_err = row['ap50_s']
        col = row['col']
        raw_name = row['name']
        
        # Call both YOLO12s and ViT-T undistilled as (Stock) when distinction with distilled models is necessary
        if raw_name == 'YOLO12s':
            disp_name = 'YOLO12s (Stock)'
        elif raw_name == 'DINOv3 ViT-T + D-FINE':
            disp_name = 'ViT-T (Stock)'
        else:
            disp_name = raw_name
        
        # Center marker point
        ax.plot(x, y, marker='o', markersize=4.5, color='#ffffff', markeredgecolor='#111111', markeredgewidth=1.1, zorder=5)
        
        # Cross-seed error bar
        ax.errorbar(x, y, yerr=y_err, fmt='none', ecolor='#111111', elinewidth=1.4, capsize=4.0, capthick=1.4, zorder=6)
        
        # Smart label offsets to prevent collisions
        offset_x, offset_y = 0.35, 0.0035
        ha = 'left'
        if raw_name == 'YOLO12s':
            offset_x, offset_y, ha = -0.45, 0.0075, 'right'
        elif raw_name == 'YOLO12s (SAT-493M)':
            offset_x, offset_y, ha = 0.50, 0.0010, 'left'
        elif raw_name == 'YOLO12s (LVD-1689M)':
            offset_x, offset_y, ha = 0.50, -0.0085, 'left'
        elif raw_name == 'YOLO11s':
            offset_x, offset_y, ha = 0.50, 0.0070, 'left'
        elif raw_name == 'YOLO12n':
            offset_x, offset_y, ha = -0.40, 0.0065, 'right'
        elif raw_name == 'YOLO11n':
            offset_x, offset_y, ha = -0.40, -0.0080, 'right'
        elif raw_name == 'YOLO26n':
            offset_x, offset_y, ha = -0.35, -0.0070, 'right'
        elif raw_name == 'ViT-T (LVD-1689M)':
            offset_x, offset_y, ha = 0.55, 0.0055, 'left'
        elif raw_name == 'ViT-T (SAT-493M)':
            offset_x, offset_y, ha = 0.55, -0.0070, 'left'
        elif raw_name == 'DINOv3 ViT-T + D-FINE':
            offset_x, offset_y, ha = -0.55, 0.0070, 'right'
        elif raw_name == 'YOLO12s Triple DINOv3':
            offset_x, offset_y, ha = 0.60, 0.0040, 'left'
        elif raw_name == 'RT-DETR-L':
            offset_x, offset_y, ha = -0.55, 0.0060, 'right'

        ax.text(x + offset_x, y + offset_y, f"{disp_name}\n({row['ap50_m']*100:.1f}%)",
                fontsize=8.4, fontweight='bold', color='#111111', ha=ha, va='center',
                bbox=dict(boxstyle="round,pad=0.20", fc="#ffffff", ec="#cccccc", alpha=0.85, lw=0.6), zorder=7)

    # Family Legend placed cleanly outside the plot canvas centered above the axis (2 compact rows)
    fam_handles = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#4c72b0', markersize=9, label='Pure CNN Baselines'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#55a868', markersize=9, label='Vision Transformer Baselines'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#dd8452', markersize=9, label='Distilled Students'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#8172b3', markersize=9, label='Multi-Scale Feature Fusion'),
        plt.Line2D([0], [0], color='#2b2b2b', linestyle='--', lw=1.8, label='Empirical Pareto Frontier')
    ]
    ax.legend(handles=fam_handles, frameon=True, facecolor='#ffffff', edgecolor='#cccccc', framealpha=0.95,
              fontsize=8.8, ncol=3, loc='lower center', bbox_to_anchor=(0.5, 1.01))

    # Explanatory Inset Box explaining Bubble & Cake Slice Meaning
    ax.text(19.8, 0.362,
            "● Bubble Area: Total Parameter Count (2.3M – 95.8M)\n"
            "● Colored Cake Wedge: Trainable Parameters (%)\n"
            "   (Triple DINOv3: 9.8M Trainable / 86M Frozen)",
            fontsize=8.5, fontweight='semibold', color='#333333', ha='right', va='bottom',
            bbox=dict(boxstyle="round,pad=0.45", fc="#fbfbfb", ec="#999999", lw=0.8))

    plt.tight_layout()
    save_plot_to_all(fig, "thesis_fig_1_4_pareto_frontier.png")
    plt.close(fig)

# ==============================================================================
# Master Generation Pipeline
# ==============================================================================
def main():
    print("======================================================================")
    print("Generating Master Results Figure Suite (Sections 1.1, 1.2, 1.3, 1.4)")
    print("======================================================================")
    
    # Load Master Database
    master_path = r"thesis_evaluation/master_runs_database.csv"
    df_master = pd.read_csv(master_path)
    
    make_fig_1_1_cnn_performance(df_master)
    make_fig_1_2a_transformer_ablation()
    make_fig_1_2b_transformer_vs_rtdetr(df_master)
    make_fig_1_3a_distillation_fusion_map(df_master)
    make_fig_1_3b_loss_trajectories()
    make_fig_1_3c_overfitting_index()
    make_fig_1_3d_compound_overfitting_index()
    make_fig_1_4_pareto_frontier(df_master)
    
    print("\n======================================================================")
    print("All 8 Publication Figures Successfully Generated and Mirrored!")
    print("======================================================================")

if __name__ == '__main__':
    main()
