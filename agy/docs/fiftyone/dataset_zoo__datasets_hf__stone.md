---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/stone.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/STONE)

# Dataset Card for STONE#

![image/png](https://huggingface.co/datasets/Voxel51/STONE/resolve/main/stone.gif)

STONE is a large-scale multi-modal dataset for off-road 3D traversability prediction, collected by autonomous ground vehicles across four outdoor environments in South Korea. It provides 7,000 keyframes with surround-view imagery from 6 cameras (1904Ã1200), 128-channel LiDAR scans (230K points), and voxel-level traversability annotations classifying terrain into free, traversable, potentially traversable, and non-traversable regions. Following the nuScenes format, the dataset includes 3D obstacle bounding boxes, ego-pose trajectories, and synchronized multi-sensor data at ~10 Hz. This FiftyOne version contains a stratified sample of 35 scenes (200 frames each) from the full 279-scene collection, organized as grouped samples with 7 slices per keyframe (6 cameras + 1 LiDAR 3D scene).

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 7000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/STONE")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# STONE â FiftyOne Dataset Card#

STONE is a large-scale multi-modal dataset for **off-road 3D traversability prediction** , collected by an autonomous ground vehicle (UGV) across four outdoor environments in South Korea. The dataset follows the nuScenes format and provides surround-view camera imagery, 128-channel LiDAR scans, and voxel-level traversability annotations.

  * **Paper:** Park et al., _âSTONE: A Scalable Multi-Modal Surround-View 3D Traversability Dataset for Off-Road Robot Navigationâ_ , ICRA 2026

  * **arXiv:** https://arxiv.org/abs/2603.09175

  * **License:** CC BY-NC-ND 4.0 (dataset) Â· Apache 2.0 (code)

  * **Format:** nuScenes / Occ3D-nuScenes

  * **Project Page: https://konyul.github.io/STONE-dataset/**




## FiftyOne Dataset Structure#

The dataset is a **grouped dataset** â one group per keyframe, with seven slices:

Slice | Media type | Content  
---|---|---  
`CAM_FRONT` | `image` | 1904 Ã 1200 JPEG, front-facing camera  
`CAM_FRONT_LEFT` | `image` | 1904 Ã 1200 JPEG  
`CAM_FRONT_RIGHT` | `image` | 1904 Ã 1200 JPEG  
`CAM_BACK` | `image` | 1904 Ã 1200 JPEG  
`CAM_BACK_LEFT` | `image` | 1904 Ã 1200 JPEG  
`CAM_BACK_RIGHT` | `image` | 1904 Ã 1200 JPEG  
`LIDAR_TOP` | `3d` | `.fo3d` scene (LiDAR + Traversability + Trajectory layers)  
  
## Sample Fields#

These fields are present on **every sample** across all seven slices.

### Identity & Provenance#

Field | Type | Description  
---|---|---  
`channel` | `StringField` | Sensor name: `CAM_FRONT`, `CAM_BACK`, â¦, `LIDAR_TOP`  
`sample_token` | `StringField` | nuScenes sample token (shared across all 7 slices in a group)  
`scene_token` | `StringField` | nuScenes scene token  
`scene_name` | `StringField` | Human-readable scene ID, e.g. `scene-0053`  
`location` | `StringField` | Recording site: `siheung_lake`, `siheung_farmland`, `siheung_land`, `kwangmyeong_land`  
`vehicle` | `StringField` | Vehicle ID: `n001` â `n004`  
`timestamp` | `IntField` | Unix timestamp in microseconds  
  
### nuScenes Metadata (matching the official nuScenes guide)#

Field | Type | Description  
---|---|---  
`token` | `StringField` | `sample_data` token for this specific sensor record  
`ego_pose_token` | `StringField` | Token into `ego_pose.json` â vehicle pose at this timestamp  
`calibrated_sensor_token` | `StringField` | Token into `calibrated_sensor.json` â intrinsics & extrinsics  
`is_key_frame` | `BooleanField` | Always `True` (STONE only contains keyframes)  
`prev` | `StringField` | Previous `sample_data` token for this sensor (empty at scene start)  
`next` | `StringField` | Next `sample_data` token for this sensor (empty at scene end)  
`sample_prev` | `StringField` | Previous nuScenes sample token in the scene  
`sample_next` | `StringField` | Next nuScenes sample token in the scene  
  
### Labels#

Field | Type | Slices | Description  
---|---|---|---  
`ground_truth` | `fo.Detections` | LIDAR_TOP | 3D obstacle annotations. Each `fo.Detection` carries `location=[x,y,z]`, `rotation=[roll,pitch,yaw]`, `dimensions=[l,w,h]` in the LiDAR sensor frame, plus `num_lidar_pts` and `instance_token`  
`cuboids` | `fo.Polylines` | cameras | 3D bounding boxes projected onto each camera as wireframe outlines using `fo.Polyline.from_cuboid()`. Filtered to boxes with all corners in front of the camera  
`ground_truth_2d` | `fo.Detections` | cameras | Flat 2D bounding boxes from the pre-computed `bbox_2d` field in `sample_annotation.json`. Normalised `[x, y, w, h]` in `[0, 1]` space  
`terrain` | `fo.Classification` | all | Dominant traversability class in the frameâs voxel grid. `label` â `{free, traversable, potentially_traversable, non_traversable}`. `confidence` = fraction of labeled voxels in that class  
`trajectory_2d` | `fo.Polylines` | cameras | Projected path of the next 30 ego-pose waypoints (~3 seconds ahead) into the camera image plane. Present on ~83% of frames (absent near scene end)  
  
### Traversability Fractions#

These fields are on all slices, derived from `gts/<scene>/<token>/labels.npz`.

Field | Type | Description  
---|---|---  
`pct_free` | `FloatField` | Fraction of labeled voxels classified as Free (class 0)  
`pct_traversable` | `FloatField` | Fraction classified as Traversable (class 1)  
`pct_potentially_traversable` | `FloatField` | Fraction classified as Potentially Traversable (class 2)  
`pct_non_traversable` | `FloatField` | Fraction classified as Non-Traversable (class 3)  
  
* * *

## LIDAR_TOP `.fo3d` Scene#

Each LIDAR_TOP sample points to a `.fo3d` scene file containing three stacked point cloud layers:

Layer | Shading | Source | Description  
---|---|---|---  
`LiDAR` | `height` | `samples/LIDAR_TOP/*.pcd` | 230,400-point raw scan from Hesai OT128. Points coloured by Z elevation via the viridis colorscale  
`Traversability` | `rgb` | `samples/VOXEL_OVERLAY/*_voxels.pcd` | ~140K points from the same scan, coloured by traversability class. Each pointâs class is looked up from the voxel grid after transforming from LiDAR sensor frame to ego frame  
`Trajectory` | `rgb` | `samples/TRAJECTORY/*_traj.pcd` | All 200 ego-pose waypoints for the scene, transformed to the current frameâs LiDAR sensor frame. Blue = past Â· White = current Â· Yellow = future  
  
Camera configuration: `defaultCameraPosition = {x: -15, y: 0, z: 10}` (15 m behind, 10 m above), `up = "Z"` (NuScenes Z-up convention), set via `dataset.app_config.plugins["3d"]`.

* * *

## Traversability Classes#

Class ID | Label | `terrain.label` value | Colour in viewer  
---|---|---|---  
0 | Free | `free` | green `rgb(50, 230, 50)`  
1 | Traversable | `traversable` | yellow `rgb(230, 230, 50)`  
2 | Potentially Traversable | `potentially_traversable` | orange `rgb(255, 153, 0)`  
3 | Non-Traversable | `non_traversable` | red `rgb(230, 25, 25)`  
  
The voxel grid has shape `(200, 200, 16)` â a 40 m Ã 40 m Ã 3.2 m volume centred on the vehicle at 0.2 m resolution. Value `255` = unoccupied.

* * *

## Citation#
    
    
    @inproceedings{park2026stone,
      title={STONE: A Scalable Multi-Modal Surround-View 3D Traversability Dataset for Off-Road Robot Navigation},
      author={Park, Konyul and Kim, Daehun and Oh, Jiyong and Yu, Seunghoon and Park, Junseo
              and Park, Jaehyun and Shin, Hongjae and Cho, Hyungchan and Kim, Jungho and Choi, Jun Won},
      booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
      year={2026}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
