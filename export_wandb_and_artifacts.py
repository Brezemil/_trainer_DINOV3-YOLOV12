#!/usr/bin/env python3
"""
Export Training Artifacts and WandB Logs into export/ directory.
"""

import os
import sys
import json
import shutil
from pathlib import Path
import pandas as pd
import wandb

CURRENT_DIR = Path(__file__).parent.resolve()
EXPORT_DIR = CURRENT_DIR / "export"
BRAIN_DIR = Path(r"C:\Users\emil_brezovsky\.gemini\antigravity-cli\brain\9cd382f0-394b-4c1c-8528-c965fc283566")

RUNS = [
    {
        "seed": 42,
        "run_id": "ovdgoz21",
        "run_name": "yolo12s_triple_dino3_vitb16_seed_42",
        "baseline_dir": CURRENT_DIR / "_baseline" / "triple_dino3_vitb16_seed422",
        "wandb_local_dir": CURRENT_DIR / "wandb" / "run-20260827_234011-ovdgoz21",
    },
    {
        "seed": 100,
        "run_id": "p96dlaj5",
        "run_name": "yolo12s_triple_dino3_vitb16_seed_100",
        "baseline_dir": CURRENT_DIR / "_baseline" / "triple_dino3_vitb16_seed100",
        "wandb_local_dir": CURRENT_DIR / "wandb" / "run-20260831_020740-p96dlaj5",
    },
    {
        "seed": 999,
        "run_id": "ftxj3r9n",
        "run_name": "yolo12s_triple_dino3_vitb16_seed_999",
        "baseline_dir": CURRENT_DIR / "_baseline" / "triple_dino3_vitb16_seed999",
        "wandb_local_dir": CURRENT_DIR / "wandb" / "run-20260903_094414-ftxj3r9n",
    },
]


def export_artifacts():
    print("=" * 80)
    print("1. COPYING THESIS ARTIFACTS TO EXPORT FOLDER")
    print("=" * 80)

    # Copy markdown artifact from brain directory to export directory
    src_artifact = BRAIN_DIR / "f1_confidence_optimization_analysis.md"
    dest_artifact = EXPORT_DIR / "f1_confidence_optimization_analysis.md"
    if src_artifact.exists():
        shutil.copy2(src_artifact, dest_artifact)
        print(f"Copied {src_artifact} -> {dest_artifact}")
        
        # Also create export/artifacts/ folder for organization
        artifacts_dir = EXPORT_DIR / "artifacts"
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_artifact, artifacts_dir / "f1_confidence_optimization_analysis.md")
        print(f"Copied to {artifacts_dir / 'f1_confidence_optimization_analysis.md'}")
    else:
        print(f"Warning: {src_artifact} not found")

    print("\n" + "=" * 80)
    print("2. COPYING TRAINING RUN ARTIFACTS (CURVES, LOGS, CONFIGS)")
    print("=" * 80)

    training_artifacts_dir = EXPORT_DIR / "training_artifacts"
    training_artifacts_dir.mkdir(parents=True, exist_ok=True)

    artifact_patterns = [
        "*.png",
        "*.jpg",
        "results.csv",
        "args.yaml",
    ]

    for run in RUNS:
        seed = run["seed"]
        src_dir = run["baseline_dir"]
        dest_run_dir = training_artifacts_dir / f"seed_{seed}"
        dest_run_dir.mkdir(parents=True, exist_ok=True)

        copied_count = 0
        if src_dir.exists():
            for pat in artifact_patterns:
                for file_path in src_dir.glob(pat):
                    shutil.copy2(file_path, dest_run_dir / file_path.name)
                    copied_count += 1
            print(f"Seed {seed}: Copied {copied_count} files from {src_dir.name} -> {dest_run_dir.relative_to(CURRENT_DIR)}")
        else:
            print(f"Warning: Source directory {src_dir} does not exist")


