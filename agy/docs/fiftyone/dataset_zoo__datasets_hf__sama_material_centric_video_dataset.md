---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/sama_material_centric_video_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/sama_material_centric_video_dataset)

# Dataset Card for sama_material_aware#

![image/png](https://huggingface.co/datasets/Voxel51/sama_material_centric_video_dataset/resolve/main/sama_material_aware.gif)

This is the training and evaluation dataset introduced alongside **SAMa: Material-Aware 3D Selection and Segmentation**. It is an object-centric synthetic video dataset with dense per-frame, per-material pixel-level segmentation annotations, designed to fine-tune video object-selection models for the task of material selection.

This [FiftyOne](https://github.com/voxel51/fiftyone) dataset contains 500 samples (450 train, 50 test).

## Installation#
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    dataset = load_from_hub("Voxel51/sama_material_centric_video_dataset")
    
    session = fo.launch_app(dataset)
    

* * *

## Dataset Details#

### Dataset Description#

The SAMa dataset is a synthetic, procedurally generated video dataset of 3D objects rendered across 30-frame sequences with multiple camera trajectories. Each video depicts one or more 3D objects, each composed of several distinct surface materials. The dataset provides dense per-pixel material segmentation masks for every frame, encoded in COCO RLE format.

The key motivation for the video format (rather than static images) is multiview consistency: by training on temporally coherent material annotations, a video model learns to produce consistent material selections across viewpoints â a prerequisite for lifting 2D material selection into 3D representations (NeRFs, 3D Gaussians, meshes).

  * **Curated by:** Michael Fischer (UCL / Adobe Research), Iliyan Georgiev, Thibault Groueix, Vladimir G. Kim, Valentin Deschaintre (Adobe Research), Tobias Ritschel (UCL)

  * **Language(s):** N/A (vision dataset)

  * **License:** [More Information Needed]




### Dataset Sources#

  * **Paper:** [SAMa: Material-Aware 3D Selection and Segmentation](https://arxiv.org/abs/2411.19322)

  * **Project page / Demo:** https://mfischer-ucl.github.io/sama/




* * *

## Uses#

### Direct Use#

  * Fine-tuning video segmentation models (e.g. SAM2) for per-material selection

  * Training and evaluating material segmentation models that require cross-frame consistency

  * Benchmarking material-aware 3D selection methods on synthetic object-centric scenes




### Out-of-Scope Use#

  * General semantic segmentation (labels are appearance-based material instances, not semantic categories like âwoodâ or âmetalâ)

  * Real-world scene understanding â all content is synthetic

  * Glass, mirror, or highly transparent materials are acknowledged limitations of the method trained on this data




* * *

## Dataset Structure#

### Splits#

Split | Videos | Frames  
---|---|---  
train | 450 | 13,500  
test | 50 | 1,500  
  
### FiftyOne Schema#

Each sample in the dataset corresponds to one video and has the following fields:

**Sample-level fields:**

Field | Type | Description  
---|---|---  
`filepath` | string | Path to the H.264 MP4 video (1024Ã1024, 30 frames, 10 FPS)  
`split` | string | `"train"` or `"test"`  
`obj_idx` | int | Object index â matches the integer `N` in `video{N}.mp4` / `annotations{N}.json`  
`render_mode` | string | Camera trajectory: `"flyover"`, `"turntable"`, `"flyovernoLookatZoomOut"`, etc.  
`n_materials` | int | Number of distinct material regions in this video  
  
**Frame-level fields** (accessed via `sample.frames[1]` through `sample.frames[30]`, 1-indexed):

Field | Type | Description  
---|---|---  
`segmentation` | `fo.Segmentation` | Per-pixel material index mask stored as a uint8 PNG on disk  
  
The segmentation mask is a uint8 grayscale PNG where:

  * Pixel value `0` = background

  * Pixel value `1` through `N` = material index (1-based), corresponding to `dataset.mask_targets["segmentation"]`




**Dataset-level:**

  * `dataset.mask_targets["segmentation"]` maps integer pixel values to generic label strings: `{1: "material_1", 2: "material_2", ...}` up to the maximum number of materials observed. Human-readable material names are not included in this release.

  * `dataset.info` contains source and paper metadata.




### Parsing Notes#

  * Original videos are encoded as **MPEG-4 Part 2** and must be re-encoded to **H.264** for FiftyOneâs App to stream them. The `reencode_h264.sh` script handles this.

  * Annotations in the raw release are COCO RLE JSON files (`annotations{N}.json`). The `build_fiftyone_dataset.py` script decodes them using `pycocotools` and saves per-frame uint8 PNG mask files under `masks/`.

  * FiftyOne uses **1-based frame indexing** : annotation frame index 0 maps to `sample.frames[1]`.

  * Video frames are rendered in **linear RGB** space. For visualization, apply sRGB gamma correction (`frame ** 0.4545`).




* * *

## Dataset Creation#

### Curation Rationale#

Prior material segmentation datasets (Materialistic, OpenSurfaces, Dense Material Segmentation) only contain static images, which cannot teach multiview consistency â a critical requirement for lifting 2D material selection into 3D. This dataset was purpose-built to address that gap by providing temporally consistent per-material annotations across rendered camera trajectories.

### Source Data#

#### Data Collection and Processing#

Videos were procedurally generated in **Blender 4.3** using the Principled BSDF shader:

  * **3D objects:** Randomly sampled from a subset of **9,082 textured Substance 3D objects**. Objects with only a single material were excluded (no supervision signal for selection).

  * **Materials:** Randomly sampled from a library of **29,472 Substance material maps** (including multiple variants of the same base material, e.g., different wood types). Each material is assigned to appear at least twice per scene to provide positive supervision and disambiguate material selection from object selection.

  * **Scene layout:** Each video contains at least two objects, displaced by up to half their bounding box extent to reduce spatial overlap.

  * **Lighting:** Randomly selected HDR environment maps from a set of **420 HDRIs** sourced from [PolyHaven](https://polyhaven.com/). Objects are alpha-composited onto the environment map background to reduce the domain gap between synthetic and real-world data.

  * **Camera trajectories:** Four motion patterns used at specific sampling rates:

    * Turntable (spherical, fixed-radius): 33%

    * Flyover: 33%

    * Zoom-in: 22%

    * Zoom-out: 12%




#### Who are the source data producers?#

The dataset was created by the SAMa paper authors at **Adobe Research** and **University College London**. 3D assets are from Adobeâs Substance 3D library; HDRIs are from PolyHaven (CC0 licensed).

### Annotations#

#### Annotation process#

Annotations are **automatically generated** as part of the Blender rendering pipeline. Dense per-pixel material indices are rendered directly from the scene graph using integer material IDs, with label `0` reserved for the background. No human annotators were involved. Annotations are stored as COCO RLE-encoded binary masks, one per material per frame.

#### Who are the annotators?#

Automated (procedural rendering in Blender 4.3).

#### Personal and Sensitive Information#

None. The dataset contains only synthetic 3D renders of objects and materials.

* * *

## Bias, Risks, and Limitations#

  * **Synthetic domain gap:** All content is synthetically rendered. Performance may degrade on real-world captures with complex lighting, subsurface scattering, or non-Principled BSDF materials.

  * **Transparent and mirror-like materials:** The paper explicitly identifies glass and mirrors as failure cases â it is unclear whether a user would prefer to select the transparent/mirror material or what is behind/reflected.

  * **Fixed material definition:** Materials are defined by shared texture and reflectance properties. The model cannot adapt to user-defined selection criteria (e.g., selecting only by roughness).

  * **Depth dependency:** The 3D lifting pipeline depends on accurate depth estimation. Errors in volumetric reconstruction can cause noise in the similarity point cloud.




### Recommendations#

Users should be aware that this dataset targets appearance-based material similarity, not semantic categories. Two visually similar materials of different types (e.g., two different metals with the same texture) will be treated as the same material; two visually distinct materials of the same category (e.g., two different woods) will be treated as different.

* * *

## Citation#

**BibTeX:**
    
    
    @article{fischer2024sama,
      title={SAMa: Material-Aware 3D Selection and Segmentation},
      author={Fischer, Michael and Georgiev, Iliyan and Groueix, Thibault and Kim, Vladimir G. and Ritschel, Tobias and Deschaintre, Valentin},
      journal={arXiv preprint arXiv:2411.19322},
      year={2024}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
