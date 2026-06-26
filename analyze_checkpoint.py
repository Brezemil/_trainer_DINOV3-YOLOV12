#!/usr/bin/env python3
"""
Robust checkpoint analyzer for DINO-YOLOv12 models
"""

import torch
import sys
from pathlib import Path


def safe_get_value(obj, key, default="unknown"):
    """Safely get value from object or dict."""
    try:
        if hasattr(obj, key):
            return getattr(obj, key)
        elif isinstance(obj, dict) and key in obj:
            return obj[key]
        else:
            return default
    except Exception:
        return default


def analyze_checkpoint(checkpoint_path):
    """Analyze checkpoint with robust error handling."""
    try:
        print(f"🔍 Analyzing checkpoint: {checkpoint_path}")
        checkpoint = torch.load(checkpoint_path, map_location="cpu")

        print("\n📊 Checkpoint Keys:")
        print("=" * 50)
        for key in checkpoint.keys():
            print(f"   ✅ {key}")

        print("\n📊 Detailed Analysis:")
        print("=" * 50)

        # Basic checkpoint info
        epoch = safe_get_value(checkpoint, "epoch", "unknown")
        print(f"📅 Epoch: {epoch}")

        best_fitness = safe_get_value(checkpoint, "best_fitness", "unknown")
        if best_fitness != "unknown":
            print(f"🏆 Best Fitness: {best_fitness}")

        # Training arguments analysis
        train_args = safe_get_value(checkpoint, "train_args", None)
        if train_args is not None:
            print("\n🏗️ Training Arguments Found:")

            # Handle different argument formats
            if hasattr(train_args, "__dict__"):
                args_dict = train_args.__dict__
            elif isinstance(train_args, dict):
                args_dict = train_args
            else:
                args_dict = {}

            print(f"   📋 Available arguments: {list(args_dict.keys())}")

            # Look for model configuration
            model_config = None
            for key in ["model", "cfg", "config"]:
                if key in args_dict:
                    model_config = args_dict[key]
                    print(f"   🏗️ Model Config ({key}): {model_config}")
                    break

            # Look for other important parameters
            important_keys = ["data", "epochs", "batch", "imgsz", "lr0", "optimizer"]
            for key in important_keys:
                if key in args_dict:
                    value = args_dict[key]
                    print(f"   {key}: {value}")

        # Model state analysis
        model_state = safe_get_value(checkpoint, "model", None)
        if model_state is not None:
            print("\n🔧 Model State Analysis:")

            # Check if it's a DetectionModel
            if hasattr(model_state, "yaml_file"):
                yaml_file = model_state.yaml_file
                print(f"   📄 YAML File: {yaml_file}")

                # Analyze YAML filename for architecture info
                if yaml_file:
                    yaml_name = Path(yaml_file).name if isinstance(yaml_file, str) else str(yaml_file)
                    print(f"   📄 YAML Name: {yaml_name}")

                    # Detect integration type from filename
                    if "triple" in yaml_name:
                        integration = "triple"
                    elif "dualp0p3" in yaml_name:
                        integration = "dualp0p3"
                    elif "dual" in yaml_name:
                        integration = "dual"
                    elif "single" in yaml_name:
                        integration = "single"
                    else:
                        integration = "unknown"

                    print(f"   🎯 Detected Integration: {integration}")

                    # Detect YOLO size
                    if "yolov12n" in yaml_name:
                        yolo_size = "n"
                    elif "yolov12s" in yaml_name:
                        yolo_size = "s"
                    elif "yolov12m" in yaml_name:
                        yolo_size = "m"
                    elif "yolov12l" in yaml_name:
                        yolo_size = "l"
                    elif "yolov12x" in yaml_name:
                        yolo_size = "x"
                    else:
                        yolo_size = "unknown"

                    print(f"   📏 Detected YOLO Size: {yolo_size}")

                    # Detect DINO variant
                    if "vitb16" in yaml_name:
                        dino_variant = "vitb16"
                    elif "vitl16" in yaml_name:
                        dino_variant = "vitl16"
                    elif "vits16" in yaml_name:
                        dino_variant = "vits16"
                    elif "convnext" in yaml_name:
                        dino_variant = "convnext_base"
                    else:
                        dino_variant = "vitb16"  # default

                    print(f"   🧬 Detected DINO Variant: {dino_variant}")

            # Check number of classes
            if hasattr(model_state, "nc"):
                nc = model_state.nc
                print(f"   📊 Number of Classes: {nc}")

            # Check model architecture by examining state dict
            if hasattr(model_state, "state_dict"):
                state_dict = model_state.state_dict()
            elif isinstance(model_state, dict):
                state_dict = model_state
            else:
                state_dict = {}

            # Count DINO components
            dino_layers = []
            for key in state_dict.keys():
                if "dino" in key.lower():
                    layer_info = key.split(".")[0] if "." in key else key
                    if layer_info not in dino_layers:
                        dino_layers.append(layer_info)

            if dino_layers:
                print(f"   🧬 DINO Layers Found: {len(dino_layers)} layers")
                for layer in dino_layers[:5]:  # Show first 5
                    print(f"      - {layer}")
                if len(dino_layers) > 5:
                    print(f"      ... and {len(dino_layers) - 5} more")

        # Generate recommended command
        print("\n✅ RECOMMENDED RESUME COMMAND:")
        print("=" * 50)

        # Try to extract configuration for command generation
        integration = "triple"  # User said they trained with triple
        yolo_size = "l"  # Default, will try to detect
        dino_variant = "vitb16"  # Default, will try to detect

        # Override with detected values if available
        if model_state and hasattr(model_state, "yaml_file") and model_state.yaml_file:
            yaml_name = str(model_state.yaml_file)

            if "yolov12n" in yaml_name:
                yolo_size = "n"
            elif "yolov12s" in yaml_name:
                yolo_size = "s"
            elif "yolov12m" in yaml_name:
                yolo_size = "m"
            elif "yolov12l" in yaml_name:
                yolo_size = "l"
            elif "yolov12x" in yaml_name:
                yolo_size = "x"

            if "vitl16" in yaml_name:
                dino_variant = "vitl16"
            elif "vits16" in yaml_name:
                dino_variant = "vits16"
            elif "convnext" in yaml_name:
                dino_variant = "convnext_base"

        print("python train_yolov12_dino.py \\")
        print("    --data coco.yaml \\")
        print(f"    --yolo-size {yolo_size} \\")
        print(f"    --pretrain {checkpoint_path} \\")
        print("    --dinoversion 3 \\")
        print(f"    --dino-variant {dino_variant} \\")
        print(f"    --integration {integration} \\")
        print("    --epochs 400 \\")
        print("    --batch-size 60 \\")
        print("    --name cont_triple_training \\")
        print("    --device 0,1")

        return True

    except Exception as e:
        print(f"❌ Error analyzing checkpoint: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_checkpoint.py <checkpoint_path>")
        sys.exit(1)

    checkpoint_path = sys.argv[1]
    if not Path(checkpoint_path).exists():
        print(f"❌ Checkpoint file not found: {checkpoint_path}")
        sys.exit(1)

    analyze_checkpoint(checkpoint_path)
