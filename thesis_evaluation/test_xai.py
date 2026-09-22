import os
import sys
import torch
import numpy as np

try:
    from ultralytics import YOLO
    model_path = r"E:\Götterbaum\_export_data\_trainer_lightly\weights\distillation\yolo12s_stock_seed42_best.pt"
    print("Loading YOLO model from:", model_path)
    yolo_model = YOLO(model_path)
    print("Model loaded successfully.")
    
    submodules = list(yolo_model.model.model.children())
    print("Number of top-level layers in YOLO:", len(submodules))
    for i, sm in enumerate(submodules):
        print(f"Layer {i}: {sm.__class__.__name__}")
        
except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc()