def export_wandb_logs():
    print("\n" + "=" * 80)
    print("3. EXPORTING WANDB LOGS, HISTORY, AND ENRICHING LOSS METRICS")
    print("=" * 80)

    wandb_export_dir = EXPORT_DIR / "wandb_logs"
    wandb_export_dir.mkdir(parents=True, exist_ok=True)
    metric_histories_dir = wandb_export_dir / "metric_histories"
    metric_histories_dir.mkdir(parents=True, exist_ok=True)
    aborted_dir = wandb_export_dir / "aborted_test_runs"
    aborted_dir.mkdir(parents=True, exist_ok=True)
    training_artifacts_dir = EXPORT_DIR / "training_artifacts"

    api = wandb.Api()
    overview_runs = []
    summary_rows = []

    for run in RUNS:
        seed = run["seed"]
        run_id = run["run_id"]
        run_name = run["run_name"]
        local_dir = run["wandb_local_dir"]
        dest_run_dir = wandb_export_dir / f"seed_{seed}_{run_id}"
        dest_run_dir.mkdir(parents=True, exist_ok=True)

        print(f"\nProcessing W&B run {run_name} (ID: {run_id})...")

        # 1. Copy local wandb files (output.log, config.yaml, metadata, summary, media)
        if local_dir.exists():
            local_files_dir = local_dir / "files"
            if local_files_dir.exists():
                for f in local_files_dir.iterdir():
                    if f.is_file():
                        shutil.copy2(f, dest_run_dir / f.name)
                        print(f"  Copied local file: {f.name}")
                local_media = local_files_dir / "media"
                dest_media = dest_run_dir / "media"
                if local_media.exists() and not dest_media.exists():
                    shutil.copytree(local_media, dest_media)
                    print(f"  Copied media/ folder recursively")

            local_logs_dir = local_dir / "logs"
            if local_logs_dir.exists():
                for f in local_logs_dir.iterdir():
                    if f.is_file():
                        shutil.copy2(f, dest_run_dir / f.name)
                        print(f"  Copied local log: {f.name}")

        # 2. Fetch full history and metadata from WandB API
        try:
            wandb_run = api.run(f"brezo-boku-vienna/_baseline/{run_id}")
            print(f"  Connected to W&B API: {wandb_run.name} ({wandb_run.state})")

            # Fetch complete metric history (all epochs)
            history_df = wandb_run.history(samples=2000)

            # Compute Total Train and Val Losses and alias columns
            if "train/box_loss" in history_df.columns:
                history_df["train/loss"] = history_df["train/box_loss"] + history_df["train/cls_loss"] + history_df["train/dfl_loss"]
                history_df["val/loss"] = history_df["val/box_loss"] + history_df["val/cls_loss"] + history_df["val/dfl_loss"]
                history_df["train_loss"] = history_df["train/loss"]
                history_df["val_loss"] = history_df["val/loss"]
                history_df["train_box_loss"] = history_df["train/box_loss"]
                history_df["train_cls_loss"] = history_df["train/cls_loss"]
                history_df["train_dfl_loss"] = history_df["train/dfl_loss"]
                history_df["val_box_loss"] = history_df["val/box_loss"]
                history_df["val_cls_loss"] = history_df["val/cls_loss"]
                history_df["val_dfl_loss"] = history_df["val/dfl_loss"]

            history_csv = dest_run_dir / "wandb_history.csv"
            history_df.to_csv(history_csv, index=False)
            print(f"  Saved enriched W&B history ({len(history_df)} steps) with train/loss and val/loss to {history_csv.name}")

            history_json = dest_run_dir / "wandb_history.json"
            history_df.to_json(history_json, orient="records", indent=4)
            print(f"  Saved W&B history JSON to {history_json.name}")

            # Save standardized history copy to metric_histories/
            std_history_file = metric_histories_dir / f"{run_name}_{run_id}_history.csv"
            history_df.to_csv(std_history_file, index=False)

            # Also ensure results.csv has train/loss and val/loss
            results_csv_path = training_artifacts_dir / f"seed_{seed}" / "results.csv"
            if results_csv_path.exists():
                df_res = pd.read_csv(results_csv_path)
                df_res.columns = [c.strip() for c in df_res.columns]
                if "train/box_loss" in df_res.columns and "train/loss" not in df_res.columns:
                    df_res["train/loss"] = df_res["train/box_loss"] + df_res["train/cls_loss"] + df_res["train/dfl_loss"]
                    df_res["val/loss"] = df_res["val/box_loss"] + df_res["val/cls_loss"] + df_res["val/dfl_loss"]
                    df_res["train_loss"] = df_res["train/loss"]
                    df_res["val_loss"] = df_res["val/loss"]
                    df_res.to_csv(results_csv_path, index=False)

            final_train_loss = float(history_df["train/loss"].iloc[-1]) if "train/loss" in history_df.columns else None
            final_val_loss = float(history_df["val/loss"].iloc[-1]) if "val/loss" in history_df.columns else None
            best_val_loss = float(history_df["val/loss"].min()) if "val/loss" in history_df.columns else None
            best_val_loss_epoch = int(history_df["val/loss"].idxmin() + 1) if "val/loss" in history_df.columns else None

            # Update wandb-summary.json
            summary_path = dest_run_dir / "wandb-summary.json"
            summary_dict = dict(wandb_run.summary)
            if final_train_loss is not None:
                summary_dict["train/loss"] = final_train_loss
                summary_dict["val/loss"] = final_val_loss
                summary_dict["train_loss"] = final_train_loss
                summary_dict["val_loss"] = final_val_loss
                summary_dict["best_val/loss"] = best_val_loss
                summary_dict["best_val_loss_epoch"] = best_val_loss_epoch
            with open(summary_path, "w") as f:
                json.dump(summary_dict, f, indent=4)

            # Save detailed run info
            run_info = {
                "id": wandb_run.id,
                "name": wandb_run.name,
                "url": wandb_run.url,
                "state": wandb_run.state,
                "created_at": wandb_run.created_at,
                "tags": wandb_run.tags,
                "notes": wandb_run.notes,
                "config": dict(wandb_run.config),
                "summary": summary_dict,
            }
            run_info_file = dest_run_dir / "wandb_run_info.json"
            with open(run_info_file, "w") as f:
                json.dump(run_info, f, indent=4, default=str)
            print(f"  Saved W&B run info to {run_info_file.name}")

            overview_runs.append({
                "seed": seed,
                "run_id": run_id,
                "name": wandb_run.name,
                "url": wandb_run.url,
                "state": wandb_run.state,
                "epochs_logged": len(history_df),
                "tags": wandb_run.tags,
                "summary_metrics": {
                    "mAP50": wandb_run.summary.get("metrics/mAP50(B)"),
                    "mAP50_95": wandb_run.summary.get("metrics/mAP50-95(B)"),
                    "precision": wandb_run.summary.get("metrics/precision(B)"),
                    "recall": wandb_run.summary.get("metrics/recall(B)"),
                    "train_loss": final_train_loss,
                    "val_loss": final_val_loss,
                    "train_box_loss": float(history_df["train/box_loss"].iloc[-1]),
                    "train_cls_loss": float(history_df["train/cls_loss"].iloc[-1]),
                    "train_dfl_loss": float(history_df["train/dfl_loss"].iloc[-1]),
                    "val_box_loss": float(history_df["val/box_loss"].iloc[-1]),
                    "val_cls_loss": float(history_df["val/cls_loss"].iloc[-1]),
                    "val_dfl_loss": float(history_df["val/dfl_loss"].iloc[-1]),
                    "best_val_loss": best_val_loss,
                    "best_val_loss_epoch": best_val_loss_epoch,
                }
            })

            summary_rows.append({
                "run_id": run_id,
                "run_name": run_name,
                "seed": seed,
                "state": wandb_run.state,
                "epochs": len(history_df),
                "url": wandb_run.url,
                "mAP50": wandb_run.summary.get("metrics/mAP50(B)"),
                "mAP50_95": wandb_run.summary.get("metrics/mAP50-95(B)"),
                "precision": wandb_run.summary.get("metrics/precision(B)"),
                "recall": wandb_run.summary.get("metrics/recall(B)"),
                "final_train_loss": final_train_loss,
                "final_val_loss": final_val_loss,
                "best_val_loss": best_val_loss,
                "best_val_loss_epoch": best_val_loss_epoch,
                "train_box_loss": float(history_df["train/box_loss"].iloc[-1]),
                "train_cls_loss": float(history_df["train/cls_loss"].iloc[-1]),
                "train_dfl_loss": float(history_df["train/dfl_loss"].iloc[-1]),
                "val_box_loss": float(history_df["val/box_loss"].iloc[-1]),
                "val_cls_loss": float(history_df["val/cls_loss"].iloc[-1]),
                "val_dfl_loss": float(history_df["val/dfl_loss"].iloc[-1]),
                "batch_size": 4,
                "imgsz": 1024,
                "optimizer": "SGD",
                "lr0": 0.01,
            })
        except Exception as e:
            print(f"  Error querying WandB API: {e}")

    # Save overview file
    overview_file = wandb_export_dir / "wandb_runs_overview.json"
    with open(overview_file, "w") as f:
        json.dump({
            "project": "https://wandb.ai/brezo-boku-vienna/_baseline?nw=nwuserbrezo",
            "model_architecture": "yolo12s_triple_dino3_vitb16",
            "runs": overview_runs
        }, f, indent=4)
    print(f"\nSaved master W&B overview to {overview_file.relative_to(CURRENT_DIR)}")

    # Save runs_summary.csv and runs_summary.json
    if summary_rows:
        summary_df = pd.DataFrame(summary_rows)
        runs_summary_csv = wandb_export_dir / "runs_summary.csv"
        summary_df.to_csv(runs_summary_csv, index=False)
        print(f"Saved runs summary CSV to {runs_summary_csv.relative_to(CURRENT_DIR)}")

        runs_summary_json = wandb_export_dir / "runs_summary.json"
        summary_df.to_json(runs_summary_json, orient="records", indent=4)
        print(f"Saved runs summary JSON to {runs_summary_json.relative_to(CURRENT_DIR)}")

    # Archive local aborted runs
    aborted_runs = [
        ("run-20260827_231542-w74twqoh", "w74twqoh", "Aborted epoch 1 batch 4 (batch_size=4, workers=8)"),
        ("run-20260827_232048-pa4nxsul", "pa4nxsul", "Aborted epoch 1 batch 4 (batch_size=8, workers=8)"),
        ("run-20260827_232529-h9h0frsv", "h9h0frsv", "Aborted epoch 1 batch 4 (batch_size=4, workers=8)"),
        ("run-20260827_233639-z55wlb4g", "z55wlb4g", "Aborted epoch 1 batch 4 (batch_size=8, workers=4)"),
    ]
    for run_folder, run_id, note in aborted_runs:
        src_dir = CURRENT_DIR / "wandb" / run_folder
        dest_dir = aborted_dir / run_folder
        if src_dir.exists() and not dest_dir.exists():
            shutil.copytree(src_dir, dest_dir, ignore=shutil.ignore_patterns("*.wandb*"))
            with open(dest_dir / "run_status.json", "w") as f:
                json.dump({"run_id": run_id, "state": "aborted", "note": note}, f, indent=4)
            print(f"Archived aborted run: {run_folder}")


if __name__ == "__main__":
    export_artifacts()
    export_wandb_logs()
    print("\n" + "=" * 80)
    print("ALL ARTIFACTS AND WANDB LOGS EXPORTED SUCCESSFULLY!")
    print("=" * 80)
