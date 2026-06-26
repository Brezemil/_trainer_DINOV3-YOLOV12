#!/usr/bin/env python3
"""
plot_results.py - Aggregation & Plotting Script for YOLOv12-DINO3 benchmark results.

This script reads all *_coco_metrics.json files in the results directory,
groups them by model type (stripping seed suffixes), calculates Mean ± SD,
generates publication-quality charts, and writes out a summary markdown table.
"""

import argparse
import json
import re
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def parse_args():
    parser = argparse.ArgumentParser(description="Aggregate and Plot COCO evaluation results")
    parser.add_argument("--results-dir", type=str, default="results", help="Directory containing metric JSON files")
    parser.add_argument("--output-dir", type=str, default="results", help="Directory to save generated plots")
    return parser.parse_args()


def clean_model_name(file_stem):
    """
    Strips '_seed_X' or similar suffixes to group by model variant.
    e.g., 'yolov12s_dino3_vitl16_sat493m_seed_42' -> 'yolov12s_dino3_vitl16_sat493m'
    """
    # Remove _seed_ followed by numbers, or _seed_ followed by any text, or trailing _seed
    name = re.sub(r"_seed_\d+$", "", file_stem)
    name = re.sub(r"_seed_[a-zA-Z0-9]+$", "", name)
    name = name.replace("_coco_metrics", "")
    return name


