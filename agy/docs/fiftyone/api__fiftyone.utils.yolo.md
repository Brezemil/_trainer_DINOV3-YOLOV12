---
source_url: https://docs.voxel51.com/api/fiftyone.utils.yolo.html
---

# fiftyone.utils.yolo#

Utilities for working with datasets in YOLO format.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`add_yolo_labels`(sample_collection,Â ...[,Â ...]) | Adds the given YOLO-formatted labels to the collection.  
---|---  
`load_yolo_annotations`(txt_path,Â classes[,Â ...]) | Loads the YOLO-style annotations from the given TXT file.  
  
**Classes:**

`YOLOv4DatasetImporter`([dataset_dir,Â ...]) | Importer for YOLOv4 datasets stored on disk.  
---|---  
`YOLOv5DatasetImporter`([dataset_dir,Â ...]) | Importer for YOLOv5 datasets stored on disk.  
`YOLOv4DatasetExporter`([export_dir,Â ...]) | Exporter that writes YOLOv4 datasets to disk.  
`YOLOv5DatasetExporter`([export_dir,Â split,Â ...]) | Exporter that writes YOLOv5 datasets to disk.  
`YOLOAnnotationWriter`() | Class for writing annotations in YOLO-style TXT format.  
  
fiftyone.utils.yolo.add_yolo_labels(_sample_collection_ , _label_field_ , _labels_path_ , _classes_ , _label_type ='detections'_, _mask_size =None_, _include_missing =False_)#
    

Adds the given YOLO-formatted labels to the collection.

Each YOLO txt file should be a space-delimited file whose rows define objects in one of the following formats:
    
    
    # Detections
    <target> <x-center> <y-center> <width> <height>
    <target> <x-center> <y-center> <width> <height> <confidence>
    
    # Instance segmentations or polygons
    <target> <x1> <y1> <x2> <y2> <x3> <y3> ...
    

where `target` is the zero-based integer index of the object class label from `classes` and the bounding box coordinates are expressed as relative coordinates in `[0, 1] x [0, 1]`.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **label_field** â the label field in which to store the labels. The field will be created if necessary

  * **labels_path** â 

the YOLO-formatted labels to load. This can be any of the following:

    * a dict mapping either image filenames or absolute filepaths to YOLO TXT filepaths. The image filenames/filepaths should match those in `sample_collection`, in any order

    * a list of YOLO TXT filepaths corresponding 1-1 to the samples in `sample_collection`

    * a directory containing YOLO TXT files whose filenames (less extension) correspond to image filenames in `sample_collection`, in any order

  * **classes** â the list of class label strings

  * **label_type** (_"detections"_) â the label format to load. The supported values are `("detections", "instances", "polylines")`

  * **mask_size** (_None_) â an optional `(width, height)` at which to render each instance mask. Only used when `label_type="instances"`. If no mask size is provided then instance masks are rendered proportionally to each imageâs dimensions

  * **include_missing** (_False_) â whether to insert empty labels for any samples in the input collection whose `label_field` is `None` after import




class fiftyone.utils.yolo.YOLOv4DatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _images_path =None_, _objects_path =None_, _classes =None_, _label_type ='detections'_, _mask_size =None_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for YOLOv4 datasets stored on disk.

