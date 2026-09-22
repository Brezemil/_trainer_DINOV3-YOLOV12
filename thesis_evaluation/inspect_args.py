import os
import json
import glob
import pandas as pd
import yaml

def inspect_all_sources():
    print("=== Checking Lightly run_reports ===")
    run_reports_dir = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports'
    reports = sorted(os.listdir(run_reports_dir))
    for r in reports:
        args_file = os.path.join(run_reports_dir, r, 'args.yaml')
        if os.path.exists(args_file):
            with open(args_file) as f:
                args = yaml.safe_load(f)
            print(f"{r:35} | model={args.get('model')} | epochs={args.get('epochs')} | batch={args.get('batch')} | imgsz={args.get('imgsz')} | lr0={args.get('lr0')} | lrf={args.get('lrf')} | opt={args.get('optimizer')} | freeze={args.get('freeze')}")

    print("\n=== Checking DINO Triple Training Artifacts ===")
    dino_artifacts = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\training_artifacts'
    for s in sorted(os.listdir(dino_artifacts)):
        args_file = os.path.join(dino_artifacts, s, 'args.yaml')
        if os.path.exists(args_file):
            with open(args_file) as f:
                args = yaml.safe_load(f)
            print(f"DINO {s:10} | model={args.get('model')} | epochs={args.get('epochs')} | batch={args.get('batch')} | imgsz={args.get('imgsz')} | lr0={args.get('lr0')} | lrf={args.get('lrf')} | opt={args.get('optimizer')} | freeze={args.get('freeze')}")

if __name__ == '__main__':
    inspect_all_sources()
