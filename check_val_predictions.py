import sys
from pathlib import Path
import yaml
import torch

# Add root directory to path dynamically
FILE = Path(__file__).resolve()
ROOT = FILE.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from ultralytics import YOLO

def check_val_predictions():
    print("🔍 Diagnostic: Checking Validation Set Predictions & Confidences")
    print("=" * 60)
    
    # Resolve checkpoint path: prefer last.pt to get the actual active training weights
    model_path = ROOT / "runs/detect/yolov12m_dino3_vitl16_seed_42/weights/last.pt"
    
    if not model_path.exists():
        # Search for any last.pt or best.pt in runs/detect/
        print("⚠️  last.pt not found at standard path. Searching in runs/detect/...")
        runs_dir = ROOT / "runs/detect"
        checkpoints = list(runs_dir.glob("**/last.pt"))
        if not checkpoints:
            checkpoints = list(runs_dir.glob("**/best.pt"))
            
        if len(checkpoints) > 0:
            # Pick the most recent one
            checkpoints.sort(key=lambda p: p.stat().st_mtime, reverse=True)
            model_path = checkpoints[0]
            print(f"✅ Found checkpoint: {model_path}")
        else:
            print("❌ No last.pt or best.pt checkpoints found in runs/detect/.")
            return
        
    try:
        # Load the model
        model = YOLO(str(model_path))
        data_path = model.args.get("data", None)
        print(f"Dataset YAML from checkpoint: {data_path}")
        
        if not data_path or not Path(data_path).exists():
            print("❌ Dataset yaml not found, trying fallback path...")
            # Fallback path from user prompt
            data_path = "C:/Users/photo10/Documents/GitHub/_dataset_ail/dataset.yaml"
            if not Path(data_path).exists():
                # Try emilb path
                data_path = "C:/Users/emilb/Documents/GitHub/_dataset_ail/dataset.yaml"
                if not Path(data_path).exists():
                    # Check current dir
                    data_path = ROOT / "dataset.yaml"
                    if not Path(data_path).exists():
                        print("❌ Could not locate dataset.yaml on disk. Please enter the correct path in the script.")
                        return
        
        print(f"Reading dataset config: {data_path}")
        with open(data_path, 'r') as f:
            dataset_cfg = yaml.safe_load(f)
            
        path_root = Path(dataset_cfg.get("path", ""))
        val_dir = dataset_cfg.get("val", "")
        
        # Resolve validation path
        full_val_path = path_root / val_dir if not Path(val_dir).is_absolute() else Path(val_dir)
        print(f"Resolved validation split directory: {full_val_path}")
        
        if not full_val_path.exists():
            # Try appending dataset directory prefix if it's relative on another drive/machine
            full_val_path = Path(data_path).parent / val_dir
            print(f"Retrying validation split directory: {full_val_path}")
            if not full_val_path.exists():
                print("❌ Validation directory does not exist.")
                return
                
        # Get first 5 image files
        valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
        val_images = [p for p in full_val_path.glob("**/*") if p.suffix.lower() in valid_extensions]
        print(f"Found {len(val_images)} validation images.")
        
        if len(val_images) == 0:
            print("❌ No images found in validation directory.")
            return
            
        # Select first 3 images
        test_imgs = val_images[:3]
        
        print("\n🏃 Running inference on validation images with conf=1e-6...")
        print("-" * 60)
        
        for idx, img_path in enumerate(test_imgs):
            print(f"\n🖼️ Image {idx+1}: {img_path.name}")
            results = model.predict(str(img_path), conf=1e-6, verbose=False)
            boxes = results[0].boxes
            
            print(f"   Detected boxes (conf > 1e-6): {len(boxes)}")
            if len(boxes) > 0:
                # Print stats of predicted confidences
                conf_tensor = boxes.conf
                print(f"   Confidence stats:")
                print(f"      Min:  {conf_tensor.min().item():.8f}")
                print(f"      Max:  {conf_tensor.max().item():.8f}")
                print(f"      Mean: {conf_tensor.mean().item():.8f}")
                print(f"   Top 5 box detections:")
                for i in range(min(5, len(boxes))):
                    print(f"      - Box {i}: class={int(boxes.cls[i])}, conf={float(boxes.conf[i]):.8f}, xyxy={[round(v, 1) for v in boxes.xyxy[i].tolist()]}")
            else:
                print("   ⚠️ No boxes detected even at conf=1e-6!")
                
        # Also inspect the raw outputs from the forward pass
        print("\n🔍 Inspecting raw model output tensors for anomaly detection...")
        print("-" * 60)
        pytorch_model = model.model
        pytorch_model.eval()
        
        # Load one image using the internal preprocessor
        from ultralytics.data.augment import LetterBox
        import cv2
        import numpy as np
        
        img0 = cv2.imread(str(test_imgs[0]))
        # Resize to model size
        imgsz = model.args.get("imgsz", 512)
        if isinstance(imgsz, int):
            imgsz = (imgsz, imgsz)
            
        # Preprocess
        letterbox = LetterBox(imgsz, auto=True, stride=32)
        img = letterbox(image=img0)
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)
        
        img_tensor = torch.from_numpy(img).to(next(pytorch_model.parameters()).device).float()
        img_tensor /= 255.0  # 0 - 255 to 0.0 - 1.0
        if len(img_tensor.shape) == 3:
            img_tensor = img_tensor.unsqueeze(0)  # add batch dim
            
        with torch.no_grad():
            preds = pytorch_model(img_tensor)
            
        print(f"Raw output structure: {type(preds)}")
        if isinstance(preds, (list, tuple)):
            print(f"Number of primary outputs: {len(preds)}")
            for i, p in enumerate(preds):
                if isinstance(p, torch.Tensor):
                    print(f"   Tensor {i} shape: {p.shape}")
                    print(f"      Min:  {p.min().item():.8f}, Max: {p.max().item():.8f}, Mean: {p.mean().item():.8f}")
                    print(f"      NaN count: {torch.isnan(p).sum().item()}, Inf count: {torch.isinf(p).sum().item()}")
                elif isinstance(p, (list, tuple)):
                    print(f"   Nested container {i} length: {len(p)}")
                    for j, sub_p in enumerate(p):
                        if isinstance(sub_p, torch.Tensor):
                            print(f"      - Sub-tensor {j} shape: {sub_p.shape}")
                            print(f"        Min:  {sub_p.min().item():.8f}, Max: {sub_p.max().item():.8f}")
                            print(f"        NaN count: {torch.isnan(sub_p).sum().item()}")
                else:
                    print(f"   Item {i}: {type(p)}")
                
    except Exception as e:
        print(f"❌ Diagnostic failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_val_predictions()
