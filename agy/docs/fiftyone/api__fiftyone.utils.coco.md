---
source_url: https://docs.voxel51.com/api/fiftyone.utils.coco.html
---

# fiftyone.utils.coco#

Utilities for working with datasets in [COCO format](https://cocodataset.org/#format-data).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`add_coco_labels`(sample_collection,Â ...[,Â ...]) | Adds the given COCO labels to the collection.  
---|---  
`load_coco_detection_annotations`(json_path[,Â ...]) | Loads the COCO annotations from the given JSON file.  
`parse_coco_categories`(categories) | Parses the COCO categories list.  
`download_coco_dataset_split`(dataset_dir,Â split) | Utility that downloads full or partial splits of the [COCO dataset](https://cocodataset.org).  
  
**Classes:**

`COCODetectionDatasetImporter`([dataset_dir,Â ...]) | Importer for COCO detection datasets stored on disk.  
---|---  
`COCODetectionDatasetExporter`([export_dir,Â ...]) | Exporter that writes COCO detection datasets to disk.  
`COCOObject`([id,Â image_id,Â category_id,Â ...]) | An object in COCO format.  
  
fiftyone.utils.coco.add_coco_labels(_sample_collection_ , _label_field_ , _labels_or_path_ , _categories_ , _label_type ='detections'_, _coco_id_field =None_, _include_annotation_id =False_, _extra_attrs =True_, _use_polylines =False_, _tolerance =None_)#
    

Adds the given COCO labels to the collection.

The `labels_or_path` argument can be any of the following:

  * a list of COCO annotations in the format below

  * the path to a JSON file containing a list of COCO annotations

  * the path to a JSON file whose `"annotations"` key contains a list of COCO annotations




When `label_type="detections"`, the labels should have format:
    
    
    [
        {
            "id": 1,
            "image_id": 1,
            "category_id": 1,
            "bbox": [260, 177, 231, 199],
    
            # optional
            "score": 0.95,
            "area": 45969,
            "iscrowd": 0,
    
            # extra attrs
            ...
        },
        ...
    ]
    

When `label_type="segmentations"`, the labels should have format:
    
    
    [
        {
            "id": 1,
            "image_id": 1,
            "category_id": 1,
            "bbox": [260, 177, 231, 199],
            "segmentation": [...],
    
            # optional
            "score": 0.95,
            "area": 45969,
            "iscrowd": 0,
    
            # extra attrs
            ...
        },
        ...
    ]
    

When `label_type="keypoints"`, the labels should have format:
    
    
    [
        {
            "id": 1,
            "image_id": 1,
            "category_id": 1,
            "keypoints": [224, 226, 2, ...],
            "num_keypoints": 10,
    
            # extra attrs
            ...
        },
        ...
    ]
    

See [this page](https://cocodataset.org/#format-data) for more information about the COCO data format.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **label_field** â the label field in which to store the labels. The field will be created if necessary

  * **labels_or_path** â a list of COCO annotations or the path to a JSON file containing such data on disk

  * **categories** â 

can be any of the following:

    * a list of category dicts in the format of `parse_coco_categories()` specifying the classes and their category IDs

    * a dict mapping class IDs to class labels

    * a list of class labels whose 1-based ordering is assumed to correspond to the category IDs in the provided COCO labels

  * **label_type** (_"detections"_) â the type of labels to load. Supported values are `("detections", "segmentations", "keypoints")`

  * **coco_id_field** (_None_) â 

this parameter determines how to map the predictions onto samples in `sample_collection`. The supported values are:

    * `None` (default): in this case, the `image_id` of the predictions are assumed to be the 1-based positional indexes of samples in `sample_collection`

    * the name of a field of `sample_collection` containing the COCO IDs for the samples that correspond to the `image_id` of the predictions

  * **include_annotation_id** (_False_) â whether to include the COCO ID of each annotation in the loaded labels

  * **extra_attrs** (_True_) â 

whether to load extra annotation attributes onto the imported labels. Supported values are:

    * `True`: load all extra attributes found

    * `False`: do not load extra attributes

    * a name or list of names of specific attributes to load

  * **use_polylines** (_False_) â whether to represent segmentations as [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances rather than [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with dense masks

  * **tolerance** (_None_) â a tolerance, in pixels, when generating approximate polylines for instance masks. Typical values are 1-3 pixels




class fiftyone.utils.coco.COCODetectionDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _label_types =None_, _classes =None_, _image_ids =None_, _include_id =False_, _include_annotation_id =False_, _include_license =False_, _extra_attrs =True_, _only_matching =False_, _use_polylines =False_, _tolerance =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for COCO detection datasets stored on disk.

See [this page](user_guide__import_datasets.md#cocodetectiondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

    * a dict mapping filenames to absolute filepaths

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a filename like `"labels.json"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels.json`

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "segmentations", "keypoints")`. By default, all label types are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. Only samples containing at least one instance of a specified class will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` ints or strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **include_id** (_False_) â whether to include the COCO ID of each sample in the loaded labels

  * **include_annotation_id** (_False_) â whether to include the COCO ID of each annotation in the loaded labels

  * **include_license** (_False_) â 

whether to include the license ID of each sample in the loaded labels, if available. Supported values are:

    * `"False"`: donât load the license

    * `True`/`"name"`: store the string license name

    * `"id"`: store the integer license ID

    * `"url"`: store the license URL

Note that the license descriptions (if available) are always loaded into `dataset.info["licenses"]` and can be used to convert between ID, name, and URL later

  * **extra_attrs** (_True_) â 

whether to load extra annotation attributes onto the imported labels. Supported values are:

    * `True`: load all extra attributes found

    * `False`: do not load extra attributes

    * a name or list of names of specific attributes to load

  * **only_matching** (_False_) â whether to only load labels that match the `classes` requirement that you provide (True), or to load all labels for samples that match the requirements (False)

  * **use_polylines** (_False_) â whether to represent segmentations as [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") instances rather than [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") with dense masks

  * **tolerance** (_None_) â a tolerance, in pixels, when generating approximate polylines for instance masks. Typical values are 1-3 pixels

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load. If `label_types` and/or `classes` are also specified, first priority will be given to samples that contain all of the specified label types and/or classes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the labels that it may return




setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

class fiftyone.utils.coco.COCODetectionDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _image_format =None_, _classes =None_, _categories =None_, _info =None_, _extra_attrs =True_, _coco_id =None_, _annotation_id =None_, _iscrowd ='iscrowd'_, _num_decimals =None_, _tolerance =None_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes COCO detection datasets to disk.

See [this page](user_guide__export_datasets.md#cocodetectiondataset-export) for format details.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. This has no effect if `data_path` and `labels_path` are absolute paths

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `export_dir` in which to export the media

    * an absolute directory path in which to export the media. In this case, the `export_dir` has no effect on the location of the data

    * a JSON filename like `"data.json"` specifying the filename of the manifest file in `export_dir` generated when `export_media` is `"manifest"`

    * an absolute filepath specifying the location to write the JSON manifest file when `export_media` is `"manifest"`. In this case, `export_dir` has no effect on the location of the data

If None, the default value of this parameter will be chosen based on the value of the `export_media` parameter

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Can be any of the following:

    * a filename like `"labels.json"` specifying the location in `export_dir` in which to export the labels

    * an absolute filepath to which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

If None, the labels will be exported into `export_dir` using the default filename

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **abs_paths** (_False_) â whether to store absolute paths to the images in the exported labels

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **classes** (_None_) â the list of possible class labels

  * **categories** (_None_) â a list of category dicts in the format of `parse_coco_categories()` specifying the classes and their category IDs

  * **info** (_None_) â a dict of info as returned by `load_coco_detection_annotations()` to include in the exported JSON. If not provided, this info will be extracted when `log_collection()` is called, if possible

  * **extra_attrs** (_True_) â 

whether to include extra object attributes in the exported labels. Supported values are:

    * `True`: export all extra attributes found

    * `False`: do not export extra attributes

    * a name or list of names of specific attributes to export

  * **coco_id** (_None_) â the name of a sample field containing the COCO IDs of each image

  * **annotation_id** (_None_) â the name of a label field containing the COCO annotation ID of each label

  * **iscrowd** (_"iscrowd"_) â the name of a detection attribute that indicates whether an object is a crowd (the value is automatically set to 0 if the attribute is not present)

  * **num_decimals** (_None_) â an optional number of decimal places at which to round bounding box pixel coordinates. By default, no rounding is done

  * **tolerance** (_None_) â a tolerance, in pixels, when generating approximate polylines for instance masks. Typical values are 1-3 pixels




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can handle label dictionaries with value-types specified by this dictionary. Not all keys need be present in the exported label dicts

  * `None`. In this case, the exporter makes no guarantees about the labels that it can export




setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_image_or_path_ , _label_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled

  * **metadata** (_None_) â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the sample. Only required when `requires_image_metadata()` is `True`




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

class fiftyone.utils.coco.COCOObject(_id =None_, _image_id =None_, _category_id =None_, _bbox =None_, _segmentation =None_, _keypoints =None_, _score =None_, _area =None_, _iscrowd =None_, _** attributes_)#
    

Bases: `object`

An object in COCO format.

Parameters:
    

  * **id** (_None_) â the ID of the annotation

  * **image_id** (_None_) â the ID of the image in which the annotation appears

  * **category_id** (_None_) â the category ID of the object

  * **bbox** (_None_) â a bounding box for the object in `[xmin, ymin, width, height]` format

  * **segmentation** (_None_) â the segmentation data for the object

  * **keypoints** (_None_) â the keypoints data for the object

  * **score** (_None_) â a confidence score for the object

  * **area** (_None_) â the area of the bounding box, in pixels

  * **iscrowd** (_None_) â whether the object is a crowd

  * ****attributes** â additional custom attributes




**Methods:**

`to_polyline`(frame_size[,Â classes_map,Â ...]) | Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the object.  
---|---  
`to_keypoints`(frame_size[,Â classes_map,Â ...]) | Returns a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") representation of the object.  
`to_detection`(frame_size[,Â classes_map,Â ...]) | Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the object.  
`to_anno_dict`() | Returns a COCO annotation dictionary representation of the object.  
`from_anno_dict`(d[,Â extra_attrs]) | Creates a `COCOObject` from a COCO annotation dict.  
`from_label`(label,Â metadata[,Â image_id,Â ...]) | Creates a `COCOObject` from a compatible [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label").  
  
to_polyline(_frame_size_ , _classes_map =None_, _supercategory_map =None_, _tolerance =None_, _include_id =False_)#
    

Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the object.

Parameters:
    

  * **frame_size** â the `(width, height)` of the image

  * **classes_map** (_None_) â a dict mapping class IDs to class labels

  * **supercategory_map** (_None_) â a dict mapping class names to category dicts

  * **tolerance** (_None_) â a tolerance, in pixels, when generating approximate polylines for instance masks. Typical values are 1-3 pixels

  * **include_id** (_False_) â whether to include the COCO ID of the object as a label attribute



Returns:
    

a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or None if no segmentation data is available

to_keypoints(_frame_size_ , _classes_map =None_, _supercategory_map =None_, _include_id =False_)#
    

Returns a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") representation of the object.

Parameters:
    

  * **frame_size** â the `(width, height)` of the image

  * **classes_map** (_None_) â a dict mapping class IDs to class labels

  * **supercategory_map** (_None_) â a dict mapping class names to category dicts

  * **include_id** (_False_) â whether to include the COCO ID of the object as a label attribute



Returns:
    

a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint"), or None if no keypoints data is available

to_detection(_frame_size_ , _classes_map =None_, _supercategory_map =None_, _load_segmentation =False_, _include_id =False_)#
    

Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the object.

Parameters:
    

  * **frame_size** â the `(width, height)` of the image

  * **classes_map** (_None_) â a dict mapping class IDs to class labels

  * **supercategory_map** (_None_) â a dict mapping class names to category dicts

  * **load_segmentation** (_False_) â whether to load the segmentation mask for the object, if available

  * **include_id** (_False_) â whether to include the COCO ID of the object as a label attribute



Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), or None if no bbox data is available

to_anno_dict()#
    

Returns a COCO annotation dictionary representation of the object.

Returns:
    

a COCO annotation dict

classmethod from_anno_dict(_d_ , _extra_attrs =True_)#
    

Creates a `COCOObject` from a COCO annotation dict.

Parameters:
    

  * **d** â a COCO annotation dict

  * **extra_attrs** (_True_) â 

whether to load extra annotation attributes. Supported values are:

    * `True`: load all extra attributes

    * `False`: do not load extra attributes

    * a name or list of names of specific attributes to load



Returns:
    

a `COCOObject`

classmethod from_label(_label_ , _metadata_ , _image_id =None_, _category_id =None_, _keypoint =None_, _extra_attrs =True_, _id_attr =None_, _iscrowd ='iscrowd'_, _num_decimals =None_, _tolerance =None_)#
    

Creates a `COCOObject` from a compatible [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label").

Parameters:
    

  * **label** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") for the image

  * **image_id** (_None_) â an image ID

  * **category_id** (_None_) â the category ID for the object

  * **keypoint** (_None_) â an optional [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") containing keypoints to include for the object

  * **extra_attrs** (_True_) â 

whether to include extra attributes from the object. Supported values are:

    * `True`: include all extra attributes found

    * `False`: do not include extra attributes

    * a name or list of names of specific attributes to include

  * **id_attr** (_None_) â the name of the attribute containing the annotation ID of the label, if any

  * **iscrowd** (_"iscrowd"_) â the name of the crowd attribute (the value is automatically set to 0 if the attribute is not present)

  * **num_decimals** (_None_) â an optional number of decimal places at which to round bounding box pixel coordinates. By default, no rounding is done

  * **tolerance** (_None_) â a tolerance, in pixels, when generating approximate polylines for instance masks. Typical values are 1-3 pixels



Returns:
    

a `COCOObject`

fiftyone.utils.coco.load_coco_detection_annotations(_json_path_ , _extra_attrs =True_)#
    

Loads the COCO annotations from the given JSON file.

See [this page](user_guide__import_datasets.md#cocodetectiondataset-import) for format details.

Parameters:
    

  * **json_path** â the path to the annotations JSON file

  * **extra_attrs** (_True_) â 

whether to load extra annotation attributes. Supported values are:

    * `True`: load all extra attributes found

    * `False`: do not load extra attributes

    * a name or list of names of specific attributes to load



Returns:
    

a tuple of

  * info: a dict of dataset info

  * classes_map: a dict mapping class IDs to labels

  * supercategory_map: a dict mapping class labels to category dicts

  * images: a dict mapping image IDs to image dicts

  * annotations: a dict mapping image IDs to list of `COCOObject` instances, or `None` for unlabeled datasets




fiftyone.utils.coco.parse_coco_categories(_categories_)#
    

Parses the COCO categories list.

Parameters:
    

**categories** â 

a list of dict of the form:
    
    
    [
        ...
        {
            "id": 2,
            "name": "cat",
            "supercategory": "animal",
            "keypoints": ["nose", "head", ...],
            "skeleton": [[12, 14], [14, 16], ...]
        },
        ...
    ]
    

Returns:
    

a tuple of

  * classes_map: a dict mapping class IDs to labels

  * supercategory_map: a dict mapping class labels to category dicts




fiftyone.utils.coco.download_coco_dataset_split(_dataset_dir_ , _split_ , _year ='2017'_, _label_types =None_, _classes =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_, _raw_dir =None_, _scratch_dir =None_)#
    

Utility that downloads full or partial splits of the [COCO dataset](https://cocodataset.org).

See [this page](user_guide__export_datasets.md#cocodetectiondataset-export) for the format in which `dataset_dir` will be arranged.

Any existing files are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory to download the dataset

  * **split** â the split to download. Supported values are `("train", "validation", "test")`

  * **year** (_"2017"_) â the dataset year to download. Supported values are `("2014", "2017")`

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "segmentations")`. By default, all label types are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. Only samples containing at least one instance of a specified class will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` ints or strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load. If `label_types` and/or `classes` are also specified, first priority will be given to samples that contain all of the specified label types and/or classes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded

  * **raw_dir** (_None_) â a directory in which full annotations files may be stored to avoid re-downloads in the future

  * **scratch_dir** (_None_) â a scratch directory to use to download any necessary temporary files



Returns:
    

  * num_samples: the total number of downloaded images

  * classes: the list of all classes

  * did_download: whether any content was downloaded (True) or if all necessary files were already downloaded (False)




Return type:
    

a tuple of

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
