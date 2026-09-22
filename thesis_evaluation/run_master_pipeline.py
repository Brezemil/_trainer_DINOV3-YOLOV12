# Master Pipeline Orchestrator for testset_unlabeled_combined Evaluation
# Automatically coordinates lightly models, triple DINO models, evaluation metrics compilation, overlay plotting, and catalog generation

import os
import sys
import time
import subprocess
import glob

sys.stdout.reconfigure(line_buffering=True)

PYTHON_LIGHTLY = r"C:\Users\emilb\Documents\GitHub\_trainer_lightly\.pixi\envs\default\python.exe"
PYTHON_DINO = sys.executable

DIR_REPO = r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12"
SCRIPT_LIGHTLY = os.path.join(DIR_REPO, "thesis_evaluation", "run_inference_lightly_cohort.py")
SCRIPT_TRIPLE_DINO = os.path.join(DIR_REPO, "thesis_evaluation", "run_inference_triple_dino.py")
SCRIPT_COMPILE = os.path.join(DIR_REPO, "thesis_evaluation", "compile_inference_results.py")
SCRIPT_OVERLAYS = os.path.join(DIR_REPO, "thesis_evaluation", "generate_sample_overlays.py")
SCRIPT_README = os.path.join(DIR_REPO, "thesis_evaluation", "build_testset_predictions_readme.py")

PREDICTIONS_DIR = r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"

def check_lightly_completed():
    json_dir = os.path.join(PREDICTIONS_DIR, "predictions_json")
    expected = [
        "1_yolo12s_undistilled_seed42.json",
        "1_yolo12s_undistilled_seed100.json",
        "1_yolo12s_undistilled_seed999.json",
        "2_vitt16_dfine_undistilled_seed42.json",
        "2_vitt16_dfine_undistilled_seed100.json",
        "2_vitt16_dfine_undistilled_seed999.json",
        "3_yolo12s_distilled_sat493m_seed42.json",
        "3_yolo12s_distilled_sat493m_seed100.json",
        "3_yolo12s_distilled_sat493m_seed999.json",
        "4_vitt16_distilled_lvd1689m_seed42.json",
        "4_vitt16_distilled_lvd1689m_seed100.json",
        "4_vitt16_distilled_lvd1689m_seed999.json",
    ]
    completed = [f for f in expected if os.path.exists(os.path.join(json_dir, f)) and os.path.getsize(os.path.join(json_dir, f)) > 100]
    return len(completed) == len(expected), len(completed), len(expected)

def check_triple_dino_completed():
    json_dir = os.path.join(PREDICTIONS_DIR, "predictions_json")
    expected = [
        "5_yolo12s_triple_dino3_seed42.json",
        "5_yolo12s_triple_dino3_seed100.json",
        "5_yolo12s_triple_dino3_seed999.json",
    ]
    completed = [f for f in expected if os.path.exists(os.path.join(json_dir, f)) and os.path.getsize(os.path.join(json_dir, f)) > 100]
    return len(completed) == len(expected), len(completed), len(expected)

def run_step(name, cmd, cwd=None):
    print(f"\n======================================================================", flush=True)
    print(f"STEP: {name}", flush=True)
    print(f"Command: {' '.join(cmd)}", flush=True)
    print(f"======================================================================", flush=True)
    t0 = time.time()
    res = subprocess.run(cmd, cwd=cwd)
    dt = time.time() - t0
    if res.returncode != 0:
        print(f"[ERROR] Step {name} failed with exit code {res.returncode}", flush=True)
        sys.exit(res.returncode)
    print(f"[SUCCESS] Step {name} completed in {dt:.1f}s", flush=True)

def main():
    print("======================================================================", flush=True)
    print("MASTER PIPELINE: High-Resolution Combined Testset Evaluation", flush=True)
    print("======================================================================", flush=True)
    
    # Check lightly cohort
    is_done, n_done, n_exp = check_lightly_completed()
    if not is_done:
        print(f"Lightly cohort in progress: {n_done}/{n_exp} completed. Running lightly inference script...", flush=True)
        run_step("12 Lightly Models Inference", [PYTHON_LIGHTLY, SCRIPT_LIGHTLY], cwd=r"C:\Users\emilb\Documents\GitHub\_trainer_lightly")
    else:
        print(f"All {n_done}/{n_exp} Lightly models already completed!", flush=True)
        
    # Check triple dino cohort
    is_done, n_done, n_exp = check_triple_dino_completed()
    if not is_done:
        print(f"Triple DINO cohort in progress: {n_done}/{n_exp} completed. Running triple DINO inference script...", flush=True)
        run_step("3 Triple DINO Models Inference", [PYTHON_DINO, SCRIPT_TRIPLE_DINO], cwd=DIR_REPO)
    else:
        print(f"All {n_done}/{n_exp} Triple DINO models already completed!", flush=True)
        
    # Step 3: Compile metrics and generate figures
    run_step("Compile Evaluation Metrics & Figures", [PYTHON_DINO, SCRIPT_COMPILE], cwd=DIR_REPO)
    
    # Step 4: Generate visual prediction overlays
    run_step("Generate Sample Prediction Overlays", [PYTHON_DINO, SCRIPT_OVERLAYS], cwd=DIR_REPO)
    
    # Step 5: Build monograph README and sync across mirrors
    run_step("Build Testset Predictions Monograph README", [PYTHON_DINO, SCRIPT_README], cwd=DIR_REPO)
    
    print("\n======================================================================", flush=True)
    print("MASTER PIPELINE EXECUTION FULLY COMPLETED!", flush=True)
    print("======================================================================", flush=True)

if __name__ == "__main__":
    main()
