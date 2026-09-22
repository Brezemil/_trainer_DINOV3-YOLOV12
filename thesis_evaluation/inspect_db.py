import os
import pandas as pd

def inspect_db():
    p = r"C:\Users\emilb\My Drive\_thesis_eval\master_runs_database.csv"
    df = pd.read_csv(p)
    print(f"Master Database Shape: {df.shape}")
    print("\nColumns (58 attributes):")
    for i, c in enumerate(df.columns):
        print(f"  {i+1:2d}. {c}")

    print("\nDistinct Canonical Models:")
    print(df['canonical_model'].value_counts())

    print("\nSample records for pure CNN, ViT, Distilled, and Multi-Scale Fused:")
    sub_cols = ['canonical_model', 'arch_family', 'seed', 'epochs', 'batch_size', 'imgsz', 'lr0', 'is_distilled', 'teacher_model', 'params_m', 'latency_ms', 'test_coco_AP50', 'unlabeled_c025_f1', 'unlabeled_opt_f1']
    sample_models = ['YOLO12s', 'DINOv3 ViT-T + D-FINE', 'YOLO12s (SAT-493M)', 'ViT-T (LVD-1689M)', 'YOLO12s Triple DINOv3']
    print(df[df['canonical_model'].isin(sample_models)][sub_cols].drop_duplicates(subset=['canonical_model', 'seed']).to_string())

if __name__ == '__main__':
    inspect_db()
