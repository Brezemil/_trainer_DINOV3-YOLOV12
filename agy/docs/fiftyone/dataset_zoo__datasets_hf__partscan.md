---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/partscan.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/partscan)

# Dataset Card for PartScan#

![image/png](https://huggingface.co/datasets/Voxel51/partscan/resolve/main/partscan.gif)

![FiftyOne](https://img.shields.io/badge/FiftyOne-3D%20point%20cloud-orange)

Fine-grained 3D part segmentation is crucial for embodied AI systems that must interact with specific functional components of an object (e.g. a _drawer handle_ rather than the whole _cabinet_). Acquiring dense, part-level 3D annotations is a major bottleneck, so PinPoint3D introduces a 3D data-synthesis pipeline that produces a large-scale, **scene-level** dataset with dense part annotations on sparse, real-world-style scans.

**partscan** has been parsed as a FiftyOne **3D point cloud** dataset of scene-level scans with dense, per-point **part-level** annotations. It is the synthesized dataset introduced for **PinPoint3D** , a framework for fine-grained, multi-granularity 3D part segmentation from a few user clicks. Each sample is a colored point cloud of one scene fragment, rendered in the FiftyOne Appâs 3D viewer.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/partscan", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="PartScan"  # Assign a name to the dataset for identification
    )
    
    # Launch the App
    session = fo.launch_app(dataset)
    
    

## Dataset Details#

### Dataset Description#

This FiftyOne dataset wraps each scan as an `.fo3d` point-cloud scene (`fo3d.PlyMesh`, `is_point_cloud=True`), so the per-point RGB color is rendered directly in the Appâs interactive 3D viewer. Scene/fragment identifiers follow the ScanNet-style `sceneXXXX_YY` naming convention.

  * **Paper:** [PinPoint3D: Fine-Grained 3D Part Segmentation from a Few Clicks](https://arxiv.org/abs/2509.25970) (Zhang et al., SUSTech)

  * **Repo:** https://github.com/Quit123/PinPoint3D

  * **Project Page:** https://pinpoint3d.online/




* * *

## FiftyOne Dataset Structure#

**Dataset name:** `partscan`

**Media type:** `3d`

### Summary#

Property | Value  
---|---  
Samples (scan fragments) | 1,509  
Unique scenes | 707  
Fragments per scene | 1â7  
  
### Per-point data (in each PLY)#

Each point carries `x, y, z` coordinates, `red, green, blue` color, and a `label` part ID. A label of `-1` denotes an unlabeled / ignore point.

### Sample-level fields#

Field | Type | Description  
---|---|---  
`scene_id` | string | Scene identifier, e.g. `scene0002`  
`fragment` | string | Fragment suffix within the scene, e.g. `01`  
`num_points` | int | Total number of points in the scan  
`unique_labels` | list(int) | Distinct part labels present (excluding `-1`)  
`num_labeled_points` | int | Number of points with a valid (`!= -1`) label  
`ignore_fraction` | float | Fraction of points with label `-1` (unlabeled)  
  
## Citation#
    
    
    @article{zhang2025pinpoint3d,
      title   = {PinPoint3D: Fine-Grained 3D Part Segmentation from a Few Clicks},
      author  = {Zhang, Bojun and Ye, Hangjian and Zheng, Hao and Huang, Jianzheng and Lin, Zhengyu and Guo, Zhenhong and Zheng, Feng},
      journal = {arXiv preprint arXiv:2509.25970},
      year    = {2025}
    }
    

## License#

Please refer to the PinPoint3D project for the source datasetâs licensing terms.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
