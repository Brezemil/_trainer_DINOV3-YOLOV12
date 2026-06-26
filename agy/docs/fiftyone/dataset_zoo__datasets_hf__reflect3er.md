---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/reflect3er.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/reflect3er)

# Dataset Card for reflect3r#

![image/png](https://huggingface.co/datasets/Voxel51/reflect3er/resolve/main/relfect3r.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) grouped dataset containing the synthetic evaluation benchmark from [Reflect3r: Single-View 3D Stereo Reconstruction Aided by Mirror Reflections](https://arxiv.org/abs/2509.20607) (3DV 2026). It contains 16 synthetic Blender interior scenes, each with a mirror, rendered from both a real camera and a geometrically derived virtual mirror camera, along with ground-truth point clouds.

## Installation#
    
    
    pip install -U fiftyone openexr
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/reflect3er", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="reflect3er"  # Assign a name to the dataset for identification
    )
    
    

## Dataset Details#

### Dataset Description#

Reflect3r is a synthetic evaluation dataset constructed to benchmark single-view 3D reconstruction methods in the presence of mirror reflections. The core insight of the accompanying paper is that a mirror in a scene provides a second, geometrically consistent viewpoint for free â a virtual camera whose pose is fully determined by reflecting the real camera pose across the mirror plane. This transforms an ostensibly single-view problem into a stereo reconstruction problem.

