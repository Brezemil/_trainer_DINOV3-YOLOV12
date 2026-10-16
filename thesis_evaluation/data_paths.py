"""
data_paths.py
Central path resolution for thesis evaluation scripts in _trainer_DINOV3-YOLOV12.
Resolves all datasets, predictions, and model weights against the unified _data directory.
"""

from pathlib import Path
import os

REPO_ROOT = Path(__file__).resolve().parents[1]

def get_data_dir() -> Path:
    """Returns the absolute Path to the unified _data directory."""
    # 1. Environment variable
    env_dir = os.environ.get("DATA_DIR")
    if env_dir and Path(env_dir).exists():
        return Path(env_dir).resolve()
    # 2. Sibling directory to repo root
    sibling_data = REPO_ROOT.parent / "_data"
    if sibling_data.exists():
        return sibling_data.resolve()
    # 3. Default path
    default_c = Path(r"C:\Users\emilb\Documents\GitHub\_data")
    if default_c.exists():
        return default_c.resolve()
    return sibling_data

DATA_DIR = get_data_dir()

# Dataset directories
_testset = DATA_DIR / "testset_unlabeled_combined"
IMAGES_DIR = str(_testset / "images") if (_testset / "images").exists() else r"E:\Götterbaum\_export_data\testset_unlabeled_combined\images"
LABELS_DIR = str(_testset / "labels") if (_testset / "labels").exists() else r"E:\Götterbaum\_export_data\testset_unlabeled_combined\labels"
PREDICTIONS_DIR = str(DATA_DIR / "testset_unlabeled_combined_predictions") if (DATA_DIR / "testset_unlabeled_combined_predictions").exists() else r"E:\Götterbaum\_export_data\testset_unlabeled_combined_predictions"

def resolve_weight(rel_or_name: str) -> str:
    """Resolves a model weight path across _data/weights and local repositories."""
    fn = Path(rel_or_name).name
    candidates = [
        DATA_DIR / "weights" / "checkpoints" / fn,
        DATA_DIR / "weights" / "distillation" / fn,
        DATA_DIR / "weights" / "baseline" / fn,
        DATA_DIR / "weights" / "pretrained_base" / fn,
        DATA_DIR / "weights" / "pretrained_backbones" / fn,
        DATA_DIR / "weights" / fn,
        REPO_ROOT / "export" / "weights" / fn,
        REPO_ROOT.parent / "_trainer_lightly" / "weights" / fn,
        REPO_ROOT.parent / "_trainer_lightly" / "weights" / "distillation" / fn,
        REPO_ROOT.parent / "_trainer_lightly" / "weights" / "baseline" / fn,
        Path(rel_or_name),
    ]
    for cand in candidates:
        if cand.exists():
            return str(cand.resolve())
    return rel_or_name
