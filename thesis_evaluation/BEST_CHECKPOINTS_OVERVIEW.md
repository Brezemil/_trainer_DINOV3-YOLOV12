# Best Checkpoints, Training Epochs, Batch Size & Compute Walltime Overview

* **Master's Thesis:** *High-Resolution UAV Detection, Geolocation, and Knowledge Distillation of Invasive Ailanthus altissima Canopies*
* **Candidate / Author:** Emil Brezovsky
* **Target Species:** *Ailanthus altissima* (Tree of Heaven)
* **Cohort Summary:** 14 neural network configurations across 4 architectural paradigms evaluated across $n = 3$ independent random initialization seeds (`42`, `100`, `999`).

---

## Checkpoint Selection Criteria

1. **Ultralytics YOLO & RT-DETR Models:**
   The saved `best.pt` checkpoint is selected based on Ultralytics composite fitness:
   $$\text{fitness} = 0.1 \times \text{mAP@50} + 0.9 \times \text{mAP(50-95)}$$
   $90\%$ of the selection weight is governed by the COCO strict metric $\text{mAP(50-95)}$, and $10\%$ by $\text{mAP@50}$.

2. **DINOv3 ViT-T + D-FINE Models:**
   The saved `best.pth` checkpoint tracks the overall COCO validation $\text{mAP(50-95)}$ (`AP_all`), with $\text{mAP@50}$ utilized as a secondary resolution metric.

---

## Master Checkpoint, Hyperparameter & Compute Overview

