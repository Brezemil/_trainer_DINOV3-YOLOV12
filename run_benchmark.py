#!/usr/bin/env python3
"""
run_benchmark.py - Orchestrator script for YOLOv12-DINO3 Benchmarking.

This script automates running the benchmark for YOLOv12s with standard DINOv3 ViT-L (vitl16)
versus YOLOv12s with DINOv3 ViT-L Satellite (vitl16_sat493m) across multiple seeds.
It supports a preliminary smoketest (fraction of dataset, few epochs) and coordinates
training, strict COCO evaluation, and results aggregation/plotting.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from config import BenchmarkConfig


def run_command(cmd, env=None):
    """Run a system command and print output in real-time."""
    print(f"\n[EXEC] {' '.join(cmd)}")

    # Merge existing environment variables
    run_env = os.environ.copy()
    if env:
        run_env.update(env)

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, env=run_env)

    assert process.stdout is not None, "Subprocess stdout was not piped"

    # Read output line by line
    while True:
        line = process.stdout.readline()
        if not line and process.poll() is not None:
            break
        if line:
            sys.stdout.write(line)
            sys.stdout.flush()

    return_code = process.poll()
    if return_code != 0:
        print(f"[ERROR] Command failed with exit code: {return_code}")
    return return_code == 0


def main():
    parser = argparse.ArgumentParser(description="YOLOv12-DINO3 Benchmark Orchestrator")
    parser.add_argument("--data", type=str, default=None, help="Path to dataset YAML file (default: from config.py)")
    parser.add_argument(
        "--fraction", type=float, default=None, help="Dataset fraction to use for training/eval (0.0 to 1.0)"
    )
    parser.add_argument("--epochs", type=int, default=None, help="Number of training epochs (overrides config)")
    parser.add_argument("--batch-size", type=int, default=None, help="Batch size for training")
    parser.add_argument("--device", type=str, default=None, help="CUDA device or 'cpu'")
    parser.add_argument("--split", type=str, default="val", help="Dataset split for evaluation (default: val)")
    parser.add_argument("--smoketest", action="store_true", help="Quick test run (sets fraction=0.05, epochs=2)")

    args = parser.parse_args()

    # Load unified configurations
    cfg = BenchmarkConfig()

    # Override config values with CLI args if provided
    dataset_yaml = args.data if args.data is not None else cfg.dataset_yaml
    device = args.device if args.device is not None else cfg.device
    batch_size = args.batch_size if args.batch_size is not None else cfg.batch_size
    split = args.split

    # Determine fraction and epochs based on smoketest flag or CLI inputs
    if args.smoketest:
        fraction = 0.05
        epochs = 2
        print("[INFO] Smoketest mode activated! Setting fraction=0.05 and epochs=2 for rapid validation.")
    else:
        fraction = args.fraction if args.fraction is not None else cfg.fraction
        epochs = args.epochs if args.epochs is not None else cfg.epochs_production

    print("=" * 70)
    print("🚀 YOLOv12-DINO3 BENCHMARK ORCHESTRATOR STARTED")
    print("=" * 70)
    print(f"Dataset config:      {dataset_yaml}")
    print(f"Dataset fraction:    {fraction}")
    print(f"Epochs per run:      {epochs}")
    print(f"Batch size:          {batch_size}")
    print(f"Device:              {device}")
    print(f"Evaluation split:    {split}")
    print(f"Target seeds:        {cfg.seeds}")
    print("Model variants:      ['vitl16', 'vitl16_sat493m']")
    print("=" * 70)

    # Define models to compare (Standard vs. Satellite pretrained ViT-L)
    variants = ["vitl16", "vitl16_sat493m"]

    # Setup W&B environment variables to force unified project configurations
    wandb_env = {
        "WANDB_ENTITY": cfg.wandb_entity,
        "WANDB_PROJECT": cfg.wandb_project,
        "WANDB_DIR": cfg.wandb_dir,
    }

    # Create required directories
    os.makedirs(cfg.results_dir, exist_ok=True)
    os.makedirs(cfg.wandb_dir, exist_ok=True)

    success_count = 0
    failed_runs = []

    # Run the benchmarking pipeline
    for variant in variants:
        variant_display = "DINOv3-Web (vitl16)" if variant == "vitl16" else "DINOv3-Sat (vitl16_sat493m)"
        for seed in cfg.seeds:
            run_name = f"yolov12s_dino3_{variant}_seed_{seed}"
            if fraction < 1.0:
                run_name += f"_frac_{fraction}"

            print("\n" + "#" * 70)
            print(f"👉 RUNNING: {variant_display} | Seed: {seed} | Run Name: {run_name}")
            print("#" * 70)

            # --- 1. TRAINING PHASE ---
            train_cmd = [
                sys.executable,
                "train_yolov12_dino.py",
                "--data",
                dataset_yaml,
                "--yolo-size",
                "s",
                "--dinoversion",
                "3",
                "--dino-variant",
                variant,
                "--integration",
                "single",
                "--epochs",
                str(epochs),
                "--batch-size",
                str(batch_size),
                "--device",
                device,
                "--seed",
                str(seed),
                "--name",
                run_name,
                "--fraction",
                str(fraction),
            ]

            train_ok = run_command(train_cmd, env=wandb_env)
            if not train_ok:
                print(f"[WARNING] Training failed for {run_name}. Skipping evaluation.")
                failed_runs.append((run_name, "training"))
                continue

            # Path to the best model checkpoint
            model_path = Path("runs") / "detect" / run_name / "weights" / "best.pt"
            if not model_path.exists():
                # Fallback check if project output structure is slightly different
                model_path = Path("runs") / "detect" / f"{run_name}" / "weights" / "best.pt"
                if not model_path.exists():
                    print(f"[WARNING] Best checkpoint not found at: {model_path}. Skipping evaluation.")
                    failed_runs.append((run_name, "checkpoint_missing"))
                    continue

            # --- 2. EVALUATION PHASE (Strict COCOeval) ---
            eval_cmd = [
                sys.executable,
                "coco_evaluate.py",
                "--model",
                str(model_path),
                "--data",
                dataset_yaml,
                "--split",
                split,
                "--fraction",
                str(fraction),
                "--name",
                run_name,
                "--device",
                device,
                "--output-dir",
                cfg.results_dir,
            ]

            eval_ok = run_command(eval_cmd)
            if not eval_ok:
                print(f"[WARNING] Evaluation failed for {run_name}.")
                failed_runs.append((run_name, "evaluation"))
            else:
                success_count += 1

    # --- 3. AGGREGATION & PLOTTING ---
    print("\n" + "=" * 70)
    print("📊 AGGREGATING RESULTS & GENERATING COMPARISONS")
    print("=" * 70)

    plot_cmd = [sys.executable, "plot_results.py", "--results-dir", cfg.results_dir, "--output-dir", cfg.results_dir]

    plot_ok = run_command(plot_cmd)

    print("\n" + "=" * 70)
    print("🏁 BENCHMARK COMPLETE SUMMARY")
    print("=" * 70)
    print("Total planned runs: 6 (2 variants x 3 seeds)")
    print(f"Successful runs:    {success_count}")
    print(f"Failed runs:        {len(failed_runs)}")

    if failed_runs:
        print("\nFailed runs list:")
        for name, stage in failed_runs:
            print(f" - {name} ({stage} stage)")

    if plot_ok:
        print(f"\n[SUCCESS] Aggregated metrics and comparison figures generated in: {Path(cfg.results_dir).resolve()}")
        print(f"          Summary table written to: {Path(cfg.results_dir) / 'benchmark_summary.md'}")
    else:
        print("\n[ERROR] Plotting/aggregation execution failed.")

    print("=" * 70)


if __name__ == "__main__":
    main()
