---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/kitscenes_multimodal.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/kitscenes-multimodal)

# KITScenes Multimodal â FiftyOne Dataset#

![image/png](https://huggingface.co/datasets/Voxel51/kitscenes-multimodal/resolve/main/kitscenes.gif)

A FiftyOne build of **KITScenes Multimodal** (KIT-MRT), a high-fidelity European urban autonomous-driving dataset. Each frame is a synchronized capture from a full robotaxi sensor suite â nine global-shutter cameras giving 360Â° coverage, seven long-range lidars, and three 4D imaging radars â paired with production-grade Lanelet2 HD-map labels, projected lidar depth, the future ego path, and image instance predictions.

This build packages those captures as a **grouped FiftyOne dataset** so every sensor for a given moment lives in one group, and the 3D lidar/radar point cloud sits alongside the camera images. The card below describes exactly what is in the dataset and how it is organized.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 680 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/kitscenes-multimodal")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## At a glance#

|   
---|---  
**Dataset name** | `kitscenes-multimodal`  
**Media type** | `group` (grouped dataset)  
**Samples** | 6,800  
**Frames (groups)** | 680  
**Scenes** | 4 (validation split)  
**Frames per scene** | 100 / 100 / 200 / 280  
**Group slices** | 9 cameras + 1 fused 3D lidar slice  
**Capture rate** | 10 Hz  
**Region** | Frankfurt, Germany (European urban)  
**License** | CC-BY-NC-4.0  
  
A _group_ corresponds to one timestamped frame and holds 10 samples: the 9 camera images plus the fused 3D point cloud. With 680 groups that gives 6,120 image samples + 680 3D samples = 6,800 total.

## Dataset sources#

  * **Curated by:** the KITScenes team at the Institute of Measurement and Control Systems (MRT), Karlsruhe Institute of Technology (KIT), and the FZI Research Center for Information Technology â Richard Schwarzkopf and Fabian Immel (joint first authors), Jan-Hendrik Pauls (project lead), Christoph Stiller, and collaborators. This FiftyOne build was prepared by Harpreet Sahota (Voxel51).

  * **Language:** English

  * **License:** CC-BY-NC-4.0




Resource | Link  
---|---  
Original dataset (Hugging Face) | [KIT-MRT/KITScenes-Multimodal](https://huggingface.co/datasets/KIT-MRT/KITScenes-Multimodal)  
Single-scene preview (Hugging Face) | [KIT-MRT/KITScenes-Multimodal-Sample](https://huggingface.co/datasets/KIT-MRT/KITScenes-Multimodal-Sample)  
Python API / devkit (GitHub) | [KIT-MRT/kitscenes](https://github.com/KIT-MRT/kitscenes)  
Paper | _The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset_ â [arXiv:2606.02956](https://arxiv.org/abs/2606.02956)  
Project page | [kitscenes.com/multimodal](https://kitscenes.com/multimodal/)  
This FiftyOne build | `harpreetsahota/kitscenes-multimodal` (Hugging Face)  
  
The `kitscenes` Python package on GitHub (the devkit) is the official loader for the sensor, calibration, and map data; this FiftyOne build uses it to decode and project the geometry and labels.

## Dataset structure#

### Group slices#

The dataset is grouped on the `group` field. Each frame contains the following slices (the slice name doubles as the sensor name in the `sensor` field). The default slice shown in the App is `camera_ring_front`.

Slice | Media | Role  
---|---|---  
`camera_ring_front` | image | Forward ring camera (default view)  
`camera_ring_front_left` | image | Ring camera, front-left  
`camera_ring_front_right` | image | Ring camera, front-right  
`camera_ring_rear` | image | Rear ring camera  
`camera_ring_rear_left` | image | Ring camera, rear-left  
`camera_ring_rear_right` | image | Ring camera, rear-right  
`camera_base_front_center` | image | High-resolution long-range front camera  
`camera_base_front_left_rect` | image | Rectified front stereo, left  
`camera_base_front_right_rect` | image | Rectified front stereo, right  
`lidar` | 3d | Fused point cloud: 7 lidars + 3 radars, in the ego frame  
  
The six `camera_ring_*` slices form the 360Â° surround view; the three `camera_base_*` slices are the long-range and stereo cameras.

### Sample-level fields#

These fields are present on every sample (cameras and the 3D slice), giving each sample its scene context, timing, and ego pose.

Field | Type | Description  
---|---|---  
`scene_id` | string | UUID of the source scene  
`frame` | int | Frame index within the scene (0-based)  
`timestamp` | float | Reference timestamp (seconds)  
`sensor` | string | Sensor / slice name  
`ego_translation` | list[float] | Ego position `[x, y, z]` in the world frame  
`ego_quaternion` | list[float] | Ego orientation `[qx, qy, qz, qw]`  
`ego_yaw_deg` | float | Ego heading (degrees)  
`location` | `GeoLocation` | GNSS longitude/latitude  
`altitude` | float | GNSS altitude (meters)  
`gnss_fix_status` | int | GNSS fix-status code  
`ego_speed` | float | Ego speed from GNSS twist (m/s)  
  
The per-frame ego pose plus GNSS together give the full **car trajectory** â the sequence of ego positions and headings over each scene.

Camera slices additionally carry:

Field | Type | Description  
---|---|---  
`intrinsics` | dict | Pinhole intrinsics (focal length, principal point)  
`resolution` | dict | Image `width` / `height`  
  
### Label fields#

Labels are attached per camera slice; not every label exists on every camera. The table shows where each one is populated.

Field | FiftyOne type | Where | What it is  
---|---|---|---  
`lidar_depth` | `Heatmap` | all 9 cameras | Fused lidar depth projected into the image, encoded as an 8-bit depth heatmap (nearâfar)  
`hd_map` | `Polylines` | 6 ring cameras | Lanelet2 HD-map elements reprojected into the image (lane markings, borders, road markings, poles, traffic signs, traffic lights)  
`ego_trajectory` | `Keypoints` | `camera_ring_front` | The vehicleâs future path (ego waypoints) projected onto the road ahead, label `ego_path`  
`seamseg` | `Detections` | `camera_ring_front`, `camera_ring_rear` | Instance predictions (boxes + masks) in the Mapillary-Vistas taxonomy  
  
`hd_map` polylines carry a top-level `label` (the coarse category) and a `subtype` attribute holding the fine-grained Lanelet2 class (e.g. lane-marking style, or the specific German traffic-sign code such as `de206`).

### The 3D lidar slice#

The `lidar` slice is a single `.fo3d` scene per frame that fuses **seven lidars and three radars** into one ego-frame point cloud (lidar sweeps are motion-deskewed; radar detections are ego-motion compensated). Points are shaded by intensity in the App. The point clouds carry these per-point scalar fields:

  * **Lidar points:** `intensity` (reflectivity) and `isground` (per-point ground flag from ground segmentation).

  * **Radar points:** `intensity` (RCS) and `range_rate` (Doppler velocity).




### Saved views#

Three dynamic grouped views ship with the dataset for browsing:

View | What it shows  
---|---  
`ring_front_by_scene_frame` | The forward ring camera, grouped by `(scene_id, frame)` â 680 groups  
`ring_rear_by_scene_frame` | The rear ring camera, grouped by `(scene_id, frame)` â 680 groups  
`lidar_by_scene` | The fused lidar slice grouped by `scene_id` â 4 groups, one per scene  
  
## Label taxonomies#

**HD map (` hd_map`) categories:** `lane_marking`, `road_marking`, `road_border`, `pole`, `traffic_sign`, `traffic_light`. Each polylineâs `subtype` holds the detailed Lanelet2 class â lane-marking styles (e.g. `dashed`, `solid`, `dashed_solid`) and the fine-grained German traffic-sign codes (`deâ¦`).

**Instance predictions (` seamseg`) classes:** Mapillary-Vistas âthingâ classes, including `Car`, `Truck`, `Bus`, `Bicycle`, `Motorcycle`, `Trailer`, `Other Vehicle`, `Person`, `Bicyclist`, `Motorcyclist`, `Other Rider`, `Traffic Light`, `Traffic Sign (Front)`, `Traffic Sign (Back)`, `Traffic Sign Frame`, `Pole`, `Utility Pole`, `Street Light`, `Bench`, `Billboard`, `Banner`, `Bike Rack`, `Trash Can`, `Mailbox`, `Fire Hydrant`, `Junction Box`, `Catch Basin`, `Manhole`, `Phone Booth`, `CCTV Camera`, `Bird`, `Wheeled Slow`, `Crosswalk - Plain`, `Lane Marking - Crosswalk`.

## Uses#

This FiftyOne build is suited to:

  * **Multimodal browsing and curation** â inspect all 9 cameras and the fused point cloud for any frame, side by side.

  * **HD-map perception** â the `hd_map` polylines provide reprojection-accurate Lanelet2 map labels aligned to image pixels.

  * **Long-range depth** â `lidar_depth` heatmaps provide dense, long-range depth ground truth (the source lidar reaches beyond 400 m).

  * **Trajectory / motion work** â per-frame ego pose plus the projected `ego_trajectory` future path.

  * **2D object analysis** â the `seamseg` instance detections on the front and rear ring cameras.




### Out-of-scope#

This is an early-release **preview** subset (4 validation scenes). It is meant for exploration and pipeline development, not final benchmark reporting. The build also does **not** include 3D bounding boxes, tracks, or instance segmentation for dynamic agents (the source dataset omits these in the current release). The `seamseg` detections are model predictions, not human annotations.

## Source data#

KITScenes Multimodal was recorded across Karlsruhe, Frankfurt, and Sindelfingen by the Institute of Measurement and Control Systems (MRT) at the Karlsruhe Institute of Technology (KIT). The scenes here are from the validation split (Frankfurt). Camera imagery is anonymized (faces and license plates). Geometry and label projections in this build are produced with the official `kitscenes` Python API. See Dataset sources above for the original dataset, devkit, paper, and project-page links.

## Citation#
    
    
    @misc{schwarzkopf2026kitscenes,
          title={The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset},
          author={Richard Schwarzkopf and Fabian Immel and Alexander Blumberg and Jonas Merkert and Nils Rack and Kaiwen Wang and Fabian Konstantinidis and Julian Truetsch and Carlos Fernandez and Annika BÃ¤tz and Kevin RÃ¶sch and Marlon Steiner and Willi Poh and Yinzhe Shen and Royden Wagner and Felix Hauser and Dominik Strutz and Jaime Villa and Gleb Stepanov and Holger Caesar and Ãmer Åahin TaÅ and Frank Bieder and Jan-Hendrik Pauls and Christoph Stiller},
          year={2026},
          eprint={2606.02956},
          archivePrefix={arXiv},
          primaryClass={cs.CV},
          url={https://arxiv.org/abs/2606.02956},
    }
    

## License#

Released under [CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/), matching the source datasetâs terms. Non-commercial use only; attribution required.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
