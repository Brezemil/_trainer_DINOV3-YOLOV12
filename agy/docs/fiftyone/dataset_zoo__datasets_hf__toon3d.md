---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/toon3d.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/toon3d)

# Dataset Card for toon3d#

![image/png](https://huggingface.co/datasets/Voxel51/toon3d/resolve/main/toon3d.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 12 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/toon3d", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="toon3d"  # Assign a name to the dataset for identification
    )
    
    

## Dataset Details#

### Dataset Description#

Toon3D is a multi-view cartoon scene reconstruction dataset introduced in the paper _âToon3D: Seeing Cartoons from New Perspectivesâ_ (Weber et al., arXiv:2405.10320, 2024). It contains 12 scenes from popular hand-drawn cartoons and anime, each comprising 5â12 frames that depict the same environment from geometrically inconsistent viewpoints.

This FiftyOne dataset wraps the Toon3D scenes together with the outputs of the authorsâ custom Structure-from-Motion (SfM) pipeline, which recovers camera poses and dense 3D point clouds from the geometrically inconsistent input images.

  * **Curated by:** Ethan Weber, Riley Peterlinz, Rohan Mathur, Frederik Warburg, Alexei A. Efros, Angjoo Kanazawa (UC Berkeley / Teton.ai)

  * **Paper:** [arXiv:2405.10320](https://arxiv.org/abs/2405.10320)

  * **Project page:** https://toon3d.studio/

  * **Dataset repository:** https://github.com/ethanweber/toon3d-dataset




* * *

## FiftyOne Dataset Structure#

### Overview#

Property | Value  
---|---  
Dataset name | `toon3d`  
FiftyOne media type | `group`  
Number of groups | 12  
Number of samples | 92  
Default group slice | `frame_00`  
Total named slices | 13  
  
### Groups#

Each **group** corresponds to one cartoon scene. There are 12 groups, one per scene:

Group (scene tag) | Frame slices | Total samples (frames + 3D)  
---|---|---  
`avatar-house` | `frame_00` â `frame_07` | 9  
`bobs-burgers` | `frame_00` â `frame_06` | 8  
`bojak-room` | `frame_00` â `frame_11` | 13  
`family-guy-dining` | `frame_00` â `frame_06` | 8  
`family-guy-house` | `frame_00` â `frame_05` | 7  
`krusty-krab` | `frame_00` â `frame_08` | 10  
`magic-school-bus` | `frame_00` â `frame_04` | 6  
`mystery-machine` | `frame_00` â `frame_05` | 7  
`planet-express` | `frame_00` â `frame_04` | 6  
`simpsons-house` | `frame_00` â `frame_04` | 6  
`smith-residence` | `frame_00` â `frame_03` | 5  
`spirited-away` | `frame_00` â `frame_05` | 7  
  
Groups have a variable number of frame slices (4â12). Slice names are zero-padded to two digits (`frame_00`â`frame_11`) and are consistent across all groups; scenes with fewer frames simply have no sample in the higher-indexed slices.

### Slices#

#### Frame slices â `frame_00` through `frame_11`#

Each frame slice sample represents one original cartoon image from the scene.

**`filepath`** points to the original cartoon PNG (`toon3d-dataset/<scene>/images/<NNNNN>.png`). Images are resized to a maximum of 960 Ã 720 px during preprocessing.

**Fields:**

Field | Type | Description  
---|---|---  
`group` | `EmbeddedDocumentField(Group)` | Group membership â id shared across all slices of the same scene, name is the slice identifier (e.g. `frame_02`)  
`tags` | `ListField(StringField)` | Single-element list containing the scene name, e.g. `["bobs-burgers"]`  
`depth` | `EmbeddedDocumentField(Heatmap)` | Marigold monocular depth estimate visualised as a heatmap. `map_path` points to the depth colormap PNG at `toon3d-dataset/<scene>/depth-images/<NNNNN>.png`  
`keypoints` | `EmbeddedDocumentField(Keypoints)` | Human-annotated 2D sparse correspondences from the Toon3D Labeler, stored as a single `fo.Keypoint` with `label="correspondence"`. Coordinates are normalised to `[0, 1]`. Only valid (visible) points are included. `None` if no valid points exist for the frame.  
`scene` | `StringField` | Scene name, e.g. `"bobs-burgers"`  
`frame_idx` | `IntField` | Zero-based frame index within the scene (matches the SfM frame order after filtering invalid images)  
`n_frames` | `IntField` | Total number of valid frames in this scene  
`camera` | `DictField` | Camera parameters recovered by the Toon3D SfM pipeline (see below)  
  
**`camera` dict schema:**

Key | Type | Description  
---|---|---  
`fl_x` | `float` | Learned focal length in pixels, x-axis  
`fl_y` | `float` | Learned focal length in pixels, y-axis  
`cx` | `float` | Principal point x (half image width)  
`cy` | `float` | Principal point y (half image height)  
`w` | `int` | Image width in pixels  
`h` | `int` | Image height in pixels  
`transform_matrix` | `list[list[float]]` | 4Ã4 camera-to-world matrix in OpenCV / Nerfstudio convention. Camera 0 is placed at the world origin; all other cameras are expressed relative to it.  
  
The `transform_matrix` coordinate convention matches Nerfstudioâs OPENCV camera model. A coordinate flip `diag(1, -1, -1)` is applied to the internal toon3d rotation before writing, converting from the SfM-internal convention to Nerfstudio convention. In world space, camera 0 looks in the **+Z** direction with **âY** as the image-up axis.

* * *

#### `scene_3d` slice#

Each group has exactly one `scene_3d` sample. Its **`filepath`** points to a `.fo3d` scene file (written by `fo3d.Scene.write(..., resolve_relative_paths=True)`).

**Fields:**

Field | Type | Description  
---|---|---  
`group` | `EmbeddedDocumentField(Group)` | Group membership â same group id as the frame slices for this scene  
`tags` | `ListField(StringField)` | `[scene_name]`  
`scene` | `StringField` | Scene name  
`n_frames` | `IntField` | Number of per-frame PLY nodes in the scene  
  
**`.fo3d` scene contents:**

Each `.fo3d` file contains:

  * **`camera`** â a `PerspectiveCamera` with:

    * `up = "-Y"` â consistent with the SfM coordinate convention where image-up maps to world âY

    * `position` â auto-computed as the point cloud centroid offset by 1.5Ã the scene diagonal along âZ, placing the viewer behind the scene looking forward

    * `look_at` â centroid of the combined `all.ply` point cloud

    * `fov = 50.0Â°`, `near = 0.1`, `far = 2000.0`

  * **N` PlyMesh` nodes** (one per frame) with:

    * `name` = `"frame_NNNNN"` (zero-padded 5 digits)

    * `ply_path` â absolute path to `outputs/<scene>/run/<timestamp>/nerfstudio/plys/<NNNNN>.ply`

    * `is_point_cloud = False` (set to `True` for point cloud rendering)

    * `center_geometry = False` â the PLYs are already in SfM world space and must not be re-centred

    * `default_material` â `MeshBasicMaterial` with a distinct per-frame colour (cycles through 13 colours: `#e63946`, `#457b9d`, `#2a9d8f`, `#e9c46a`, `#f4a261`, `#264653`, `#a8dadc`, `#bc4749`, `#6a994e`, `#7209b7`, `#3a0ca3`, `#f77f00`, `#4cc9f0`)

The PLY format is ASCII with per-vertex fields `x y z red green blue` (float32 x/y/z, uint8 RGB). Points are in SfM world space â back-projected from Marigold depth maps through the recovered camera poses. All per-frame PLYs share the same coordinate system and can be composed directly.




* * *

### How the Dataset Was Built#

  1. **SfM outputs generated** with `tnd-run` (from the `toon3d` package) for all 12 scenes. Each run reads `toon3d-dataset/<scene>/` (images, `.pt` depth tensors, `points.json`) and writes Nerfstudio-format outputs to `outputs/<scene>/run/<timestamp>/nerfstudio/`.

  2. **`.fo3d` scene files written** â one per scene â into `outputs/<scene>/run/<timestamp>/nerfstudio/fo3d/scene.fo3d`. The camera position is computed programmatically from the `all.ply` centroid and extent.

  3. **FiftyOne grouped dataset created** with `fo.Dataset.add_group_field("group", default="frame_00")`. All 92 samples are added in a single `dataset.add_samples(all_samples)` call.




The build script is `build_dataset.py` at the root of this workspace.

* * *

## Citation#
    
    
    @inproceedings{weber2024toon3d,
      title     = {Toon3D: Seeing Cartoons from New Perspectives},
      author    = {Ethan Weber and Riley Peterlinz and Rohan Mathur and
                   Frederik Warburg and Alexei A. Efros and Angjoo Kanazawa},
      booktitle = {arXiv:2405.10320},
      year      = {2024},
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
