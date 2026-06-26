---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/dronescapes2_annotated_train_set.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/dronescapes2_annotated_train_set)

# Dataset Card for DroneScapes2 (annotated train set)#

![image/png](https://huggingface.co/datasets/Voxel51/dronescapes2_annotated_train_set/resolve/main/dronescapes2.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 218 samples. Itâs [a subset of this split](https://huggingface.co/datasets/Meehai/dronescapes2/tree/main/data/train_set_annotated_only) from the original repo.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/dronescapes2_annotated_train_set")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Dronescapes is a multi-modal aerial imagery dataset captured from drones, designed for multi-task learning research including semantic segmentation, depth estimation, and surface normal prediction. The dataset contains RGB images at 960Ã540 resolution along with multiple annotation modalities across three distinct test scenes (Barsana, Comana, and Norway). This version is formatted for FiftyOne with comprehensive field structure and mask targets.

  * **Curated by:** Alina Marcu, Mihai Pirvu, Dragos Costea, Emanuela Haller, Emil Slusanschi, Ahmed Nabil Belbachir, Rahul Sukthankar, Marius Leordeanu

  * **Language(s) (NLP):** Not applicable (computer vision dataset)

  * **License:** [More Information Needed]




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/Meehai/dronescapes

  * **Paper:** [Self-Supervised Hypergraphs for Learning Multiple World Interpretations](https://openaccess.thecvf.com/content/ICCV2023W/LIMIT/papers/Marcu_Self-Supervised_Hypergraphs_for_Learning_Multiple_World_Interpretations_ICCVW_2023_paper.pdf) (ICCV 2023 Workshop)

  * **Website:** https://sites.google.com/view/dronescapes-dataset




## Uses#

### Direct Use#

This dataset is suitable for:

  * Multi-task learning research combining semantic segmentation, depth estimation, and surface normal prediction

  * Aerial scene understanding and drone navigation research

  * Safe landing zone detection for UAVs

  * Benchmarking computer vision models on aerial imagery

  * Multi-modal learning with various sensor modalities

  * Comparative analysis across different segmentation models (COCO, Mapillary, ensemble methods)




## Dataset Structure#

### FiftyOne Dataset Format#

### Sample Fields#

**Core Fields:**

  * `filepath`: Path to RGB image file

  * `metadata`: Image metadata including size_bytes, mime_type, width, height, num_channels

  * `tags`: List of tags for organizational purposes

  * `id`, `created_at`, `last_modified_at`: Standard FiftyOne tracking fields




**Video Context Fields:**

  * `location`: Classification field indicating scene/location

  * `video_name`: Original video sequence name

  * `video_type`: Type/category of video

  * `frame_number`: Frame index within video sequence

  * `has_ground_truth`: Boolean indicating availability of SfM-derived ground truth




**Depth and Normal Fields (Heatmap type):**

  * `ground_truth_depth`: SfM-derived depth maps

  * `ground_truth_normals`: SfM-derived surface normals

  * `depth_marigold`: Monocular depth predictions from Marigold model

  * `normals_svd`: Surface normal predictions from SVD-based method




**Semantic Segmentation Fields (Segmentation type):**

_Original Model Outputs:_

  * `semantic_coco`: 133-class COCO panoptic segmentation

  * `semantic_mapillary_swin`: 65-class Mapillary segmentation (Swin backbone)

  * `semantic_mapillary_r50`: 65-class Mapillary segmentation (ResNet-50 backbone)




_Converted to 8-Class Dronescapes Format:_

  * `semantic_converted_mapillary_swin`: 8-class (land, forest, residential, road, little-objects, water, sky, hill)

  * `semantic_converted_mapillary_r50`: 8-class conversion

  * `semantic_converted_coco`: 8-class conversion

  * `semantic_ensemble`: 8-class ensemble prediction




_Binary Segmentation Tasks:_

  * `buildings`: Building detection (binary: other/buildings)

  * `buildings_nearby`: Nearby buildings detection

  * `sky_and_water`: Sky and water segmentation

  * `transportation`: Transportation infrastructure

  * `containing`: Containing regions

  * `vegetation`: Vegetation detection

  * `safe_landing_no_sseg`: Safe landing zones without semantic input

  * `safe_landing_semantics`: Safe landing zones using semantic information




**Tiling Fields:**

  * `slice_x`: X-coordinate for spatial slicing/tiling

  * `slice_y`: Y-coordinate for spatial slicing/tiling




### Class Mappings#

**8-Class Dronescapes Semantic Segmentation:**
    
    
    0: land
    1: forest
    2: residential
    3: road
    4: little-objects
    5: water
    6: sky
    7: hill
    

**65-Class Mapillary Segmentation:** Includes detailed urban and natural scene categories (Bird, Ground Animal, Curb, Fence, Road, Building, Vegetation, Vehicle types, etc.)

**133-Class COCO Panoptic:** Comprehensive object and stuff categories from COCO dataset

**Binary Task Classes:** All binary tasks use: `{0: "other", 1: [task_name]}`

### Saved Views#

  * **scenes** : Groups samples by `video_name`, ordered by `frame_number` for temporal visualization




### Data Organization#

Samples are organized by video sequences with frame-level annotations. The `has_ground_truth` field indicates which frames have SfM-derived depth and normal ground truth available (not all frames have this due to SfM reconstruction limitations).

## Dataset Creation#

### Curation Rationale#

The dataset was created to enable research in multi-task learning for aerial scene understanding, particularly focused on enabling safe autonomous drone navigation through simultaneous semantic segmentation, depth estimation, and surface normal prediction.

### Source Data#

#### Data Collection and Processing#

Data was collected from drone flights across multiple scenes in Romania and Norway. Ground truth depth and surface normals were generated using Structure from Motion (SfM) techniques. Semantic segmentation was manually annotated by human annotators for 8 semantic classes relevant to drone navigation. Additional predictions were generated using state-of-the-art models (COCO, Mapillary, Marigold, SVD) and converted to the 8-class format for consistency.

#### Who are the source data producers?#

Aerial video footage was captured by the research team using DJI drones across various landscapes including rural areas (Barsana, Comana) and Norwegian terrain.

### Annotations#

#### Annotation process#

  * **Semantic Segmentation:** Human annotators labeled frames with 8 semantic classes

  * **Depth and Normals:** Generated using SfM reconstruction from video sequences

  * **Binary Tasks:** Derived from the 8-class semantic segmentation through class grouping

  * **Model Predictions:** Multiple semantic segmentation models (COCO, Mapillary variants) applied and converted to unified format




## Citation#

**BibTeX:**
    
    
    @InProceedings{Marcu_2023_ICCV,
        author = {Marcu, Alina and Pirvu, Mihai and Costea, Dragos and Haller, Emanuela and Slusanschi, Emil and Belbachir, Ahmed Nabil and Sukthankar, Rahul and Leordeanu, Marius},
        title = {Self-Supervised Hypergraphs for Learning Multiple World Interpretations},
        booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops},
        month = {October},
        year = {2023},
        pages = {983-992}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
