---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/floorplancad.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/FloorPlanCAD)

# Dataset Card for FloorPlanCAD (test split)#

![image](https://huggingface.co/datasets/Voxel51/FloorPlanCAD/resolve/main/floorplancad.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 5308 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/FloorPlanCAD")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

FloorPlanCAD is a large-scale real-world CAD drawing dataset containing over 15,000 annotated floor plans for panoptic symbol spotting in architectural drawings. The dataset provides line-grained vector annotations for 30 object categories across residential and commercial buildings.

**Key Features:**

  * **Format** : Vector graphics (SVG) with corresponding PNG rasterizations

  * **Scale** : 15,663 CAD drawings (originally 10,094 in v1, updated to 15,663)

  * **Categories** : 30 classes total

    * 28 âthingâ classes (countable instances): doors, windows, furniture, appliances, equipment

    * 2 âstuffâ classes (semantic regions): wall, parking

  * **Annotation Type** : Line-grained primitive-level annotations with semantic and instance labels

  * **Original Split** : 6,382 training / 3,712 testing drawings

  * **Privacy Protected** : Cropped into 20m Ã 20m blocks, 50% retention rate, sensitive text removed



  * **Curated by** : Zhiwen Fanâ , Lingjie Zhuâ , Honghua Li, Xiaohao Chen, Siyu Zhu, Ping Tan (Alibaba A.I. Labs & Simon Fraser University, â Equal contribution)

  * **Funded by** : Alibaba A.I. Labs

  * **Language(s)** : Not applicable (architectural vector graphics)

  * **License** : Creative Commons Attribution-NonCommercial 4.0 License

  * **Project shutdown notice** : As of January 2023, the project was shut down and most participants left the company




### Dataset Sources#

  * **Repository** : https://floorplancad.github.io/ (Note: Project shut down in 2022)

  * **Paper** : Fan et al. âFloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spottingâ (ICCV 2021)




## Uses#

### Direct Use#

This dataset is designed for:

  * **Panoptic symbol spotting** : Detecting both countable object instances and semantic regions in architectural drawings

  * **Instance segmentation** : Identifying individual furniture, fixtures, and building elements

  * **Semantic segmentation** : Recognizing structural elements like walls and parking areas

  * **CAD drawing analysis** : Training models for automated floor plan understanding

  * **Architecture/Engineering/Construction (AEC) applications** : Automated 3D modeling from 2D CAD drawings




### Out-of-Scope Use#

  * **Commercial applications** : Dataset is licensed for non-commercial use only

  * **Privacy-sensitive reconstruction** : The dataset is intentionally cropped and anonymized; attempting to reconstruct original complete floor plans or identify building locations violates privacy protections

  * **As-is architectural design** : The cropped 20m Ã 20m blocks are not complete floor plans suitable for construction




## Dataset Structure#

The converted FiftyOne dataset contains the following structure:
    
    
    <Sample: {
        'id': '690a547c0420c654cb79d521',
        'media_type': 'image',
        'filepath': '../image_data/0000-0003.png',
        'tags': [],
        'metadata': <ImageMetadata: {
            'size_bytes': 7803,
            'mime_type': 'image/png',
            'width': 1000,
            'height': 1000,
            'num_channels': 4,
        }>,
        'created_at': datetime.datetime(2025, 11, 4, 19, 31, 8, 427000),
        'last_modified_at': datetime.datetime(2025, 11, 4, 19, 39, 58, 326000),
        'ground_truth': <Detections: {
            'detections': [
                <Detection: {
                    'id': '690a547c0420c654cb79d520',
                    'attributes': {},
                    'tags': [],
                    'label': 'wall',
                    'bounding_box': [0.30975255, 0.0, 0.69024745, 0.7205705549999999],
                    'mask': array([[255, 255, 255, ...,   0,   0,   0],
                           [255, 255, 255, ...,   0,   0,   0],
                           [255, 255, 255, ...,   0,   0,   0],
                           ...,
                           [255, 255, 255, ...,   0,   0,   0],
                           [255, 255, 255, ..., 255, 255, 255],
                           [255, 255, 255, ..., 255, 255, 255]], dtype=uint8),
                    'mask_path': None,
                    'confidence': None,
                    'index': None,
                }>,
            ],
        }>,
    }>
    

**Object Categories (30 total):**

_Doors (3):_ single_door, double_door, sliding_door

_Windows (4):_ window, bay_window, blind_window, opening_symbol

_Stairs (1):_ stair

_Home Appliances (3):_ gas_stove, refrigerator, washing_machine

_Furniture (11):_ sofa, bed, chair, table, bedside_cupboard, tv_cabinet, half_height_cabinet, high_cabinet, wardrobe, sink, bath

_Equipment (6):_ bath_tub, squat_toilet, urinal, toilet, elevator, escalator

_Stuff Classes (2):_ wall, parking

**Note on class distribution:** Wall and parking together account for ~27% of all annotated primitives. Significant class imbalance exists across categories.

## Dataset Creation#

### Curation Rationale#

The FloorPlanCAD dataset was created to address critical limitations in existing symbol spotting research:

  1. **Scale** : Previous datasets (SESYD with 1,000 synthetic plans, FPLAN-POLY with 42 plans) were too small for deep learning

  2. **Real-world diversity** : Prior datasets lacked the symbol variation seen across different architectural firms and building types

  3. **Vector graphics** : Maintaining CADâs native vector format (rather than rasterization) preserves accuracy and enables graph-based methods

  4. **Panoptic scope** : Traditional symbol spotting focused only on âthingâ instances; this dataset includes âstuffâ classes (walls, parking) for complete scene understanding




### Source Data#

#### Data Collection and Processing#

**Original Data Sources:**

  * 100+ architectural projects from production environments

  * Multiple partner companies and institutions

  * Building types: residential towers, schools, hospitals, shopping malls, office buildings

  * Geographic diversity: Projects from various regions (layer names include Chinese characters indicating Asian sources)




**Technical Processing:**

  * Multi-layer SVG organization (dozens of layers per drawing)

  * Layer-by-layer annotation to reduce clutter

  * Scale handling: Entity lengths range from millimeters to tens of meters (5+ orders of magnitude)

  * Coordinate systems: Metric units (meters) for real-world measurements




#### Who are the source data producers?#

  * **Primary producers** : Architects, engineers, and CAD designers from various companies creating production floor plans

  * **Data providers** : Multiple partner companies and institutions in the AEC industry (anonymized for privacy)

  * **Geographic origin** : Multinational (layer names suggest significant Asian representation)




### Annotations#

#### Annotation Process#

**From SVG to FiftyOne Annotations:**

The conversion from vector SVG to structured annotations involves several stages:

  1. **SVG Primitive Parsing** (using `svgpathtools`):
         
         # For each <path>, <circle>, <ellipse> element:
         - Extract semantic-id (class label 1-35)
         - Extract instance-id (unique instance number or -1 for stuff)
         - Parse geometry:
           * Paths: start point, end point, middle point via path.point(0.5)
           * Circles: center (cx, cy), radius (r)
           * Ellipses: center, radii (rx, ry)
         

  2. **Coordinate Transformation** :

     * SVG coordinates scaled by 10x to match PNG dimensions

     * svg_x * 10 â png_x

     * Maintains accurate spatial relationships

  3. **Instance Grouping** :

     * Primitives grouped by (semantic_id, instance_id) tuple

     * Each unique tuple represents one object instance

     * âStuffâ classes have instance_id = -1 (no individual instances)

  4. **Bounding Box Computation** :
         
         # For each instance:
         - Collect all primitive endpoints and centers
         - Compute axis-aligned bounding box:
           x_min = min(all_x_coordinates)
           y_min = min(all_y_coordinates)
           width = x_max - x_min
           height = y_max - y_min
         - Normalize to [0, 1] by dividing by image dimensions
         

  5. **Segmentation Mask Rendering** :
         
         # For each instance:
         - Create blank mask (image_height Ã image_width)
         - Render each primitive with line_width=3 pixels:
           * Paths: cv2.line() or cv2.polylines()
           * Circles: cv2.circle()
           * Ellipses: cv2.ellipse()
         - Crop mask to bounding box region
         

  6. **FiftyOne Detection Object Creation** :

     * Each instance becomes `fo.Detection()` with:

       * label: mapped class name (e.g., âwallâ, âsingle_doorâ)

       * bounding_box: normalized [x, y, w, h]

       * mask: binary array (if include_masks=True)




#### Who are the annotators?#

  * **Number** : 11 specialist annotators

  * **Time investment** : Over 1,000 hours total annotation effort

  * **Expertise** : Domain specialists familiar with architectural CAD drawings

  * **Quality control** : Layer-by-layer annotation methodology for accuracy

  * **Employer** : Alibaba A.I. Labs (annotation team)




## Citation#

### BibTeX#
    
    
    @InProceedings{Fan_2021_ICCV,
        author    = {Fan, Zhiwen and Zhu, Lingjie and Li, Honghua and Zhu, Siyu and Tan, Ping},
        title     = {FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting},
        booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
        month     = {October},
        year      = {2021},
        pages     = {10128-10137}
    }
    

### APA#

Fan, Z., Zhu, L., Li, H., Zhu, S., & Tan, P. (2021). FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting. In _Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)_ (pp. 10128-10137).

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
