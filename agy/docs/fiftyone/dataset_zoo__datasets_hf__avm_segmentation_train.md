---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/avm_segmentation_train.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/AVM_Segmentation_train)

# Dataset Card for AVM (Around View Monitoring) Semantic Segmentation Dataset#

![image/png](https://huggingface.co/datasets/Voxel51/AVM_Segmentation_train/resolve/main/avm_segmentation-mq.gif)

This repository provides a FiftyOne-compatible version of the AVM semantic segmentation dataset for autonomous parking systems, with enhanced metadata and visualization capabilities.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 6763 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("harpreetsahota/AVM_Segmentation_train")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The AVM dataset is a specialized computer vision dataset designed for training semantic segmentation models for autonomous parking systems. It contains birdâs-eye view images from around-view monitoring cameras with pixel-level annotations for parking space detection and obstacle avoidance.

  * **Curated by:** Chulhoon Jang and team at [original repository](https://github.com/ChulhoonJang/avm_dataset)

  * **FiftyOne Integration by:** Harpreet Sahota (Voxel51)

  * **License:** Please refer to the [original dataset repository](https://github.com/ChulhoonJang/avm_dataset) for license information (which currently has no License)




### Dataset Sources#

  * **Original Repository:** [ChulhoonJang/avm_dataset](https://github.com/ChulhoonJang/avm_dataset)




## Uses#

### Direct Use#

This dataset is designed for:

  * **Autonomous Parking Systems** : Training models to detect and navigate into parking spaces

  * **Semantic Segmentation Research** : Benchmarking segmentation algorithms on fisheye/birdâs-eye view images

  * **Parking Space Detection** : Identifying available vs occupied parking spots

  * **Obstacle Detection** : Recognizing curbs, pillars, walls, and other vehicles

  * **360Â° Surround View Systems** : Enhancing camera-based parking assistance features




### Out-of-Scope Use#

This dataset should NOT be used for:

  * Forward-facing autonomous driving (itâs specifically birdâs-eye view)

  * General object detection (annotations are polygon-based for segmentation)

  * High-speed navigation (designed for low-speed parking scenarios)

  * Pedestrian detection (pedestrians are not annotated)




## Dataset Structure#

### Overview#

  * **Total Images** : 6,763 (320 x 160 pixels)

  * **Training Set** : 4,057 images

  * **Test Set** : 2,706 images

  * **Outdoor Images** : 3,614

  * **Indoor Images** : 3,149




### Semantic Classes#

The dataset contains 5 semantic classes with specific RGB color mappings:

Class | Description | RGB Color | Hex Color  
---|---|---|---  
0 | Free Space (drivable area) | [0, 0, 255] | #0000FF (Blue)  
1 | Marker (parking lines) | [255, 255, 255] | #FFFFFF (White)  
2 | Vehicle (other cars) | [255, 0, 0] | #FF0000 (Red)  
3 | Other (curbs, pillars, walls) | [0, 255, 0] | #00FF00 (Green)  
4 | Ego Vehicle (camera car) | [0, 0, 0] | #000000 (Black)  
  
### FiftyOne Fields#

When parsed into FiftyOne, each sample includes:

Field | Type | Description  
---|---|---  
`filepath` | string | Path to the image file  
`split` | string | âtrainâ or âtestâ  
`sample_id` | int | Unique identifier from filename  
`environment` | Classification | âindoorâ or âoutdoorâ (heuristic based on curb presence)  
`parking_type` | Classification | âperpendicularâ or âparallelâ  
`slot_type` | Classification | âclosedâ, âopenedâ, or âno_markerâ  
`polygon_annotations` | Polylines | Normalized polygon coordinates for each object  
`ground_truth` | Segmentation | Pixel-level segmentation mask  
`classes_present` | list | Classes present in the image  
`num_markers` | int | Count of parking marker polygons  
`num_vehicles` | int | Count of vehicle polygons  
`has_curb` | bool | Whether curb is present  
`has_ego_vehicle` | bool | Whether ego vehicle is annotated  
  
## Dataset Creation#

### Curation Rationale#

The dataset was created to address the lack of birdâs-eye view datasets for autonomous parking systems. Most existing datasets focus on forward-facing cameras, but parking assistance requires a top-down perspective to accurately detect parking spaces and navigate safely.

### Source Data#

#### Data Collection and Processing#

  * **Camera Setup** : Around View Monitoring (AVM) system with fisheye cameras

  * **View Angle** : Birdâs-eye view (top-down perspective)

  * **Resolution** : 320 x 160 pixels (optimized for embedded systems)

  * **Environments** : Real parking lots (both indoor parking garages and outdoor lots)

  * **Conditions** : Various lighting conditions, weather (sunny, cloudy, rainy)




#### Who are the source data producers?#

The original dataset was produced by researchers developing autonomous parking systems, likely in an academic or industrial research setting.

### Annotations#

#### Annotation Process#

  1. **Polygon Annotation** : Each object is annotated with precise polygon boundaries in YAML format

  2. **Semantic Masks** : Ground truth masks are generated from polygon annotations

  3. **Multi-polygon Support** : Multiple instances of the same class are supported (e.g., multiple vehicles)

  4. **Coordinate System** : Polygons use image coordinates (0-319 x 0-159)




#### Who are the annotators?#

Information about specific annotators is not provided in the original dataset documentation.

## Personal and Sensitive Information#

The dataset contains images from parking lots but does not include:

  * License plate information (resolution too low)

  * Personally identifiable information

  * Pedestrian annotations

  * Location-specific information




## Bias, Risks, and Limitations#

### Known Limitations#

  1. **Limited Resolution** : 320x160 pixels may not capture fine details

  2. **Geographic Bias** : Dataset may be from specific geographic regions

  3. **Weather Conditions** : Limited representation of extreme weather

  4. **Vehicle Types** : May not include all vehicle types (trucks, motorcycles, etc.)

  5. **Parking Styles** : Primarily perpendicular and parallel parking




### Technical Challenges#

  * **Indoor Reflections** : Reflected lights can be mistaken for parking markers

  * **Fisheye Distortion** : Birdâs-eye view introduces geometric distortions

  * **Class Imbalance** : Some classes (like curbs) appear less frequently




## Recommendations#

  1. **Augmentation** : Apply data augmentation to improve model robustness

  2. **Validation** : Test models on diverse parking environments not in the dataset

  3. **Resolution** : Consider upscaling techniques if higher resolution is needed

  4. **Edge Cases** : Be aware that the dataset may not cover all parking scenarios




### Exploring the Dataset#
    
    
    # View class distribution
    print(dataset.count_values("classes_present"))
    
    # Filter indoor vs outdoor
    indoor = dataset.match(F("environment.label") == "indoor")
    outdoor = dataset.match(F("environment.label") == "outdoor")
    
    # Samples with multiple vehicles
    multi_vehicle = dataset.match(F("num_vehicles") > 2)
    

## Citation#

### BibTeX#
    
    
    @dataset{avm_dataset,
      title={AVM (Around View Monitoring) System Datasets for Auto Parking},
      author={Chulhoon Jang and others},
      year={2020},
      url={https://github.com/ChulhoonJang/avm_dataset}
    }
    

### APA#

Jang, C., et al. (2020). AVM (Around View Monitoring) System Datasets for Auto Parking. GitHub. https://github.com/ChulhoonJang/avm_dataset

## More Information#

### Related Resources#

  * [Original Dataset Repository](https://github.com/ChulhoonJang/avm_dataset)

  * [FiftyOne Documentation](https://docs.voxel51.com)

  * Implementation code for semantic segmentation models (link in original repo)




### Dataset Statistics#

  * Average polygons per class:

    * Ego vehicle: 1.0 polygons (fixed position)

    * Markers: 2.6 polygons per image

    * Vehicles: 2.1 polygons per image

    * Curbs: 1.4 polygons per image (when present)




## Dataset Card Authors#

  * **FiftyOne Integration** : Harpreet Sahota (Voxel51)

  * **Original Dataset** : Chulhoon Jang and team




## Dataset Card Contact#

  * **Original dataset** : See [original repository](https://github.com/ChulhoonJang/avm_dataset)




* * *

## Acknowledgments#

Thanks to the original dataset creators for making this valuable resource available to the research community. The FiftyOne integration enhances the datasetâs usability for modern computer vision workflows.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
