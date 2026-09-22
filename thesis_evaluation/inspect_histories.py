import os
import json
import glob
import pandas as pd
import yaml

def inspect_histories():
    lightly_wandb = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb'
    hist_dir = os.path.join(lightly_wandb, 'metric_histories')
    files = sorted(os.listdir(hist_dir))
    print(f"Total metric history files in Lightly: {len(files)}")
    
    # Check sample files: columns, length
    for sample in ['vitt16_stock_seed42_history.csv', 'vitt16_lvd1689m_seed42_history.csv', 'yolo12s_stock_seed42_history.csv', 'yolo12s_sat493m_seed42_history.csv', 'rtdetr_l_seed42_history.csv']:
        sp = os.path.join(hist_dir, sample)
        if os.path.exists(sp):
            df = pd.read_csv(sp)
            print(f"\nFile: {sample} (shape {df.shape})")
            print("  Columns:", list(df.columns)[:15])
            print("  Head row 0:", df.iloc[0].to_dict() if len(df) > 0 else "empty")
            print("  Tail row -1:", df.iloc[-1].to_dict() if len(df) > 0 else "empty")

    # DINO wandb
    dino_wandb = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\wandb_logs\metric_histories'
    if os.path.exists(dino_wandb):
        dfiles = sorted(os.listdir(dino_wandb))
        print(f"\nTotal metric history files in DINO: {len(dfiles)}")
        for sample in dfiles:
            sp = os.path.join(dino_wandb, sample)
            df = pd.read_csv(sp)
            print(f"\nFile: {sample} (shape {df.shape})")
            print("  Columns:", list(df.columns)[:15])

if __name__ == '__main__':
    inspect_histories()
