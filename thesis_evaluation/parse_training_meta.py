import os
import json
import glob
import pandas as pd
import yaml

def parse_runs():
    print("=== DINOV3 export/training_artifacts ===")
    dino_train = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\training_artifacts'
    for s in ['seed_42', 'seed_100', 'seed_999']:
        sp = os.path.join(dino_train, s)
        if os.path.exists(sp):
            print(f"{s}:", os.listdir(sp))
            args_f = os.path.join(sp, 'args.yaml')
            if os.path.exists(args_f):
                with open(args_f) as f:
                    args = yaml.safe_load(f)
                    print(f"  args: model={args.get('model')}, epochs={args.get('epochs')}, batch={args.get('batch')}, imgsz={args.get('imgsz')}, lr0={args.get('lr0')}, lrf={args.get('lrf')}")

    print("\n=== DINOV3 wandb_logs/runs_summary.csv ===")
    dino_runs_summary = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\wandb_logs\runs_summary.csv'
    if os.path.exists(dino_runs_summary):
        df = pd.read_csv(dino_runs_summary)
        print("DINO runs shape:", df.shape)
        print("Columns:", list(df.columns))
        print(df.to_string())

    print("\n=== Lightly evaluations/run_reports directories ===")
    run_reports = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports'
    all_reports = sorted(os.listdir(run_reports))
    print(f"Total reports: {len(all_reports)}")
    for r in all_reports:
        rp = os.path.join(run_reports, r)
        args_f = os.path.join(rp, 'args.yaml')
        res_f = os.path.join(rp, 'results.csv')
        info = []
        if os.path.exists(args_f):
            try:
                with open(args_f) as f:
                    a = yaml.safe_load(f)
                    info.append(f"epochs={a.get('epochs')}, batch={a.get('batch')}, imgsz={a.get('imgsz')}, lr0={a.get('lr0')}")
            except Exception as e:
                info.append(f"args err: {e}")
        if os.path.exists(res_f):
            try:
                rdf = pd.read_csv(res_f)
                info.append(f"rows={len(rdf)}")
            except Exception as e:
                info.append(f"res err: {e}")
        print(f"  {r:35} | {', '.join(info)}")

if __name__ == '__main__':
    parse_runs()
