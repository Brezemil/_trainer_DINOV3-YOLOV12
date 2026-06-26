---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/retailaction.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/RetailAction)

# Dataset Card for RetailAction#

![img/png](https://huggingface.co/datasets/Voxel51/RetailAction/resolve/main/retailaction.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 21000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/RetailAction")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

* * *

## Dataset Details#

### Dataset Description#

RetailAction is designed for spatio-temporal localization of **customerâproduct interactions** (`take`, `put`, `touch`) across synchronized multi-view ceiling-mounted cameras in real stores.

  * **Curated by:** Standard AI â Davide Mazzini, Alberto Raimondi, Bruno Abbate, Daniel Fischetti, David M. Woollard

  * **License:** Standard AI proprietary license (see LICENSE)

  * **Paper:** _RetailAction: Dataset for Multi-View Spatio-Temporal Localization of Human-Object Interactions in Retail_ â ICCV 2025 Retail Vision Workshop




### Dataset Sources#

  * **Repository:** [standard-cognition/RetailAction on Hugging Face](https://huggingface.co/datasets/standard-cognition/RetailAction)

  * **Paper:** ICCV 2025 RetailAction paper




* * *

## FiftyOne Dataset Structure#

The dataset is a **grouped video dataset** (`media_type = "group"`). Each RetailAction sample folder maps to one **FiftyOne Group** with two **video slices** : `rank0` (default) and `rank1`. Each slice is a `fo.Sample` pointing to the respective `.mp4` file, with all annotations stored per slice using the camera-specific coordinates.

### Top-level dataset properties#
    
    
    dataset.media_type         # "group"
    dataset.group_field        # "group"
    dataset.group_slices       # ["rank0", "rank1"]
    dataset.group_media_types  # {"rank0": "video", "rank1": "video"}
    dataset.default_group_slice  # "rank0"
    dataset.skeletons          # {"pose_keypoints": <KeypointSkeleton>}
    

### Sample-level fields#

These fields are present on every `fo.Sample` in both `rank0` and `rank1` slices.

Field | Type | Description  
---|---|---  
`sample_id` | `str` | Zero-padded folder name, e.g. `"000000"`  
`split` | `str` | `"train"`, `"validation"`, or `"test"`  
`tags` | `list[str]` | Also contains the split name for tag-based filtering  
`segment_duration` | `float` | Original video segment duration in seconds (0.9â37s)  
`has_frame_timestamps` | `bool` | `False` for ~12% of samples where frame timestamps were not recorded  
`actions` | `fo.TemporalDetections` | One `fo.TemporalDetection` per annotated action  
`interaction_points` | `fo.Detections` | One `fo.Detection` per annotated interaction point  
  
#### `actions` â `fo.TemporalDetections`#

Each `fo.TemporalDetection` in `sample.actions.detections` represents one humanâobject interaction:

Attribute | Type | Description  
---|---|---  
`label` | `str` | Action class: `"take"`, `"put"`, or `"touch"`  
`support` | `[int, int]` | `[first_frame, last_frame]` (1-based, inclusive) derived from normalized `[start, end]` Ã total frames  
  
#### `interaction_points` â `fo.Detections`#

Each `fo.Detection` in `sample.interaction_points.detections` marks where the hand contacts the shelf item. Detections are parallel in order to `sample.actions.detections` (index `i` in both refers to the same action).

Attribute | Type | Description  
---|---|---  
`label` | `str` | Action class: `"take"`, `"put"`, or `"touch"`  
`bounding_box` | `[x, y, w, h]` | Small 4%Ã4% box centered on the interaction point (normalized, for App visibility)  
`interaction_x` | `float` | Raw normalized x-coordinate of the interaction point (for metric computation)  
`interaction_y` | `float` | Raw normalized y-coordinate of the interaction point (for metric computation)  
  
> **Note:** `interaction_x` / `interaction_y` preserve the exact annotated point coordinates for use in the paperâs `m_px_factor`-based spatial distance metric. The bounding box is a visualization convenience only.

### Frame-level fields#

These fields are stored in `sample.frames[i]` (1-indexed) and are populated for each of the up to 32 selected video frames. Frames with no detected pose have `pose_keypoints = None`.

Field | Type | Description  
---|---|---  
`pose_keypoints` | `fo.Keypoints` | Body pose for the subject of interest  
`face_position` | `fo.Keypoint` | Head center point of the subject of interest  
`sampling_score` | `float` | Motion-aware frame importance score (higher = more hand movement)  
  
#### `pose_keypoints` â `fo.Keypoints`#

Each frameâs `fo.Keypoints` contains one `fo.Keypoint` with label `"person"` representing the full-body pose of the interaction subject.

  * **Points:** Fixed-length list of 24 `[x, y]` coordinates in normalized frame space, one per joint in `JOINT_ORDER`. Missing joints (not detected by the pose model for that frame/view) are `[nan, nan]`.

  * **Confidence:** Parallel list of 24 raw heatmap activation scores from the PersonLab model. Missing joints have `nan`. Scores are **not probabilities** â they are uncalibrated logit-like values typically in `[0.06, 1.41]`; values >1.0 are possible.




The canonical 24-joint ordering (`JOINT_ORDER`):
    
    
     0: top_of_head      1: nose             2: neck
     3: left_ear         4: right_ear        5: left_eye         6: right_eye
     7: left_shoulder    8: right_shoulder
     9: left_elbow      10: right_elbow
    11: left_wrist      12: right_wrist
    13: left_hand       14: right_hand
    15: middle_of_waist
    16: left_hip        17: right_hip
    18: left_knee       19: right_knee
    20: left_ankle      21: right_ankle
    22: left_foot       23: right_foot
    

The datasetâs `skeletons["pose_keypoints"]` stores the `fo.KeypointSkeleton` with this ordering and 25 bone connectivity edges, enabling automatic skeleton rendering in the FiftyOne App.

**Important notes on pose data:**

  * Joint sets vary per frame and per camera view â one view may detect the left arm while the other detects the lower body.

  * Coordinates are quantized to a **1/64 grid** (PersonLabâs heatmap resolution), giving a step size of 0.015625.

  * ~9% of samples have at least one null pose entry due to the tracker losing the subject mid-segment.

  * Only the **subject of interest** (the person performing the labeled interaction) has pose data. Other people in frame have no annotations.




#### `face_position` â `fo.Keypoint`#

Single-point keypoint with label `"face"` marking the detected head center of the subject of interest.

  * **Points:** `[[x, y]]` â normalized continuous float coordinates from the face detector (not quantized, unlike pose).

  * Present for all frames where the subjectâs face was detected.




#### `sampling_score` â `float`#

Motion-aware importance score computed from the velocity and acceleration of the subjectâs hands. Higher scores indicate frames with significant hand movement. Used during dataset construction to select the most informative â¤32 frames from longer original segments.

  * For ~12% of samples (`has_frame_timestamps = False`), scores are matched positionally (score `i` â frame `i`) rather than by timestamp.

  * For the remainder, scores are matched to the nearest timestamp from the original dense score timeline.




### Querying examples#
    
    
    import fiftyone as fo
    
    ds = fo.load_dataset("RetailAction")
    
    # Filter to samples with at least one action
    ds_with_actions = ds.filter_labels("actions", fo.ViewField("support").length() > 0)
    
    # Get only test samples
    test_view = ds.match_tags("test")
    
    # Get multi-action samples (2+ actions in one segment)
    multi_action = ds.select_group_slices("rank0").filter_labels(
        "actions",
        fo.ViewField("detections").length() >= 2,
        only_matches=False
    ).match(fo.ViewField("actions.detections").length() >= 2)
    
    # Filter to frames where pose was detected
    frames_with_pose = ds.match_frames(fo.ViewField("pose_keypoints") != None)
    
    # Switch to the second camera view
    ds.group_slice = "rank1"
    

* * *

## Dataset Creation#

### Curation Rationale#

RetailAction was created to fill a gap in existing action recognition datasets: no large-scale dataset provided **spatio-temporal localization** of interactions in **real retail stores** from **multiple synchronized camera views**. Prior retail datasets (MERL Shopping, RetailVision) were small, lab-based, or single-view. General-purpose datasets (Kinetics, AVA) lacked retail context and provided bounding boxes around people rather than precise interaction points.

### Data Collection and Processing#

Data was collected over multiple years from 10 operational US convenience stores. An automated pipeline handled the full flow from raw continuous camera streams to annotated clips:

  1. **360-degree cameras** (2880Ã2880, 30 FPS) mounted at ~2.5m ceiling height provided continuous multi-TB/day streams.

  2. A **custom PersonLab model** fine-tuned on 360-degree top-view footage estimated 2D poses per person per frame.

  3. **Multi-view 3D pose reconstruction** triangulated per-camera tracklets into unified 3D tracks.

  4. A **kinematic GCN** (based on ST-GCN) operating on 3D poses and shelf geometry detected candidate interaction intervals, filtering out walking and browsing.

  5. A **camera scoring algorithm** selected the two best views per interaction based on occlusion, body visibility, and hand joint visibility.

  6. **Motion-aware frame subsampling** down-sampled each clip to â¤32 frames by prioritizing frames with high hand velocity/acceleration.

  7. **Anonymization** applied facial blurring and timestamp scrubbing (all timestamps are relative to `1970-01-01T00:00:00`).




### Annotations#

Annotations were produced through a two-step human annotation process:

**Step 1 â Binary classification + quality labels:** Annotators labeled each segment as interaction/non-interaction and flagged quality issues (bad camera selection, low resolution, too few frames, pose errors). A model-in-the-loop strategy was used: after an initial labeling pass, a model was trained on half the data and the 10% most-disagreed samples were re-reviewed. This cycle repeated three times.

**Step 2 â Spatio-temporal fine-grained labels:** Annotators marked the precise temporal boundaries of each interaction and spatially localized the exact pixel where the hand contacts the shelf item, for both camera views. In multi-person scenes, a red dot overlay identified the subject of interest to avoid ambiguity.

**Action categories:**

  * `take` â subject picks up an item from a shelf, fridge, or counter

  * `put` â subject places an item back onto a shelf, fridge, or counter

  * `touch` â hand contact without taking or placing




Labels apply only to interactions with retail shelves â not to shopping baskets, checkout interactions, or other in-store objects.

**Post-annotation curation** removed single-view segments, low-quality samples, outlier-duration segments, and excess no-interaction segments (capped at 10% of total).

### Personal and Sensitive Information#

All shoppers consented to recording via terms of service with the collecting organization. Videos have been anonymized:

  * Faces are blurred using automated facial detection

  * All timestamps are replaced with epoch-relative offsets (starting at `1970-01-01T00:00:00`)

  * Store names and identifiers are removed or blurred

  * Shopper identity labels are withheld â splits are partitioned by shopper but identifiers are not released




* * *

## Bias, Risks, and Limitations#

**Class imbalance:** 97.2% of labeled actions are `take`. The `put` and `touch` classes are heavily underrepresented, reflecting real customer behavior rather than a collection artifact.

**Store distribution skew:** Store 1 accounts for 36.2% of samples; stores 5â10 together account for <10%. Models trained on this dataset may generalize poorly to stores with unusual layouts or lighting.

**Top-down perspective:** All footage is from ceiling-mounted cameras. Models trained here are not expected to generalize to handheld, egocentric, or eye-level viewpoints.

**Partial pose observations:** Due to occlusion and the 360-degree fisheye distortion, ~20% of joint detections have low confidence (<0.5), and the detected joint set varies considerably per frame.

**Non-uniform frame rate:** Clips contain â¤32 frames but span segments of 0.9â37 seconds. The effective frame rate is non-uniform and lower than the original 30 FPS. Temporal models must account for variable time gaps between frames.

**Null frame timestamps:** ~12% of samples lack `frame_timestamps`, preventing precise temporal alignment of pose and face data to wall-clock time.

### Recommendations#

  * Apply a confidence threshold (e.g., >0.5) to `pose_keypoints.confidence` values before using joints for bone-length normalization or feature extraction.

  * Use `has_frame_timestamps` to identify samples where frame-level temporal alignment is unavailable.

  * For the spatial localization metric, use `interaction_x` / `interaction_y` attributes (not the bounding box center) and apply the per-video `m_px_factor` computed from bone lengths as described in the paper.

  * When evaluating across action classes, report per-class metrics given the severe `take`/`put`/`touch` imbalance.




* * *

## Citation#

**BibTeX:**
    
    
    @inproceedings{mazzini2025retailaction,
      title={RetailAction: Dataset for Multi-View Spatio-Temporal Localization of Human-Object Interactions in Retail},
      author={Mazzini, Davide and Raimondi, Alberto and Abbate, Bruno and Fischetti, Daniel and Woollard, David M.},
      booktitle={ICCV Retail Vision Workshop},
      year={2025}
    }
    

**APA:**

Mazzini, D., Raimondi, A., Abbate, B., Fischetti, D., & Woollard, D. M. (2025). RetailAction: Dataset for Multi-View Spatio-Temporal Localization of Human-Object Interactions in Retail. _ICCV Retail Vision Workshop_.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
