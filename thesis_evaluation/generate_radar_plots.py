# -*- coding: utf-8 -*-
"""
Generate Publication-Grade Polar Radar Plots for Master's Thesis:
1. Radar plot for Benchmark mAP@50 across all 14 trained models (with ± 1 STD top-down error bands)
2. Radar plot for Strict mAP(50-95) across all 14 trained models (with ± 1 STD top-down error bands)
3. Combined 2-panel publication figure with generous spacing and zero label collisions

Updates:
- Strictly top-down 2D radial error bars with geometrically perpendicular end caps (zero 3D tilt/skew).
- Scientific naming: YOLO12s (SAT-493M), YOLO12s (LVD-1689M), ViT-T (SAT-493M), ViT-T (LVD-1689M).
- Removed qualitative terms like [Champion], [Winner] from plots, legends, and axis labels.
- Optimized typography and margins to eliminate occlusion.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Set high-resolution styling
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

DEST_DIRS = [
    r"thesis_evaluation",
    r"C:\Users\emilb\My Drive\_thesis_eval\figures",
    r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363"
]

for d in DEST_DIRS:
    os.makedirs(d, exist_ok=True)

# 14 Models in structured order by architecture
MODELS_DATA = [
    # Undistilled CNNs
    {"name": "YOLO12s (Stock)", "short": "YOLO12s\n(Stock)", "cat": "CNN", "map50": 49.91, "map50_std": 0.75, "mapstrict": 23.18, "mapstrict_std": 0.45},
    {"name": "YOLO12n", "short": "YOLO12n", "cat": "CNN", "map50": 49.16, "map50_std": 0.35, "mapstrict": 22.95, "mapstrict_std": 0.30},
    {"name": "YOLO11n", "short": "YOLO11n", "cat": "CNN", "map50": 48.59, "map50_std": 0.38, "mapstrict": 22.84, "mapstrict_std": 0.31},
    {"name": "YOLO11s", "short": "YOLO11s", "cat": "CNN", "map50": 48.41, "map50_std": 2.53, "mapstrict": 23.54, "mapstrict_std": 1.65},
    {"name": "YOLO26s", "short": "YOLO26s", "cat": "CNN", "map50": 47.70, "map50_std": 1.32, "mapstrict": 21.48, "mapstrict_std": 1.32},
    {"name": "YOLO26n", "short": "YOLO26n", "cat": "CNN", "map50": 46.22, "map50_std": 0.42, "mapstrict": 21.15, "mapstrict_std": 0.28},
    
    # Vision Transformers
    {"name": "DINOv3 ViT-T + D-FINE", "short": "DINOv3 ViT-T\n+ D-FINE", "cat": "ViT", "map50": 48.84, "map50_std": 0.99, "mapstrict": 23.38, "mapstrict_std": 0.64},
    {"name": "RT-DETRv2-S", "short": "RT-DETRv2-S", "cat": "ViT", "map50": 46.50, "map50_std": 0.60, "mapstrict": 21.80, "mapstrict_std": 0.74},
    {"name": "RT-DETR-L", "short": "RT-DETR-L", "cat": "ViT", "map50": 40.63, "map50_std": 0.85, "mapstrict": 18.92, "mapstrict_std": 0.61},
    
    # Distilled Models
    {"name": "YOLO12s (SAT-493M)", "short": "YOLO12s\n(SAT-493M)", "cat": "Distilled", "map50": 48.01, "map50_std": 0.41, "mapstrict": 22.71, "mapstrict_std": 0.37},
    {"name": "YOLO12s (LVD-1689M)", "short": "YOLO12s\n(LVD-1689M)", "cat": "Distilled", "map50": 46.49, "map50_std": 0.67, "mapstrict": 21.90, "mapstrict_std": 0.52},
    {"name": "DINOv3 ViT-T (LVD-1689M)", "short": "DINOv3 ViT-T\n(LVD-1689M)", "cat": "Distilled", "map50": 48.38, "map50_std": 2.09, "mapstrict": 23.04, "mapstrict_std": 0.66},
    {"name": "DINOv3 ViT-T (SAT-493M)", "short": "DINOv3 ViT-T\n(SAT-493M)", "cat": "Distilled", "map50": 47.52, "map50_std": 0.59, "mapstrict": 22.15, "mapstrict_std": 0.44},
    
    # Fused Multi-Scale
    {"name": "YOLO12s (DINOv3)", "short": "YOLO12s\n(DINOv3)", "cat": "Fused", "map50": 46.10, "map50_std": 0.17, "mapstrict": 22.77, "mapstrict_std": 0.33},
]

CAT_COLORS = {
    "CNN": "#1f77b4",        # Blue
    "ViT": "#2ca02c",        # Green
    "Distilled": "#ff7f0e",  # Orange
    "Fused": "#9467bd"       # Purple
}

import shutil

def save_all(fig, fname):
    primary_target = os.path.join(DEST_DIRS[0], fname)
    fig.savefig(primary_target, dpi=300, bbox_inches='tight', pad_inches=0.25)
    for d in DEST_DIRS[1:]:
        target = os.path.join(d, fname)
        try:
            shutil.copy2(primary_target, target)
        except Exception as e:
            print(f"Warning: Could not copy to {target}: {e}")
    print(f"Saved {fname} to all mirrors.")

def draw_radar_subplot(ax, metric_key, std_key, r_lim, r_ticks, unit="%", r_offset_text=1.07):
    N = len(MODELS_DATA)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    
    # Values
    means = np.array([m[metric_key] for m in MODELS_DATA])
    stds = np.array([m[std_key] for m in MODELS_DATA])
    
    # Close loops for polygon filling
    angles_c = np.concatenate((angles, [angles[0]]))
    means_c = np.concatenate((means, [means[0]]))
    lower_c = np.concatenate((means - stds, [means[0] - stds[0]]))
    upper_c = np.concatenate((means + stds, [means[0] + stds[0]]))
    
    # Polar setup: North is zero, clockwise direction
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(r_lim)
    
    # Set radial labels offset at 13 degrees to avoid spokes
    ax.set_rgrids(r_ticks, angle=13, fontsize=8.8, color='#444444', zorder=2)
    ax.grid(True, color='#cccccc', linestyle='--', linewidth=0.75, alpha=0.75)
    
    # Shaded band (2D top-down)
    is_map50 = ('50' in metric_key and 'strict' not in metric_key)
    band_col = '#3498db' if is_map50 else '#9b59b6'
    line_col = '#1a5276' if is_map50 else '#6c3483'
    
    ax.fill_between(angles_c, lower_c, upper_c, color=band_col, 
                    alpha=0.22, label='± 1 STD Confidence Band', zorder=3)
    ax.plot(angles_c, means_c, color=line_col, linewidth=2.4, linestyle='-', zorder=4)
    
    # Plot spokes error bars & individual markers (strictly top-down 2D)
    for i, m in enumerate(MODELS_DATA):
        theta = angles[i]
        c = CAT_COLORS[m["cat"]]
        val = m[metric_key]
        s = m[std_key]
        
        # Radial line along spoke
        ax.plot([theta, theta], [val - s, val + s], color=c, linewidth=2.2, zorder=5)
        
        # Geometrically perpendicular end caps in polar coordinates:
        # A tangential bar at radius r spans [theta - d_theta, theta + d_theta]
        # where arc length ds = r * d_theta. We want a constant physical cap width (~0.65 units in data space)
        d_theta_top = 0.65 / max(val + s, 1.0)
        d_theta_bot = 0.65 / max(val - s, 1.0)
        
        cap_angles_top = np.linspace(theta - d_theta_top, theta + d_theta_top, 10)
        ax.plot(cap_angles_top, np.full_like(cap_angles_top, val + s), color=c, linewidth=1.6, zorder=6)
        
        cap_angles_bot = np.linspace(theta - d_theta_bot, theta + d_theta_bot, 10)
        ax.plot(cap_angles_bot, np.full_like(cap_angles_bot, val - s), color=c, linewidth=1.6, zorder=6)
        
        # Central marker point
        marker = 'o' if m["cat"] == 'CNN' else ('s' if m["cat"] == 'ViT' else ('D' if m["cat"] == 'Distilled' else 'p'))
        ax.scatter([theta], [val], color=c, edgecolor='black', linewidth=1.0, marker=marker, s=55, zorder=7)
        
        # Label text positioning outside the radar polygon
        label_r = r_lim[1] * r_offset_text
        deg = np.degrees(theta) % 360
        
        if 345 <= deg or deg <= 15:
            ha = 'center'
            va = 'bottom'
        elif 15 < deg < 165:
            ha = 'left'
            va = 'center'
        elif 165 <= deg <= 195:
            ha = 'center'
            va = 'top'
        else:
            ha = 'right'
            va = 'center'
            
        label_str = f"{m['short']}\n{val:.2f} ± {s:.2f}{unit}"
        ax.text(theta, label_r, label_str, fontsize=8.2, fontweight='semibold',
                ha=ha, va=va, color='#111111', zorder=8,
                bbox=dict(boxstyle='round,pad=0.18', facecolor='white', edgecolor='#e0e0e0', alpha=0.85))
    
    # Hide outer polar boundary spine
    ax.spines['polar'].set_visible(True)
    ax.spines['polar'].set_color('#aaaaaa')
    ax.spines['polar'].set_linewidth(1.0)
    ax.set_xticklabels([])


def generate_combined_figure():
    print("Generating Figure 11 (Combined 2-Panel Polar Radar Profiles)...")
    fig = plt.figure(figsize=(16.0, 9.5))
    
    # Grid layout with generous margins
    gs = fig.add_gridspec(1, 2, left=0.06, right=0.94, bottom=0.18, top=0.76, wspace=0.48)
    
    ax1 = fig.add_subplot(gs[0, 0], polar=True)
    draw_radar_subplot(ax1, "map50", "map50_std", r_lim=(35.0, 53.0), 
                       r_ticks=[38.0, 42.0, 46.0, 50.0], unit="%", r_offset_text=1.055)
    
    ax2 = fig.add_subplot(gs[0, 1], polar=True)
    draw_radar_subplot(ax2, "mapstrict", "mapstrict_std", r_lim=(16.0, 26.0), 
                       r_ticks=[18.0, 20.0, 22.0, 24.0], unit="%", r_offset_text=1.055)
    
    # Clean main title & panel titles
    fig.text(0.50, 0.94, "Cross-Architecture Polar Radar Profiles: Global Accuracy and Precision Envelopes",
             fontsize=14, fontweight='bold', ha='center', color='#111111')
    
    fig.text(0.26, 0.86, "(a) Benchmark Delineation Profile: Test mAP@50 [%]\n(Radial Spokes with ± 1 STD Error Bounds)", 
             fontsize=11, fontweight='bold', ha='center', color='#1a5276', linespacing=1.2)
    fig.text(0.74, 0.86, "(b) Strict Precision Profile: Test mAP(50-95) [%]\n(Radial Spokes with ± 1 STD Error Bounds)", 
             fontsize=11, fontweight='bold', ha='center', color='#6c3483', linespacing=1.2)
    
    # Shared Legend at bottom center
    legend_elements = [
        Line2D([0], [0], color='#1a5276', lw=2.4, label='Mean Metric Polygon (mAP@50)'),
        Line2D([0], [0], color='#6c3483', lw=2.4, label='Mean Metric Polygon (mAP(50-95))'),
        Patch(facecolor='#3498db', edgecolor='none', alpha=0.35, label='± 1 STD Confidence Envelope'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4', markersize=8, label='Pure CNN Models'),
        Line2D([0], [0], marker='s', color='w', markerfacecolor='#2ca02c', markersize=8, label='Vision Transformers'),
        Line2D([0], [0], marker='D', color='w', markerfacecolor='#ff7f0e', markersize=7, label='Distilled Student-Teacher Models'),
        Line2D([0], [0], marker='p', color='w', markerfacecolor='#9467bd', markersize=8, label='Multi-Scale Fused')
    ]
    fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.50, 0.04),
               ncol=4, framealpha=0.96, edgecolor='#cccccc', fontsize=9.2)
    
    save_all(fig, "thesis_fig11_isolated_radar_map50_map50_95.png")
    plt.close(fig)


def generate_standalone_map50():
    print("Generating Figure 11a (Standalone mAP@50 Radar Profile)...")
    fig = plt.figure(figsize=(9.8, 9.2))
    ax = fig.add_axes([0.10, 0.16, 0.80, 0.65], polar=True)
    
    draw_radar_subplot(ax, "map50", "map50_std", r_lim=(35.0, 53.0), 
                       r_ticks=[38.0, 42.0, 46.0, 50.0], unit="%", r_offset_text=1.07)
    
    fig.text(0.50, 0.94, "Polar Radar Profile: Cross-Architecture Test mAP@50 [%]",
             fontsize=13, fontweight='bold', ha='center')
    fig.text(0.50, 0.89, "Radial Spoke Profiles Across 14 Evaluated Configurations with ± 1 STD Dispersion Corridors",
             fontsize=10, style='italic', ha='center', color='#555555')
    
    legend_elements = [
        Line2D([0], [0], color='#1a5276', lw=2.4, label='Mean mAP@50 Polygon'),
        Patch(facecolor='#3498db', edgecolor='none', alpha=0.35, label='± 1 STD Empirical Confidence Ribbon'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4', markersize=8, label='Pure CNN Models'),
        Line2D([0], [0], marker='s', color='w', markerfacecolor='#2ca02c', markersize=8, label='Vision Transformers'),
        Line2D([0], [0], marker='D', color='w', markerfacecolor='#ff7f0e', markersize=7, label='Distilled Models'),
        Line2D([0], [0], marker='p', color='w', markerfacecolor='#9467bd', markersize=8, label='Multi-Scale Fused')
    ]
    fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.50, 0.04),
               ncol=3, framealpha=0.96, edgecolor='#cccccc', fontsize=9.2)
    
    save_all(fig, "thesis_fig11a_radar_map50.png")
    plt.close(fig)


def generate_standalone_map50_95():
    print("Generating Figure 11b (Standalone Strict mAP(50-95) Radar Profile)...")
    fig = plt.figure(figsize=(9.8, 9.2))
    ax = fig.add_axes([0.10, 0.16, 0.80, 0.65], polar=True)
    
    draw_radar_subplot(ax, "mapstrict", "mapstrict_std", r_lim=(16.0, 26.0), 
                       r_ticks=[18.0, 20.0, 22.0, 24.0], unit="%", r_offset_text=1.07)
    
    fig.text(0.50, 0.94, "Polar Radar Profile: Cross-Architecture Strict mAP(50-95) [%]",
             fontsize=13, fontweight='bold', ha='center')
    fig.text(0.50, 0.89, "Radial Spoke Profiles Across 14 Evaluated Configurations with ± 1 STD Dispersion Corridors",
             fontsize=10, style='italic', ha='center', color='#555555')
    
    legend_elements = [
        Line2D([0], [0], color='#6c3483', lw=2.4, label='Mean mAP(50-95) Polygon'),
        Patch(facecolor='#9b59b6', edgecolor='none', alpha=0.35, label='± 1 STD Empirical Confidence Ribbon'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4', markersize=8, label='Pure CNN Models'),
        Line2D([0], [0], marker='s', color='w', markerfacecolor='#2ca02c', markersize=8, label='Vision Transformers'),
        Line2D([0], [0], marker='D', color='w', markerfacecolor='#ff7f0e', markersize=7, label='Distilled Models'),
        Line2D([0], [0], marker='p', color='w', markerfacecolor='#9467bd', markersize=8, label='Multi-Scale Fused')
    ]
    fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.50, 0.04),
               ncol=3, framealpha=0.96, edgecolor='#cccccc', fontsize=9.2)
    
    save_all(fig, "thesis_fig11b_radar_map50_95.png")
    plt.close(fig)


if __name__ == '__main__':
    print("Executing publication-grade polar radar generation...")
    generate_combined_figure()
    generate_standalone_map50()
    generate_standalone_map50_95()
    print("Complete! All 3 radar figures successfully updated.")
