#!/usr/bin/env python3
"""
Demo: --unfreeze-dino argument usage examples
"""

print("🚀 DINOv3-YOLOv12 Training with --unfreeze-dino")
print("=" * 60)

print("\n📖 **DINO Weight Control Options:**")
print()
print("🔒 **Default (Recommended): FROZEN DINO Weights**")
print("   • Faster training, lower VRAM usage")
print("   • Preserves pretrained DINOv3 knowledge")
print("   • Best for most use cases")
print("   Command:")
print("   python train_yolov12_dino.py \\")
print("       --data /path/to/data.yaml \\")
print("       --yolo-size s \\")
print("       --dino-variant vitb16 \\")
print("       --integration single")
print()

print("🔥 **Advanced: TRAINABLE DINO Weights**")
print("   • Allows fine-tuning of DINOv3 features")
print("   • Higher VRAM usage, slower training")
print("   • Best for specialized domains or research")
print("   Command:")
print("   python train_yolov12_dino.py \\")
print("       --data /path/to/data.yaml \\")
print("       --yolo-size s \\")
print("       --dino-variant vitb16 \\")
print("       --integration single \\")
print("       --unfreeze-dino")
print()

print("🎯 **Integration Examples:**")
print()
print("1️⃣ **Single P4 Integration (Efficient)**")
print("   # Frozen (default):")
print("   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-variant vitb16 --integration single")
print("   # Trainable:")
print(
    "   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-variant vitb16 --integration single --unfreeze-dino"
)
print()

print("2️⃣ **Dual P3+P4 Integration (High Performance)**")
print("   # Frozen (default):")
print("   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-variant vitb16 --integration dual")
print("   # Trainable:")
print(
    "   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-variant vitb16 --integration dual --unfreeze-dino"
)
print()

print("3️⃣ **Input Preprocessing P0 (Most Stable)**")
print("   # Frozen (default):")
print("   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-input dinov3_vitb16")
print("   # Trainable:")
print("   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-input dinov3_vitb16 --unfreeze-dino")
print()

print("4️⃣ **Full-Scale P0+P3+P4 Integration (Ultimate)**")
print("   # Frozen (default):")
print(
    "   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-input dinov3_vitb16 --dino-variant vitb16 --integration dual"
)
print("   # Trainable:")
print(
    "   python train_yolov12_dino.py --data data.yaml --yolo-size s --dino-input dinov3_vitb16 --dino-variant vitb16 --integration dual --unfreeze-dino"
)
print()

print("💡 **Resource Requirements:**")
print()
print("| Configuration | DINO Weights | VRAM Usage | Training Speed | When to Use |")
print("|:--------------|:-------------|:-----------|:---------------|:------------|")
print("| **Frozen**    | ❄️ Fixed      | 🟢 Lower    | ⚡ Faster       | Production, general use |")
print("| **Trainable** | 🔥 Learning   | 🔴 Higher   | 🐌 Slower       | Research, specialized domains |")
print()

print("🎯 **Recommendation:**")
print("Start with **frozen weights** (default) for fastest training and good results.")
print("Use **--unfreeze-dino** only if you need domain-specific fine-tuning.")
print()

print("✅ **Ready to train with optimal DINO weight control!**")
