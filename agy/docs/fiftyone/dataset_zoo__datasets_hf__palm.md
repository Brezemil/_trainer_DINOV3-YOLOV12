---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/palm.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/PALM)

# Dataset Card for PALM-XR20A (1000 Sample Subset)#

![image/png](https://huggingface.co/datasets/Voxel51/PALM/resolve/main/palm_dataset.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from huggingface_hub import snapshot_download
    
    
    # Download the dataset snapshot to the current working directory
    
    snapshot_download(
        repo_id="Voxel51/PALM", 
        local_dir=".", 
        repo_type="dataset"
        )
    
    
    
    # Load dataset from current directory using FiftyOne's native format
    dataset = fo.Dataset.from_dir(
        dataset_dir=".",  # Current directory contains the dataset files
        dataset_type=fo.types.FiftyOneDataset,  # Specify FiftyOne dataset format
        name="PALM"  # Assign a name to the dataset for identification
    )
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

PALM is a large-scale dataset of human hands designed to support learning generalizable, physically grounded models of hand shape and appearance. It contains approximately 90,000 high-resolution multi-view RGB images and 13,000 high-quality 3D hand scans from 263 subjects, each performing approximately 50 predefined right-hand gestures. Subjects span a broad range of skin tones (light, tan, medium, dark), ages (21â70 years), and heights (145â200 cm), with an even gender split (131 male, 132 female). All data was captured in a fixed lighting and camera environment using a 3dMD hand scanner with 7 synchronized and calibrated RGB cameras. Each scan is paired with synchronized multi-view images and a MANO registration (pose and shape parameters) obtained via multi-viewâconsistent alignment to the 3D scans.

This FiftyOne dataset wraps the high-resolution XR20A variant of PALM as a grouped dataset, providing direct access to all modalities â RGB images, depth maps, surface normals, binary hand masks, MANO overlays, 3D mesh scans, camera calibration, and MANO pose parameters â through a unified sample schema.

  * **Curated by:** Zicong Fan, Edoardo Remelli, David Dimond, Fadime Sener, Liuhao Ge, Bugra Tekin, Cem Keskin, Shreyas Hampali (Meta Reality Labs; ETH ZÃ¼rich; Max Planck Institute for Intelligent Systems)

  * **Language(s):** N/A (no natural language content)

  * **License:** Attribution-NonCommercial 4.0 International




### Dataset Sources#

  * **Paper:** Fan et al., âPALM: A Dataset and Baseline for Learning Multi-Subject Hand Priorâ, arXiv:2511.05403

  * **Repository:** https://github.com/facebookresearch/PALM




## Uses#

### Direct Use#

This dataset is intended for research on hand modeling, including:

  * Learning generalizable priors over human hand geometry and appearance

  * Hand pose and shape estimation from single or multi-view RGB images

  * Physically based inverse rendering and relighting of hand avatars

  * Single-image hand avatar personalization under unknown lighting

  * Training and evaluating models that require accurate 3D hand geometry, high-resolution imagery, and diverse subject populations




### Out-of-Scope Use#

  * The dataset captures only the right hand; it is not suitable for tasks requiring left-hand or two-hand data

  * All captures are of isolated hands with no objects; it is not suitable for hand-object interaction tasks

  * The fixed capture environment and lighting conditions may limit generalization to fully in-the-wild appearance modeling without additional adaptation




## Dataset Structure#

This FiftyOne dataset is a **grouped dataset** named `PALM-XR20A`. Each group corresponds to a unique `(subject, frame)` capture and contains up to **8 slices** : one per synchronized camera view (`MCU_01` through `MCU_07`) and one 3D mesh slice (`mesh`). The default displayed slice is `MCU_04`, the reference camera used for environment-map calibration.

**Approximate scale:**

  * 263 subjects Ã ~49 frames = ~12,900 groups

  * 8 slices per group (7 image + 1 mesh) = ~103,000 total samples




* * *

### Image Slices (`MCU_01` â `MCU_07`)#

Each image slice corresponds to one of the seven synchronized 2448 Ã 2048 RGB cameras. All seven slices in a group share the same MANO pose parameters, quality score, and frame identity; each carries its own label overlays and camera calibration.

Field | FiftyOne Type | Description  
---|---|---  
`filepath` | `StringField` | Absolute path to the 2K RGB JPEG (2448 Ã 2048)  
`group` | `EmbeddedDocumentField(Group)` | Group membership; slice name equals the camera ID (e.g., `"MCU_04"`)  
`depth` | `fo.Heatmap` | 16-bit depth map (PNG). Visualized over the range `[26000, 40000]` sensor units, which covers the hand region  
`mask` | `fo.Segmentation` | Binary hand segmentation mask (PNG). `0` = background, `255` = hand  
`normals` | `fo.Heatmap` | RGBA surface normal map (PNG). Channels encode Nx, Ny, Nz, and alpha  
`mano_overlay` | `fo.Heatmap` | Rendered projection of the fitted MANO mesh onto the camera plane; non-zero alpha pixels indicate where the fitted mesh aligns with the captured hand  
`camera_id` | `StringField` | Camera identifier, e.g., `"MCU_04"`  
`camera_K` | `ArrayField` | 3 Ã 3 camera intrinsic matrix  
`camera_dist` | `ArrayField` | 10-parameter radial/tangential distortion coefficients  
`camera_Rt` | `ArrayField` | 4 Ã 4 world-to-camera extrinsic matrix  
`subject_id` | `StringField` | Zero-padded four-digit subject identifier, e.g., `"0000"`  
`frame_id` | `IntField` | Frame number as an integer (e.g., frame file `"000001"` â `1`)  
`quality_score` | `FloatField` | MANO fitting error for this frame (lower = better fit)  
`mano_betas` | `ArrayField` | MANO shape coefficients, shape `(10,)`. Subject-level identity; constant across all frames of the same subject  
`mano_global_orient` | `ArrayField` | Global hand orientation in axis-angle representation, shape `(3,)`  
`mano_hand_pose` | `ArrayField` | Finger joint pose parameters for 15 joints in axis-angle representation, shape `(45,)`  
`mano_translation` | `ArrayField` | Hand root translation in metres, shape `(3,)`  
`metric_j3d` | `FloatField` | Joint 3D fitting error (lower = better)  
`metric_scan` | `FloatField` | Scan alignment error (lower = better)  
`metric_bmc` | `FloatField` | Bone-length consistency metric (lower = better)  
`metric_kp2d` | `FloatField` | 2D keypoint reprojection error (lower = better)  
  
* * *

### Mesh Slice (`mesh`)#

Each group contains one mesh slice pointing to a `.fo3d` scene file that wraps the per-frame 3dMD PLY hand scan. Frame-level metadata is duplicated on this slice so the 3D viewer can display it without joining against an image sample.

Field | FiftyOne Type | Description  
---|---|---  
`filepath` | `StringField` | Absolute path to the `.fo3d` scene file (wraps the 3dMD PLY mesh)  
`group` | `EmbeddedDocumentField(Group)` | Group membership; slice name is `"mesh"`  
`subject_id` | `StringField` | Zero-padded four-digit subject identifier  
`frame_id` | `IntField` | Frame number as an integer  
`quality_score` | `FloatField` | MANO fitting error for this frame (lower = better)  
`mano_betas` | `ArrayField` | MANO shape coefficients, shape `(10,)`  
`mano_global_orient` | `ArrayField` | Global hand orientation (axis-angle), shape `(3,)`  
`mano_hand_pose` | `ArrayField` | Finger joint pose (axis-angle), shape `(45,)`  
`mano_translation` | `ArrayField` | Hand root translation in metres, shape `(3,)`  
  
* * *

### Dataset-level metadata#
    
    
    dataset.default_mask_targets = {0: "background", 255: "hand"}
    
    dataset.info = {
        "source": "PALM Dataset XR20A",
        "cameras": ["MCU_01", "MCU_02", "MCU_03", "MCU_04", "MCU_05", "MCU_06", "MCU_07"],
        "reference_camera": "MCU_04",
        "coord_unit": "metres",
        "image_resolution": "2448x2048",
    }
    

All 3D coordinates (camera extrinsics, MANO translation) are in metres.

## Dataset Creation#

### Curation Rationale#

PALM was created to address the absence of a large-scale, high-quality dataset that simultaneously provides accurate 3D hand geometry from real-world scans, high-resolution calibrated multi-view RGB imagery, and a diverse subject population. Prior datasets were limited by small subject counts, lack of 3D scan data, synthetic imagery, or low image resolution â constraints that impede training generalizable models of hand shape and appearance.

### Source Data#

#### Data Collection and Processing#

Data was captured using a 3dMD hand scanner with a 7-viewpoint array of 21 synchronized and calibrated machine vision cameras (7 RGB, 14 monochrome) providing 360-degree coverage. RGB images were captured at 2448 Ã 2048 resolution. Random light projectors were integrated to enhance surface detail. 3D hand meshes were reconstructed using 3dMDâs software-driven triangulation based on Active Stereo Photogrammetry.

Each of the 263 participants performed approximately 50 predefined right-hand gestures, covering open-hand poses, pinches, fist closures, and fine-grained finger movements. Each gesture was captured as an independent scan. All subjects were captured in the same fixed lighting and camera environment.

3D keypoint annotations were generated using a semi-automatic pipeline: 2D keypoints were manually annotated on a subset of images to train a U-Netâbased detector (pre-trained on InterHand2.6M and fine-tuned on 10,000 manually annotated PALM images), then triangulated via RANSAC-based multi-view geometry to obtain 3D poses. The final 3D keypoints achieve a recall rate of 95% at a 10 mm threshold.

MANO registrations were obtained by fitting the MANO hand model to each scan using a combination of 2D/3D keypoint supervision, segmentation mask alignment via Soft Rasterizer, and closest-point distance minimization to the scan surface. Registration was performed in two stages: the first optimizes per-subject shape parameters and per-frame pose on simple hand poses; the second freezes shape and optimizes only pose. Mean MANO fitting error is 5.3 mm with respect to 3D keypoints.

#### Who are the source data producers?#

Participants are 263 human subjects recruited for the study (131 male, 132 female), aged 21â70 years, with a range of heights (145â200 cm) and skin tones (light, tan, medium, dark).

### Annotations#

#### Annotation process#

2D keypoints were manually annotated on a subset of images, then a trained detector was applied to all camera views and triangulated to 3D using RANSAC. MANO pose and shape parameters were obtained by fitting the MANO parametric model to the 3D scans using a differentiable multi-stage optimization. Binary segmentation masks were derived from the 3D scans via rendering.

#### Who are the annotators?#

Annotations were produced by the research team at Meta Reality Labs using a semi-automatic pipeline as described above.

#### Personal and Sensitive Information#

The dataset contains high-resolution images and 3D geometry of human hands. Hand appearance encodes skin tone, which is a demographic characteristic. No facial or full-body imagery is included. Subjects are identified by anonymous numeric identifiers only (e.g., `"0000"`).

## Bias, Risks, and Limitations#

  * **Right hand only:** All captures are of the right hand. Models trained on this data cannot be directly applied to left hands without mirroring.

  * **Controlled capture environment:** All data was captured in a fixed laboratory setting with fixed lighting. Models may not generalize without adaptation to images captured in varied or uncontrolled illumination.

  * **Demographic representation:** While the dataset covers a range of skin tones, ages, and hand sizes, it comprises 263 subjects, which may not fully represent the global distribution of hand appearance and geometry.

  * **Predefined gesture vocabulary:** Subjects performed a fixed set of approximately 50 gestures. Dynamic or free-form hand motion is not represented.




### Recommendations#

Users should be aware that the dataset covers only right-hand, controlled-environment captures of 263 subjects performing predefined gestures. Models trained on this data should be evaluated carefully before deployment in settings with left hands, dynamic motion, or unconstrained illumination.

## Citation#

**BibTeX:**
    
    
    @article{fan2025palm,
      title={PALM: A Dataset and Baseline for Learning Multi-Subject Hand Prior},
      author={Fan, Zicong and Remelli, Edoardo and Dimond, David and Sener, Fadime and Ge, Liuhao and Tekin, Bugra and Keskin, Cem and Hampali, Shreyas},
      journal={arXiv preprint arXiv:2511.05403},
      year={2025}
    }
    

**APA:**

Fan, Z., Remelli, E., Dimond, D., Sener, F., Ge, L., Tekin, B., Keskin, C., & Hampali, S. (2025). PALM: A Dataset and Baseline for Learning Multi-Subject Hand Prior. _arXiv preprint arXiv:2511.05403_.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