def main():
    args = parse_args()
    results_path = Path(args.results_dir)
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not results_path.exists():
        print(f"[ERROR] Results directory not found: {results_path}")
        return

    # Find all metrics files
    metric_files = list(results_path.glob("*_coco_metrics.json"))
    if not metric_files:
        print(f"[ERROR] No metrics files found (*_coco_metrics.json) in {results_path}")
        return

    print(f"[INFO] Found {len(metric_files)} evaluation runs. Parsing...")

    individual_runs = []

    for mf in metric_files:
        try:
            with open(mf, "r") as f:
                metrics = json.load(f)

            stem = mf.stem
            model_variant = clean_model_name(stem)

            # Find seed if possible
            seed_match = re.search(r"_seed_(\d+)", stem)
            seed = int(seed_match.group(1)) if seed_match else "unknown"

            run_data = {
                "RunName": stem,
                "ModelVariant": model_variant,
                "Seed": seed,
            }
            run_data.update(metrics)
            individual_runs.append(run_data)
        except Exception as e:
            print(f"   [WARNING] Could not parse file {mf.name}: {e}")

    df_runs = pd.DataFrame(individual_runs)

    # Save the aggregated individual runs for reference
    df_runs.to_csv(output_path / "aggregated_runs.csv", index=False)

    # Group by ModelVariant and calculate Mean and Std Dev
    grouped = df_runs.groupby("ModelVariant")

    summary_data = []

    # The 12 standard COCO metrics
    metrics_to_agg = [
        "mAP_50_95",
        "mAP_50",
        "mAP_75",
        "AP_small",
        "AP_medium",
        "AP_large",
        "AR_1",
        "AR_10",
        "AR_100",
        "AR_small",
        "AR_medium",
        "AR_large",
    ]

    for model_name, group in grouped:
        model_summary = {"Model Variant": model_name, "Runs": len(group)}
        for metric in metrics_to_agg:
            if metric in group.columns:
                mean_val = float(group[metric].mean())
                raw_std = group[metric].std()
                std_val = 0.0 if bool(pd.isna(raw_std)) else float(raw_std)
                model_summary[f"{metric}_mean"] = mean_val
                model_summary[f"{metric}_std"] = std_val
        summary_data.append(model_summary)

    df_summary = pd.DataFrame(summary_data)
    df_summary.to_csv(output_path / "summary_metrics.csv", index=False)

    print("[SUCCESS] Successfully aggregated metrics.")

    # Apply publication-quality styling
    sns.set_theme(style="whitegrid", context="talk")
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "figure.titlesize": 18,
            "axes.titlesize": 16,
            "axes.labelsize": 14,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "legend.fontsize": 12,
            "savefig.dpi": 300,
        }
    )

    # Pre-select a clean, professional palette
    palette = sns.color_palette("muted")
    sns.set_palette(palette)

    # =========================================================================
    # Plot 1: AP comparison plot (ap_metrics_comparison.png)
    # =========================================================================
    print("[INFO] Generating AP metrics comparison plot...")
    fig, ax = plt.subplots(figsize=(10, 6))

    ap_metrics = ["mAP_50_95", "mAP_50", "mAP_75"]
    plot_data = []

    for metric in ap_metrics:
        for idx, row in df_summary.iterrows():
            plot_data.append(
                {
                    "Metric": metric.replace("mAP_50_95", "mAP@0.50:0.95")
                    .replace("mAP_50", "mAP@0.50")
                    .replace("mAP_75", "mAP@0.75"),
                    "Model Variant": row["Model Variant"],
                    "Value": row[f"{metric}_mean"],
                    "Error": row[f"{metric}_std"],
                }
            )

    df_plot_ap = pd.DataFrame(plot_data)

    # We use manual matplotlib plotting with error bars for precise control
    variants = df_summary["Model Variant"].unique()
    x_indices = np.arange(len(ap_metrics))
    width = 0.8 / len(variants)

    for i, variant in enumerate(variants):
        variant_data = df_plot_ap[df_plot_ap["Model Variant"] == variant]
        means = list(variant_data["Value"])
        errors = list(variant_data["Error"])
        ax.bar(
            x_indices + i * width - (len(variants) - 1) * width / 2,
            means,
            width,
            yerr=errors,
            label=variant,
            capsize=5,
            edgecolor="black",
            alpha=0.85,
        )

    ax.set_ylabel("AP Score")
    ax.set_title("Average Precision (AP) Metrics Comparison")
    ax.set_xticks(x_indices)
    ax.set_xticklabels(["mAP@0.50:0.95", "mAP@0.50", "mAP@0.75"])
    ax.legend(title="Model Variant", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(output_path / "ap_metrics_comparison.png", bbox_inches="tight")
    plt.close()

    # =========================================================================
    # Plot 2: Scale-wise AP plot (ap_scale_comparison.png)
    # =========================================================================
    print("[INFO] Generating scale-wise AP plot...")
    fig, ax = plt.subplots(figsize=(10, 6))

    scale_metrics = ["AP_small", "AP_medium", "AP_large"]
    plot_data_scale = []

    for metric in scale_metrics:
        for idx, row in df_summary.iterrows():
            plot_data_scale.append(
                {
                    "Metric": metric.replace("AP_", "AP "),
                    "Model Variant": row["Model Variant"],
                    "Value": row[f"{metric}_mean"],
                    "Error": row[f"{metric}_std"],
                }
            )

    df_plot_scale = pd.DataFrame(plot_data_scale)

    for i, variant in enumerate(variants):
        variant_data = df_plot_scale[df_plot_scale["Model Variant"] == variant]
        means = list(variant_data["Value"])
        errors = list(variant_data["Error"])
        ax.bar(
            x_indices + i * width - (len(variants) - 1) * width / 2,
            means,
            width,
            yerr=errors,
            label=variant,
            capsize=5,
            edgecolor="black",
            alpha=0.85,
        )

    ax.set_ylabel("AP Score")
    ax.set_title("Scale-wise Detection Performance (AP)")
    ax.set_xticks(x_indices)
    ax.set_xticklabels(["AP Small", "AP Medium", "AP Large"])
    ax.legend(title="Model Variant", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(output_path / "ap_scale_comparison.png", bbox_inches="tight")
    plt.close()

    # =========================================================================
    # Plot 3: Recall comparison plot (ar_metrics_comparison.png)
    # =========================================================================
    print("[INFO] Generating recall comparison plot...")
    fig, ax = plt.subplots(figsize=(10, 6))

    ar_metrics = ["AR_1", "AR_10", "AR_100"]
    plot_data_ar = []

    for metric in ar_metrics:
        for idx, row in df_summary.iterrows():
            plot_data_ar.append(
                {
                    "Metric": metric.replace("AR_", "AR@"),
                    "Model Variant": row["Model Variant"],
                    "Value": row[f"{metric}_mean"],
                    "Error": row[f"{metric}_std"],
                }
            )

    df_plot_ar = pd.DataFrame(plot_data_ar)

    for i, variant in enumerate(variants):
        variant_data = df_plot_ar[df_plot_ar["Model Variant"] == variant]
        means = list(variant_data["Value"])
        errors = list(variant_data["Error"])
        ax.bar(
            x_indices + i * width - (len(variants) - 1) * width / 2,
            means,
            width,
            yerr=errors,
            label=variant,
            capsize=5,
            edgecolor="black",
            alpha=0.85,
        )

    ax.set_ylabel("Recall Score")
    ax.set_title("Average Recall (AR) Metrics Comparison")
    ax.set_xticks(x_indices)
    ax.set_xticklabels(["AR@1", "AR@10", "AR@100"])
    ax.legend(title="Model Variant", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(output_path / "ar_metrics_comparison.png", bbox_inches="tight")
    plt.close()

    # =========================================================================
    # Plot 4: Seed spread distribution (ap_seed_distribution.png)
    # =========================================================================
    print("[INFO] Generating seed spread distribution plot...")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Strip plot (jittered scatter points) overlaying a box/violin plot
    sns.boxplot(
        x="ModelVariant", y="mAP_50_95", data=df_runs, ax=ax, whis=np.inf, color="0.9", width=0.4, showfliers=False
    )

    # Overlay the individual points
    sns.stripplot(
        x="ModelVariant",
        y="mAP_50_95",
        data=df_runs,
        ax=ax,
        size=10,
        jitter=0.15,
        palette="Set2",
        linewidth=1,
        edgecolor="gray",
    )

    ax.set_xlabel("Model Variant")
    ax.set_ylabel("mAP @ 0.50:0.95")
    ax.set_title("Seed Spread and Model Stability (mAP)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(output_path / "ap_seed_distribution.png", bbox_inches="tight")
    plt.close()

    # =========================================================================
    # Generate Markdown Summary Table
    # =========================================================================
    print("[INFO] Generating markdown summary table...")

    md_lines = []
    md_lines.append("# Model Performance Benchmark Summary")
    md_lines.append("")
    md_lines.append(
        "This document summarizes the performance evaluation results across seeds (Mean ± Standard Deviation)."
    )
    md_lines.append("")
    md_lines.append(
        "| Model Variant | Runs | mAP@0.50:0.95 | mAP@0.50 | mAP@0.75 | AP (Small) | AP (Medium) | AP (Large) | AR@100 |"
    )
    md_lines.append("| :--- | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    for idx, row in df_summary.iterrows():
        name = row["Model Variant"]
        runs = int(row["Runs"])

        m_ap_50_95 = f"{row['mAP_50_95_mean']:.4f} ± {row['mAP_50_95_std']:.4f}"
        m_ap_50 = f"{row['mAP_50_mean']:.4f} ± {row['mAP_50_std']:.4f}"
        m_ap_75 = f"{row['mAP_75_mean']:.4f} ± {row['mAP_75_std']:.4f}"
        ap_s = f"{row['AP_small_mean']:.4f} ± {row['AP_small_std']:.4f}"
        ap_m = f"{row['AP_medium_mean']:.4f} ± {row['AP_medium_std']:.4f}"
        ap_l = f"{row['AP_large_mean']:.4f} ± {row['AP_large_std']:.4f}"
        ar_100 = f"{row['AR_100_mean']:.4f} ± {row['AR_100_std']:.4f}"

        md_lines.append(
            f"| {name} | {runs} | {m_ap_50_95} | {m_ap_50} | {m_ap_75} | {ap_s} | {ap_m} | {ap_l} | {ar_100} |"
        )

    md_text = "\n".join(md_lines)

    # Save markdown summary table
    with open(output_path / "benchmark_summary.md", "w") as f:
        f.write(md_text)

    print("\n" + "=" * 60)
    print("BENCHMARK SUMMARY TABLE:")
    print("=" * 60)
    for line in md_lines[4:]:
        print(line)
    print("=" * 60)
    print(f"[SUCCESS] Generated report tables and images in: {output_path.resolve()}")


if __name__ == "__main__":
    main()