See [this page](user_guide__import_datasets.md#yolov4dataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a folder name like `"labels"` or `"labels/"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the labels are assumed to be in the same folder as the data

  * **images_path** (_None_) â 

an optional parameter that enables explicit control over the location of the image listing file. Can be any of the following:

    * a filename like `"images.txt"` specifying the location of the image listing file labels in `dataset_dir`

    * an absolute filepath to the image listing file. In this case, `dataset_dir` has no effect on the location of the file

If None, the parameter will default to `images.txt`

  * **objects_path** (_None_) â 

an optional parameter that enables explicit control over the location of the object names file. Can be any of the following:

    * a filename like `"obj.names"` specifying the location of the object names file labels in `dataset_dir`

    * an absolute filepath to the object names file. In this case, `dataset_dir` has no effect on the location of the file

If None, the parameter will default to `obj.names`

  * **classes** (_None_) â the list of possible class labels. This does not need to be provided if `objects_path` contains the class labels

  * **label_type** (_"detections"_) â the label format to load. The supported values are `("detections", "instances", "polylines")`

  * **mask_size** (_None_) â an optional `(width, height)` at which to render each instance mask. Only used when `label_type="instances"`. If no mask size is provided then instance masks are rendered proportionally to each imageâs dimensions

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with labels (False)

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




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

class fiftyone.utils.yolo.YOLOv5DatasetImporter(_dataset_dir =None_, _yaml_path =None_, _split ='val'_, _label_type ='detections'_, _mask_size =None_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for YOLOv5 datasets stored on disk.

See [this page](user_guide__import_datasets.md#yolov5dataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `yaml_path` must be provided

  * **yaml_path** (_None_) â 

an optional parameter that enables explicit control over the location of the dataset YAML file. Can be any of the following:

    * a filename like `"dataset.yaml"` specifying the name of the YAML file in `dataset_dir`

    * an absolute path to the YAML file. In this case, `dataset_dir` has no effect

If None, the parameter will default to `dataset.yaml`

  * **split** (_"val"_) â the split to load. Typical values are `("train", "val")`

  * **label_type** (_"detections"_) â the label format to load. The supported values are `("detections", "instances", "polylines")`

  * **mask_size** (_None_) â an optional `(width, height)` at which to render each instance mask. Only used when `label_type="instances"`. If no mask size is provided then instance masks are rendered proportionally to each imageâs dimensions

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with labels (False)

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




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

class fiftyone.utils.yolo.YOLOv4DatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _objects_path =None_, _images_path =None_, _export_media =None_, _rel_dir =None_, _classes =None_, _include_confidence =False_, _use_masks =False_, _tolerance =2_, _image_format =None_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes YOLOv4 datasets to disk.

See [this page](user_guide__export_datasets.md#yolov4dataset-export) for format details.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. This has no effect if `data_path`, `objects_path`, and `images_path` are absolute paths

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported data and labels. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `export_dir` in which to export the data and labels

    * an absolute directory path in which to export the data and labels. In this case, the `export_dir` has no effect on the location of the data

If None, the data will be written into `export_dir` using the default folder name

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Can be any of the following:

    * a folder name like `"labels"` or `"labels/"` specifying the location in `export_dir` in which to export the labels

    * an absolute folder path to which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

If None, the labels will be written into the same directory as the exported media

  * **objects_path** (_None_) â 

an optional parameter that enables explicit control over the location of the object names file. Can be any of the following:

    * a filename like `"obj.names"` specifying the location in `export_dir` in which to export the object names

    * an absolute filepath to which to export the object names. In this case, the `export_dir` has no effect on the location of the object names

If None, the object names will be written into `export_dir` using the default filename, unless no media is being exported, in which case this file will not be written

  * **images_path** (_None_) â 

an optional parameter that enables explicit control over the location of the image listing file. Can be any of the following:

    * a filename like `"images.txt"` specifying the location in `export_dir` in which to export the image listing

    * an absolute filepath to which to export the image listing. In this case, the `export_dir` has no effect on the location of the image listing

If None, the image listing will be written into `export_dir` using the default filename, unless no media is being exported, in which case this file will not be written

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `data_path` and `labels_path` to generate output paths for each exported image and labels file. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **classes** (_None_) â the list of possible class labels

  * **include_confidence** (_False_) â whether to include detection confidences in the export, if they exist

  * **use_masks** (_False_) â whether to export detections based on their instance masks rather than their bounding boxes

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polylines for the instance masks. Typical values are 1-3 pixels

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.yolo.YOLOv5DatasetExporter(_export_dir =None_, _split ='val'_, _data_path =None_, _labels_path =None_, _yaml_path =None_, _export_media =None_, _rel_dir =None_, _classes =None_, _include_confidence =False_, _use_masks =False_, _tolerance =2_, _image_format =None_, _include_path =True_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes YOLOv5 datasets to disk.

See [this page](user_guide__export_datasets.md#yolov5dataset-export) for format details.

Parameters:
    

  * **export_dir** (_None_) â the directory to write the export. This has no effect if `data_path`, `labels_path`, and `yaml_path` are absolute paths

  * **split** (_"val"_) â the split being exported. Typical values are `("train", "val")`

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported media. Can be any of the following:

    * a folder name like `"images"` or `"images/"` specifying a subfolder of `export_dir` in which to export the images

    * an absolute directory path in which to export the images. In this case, the `export_dir` has no effect on the location of the images

If None, the data will be written into `export_dir` using the default folder name

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Can be any of the following:

    * a folder name like `"labels"` or `"labels/"` specifying the location in `export_dir` in which to export the labels

    * an absolute folder path to which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

If None, the labels will be written into `export_dir` using the default folder name

  * **yaml_path** (_None_) â 

an optional parameter that enables explicit control over the location of the dataset YAML file. Can be any of the following:

    * a filename like `"dataset.yaml"` specifying the location in `export_dir` to write the YAML file

    * an absolute filepath to which to write the YAML file. In this case, the `export_dir` has no effect on the location of the image listing

If None, the dataset YAML file will be written into `export_dir` using the default filename, unless no media is being exported, in which case this file will not be written

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `data_path` and `labels_path` to generate output paths for each exported image and labels file. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **classes** (_None_) â the list of possible class labels

  * **include_confidence** (_False_) â whether to include detection confidences in the export, if they exist

  * **use_masks** (_False_) â whether to export detections based on their instance masks rather than their bounding boxes

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polylines for the instance masks. Typical values are 1-3 pixels

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **include_path** (_True_) â whether to include the directory name containing the YAML file in the `path` key of the exported YAML




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.yolo.YOLOAnnotationWriter#
    

Bases: `object`

Class for writing annotations in YOLO-style TXT format.

**Methods:**

`write`(label,Â txt_path,Â labels_map_rev[,Â ...]) | Writes the labels to disk.  
---|---  
  
write(_label_ , _txt_path_ , _labels_map_rev_ , _dynamic_classes =False_, _include_confidence =False_, _use_masks =False_, _tolerance =2_)#
    

Writes the labels to disk.

Parameters:
    

  * **label** â a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

  * **txt_path** â the path to write the annotation TXT file

  * **labels_map_rev** â a dictionary mapping class label strings to target integers

  * **dynamic_classes** (_False_) â whether to dynamically add new labels to `labels_map_rev`

  * **include_confidence** (_False_) â whether to include confidences in the export, if they exist

  * **use_masks** (_False_) â whether to export detections based on their instance masks rather than their bounding boxes

  * **tolerance** (_2_) â a tolerance, in pixels, when generating approximate polylines for the instance masks. Typical values are 1-3 pixels




fiftyone.utils.yolo.load_yolo_annotations(_txt_path_ , _classes_ , _label_type ='detections'_, _mask_size =None_, _frame_size =None_)#
    

Loads the YOLO-style annotations from the given TXT file.

The txt file should be a space-delimited file where each row corresponds to an object in one the following formats:
    
    
    # Detections
    <target> <x-center> <y-center> <width> <height>
    <target> <x-center> <y-center> <width> <height> <confidence>
    
    # Instance segmentations or polygons
    <target> <x1> <y1> <x2> <y2> <x3> <y3> ...
    

where `target` is the zero-based integer index of the object class label from `classes` and all coordinates are expressed as relative values in `[0, 1] x [0, 1]`.

Parameters:
    

  * **txt_path** â the path to the annotations TXT file

  * **classes** â the list of class label strings

  * **label_type** (_"detections"_) â the label format to load. The supported values are `("detections", "instances", "polylines")`

  * **mask_size** (_None_) â an optional `(width, height)` at which to render each instance mask. Only used when `label_type="instances"`

  * **frame_size** (_None_) â the `(width, height)` of the frame containing the annotations. Only used when `label_type="instances"` and no `mask_size` is provided



Returns:
    

a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
