import os
import glob

def scan():
    targets = [
        ('Local DINOV3-YOLO12', r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12'),
        ('Local Lightly', r'C:\Users\emilb\Documents\GitHub\_trainer_lightly'),
        ('Drive Lightly', r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly'),
        ('Drive thesis_evaluation_2D', r'C:\Users\emilb\My Drive\Model_Exports\thesis_evaluation_2D'),
        ('E: Drive Predictions & Data', r'E:\Götterbaum\_export_data'),
    ]

    for title, base in targets:
        print(f"=== {title}: {base} ===")
        if not os.path.exists(base):
            print("DOES NOT EXIST")
            continue
        items = os.listdir(base)
        print(f"Top-level ({len(items)} items): {items[:15]}")
        # Look for wandb, csv, json, runs
        for sub in ['wandb', 'runs', 'evaluations', 'evaluation_results', 'export']:
            sp = os.path.join(base, sub)
            if os.path.exists(sp):
                print(f"  Subdir '{sub}' exists, contains: {os.listdir(sp)[:10]}")

if __name__ == '__main__':
    scan()
