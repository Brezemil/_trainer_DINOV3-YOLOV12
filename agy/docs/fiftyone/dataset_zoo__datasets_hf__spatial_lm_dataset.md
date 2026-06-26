---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/spatial_lm_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/spatial_lm_dataset)

# Dataset Card for Spatial LM#

![image/png](https://huggingface.co/datasets/Voxel51/spatial_lm_dataset/resolve/main/spatial_lm.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) 3D dataset with 19,992 samples representing indoor room point clouds with structured 3D layout and object annotations from the [SpatialLM](https://manycore-research.github.io/SpatialLM) benchmark.

Each sample is an `.fo3d` scene containing a coloured point cloud with overlaid 3D bounding box annotations for walls, doors, windows, and furniture/objects â all browsable and queryable in the FiftyOne App.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/spatial_lm_dataset", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="spatial_lm_dataset"  # Assign a name to the dataset for identification
    )
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Viewer Tips#

  * The point cloud renders at full RGB colour by default.

  * Toggle **walls** / **doors** / **windows** / **objects** in the sidebar to overlay coloured 3D bounding boxes on the point cloud.

  * Filter by `room_type`, `split`, or `sample_type` for targeted exploration.

  * The viewer uses a **Z-up** coordinate convention (floor at Z = 0, height along +Z).




## Dataset Details#

### Dataset Description#

