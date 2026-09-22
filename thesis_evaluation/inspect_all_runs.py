import os
import json
import glob
import pandas as pd
import yaml

def inspect_all_runs():
    lightly_wandb = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb'
    dino_wandb = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\wandb_logs'
    lightly_eval = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    dino_eval = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\evaluation_results'
    run_reports = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports'

    # Load lightly runs_summary
    df_l_runs = pd.read_csv(os.path.join(lightly_wandb, 'runs_summary.csv'))
    print("Lightly runs summary shape:", df_l_runs.shape)
    print("Lightly models:", df_l_runs['model'].unique().tolist())
    print("Lightly groups:", df_l_runs['group'].unique().tolist())

    # Load lightly inventory
    df_l_inv = pd.read_csv(os.path.join(lightly_wandb, 'loss_and_weights_inventory.csv'))
    print("\nLightly inventory shape:", df_l_inv.shape)
    print("Lightly inventory model_families:", df_l_inv['model_family'].unique().tolist())
    print("Lightly inventory variants:", df_l_inv['variant'].unique().tolist())

    # Load dino runs_summary
    df_d_runs = pd.read_csv(os.path.join(dino_wandb, 'runs_summary.csv'))
    print("\nDINO runs summary shape:", df_d_runs.shape)
    print(df_d_runs[['run_id', 'run_name', 'seed', 'epochs', 'batch_size', 'mAP50', 'mAP50_95']])

    # Check metric history CSV files in both repositories
    l_hists = glob.glob(os.path.join(lightly_wandb, 'metric_histories', '*.csv'))
    d_hists = glob.glob(os.path.join(dino_wandb, 'metric_histories', '*.csv'))
    print(f"\nMetric history files: {len(l_hists)} in Lightly, {len(d_hists)} in DINO")

if __name__ == '__main__':
    inspect_all_runs()
