import os
import json
import glob
import pandas as pd

def build_full_dataset():
    # Directories
    lightly_wandb = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb'
    dino_wandb = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\wandb_logs'
    lightly_eval = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    dino_eval = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\evaluation_results'
    run_reports = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports'
    predictions_summary = r'E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions\summary_tables'

    # 1. Inspect all 14 thesis models from AGENTS.md + baseline models
    # The thesis core cohort:
    # 1. Pure CNNs: YOLO12s, YOLO12n, YOLO11s, YOLO11n, YOLO26s, YOLO26n (seeds 42, 100, 999)
    # 2. Vision Transformers: DINOv3 ViT-T + D-FINE, RT-DETRv2-S, RT-DETR-L (seeds 42, 100, 999)
    # 3. Distilled Students: YOLO12s (SAT-493M), YOLO12s (LVD-1689M), ViT-T (SAT-493M), ViT-T (LVD-1689M) (seeds 42, 100, 999)
    # 4. Multi-Scale Fused: yolo12s_triple_dino3 (seeds 42, 100, 999)
    
    # Let's see all unique runs recorded across inventory, reports, and wandb
    inv_df = pd.read_csv(os.path.join(lightly_wandb, 'loss_and_weights_inventory.csv'))
    dino_runs = pd.read_csv(os.path.join(dino_wandb, 'runs_summary.csv'))
    
    print("Inventory runs:", len(inv_df))
    print("DINO runs:", len(dino_runs))
    print("Inventory columns:", list(inv_df.columns))

if __name__ == '__main__':
    build_full_dataset()