The dataset consists of 16 photorealistic interior Blender scenes (bedrooms, living rooms, gyms, bathrooms, etc.), each manually augmented with a mirror surface positioned in a plausible location. Each scene is rendered from two cameras: the real physical camera (`Cam_Main`) and the virtual mirror camera (`Cam_Mirror`), whose extrinsics are derived via the Householder reflection matrix. Ground-truth XYZRGB point clouds are provided for quantitative evaluation.

  * **Created by:** Jing Wu, Zirui Wang, Iro Laina, Victor Adrian Prisacariu (University of Oxford)

  * **Funded by:** Zirui Wang is supported by an ARIA research gift grant from Meta Reality Lab

  * **License:** MIT

  * **Paper:** [arXiv:2509.20607](https://arxiv.org/abs/2509.20607)

  * **Project page:** <https://jingwu2121.github.io/reflect3r/>

  * **GitHub:** [jingwu2121/reflect3r](https://github.com/jingwu2121/reflect3r)




* * *

## FiftyOne Dataset Structure#

This dataset is loaded as a **FiftyOne grouped dataset** with 16 groups (one per scene) and 3 slices per group. The default slice is `cam_main`.

### Group Slices#

Slice | Media type | Primary file | Fields  
---|---|---|---  
`cam_main` | Image | `Cam_Main/rgb_0001.png` | `depth`, `inside_mask`, `outside_mask`, `intrinsics`, `extrinsics`, `clip_params`, `scene_name`  
`cam_mirror` | Image | `Cam_Mirror/rgb_0001.png` | `depth`, `flipped_inside_mask`, `intrinsics`, `extrinsics`, `clip_params`, `scene_name`  
`cam_mirror_3d` | 3D | `point_cloud_gt.fo3d` | `scene_name`  
  
### Field Descriptions#

**`depth`** (`fo.Heatmap`) â Per-pixel metric depth rendered from the Blender scene. Stored as a normalized uint8 grayscale PNG derived from the original EXR files. See Depth Normalization below.

**`inside_mask` / `outside_mask`** (`fo.Segmentation`, on `cam_main`) â Binary segmentation masks separating mirror interior (`inside_mask`, class 1) from the surrounding real scene (`outside_mask`, class 1). These are in the coordinate frame of `Cam_Main`.

**`flipped_inside_mask`** (`fo.Segmentation`, on `cam_mirror`) â The mirror region mask horizontally flipped to align with the virtual cameraâs coordinate frame. This is the mask used by the Reflect3r pipeline to isolate the reflection region as seen from the virtual cameraâs perspective.

**`intrinsics`** (`list[list[float]]`) â 3Ã3 camera intrinsic matrix K stored as a nested Python list. Both cameras share the same intrinsics per scene, though focal length varies across scenes (e.g. `gym` uses fx=1600 while most others use fxâ2667).

**`extrinsics`** (`list[list[float]]`) â 4Ã4 camera-to-world transform stored as a nested Python list. The `Cam_Mirror` extrinsics are the reflection of `Cam_Main` extrinsics across the mirror plane, derived via the Householder matrix: `C_vir = diag(-1,1,1,1) Â· (I - 2nnâ¤) Â· C_real`.

**`clip_params`** (`list[float]`) â `[near, far]` clipping distances in metres used during Blender rendering.

**`scene_name`** (`str`) â The scene identifier (e.g. `archiviz`, `gym`, `terrazzo`).

* * *

## Parsing Decisions#

Several non-trivial choices were made when converting the raw rendered data into FiftyOne format.

### What Was Ignored#

The `imgs/` subdirectory in each scene contains pre-composited and masked variants of the main image (`image.png`, `image_outside_masked.png`, `flipped_image_inside_masked.png`, `outside.png`). These are fully derivable from `Cam_Main/rgb_0001.png` combined with the masks and were excluded to avoid redundancy. The `blender_source_files/` directory containing raw `.blend` files and texture assets was also excluded.

### Depth Normalization#

The Blender-rendered `depth_png_0001.png` files are unusable â they are all-white because Blender normalizes depth over the full `[near, far]` clip range (typically 0.1 m to 1000 m), which collapses all real scene depth variation into a tiny portion of the value range.

Instead, the raw `depth_exr_0001.exr` files are read directly. Blender stores metric depth identically in the R, G, B channels of the EXR. Some scenes (e.g. `gym`, `terrazzo`, `livingroom`) contain pixels with a sentinel value of ~1Ã10Â¹â° m assigned to background geometry, transparent surfaces, and the mirror plane itself (which has no real depth). These pixels are excluded from the normalization range and mapped to 255 (farthest depth) in the output. Valid pixels are min-max normalized per-image to uint8 and saved as `depth_norm_0001.png`.

### Mask Binarization#

The source mask PNGs (`inside_mask.png`, `outside_mask.png`, `flipped_inside_mask.png`) use pixel values `{0, 255}`. FiftyOneâs `fo.Segmentation` treats pixel values as integer class indices, and class 255 has no guaranteed color in the viewerâs default palette, causing masks to render as invisible. The masks are remapped to `{0, 1}` and saved as `*_bin.png` files, ensuring class 1 is reliably rendered.

### 3D Slice Placement#

Each sceneâs ground-truth point cloud (`point_cloud_gt.ply`) is associated with the `cam_mirror_3d` slice rather than `cam_main`. This is a deliberate semantic choice: the GT point cloud is the reconstruction target for the virtual mirror camera, which is the central contribution of the paper. FiftyOne allows only one 3D slice per sample, so this placement best reflects the paperâs intent. The `.fo3d` scene is written with `up="Z"` to match Blenderâs coordinate convention.

* * *

## Dataset Creation#

### Source Scenes#

The 16 Blender scenes were sourced from [Blender Demo](https://download.blender.org/demo/), [BlenderKit](https://www.blenderkit.com/), and [CGTrader](https://www.cgtrader.com/). Each was manually augmented by the authors with a mirror surface. In some scenes, additional geometry was modelled to ensure consistent scene complexity. A full list of original source URLs is provided in the dataset README.

### Rendering#

Scenes were rendered using Blender Cycles. The Blender toolkit provided with the dataset ([`render_depth.py`](https://github.com/jingwu2121/reflect3r/blob/main/data_toolkit/render_depth.py)) renders RGB, depth (EXR and PNG), and camera parameters for both cameras. The virtual camera pose is computed via the reflection transformation in [`add_mirrored_cam.py`](https://github.com/jingwu2121/reflect3r/blob/main/data_toolkit/add_mirrored_cam.py). All images are 1920Ã1080.

### Ground-Truth Point Clouds#

GT point clouds were generated using [`syn_gt_point_cloud_gen.py`](https://github.com/jingwu2121/reflect3r/blob/main/data_toolkit/syn_gt_point_cloud_gen.py) and saved as binary little-endian PLY files with XYZRGB vertex attributes (Open3D format). Point counts range from hundreds of thousands to several million points per scene.

* * *

## Evaluation#

The dataset is used to evaluate 3D reconstruction quality using four metrics: **accuracy** , **completeness** , **F1 score** , and **Chamfer distance**. Accuracy and completeness measure the percentage of predicted-to-GT and GT-to-predicted nearest-neighbour distances below a 1 cm threshold. Chamfer distance measures average nearest-neighbour distance between the two point sets.

The paper benchmarks Reflect3r against DUSt3R, MASt3R, VGGT, and MoGe. All baselines fail to correctly handle mirror regions â either hallucinating false geometry or producing degenerate flat reconstructions â while Reflect3r recovers correct geometry for both the real and reflected portions of the scene.

* * *

## Citation#
    
    
    @article{wu2026reflect3r,
      author = {Wu, Jing and Wang, Zirui and Laina, Iro and Prisacariu, Victor},
      title  = {{Reflect3r: Single-View 3D Stereo Reconstruction Aided by Mirror Reflections}},
      journal = {3DV},
      year   = {2026},
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
