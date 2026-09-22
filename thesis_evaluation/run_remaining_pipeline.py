# Master Runner for Remaining Evaluation Pipeline
# Executes:
# 1. Triple DINO Batch Inference (3 Seeds)
# 2. Optimal F1 Predictions Generation for all models
# 3. Comprehensive Benchmark Compilation & Metrics Calculation
# 4. Multi-Panel Visual Prediction Overlays
# 5. Master README Monograph Compilation & Multi-Mirror Sync

import os
import sys
import subprocess
import time

sys.stdout.reconfigure(line_buffering=True)

PYTHON_EXE = sys.executable
BASE_DIR = r"C:\Users\emilb\Documents\GitHub\_trainer_DINOV3-YOLOV12"
THESIS_DIR = os.path.join(BASE_DIR, "thesis_evaluation")

def run_step(script_name, description):
    print(f"\n{'='*70}", flush=True)
    print(f">> [STEP] {description}", flush=True)
    print(f">> Running: {script_name}", flush=True)
    print(f"{'='*70}", flush=True)
    t0 = time.time()
    script_path = os.path.join(THESIS_DIR, script_name)
    ret = subprocess.run([PYTHON_EXE, script_path], cwd=BASE_DIR)
    dt = time.time() - t0
    if ret.returncode != 0:
        print(f">> [ERROR] {script_name} failed with return code {ret.returncode} after {dt:.1f}s!", flush=True)
        sys.exit(ret.returncode)
    else:
        print(f">> [SUCCESS] {script_name} finished in {dt:.1f}s.", flush=True)

def main():
    print("======================================================================", flush=True)
    print("Executing Remaining Evaluation Pipeline", flush=True)
    print("======================================================================", flush=True)

    # 1. Run Triple DINO inference
    run_step("run_inference_triple_dino.py", "Triple DINO YOLO12s Batch Inference (Seeds 42, 100, 999)")

    # 2. Generate all optimal F1 predictions
    run_step("generate_optimal_f1_predictions.py", "Generate Calibrated Optimal F1 Predictions (c = c*)")

    # 3. Compile inference results
    run_step("compile_inference_results.py", "Compile Dual-Confidence Benchmark Metrics, Tables & Figures")

    # 4. Generate sample visual overlays
    run_step("generate_sample_overlays.py", "Generate Multi-Panel Visual Comparison Overlays")

    # 5. Build master monograph README
    run_step("build_testset_predictions_readme.py", "Compile Comprehensive README Monograph & Multi-Mirror Sync")

    print("\n======================================================================", flush=True)
    print("ALL EVALUATION PIPELINE STEPS COMPLETED SUCCESSFULLY!", flush=True)
    print("======================================================================", flush=True)

if __name__ == "__main__":
    main()
