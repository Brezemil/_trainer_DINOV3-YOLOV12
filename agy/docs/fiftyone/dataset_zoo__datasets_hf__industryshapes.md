---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/industryshapes.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/IndustryShapes)

# Dataset Card for IndustryShapes#

![image/png](https://huggingface.co/datasets/Voxel51/IndustryShapes/resolve/main/industryshapes.gif)

IndustryShapes is an RGB-D benchmark dataset for 6D object pose estimation of industrial assembly tools and components. It provides high-quality annotated data of five challenging industrial objectsâcharacterized by weak texture, reflective surfaces, symmetries, and thin structuresâcaptured in realistic industrial assembly environments. The dataset is designed to support both instance-level and novel-object pose estimation approaches, and is the first dataset to include RGB-D static onboarding sequences for model-free methods.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 13012 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/IndustryShapes")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Sources#

  * **Curated by:** Panagiotis Sapoutzoglou, Orestis Vaggelis, Athina Zacharia, Evangelos Sartinas, Maria Pateraki (National Technical University of Athens, Greece)

  * **Funded by:** European HEU programmes SOPRANO (GA No 101120990) and PANDORA (GA No 101135775); data collection supported by Stellantis â Centro Ricerche FIAT (CRF)

  * **License:** MIT

  * **Paper:** [arXiv:2602.05555](https://arxiv.org/abs/2602.05555)

  * **Repository:** [POSE-Lab/IndustryShapes on Hugging Face](https://huggingface.co/datasets/POSE-Lab/IndustryShapes)

  * **Paper:** Sapoutzoglou et al., _IndustryShapes: An RGB-D Benchmark dataset for 6D object pose estimation of industrial assembly components and tools_ , arXiv 2602.05555, 2026

  * **Project page:** https://pose-lab.github.io/IndustryShapes




* * *

## Uses#

### Direct Use#

  * **6D object pose estimation** â both instance-level (known CAD model) and novel-object (model-based and model-free)

  * **Object detection and instance segmentation** in industrial scenes

  * **Depth estimation research** and RGB-D sensor evaluation in industrial settings

  * **Robotic manipulation** â grasping and assembly tasks requiring precise 6D pose




### Out-of-Scope Use#

  * Not suitable for general consumer or household object recognition

  * Not designed for ego-centric or hand-held camera scenarios

  * The five objects are industrial-specific; generalization to other domains should be validated




* * *

## Dataset Structure#

### FiftyOne Sample Fields#

Each sample corresponds to one image. The `dataset_subset` field identifies which part of the dataset the image belongs to.

Field | Type | Description  
---|---|---  
`filepath` | `string` | Absolute path to the 640Ã480 RGB image  
`split` | `string` | `"train"` or `"test"`  
`dataset_subset` | `string` | `"classic"`, `"extended_onboarding"`, or `"extended_office"`  
`scene_id` | `string` | Zero-padded scene identifier (e.g. `"000001"`)  
`image_id` | `string` | Frame index within the scene  
`depth_scale` | `float` | Multiply raw depth values by this to get millimetres (1.0 for classic, 0.1 for extended)  
`camera_intrinsics` | `list[list[float]]` | 3Ã3 camera intrinsic matrix `[[fx,0,cx],[0,fy,cy],[0,0,1]]`  
`depth` | `fo.Heatmap` | Depth map in millimetres; pixel values encode distance in the App colormap  
`ground_truth` | `fo.Detections` | Per-instance annotations (see below)  
`axes` | `fo.Polylines` | Projected coordinate frame (X/Y/Z) at the object origin, for pose visualization  
`bbox3d` | `fo.Polylines` | 12-edge 3D bounding box wireframe projected into image space  
  
### Detection Fields (`ground_truth`)#

Each `fo.Detection` inside `ground_truth` represents one annotated object instance.

Field | Type | Description  
---|---|---  
`label` | `string` | Object class: `object_01` â¦ `object_05`  
`bounding_box` | `[x, y, w, h]` | Normalised 2D bounding box (top-left origin, values in [0, 1])  
`mask` | `bool array` | Binary instance segmentation mask, cropped to the bounding box  
`rotation_matrix` | `list[list[float]]` | 3Ã3 rotation matrix **R** (BOP convention: maps object â camera frame)  
`translation_mm` | `[tx, ty, tz]` | Translation vector in **millimetres** (object origin in camera frame)  
`obj_id` | `int` | Numeric object ID (1â5)  
`visibility` | `float` | Fraction of object surface visible in the image [0, 1]  
  
### Labels#
    
    
    object_01, object_02, object_03, object_04, object_05
    

### Depth Heatmap#

The `depth` field is a `fo.Heatmap` backed by a 16-bit PNG on disk. Each pixel stores the depth in millimetres after applying `depth_scale`. Invalid pixels (no sensor return, or beyond sensor range) are encoded as 0. The `range` stored on the heatmap is the 2ndâ98th percentile of valid pixel values for that frame, used to set the colormap bounds in the FiftyOne App.

### Pose Convention#

Poses follow the **BOP convention** :
    
    
    x_camera = R @ x_object + t
    

where `R` is the 3Ã3 rotation matrix, `t` is the translation in millimetres, and `x_object` is a point in the objectâs coordinate frame.

* * *

## Dataset Creation#

### Curation Rationale#

Most existing 6D pose estimation datasets focus on household or consumer objects in controlled lab environments, which do not reflect the challenges of real-world industrial deployment. IndustryShapes was created to fill this gap by providing industrial objects with challenging physical properties (textureless surfaces, symmetries, thin and reflective parts) in realistic assembly environments, and by explicitly supporting modern model-free methods through the first publicly released RGB-D static onboarding sequences.

### Source Data#

#### Data Collection#

RGB-D data were captured at 640Ã480 resolution using:

  * **Intel RealSense D455** â classic set (industrial and lab scenes)

  * **Intel RealSense D405** â extended set (onboarding and office sequences; closer range)




Synthetic training images for Object 3 were generated with an OpenGL-based renderer using photorealistic CAD model textures. All data are formatted according to the BOP specification.

#### Who are the source data producers?#

The POSE Lab at the National Technical University of Athens (NTUA), Greece. Data were collected at a realistic industrial assembly facility with support from Stellantis â Centro Ricerche FIAT (CRF).

### Annotations#

#### Annotation Process#

Three annotation approaches were used depending on the scene type:

  1. **Marker-based** (lab/turn-table scenes) â ArUco markers provided precise camera poses.

  2. **SfM-based semi-automatic** (industrial scenes) â Structure-from-Motion reconstruction combined with manually defined anchor points on the CAD model established 2Dâ3D correspondences; the PnP problem was then solved per frame.

  3. **Synthetic** â Ground-truth poses are exact by construction.




Annotation accuracy was validated by comparing captured depth against rendered depth at the annotated poses. The mean absolute depth error is **< 12 mm** for the classic set and **â 5 mm** for the extended set â a relative error under 5% of the mean object diameter (254 mm).

### Recommendations#

Benchmark results should be interpreted per-object rather than only overall, as difficulty varies considerably (e.g. Object 5 consistently achieves lower AR than Object 1 across all methods). Users training instance-level methods should note the domain gap between the single-object training scenes and the cluttered multi-object test scenes.

* * *

## Citation#

**BibTeX:**
    
    
    @article{sapoutzoglou2026industryshapes,
      title   = {IndustryShapes: An RGB-D Benchmark dataset for 6D object pose
                 estimation of industrial assembly components and tools},
      author  = {Sapoutzoglou, Panagiotis and Vaggelis, Orestis and Zacharia, Athina
                 and Sartinas, Evangelos and Pateraki, Maria},
      journal = {arXiv preprint arXiv:2602.05555},
      year    = {2026}
    }
    

**APA:**

Sapoutzoglou, P., Vaggelis, O., Zacharia, A., Sartinas, E., & Pateraki, M. (2026). _IndustryShapes: An RGB-D Benchmark dataset for 6D object pose estimation of industrial assembly components and tools_. arXiv:2602.05555.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
