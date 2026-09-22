import os
import json
import glob
import pandas as pd

def check_vit():
    lightly_wandb = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb'
    hist_dir = os.path.join(lightly_wandb, 'metric_histories')
    if os.path.exists(hist_dir):
        files = os.listdir(hist_dir)
        print(f"Found {len(files)} metric history files in lightly wandb:")
        for f in files:
            print("  ", f)

    # Check runs_summary.csv in lightly wandb
    rs = os.path.join(lightly_wandb, 'runs_summary.csv')
    if os.path.exists(rs):
        df = pd.read_csv(rs)
        print("\nRuns summary models:", df['model'].value_counts().to_dict() if 'model' in df.columns else "no model col")
        print("\nRuns summary sample rows:")
        cols = [c for c in ['run_id', 'run_name', 'model', 'seed', 'epochs', 'batch_size', 'imgsz', 'lr0', 'mAP50', 'mAP50_95'] if c in df.columns]
        print(df[cols].dropna(subset=['model']).head(25).to_string())

    # Check loss_and_weights_inventory.csv
    lwi = os.path.join(lightly_wandb, 'loss_and_weights_inventory.csv')
    if os.path.exists(lwi):
        df_lwi = pd.read_csv(lwi)
        print("\nLoss and weights inventory shape:", df_lwi.shape)
        print(df_lwi[['model_family', 'variant', 'seed', 'wandb_run_id', 'wandb_run_name', 'best_mAP50', 'best_mAP50_95']].to_string())

if __name__ == '__main__':
    check_vit()
