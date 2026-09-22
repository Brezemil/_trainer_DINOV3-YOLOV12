import os
import json
import glob
import pandas as pd

def check():
    # 1. Check all evaluation_results in lightly
    lightly_eval = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    metric_files = glob.glob(os.path.join(lightly_eval, '*TEST_coco_metrics.json'))
    print(f"Found {len(metric_files)} TEST_coco_metrics.json files:")
    for mf in metric_files:
        print(" ", os.path.basename(mf))

    # 2. Check run_reports in lightly
    run_reports = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluations\run_reports'
    if os.path.exists(run_reports):
        subdirs = os.listdir(run_reports)
        print(f"\nFound {len(subdirs)} run_reports dirs: {subdirs[:10]}")
        for s in subdirs[:3]:
            sp = os.path.join(run_reports, s)
            print(f"  {s} contains: {os.listdir(sp)}")

    # 3. Check DINOV3-YOLO12 export/evaluation_results
    dino_eval = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\evaluation_results'
    if os.path.exists(dino_eval):
        print(f"\nDINOV3 eval_results contains: {os.listdir(dino_eval)}")
        for item in os.listdir(dino_eval):
            ip = os.path.join(dino_eval, item)
            if os.path.isdir(ip):
                print(f"  {item} contains: {os.listdir(ip)}")
            else:
                print(f"  {item} ({os.path.getsize(ip):,} bytes)")

    # 4. Check DINOV3 export/artifacts
    dino_artifacts = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\artifacts'
    if os.path.exists(dino_artifacts):
        print(f"\nDINOV3 export/artifacts contains: {os.listdir(dino_artifacts)}")

    # 5. Check DINOV3 export/training_artifacts
    dino_train = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\training_artifacts'
    if os.path.exists(dino_train):
        print(f"\nDINOV3 export/training_artifacts contains: {os.listdir(dino_train)}")

    # 6. Check DINOV3 export/wandb_logs
    dino_wandb = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\wandb_logs'
    if os.path.exists(dino_wandb):
        print(f"\nDINOV3 export/wandb_logs contains: {os.listdir(dino_wandb)}")

if __name__ == '__main__':
    check()
