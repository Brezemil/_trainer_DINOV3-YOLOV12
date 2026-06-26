---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/transphy3d.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/TransPhy3D)

# Dataset Card for TransPhy3D#

![image/png](https://huggingface.co/datasets/Voxel51/TransPhy3D/resolve/main/transphys3d.gif)

**TransPhy3D (FiftyOne)** is a grouped FiftyOne dataset built from a random subset of the [TransPhy3D](https://huggingface.co/datasets/Daniellesry/TransPhy3D) **test** split. Each group contains one RGB video sequence plus a merged 3D reconstruction of the same scene.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/TransPhy3D", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="TransPhy3D"  # Assign a name to the dataset for identification
    )
    
    # Launch the App
    session = fo.launch_app(dataset)
    
    
    

## Dataset Details#

### Dataset Description#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 51 samples.

The source dataset provides synthetic transparent/reflective object scenes rendered in Blender/Cycles with RGB video frames, 16-bit depth maps, surface normal maps, and per-frame camera calibration.

  * **Source dataset:** [Daniellesry/TransPhy3D](https://huggingface.co/datasets/Daniellesry/TransPhy3D)

  * **Source split used:** `test`

  * **License:** Apache 2.0 (source dataset license)




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/Daniellesry/TransPhy3D

  * **Paper:** [Diffusion Knows Transparency (arXiv:2512.23705)](https://arxiv.org/abs/2512.23705)

  * **Project page:** https://daniellli.github.io/projects/DKT/

  * **GitHub:** https://github.com/Daniellli/DKT




* * *

## Sampling From the Source Test Set#

The full TransPhy3D test split contains **131** WebDataset tar sequences.

This FiftyOne dataset uses a **random subset of 51 sequences** (~39% of the test split):

Step | Count | Notes  
---|---|---  
Initial random sample | 33 | ~25% of 131, `random.seed(42)`  
Additional sequences | 18 | disjoint from the first 33, same seed  
**Total in this dataset** | **51** | listed in `data/selected_tars.txt`  
  
Scene type breakdown in this sample:

  * **39** `materials` sequences (`0826_*`)

  * **12** `table_with_robot` sequences (`0827_table_with_robot_*`)




Each selected sequence contains **121 frames**.

* * *

## FiftyOne Dataset Structure#

**Dataset name:** `TransPhy3D`

**Media type:** `group`

**Default group slice:** `video`

### Groups and slices#

There are **51 groups**. Each group has two linked slices:

Slice | Media type | `filepath` | Description  
---|---|---|---  
`video` | `video` | `rgb.mp4` | RGB video assembled from source frames  
`reconstruction` | `3d` | `scene.fo3d` | Merged RGB-colored point cloud for the whole scene  
  
Switch slices in the FiftyOne App to view the video annotations or the 3D reconstruction for the same sequence.

### Sample-level fields#

Present on both slices unless noted:

Field | Type | Description  
---|---|---  
`sequence_id` | string | Sequence prefix, e.g. `0826_0004`  
`scene_type` | string | `materials` or `table_with_robot`  
`tags` | list | `["test"]` on video; `["test", "reconstruction"]` on 3D slice  
  
The import scripts also set `source_tar` and `frame_count` on the video slice when samples are built.

### Frame-level fields (video slice only)#

Each video sample has **121 frame documents** (**6,171** total across the dataset).

Field | FiftyOne type | Description  
---|---|---  
`frame_id` | int | Frame index from source metadata  
`sequence_id` | string | Sequence id for this frame  
`max_depth` | float | Depth scale factor from `depth.json`  
`depth_map` | `Heatmap` | 16-bit depth PNG on disk (`range=[0, 65535]`)  
`normal_map` | `Heatmap` | RGB-encoded normal PNG on disk  
`depth_json` | dict | Parsed contents of `depth.json`  
`camera_extrinsics` | list | 4Ã4 extrinsics matrix  
`camera_intrinsics` | list | 3Ã3 normalized intrinsics matrix  
  
There are **no object detection or segmentation labels**. Supervision is dense per-pixel depth, normals, and camera calibration.

* * *

## 3D Reconstruction#

Each sequence has **one merged point cloud** for the whole scene (not one cloud per frame).

Process (`reconstruct_scenes.py`):

  1. Decode 16-bit depth using paired `depth.json`.

  2. Convert normalized intrinsics to pixel-space `K`.

  3. Back-project depth pixels into world coordinates using per-frame extrinsics.

  4. Color each 3D point from the matching RGB video frame.

  5. Merge all 121 frames into one point cloud.

  6. Downsample with Open3D voxel grid (`voxel_size=0.01` by default).

  7. Write `scene.pcd` and wrap it in `scene.fo3d` for the `reconstruction` group slice.




Default reconstruction settings:

Parameter | Default | Purpose  
---|---|---  
`--stride` | `4` | Subsample every 4th pixel during back-projection  
`--voxel-size` | `0.01` | World-space voxel downsampling  
`--max-depth-ratio` | `0.999` | Drop saturated far-plane depth values  
  
The reconstruction is a **point cloud** , not a mesh. It is intended for interactive 3D viewing in FiftyOne, not watertight surface reconstruction.

* * *

## How to Build / Reload the Dataset#

### Prerequisites#

Download the selected source tars from [Daniellesry/TransPhy3D](https://huggingface.co/datasets/Daniellesry/TransPhy3D)

Run the two scripts in this order:

**Step 1 â Extract assets and build video samples**
    
    
    python import_transphy3d.py --overwrite
    

This:

  * Reads WebDataset tars from `data/tars/test/`

  * Writes processed PNG/JSON assets and `rgb.mp4` files

  * Creates FiftyOne video samples with per-frame heatmaps and metadata




**Step 2 â Reconstruct 3D scenes and build grouped dataset**
    
    
    python reconstruct_scenes.py --build-dataset --overwrite
    

This:

  * Builds merged RGB point clouds (`scene.pcd`, `scene.fo3d`)

  * Replaces/creates the grouped FiftyOne dataset `TransPhy3D` with `video` \+ `reconstruction` slices




* * *

## Citation#

If you use the source TransPhy3D dataset, cite:
    
    
    @article{dkt2025,
      title   = {Diffusion Knows Transparency: Repurposing Video Diffusion for Transparent Object Depth and Normal Estimation},
      author  = {Shaocong Xu and Songlin Wei and Qizhe Wei and Zheng Geng and Hong Li and Licheng Shen and Qianpu Sun and Shu Han and Bin Ma and Bohan Li and Chongjie Ye and Yuhang Zheng and Nan Wang and Saining Zhang and Hao Zhao},
      journal = {https://arxiv.org/abs/2512.23705},
      year    = {2025}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
