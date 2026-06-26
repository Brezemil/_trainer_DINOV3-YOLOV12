---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/harmony4d.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Harmony4D)

# Dataset Card for Harmony4D#

![image/png](https://huggingface.co/datasets/Voxel51/Harmony4D/resolve/main/harmony4d.gif)

Harmony4D is a large-scale multi-view video dataset of in-the-wild close humanâhuman contact interactions â wrestling, dancing, MMA, karate, fencing, and hugging â with dense ground-truth annotations for detection, tracking, 2D/3D pose estimation, and SMPL body mesh recovery. It is one of the first datasets to address close contact scenarios where standard single-person pipelines fail due to occlusion and physical interpenetration.

This card describes the **FiftyOne-formatted version** of the dataset: the parsing decisions, the dataset structure in FiftyOne, and the 3D scene design choices made during preprocessing.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with **39 groups** (sequences), **848 video slices** , and **39 3D scene slices**.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/Harmony4D", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="Harmony4D"  # Assign a name to the dataset for identification
    )
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

**Harmony4D** (_Harmony4D: A Video Dataset for In-The-Wild Close Human Interactions_ , Khirodkar et al., arXiv 2410.20294, 2024) is a portable multi-view capture system built around 20 synchronized GoPro cameras (4K @ 60 FPS, annotated at 20 FPS) and â in ego/exo sequences â a pair of Meta Project Aria glasses worn by each subject. All 208 sequences capture exactly **2 subjects** performing physically close activities across 5 real-world environments. Annotations are produced by a novel markerless pipeline that handles contact-induced occlusion using instance segmentation, multi-view 2D pose estimation, RANSAC triangulation, and sequence-level SMPL mesh fitting with an interpenetration loss.

  * **Created by:** Rawal Khirodkar*, Jyun-Ting Song*, Jinkun Cao, Zhengyi Luo, Kris Kitani (Carnegie Mellon University; * equal contribution)

  * **Language(s):** N/A (video dataset)

  * **License:** Not specified by authors

  * **Project page / data:** https://jyuntins.github.io/harmony4d/




### Dataset Sources#

  * **Paper:** https://arxiv.org/abs/2410.20294

  * **Project page:** https://jyuntins.github.io/harmony4d/




* * *

## Dataset Structure#

### FiftyOne Dataset Type: Grouped Dataset#

The FiftyOne dataset is a **grouped dataset** (`fo.Dataset` with a `group` field). Each **group** corresponds to one video sequence (a single activity clip). Within a group, each **slice** is the H.264 MP4 video for one camera view of that sequence. This models the multi-view nature of the capture directly: all camera views of a scene are co-located under the same group, making it easy to browse synchronized views side-by-side in the FiftyOne App.
    
    
    Group (1 per sequence, e.g. "010_ballroom2")
     cam01   â Video sample  (exo GoPro, 3840Ã2160)
     cam02   â Video sample  (exo GoPro, 3840Ã2160)
       ...
     cam20   â Video sample  (exo GoPro, 3840Ã2160)
     aria01_rgb    â Video sample  (ego Aria RGB,   1408Ã1408)
     aria01_left   â Video sample  (ego Aria SLAM,   480Ã640)
     aria01_right  â Video sample  (ego Aria SLAM,   480Ã640)
     aria02_rgb    â Video sample  (ego Aria RGB,   1408Ã1408)
     aria02_left   â Video sample  (ego Aria SLAM,   480Ã640)
     aria02_right  â Video sample  (ego Aria SLAM,   480Ã640)
     scene_3d â 3D scene sample (.fo3d â sequence trajectory)
    

The default group slice is `cam01`. Sequences without ego cameras (the `exo_only` mode, detected by the presence of `colmap/workplace/scale.npy`) only have `cam01`â`cam20` slices and no `scene_3d` (if no SMPL data is available).

### Sample-Level Fields#

Every video sample carries:

Field | Type | Description  
---|---|---  
`filepath` | `StringField` | Absolute path to the H.264 MP4 video  
`group` | `EmbeddedDocumentField(Group)` | Group membership and slice name  
`split` | `StringField` | `"test"` or `"train"`  
`activity` | `StringField` | Activity label with trailing digits stripped (e.g. `"ballroom"`, `"mma"`, `"grappling"`, `"sword"`, `"hugging"`)  
`sequence_name` | `StringField` | Sequence directory name (e.g. `"010_ballroom2"`)  
`camera_name` | `StringField` | Camera identifier (e.g. `"cam01"`, `"aria01"`)  
`camera_type` | `StringField` | `"exo"`, `"ego"`, or `"3d"`  
`stream` | `StringField` | `"main"` (exo), `"rgb"`, `"left"`, or `"right"` (ego)  
`camera_intrinsics` | `DictField` | COLMAP intrinsics: `{fx, fy, cx, cy, k1âk4, width, height}`  
`camera_extrinsics` | `DictField` | COLMAP extrinsics: `{R: [[3Ã3]], t: [3,]}` (world-to-camera)  
  
