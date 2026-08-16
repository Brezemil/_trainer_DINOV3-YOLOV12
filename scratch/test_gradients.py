import sys
from pathlib import Path

import torch

# Add root directory to path
FILE = Path(__file__).resolve()
ROOT = FILE.parent.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from ultralytics import YOLO


def test_gradients():
    print("🤖 Autograd & Gradient Flow Diagnostic Test")
    print("=" * 60)

    config_path = ROOT / "ultralytics/cfg/models/v12/yolov12m-dualp0p3-dino3-vitl16.yaml"
    print(f"Loading model config: {config_path}")

    try:
        # Load YOLO model
        model = YOLO(str(config_path))
        pytorch_model = model.model
        pytorch_model.train()  # Put in training mode

        # Create a mock input tensor with gradients enabled
        dummy_input = torch.randn(2, 3, 640, 640, requires_grad=True)

        # Print info about model parameters
        total_params = 0
        trainable_params = 0
        frozen_params = 0

        for name, param in pytorch_model.named_parameters():
            total_params += param.numel()
            if param.requires_grad:
                trainable_params += param.numel()
            else:
                frozen_params += param.numel()

        print(f"📊 Total parameters:     {total_params:,}")
        print(f"📊 Trainable parameters: {trainable_params:,}")
        print(f"📊 Frozen parameters:    {frozen_params:,}")

        # Forward pass
        print("\n🏃 Running forward pass...")
        outputs = pytorch_model(dummy_input)

        # Check output structure
        print("✅ Forward pass complete.")

        # We need to compute a dummy loss to check gradients.
        # YOLOv12 model in training mode returns loss components or raw detections.
        # Let's see what outputs contains:
        if isinstance(outputs, (list, tuple)):
            print(f"   Outputs type: {type(outputs)}, length: {len(outputs)}")
            # If it's a list/tuple, sum all elements that are tensors
            loss = torch.tensor(0.0, device=dummy_input.device)
            for i, out in enumerate(outputs):
                if isinstance(out, torch.Tensor):
                    loss = loss + out.sum()
                    print(f"   - Output {i} shape: {out.shape}")
                elif isinstance(out, dict):
                    print(f"   - Output {i} is a dict with keys: {list(out.keys())}")
                    for k, v in out.items():
                        if isinstance(v, torch.Tensor):
                            loss = loss + v.sum()
        elif isinstance(outputs, torch.Tensor):
            print(f"   Output tensor shape: {outputs.shape}")
            loss = outputs.sum()
        elif isinstance(outputs, dict):
            print(f"   Output dict keys: {list(outputs.keys())}")
            loss = torch.tensor(0.0)
            for k, v in outputs.items():
                if isinstance(v, torch.Tensor):
                    loss = loss + v.sum()
        else:
            print(f"   Unexpected output type: {type(outputs)}")
            loss = torch.tensor(1.0, requires_grad=True)

        print(f"🎯 Dummy Loss value: {loss.item():.4f}")

        # Backward pass
        print("\n🏃 Running backward pass...")
        loss.backward()
        print("✅ Backward pass complete.")

        # Check gradients for key modules
        print("\n🔍 Checking gradient status of custom components:")
        print("-" * 60)

        modules_to_check = [
            ("Preprocessor (layer 0)", "model.0"),
            ("Preprocessor feature_processor", "model.0.feature_processor"),
            ("Preprocessor dino_model", "model.0.dino_model"),
            ("Backbone P3 Adapter (layer 6)", "model.6"),
            ("Backbone P3 input_projection", "model.6.input_projection"),
            ("Backbone P3 feature_adapter", "model.6.feature_adapter"),
            ("Backbone P3 dino_model", "model.6.dino_model"),
            ("YOLO Conv layer (layer 1)", "model.1"),
            ("YOLO Detect Head (layer 23)", "model.23"),
        ]

        for label, prefix in modules_to_check:
            found = False
            has_grads = []
            no_grads = []
            for name, param in pytorch_model.named_parameters():
                if name.startswith(prefix):
                    found = True
                    if param.requires_grad:
                        if param.grad is not None:
                            grad_norm = param.grad.norm().item()
                            has_grads.append((name, grad_norm))
                        else:
                            no_grads.append(name)

            if not found:
                print(f"❓ {label}: Not found in model named parameters.")
            else:
                print(f"📌 {label}:")
                if has_grads:
                    print(f"   ✅ Trainable parameters with ACTIVE gradients: {len(has_grads)}")
                    # Show first 2 parameter gradient norms
                    for name, norm in has_grads[:2]:
                        short_name = name.replace(prefix + ".", "")
                        print(f"      - {short_name}: grad_norm = {norm:.6f}")
                if no_grads:
                    print(f"   ⚠️  Trainable parameters with MISSING/NONE gradients: {len(no_grads)}")
                    for name in no_grads[:3]:
                        short_name = name.replace(prefix + ".", "")
                        print(f"      - {short_name}")
                # Check for parameters with requires_grad=False (should have no grads)
                non_trainable = [
                    n for n, p in pytorch_model.named_parameters() if n.startswith(prefix) and not p.requires_grad
                ]
                if non_trainable:
                    print(f"   🧊 Frozen parameters (requires_grad=False): {len(non_trainable)}")
            print()

    except Exception as e:
        print(f"❌ Diagnostic failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_gradients()
