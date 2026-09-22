import os
import json
import glob
import pandas as pd

def check_vit_reports():
    lightly_wandb = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb'
    # check runs_summary.csv for vitt16
    df = pd.read_csv(os.path.join(lightly_wandb, 'runs_summary.csv'))
    vitt_runs = df[df['run_name'].str.contains('vit|dfine', case=False, na=False)]
    print(f"Found {len(vitt_runs)} ViT/D-FINE runs in runs_summary.csv:")
    cols = ['run_id', 'run_name', 'model', 'seed', 'epochs', 'batch_size', 'imgsz', 'lr0', 'lrf', 'optimizer', 'weight_decay']
    print(vitt_runs[cols].to_string())

if __name__ == '__main__':
    check_vit_reports()
