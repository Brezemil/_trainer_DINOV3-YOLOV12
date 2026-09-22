import os
import glob
import pandas as pd
import json

def inspect():
    # 1. Inspect _trainer_DINOV3-YOLOV12/export
    dino_export = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export'
    print("=== DINOV3-YOLO12 Export Contents ===")
    for root, dirs, files in os.walk(dino_export):
        for f in files:
            if f.endswith(('.csv', '.json', '.yaml', '.md', '.txt')):
                p = os.path.join(root, f)
                print(os.path.relpath(p, dino_export), f"({os.path.getsize(p):,} bytes)")

    # 2. Inspect _trainer_lightly wandb runs_summary
    lightly_wandb = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\wandb'
    print("\n=== Lightly WandB CSVs ===")
    for f in ['runs_summary.csv', 'loss_and_weights_inventory.csv']:
        p = os.path.join(lightly_wandb, f)
        if os.path.exists(p):
            df = pd.read_csv(p)
            print(f"{f}: shape {df.shape}")
            print("Columns:", list(df.columns)[:20])
            if 'name' in df.columns:
                print("Run names sample:", df['name'].dropna().tolist()[:10])

    # 3. Inspect _trainer_lightly/evaluation_results
    eval_res = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    print("\n=== Lightly Evaluation Results ===")
    bench_stat = os.path.join(eval_res, 'benchmark_statistical_report.json')
    if os.path.exists(bench_stat):
        with open(bench_stat, 'r') as fp:
            data = json.load(fp)
            print("benchmark_statistical_report.json keys:", list(data.keys())[:15] if isinstance(data, dict) else len(data))
            if isinstance(data, dict):
                first_k = list(data.keys())[0]
                print(f"Sample key '{first_k}':", data[first_k])

if __name__ == '__main__':
    inspect()
