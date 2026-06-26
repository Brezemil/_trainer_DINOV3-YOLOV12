---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/extended_video_activities_drop_4.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/extended_video_activities_drop_4)

# Dataset Card for meva_mevid#

![img/png](https://huggingface.co/datasets/Voxel51/extended_video_activities_drop_4/resolve/main/meva_dataset.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 201 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/extended_video_activities_drop_4")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Card â MEVA Drop-4 / MeVID (`meva_mevid`)#

MEVA drop-4-hadcv22 is a 201-clip subset of the [Multiview Extended Video with Activities (MEVA)](https://mevadata.org) Known Facility 1 dataset. It was released specifically to support the [HADCV22 Self-Reported Leaderboard Challenge](https://actev.nist.gov/SRL) and the broader ActEV activity-detection evaluation series run by NIST. The [MeVID](https://arxiv.org/abs/2211.04843) (Multi-view Extended Video ID) person re-identification benchmark builds its test/query annotations on top of this same footage.

## Dataset Details#

### Collection#

The footage was recorded at the Muscatatuck Urban Training Center (MUTC) with over 100 actors performing scripted scenarios. It was collected by Kitware Inc. under the IARPA Deep Intermodal Video Analytics (DIVA) program.

Property | Value  
---|---  
Clips | 201  
Total duration | ~16.75 hours  
Clip length | ~5 minutes each  
Resolution | 1920 Ã 1080  
Frame rate | 30 fps  
Codec | H.264 (remuxed to MP4 for FiftyOne)  
Cameras | 19 fixed ground cameras  
Recording dates | 7 days (MarchâMay 2018)  
Scenes | hospital, school, bus  
  
### Annotations (MeVID)#

Person re-identification tracklets from the [MeVID benchmark](https://arxiv.org/abs/2211.04843). Each tracklet records that a specific person (identified by a cross-camera integer ID) was visible in a specific clip for a given number of consecutive frames.

Split | Clips with tracklets | Tracklets | Unique persons  
---|---|---|---  
train | 77 | 657 | â  
test | 64 | 499 | â  
unlabeled | 60 | 0 | â  
**total** | **141** | **1 156** | **155**  
  
317 of the 499 test tracklets are designated **query** tracklets for the re-identification evaluation (matching a query sequence against a gallery of test sequences across cameras and time).

> **Coverage** : drop-4 accounts for roughly 14% of the full MeVID annotation. The remaining 86% of MeVID tracklets reference cameras from other MEVA drops not included in this download and are silently ignored by the parser.

The MeVID annotation provides **tracklet-level metadata only** â it does not include per-frame bounding boxes, absolute frame offsets within a clip, or activity labels. The MEVA dataset does publish separate DIVA-format activity annotations with bounding boxes (available via the [MEVA data repo](https://gitlab.kitware.com/meva/meva-data-repo)), but those are a separate download not included here.

* * *

## FiftyOne Dataset Structure#

Each of the 201 samples corresponds to one 5-minute MP4 clip.

### Sample-level fields#

Field | Type | Description  
---|---|---  
`filepath` | str | Absolute path to the `.mp4` file  
`recording_date` | str | Recording date, e.g. `"2018-03-12"`  
`start_time` | str | Clip start time, e.g. `"12:20:04"`  
`end_time` | str | Clip end time, e.g. `"12:25:04"`  
`scene` | str | Camera location: `"school"`, `"hospital"`, or `"bus"`  
`camera_id` | int | Numeric camera ID, e.g. `424`  
`camera_name` | str | Camera label used in MEVA filenames, e.g. `"G424"`  
`temporal_segment` | int | 0-based index of this clip within its cameraâs chronological sequence (matches the `T` value in MeVID filenames)  
`split` | str | `"train"`, `"test"`, or `"unlabeled"`  
`has_query` | bool | `True` if at least one query tracklet originates from this clip  
`person_ids` | list[int] | Sorted list of unique person IDs visible in this clip per MeVID  
`num_tracklets` | int | Total annotated tracklets in this clip  
`tracklets` | list[dict] | One dict per tracklet â see below  
  
### Tracklet dict schema#

Each entry in the `tracklets` list describes one contiguous person track:

Key | Type | Description  
---|---|---  
`person_id` | int | Cross-camera person identity (shared across all clips)  
`occurrence_id` | int | Which occurrence this is for this person (a person may appear multiple times across the dataset)  
`frame_count` | int | Number of frames in the track  
`split` | str | `"train"` or `"test"`  
`is_query` | bool | Whether this tracklet is a re-ID query  
  
### Filtering examples#
    
    
    import fiftyone as fo
    
    ds = fo.load_dataset("meva_mevid")
    
    # All test clips that contain a query tracklet
    queries = ds.match(
        (fo.ViewField("split") == "test") & fo.ViewField("has_query")
    )
    
    # Hospital clips only
    hospital = ds.match(fo.ViewField("scene") == "hospital")
    
    # Clips from a specific camera
    cam424 = ds.match(fo.ViewField("camera_name") == "G424")
    
    # Clips where person 212 appears
    person212 = ds.match(fo.ViewField("person_ids").contains(212))
    

* * *

## Source & License#

  * **Videos** : [mevadata.org](https://mevadata.org) â licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0)

  * **MeVID annotations** : distributed with the MeVID benchmark

  * **Produced by** : Kitware Inc. and IARPA




## Citation#
    
    
    @InProceedings{Corona_2021_WACV,
        author    = {Corona, Kellie and Osterdahl, Katie and Collins, Roderic and Hoogs, Anthony},
        title     = {MEVA: A Large-Scale Multiview, Multimodal Video Dataset for Activity Detection},
        booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
        month     = {January},
        year      = {2021},
        pages     = {1060-1068}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
