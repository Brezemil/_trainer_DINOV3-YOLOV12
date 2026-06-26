---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/egocart_videos.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/egocart_videos)

# Dataset Card for EgoCart#

![image/png](https://huggingface.co/datasets/Voxel51/egocart_videos/resolve/main/ego_cart.gif)

EgoCart is a large-scale benchmark dataset for egocentric, image-based indoor localization in a retail store. RGB images and depth maps were captured by cameras mounted on shopping carts moving through a real supermarket. Each frame is annotated with a 3-DOF camera pose (position + orientation) and a store-zone class label.

This card covers the **`egocart_videos`** FiftyOne dataset: 9 MP4 videos â one per recording sequence â with frame-level pose and zone annotations.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 9 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/egocart_videos")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Navigating the dataset#
    
    
    import fiftyone as fo
    
    dataset = fo.load_dataset("egocart_videos")
    
    # Split views
    train = dataset.match_tags("train")  # sequences 0, 1, 2, 4, 6, 8  (6 videos)
    test  = dataset.match_tags("test")   # sequences 3, 5, 7             (3 videos)
    
    # Access a specific sequence
    seq4 = dataset.match(fo.ViewField("sequence_id") == "4").first()
    
    # Frame-level access â FiftyOne frames are 1-indexed
    first_frame  = seq4.frames[1]
    middle_frame = seq4.frames[len(seq4.frames) // 2]
    
    print(first_frame.location_x, first_frame.location_y)
    print(first_frame.zone_id)
    print(first_frame.heading_deg)
    
    # Iterate frames in a video
    for frame_number, frame in seq4.frames.items():
        print(frame_number, frame.zone_id, frame.location_x, frame.location_y)
    
    # Convert frame-level fields to a flat DataFrame
    frame_df = dataset.to_frames().to_pandas()
    

### Filtering on frame-level fields#

FiftyOne lets you filter videos by properties of their frames using `match_frames`:
    
    
    # Videos that contain at least one frame in zone 15
    has_zone_15 = dataset.match_frames(fo.ViewField("zone_id") == 15)
    
    # Videos where the cart was in the right half of the store
    has_right_half = dataset.match_frames(fo.ViewField("location_x") > 0)
    
    # Videos where the cart was facing roughly East (heading â 0Â°)
    has_east = dataset.match_frames(
        (fo.ViewField("heading_deg") > -30) & (fo.ViewField("heading_deg") < 30)
    )
    
    # Build a frame-level view to analyse pose across all sequences
    frames_view = dataset.to_frames()
    print(frames_view.count("frames"))  # 19,531 total frames
    

## Dataset Details#

### Dataset Description#

EgoCart was collected to study the problem of localising shopping carts in a large retail store from egocentric images. It supports research into indoor localisation (image retrieval, pose regression), egocentric video understanding, and analysis of customer movement patterns.

RGB-D cameras (1280 Ã 720) mounted on shopping carts captured footage at **50 fps** during real shopping sessions in a single Italian retail store. Nine independent recording sequences were made; six form the training split and three the test split. The store floor plan spans roughly 40 m Ã 17 m.

  * **Original dataset creators:** E. Spera, A. Furnari, S. Battiato, G. M. Farinella â University of Catania, Italy

  * **FiftyOne curation:** Harpreet Sahota

  * **License:** Research use only (see original dataset page)




### Dataset Sources#

  * **Original dataset page:** <http://iplab.dmi.unict.it/EgocentricShoppingCartLocalization/>

  * **Paper:** Spera et al., _EgoCart: A Benchmark Dataset for Large-Scale Indoor Image-Based Localization in Retail Stores_ , IEEE TCSVT 2021. <https://ieeexplore.ieee.org/document/8835071>




## Uses#

### Direct Use#

  * **Indoor localisation / place recognition:** Use frame-level pose annotations as ground truth for image retrieval and nearest-neighbour localisation methods.

  * **Pose regression from video:** Train networks to predict `(location_x, location_y, heading_deg)` from RGB frames, exploiting temporal context across the video.

  * **Store zone classification:** Predict `zone_id` (1â16) from each video frame as a discrete localization proxy.

  * **Trajectory analysis:** Examine how shopping carts move through the store over time; the video format makes it easy to study motion continuity, revisitation patterns, and zone transitions.




### Out-of-Scope Use#

  * The dataset captures a **single retail store** at a **single point in time**. Models trained here will not generalise to different stores or layouts without re-collection.

  * The camera faces forward along aisles; there are **no identifiable people** in the footage, making it unsuitable for pedestrian detection or customer re-identification.

  * Videos encode only **camera heading** (yaw). Camera pitch and roll are not captured, so the dataset is unsuitable for full 6-DOF pose estimation.




## Dataset Structure#

### FiftyOne video dataset overview#

`egocart_videos` is a FiftyOne **video dataset** (`media_type = "video"`) containing 9 samples. In FiftyOneâs data model, each sample corresponds to one video file; annotations that change over time are stored as **frame-level fields** accessible via `sample.frames[frame_number]` (1-indexed).
    
    
    egocart_videos
    
     Sample 0   filepath = egocart_seq_0.mp4   tags = ["train"]   sequence_id = "0"
        Frame 1   location_x=-17.90  location_y=4.77  heading_deg=-2.49  zone_id=16
        Frame 2   location_x=-17.93  location_y=4.76  heading_deg=-4.57  zone_id=16
        ...  (1,838 frames total)
    
     Sample 1   filepath = egocart_seq_1.mp4   tags = ["train"]   sequence_id = "1"
        ...  (1,740 frames)
    
    ...
    
     Sample 8   filepath = egocart_seq_8.mp4   tags = ["train"]   sequence_id = "8"
         ...  (3,101 frames)
    

### Sample-level fields#

Field | Type | Description  
---|---|---  
`filepath` | `StringField` | Absolute path to the MP4 file  
`tags` | `ListField(StringField)` | `["train"]` or `["test"]`  
`sequence_id` | `StringField` | Recording run identifier (`"0"`â`"8"`)  
`metadata` | `VideoMetadata` | Auto-populated: duration, fps, resolution, frame count  
  
### Frame-level fields#

Each frame corresponds to one original RGB image from the dataset. Frames are **1-indexed** in FiftyOne.

Field | Type | Description  
---|---|---  
`frame_number` | `FrameNumberField` | 1-indexed position within the video  
`location_x` | `FloatField` | Cart X position in the store (metres, â â20 to +20)  
`location_y` | `FloatField` | Cart Y position in the store (metres, â â9 to +8)  
`orientation_u` | `FloatField` | Camera heading unit-vector, X component  
`orientation_v` | `FloatField` | Camera heading unit-vector, Y component  
`heading_deg` | `FloatField` | `atan2(v, u)` in degrees â see coordinate system below  
`zone_id` | `IntField` | Store location class (1â16)  
  
### Train / test split#

Split | Sequences | Frames | Duration at 15 fps  
---|---|---|---  
Train | 0, 1, 2, 4, 6, 8 | 13,360 | â 15 min total  
Test | 3, 5, 7 | 6,171 | â 7 min total  
  
Sequences were recorded independently on different occasions. The split is at the **sequence level** , ensuring no temporal overlap between train and test.

### Video encoding#

Videos are encoded with **H.264 / yuv420p** at **15 fps** (original capture rate: 50 fps, so playback is â 3Ã slower than real time). This makes the cartâs motion easy to inspect frame-by-frame in the FiftyOne App. Frame-level annotations are aligned to the 15 fps video â frame `n` in the video corresponds to row `n` in the sorted annotation file for that sequence.

### Store coordinate system#

The coordinate origin is a fixed reference point inside the store. Axes are in metres:

Axis | Range | Direction  
---|---|---  
X | â20.2 to +19.8 m | Left â Right  
Y | â9.5 to +8.0 m | Bottom â Top  
  
`(orientation_u, orientation_v)` is a 2D unit vector in the storeâs XY floor plane (`uÂ² + vÂ² â 1.0`). The derived field `heading_deg = atan2(v, u)` gives a compass-style angle: 0Â° = East (+X), 90Â° = North (+Y), Â±180Â° = West (âX), â90Â° = South (âY).

The store aisles run primarily NorthâSouth, so most frames show heading values near Â±90Â°. The cart reverses direction between adjacent aisle lanes (serpentine route), which is clearly visible as alternating heading clusters in each sequence.

### Store zone distribution#

Zones 1â9 are sequential single-aisle sections along the central spine from left to right. Zones 10â16 are larger structural zones (perimeter walkways, wide sections).

Zone | Description | Train frames | Test frames  
---|---|---|---  
1 | Left aisle zone 1 | 311 | 173  
2 | Left aisle zone 2 | 244 | 131  
3 | Left aisle zone 3 | 241 | 177  
4 | Left aisle zone 4 | 278 | 117  
5 | Left aisle zone 5 | 665 | 174  
6 | Center aisle zone 6 | 403 | 217  
7 | Center aisle zone 7 | 394 | 201  
8 | Center aisle zone 8 | 266 | 190  
9 | Right aisle zone 9 | 366 | 235  
10 | Right half aisles | 1,722 | 751  
11 | Back wall aisle (full width) | 1,610 | 658  
12 | Right wall | 1,355 | 409  
13 | Bottom right | 897 | 456  
14 | Bottom left | 1,138 | 788  
15 | Central bottom aisle (full width) | 2,668 | 1,130  
16 | Left wall | 802 | 364  
  
Zone distribution is imbalanced: zone 15 is the most frequent because the cart must traverse the full-width bottom aisle when moving between the two halves of the store. Zones 1â4 are the rarest.

## Dataset Creation#

### Curation Rationale#

Indoor localisation from images is a practically important but data-scarce problem. At the time of publication, existing datasets were too small, collected in corridor environments, or lacked ground-truth poses. EgoCart provides a large, real-world retail benchmark with accurate 3-DOF pose annotations to enable reproducible benchmarking of image retrieval and pose regression methods.

The video format presented here groups the original frame sequences into their natural temporal structure, making it straightforward to study motion context, temporal consistency of predictions, and zone transition behaviour.

### Source Data#

#### Data Collection and Processing#

RGB-D cameras were mounted on shopping carts and driven through a real retail store in Italy. Cameras captured at 50 fps â confirmed by the 20 ms (20-unit) increments in the numeric portion of each source filename. Ground-truth 3-DOF poses `(x, y, u, v)` were obtained through a separate localisation system. Zone labels (1â16) were assigned based on which manually defined store region contains each frameâs `(x, y)` position.

#### Who are the source data producers?#

The dataset was produced by researchers at the [Image Processing Laboratory (IPLab)](https://iplab.dmi.unict.it/), Department of Mathematics and Computer Science, University of Catania, Italy.

### Annotations#

#### Annotation process#

Camera poses `(x, y, u, v)` were obtained via an automated localisation pipeline. Zone labels correspond to manually defined rectangular floor regions; each frame receives the label of the zone containing its `(x, y)` position.

#### Who are the annotators?#

Researchers at the University of Catania (Spera, Furnari, Battiato, Farinella).

## Citation#

**BibTeX:**
    
    
    @article{spera2021egocart,
      author  = {Spera, E. and Furnari, A. and Battiato, S. and Farinella, G. M.},
      title   = {{EgoCart}: A Benchmark Dataset for Large-Scale Indoor Image-Based Localization in Retail Stores},
      journal = {IEEE Transactions on Circuits and Systems for Video Technology},
      volume  = {31},
      number  = {4},
      pages   = {1253--1267},
      year    = {2021},
      month   = apr,
      doi     = {10.1109/TCSVT.2019.2941040}
    }
    

**APA:**

Spera, E., Furnari, A., Battiato, S., & Farinella, G. M. (2021). EgoCart: A benchmark dataset for large-scale indoor image-based localization in retail stores. _IEEE Transactions on Circuits and Systems for Video Technology_ , _31_(4), 1253â1267. https://doi.org/10.1109/TCSVT.2019.2941040

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
