---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/cleardepth.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/ClearDepth)

# Dataset Card for cleardepth#

![image/png](https://huggingface.co/datasets/Voxel51/ClearDepth/resolve/main/cleardepth.gif)

**ClearDepth Transparent (FiftyOne)** is a grouped FiftyOne dataset built from the synthetic transparent-object stereo data described in the ClearDepth paper (SynClearDepth).

Each group represents one indoor scene with stereo RGB video, dense per-pixel labels, and (optionally) a merged 3D point-cloud reconstruction of the same scene.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/ClearDepth", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="ClearDepth"  # Assign a name to the dataset for identification
    )
    
    # Launch the App
    session = fo.launch_app(dataset)
    
    

### Dataset Description#

Scenes are synthetic renders of household rooms containing transparent objects, with left/right stereo views, ground-truth depth, surface normals, instance segmentation, and camera poses.

  * **Source paper:** [ClearDepth: Enhanced Stereo Perception of Transparent Objects for Robotic Manipulation (arXiv:2409.08926)](https://arxiv.org/abs/2409.08926)

  * **Project page:** https://sites.google.com/view/cleardepth




## FiftyOne Dataset Structure#

**Media type:** `group`

**Default group slice:** `left`

### Groups and slices#

There are **204 groups**. Each group links one or more slices of the same scene:

Slice | Media type | Description  
---|---|---  
`left` | `video` | Left stereo camera as an H.264 MP4  
`right` | `video` | Right stereo camera as an H.264 MP4  
`reconstruction` | `3d` | Merged RGB-colored point cloud (`scene.fo3d`), if reconstruction has been run  
  
Switch slices in the FiftyOne App to view the left video, right video, or 3D reconstruction for the same scene. The `left` and `right` slices carry identical sample metadata and matching frame-aligned labels for their respective eyes.

### Sample-level fields#

Present on the video slices (`left`, `right`) and partially mirrored on `reconstruction`:

Field | Type | Description  
---|---|---  
`scene_name` | string | Unique scene id, e.g. `bathroom001_0000_circle000`  
`room_type` | string | Room category (`bathroom`, `diningroom`, `kitchen`, `livingroom`)  
`room_id` | string | Numeric room id within the category  
`room_name` | string | Combined room label, e.g. `bathroom001`  
`scene_variant` | string | Scene variant index from the source export  
`circle_id` | string | Camera trajectory / circle index  
`scene_objects` | list | Objects in the scene; each entry has `object_id`, `category`, `name`, and `transform`  
`object_categories` | list | Sorted unique object categories in the scene  
`tags` | list | `["reconstruction"]` on the `reconstruction` slice only  
  
The `reconstruction` slice repeats the scene metadata fields above but has **no frame labels**.

### Frame-level fields (video slices only)#

Labels are attached to frames on `left` and `right` only:

Field | FiftyOne type | Description  
---|---|---  
`depth` | `Heatmap` | Metric depth stored as a 16-bit PNG (millimeters on disk). App heatmap range defaults to 0â3000 mm. Decode to meters with `depth_m = png_mm / 1000`.  
`normal` | `Heatmap` | RGB-encoded surface normal PNG. Directions use the standard mapping `pixel = 127.5 * (normal + 1)` with unit-length normals.  
`segmentation` | `Segmentation` | Per-pixel instance segmentation mask PNG  
`camera_pose` | list | 4Ã4 camera-to-world pose matrix for that frame  
  
Depth and normal fields reference PNG files on disk via absolute `map_path` values inside the `Heatmap` / `Segmentation` documents.

There are **no bounding-box or classification labels**. Supervision is dense per-pixel depth, normals, segmentation, plus per-frame camera pose and scene-level object metadata.

* * *

## 3D Reconstruction Slice#

When reconstruction has been added, each group includes a `reconstruction` slice pointing at a FiftyOne `scene.fo3d` file that wraps one merged **RGB-colored point cloud** for the whole scene (not one cloud per frame).

The cloud is built by back-projecting depth from the left camera across all frames, coloring points from the corresponding RGB images, and merging them into a single scene-level point cloud. It is intended for interactive 3D viewing in FiftyOne, not watertight mesh reconstruction.

* * *

## Direct Use#

Suitable for:

  * Exploring stereo transparent-object scenes in FiftyOne

  * Training or evaluating dense depth / normal / segmentation models

  * Inspecting camera motion and scene object layout

  * Comparing left vs. right stereo views and 3D reconstructions side by side




## Out-of-Scope Use#

  * **Real-world deployment without adaptation:** source data is synthetic

  * **Object detection benchmarks:** only dense pixel labels and scene object lists are provided

  * **Metric grasp planning from reconstruction alone:** the 3D slice is a merged point cloud for visualization, not a calibrated manipulation pipeline




* * *

## Citation#

If you use the source ClearDepth dataset or method, cite:
    
    
    @article{bai2024cleardepth,
    
      title={ClearDepth: Enhanced Stereo Perception of Transparent Objects for Robotic Manipulation},
    
      author={Bai, Kaixin and Zeng, Huajian and Zhang, Lei and Liu, Yiwen and Xu, Hongli and Chen, Zhaopeng and Zhang, Jianwei},
    
      journal={arXiv preprint arXiv:2409.08926},
    
      year={2024}
    
    }
    
    
    
    @article{bai2025stereoanything,
    
      title={StereoAnything: Advanced Zero-Shot Stereo Imaging for Multi-Finger Grasp Detection with Transparent Objects},
    
      author={Bai, Kaixin and Zhang, Lei and Liu, Yiwen and Chen, Zhaopeng and Zhang, Jianwei},
    
      journal={Authorea Preprints},
    
      year={2025},
    
      doi={10.36227/techrxiv.174612328.83478240/v1},
    
    url={https://doi.org/10.36227/techrxiv.174612328.83478240/v1},
    
      publisher={Authorea}
    
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
