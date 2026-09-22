import os
import json
import glob
import pandas as pd

def check_more():
    # 1. DINOV3 export/evaluation_results/optimal_f1_evaluation_summary.csv and evaluation_summary.csv
    dino_eval = r'C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12\export\evaluation_results'
    for f in ['evaluation_summary.csv', 'optimal_f1_evaluation_summary.csv']:
        p = os.path.join(dino_eval, f)
        if os.path.exists(p):
            print(f"=== {f} ===")
            print(pd.read_csv(p).to_string())

    # 2. Check all files in lightly evaluation_results
    lightly_eval = r'C:\Users\emilb\My Drive\Model_Exports\_trainer_lightly\evaluation_results'
    csv_files = glob.glob(os.path.join(lightly_eval, '*.csv'))
    print("\nCSV files in lightly evaluation_results:", [os.path.basename(c) for c in csv_files])

    # 3. Check baseline subdirectory in lightly evaluation_results
    base_sub = os.path.join(lightly_eval, 'baseline')
    if os.path.exists(base_sub):
        print("\nBaseline subdir in lightly eval:", os.listdir(base_sub)[:15])

    # 4. Check dinov3 subdirectory in lightly evaluation_results
    dino_sub = os.path.join(lightly_eval, 'dinov3')
    if os.path.exists(dino_sub):
        print("\nDinov3 subdir in lightly eval:", os.listdir(dino_sub)[:15])

if __name__ == '__main__':
    check_more()
