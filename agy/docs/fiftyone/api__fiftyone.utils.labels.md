---
source_url: https://docs.voxel51.com/api/fiftyone.utils.labels.html
---

# fiftyone.utils.labels#

Label utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`objects_to_segmentations`(sample_collection,Â ...) | Converts the instance segmentations or polylines in the specified field of the collection into semantic segmentation masks.  
---|---  
`export_segmentations`(sample_collection,Â ...) | Exports the semantic segmentations, instance segmentations, or heatmaps stored as in-database arrays in the specified field to images on disk.  
`import_segmentations`(sample_collection,Â in_field) | Imports the semantic segmentations, instance segmentations, or heatmaps stored on disk in the specified field to in-database arrays.  
`transform_segmentations`(sample_collection,Â ...) | Transforms the segmentations in the given field according to the provided targets map.  
`segmentations_to_detections`(...[,Â ...]) | Converts the semantic segmentations masks in the specified field of the collection into [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with instance masks populated.  
`binarize_instances`(sample_collection,Â in_field) | Binarizes the instance segmentations in the specified field according to the provided threshold.  
`instances_to_polylines`(sample_collection,Â ...) | Converts the instance segmentations in the specified field of the collection into [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances.  
`segmentations_to_polylines`(...[,Â ...]) | Converts the semantic segmentations masks in the specified field of the collection into [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances.  
`classification_to_detections`(...[,Â progress]) | Converts the [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") field of the collection into a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field containing a single detection whose bounding box spans the entire image.  
`classifications_to_detections`(...[,Â progress]) | Converts the [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") field of the collection into a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field containing detections whose bounding boxes span the entire image with one detection for each classification.  
`index_to_instance`(sample_collection,Â label_field) | Populates [`fiftyone.core.labels.Instance`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Instance "fiftyone.core.labels.Instance") values in the ``instance``attribute of the specified label field based on the values in the specified index attribute.  
`perform_nms`(sample_collection,Â in_field[,Â ...]) | Performs non-maximum suppression (NMS) on the specified [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field.  
`detections_3d_to_cuboids_2d`(...[,Â progress]) | High-level orchestration of 3D â 2D label conversion.  
  
fiftyone.utils.labels.objects_to_segmentations(_sample_collection_ , _in_field_ , _out_field_ , _mask_size =None_, _mask_targets =None_, _thickness =1_, _output_dir =None_, _rel_dir =None_, _overwrite =False_, _save_mask_targets =False_, _progress =None_)#
    

Converts the instance segmentations or polylines in the specified field of the collection into semantic segmentation masks.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the objects field for which to render segmentation masks. Supported types are [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), and [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

  * **out_field** â the name of the [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") field to populate

  * **mask_size** (_None_) â the `(width, height)` at which to render the segmentation masks. If not provided, masks will be rendered to match the resolution of each input image

  * **mask_targets** (_None_) â a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to label strings defining which object classes to render and which pixel values to use for each class. If omitted, all objects are rendered with pixel value 255

  * **thickness** (_1_) â the thickness, in pixels, at which to render (non-filled) polylines

  * **output_dir** (_None_) â an optional output directory in which to write the segmentation images. If none is provided, the segmentations are stored in the database

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each segmentation image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **overwrite** (_False_) â whether to overwrite any existing files in `output_dir`

  * **save_mask_targets** (_False_) â whether to store the `mask_targets` on the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.export_segmentations(_sample_collection_ , _in_field_ , _output_dir_ , _rel_dir =None_, _update =True_, _overwrite =False_, _progress =None_)#
    

Exports the semantic segmentations, instance segmentations, or heatmaps stored as in-database arrays in the specified field to images on disk.

Any labels without in-memory arrays are skipped.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation"), [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), or [`fiftyone.core.labels.Heatmap`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap "fiftyone.core.labels.Heatmap") field

  * **output_dir** â the directory in which to write the images

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **update** (_True_) â whether to delete the arrays from the database

  * **overwrite** (_False_) â whether to overwrite any existing files in `output_dir`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.import_segmentations(_sample_collection_ , _in_field_ , _update =True_, _delete_images =False_, _progress =None_)#
    

Imports the semantic segmentations, instance segmentations, or heatmaps stored on disk in the specified field to in-database arrays.

Any labels without images on disk are skipped.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation"), [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), or [`fiftyone.core.labels.Heatmap`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Heatmap "fiftyone.core.labels.Heatmap") field

  * **update** (_True_) â whether to delete the image paths from the labels

  * **delete_images** (_False_) â whether to delete any imported images from disk

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.transform_segmentations(_sample_collection_ , _in_field_ , _targets_map_ , _output_dir =None_, _rel_dir =None_, _update =True_, _update_mask_targets =False_, _overwrite =False_, _progress =None_)#
    

Transforms the segmentations in the given field according to the provided targets map.

This method can be used to transform between grayscale and RGB masks, or it can be used to edit the pixel values or colors of masks without changing the number of channels.

Note that any pixel values not in `targets_map` will be zero in the transformed masks.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") field

  * **targets_map** â a dict mapping existing pixel values (2D masks) or RGB hex strings (3D masks) to new pixel values or RGB hex strings to use. You may convert between grayscale and RGB using this argument

  * **output_dir** (_None_) â an optional directory in which to write the transformed images

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **update** (_True_) â whether to update the mask paths on the instances

  * **update_mask_targets** (_False_) â whether to update the mask targets on the dataset to reflect the transformed targets

  * **overwrite** (_False_) â whether to overwrite any existing files in `output_dir`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.segmentations_to_detections(_sample_collection_ , _in_field_ , _out_field_ , _mask_targets =None_, _mask_types ='stuff'_, _output_dir =None_, _rel_dir =None_, _overwrite =False_, _progress =None_)#
    

Converts the semantic segmentations masks in the specified field of the collection into [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with instance masks populated.

Each `"stuff"` class will be converted to a single [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") whose instance mask spans all region(s) of the class.

Each `"thing"` class will result in one [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") instance per connected region of that class in the segmentation.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") field to convert

  * **out_field** â the name of the [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field to populate

  * **mask_targets** (_None_) â a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to label strings defining which object classes to label and which pixel values to use for each class. If omitted, all labels are assigned to the pixel values

  * **mask_types** (_"stuff"_) â 

whether the classes are `"stuff"` (amorphous regions of pixels) or `"thing"` (connected regions, each representing an instance of the thing). Can be any of the following:

    * `"stuff"` if all classes are stuff classes

    * `"thing"` if all classes are thing classes

    * a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to `"stuff"` or `"thing"` for each class

  * **output_dir** (_None_) â an optional output directory in which to write instance segmentation images. If none is provided, the instance segmentations are stored in the database

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each instance segmentation image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **overwrite** (_False_) â whether to overwrite any existing files in `output_dir`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.binarize_instances(_sample_collection_ , _in_field_ , _threshold =1_, _output_dir =None_, _rel_dir =None_, _overwrite =False_, _progress =None_)#
    

Binarizes the instance segmentations in the specified field according to the provided threshold.

Each instance mask is updated in-place with `mask >= threshold`.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") or [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field containing instance segmentations

  * **threshold** (_1_) â the threshold for âinstanceâ pixels

  * **output_dir** (_None_) â an optional output directory in which to write the instance segmentation images. If none is provided, the segmentations are overwritten in-place, either on disk or in the database

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier that is joined with `output_dir` to generate an output path for each instance segmentation image. This argument allows for populating nested subdirectories in `output_dir` that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **overwrite** (_False_) â whether to overwrite any existing files in `output_dir`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.instances_to_polylines(_sample_collection_ , _in_field_ , _out_field_ , _tolerance =2_, _filled =True_, _progress =None_)#
    

Converts the instance segmentations in the specified field of the collection into [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances.

For detections with masks, the returned polylines will trace the boundaries of the masks; otherwise, the polylines will trace the bounding boxes themselves.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field to convert

  * **out_field** â the name of the [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") field to populate

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polylines for each region. Typical values are 1-3 pixels

  * **filled** (_True_) â whether the polylines should be filled

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.segmentations_to_polylines(_sample_collection_ , _in_field_ , _out_field_ , _mask_targets =None_, _mask_types ='stuff'_, _tolerance =2_, _progress =None_)#
    

Converts the semantic segmentations masks in the specified field of the collection into [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances.

Each `"stuff"` class will be converted to a single [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") that may contain multiple disjoint shapes capturing the class.

Each `"thing"` class will result in one [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instance per connected region of that class.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation") field to convert

  * **out_field** â the name of the [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") field to populate

  * **mask_targets** (_None_) â a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to label strings defining which object classes to label and which pixel values to use for each class. If omitted, all labels are assigned to the pixel values

  * **mask_types** (_"stuff"_) â 

whether the classes are `"stuff"` (amorphous regions of pixels) or `"thing"` (connected regions, each representing an instance of the thing). Can be any of the following:

    * `"stuff"` if all classes are stuff classes

    * `"thing"` if all classes are thing classes

    * a dict mapping pixel values (2D masks) or RGB hex strings (3D masks) to `"stuff"` or `"thing"` for each class

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polylines for each region. Typical values are 1-3 pixels

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.classification_to_detections(_sample_collection_ , _in_field_ , _out_field_ , _progress =None_)#
    

Converts the [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") field of the collection into a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field containing a single detection whose bounding box spans the entire image.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") field

  * **out_field** â the name of the [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field to populate

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.classifications_to_detections(_sample_collection_ , _in_field_ , _out_field_ , _progress =None_)#
    

Converts the [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") field of the collection into a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field containing detections whose bounding boxes span the entire image with one detection for each classification.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") field

  * **out_field** â the name of the [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field to populate

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.index_to_instance(_sample_collection_ , _label_field_ , _index_attr ='index'_, _clear_index =False_, _progress =None_)#
    

Populates [`fiftyone.core.labels.Instance`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Instance "fiftyone.core.labels.Instance") values in the ``instance``attribute of the specified label field based on the values in the specified index attribute.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **label_field** â the label field to process. Supported types are [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint"), and [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **index_attr** (_"index"_) â the attribute whose unique values define the object instances. When `index_attr="index"` specifically, the `(label, index)` of each object is used as the unique identifier. Otherwise, the `index_attr` values alone are used. In either case, any objects whose index attribute is None/missing are not assigned an `instance`

  * **clear_index** (_False_) â whether to clear the values in `index_attr` (True) or leave them (False) after populating the `instance` attribute

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.perform_nms(_sample_collection_ , _in_field_ , _out_field =None_, _iou_thresh =0.5_, _confidence_thresh =None_, _classwise =True_, _progress =None_)#
    

Performs non-maximum suppression (NMS) on the specified [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field.

NMS is a post-processing technique used in object detection to eliminate duplicate detections and select the most relevant detected objects. This helps reduce false positives.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **in_field** â the name of the [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field

  * **out_field** (_None_) â the name of the [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field to populate. If not specified, the input field is updated in-place

  * **iou_thresh** (_0.5_) â an intersection over union (IoU) threshold to use. This determines the minimum overlap required between bounding boxes to be considered duplicates. Bounding boxes with IoU values greater than or equal to this threshold will be suppressed

  * **confidence_thresh** (_None_) â a minimum confidence score required for a detection to be considered valid. Detections with confidence scores lower than this threshold will be discarded

  * **classwise** (_True_) â whether to treat each class `label` separately (True) or suppress all detections jointly (False)

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.labels.detections_3d_to_cuboids_2d(_sample_collection: ~fiftyone.core.collections.SampleCollection, spatial_slice_name: str, camera_slice_name: str, in_field: str, out_field: str, transformations: ~typing.Dict[str, ~typing.List[~typing.Tuple[list[float] | ~numpy.ndarray, list[list[float]] | ~numpy.ndarray]]], camera_params: ~typing.Dict[str, ~typing.Dict[str, ~typing.Any]], forward_transform_flags: ~typing.Dict[str, ~typing.List[bool]] | None = None, camera_model: ~typing.Callable = <function pinhole_projector>, transformation_key_field: str = 'id', camera_key_field: str = 'id', progress=None_)#
    

High-level orchestration of 3D â 2D label conversion. Processes the in_field on the spatial_slice_name slice of a grouped sample collection, uses the transformations and camera parameters to convert the labels to 2D polylines, and saves them to the out_field on the camera_slice_name slice.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **spatial_slice_name** â the name of the spatial slice in the sample_collection

  * **camera_slice_name** â the name of the camera slice in the sample_collection

  * **in_field** â the name of the [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") field containing 3D labels to convert

  * **out_field** â the name of the [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") field to populate with 2D cuboids

  * **transformations** â a dict mapping transformation_key_field to a list of transformation tuples (translation, rotation) for each sample in the sample_collection. Translation is a 3-element list or np.ndarray, and rotation is a (3, 3) list of lists or np.ndarray representing a rotation matrix.

  * **camera_params** â a dict mapping camera_key_field to per-camera parameter dicts required by camera_model. Each dict must include an `"intrinsics"` 3x3 (or 4x4) matrix if using the default pinhole camera model; additional keys such as distortion parameters may be provided depending on the model

  * **forward_transform_flags** â an optional dict mapping transformation_key_field to lists of booleans indicating whether to apply forward or inverse transformations for each transform in the list of transformations for each sample

  * **camera_model** (_fou3d.pinhole_projector_) â a callable that takes 3D points in the camera coordinate system and the camera parameters dict and returns the projected 2D points in pixel coordinates

  * **transformation_key_field** (_"id"_) â the key field to use for looking up transformations for each sample

  * **camera_key_field** (_"id"_) â the key field to use for looking up camera parameters for each camera sample

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
