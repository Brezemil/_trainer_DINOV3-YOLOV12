---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/lidar_warehouse_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/lidar-warehouse-dataset)

# Dataset Card for LIDAR Warehouse Dayasey#

![image/png](https://huggingface.co/datasets/Voxel51/lidar-warehouse-dataset/resolve/main/warehouse-lidar.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 3287 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/lidar-warehouse-dataset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Description#

The Warehouse LiDAR Dataset is a 3D object detection dataset captured in warehouse environments using a Velodyne VLP-16 LiDAR sensor. The dataset consists of 3,287 consecutive scans with 6,381 annotated 3D bounding boxes across 5 object classes commonly found in industrial warehouse settings.

  * **Curated by:** Gina Abdelhalim, Kevin Simon (Karlsruher Institut fÃ¼r Technologie), Robert Bensch, Sai Parimi, Bilal Ahmed Qureshi (ANavS GmbH)

  * **Funded by:** Federal Ministry for Economic Affairs and Climate Action (BMWK) as part of the FLOOW project

  * **Language(s) (NLP):** Not applicable (3D point cloud data)

  * **License:** CC-BY-SA-4.0




### Dataset Sources#

  * **Repository:** https://github.com/anavsgmbh/lidar-warehouse-dataset

  * **Paper:** âAutomated AI-based Annotation Framework for 3D Object Detection from LiDAR Data in Industrial Areasâ (SAE Technical Paper 2024-01-2999) - https://www.sae.org/publications/technical-papers/content/2024-01-2999/

  * **Data Download:** https://drive.google.com/drive/folders/1T0hDyBnyY22pwShCDjSK95hzItTqqLqf




## Uses#

### Direct Use#

This dataset is designed for 3D object detection in warehouse environments. Suitable use cases include:

  * Training autonomous warehouse robots for navigation and obstacle avoidance

  * Developing inventory tracking and localization systems

  * Creating safety systems for detecting people, vehicles, and equipment in industrial settings

  * Path planning and routing algorithms for warehouse automation




### Out-of-Scope Use#

This dataset is specific to warehouse environments with a 16-channel LiDAR sensor. It may not generalize well to:

  * Outdoor autonomous driving scenarios

  * Indoor environments significantly different from warehouses

  * Applications requiring higher-resolution point clouds (64+ channels)

  * Detection of object classes not present in the dataset




## Dataset Structure#

### FiftyOne Dataset Structure#

The dataset is structured as a **grouped FiftyOne dataset** with two linked slices per scan:

**Group Structure:**

  * **âimageâ slice** (default): Pre-rendered birdâs-eye view PNG visualizations (3,287 samples)

    * File format: PNG images

    * Contains: Visualization images with bounding boxes already rendered

    * Fields: `scan_id`, `num_points`, `num_detections`, `pcd_path`

  * **âpcdâ slice** : 3D point cloud data with interactive annotations (3,287 samples)

    * File format: PCD (Point Cloud Data)

    * Contains: 3D point clouds with interactive bounding box annotations

    * Fields: `scan_id`, `num_points`, `ground_truth`, `image_path`

    * Point cloud format: (N, 4) array with [x, y, z, intensity]




**Total Samples:** 6,574 (3,287 groups Ã 2 slices)

**3D Bounding Box Format:** Each detection in the `ground_truth` field contains:

  * `label`: Object class (Box, ELFplusplus, CargoBike, FTS, ForkLift)

  * `location`: [x, y, z] center position in meters (sensor-centric coordinates)

  * `dimensions`: [width, length, height] in meters

  * `rotation`: [roll, pitch, yaw] Euler angles in radians (only yaw is used)




**Coordinate System:** Sensor-centric (origin at LiDAR sensor position)

  * X-axis: Forward direction

  * Y-axis: Left direction

  * Z-axis: Up direction




### Statistics#

  * **Total scans:** 3,287

  * **Total annotations:** 6,381 3D bounding boxes

  * **Point cloud size:** Average ~4,879 points per scan (range: 3,868-6,894)

  * **Objects per scan:** Average 1.94 (range: 1-5)

  * **Classes (5):**

    * Box: 2,847 instances (44.6%)

    * ELFplusplus: 1,248 instances (19.6%)

    * CargoBike: 1,205 instances (18.9%)

    * FTS: 600 instances (9.4%)

    * ForkLift: 481 instances (7.5%)




**No train/val/test splits provided** \- users should create their own splits as needed.

## Dataset Creation#

### Curation Rationale#

Created to support research and development in autonomous warehouse systems, particularly for 3D object detection in industrial environments. This is the first open-source 3D point cloud dataset specifically for warehouse environments.

### Source Data#

#### Data Collection and Processing#

  * **Sensor:** Velodyne Puck VLP-16 (16-channel LiDAR)

  * **Collection method:** Moving platform recording consecutive scans in warehouse environment

  * **Processing pipeline:**

    1. LiDAR SLAM used to create dense optimized global 3D point cloud

    2. 3D bounding boxes annotated on the dense point cloud

    3. Annotations automatically reprojected to individual LiDAR scans

    4. This approach ensures efficient and consistent annotation across all scans




#### Who are the source data producers?#

Data collected by Karlsruher Institut fÃ¼r Technologie (KIT) and ANavS GmbH in warehouse environments as part of the FLOOW project investigating autonomous transport of goods in industrial areas.

### Annotations#

#### Annotation process#

The dataset uses an âExtended Pipelineâ approach:

  1. Individual LiDAR scans collected from moving platform

  2. LiDAR SLAM creates a single dense, optimized 3D point cloud of the entire scene

  3. Human annotators place 3D bounding boxes on the dense point cloud

  4. Bounding boxes automatically reprojected to each individual scan

  5. This method provides consistent annotations across all frames




**Annotation format:** Each bounding box defined by:

  * Class name

  * 3D center position (x, y, z) in meters

  * Dimensions (width, length, height) in meters

  * Rotation angle (yaw) in radians




## Citation#

**BibTeX:**
    
    
    @Article{Abdelhalim2024,
      author = {G. Abdelhalim and K. Simon and R. Bensch and S. Parimi and B. A. Qureshi},
      title = {Automated AI-based Annotation Framework for 3D Object Detection from LIDAR Data in Industrial Areas},
      journal = {Society of Automotive Engineers (SAE) Technical Paper},
      year = {2024},
      volume = {2024-01-2999},
      issn = {2688-3627},
      url = {https://www.sae.org/publications/technical-papers/content/2024-01-2999/},
    }
    

**APA:** Abdelhalim, G., Simon, K., Bensch, R., Parimi, S., & Qureshi, B. A. (2024). Automated AI-based Annotation Framework for 3D Object Detection from LIDAR Data in Industrial Areas. SAE Technical Paper 2024-01-2999. https://doi.org/10.4271/2024-01-2999

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