### Frame-Level Labels (Video Samples)#

Annotations are stored as **frame-level labels** since the media type is video. Only annotated frames are populated (the subset of frames for which `processed_data/poses3d/*.npy` files exist, at 20 FPS):

Frame field | FiftyOne type | Description  
---|---|---  
`detections` | `fo.Detections` | Bounding boxes per subject, normalized `[x, y, w, h]` in `[0, 1]`  
`keypoints` | `fo.Keypoints` | 2D SMPL joint projections (45 joints per subject), normalized `[0, 1]`. Out-of-view joints are masked to `[None, None]` rather than clamped, matching the original visualization code.  
`poses3d` | `ListField` | List of dicts `{subject, keypoints: [[x,y,z,conf]Ã17], keypoint_names}` â 17 COCO keypoints in world metric coordinates. Stored as a plain list rather than `fo.Keypoint` because FiftyOneâs keypoint field expects normalized 2D coordinates.  
`smpl` | `ListField` | List of dicts per subject: `{subject, global_orient, transl, body_pose, betas, joints}` â all raw SMPL parameters. Vertex arrays (6890Ã3) are excluded here; they are instead exported to PLY files for 3D visualization.  
`smpl_scene` | `StringField` | Absolute path to the per-frame `.fo3d` scene file containing the subject SMPL point clouds for that timestep.  
  
### 3D Scene Slice (`scene_3d`)#

Each group has a `scene_3d` slice that points to a `sequence.fo3d` file â a FiftyOne 3D scene representing the **full sequence as a motion trajectory**. This is the primary 3D visualization entry point.

* * *

## Preprocessing Pipeline#

Two scripts are used: `preprocess_harmony4d.py` (heavy I/O, idempotent) and `parse_harmony4d.py` (FiftyOne dataset construction). Run preprocessing first.

### Step 1 â Video Encoding (`preprocess_harmony4d.py`)#

JPEG frame sequences (`%05d.jpg`) are encoded to H.264 MP4 using `ffmpeg` with CRF 18 at 20 FPS. Encoding is parallelized across all cameras and sequences using a `ThreadPoolExecutor`. Both exo GoPro sequences and ego Aria sequences (all three streams) are encoded.

### Step 2 â SMPL Point Cloud Export (`preprocess_harmony4d.py`)#

For each annotated frame, the SMPL `vertices` array (6890Ã3 float32) for each subject is exported to a binary little-endian PLY file. Per-frame `.fo3d` scene files reference these PLY files and are used for the `smpl_scene` frame attribute.

### Step 3 â Sequence Trajectory Scene (`preprocess_harmony4d.py`)#

A single `sequence.fo3d` is built per sequence for the `scene_3d` group slice, representing the full motion trajectory. Up to 20 evenly-spaced frames are sampled from the sequence. Each subjectâs vertices across all sampled frames are concatenated into one **XYZRGB PLY file** (`traj_meshes/{seq}/{subj}_trajectory.ply`). Points are colored by a **temporal gradient** â early frames receive the light end of the subjectâs color ramp, late frames the dark end â so temporal progression is readable as a color shift even when body positions overlap. The `scene.write()` call uses `resolve_relative_paths=True` so all PLY paths in the `.fo3d` JSON are absolute.

* * *

## PLY File Design Decisions#

### Why PLY instead of GLTF/OBJ/STL?#

FiftyOne supports GLTF, OBJ, PLY, STL, and FBX. PLY was chosen because:

  1. **No face topology required.** The SMPL model needs its `faces` array (from a separately-distributed model file) to produce a mesh. Rather than requiring users to supply the SMPL model weights, we export vertices only as a **point cloud PLY** , removing the external dependency entirely.

  2. **Simplicity and compactness.** Binary little-endian PLY with only XYZ or XYZRGB properties is the most compact format for raw vertex data.




### Per-Frame PLY vs. Sequence Trajectory PLY#

Two PLY layouts coexist:

Layout | Location | Content | Used by  
---|---|---|---  
Per-frame, per-subject | `smpl_meshes/{seq}/{ts:05d}_{subj}.ply` | XYZ only, one body per file | `smpl_scene` frame attribute  
Sequence trajectory | `traj_meshes/{seq}/{subj}_trajectory.ply` | XYZRGB, all sampled frames concatenated | `scene_3d` group slice  
  
