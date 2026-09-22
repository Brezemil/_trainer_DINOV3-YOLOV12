# -*- coding: utf-8 -*-
"""
Extract Empirical Loss Curves & Compute Overfitting Index (OI) for Master's Thesis
Author: Emil Brezovsky
Target: Evaluates native and distilled YOLO12s and DINOv3 ViT-T models across Seeds {42, 100, 999}
        Saves clean JSON data for Figure 3 generation.
"""

import os
import json
import numpy as np
import pandas as pd

BASE_DIR = r"C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly"
WANDB_DIR = os.path.join(BASE_DIR, "wandb", "metric_histories")

OUTPUT_DESTINATIONS = [
    r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\thesis_evaluation\oi_curves_data.json",
    r"C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D\oi_curves_data.json",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363\scratch\oi_curves_data.json",
    r"C:\Users\emilb\.gemini\antigravity-cli\brain\38cddf38-ece2-4ab7-82f4-fff268c4d363\oi_curves_data.json"
]

def extract_yolo_curves():
    configs = {
        "YOLO12s": [
            os.path.join(BASE_DIR, "evaluations", "run_reports", f"yolo12s_seed_{s}", "results.csv")
            for s in [42, 100, 999]
        ],
        "YOLO12s (SAT-493M)": [
            os.path.join(BASE_DIR, "evaluations", "run_reports", f"yolo12s_sat493m_seed{s}", "results.csv")
            for s in [42, 100, 999]
        ],
        "YOLO12s (LVD-1689M)": [
            os.path.join(BASE_DIR, "evaluations", "run_reports", f"yolo12s_lvd1689m_seed{s}", "results.csv")
            for s in [42, 100, 999]
        ]
    }
    
    yolo_data = {}
    for name, files in configs.items():
        train_curves = []
        val_curves = []
        gap_curves = []
        oi_list = []
        for f in files:
            df = pd.read_csv(f)
            df.columns = [c.strip() for c in df.columns]
            tr = (df["train/box_loss"] + df["train/cls_loss"] + df["train/dfl_loss"]).values
            va = (df["val/box_loss"] + df["val/cls_loss"] + df["val/dfl_loss"]).values
            ep = df["epoch"].values
            
            max_e = min(100, len(ep))
            tr_100 = tr[:max_e]
            va_100 = va[:max_e]
            ep_100 = ep[:max_e]
            
            gap_100 = np.maximum(0, va_100 - tr_100)
            oi = np.sum(ep_100 * gap_100)
            oi_list.append(oi)
            
            if max_e < 100:
                pad_len = 100 - max_e
                tr_100 = np.concatenate([tr_100, np.full(pad_len, tr_100[-1])])
                va_100 = np.concatenate([va_100, np.full(pad_len, va_100[-1])])
                gap_100 = np.concatenate([gap_100, np.full(pad_len, gap_100[-1])])
                
            train_curves.append(tr_100)
            val_curves.append(va_100)
            gap_curves.append(gap_100)
            
        yolo_data[name] = {
            "epochs": list(range(1, 101)),
            "train_mean": np.mean(train_curves, axis=0).tolist(),
            "train_std": np.std(train_curves, axis=0).tolist(),
            "val_mean": np.mean(val_curves, axis=0).tolist(),
            "val_std": np.std(val_curves, axis=0).tolist(),
            "gap_mean": np.mean(gap_curves, axis=0).tolist(),
            "gap_std": np.std(gap_curves, axis=0).tolist(),
            "oi_mean": float(np.mean(oi_list)),
            "oi_std": float(np.std(oi_list)),
            "oi_seeds": [float(x) for x in oi_list]
        }
    return yolo_data

def extract_vit_curves():
    vit_configs = {
        "DINOv3 ViT-T + D-FINE": [
            os.path.join(WANDB_DIR, f"vitt16_stock_seed{s}_history.csv") for s in [42, 100, 999]
        ],
        "ViT-T (SAT-493M)": [
            os.path.join(WANDB_DIR, f"vitt16_sat493m_seed{s}_history.csv") for s in [42, 100, 999]
        ],
        "ViT-T (LVD-1689M)": [
            os.path.join(WANDB_DIR, f"vitt16_lvd1689m_seed{s}_history.csv") for s in [42, 100, 999]
        ]
    }
    
    all_epochs = np.arange(1, 101)
    vit_data = {}
    
    for name, files in vit_configs.items():
        train_curves = []
        val_curves = []
        gap_curves = []
        oi_list = []
        for f in files:
            df = pd.read_csv(f)
            # Train loss
            tr_rows = df[df["train_loss"].notna()].copy()
            tr_rows["int_epoch"] = tr_rows["epoch"].astype(int)
            tr_by_epoch = tr_rows.groupby("int_epoch")["train_loss"].mean()
            
            # Val loss
            val_rows = df[df["val_loss"].notna()].copy()
            val_rows["int_epoch"] = val_rows["epoch"].astype(int)
            val_by_epoch = val_rows.groupby("int_epoch")["val_loss"].mean()
            
            val_epochs = np.array(val_by_epoch.index)
            val_vals = np.array(val_by_epoch.values)
            val_interp = np.interp(all_epochs, val_epochs, val_vals)
            
            tr_epochs = np.array(tr_by_epoch.index)
            tr_vals = np.array(tr_by_epoch.values)
            tr_interp = np.interp(all_epochs, tr_epochs, tr_vals)
            
            gap = np.maximum(0, val_interp - tr_interp)
            oi = np.sum(all_epochs * gap)
            oi_list.append(oi)
            
            train_curves.append(tr_interp)
            val_curves.append(val_interp)
            gap_curves.append(gap)
            
        vit_data[name] = {
            "epochs": list(range(1, 101)),
            "train_mean": np.mean(train_curves, axis=0).tolist(),
            "train_std": np.std(train_curves, axis=0).tolist(),
            "val_mean": np.mean(val_curves, axis=0).tolist(),
            "val_std": np.std(val_curves, axis=0).tolist(),
            "gap_mean": np.mean(gap_curves, axis=0).tolist(),
            "gap_std": np.std(gap_curves, axis=0).tolist(),
            "oi_mean": float(np.mean(oi_list)),
            "oi_std": float(np.std(oi_list)),
            "oi_seeds": [float(x) for x in oi_list]
        }
    return vit_data

def main():
    print("Extracting loss curves from raw training logs...")
    data = {}
    data.update(extract_yolo_curves())
    data.update(extract_vit_curves())
    
    for dst in OUTPUT_DESTINATIONS:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Saved extracted data to: {dst}")
        
    print("\nExtraction Summary (Overfitting Index OI = sum(e * max(0, val - train))):")
    for k, v in data.items():
        print(f"  {k:22}: OI = {v['oi_mean']:8.2f} ± {v['oi_std']:6.2f} (Seeds: {[round(s, 1) for s in v['oi_seeds']]})")

if __name__ == "__main__":
    main()
