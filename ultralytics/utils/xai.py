# Ultralytics YOLO 🚀, AGPL-3.0 license
"""
Explainable AI (XAI) feature attribution utilities for YOLOv12 and YOLOv12-DINO models.

Implements Eigen-CAM (Eigen-Class Activation Mapping) using Singular Value Decomposition (SVD)
as formulated by Muhammad & Yeasin (2020) and Gildenblat (2021).
"""

from pathlib import Path
from typing import List, Optional, Tuple, Union
import cv2
import numpy as np
import torch
import torch.nn as nn


class EigenCAMExplainer:
    """
    Eigen-CAM Explainer for YOLO and Vision-Transformer Object Detectors.

    Computes class-independent spatial feature attribution via SVD on intermediate
    layer activation tensors, bypassing gradient vanishing and logit scaling biases.
    """

    def __init__(
        self,
        model: nn.Module,
        target_layers: Optional[List[Union[str, nn.Module]]] = None,
        device: Optional[torch.device] = None,
    ):
        """
        Initialize the Eigen-CAM explainer.

        Args:
            model: PyTorch model (e.g. YOLOv12 or YOLOv12-DINO)
            target_layers: List of target layer names or modules to hook into.
                          Defaults to intermediate backbone/neck layer (e.g., model.model[9] or model.model[-2]).
            device: torch device.
        """
        self.model = model
        self.device = device or next(model.parameters()).device
        self.model.eval()
        self.activations = []
        self.hooks = []

        if target_layers is None:
            # Automatic layer discovery for YOLO / Ultralytics models
            self.target_layers = self._auto_discover_target_layers()
        else:
            self.target_layers = self._resolve_target_layers(target_layers)

        self._register_hooks()

    def _auto_discover_target_layers(self) -> List[nn.Module]:
        """Automatically selects deep backbone/neck layers for attribution."""
        layers = []
        if hasattr(self.model, "model") and hasattr(self.model.model, "model"):
            m = self.model.model.model
            # For YOLOv12, layer 9 is typically P4/R-ELAN stage, layer -2 is pre-detection neck
            idx = min(9, len(m) - 2)
            layers.append(m[idx])
        elif hasattr(self.model, "model"):
            m = self.model.model
            if isinstance(m, (nn.Sequential, nn.ModuleList)):
                idx = min(9, len(m) - 2)
                layers.append(m[idx])
            else:
                layers.append(m)
        else:
            # Fallback to last convolutional or linear block
            convs = [mod for mod in self.model.modules() if isinstance(mod, (nn.Conv2d, nn.BatchNorm2d))]
            if convs:
                layers.append(convs[-1])
            else:
                layers.append(self.model)
        return layers

    def _resolve_target_layers(self, target_layers: List[Union[str, nn.Module]]) -> List[nn.Module]:
        """Resolves layer strings (e.g. 'model.model.9') to PyTorch modules."""
        resolved = []
        for tl in target_layers:
            if isinstance(tl, nn.Module):
                resolved.append(tl)
            elif isinstance(tl, str):
                curr = self.model
                for part in tl.split("."):
                    if part.isdigit():
                        curr = curr[int(part)]
                    else:
                        curr = getattr(curr, part)
                resolved.append(curr)
        return resolved

    def _register_hooks(self):
        """Registers forward hooks to capture intermediate layer activations."""
        self._remove_hooks()
        self.activations.clear()

        def hook_fn(module, input, output):
            # Output can be tensor or tuple of tensors (e.g. multi-scale features)
            if isinstance(output, (tuple, list)):
                out_tensor = output[0]
            else:
                out_tensor = output
            self.activations.append(out_tensor.detach())

        for layer in self.target_layers:
            h = layer.register_forward_hook(hook_fn)
            self.hooks.append(h)

    def _remove_hooks(self):
        """Removes all registered PyTorch forward hooks."""
        for h in self.hooks:
            h.remove()
        self.hooks.clear()

    @staticmethod
    def compute_svd_eigencam(activation_tensor: torch.Tensor) -> np.ndarray:
        """
        Computes the first principal component activation map via SVD.

        Args:
            activation_tensor: (B, C, H, W) or (B, N, D) feature tensor
        Returns:
            Normalized 2D heatmap in [0, 1] as numpy float32 array (H, W)
        """
        # Squeeze batch if B=1
        if activation_tensor.dim() == 4:
            # (1, C, H, W) -> (C, H, W)
            act = activation_tensor[0]
            c, h, w = act.shape
            x = act.view(c, h * w).permute(1, 0)  # (H*W, C)
        elif activation_tensor.dim() == 3:
            # (1, N, D) -> (N, D)
            x = activation_tensor[0]
            # assume square grid for patch tokens
            num_tokens, d = x.shape
            grid_size = int(np.sqrt(num_tokens))
            h, w = grid_size, grid_size
        else:
            raise ValueError(f"Unsupported activation tensor shape: {activation_tensor.shape}")

        # Center the feature vectors across spatial locations
        x_centered = x - torch.mean(x, dim=0, keepdim=True)

        # Singular Value Decomposition (SVD)
        # x_centered = U @ Sigma @ V^T
        try:
            # torch.linalg.svd is fast and GPU-accelerated
            u, s, vh = torch.linalg.svd(x_centered.float(), full_matrices=False)
            # First principal component is first column of U or projection onto V_1
            # Projection: M = x_centered @ vh[0, :]
            v1 = vh[0, :]  # (C,)
            cam = torch.matmul(x_centered, v1)  # (H*W,)
        except Exception:
            # Fallback to PCA via covariance matrix
            cov = torch.matmul(x_centered.T, x_centered)
            e_vals, e_vecs = torch.linalg.eigh(cov)
            v1 = e_vecs[:, -1]
            cam = torch.matmul(x_centered, v1)

        cam = cam.view(h, w).cpu().numpy()

        # Apply ReLU to keep positive activations
        cam = np.maximum(cam, 0)

        # Min-max normalization
        min_v = np.min(cam)
        max_v = np.max(cam)
        if max_v - min_v > 1e-8:
            cam = (cam - min_v) / (max_v - min_v)
        else:
            cam = np.zeros_like(cam)

        return cam.astype(np.float32)

    def generate_heatmap(
        self,
        img_bgr: np.ndarray,
        input_size: Tuple[int, int] = (1024, 1024),
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Executes forward inference and extracts the 2D Eigen-CAM heatmap.

        Args:
            img_bgr: Input BGR image as numpy array (H, W, 3)
            input_size: Model input resolution (H_in, W_in)
        Returns:
            (raw_heatmap_resized, blended_overlay)
        """
        h_orig, w_orig = img_bgr.shape[:2]
        self.activations.clear()

        # Preprocess image
        img_resized = cv2.resize(img_bgr, input_size)
        img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
        tensor = torch.from_numpy(img_rgb).permute(2, 0, 1).unsqueeze(0).float() / 255.0
        tensor = tensor.to(self.device)

        # Forward pass (triggers hooks)
        with torch.no_grad():
            _ = self.model(tensor)

        if not self.activations:
            raise RuntimeError("No activations captured! Check target_layers definition.")

        # Aggregate across hooked layers (usually single layer)
        cam_maps = [self.compute_svd_eigencam(act) for act in self.activations]
        cam_avg = np.mean(cam_maps, axis=0)

        # Resize CAM to original image dimensions
        cam_full = cv2.resize(cam_avg, (w_orig, h_orig), interpolation=cv2.INTER_LINEAR)

        # Generate blended heatmap overlay
        heatmap_uint8 = np.uint8(255 * cam_full)
        heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_TURBO)
        overlay = cv2.addWeighted(img_bgr, 0.55, heatmap_color, 0.45, 0)

        return cam_full, overlay

    def __del__(self):
        """Clean up hooks on deletion."""
        self._remove_hooks()