The per-frame files are XYZ-only (no color) because `fo3d.PointCloudMaterial(shading_mode="custom")` applies a uniform color specified in the `.fo3d` descriptor â no per-point color is needed. The trajectory files use XYZRGB so that `shading_mode="rgb"` can render per-point gradient colors for temporal encoding.

### SMPL as Point Cloud vs. Mesh#

The original SMPL representation is a triangle mesh (6890 vertices, 13776 faces). We render it as a point cloud (`is_point_cloud=True` on `fo3d.PlyMesh`) because:

  * No face topology is embedded in the PLY (vertices only), so the mesh renderer would produce artifacts.

  * Point clouds are visually cleaner for dense vertex clouds at this scale â individual body shapes are clearly legible without face-shading artifacts.




### Exo Camera Markers (Per-Frame Scenes Only)#

The per-frame `.fo3d` scenes include a shared `camera_markers/{seq}/exo_cameras.ply` â a small PLY with one point per GoPro optical center (computed as `C = -R^T t` from COLMAP extrinsics). This gives spatial context for which cameras surround the subjects. The sequence trajectory scene omits this to keep the 3D view focused on the motion data.

* * *

## Dataset Statistics#

Metric | Value  
---|---  
Total groups (sequences) | 39 (test split)  
Total video slices | 848  
Total 3D scene slices | 39  
Activities | ballroom, grappling, hugging, mma, sword  
Subjects per sequence | 2 (always)  
Exo cameras per sequence | 20â22 (GoPro, 3840Ã2160)  
Ego cameras per sequence | 0 or 2 (Aria, 3 streams each: RGB 1408Ã1408, SLAM 480Ã640 Ã2)  
Annotated frames per sequence | 28â1200 (varies by sequence length)  
SMPL vertices per body | 6,890  
3D pose keypoints | 17 (COCO skeleton)  
2D pose joints | 45 (SMPL projected joints)  
  
* * *

## Dataset Creation#

### Curation Rationale#

Existing multi-person datasets (MuPoTS-3D, CMU Panoptic, EgoBody, etc.) avoid or under-represent close physical contact. Harmony4D was specifically designed to capture tight contact scenarios where two subjectsâ bodies touch, overlap visually, or occlude each other â the hardest regime for detection, pose estimation, and mesh recovery.

### Capture Setup#

A portable rig of 20 GoPro cameras in a ring formation at roughly floor level is set up at each location. Two subjects wearing Meta Aria glasses perform activities naturally. The rig is pre-scanned with COLMAP for camera calibration. Aria ego trajectories are registered into the shared world frame via Procrustes alignment. All cameras are hardware-synchronized; ego and exo streams are time-aligned in post-processing.

### Annotation Process#

A novel **contact-aware pipeline** handles the two regimes:

  * **Pre-contact:** Off-the-shelf multi-person 3D pose estimation (EgoHumans)

  * **In-contact:** Custom SegPose2D (ViTPose-H + mask conditioning) + RANSAC multi-view triangulation + Kalman filter forecasting for temporal coherence




SMPL meshes are fit sequence-level via differentiable optimization with 7 loss terms including an interpenetration loss using GPU signed-distance fields. All 3D pose sequences were manually inspected and rectified; all SMPL mesh sequences were manually verified after optimization.

* * *

## Bias, Risks, and Limitations#

  * The dataset contains **24 unique subjects** across 208 sequences, limiting demographic diversity.

  * All activities are physical and performance-oriented; results may not generalize to everyday casual contact.

  * Ego cameras (Aria) are present only in a subset of sequences; the `exo_only` vs. `ego_exo` split is determined at runtime by the presence of `colmap/workplace/scale.npy`.

  * SMPL body model fitting assumes a single neutral body shape (SMPL-Neutral); it may underfit extreme body proportions.

  * The SMPL vertex arrays in the FiftyOne dataset are represented as **point clouds** (no face topology) because the SMPL model file (`SMPL_NEUTRAL.pkl`) is separately distributed and not bundled here.




* * *

## Citation#

**BibTeX:**
    
    
    @article{khirodkar2024harmony4d,
      title   = {Harmony4D: A Video Dataset for In-The-Wild Close Human Interactions},
      author  = {Khirodkar, Rawal and Song, Jyun-Ting and Cao, Jinkun and Luo, Zhengyi and Kitani, Kris},
      journal = {arXiv preprint arXiv:2410.20294},
      year    = {2024}
    }
    

**APA:**

Khirodkar, R., Song, J.-T., Cao, J., Luo, Z., & Kitani, K. (2024). _Harmony4D: A Video Dataset for In-The-Wild Close Human Interactions_. arXiv:2410.20294.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
