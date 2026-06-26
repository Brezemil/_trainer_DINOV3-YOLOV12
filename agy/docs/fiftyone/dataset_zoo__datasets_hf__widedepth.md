---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/widedepth.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/widedepth)

# Dataset Card for WideDepth in FiftyOne#

![image/png](https://huggingface.co/datasets/Voxel51/widedepth/resolve/main/widedepth.gif)

[FiftyOne](https://docs.voxel51.com/) dataset for [WideDepth](https://ilyaind.github.io/WideDepth/) â an indoor fisheye depth-estimation benchmark (ICRA 2026) with millimeter-accurate ground-truth depth and disparity rendered from high-resolution LiDAR scans.

We use one fixed camera configuration from the full WideDepth benchmark â 195Â° FOV, 300 mm focal length, CENTER stereo position â across all 101 indoor scenes.

The full Hub release has many combinations (4 FOVs Ã 5 focal lengths Ã 3 positions, plus multiple RGB/depth/disparity views per config). We standardize on the widest FOV setting highlighted in the paperâs hardest evaluations, so every scene shares the same virtual rig instead of mixing 60+ configs per scene.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/widedepth", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="WideDepth"  # Assign a name to the dataset for identification
    )
    
    # Launch the App
    session = fo.launch_app(dataset)
    
    

## Dataset Soureces#

  * **Project page:** https://ilyaind.github.io/WideDepth/

  * **Hugging Face:** https://huggingface.co/datasets/IlyaInd/WideDepth

  * **Paper:** https://arxiv.org/pdf/2605.24074v1

  * **Video overview:** https://www.youtube.com/watch?v=zmxO8p5tIB8




* * *

## About WideDepth#

WideDepth provides synthetic stereo RGB, dense depth, and disparity for **101 indoor scenes** across multiple camera configurations. This FiftyOne dataset uses a single fixed rig per scene:

Parameter | Value  
---|---  
FOV | **195Â°** (widest setting in the benchmark)  
Focal length | **300 mm**  
Stereo position | **CENTER**  
  
**Known gaps:** Scenes `096_092_000` and `097_092_270` are missing the `pano_crop` view and have no 3D slice.

* * *

## Dataset summary#

Property | Value  
---|---  
**Name** | `widedepth_195fov_300mm_center`  
**Type** | Grouped (multimodal)  
**Groups** | 101 (one per scene)  
**Total samples** | 398  
**Default slice** | `pano_crop`  
  
* * *

## Group structure#

Each group is one scene (e.g. `001_057_000`) with up to four slices:

Slice | Media type | Description  
---|---|---  
`fisheye` | image | Fisheye RGB + depth  
`pano` | image | Equirectangular RGB + depth + disparity  
`pano_crop` | image | Cropped equirectangular RGB + depth + disparity  
`pointcloud` | 3d | Colored 3D point cloud (`fo3d`) from the `pano_crop` view  
  
WideDepth ships RGB, depth, and disparity only â not ready-made point clouds. For this dataset, we backprojected the `pano_crop` ground-truth depth (metric, millimeter-accurate) into 3D using the paperâs equirectangular camera model, colored each point from the matching RGB pixel, and packaged the result as an fo3d scene for the FiftyOne 3D viewer. Each cloud is a single-view snapshot from one capture position, not a full room reconstruction.
    
    
    Group: scene_id = "001_057_000"
     fisheye      â  image
     pano         â  image
     pano_crop    â  image  (default)
     pointcloud   â  3d
    

Switch slices in the App to compare projections or open the 3D view for the same capture.

* * *

## Sample fields#

Field | Type | Description  
---|---|---  
`filepath` | `str` | Path to the RGB image or `fo3d` scene file  
`group` | `fo.Group` | Slice identifier within the scene group  
`scene_id` | `str` | Scene name, e.g. `001_057_000`  
`fov` | `str` | `195FOV`  
`focal_mm` | `str` | `300mm`  
`position` | `str` | `CENTER`  
`view` | `str` | `fisheye`, `pano`, `pano_crop`, or `pointcloud`  
  
* * *

## Labels#

Depth and disparity are stored as **`fo.Heatmap`** labels on the image slices (not as separate samples).

Field | Type | On slices  
---|---|---  
`depth` | `fo.Heatmap` | `fisheye`, `pano`, `pano_crop`  
`disparity` | `fo.Heatmap` | `pano`, `pano_crop`  
  
Depth and disparity maps are **16-bit PNG** ground truth in millimeters. Zero values indicate invalid or masked regions (common on wide panoramic views).

* * *

## Citation#
    
    
    @article{indyk2026widedepth,
      title   = {WideDepth: Millimeter-Accurate Benchmark for Fisheye Depth Estimation},
      author  = {Indyk, Ilia and Penshin, Ignat and Sosin, Ivan and Monastyrny, Maxim and Valenkov, Aleksei and Makarov, Ilya},
      journal = {arXiv preprint arXiv:2605.24074},
      year    = {2026},
      url     = {https://arxiv.org/abs/2605.24074}
    }
    

## Related links#

  * [WideDepth project page](https://ilyaind.github.io/WideDepth/)

  * [Hugging Face: IlyaInd/WideDepth](https://huggingface.co/datasets/IlyaInd/WideDepth)

  * [FiftyOne depth estimation guide](https://docs.voxel51.com/getting_started/depth_estimation/01_loading_depth_data.html)

  * [FiftyOne 3D support](https://docs.voxel51.com/user_guide/3d.html)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