| Architectural Cohort | Model Architecture | Random Seed | Batch Size ($B$) | Total Epochs Trained | Best Checkpoint Epoch | Training Walltime (Hours) | Validation $\text{mAP@50}$ | Validation $\text{mAP(50-95)}$ | Checkpoint File Path |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Pure CNN** | `yolo26n` | `42` | 16 | 145 | **45** | 8.92 h | $0.6175$ | $0.3183$ | [`yolo26n_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo26n_seed_42/weights/best.pt) |
| | | `100` | 16 | 153 | **53** | 9.41 h | $0.6076$ | $0.3137$ | [`yolo26n_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo26n_seed_100/weights/best.pt) |
| | | `999` | 16 | 166 | **66** | 10.41 h | $0.6086$ | $0.3232$ | [`yolo26n_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo26n_seed_999/weights/best.pt) |
| | `yolo26s` | `42` | 16 | 194 | **94** | 16.89 h | $0.6178$ | $0.3307$ | [`yolo26s_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo26s_seed_42/weights/best.pt) |
| | | `100` | 16 | 140 | **40** | 10.80 h | $0.6161$ | $0.3146$ | [`yolo26s_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo26s_seed_100/weights/best.pt) |
| | | `999` | 16 | 159 | **59** | 12.04 h | $0.6195$ | $0.3290$ | [`yolo26s_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo26s_seed_999/weights/best.pt) |
| | `yolo11n` | `42` | 16 | 203 | **103** | 11.35 h | $0.6607$ | $0.3391$ | [`yolo11n_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo11n_seed_42/weights/best.pt) |
| | | `100` | 16 | 159 | **59** | 8.86 h | $0.6389$ | $0.3428$ | [`yolo11n_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo11n_seed_100/weights/best.pt) |
| | | `999` | 16 | 185 | **85** | 10.35 h | $0.6525$ | $0.3450$ | [`yolo11n_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo11n_seed_999/weights/best.pt) |
| | `yolo11s` | `42` | 16 | 172 | **72** | 12.00 h | $0.6388$ | $0.3391$ | [`yolo11s_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo11s_seed_42/weights/best.pt) |
| | | `100` | 16 | 141 | **41** | 9.82 h | $0.6428$ | $0.3393$ | [`yolo11s_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo11s_seed_100/weights/best.pt) |
| | | `999` | 16 | 142 | **56** | 9.91 h | $0.6369$ | $0.3298$ | [`yolo11s_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo11s_seed_999/weights/best.pt) |
| | `yolo12n` | `42` | 16 | 141 | **41** | 10.69 h | $0.6492$ | $0.3399$ | [`yolo12n_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12n_seed_42/weights/best.pt) |
| | | `100` | 16 | 166 | **64** | 12.72 h | $0.6440$ | $0.3345$ | [`yolo12n_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12n_seed_100/weights/best.pt) |
| | | `999` | 16 | 165 | **65** | 12.56 h | $0.6353$ | $0.3432$ | [`yolo12n_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12n_seed_999/weights/best.pt) |
| | `yolo12s` (Native) | `42` | 16 | 154 | **54** | 17.61 h | $0.6502$ | $0.3420$ | [`yolo12s_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_seed_42/weights/best.pt) |
| | | `100` | 16 | 166 | **66** | 18.91 h | $0.6380$ | $0.3392$ | [`yolo12s_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_seed_100/weights/best.pt) |
| | | `999` | 16 | 156 | **56** | 17.72 h | $0.6351$ | $0.3323$ | [`yolo12s_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_seed_999/weights/best.pt) |
| **Distilled Students** | `YOLO12s (SAT-493M)` | `42` | 8 | 77 | **47** | 5.16 h | $0.6421$ | $0.3375$ | [`distill_yolo12s_sat_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_sat493m_seed42/weights/best.pt) |
| | | `100` | 8 | 86 | **56** | 5.88 h | $0.6766$ | $0.3483$ | [`distill_yolo12s_sat_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_sat493m_seed100/weights/best.pt) |
| | | `999` | 8 | 84 | **54** | 5.78 h | $0.6448$ | $0.3512$ | [`distill_yolo12s_sat_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_sat493m_seed999/weights/best.pt) |
| | `YOLO12s (LVD-1689M)` | `42` | 8 | 90 | **60** | 6.13 h | $0.6265$ | $0.3310$ | [`distill_yolo12s_lvd_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_lvd1689m_seed42/weights/best.pt) |
| | | `100` | 8 | 71 | **41** | 4.86 h | $0.6514$ | $0.3449$ | [`distill_yolo12s_lvd_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_lvd1689m_seed100/weights/best.pt) |
| | | `999` | 8 | 71 | **41** | 4.89 h | $0.6375$ | $0.3460$ | [`distill_yolo12s_lvd_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/yolo12s_lvd1689m_seed999/weights/best.pt) |
| **Multi-Scale Fusion** | `yolo12s_triple_dino3` | `42` | 4 | 300 | **299** | 74.45 h | $0.5951$ | $0.3185$ | [`runs/train/triple_dino3_seed42/weights/best.pt`](file:///C:/Users/emilb/Documents/GitHub/_trainer_DINOV3-YOLOV12/runs/train/) |
| | | `100` | 4 | 300 | **299** | 79.62 h | $0.5681$ | $0.2996$ | [`runs/train/triple_dino3_seed100/weights/best.pt`](file:///C:/Users/emilb/Documents/GitHub/_trainer_DINOV3-YOLOV12/runs/train/) |
| | | `999` | 4 | 300 | **283** | 75.20 h | $0.5801$ | $0.3148$ | [`runs/train/triple_dino3_seed999/weights/best.pt`](file:///C:/Users/emilb/Documents/GitHub/_trainer_DINOV3-YOLOV12/runs/train/) |
| **Detection Transformers** | `RT-DETR-L` | `42` | 4 | 115 | **15** | 69.82 h | $0.5819$ | $0.2458$ | [`rtdetr_l_seed42/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/rtdetr_l_seed_42/weights/best.pt) |
| | | `100` | 4 | 101 | **16** | 61.59 h | $0.5732$ | $0.2282$ | [`rtdetr_l_seed100/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/rtdetr_l_seed_100/weights/best.pt) |
| | | `999` | 4 | 102 | **2** | 74.47 h | $0.5736$ | $0.2584$ | [`rtdetr_l_seed999/weights/best.pt`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/evaluations/run_reports/rtdetr_l_seed_999/weights/best.pt) |
| **DINOv3 ViTs (D-FINE)** | `DINOv3 ViT-T + D-FINE` | `42` | 8 | 100 | **97** | 18.73 h | $0.6182$ | $0.3205$ | [`checkpoints/vitt16_seed42_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_seed42_best.pth) |
| | | `100` | 8 | 100 | **100** | 9.61 h | $0.6291$ | $0.3304$ | [`checkpoints/vitt16_seed100_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_seed100_best.pth) |
| | | `999` | 8 | 100 | **100** | 9.84 h | $0.6035$ | $0.3175$ | [`checkpoints/vitt16_seed999_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_seed999_best.pth) |
| | `ViT-T (SAT-493M)` | `42` | 8 | 100 | **80** | 7.31 h | $0.6325$ | $0.3256$ | [`checkpoints/vitt16_sat_seed42_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_sat_seed42_best.pth) |
| | | `100` | 8 | 100 | **100** | 4.25 h | $0.5284$ | $0.2803$ | [`checkpoints/vitt16_sat_seed100_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_sat_seed100_best.pth) |
| | | `999` | 8 | 100 | **97** | 4.38 h | $0.5333$ | $0.2845$ | [`checkpoints/vitt16_sat_seed999_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_sat_seed999_best.pth) |
| | `ViT-T (LVD-1689M)` | `42` | 8 | 100 | **74** | 7.66 h | $0.6234$ | $0.3273$ | [`checkpoints/vitt16_lvd_seed42_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_lvd_seed42_best.pth) |
| | | `100` | 8 | 100 | **92** | 7.35 h | $0.6081$ | $0.3137$ | [`checkpoints/vitt16_lvd_seed100_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_lvd_seed100_best.pth) |
| | | `999` | 8 | 100 | **100** | 10.58 h | $0.6088$ | $0.3165$ | [`checkpoints/vitt16_lvd_seed999_best.pth`](file:///C:/Users/emilb/My%20Drive/Model_Exports/_trainer_lightly/checkpoints/vitt16_lvd_seed999_best.pth) |
