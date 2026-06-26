---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/motor_two_wheel_rider.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/motor_two_wheel_rider)

# Dataset Card for motor_two_wheel_rider#

![image/png](https://huggingface.co/datasets/Voxel51/motor_two_wheel_rider/resolve/main/motor_two_wheel_rider.gif)

MOTOR (MOtorized TwO-wheeler Rider) is the first large-scale, multi-view, multimodal dataset dedicated to understanding two-wheeler rider behavior in dense, unstructured traffic conditions typical of the Global South. The full dataset comprises **1,629 annotated sequences** (~25 hours) from **16 riders** collected across diverse traffic scenarios in India.

**This repository contains a subset of the MOTOR dataset** imported into FiftyOne format for easy exploration and analysis. Each clip in the FiftyOne dataset contains **4 synchronized camera views** (front-mounted, helmet-mounted, rear-mounted, and eye-tracker), organized as grouped samples for easy multi-view analysis. The dataset captures both **conventional riding behaviors** (going straight, turns, lane changes) and **unconventional behaviors** (weaving through traffic, obstruction avoidance, violations) with rich annotations including legality labels, traffic context, GPS trajectories, gyroscope data, vehicle speeds, and rider gaze patterns.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 324 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/motor_two_wheel_rider")
    

To visualize GPS routes in the FiftyOne App Map panel, you need a Mapbox API key:

  1. Sign up for a free Mapbox account at https://mapbox.com

  2. Get your API token from https://account.mapbox.com/access-tokens/

  3. Export the token before launching the App:



    
    
    export MAPBOX_TOKEN=your_mapbox_token_here
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Sources#

  * **Curated by:** Varun Paturkar et al., IIIT Hyderabad

  * **Paper:** [MOTOR: A Multimodal Dataset for Two-Wheeler Rider Behavior Understanding](https://arxiv.org/abs/2605.22550) (ICRA 2026)

  * **Repository:** https://github.com/varuniiith/MOTOR-Dataset

  * **Project Page:** https://varuniiith.github.io/MOTOR-Dataset/

  * **Hugging Face:** https://huggingface.co/datasets/varunpaturkar/MOTOR

  * **License:** Research use only (as specified by authors)




## Uses#

### Direct Use#

  * **Rider behavior recognition** : Train models to classify 12 riding maneuvers

  * **Legality prediction** : Predict whether maneuvers comply with traffic rules

  * **Attention modeling** : Analyze rider gaze patterns during different behaviors

  * **Multimodal fusion** : Combine video, gaze, and telemetry for improved predictions

  * **Safety research** : Study dangerous behaviors and near-collision events

  * **Traffic analysis** : Understand two-wheeler behavior in dense traffic conditions

  * **ADAS development** : Build advanced driver assistance systems for motorcycles




### Out-of-Scope Use#

  * **Real-time inference** : Clips are short (~1-20 seconds) and pre-segmented

  * **Autonomous driving** : Dataset focuses on rider behavior, not scene understanding

  * **Non-Indian traffic** : Traffic patterns are specific to dense, unstructured Indian roads

  * **Four-wheeler analysis** : Dataset is specific to two-wheelers (motorcycles, scooters)




## Dataset Structure#

### FiftyOne Organization#

The dataset is organized as a **grouped dataset** with 4 slices per clip. You can switch between camera views in the FiftyOne App using the group slice selector, or programmatically by setting `dataset.group_slice`:

  * `front` \- Front-mounted camera (default) - includes GPS routes and telemetry

  * `helmet` \- Helmet-mounted camera

  * `rear` \- Rear-mounted camera

  * `eye_tracker` \- Eye tracker with riderâs POV - includes gaze heatmaps




### Sample-Level Fields#

Each sample contains the following fields:

Field | Type | Description  
---|---|---  
`clip_id` | String | Unique clip identifier (e.g., â01_042â)  
`video_id` | Integer | Full ride video ID  
`camera` | String | Camera view: front, helmet, rear, eye_tracker  
`source_timestamp` | String | Original position in full ride (MM:SS-MM:SS)  
`duration_s` | Float | Clip duration in seconds  
`location` | GeoLocations | GPS route polylines (front slice only)  
`event` | TemporalDetections | Primary riding behavior  
`legality` | TemporalDetections | Legal/illegal/unspecified  
`head_pose` | TemporalDetections | Rider head direction  
`road_type` | TemporalDetections | Paved/unpaved  
`road_marking` | TemporalDetections | Marked/unmarked lanes  
`divider` | TemporalDetections | Yes/no lane divider  
`traffic_density` | TemporalDetections | Low/medium/high  
`n_lanes` | TemporalDetections | Number of lanes  
  
### Frame-Level Fields#

**On front slice** (telemetry):

  * `gps`: GPS position as `GeoLocation(point=[lon, lat])` â supports frame-level geo queries

  * `speed_2d_mps`: 2D speed in meters/second

  * `speed_3d_mps`: 3D speed in meters/second

  * `gyro_x`, `gyro_y`, `gyro_z`: Gyroscope readings (deg/s)

  * `gps_alt_m`: GPS altitude in meters

  * `telemetry_timestamp_s`: Telemetry timestamp in seconds




**On eye_tracker slice** (gaze):

  * `gaze`: Gaussian heatmap (224Ã224) showing attention region




**Note on GPS:** The sample-level `location` field holds the full route polyline (`GeoLocations`) and is what the Map panel renders and what `geo_near`/`geo_within` query against. The frame-level `gps` field (`GeoLocation`) stores the position at each individual frame and supports per-frame location queries.

## Dataset Creation#

### Curation Rationale#

Two-wheelers account for a disproportionately high share of road fatalities in the Global South, yet research on rider behavior lags far behind four-wheeler ADAS research.

The MOTOR dataset addresses this gap by providing the first large-scale, multi-view, multimodal resource for understanding two-wheeler behavior in dense, unstructured traffic conditions typical of countries like India and Indonesia.

### Source Data#

#### Data Collection#

  * **Platform** : Multi-camera setup with 3 GoPro Hero 10 cameras + eye-tracking glasses (Aria/Pupil)

  * **Duration** : 4 weeks of data collection

  * **Location** : Various roads in India (urban, highway, peak/off-peak hours)

  * **Riders** : 16 riders with varying experience (2-20 years)

  * **Vehicles** : Multiple two-wheeler types (motorcycles, scooters)

  * **Synchronization** : All camera streams and sensors time-synchronized




#### Data Processing#

  * **Video** : 1920Ã1080, 30 FPS, with stabilization

  * **Telemetry** : Extracted from GoPro recordings using GoPro telemetry extractor

  * **Gaze** : Red gaze marker overlay burned into eye tracker video

  * **Clips** : Pre-extracted to match event boundaries (typically 1-20 seconds)

  * **Annotations** : Professional annotators trained on Indian Motor Vehicle Act (2017)




### Annotations#

#### Annotation Process#

Two professional annotators labeled all sequences under expert supervision:

  1. First 50 sequences annotated independently by both annotators

  2. Expert reviewed work, resolved discrepancies, provided feedback

  3. Remaining sequences annotated individually with periodic random checks

  4. Annotations include:

     * Riding maneuver classification (12 classes)

     * Legality determination based on Indian Motor Vehicle Act

     * Head pose direction (on road, left, right, either side)

     * Traffic context (road type, lanes, markings, density)




#### Who are the Annotators?#

Professional annotators trained on maneuver definitions and traffic violation rules from the Indian Motor Vehicle Act (2017), working under expert supervision.

## Citation#

**BibTeX:**
    
    
    @inproceedings{paturkar2026motor,
      title={MOTOR: A Multimodal Dataset for Two-Wheeler Rider Behavior Understanding},
      author={Paturkar, Varun and others},
      booktitle={2026 IEEE International Conference on Robotics and Automation (ICRA)},
      year={2026}
    }
    

**APA:**

Paturkar, V., et al. (2026). MOTOR: A Multimodal Dataset for Two-Wheeler Rider Behavior Understanding. _2026 IEEE International Conference on Robotics and Automation (ICRA)_.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
