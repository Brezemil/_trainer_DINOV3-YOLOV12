import os
import json
import glob
import pandas as pd
import numpy as np

def build_complete_database():
    # 1. Paths
    lightly_wandb = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb'
    dino_wandb = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\wandb_logs'
    lightly_eval = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    dino_eval = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\evaluation_results'
    run_reports = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports'
    unlabeled_norm_csv = r'E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions\summary_tables\model_comparison_overview.csv'
    unlabeled_opt_csv = r'E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions\summary_tables\model_comparison_optimal_f1.csv'
    unlabeled_delta_csv = r'E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions\summary_tables\model_comparison_delta.csv'

    # Load inventories & summaries
    inv_df = pd.read_csv(os.path.join(lightly_wandb, 'loss_and_weights_inventory.csv'))
    lightly_runs_summary = pd.read_csv(os.path.join(lightly_wandb, 'runs_summary.csv'))
    dino_runs_summary = pd.read_csv(os.path.join(dino_wandb, 'runs_summary.csv'))
    
    # Load benchmark statistical reports
    with open(os.path.join(lightly_eval, 'benchmark_statistical_report.json')) as f:
        lightly_bench = json.load(f)
    with open(os.path.join(dino_eval, 'benchmark_statistical_report.json')) as f:
        dino_bench = json.load(f)

    # Load test coco metrics files
    test_coco_files = glob.glob(os.path.join(lightly_eval, '*TEST_coco_metrics.json'))
    test_coco_map = {}
    for tcf in test_coco_files:
        bn = os.path.basename(tcf)
        with open(tcf) as f:
            data = json.load(f)
            test_coco_map[bn] = data

    # Load unlabeled combined testset evaluation summaries
    df_unlab_norm = pd.read_csv(unlabeled_norm_csv) if os.path.exists(unlabeled_norm_csv) else pd.DataFrame()
    df_unlab_opt = pd.read_csv(unlabeled_opt_csv) if os.path.exists(unlabeled_opt_csv) else pd.DataFrame()
    df_unlab_delta = pd.read_csv(unlabeled_delta_csv) if os.path.exists(unlabeled_delta_csv) else pd.DataFrame()

    print("Loaded all base data files successfully.")
    print(f"Inventory: {len(inv_df)} rows")
    print(f"Lightly runs summary: {len(lightly_runs_summary)} rows")
    print(f"DINO runs summary: {len(dino_runs_summary)} rows")
    print(f"Unlabeled norm: {len(df_unlab_norm)} rows, opt: {len(df_unlab_opt)} rows")

if __name__ == '__main__':
    build_complete_database()
