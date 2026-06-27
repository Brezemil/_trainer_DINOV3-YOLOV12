#!/usr/bin/env python3
"""
config.py - Unified Configuration for YOLOv12-DINO3 Benchmarking.

This module provides a single source of truth configuration dataclass containing
W&B settings, datasets paths, model lists, seed lists, and training hyperparameters.
It also includes a utility method to query the W&B API for the best sweep configuration.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class BenchmarkConfig:
    # W&B Configuration
    wandb_entity: str = "emilb"
    wandb_project: str = "trainer_DINOV3-YOLOV12"
    wandb_dir: str = "runs/wandb"

    # Benchmarking constraints
    seeds: List[int] = field(default_factory=lambda: [42, 100, 999])
    model_variants: List[str] = field(default_factory=lambda: ["vits16", "vitb16", "vitl16", "vitl16_sat493m"])
    dataset_yaml: str = "C:/Users/emilb/_data/_smoketest/dataset.yaml"
    results_dir: str = "results/benchmark"

    # Global training constraints
    imgsz: int = 1280
    batch_size: int = 16
    epochs_sweep: int = 50
    epochs_production: int = 100
    device: str = "0"
    workers: int = 8
    fraction: float = 1.0  # Dataset fraction for training/validation (set < 1.0 for smoketests)

    @staticmethod
    def get_best_sweep_config(sweep_path: str, metric: str = "metrics/mAP50-95(B)") -> Dict[str, Any]:
        """
        Retrieves the configuration of the best run from a finished W&B sweep using the W&B API.

        Args:
            sweep_path (str): The sweep identifier in format "entity/project/sweep_id"
            metric (str): The metric name to sort by (default: "metrics/mAP50-95(B)")

        Returns:
            dict: The configuration dictionary of the best run
        """
        print(f"[INFO] Connecting to W&B API to fetch sweep: {sweep_path}")
        try:
            import wandb

            api = wandb.Api()

            # Retrieve the sweep object
            sweep = api.sweep(sweep_path)
            runs = sweep.runs

            if not runs:
                raise ValueError(f"No runs found in sweep: {sweep_path}")

            print(f"[INFO] Found {len(runs)} runs in sweep. Sorting by metric: {metric} (descending)")

            best_run = None
            best_val = -float("inf")

            # Strip prefixes if any to find the metric key
            metric_base = metric.split("/")[-1]

            for run in runs:
                if run.state != "finished":
                    continue

                # Search run summary for the target metric
                val = None
                for key in [metric, metric_base]:
                    if key in run.summary:
                        val = run.summary[key]
                        break

                if val is not None:
                    try:
                        val_float = float(val)
                        if val_float > best_val:
                            best_val = val_float
                            best_run = run
                    except ValueError:
                        continue

            if best_run is None:
                # If no run was finished or had the metric, fallback to sorting first run
                print("[WARNING] Could not find the metric in run summaries. Using the first run.")
                best_run = runs[0]

            print(f"[SUCCESS] Best run found: {best_run.name} (ID: {best_run.id})")
            print(f"          Value for {metric}: {best_val}")

            return best_run.config

        except ImportError:
            print("[ERROR] wandb library is required to retrieve sweep config. Install it using the Pixi environment.")
            return {}
        except Exception as e:
            print(f"[ERROR] Failed to fetch sweep configuration: {e}")
            return {}


if __name__ == "__main__":
    # Test configuration printout
    config = BenchmarkConfig()
    print("=" * 60)
    print("[INFO] UNIFIED CONFIGURATION REFERENCE")
    print("=" * 60)
    print(f"Dataset config:      {config.dataset_yaml}")
    print(f"Model variants:      {config.model_variants}")
    print(f"Benchmark seeds:     {config.seeds}")
    print(f"Batch Size/Img size: {config.batch_size} / {config.imgsz}")
    print(f"Dataset Fraction:    {config.fraction} (smoketest if < 1.0)")
    print(f"Training Epochs:     {config.epochs_production} (Production), {config.epochs_sweep} (Sweep)")
    print("=" * 60)
