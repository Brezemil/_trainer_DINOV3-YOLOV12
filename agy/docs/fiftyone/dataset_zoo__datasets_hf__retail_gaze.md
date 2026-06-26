---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/retail_gaze.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/retail_gaze)

# Dataset Card for retail_gaze#

![img/png](https://huggingface.co/datasets/Voxel51/retail_gaze/resolve/main/retail_gaze.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 42 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/retail_gaze")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Retail Gaze is a real-world 2D gaze estimation dataset captured inside an operating supermarket. Unlike earlier retail gaze datasets collected in controlled laboratory environments, Retail Gaze was recorded under natural in-store conditions â real lighting, fully stocked shelves, and unrestricted head orientations â making it substantially harder and more ecologically valid than its predecessors.

The dataset was introduced by Senarath et al. at DASA 2022 and has since been extended. The version used here (`RetailGaze_V2_seg`) includes segmentation masks for product category areas on each shelf, enabling not only gaze point prediction but also gaze object prediction at the region level.

Each sample is a third-person view of a shopper gazing at a shelf, annotated with:

  * The 2D gaze target point in the scene

  * The bounding box around the personâs head

  * A binary segmentation mask identifying the product region being looked at

  * **Curated by:** Shashimal Senarath, Primesh Pathirana, Dulani Meedeniya (University of Moratuwa, Sri Lanka); Sampath Jayarathna (Old Dominion University, USA)

  * **Shared by:** Primesh Pathirana and Shashimal Senarath via Kaggle

  * **License:** Not explicitly stated in the paper




### Dataset Sources#

  * **Paper:** Senarath et al., âRetail Gaze: A Dataset for Gaze Estimation in Retail Environments,â DASA 2022. DOI: [10.1109/DASA54658.2022.9765224](https://doi.org/10.1109/DASA54658.2022.9765224)

  * **Repository:** https://www.kaggle.com/dulanim/retailgaze




* * *

## Uses#

### Direct Use#

  * **Gaze following:** Predicting where in a scene a person is looking, given their head location and the scene image. The annotated gaze point serves as the regression target.

  * **Gaze object prediction:** Predicting which product region on a shelf the shopper is attending to. The per-session segmentation masks define the candidate product area regions.

  * **Head detection:** Training head detectors robust to heavy occlusion, face masks, and extreme head orientations (back-of-head, profile, partial occlusion).

  * **Retail analytics:** Understanding customer attention patterns, shelf engagement, and product visibility in real store environments.




## Dataset Structure#

### Raw Data#

The raw dataset (`RetailGaze_V2_seg/RetailGaze_V2/`) is organized as:
    
    
    RetailGaze_V2/
     {subject_id}/          # 11 subjects (1â11)
         {session_id}/      # 2â6 sessions per subject (42 total); IDs are timestamps (e.g. "060433")
             {frame_num}.jpg  # frames extracted at every 4th frame; ~113 per session
             combined.png     # composite of all masks for this session
             masks/
                 mask_out{N}.png  # binary RGBA product area masks (8â13 per session)
    

Annotations are stored in four pickle files:

File | Records | Role  
---|---|---  
`RetailGaze_V3_2.pickle` | 3,922 | Full dataset  
`RetailGaze_V3_2_train.pickle` | 2,728 | Train split  
`RetailGaze_V3_2_valid.pickle` | 585 | Validation split  
`RetailGaze_V3_2_test.pickle` | 609 | Test split  
  
Each record is a Python dict:
    
    
    {
        "filename": "1/060433/0.jpg",   # relative path: {subject}/{session}/{frame}.jpg
        "width":    640,
        "height":   480,
        "gaze_cx":  205.68,             # gaze target X, pixel coordinates
        "gaze_cy":  134.91,             # gaze target Y, pixel coordinates
        "ann": {
            "hbox": [60, 34, 140, 129]  # head bounding box [x1, y1, x2, y2], pixel coords
        },
        "seg_mask": "1/060433/masks/mask_out10.png"  # relative path to binary mask; None for 77 frames
    }
    

The segmentation masks are **binary RGBA PNGs** (640Ã480) where pixel values are 0 (background) or 255 (foreground product region). Each annotation record references one mask, but multiple frames within a session can share the same mask (the shelf region being observed changes only when the shopper moves to a new area).

### Split Rationale#

Splits are assigned at the frame level following an approximate 70%/15%/15% ratio. The paper reports 2,745/589/588 (train/val/test); the pickles in this version contain 2,728/585/609.

* * *

## FiftyOne Dataset Structure#

The dataset is loaded into FiftyOne as a **flat video dataset** (`fo.Dataset`, media type: `video`) using `load_retail_gaze_dataset.py`.

### Video Encoding#

Each of the 42 shopping sessions is encoded into an `.mp4` at **10 fps** using `ffmpeg` with the H.264 codec. Frames are sorted numerically (0, 4, 8, â¦) before encoding, so FiftyOne frame index `i` (1-based) corresponds to the `(iâ1)`-th frame in the sorted disk sequence for that session.

Encoded videos are written to `retail_gaze_dataset/videos/{subject_id}_{session_id}.mp4`.

### Sample Schema#

Each `fo.Sample` represents one shopping session (one video):

Field | Type | Description  
---|---|---  
`filepath` | `str` | Absolute path to the `.mp4` video  
`subject_id` | `int` | Shopper identity (1â11)  
`session_id` | `str` | Original timestamp-style session ID (e.g. `"060433"`)  
`session_num` | `int` | 1-based session index within this subject  
  
### Frame Schema#

Annotations appear at the **frame level** on each video sample. Only the ~3,922 annotated frames carry labels; remaining frames in the video are unannotated.

Field | FiftyOne Type | Description  
---|---|---  
`head` | `fo.Detection` | Head bounding box; coordinates normalized to `[0, 1]` in `[x, y, w, h]` format  
`gaze_target` | `fo.Keypoints` | Ground-truth gaze point in the scene; normalized to `[0, 1]`  
`gaze_vector` | `fo.Polylines` | Two-point polyline from estimated eye origin â gaze target (see note below)  
`scene_mask` | `fo.Segmentation` | Product area mask referenced by `mask_path`; loaded from disk on demand  
`split` | `str` | `"train"`, `"val"`, or `"test"`  
  
### Gaze Vector: Heuristic Eye Origin#

The dataset annotates the **gaze target** point (`gaze_cx`, `gaze_cy`) and the **head bounding box** (`hbox`), but **does not provide eye coordinates**. To construct a visually meaningful gaze vector in FiftyOne, the origin of the gaze line (the approximate eye position) is estimated geometrically from the head bounding box:
    
    
    eye_x = (x1 + x2) / 2          # horizontal centre of head box
    eye_y = y1 + 0.35 * (y2 - y1)  # 35% from the top (standard face proportion heuristic)
    

This places the estimated eye at the horizontal centre of the head and approximately one third down from the top â a common approximation for frontal and profile views. It is **not derived from ground-truth eye landmark data** , which is absent from the dataset entirely. Running a face landmark detector (e.g. MediaPipe Face Mesh) on the head crops would yield more accurate origins, but the heuristic is sufficient for visualising gaze direction in the FiftyOne App.

Despite its simplicity, the gaze vector is still practically useful: it encodes both the direction and magnitude of the shopperâs attention vector in a single spatial label, making it easy to filter, visualise, and reason about in the App.

* * *

## Dataset Creation#

### Curation Rationale#

The Retail Gaze dataset was created to address a gap in the literature: while gaze estimation benchmarks existed for general scenes and laboratory-style retail setups, no dataset captured real, in-store shopper gaze under fully natural conditions. The authors argue that existing retail datasets (notably GOO) are limited by controlled environments, few camera angles, and single-product bounding box annotations rather than area-level product segmentations.

### Source Data#

#### Data Collection and Processing#

Videos were recorded inside a real supermarket using a purpose-built device consisting of a **Raspberry Pi 3** development board and a **5 MP camera module**. Capture was under natural daylight conditions inside the store; no external lighting was used.

Twelve different shelf sections were captured from a single camera angle each. During collection, participants walked along the shelf and were instructed to look at predetermined areas in a scripted pattern. Several frames were extracted per gaze area per participant. Data collection took place during the COVID-19 pandemic, which imposed two constraints:

  1. **Single-user capture:** Only one participant at a time, due to physical distancing requirements.

  2. **Face masks worn:** All participants wore surgical or cloth face masks, causing partial occlusion of the lower face in all images.




Frames were extracted from the recorded videos at every 4th frame, yielding approximately 113 frames per session.

#### Who are the source data producers?#

The dataset was produced by researchers at the **Department of Computer Science and Engineering, University of Moratuwa, Sri Lanka** , in collaboration with **Old Dominion University, USA**. The data was collected with 11 subjects (per the V2 extended version; the original DASA 2022 paper describes 2 participants).

### Annotations#

#### Annotation Process#

Three types of annotations were collected:

  1. **Gaze point:** The 2D pixel coordinate `(gaze_cx, gaze_cy)` in the scene image that the participant is looking at, derived from the predetermined scripted gaze patterns used during collection.

  2. **Head bounding box:** A tight axis-aligned box `[x1, y1, x2, y2]` around the participantâs head.

  3. **Product area segmentation masks:** Binary masks delineating regions of the shelf where products of the same category are grouped. These are session-level annotations (the same mask covers multiple frames captured from the same shelf position). Each session has 8â13 distinct masks, covering different product regions on that shelf.




## Bias, Risks, and Limitations#

  * **Limited subject diversity:** 11 subjects total (2 in the original paper), all appearing to be adult males from Sri Lanka. Models trained on this data may not generalize to broader shopper demographics.

  * **Single-user scenes:** The dataset captures one shopper at a time. Real retail environments involve multiple concurrent shoppers.

  * **Scripted gaze patterns:** Participants followed a predetermined pattern rather than shopping naturally, which may not reflect genuine browsing behavior.

  * **No explicit eye coordinates:** The gaze vector start point must be estimated from the head bounding box. No eye keypoint annotations exist in the dataset.

  * **Face masks:** All participants wore face masks, making the data unrepresentative of scenarios where the full face is visible. Standard face-landmark detectors may fail on these images.

  * **Fixed camera angles:** Each shelf is captured from exactly one camera angle; there is no multi-view or depth information.

  * **Mask coverage gaps:** 77 of 3,922 frames (2%) have no associated segmentation mask (`seg_mask: None`) and cannot be used for the gaze object prediction task.




## Citation#

**BibTeX:**
    
    
    @inproceedings{senarath2022retailgaze,
      title     = {Retail Gaze: A Dataset for Gaze Estimation in Retail Environments},
      author    = {Senarath, Shashimal and Pathirana, Primesh and Meedeniya, Dulani and Jayarathna, Sampath},
      booktitle = {2022 International Conference on Decision Aid Sciences and Applications (DASA)},
      pages     = {1040--1044},
      year      = {2022},
      doi       = {10.1109/DASA54658.2022.9765224}
    }
    

**APA:**

Senarath, S., Pathirana, P., Meedeniya, D., & Jayarathna, S. (2022). Retail Gaze: A Dataset for Gaze Estimation in Retail Environments. _2022 International Conference on Decision Aid Sciences and Applications (DASA)_ , 1040â1044. https://doi.org/10.1109/DASA54658.2022.9765224

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
