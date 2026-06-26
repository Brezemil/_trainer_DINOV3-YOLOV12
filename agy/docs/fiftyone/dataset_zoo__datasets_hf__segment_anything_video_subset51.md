---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/segment_anything_video_subset51.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/segment_anything_video_subset51)

# Dataset Card for Segment Anything Video (Subset 51)#

![img/png](https://huggingface.co/datasets/Voxel51/segment_anything_video_subset51/resolve/main/sav_dataset.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset containing 917 video samples from the SA-V (Segment Anything Video) dataset. The videos are at 6 fps (matching the annotation cadence) and include both manual and automatic masklet (object mask tracklets) annotations for video object segmentation tasks.

These are the videos from Subset 51 of the full dataset.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/segment_anything_video_subset51")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This FiftyOne dataset represents a subset of the SA-V (Segment Anything Video) dataset, designed for promptable visual segmentation (PVS) tasks. This subset contains 917 videos at 6 fps with masklet annotations - object masks tracked throughout the video - without semantic category labels. Annotations include both manually created masklets (average 3.8 per video) and automatically generated masklets from SAM 2 (average 8.9 per video).

  * **Curated by:** Meta FAIR

  * **Funded by:** Meta FAIR

  * **Shared by:** harpreetsahota (FiftyOne format)

  * **Language(s) (NLP):** Not applicable (video segmentation dataset)

  * **License:** Creative Commons Attribution 4.0 International Public License




### Dataset Sources#

  * **Repository:** https://ai.meta.com/datasets/segment-anything-video/

  * **Paper:** https://arxiv.org/abs/2408.00714




## Uses#

### Direct Use#

This dataset is suitable for:

  * **Video Object Segmentation (VOS)** \- tracking and segmenting objects throughout video sequences

  * **Interactive Video Object Segmentation (iVOS)** \- user-guided object segmentation in videos

  * **Promptable Visual Segmentation (PVS)** \- the primary task for which SA-V was designed

  * **Image Segmentation** \- by sampling individual frames from the videos

  * **Training and evaluating video segmentation models** \- particularly models like SAM 2




The FiftyOne format enables easy exploration, visualization, filtering, and analysis of the video annotations.

### Out-of-Scope Use#

  * **Semantic segmentation with predefined categories** \- SA-V masklets do not include semantic category labels

  * **Real-time video processing at original frame rates** \- videos have been downsampled to 6 fps

  * **Audio analysis** \- audio has been removed during preprocessing

  * **Tasks requiring high temporal resolution** \- annotation cadence is 6 fps, not suitable for fine-grained motion analysis




## Dataset Structure#

### FiftyOne Sample-Level Fields#

Each video sample in the FiftyOne dataset contains:

  * **`filepath`** \- Path to the 6 fps MP4 video file

  * **`video_id`** \- Unique identifier (e.g., âsav_051000â)

  * **`video_environment`** \- Environment type: âIndoorâ or âOutdoorâ

  * **`video_split`** \- Original split: âtrainâ, âvalâ, or âtestâ

  * **`video_duration`** \- Duration in seconds

  * **`num_manual_masklets`** \- Count of manually annotated objects

  * **`num_auto_masklets`** \- Count of automatically annotated objects (0 if none)




### FiftyOne Frame-Level Fields#

Annotations are provided only at the 6 fps cadence (every frame in the processed videos). Each annotated frame contains up to two detection fields:

  * **`manual`** \- `fo.Detections` containing manually annotated masklets

  * **`auto`** \- `fo.Detections` containing automatically generated masklets (when available)




### Detection Schema#

Each `fo.Detection` object represents one masklet instance and contains:

  * **`label`** \- Always âmaskletâ (no semantic categories in SA-V)

  * **`bounding_box`** \- Normalized `[x, y, w, h]` tight box around the mask

  * **`mask`** \- Boolean instance mask array cropped to the bounding box

  * **`masklet_id`** \- Object ID within the video (unique per object track)

  * **`masklet_size_bucket`** \- Size category: âsmallâ, âmediumâ, or âlargeâ

  * **`masklet_size_rel`** \- Relative mask area (fraction of frame pixels)

  * **`stability_score`** \- Per-frame quality score (auto annotations only; absent in manual)




### Video Format#

Videos are provided at 6 fps, matching the annotation cadence. Each frame in the 6 fps videos has corresponding annotations.

## Dataset Creation#

### Curation Rationale#

This FiftyOne dataset provides the SA-V data in a structured format for exploration and experimentation with video segmentation annotations.

### Source Data#

#### Data Collection and Processing#

**Original Data:**

  * Videos provided at 6 fps matching the annotation cadence

  * Annotations provided as COCO RLE format masks in JSON files




**FiftyOne Processing:**

  * COCO RLE masks decoded to boolean arrays and cropped to bounding boxes

  * Masks stored as `fo.Detection` objects with bounding boxes and instance masks

  * Both manual and auto annotations (when available) loaded as separate detection fields




#### Who are the source data producers?#

Crowdworkers contracted through a third-party vendor.

### Annotations#

#### Annotation process#

**Annotation Methods:**

  1. **Manual Masklets** \- SAM 2-assisted manual annotation (average 3.8 per video)

  2. **Auto Masklets** \- Automatically generated by SAM 2 (average 8.9 per video)




**Annotation Cadence:**

  * Annotations provided at 6 fps




#### Who are the annotators?#

Professional annotators contracted through a third-party vendor.

#### Personal and Sensitive Information#

  * Videos subjected to face blurring

  * Reports about videos can be submitted to segment-anything@meta.com




## Bias, Risks, and Limitations#

**Technical Limitations:**

  * No semantic category labels (only instance masks)

  * 6 fps temporal resolution

  * Annotations may contain errors (both manual and automatic)

  * Object selection is subjective




**FiftyOne-Specific:**

  * This is a subset (917 samples) of the full SA-V dataset

  * Mask storage format changed from COCO RLE to boolean arrays (increased storage)




### Recommendations#

  * Consider the lack of semantic labels when designing downstream tasks

  * Be mindful of storage requirements due to decoded mask format

  * Use FiftyOneâs filtering and visualization capabilities to explore annotations




## Citation#

**BibTeX:**
    
    
    @article{ravi2024sam2,
      title={SAM 2: Segment Anything in Images and Videos},
      author={Ravi, Nikhila and Gabeur, Valentin and Hu, Yuan-Ting and Hu, Ronghang and Ryali, Chaitanya and Ma, Tengyu and Khedr, Haitham and R{\"a}dle, Roman and Rolland, Chlo{\'e} and Gustafson, Laura and Mintun, Eric and Pan, Junting and Alwala, Kalyan Vasudev and Carion, Nicolas and Wu, Chao-Yuan and Girshick, Ross and Doll{\'a}r, Piotr and Feichtenhofer, Christoph},
      journal={arXiv preprint arXiv:2408.00714},
      year={2024}
    }
    

## More Information#

  * SA-V dataset: https://ai.meta.com/datasets/segment-anything-video/

  * FiftyOne: https://docs.voxel51.com/




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