SpatialLM is a large-scale synthetic indoor scene dataset created by [Manycore Tech Inc.](https://www.kujiale.com/) and researchers at HKUST. It contains point clouds from 12,328 diverse indoor scenes comprising 54,778 rooms, each paired with ground-truth 3D annotations for architectural layout (walls, doors, windows) and oriented object bounding boxes across 59 semantic categories. The scenes are sourced from professional interior designs on the Kujiale online platform and rendered with a production-grade rendering engine.

This FiftyOne version represents 19,992 room-level samples as `.fo3d` 3D scenes. Each sample pairs a PLY point cloud (rendered as coloured points in world-space coordinates) with `fo.Detections` fields for walls, doors, windows, and objects â making all annotations browsable, filterable, and queryable directly in the FiftyOne Appâs 3D viewer.

  * **Curated by:** Yongsen Mao, Junhao Zhong, Chuan Fang, Jia Zheng, Rui Tang, Hao Zhu, Ping Tan, Zihan Zhou â Manycore Tech Inc. and Hong Kong University of Science and Technology

  * **FiftyOne integration by:** [Harpreet Sahota](https://huggingface.co/harpreetsahota)

  * **Language(s):** en (annotations are English category labels)

  * **License:** CC-BY-NC-4.0




### Dataset Sources#

  * **Project page:** [manycore-research.github.io/SpatialLM](https://manycore-research.github.io/SpatialLM)

  * **Paper:** [arXiv:2506.07491](https://arxiv.org/abs/2506.07491) (NeurIPS 2025)

  * **Code:** [github.com/manycore-research/SpatialLM](https://github.com/manycore-research/SpatialLM)

  * **Original dataset:** [huggingface.co/datasets/manycore-research/SpatialLM-Dataset](https://huggingface.co/datasets/manycore-research/SpatialLM-Dataset)

  * **Model weights:** [huggingface.co/manycore-research/SpatialLM1.1-Qwen-0.5B](https://huggingface.co/manycore-research/SpatialLM1.1-Qwen-0.5B)




## FiftyOne Dataset Structure#

### Scene Format#

Each sampleâs `filepath` points to an `.fo3d` scene file containing a single `fo.PlyMesh` node with `is_point_cloud=True`. The PLY files carry per-vertex RGB colours which FiftyOne renders automatically. `center_geometry=False` preserves the original world-space coordinates so annotations stay spatially aligned with the point cloud.

The scene uses a dark background (`#1a1a2e`) and a `fo.PerspectiveCamera` with `up="Z"`.

### Sample Fields#

Field | Type | Description  
---|---|---  
`filepath` | `str` | Path to the `.fo3d` scene file  
`sample_id` | `str` | Unique identifier following `{scene_id}_{room_id}_{sample}` convention (e.g., `scene_001523_00_2`)  
`scene_id` | `str` | Identifier for the multi-room apartment scene  
`room_type` | `str` | Functional room type (e.g., `bedroom`, `living_room`, `kitchen`, `bathroom`, `balcony`)  
`sample_type` | `int` | Point cloud sampling configuration: **0** = 8 panoramic views (most complete), **1** = 8 perspective views (most sparse), **2** = 16 perspective views, **3** = 24 perspective views  
`split` | `str` | Dataset partition: `train`, `val`, `test`, or `reserved`  
`walls` | `fo.Detections` | Wall annotations as 3D bounding boxes  
`doors` | `fo.Detections` | Door annotations as 3D bounding boxes  
`windows` | `fo.Detections` | Window annotations as 3D bounding boxes  
`objects` | `fo.Detections` | Furniture/object annotations as oriented 3D bounding boxes  
  
### 3D Detection Fields#

All annotation fields use `fo.Detection` with 3D attributes:

Attribute | Description  
---|---  
`label` | Semantic category (e.g., `wall`, `door`, `window`, `sofa`, `bed`)  
`location` | `[x, y, z]` centre position in world-space coordinates  
`dimensions` | `[sx, sy, sz]` bounding box extents in metres  
`rotation` | `[rx, ry, rz]` Euler rotation; walls and openings use yaw (Z-rotation) derived from wall endpoints  
  
**Walls** have `tags` containing the wall ID (e.g., `wall_0`). **Doors** and **windows** have `tags` containing both the opening ID and the parent wall ID they are attached to (e.g., `["door_0", "wall_16"]`).

A minimum thickness of 0.05 m is enforced on walls and openings so they remain visible in the 3D viewer.

### Coordinate System#

The dataset uses a **Z-up** convention: the floor sits at Z = 0, height extends along +Z. Coordinates are quantized into 1,280 bins at 2.5 cm resolution in the original SpatialLM format and stored as continuous float values in FiftyOne.

### Dataset Splits#

Split | Scenes | Point Cloud Samples  
---|---|---  
Train | 11,328 | ~199,286  
Val | 500 | 500  
Test | 500 | 500  
Reserved | â | â  
  
Multiple point cloud samples of the same room (varying observation completeness) exist in the training set. Val/test splits use a single random sample per room.

## Object Categories#

The dataset annotates 59 object categories (excluding walls, doors, and windows) organised by function:

Super Category | Categories  
---|---  
**Seating** | sofa, chair, dining_chair, bar_chair, stool  
**Bedding** | bed, pillow  
**Cabinetry** | wardrobe, nightstand, tv_cabinet, wine_cabinet, bathroom_cabinet, shoe_cabinet, entrance_cabinet, decorative_cabinet, washing_cabinet, wall_cabinet, sideboard, cupboard  
**Tables** | coffee_table, dining_table, side_table, dressing_table, desk  
**Kitchen** | integrated_stove, gas_stove, range_hood, microwave_oven, sink, stove, refrigerator  
**Bathroom** | hand_sink, shower, shower_room, toilet, tub  
**Lighting** | illumination, chandelier, floor_standing_lamp  
**Decoration** | wall_decoration, painting, curtain, carpet, plants, potted_bonsai  
**Electronics** | tv, computer, air_conditioner, washing_machine  
**Other** | clothes_rack, mirror, bookcase, cushion, bar, screen, combination_sofa, dining_table_combination, leisure_table_and_chair_combination, multifunctional_combination_bed  
  
Small objects with all side lengths below 15 cm are filtered out. The dataset contains 412,932 annotated object instances from 35,426 unique CAD models.

## Dataset Creation#

### Curation Rationale#

SpatialLM was created to address the lack of large-scale, high-quality datasets that provide **both** architectural layout annotations (walls, doors, windows) and 3D object bounding boxes for indoor scenes. Existing real-world datasets like ScanNet and ScanCAD are limited in scale (hundreds to low thousands of scenes) and typically provide only object annotations. Existing synthetic alternatives either lack visual realism (ProcTHOR, ASE â procedurally generated) or are too small (Hypersim: 461 scenes, HSSD: 211 scenes). SpatialLM fills this gap by leveraging professionally designed interiors at scale.

### Source Data#

#### Data Collection and Processing#

The 3D scenes originate from a large repository of interior designs on [Kujiale](https://www.kujiale.com/), an online interior design platform. Most designs were created by professional designers for real-world production use. The authors parsed each 3D house model into individual rooms and applied filtering rules, yielding 12,328 distinct scenes with 54,778 rooms.

For each scene, photo-realistic RGBD images were rendered using a production-grade rendering engine. Camera trajectories traversing each room were simulated, with images captured at 0.5 m intervals. Point clouds were then reconstructed from these RGBD renders. Each room has up to 4 point cloud sampling configurations varying in observation completeness (8 panoramic views through 24 perspective views).

#### Who are the source data producers?#

Professional interior designers using the Kujiale platform. The scenes reflect real-world Chinese residential interior design conventions and standards.

### Annotations#

#### Annotation process#

Annotations are derived directly from the source 3D scene geometry â no manual annotation was required. Walls, doors, and windows are extracted from the architectural model. Object bounding boxes (oriented 3D boxes with semantic categories) are computed from the placed 3D assets in the design. Objects are annotated across 59 categories, with small objects

# Citation#
    
    
    @inproceedings{SpatialLM,
      title     = {SpatialLM: Training Large Language Models for Structured Indoor Modeling},
      author    = {Mao, Yongsen and Zhong, Junhao and Fang, Chuan and Zheng, Jia and Tang, Rui and Zhu, Hao and Tan, Ping and Zhou, Zihan},
      booktitle = {Advances in Neural Information Processing Systems},
      year      = {2025}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
