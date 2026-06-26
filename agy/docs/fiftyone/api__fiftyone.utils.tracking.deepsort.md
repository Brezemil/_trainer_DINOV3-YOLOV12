---
source_url: https://docs.voxel51.com/api/fiftyone.utils.tracking.deepsort.html
---

# fiftyone.utils.tracking.deepsort#

[DeepSort](https://arxiv.org/abs/1703.07402) wrapper for FiftyOne.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`DeepSort`() |   
---|---  
  
class fiftyone.utils.tracking.deepsort.DeepSort#
    

Bases: `object`

**Methods:**

`track`(sample_collection,Â in_field[,Â ...]) | Performs object tracking using the DeepSort algorithm on the given video samples.  
---|---  
`track_sample`(sample,Â in_field[,Â out_field,Â ...]) | Performs object tracking using the DeepSort algorithm on the given video sample.  
  
static track(_sample_collection_ , _in_field_ , _out_field ='frames.ds_tracks'_, _max_age =5_, _keep_confidence =False_, _skip_failures =True_, _progress =None_)#
    

Performs object tracking using the DeepSort algorithm on the given video samples.

DeepSort is an algorithm for tracking multiple objects in video streams based on deep learning techniques. It associates bounding boxes between frames and maintains tracks of objects over time.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of a frame field containing [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") to track. The `"frames."` prefix is optional

  * **out_field** (_"frames.ds_tracks"_) â the name of a frame field to store the output [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with tracking information. The `"frames."` prefix is optional

  * **max_age** (_5_) â the maximum number of missed misses before a track is deleted

  * **keep_confidence** (_False_) â whether to store the detection confidence of the tracked objects in the `out_field`

  * **skip_failures** (_True_) â whether to gracefully continue without raising an error if tracking fails for a video

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




static track_sample(_sample_ , _in_field_ , _out_field ='ds_tracks'_, _max_age =5_, _keep_confidence =False_)#
    

Performs object tracking using the DeepSort algorithm on the given video sample.

DeepSort is an algorithm for tracking multiple objects in video streams based on deep learning techniques. It associates bounding boxes between frames and maintains tracks of objects over time.

Parameters:
    

  * **sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

  * **in_field** â the name of the frame field containing [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") to track

  * **out_field** (_"ds_tracks"_) â the name of a frame field to store the output [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with tracking information. The `"frames."` prefix is optional

  * **max_age** (_5_) â the maximum number of missed misses before a track is deleted

  * **keep_confidence** (_False_) â whether to store the detection confidence of the tracked objects in the `out_field`




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
