---
source_url: https://docs.voxel51.com/api/fiftyone.utils.iou.html
---

# fiftyone.utils.iou#

Intersection over union (IoU) utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`compute_ious`(preds,Â gts[,Â iscrowd,Â ...]) | Computes the pairwise IoUs between the predicted and ground truth objects.  
---|---  
`compute_segment_ious`(preds,Â gts[,Â sparse]) | Computes the pairwise IoUs between the predicted and ground truth temporal detections.  
`compute_max_ious`(sample_collection,Â label_field) | Populates an attribute on each label in the given spatial field(s) that records the max IoU between the object and another object in the same sample/frame.  
`find_duplicates`(sample_collection,Â label_field) | Returns IDs of duplicate labels in the given field of the collection, as defined as labels with an IoU greater than a chosen threshold with another label in the field.  
`compute_bbox_iou`(gt,Â pred[,Â gt_crowd]) | Computes the IoU between the given ground truth and predicted detections.  
  
fiftyone.utils.iou.compute_ious(_preds_ , _gts_ , _iscrowd =None_, _classwise =False_, _use_masks =False_, _use_boxes =False_, _tolerance =None_, _sparse =False_, _error_level =1_)#
    

Computes the pairwise IoUs between the predicted and ground truth objects.

For polylines, IoUs are computed as solid shapes when `filled=True` and "IoUs" are computed using `object keypoint similarity <https://cocodataset.org/#keypoints-eval>`_ when ``filled=False`.

For keypoints, âIoUsâ are computed via [object keypoint similarity](https://cocodataset.org/#keypoints-eval).

Parameters:
    

  * **preds** â a list of predicted [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") instances

  * **gts** â a list of ground truth [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") instances

  * **iscrowd** (_None_) â an optional name of a boolean attribute or boolean function to apply to each label that determines whether a ground truth object is a crowd. If provided, the area of the predicted object is used as the âunionâ area for IoU calculations involving crowd objects

  * **classwise** (_False_) â whether to consider objects with different `label` values as always non-overlapping (True) or to compute IoUs for all objects regardless of label (False)

  * **use_masks** (_False_) â whether to compute IoUs using the instances masks in the `mask` attribute of the provided objects, which must be [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") instances

  * **use_boxes** (_False_) â whether to compute IoUs using the bounding boxes of the provided [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") instances rather than using their actual geometries

  * **tolerance** (_None_) â a tolerance, in pixels, when generating approximate polylines for instance masks. Typical values are 1-3 pixels. By default, IoUs are computed directly on the dense pixel masks

  * **sparse** (_False_) â whether to return a sparse dict of non-zero IoUs rather than a full matrix

  * **error_level** (_1_) â 

the error level to use when manipulating instance masks or polylines. Valid values are:

    * 0: raise geometric errors that are encountered

    * 1: log warnings if geometric errors are encountered

    * 2: ignore geometric errors

If `error_level > 0`, any calculation that raises a geometric error will default to an IoU of 0



Returns:
    

a `num_preds x num_gts` array of IoUs when `sparse=False`, or a dict of the form `d[pred.id] = [(gt.id, iou), ...]` when `sparse=True`

fiftyone.utils.iou.compute_segment_ious(_preds_ , _gts_ , _sparse =False_)#
    

Computes the pairwise IoUs between the predicted and ground truth temporal detections.

Parameters:
    

  * **preds** â a list of predicted [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection") instances

  * **gts** â a list of ground truth [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection") instances

  * **sparse** (_False_) â whether to return a sparse dict of non-zero IoUs rather than a full matrix



Returns:
    

a `num_preds x num_gts` array of segment IoUs when `sparse=False`, or a dict of the form `d[pred.id] = [(gt.id, iou), ...]` when `sparse=True`

fiftyone.utils.iou.compute_max_ious(_sample_collection_ , _label_field_ , _other_field =None_, _iou_attr ='max_iou'_, _id_attr =None_, _progress =None_, _** kwargs_)#
    

Populates an attribute on each label in the given spatial field(s) that records the max IoU between the object and another object in the same sample/frame.

If `other_field` is provided, IoUs are computed between objects in `label_field` and `other_field`.

If no `other_field` is provided, IoUs are computed between objects in `label_field` alone, excluding the object itself.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **label_field** â a label field of type [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **other_field** (_None_) â another label field of type [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **iou_attr** (_"max_iou"_) â the label attribute in which to store the max IoU

  * **id_attr** (_None_) â an optional attribute in which to store the label ID of the maximum overlapping label

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for `compute_ious()`




fiftyone.utils.iou.find_duplicates(_sample_collection_ , _label_field_ , _iou_thresh =0.999_, _method ='simple'_, _progress =None_, _** kwargs_)#
    

Returns IDs of duplicate labels in the given field of the collection, as defined as labels with an IoU greater than a chosen threshold with another label in the field.

The following duplicate removal methods are supported:

  * `method="simple"`: mark the latter label in every pair of labels whose IoU exceeds the threshold. This may remove more labels than the greedy method

  * `method="greedy"`: apply a greedy method to mark the fewest number of labels as duplicate such that no non-duplicate labels have IoU greater than the specified threshold. This method is more computationally expensive than the simple method




Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **label_field** â a label field of type [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **iou_thresh** (_0.999_) â the IoU threshold to use to determine whether labels are duplicates

  * **method** (_"simple"_) â the duplicate removal method to use. The supported values are `("simple", "greedy")`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * ****kwargs** â optional keyword arguments for `compute_ious()`



Returns:
    

a list of IDs of duplicate labels

fiftyone.utils.iou.compute_bbox_iou(_gt_ , _pred_ , _gt_crowd =False_)#
    

Computes the IoU between the given ground truth and predicted detections.

Parameters:
    

  * **gt** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **pred** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **gt_crowd** (_False_) â whether the ground truth object is a crowd



Returns:
    

the IoU, in `[0, 1]`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
