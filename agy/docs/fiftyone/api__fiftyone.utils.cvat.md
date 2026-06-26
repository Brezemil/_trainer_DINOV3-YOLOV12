---
source_url: https://docs.voxel51.com/api/fiftyone.utils.cvat.html
---

# fiftyone.utils.cvat#

Utilities for working with datasets in [CVAT format](https://github.com/opencv/cvat).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`import_annotations`(sample_collection[,Â ...]) | Imports annotations from the specified CVAT project or task(s) into the given sample collection.  
---|---  
`load_cvat_image_annotations`(xml_path) | Loads the CVAT image annotations from the given XML file.  
`load_cvat_video_annotations`(xml_path) | Loads the CVAT video annotations from the given XML file.  
  
**Classes:**

`CVATImageDatasetImporter`([dataset_dir,Â ...]) | Importer for CVAT image datasets stored on disk.  
---|---  
`CVATVideoDatasetImporter`([dataset_dir,Â ...]) | Importer for CVAT video datasets stored on disk.  
`CVATImageDatasetExporter`([export_dir,Â ...]) | Exporter that writes CVAT image datasets to disk.  
`CVATVideoDatasetExporter`([export_dir,Â ...]) | Exporter that writes CVAT video datasets to disk.  
`CVATTaskLabels`([labels]) | Description of the labels in a CVAT image annotation task.  
`CVATImage`(id,Â name,Â width,Â height[,Â tags,Â ...]) | An annotated image in CVAT image format.  
`HasCVATBinaryMask`() | Mixin for CVAT annotations that store RLE format instance masks.  
`HasCVATPoints`(points) | Mixin for CVAT annotations that store a list of `(x, y)` pixel coordinates.  
`CVATImageAnno`([occluded,Â attributes]) | Mixin for annotations in CVAT image format.  
`CVATImageTag`(label[,Â attributes]) | A tag in CVAT image format.  
`CVATImageBox`(label,Â xtl,Â ytl,Â xbr,Â ybr[,Â ...]) | An object bounding box in CVAT image format.  
`CVATImagePolygon`(label,Â points[,Â occluded,Â ...]) | A polygon in CVAT image format.  
`CVATImagePolyline`(label,Â points[,Â occluded,Â ...]) | A polyline in CVAT image format.  
`CVATImagePoints`(label,Â points[,Â occluded,Â ...]) | A set of keypoints in CVAT image format.  
`CVATTrack`(id,Â label,Â width,Â height[,Â boxes,Â ...]) | An annotation track in CVAT video format.  
`CVATVideoAnno`([outside,Â occluded,Â keyframe,Â ...]) | Mixin for annotations in CVAT video format.  
`CVATVideoBox`(frame,Â label,Â xtl,Â ytl,Â xbr,Â ybr) | An object bounding box in CVAT video format.  
`CVATVideoPolygon`(frame,Â label,Â points[,Â ...]) | A polygon in CVAT video format.  
`CVATVideoPolyline`(frame,Â label,Â points[,Â ...]) | A polyline in CVAT video format.  
`CVATVideoPoints`(frame,Â label,Â points[,Â ...]) | A set of keypoints in CVAT video format.  
`CVATAttribute`(name,Â value) | An attribute in CVAT image format.  
`CVATImageAnnotationWriter`() | Class for writing annotations in CVAT image format.  
`CVATVideoAnnotationWriter`() | Class for writing annotations in CVAT video format.  
`CVATBackendConfig`(name,Â label_schema[,Â ...]) | Class for configuring `CVATBackend` instances.  
`CVATBackend`(*args,Â **kwargs) | Class for interacting with the CVAT annotation backend.  
`CVATAnnotationResults`(samples,Â config,Â ...) | Class that stores all relevant information needed to monitor the progress of an annotation run sent to CVAT and download the results.  
`CVATAnnotationAPI`(name,Â url[,Â username,Â ...]) | A class to facilitate connection to and management of tasks in CVAT.  
`CVATLabel`(label_dict,Â class_map,Â ...[,Â ...]) | A label returned by the CVAT API.  
`CVATShape`(label_dict,Â class_map,Â ...[,Â ...]) | A shape returned by the CVAT API.  
`CVATTag`(label_dict,Â class_map,Â attr_id_map,Â ...) | A tag returned by the CVAT API.  
  
fiftyone.utils.cvat.import_annotations(_sample_collection_ , _project_name =None_, _project_id =None_, _task_ids =None_, _data_path =None_, _label_types =None_, _insert_new =True_, _download_media =False_, _num_workers =None_, _occluded_attr =None_, _group_id_attr =None_, _backend ='cvat'_, _** kwargs_)#
    

Imports annotations from the specified CVAT project or task(s) into the given sample collection.

Provide one of `project_name`, `project_id`, or `task_ids` to perform an import.

This method can be configured in any of the following three ways:

  1. Pass the `data_path` argument to define a mapping between media filenames in CVAT and local filepaths to the same media.

  2. Pass the `download_media=True` option to download both the annotations and the media files themselves, which are stored in a directory you specify via the `data_path` argument.

  3. Donât provide `data_path` or `download_media=True`, in which case it is assumed that the CVAT filenames correspond to the base filenames of existing sample filepaths in the provided `sample_collection`.




Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **project_name** (_None_) â the name of a CVAT project to import

  * **project_id** (_None_) â the ID of a CVAT project to import

  * **task_ids** (_None_) â a CVAT task ID or iterable of CVAT task IDs to import

  * **data_path** (_None_) â 

a parameter that defines the correspondence between the filenames in CVAT and the filepaths of `sample_collection`. Can be any of the following:

    * a directory on disk where the media files reside. In this case, the filenames must match those in CVAT

    * a dict mapping CVAT filenames to absolute filepaths to the corresponding media on disk

    * the path to a JSON manifest on disk containing a mapping between CVAT filenames and absolute filepaths to the media on disk

By default, only annotations whose filename matches an existing filepath in `sample_collection` will be imported

  * **label_types** (_None_) â 

an optional parameter specifying the label types to import. Can be any of the following:

    * `None` (default): all label types will be stored in fields of the same name on `sample_collection`

    * a list of label types to load. In this case, the labels will be stored in fields of the same names in `sample_collection`

    * a dict mapping label types to field names of `sample_collection` in which to store the labels

    * `"prompt"`: present an interactive prompt to decide/discard field names in which to store each label type

  * **insert_new** (_True_) â whether to create new samples for any media for which annotations are found in CVAT but which do not exist in `sample_collection`

  * **download_media** (_False_) â whether to download the images or videos found in CVAT to the directory or filepaths in `data_path` if not already present

  * **num_workers** (_None_) â a suggested number of threads to use when downloading media

  * **occluded_attr** (_None_) â an optional attribute name in which to store the occlusion information for all spatial labels

  * **group_id_attr** (_None_) â an optional attribute name in which to store the group id for labels

  * **backend** (_"cvat"_) â the name of the CVAT backend to use

  * ****kwargs** â CVAT authentication credentials to pass to `CVATBackendConfig`




class fiftyone.utils.cvat.CVATImageDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for CVAT image datasets stored on disk.

See [this page](user_guide__import_datasets.md#cvatimagedataset-import) for format details.

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

    * a filename like `"labels.xml"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels.xml`

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with label entries (False)

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

class fiftyone.utils.cvat.CVATVideoDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledVideoDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledVideoDatasetImporter "fiftyone.utils.data.importers.LabeledVideoDatasetImporter"), [`ImportPathsMixin`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.ImportPathsMixin "fiftyone.utils.data.importers.ImportPathsMixin")

Importer for CVAT video datasets stored on disk.

See [this page](user_guide__import_datasets.md#cvatvideodataset-import) for format details.

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

    * a folder name like `"labels"` or `"labels/"` specifying the location of the labels in `dataset_dir`

    * an absolute folder path to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels/`

  * **include_all_data** (_False_) â whether to generate samples for all videos in the data directory (True) rather than only creating samples for videos with label entries (False)

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the sample-level labels that it may return




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the importer makes no guarantees about the frame labels that it may return




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

class fiftyone.utils.cvat.CVATImageDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _image_format =None_)#
    

Bases: [`LabeledImageDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledImageDatasetExporter "fiftyone.utils.data.exporters.LabeledImageDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes CVAT image datasets to disk.

See [this page](user_guide__export_datasets.md#cvatimagedataset-export) for format details.

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

    * a filename like `"labels.xml"` specifying the location in `export_dir` in which to export the labels

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




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(image_or_path,Â labels[,Â metadata]) | Exports the given sample to the dataset.  
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

export_sample(_image_or_path_ , _labels_ , _metadata =None_)#
    

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

class fiftyone.utils.cvat.CVATVideoDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_)#
    

Bases: [`LabeledVideoDatasetExporter`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.LabeledVideoDatasetExporter "fiftyone.utils.data.exporters.LabeledVideoDatasetExporter"), [`ExportPathsMixin`](api__fiftyone.utils.data.exporters.md#fiftyone.utils.data.exporters.ExportPathsMixin "fiftyone.utils.data.exporters.ExportPathsMixin")

Exporter that writes CVAT video datasets to disk.

See [this page](user_guide__export_datasets.md#cvatvideodataset-export) for format details.

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

    * a folder name like `"labels"` or `"labels/"` specifying the location in `export_dir` in which to export the labels

    * an absolute filepath to which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

If None, the labels will be exported into `export_dir` using the default folder name

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(video_path,Â _,Â frames[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple label fields with value-types specified by this dictionary. Not all keys need be present in the exported sample-level labels

  * `None`. In this case, the exporter makes no guarantees about the sample-level labels that it can export




property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export multiple frame label fields with value-types specified by this dictionary. Not all keys need be present in the exported frame labels

  * `None`. In this case, the exporter makes no guarantees about the frame labels that it can export




setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_video_path_ , ___ , _frames_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **label** â an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no sample-level labels

  * **frames** â a dictionary mapping frame numbers to dictionaries that map field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample has no frame-level labels

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

class fiftyone.utils.cvat.CVATTaskLabels(_labels =None_)#
    

Bases: `object`

Description of the labels in a CVAT image annotation task.

Parameters:
    

**labels** (_None_) â 

a list of label dicts in the following format:
    
    
    [
        {
            "name": "car",
            "attributes": [
                {
                    "name": "type"
                    "categories": ["coupe", "sedan", "truck"]
                },
                ...
            }
        },
        ...
    ]
    

**Methods:**

`merge_task_labels`(task_labels) | Merges the given `CVATTaskLabels` into this instance.  
---|---  
`to_schema`() | Returns an `eta.core.image.ImageLabelsSchema` representation of the task labels.  
`from_cvat_images`(cvat_images) | Creates a `CVATTaskLabels` instance that describes the active schema of the given annotations.  
`from_cvat_tracks`(cvat_tracks) | Creates a `CVATTaskLabels` instance that describes the active schema of the given annotations.  
`from_labels_dict`(d) | Creates a `CVATTaskLabels` instance from the `<labels>` tag of a CVAT annotation XML file.  
`from_schema`(schema) | Creates a `CVATTaskLabels` instance from an `eta.core.image.ImageLabelsSchema`.  
  
merge_task_labels(_task_labels_)#
    

Merges the given `CVATTaskLabels` into this instance.

Parameters:
    

**task_labels** â a `CVATTaskLabels`

to_schema()#
    

Returns an `eta.core.image.ImageLabelsSchema` representation of the task labels.

Note that CVATâs task labels schema does not distinguish between boxes, polylines, and keypoints, so the returned schema stores all annotations under the `"objects"` field.

Returns:
    

an `eta.core.image.ImageLabelsSchema`

classmethod from_cvat_images(_cvat_images_)#
    

Creates a `CVATTaskLabels` instance that describes the active schema of the given annotations.

Parameters:
    

**cvat_images** â a list of `CVATImage` instances

Returns:
    

a `CVATTaskLabels`

classmethod from_cvat_tracks(_cvat_tracks_)#
    

Creates a `CVATTaskLabels` instance that describes the active schema of the given annotations.

Parameters:
    

**cvat_tracks** â a list of `CVATTrack` instances

Returns:
    

a `CVATTaskLabels`

classmethod from_labels_dict(_d_)#
    

Creates a `CVATTaskLabels` instance from the `<labels>` tag of a CVAT annotation XML file.

Parameters:
    

**d** â a dict representation of a `<labels>` tag

Returns:
    

a `CVATTaskLabels`

classmethod from_schema(_schema_)#
    

Creates a `CVATTaskLabels` instance from an `eta.core.image.ImageLabelsSchema`.

Parameters:
    

**schema** â an `eta.core.image.ImageLabelsSchema`

Returns:
    

a `CVATTaskLabels`

class fiftyone.utils.cvat.CVATImage(_id_ , _name_ , _width_ , _height_ , _tags =None_, _boxes =None_, _polygons =None_, _polylines =None_, _points =None_, _subset =None_)#
    

Bases: `object`

An annotated image in CVAT image format.

Parameters:
    

  * **id** â the ID of the image

  * **name** â the filename of the image

  * **width** â the width of the image, in pixels

  * **height** â the height of the image, in pixels

  * **tags** (_None_) â a list of `CVATImageTag` instances

  * **boxes** (_None_) â a list of `CVATImageBox` instances

  * **polygons** (_None_) â a list of `CVATImagePolygon` instances

  * **polylines** (_None_) â a list of `CVATImagePolyline` instances

  * **points** (_None_) â a list of `CVATImagePoints` instances

  * **subset** (_None_) â the project subset of the image, if any




**Attributes:**

`has_tags` | Whether this image has tags.  
---|---  
`has_boxes` | Whether this image has 2D boxes.  
`has_polylines` | Whether this image has polygons or polylines.  
`has_points` | Whether this image has keypoints.  
  
**Methods:**

`iter_annos`() | Returns an iterator over the annotations in the image.  
---|---  
`get_image_metadata`() | Returns a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the annotations.  
`to_labels`() | Returns [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") representations of the annotations.  
`from_labels`(labels,Â metadata) | Creates a `CVATImage` from a dictionary of labels.  
`from_image_dict`(d) | Creates a `CVATImage` from an `<image>` tag of a CVAT image annotations XML file.  
  
property has_tags#
    

Whether this image has tags.

property has_boxes#
    

Whether this image has 2D boxes.

property has_polylines#
    

Whether this image has polygons or polylines.

property has_points#
    

Whether this image has keypoints.

iter_annos()#
    

Returns an iterator over the annotations in the image.

Returns:
    

an iterator that emits `CVATImageAnno` instances

get_image_metadata()#
    

Returns a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instance for the annotations.

Returns:
    

a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata")

to_labels()#
    

Returns [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") representations of the annotations.

Returns:
    

a dict mapping field keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

classmethod from_labels(_labels_ , _metadata_)#
    

Creates a `CVATImage` from a dictionary of labels.

Parameters:
    

  * **labels** â a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") for the image



Returns:
    

a `CVATImage`

classmethod from_image_dict(_d_)#
    

Creates a `CVATImage` from an `<image>` tag of a CVAT image annotations XML file.

Parameters:
    

**d** â a dict representation of an `<image>` tag

Returns:
    

a `CVATImage`

class fiftyone.utils.cvat.HasCVATBinaryMask#
    

Bases: `object`

Mixin for CVAT annotations that store RLE format instance masks.

class fiftyone.utils.cvat.HasCVATPoints(_points_)#
    

Bases: `object`

Mixin for CVAT annotations that store a list of `(x, y)` pixel coordinates.

points#
    

a list of `(x, y)` pixel coordinates defining points

**Attributes:**

`points_str` |   
---|---  
  
property points_str#
    

class fiftyone.utils.cvat.CVATImageAnno(_occluded =None_, _attributes =None_)#
    

Bases: `object`

Mixin for annotations in CVAT image format.

Parameters:
    

  * **occluded** (_None_) â whether the object is occluded

  * **attributes** (_None_) â a list of `CVATAttribute` instances




class fiftyone.utils.cvat.CVATImageTag(_label_ , _attributes =None_)#
    

Bases: `CVATImageAnno`

A tag in CVAT image format.

Parameters:
    

  * **label** â the tag string

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_classification`() | Returns a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") representation of the tag.  
---|---  
`from_classification`(classification) | Creates a `CVATImageTag` from a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification").  
`from_tag_dict`(d) | Creates a `CVATImageTag` from a `<tag>` tag of a CVAT image annotation XML file.  
  
to_classification()#
    

Returns a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") representation of the tag.

Returns:
    

a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

classmethod from_classification(_classification_)#
    

Creates a `CVATImageTag` from a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification").

Parameters:
    

**classification** â a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

Returns:
    

a `CVATImageTag`

classmethod from_tag_dict(_d_)#
    

Creates a `CVATImageTag` from a `<tag>` tag of a CVAT image annotation XML file.

Parameters:
    

**d** â a dict representation of a `<tag>` tag

Returns:
    

a `CVATImageTag`

class fiftyone.utils.cvat.CVATImageBox(_label_ , _xtl_ , _ytl_ , _xbr_ , _ybr_ , _occluded =None_, _attributes =None_)#
    

Bases: `CVATImageAnno`

An object bounding box in CVAT image format.

Parameters:
    

  * **label** â the object label string

  * **xtl** â the top-left x-coordinate of the box, in pixels

  * **ytl** â the top-left y-coordinate of the box, in pixels

  * **xbr** â the bottom-right x-coordinate of the box, in pixels

  * **ybr** â the bottom-right y-coordinate of the box, in pixels

  * **occluded** (_None_) â whether the object is occluded

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_detection`(frame_size) | Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the box.  
---|---  
`from_detection`(detection,Â metadata) | Creates a `CVATImageBox` from a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").  
`from_box_dict`(d) | Creates a `CVATImageBox` from a `<box>` tag of a CVAT image annotation XML file.  
  
to_detection(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the box.

Parameters:
    

**frame_size** â the `(width, height)` of the image

Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

classmethod from_detection(_detection_ , _metadata_)#
    

Creates a `CVATImageBox` from a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").

Parameters:
    

  * **detection** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") for the image



Returns:
    

a `CVATImageBox`

classmethod from_box_dict(_d_)#
    

Creates a `CVATImageBox` from a `<box>` tag of a CVAT image annotation XML file.

Parameters:
    

**d** â a dict representation of a `<box>` tag

Returns:
    

a `CVATImageBox`

class fiftyone.utils.cvat.CVATImagePolygon(_label_ , _points_ , _occluded =None_, _attributes =None_)#
    

Bases: `CVATImageAnno`, `HasCVATPoints`

A polygon in CVAT image format.

Parameters:
    

  * **label** â the polygon label string

  * **points** â a list of `(x, y)` pixel coordinates defining the vertices of the polygon

  * **occluded** (_None_) â whether the polygon is occluded

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_polyline`(frame_size) | Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polygon.  
---|---  
`from_polyline`(polyline,Â metadata) | Creates a `CVATImagePolygon` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").  
`from_polygon_dict`(d) | Creates a `CVATImagePolygon` from a `<polygon>` tag of a CVAT image annotation XML file.  
  
**Attributes:**

`points_str` |   
---|---  
  
to_polyline(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polygon.

Parameters:
    

**frame_size** â the `(width, height)` of the image

Returns:
    

a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

classmethod from_polyline(_polyline_ , _metadata_)#
    

Creates a `CVATImagePolygon` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").

If the [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") is composed of multiple shapes, one `CVATImagePolygon` per shape will be generated.

Parameters:
    

  * **polyline** â a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") for the image



Returns:
    

a list of `CVATImagePolygon` instances

classmethod from_polygon_dict(_d_)#
    

Creates a `CVATImagePolygon` from a `<polygon>` tag of a CVAT image annotation XML file.

Parameters:
    

**d** â a dict representation of a `<polygon>` tag

Returns:
    

a `CVATImagePolygon`

property points_str#
    

class fiftyone.utils.cvat.CVATImagePolyline(_label_ , _points_ , _occluded =None_, _attributes =None_)#
    

Bases: `CVATImageAnno`, `HasCVATPoints`

A polyline in CVAT image format.

Parameters:
    

  * **label** â the polyline label string

  * **points** â a list of `(x, y)` pixel coordinates defining the vertices of the polyline

  * **occluded** (_None_) â whether the polyline is occluded

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_polyline`(frame_size) | Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polyline.  
---|---  
`from_polyline`(polyline,Â metadata) | Creates a `CVATImagePolyline` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").  
`from_polyline_dict`(d) | Creates a `CVATImagePolyline` from a `<polyline>` tag of a CVAT image annotation XML file.  
  
**Attributes:**

`points_str` |   
---|---  
  
to_polyline(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polyline.

Parameters:
    

**frame_size** â the `(width, height)` of the image

Returns:
    

a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

classmethod from_polyline(_polyline_ , _metadata_)#
    

Creates a `CVATImagePolyline` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").

If the [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") is composed of multiple shapes, one `CVATImagePolyline` per shape will be generated.

Parameters:
    

  * **polyline** â a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") for the image



Returns:
    

a list of `CVATImagePolyline` instances

classmethod from_polyline_dict(_d_)#
    

Creates a `CVATImagePolyline` from a `<polyline>` tag of a CVAT image annotation XML file.

Parameters:
    

**d** â a dict representation of a `<polyline>` tag

Returns:
    

a `CVATImagePolyline`

property points_str#
    

class fiftyone.utils.cvat.CVATImagePoints(_label_ , _points_ , _occluded =None_, _attributes =None_)#
    

Bases: `CVATImageAnno`, `HasCVATPoints`

A set of keypoints in CVAT image format.

Parameters:
    

  * **label** â the keypoints label string

  * **points** â a list of `(x, y)` pixel coordinates defining the vertices of the keypoints

  * **occluded** (_None_) â whether the keypoints are occluded

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_keypoint`(frame_size) | Returns a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") representation of the points.  
---|---  
`from_keypoint`(keypoint,Â metadata) | Creates a `CVATImagePoints` from a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").  
`from_points_dict`(d) | Creates a `CVATImagePoints` from a `<points>` tag of a CVAT image annotation XML file.  
  
**Attributes:**

`points_str` |   
---|---  
  
to_keypoint(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") representation of the points.

Parameters:
    

**frame_size** â the `(width, height)` of the image

Returns:
    

a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

classmethod from_keypoint(_keypoint_ , _metadata_)#
    

Creates a `CVATImagePoints` from a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").

Parameters:
    

  * **keypoint** â a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

  * **metadata** â a [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") for the image



Returns:
    

a `CVATImagePoints`

classmethod from_points_dict(_d_)#
    

Creates a `CVATImagePoints` from a `<points>` tag of a CVAT image annotation XML file.

Parameters:
    

**d** â a dict representation of a `<points>` tag

Returns:
    

a `CVATImagePoints`

property points_str#
    

class fiftyone.utils.cvat.CVATTrack(_id_ , _label_ , _width_ , _height_ , _boxes =None_, _polygons =None_, _polylines =None_, _points =None_)#
    

Bases: `object`

An annotation track in CVAT video format.

Parameters:
    

  * **id** â the ID of the track

  * **label** â the label for the track

  * **width** â the width of the video frames, in pixels

  * **height** â the height of the video frames, in pixels

  * **boxes** (_None_) â a dict mapping frame numbers to `CVATVideoBox` instances

  * **polygons** (_None_) â a dict mapping frame numbers to `CVATVideoPolygon` instances

  * **polylines** (_None_) â a dict mapping frame numbers to `CVATVideoPolyline` instances

  * **points** (_None_) â a dict mapping frame numbers to `CVATVideoPoints` instances




**Attributes:**

`has_boxes` | Whether this track has 2D boxes.  
---|---  
`has_polylines` | Whether this track has polygons or polylines.  
`has_points` | Whether this track has keypoints.  
  
**Methods:**

`iter_annos`() | Returns an iterator over the annotations in the track.  
---|---  
`to_labels`() | Returns [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") representations of the annotations.  
`from_labels`(id,Â labels,Â frame_size) | Creates a `CVATTrack` from a dictionary of labels.  
`from_track_dict`(d,Â frame_size) | Creates a `CVATTrack` from a `<track>` tag of a CVAT video annotation XML file.  
  
property has_boxes#
    

Whether this track has 2D boxes.

property has_polylines#
    

Whether this track has polygons or polylines.

property has_points#
    

Whether this track has keypoints.

iter_annos()#
    

Returns an iterator over the annotations in the track.

Returns:
    

an iterator that emits `CVATVideoAnno` instances

to_labels()#
    

Returns [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") representations of the annotations.

Returns:
    

a dict mapping frame numbers to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

classmethod from_labels(_id_ , _labels_ , _frame_size_)#
    

Creates a `CVATTrack` from a dictionary of labels.

Parameters:
    

  * **id** â the ID of the track

  * **labels** â a dict mapping frame numbers to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

  * **frame_size** â the `(width, height)` of the video frames



Returns:
    

a `CVATTrack`

classmethod from_track_dict(_d_ , _frame_size_)#
    

Creates a `CVATTrack` from a `<track>` tag of a CVAT video annotation XML file.

Parameters:
    

  * **d** â a dict representation of an `<track>` tag

  * **frame_size** â the `(width, height)` of the video frames



Returns:
    

a `CVATTrack`

class fiftyone.utils.cvat.CVATVideoAnno(_outside =None_, _occluded =None_, _keyframe =None_, _attributes =None_)#
    

Bases: `object`

Mixin for annotations in CVAT video format.

Parameters:
    

  * **outside** (_None_) â whether the object is outside (invisible)

  * **occluded** (_None_) â whether the object is occluded

  * **keyframe** (_None_) â whether the frame is a keyframe

  * **attributes** (_None_) â a list of `CVATAttribute` instances




class fiftyone.utils.cvat.CVATVideoBox(_frame_ , _label_ , _xtl_ , _ytl_ , _xbr_ , _ybr_ , _outside =None_, _occluded =None_, _keyframe =None_, _attributes =None_)#
    

Bases: `CVATVideoAnno`

An object bounding box in CVAT video format.

Parameters:
    

  * **frame** â the 0-based frame number

  * **label** â the object label string

  * **xtl** â the top-left x-coordinate of the box, in pixels

  * **ytl** â the top-left y-coordinate of the box, in pixels

  * **xbr** â the bottom-right x-coordinate of the box, in pixels

  * **ybr** â the bottom-right y-coordinate of the box, in pixels

  * **outside** (_None_) â whether the object is outside (invisible)

  * **occluded** (_None_) â whether the object is occluded

  * **keyframe** (_None_) â whether the frame is a keyframe

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_detection`(frame_size) | Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the box.  
---|---  
`from_detection`(frame_number,Â detection,Â ...) | Creates a `CVATVideoBox` from a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").  
`from_box_dict`(label,Â d) | Creates a `CVATVideoBox` from a `<box>` tag of a CVAT video annotation XML file.  
  
to_detection(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") representation of the box.

Parameters:
    

**frame_size** â the `(width, height)` of the video frames

Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

classmethod from_detection(_frame_number_ , _detection_ , _frame_size_)#
    

Creates a `CVATVideoBox` from a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").

Parameters:
    

  * **frame_number** â the frame number

  * **detection** â a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * **frame_size** â the `(width, height)` of the video frames



Returns:
    

a `CVATVideoBox`

classmethod from_box_dict(_label_ , _d_)#
    

Creates a `CVATVideoBox` from a `<box>` tag of a CVAT video annotation XML file.

Parameters:
    

  * **label** â the object label

  * **d** â a dict representation of a `<box>` tag



Returns:
    

a `CVATVideoBox`

class fiftyone.utils.cvat.CVATVideoPolygon(_frame_ , _label_ , _points_ , _outside =None_, _occluded =None_, _keyframe =None_, _attributes =None_)#
    

Bases: `CVATVideoAnno`, `HasCVATPoints`

A polygon in CVAT video format.

Parameters:
    

  * **frame** â the 0-based frame number

  * **label** â the polygon label string

  * **points** â a list of `(x, y)` pixel coordinates defining the vertices of the polygon

  * **outside** (_None_) â whether the polygon is outside (invisible)

  * **occluded** (_None_) â whether the polygon is occluded

  * **keyframe** (_None_) â whether the frame is a keyframe

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_polyline`(frame_size) | Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polygon.  
---|---  
`from_polyline`(frame_number,Â polyline,Â frame_size) | Creates a `CVATVideoPolygon` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").  
`from_polygon_dict`(label,Â d) | Creates a `CVATVideoPolygon` from a `<polygon>` tag of a CVAT video annotation XML file.  
  
**Attributes:**

`points_str` |   
---|---  
  
to_polyline(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polygon.

Parameters:
    

**frame_size** â the `(width, height)` of the video frames

Returns:
    

a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

classmethod from_polyline(_frame_number_ , _polyline_ , _frame_size_)#
    

Creates a `CVATVideoPolygon` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").

Parameters:
    

  * **frame_number** â the frame number

  * **polyline** â a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * **frame_size** â the `(width, height)` of the video frames



Returns:
    

a `CVATVideoPolygon`

classmethod from_polygon_dict(_label_ , _d_)#
    

Creates a `CVATVideoPolygon` from a `<polygon>` tag of a CVAT video annotation XML file.

Parameters:
    

  * **label** â the object label

  * **d** â a dict representation of a `<polygon>` tag



Returns:
    

a `CVATVideoPolygon`

property points_str#
    

class fiftyone.utils.cvat.CVATVideoPolyline(_frame_ , _label_ , _points_ , _outside =None_, _occluded =None_, _keyframe =None_, _attributes =None_)#
    

Bases: `CVATVideoAnno`, `HasCVATPoints`

A polyline in CVAT video format.

Parameters:
    

  * **frame** â the 0-based frame number

  * **label** â the polyline label string

  * **points** â a list of `(x, y)` pixel coordinates defining the vertices of the polyline

  * **outside** (_None_) â whether the polyline is outside (invisible)

  * **occluded** (_None_) â whether the polyline is occluded

  * **keyframe** (_None_) â whether the frame is a keyframe

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_polyline`(frame_size) | Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polyline.  
---|---  
`from_polyline`(frame_number,Â polyline,Â frame_size) | Creates a `CVATVideoPolyline` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").  
`from_polyline_dict`(label,Â d) | Creates a `CVATVideoPolyline` from a `<polyline>` tag of a CVAT video annotation XML file.  
  
**Attributes:**

`points_str` |   
---|---  
  
to_polyline(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") representation of the polyline.

Parameters:
    

**frame_size** â the `(width, height)` of the video frames

Returns:
    

a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

classmethod from_polyline(_frame_number_ , _polyline_ , _frame_size_)#
    

Creates a `CVATVideoPolyline` from a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").

Parameters:
    

  * **frame_number** â the frame number

  * **polyline** â a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * **frame_size** â the `(width, height)` of the video frames



Returns:
    

a `CVATVideoPolyline`

classmethod from_polyline_dict(_label_ , _d_)#
    

Creates a `CVATVideoPolyline` from a `<polyline>` tag of a CVAT video annotation XML file.

Parameters:
    

  * **label** â the object label

  * **d** â a dict representation of a `<polyline>` tag



Returns:
    

a `CVATVideoPolyline`

property points_str#
    

class fiftyone.utils.cvat.CVATVideoPoints(_frame_ , _label_ , _points_ , _outside =None_, _occluded =None_, _keyframe =None_, _attributes =None_)#
    

Bases: `CVATVideoAnno`, `HasCVATPoints`

A set of keypoints in CVAT video format.

Parameters:
    

  * **frame** â the 0-based frame number

  * **label** â the keypoints label string

  * **points** â a list of `(x, y)` pixel coordinates defining the keypoints

  * **outside** (_None_) â whether the keypoints is outside (invisible)

  * **occluded** (_None_) â whether the keypoints are occluded

  * **keyframe** (_None_) â whether the frame is a keyframe

  * **attributes** (_None_) â a list of `CVATAttribute` instances




**Methods:**

`to_keypoint`(frame_size) | Returns a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") representation of the points.  
---|---  
`from_keypoint`(frame_number,Â keypoint,Â frame_size) | Creates a `CVATVideoPoints` from a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").  
`from_points_dict`(label,Â d) | Creates a `CVATVideoPoints` from a `<points>` tag of a CVAT video annotation XML file.  
  
**Attributes:**

`points_str` |   
---|---  
  
to_keypoint(_frame_size_)#
    

Returns a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") representation of the points.

Parameters:
    

**frame_size** â the `(width, height)` of the video frames

Returns:
    

a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

classmethod from_keypoint(_frame_number_ , _keypoint_ , _frame_size_)#
    

Creates a `CVATVideoPoints` from a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").

Parameters:
    

  * **frame_number** â the frame number

  * **keypoint** â a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

  * **frame_size** â the `(width, height)` of the video frames



Returns:
    

a `CVATVideoPoints`

classmethod from_points_dict(_label_ , _d_)#
    

Creates a `CVATVideoPoints` from a `<points>` tag of a CVAT video annotation XML file.

Parameters:
    

  * **label** â the object label

  * **d** â a dict representation of a `<points>` tag



Returns:
    

a `CVATVideoPoints`

property points_str#
    

class fiftyone.utils.cvat.CVATAttribute(_name_ , _value_)#
    

Bases: `object`

An attribute in CVAT image format.

Parameters:
    

  * **name** â the attribute name

  * **value** â the attribute value




**Methods:**

`to_eta_attribute`() | Returns an `eta.core.data.Attribute` representation of the attribute.  
---|---  
`to_attribute`() | Returns a [`fiftyone.core.labels.Attribute`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Attribute "fiftyone.core.labels.Attribute") representation of the attribute.  
  
to_eta_attribute()#
    

Returns an `eta.core.data.Attribute` representation of the attribute.

Returns:
    

an `eta.core.data.Attribute`

to_attribute()#
    

Returns a [`fiftyone.core.labels.Attribute`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Attribute "fiftyone.core.labels.Attribute") representation of the attribute. :returns: a [`fiftyone.core.labels.Attribute`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Attribute "fiftyone.core.labels.Attribute")

class fiftyone.utils.cvat.CVATImageAnnotationWriter#
    

Bases: `object`

Class for writing annotations in CVAT image format.

See [this page](user_guide__export_datasets.md#cvatimagedataset-export) for format details.

**Methods:**

`write`(cvat_task_labels,Â cvat_images,Â xml_path) | Writes the annotations to disk.  
---|---  
  
write(_cvat_task_labels_ , _cvat_images_ , _xml_path_ , _id =None_, _name =None_)#
    

Writes the annotations to disk.

Parameters:
    

  * **cvat_task_labels** â a `CVATTaskLabels` instance

  * **cvat_images** â a list of `CVATImage` instances

  * **xml_path** â the path to write the annotations XML file

  * **id** (_None_) â an ID for the task

  * **name** (_None_) â a name for the task




class fiftyone.utils.cvat.CVATVideoAnnotationWriter#
    

Bases: `object`

Class for writing annotations in CVAT video format.

See [this page](user_guide__export_datasets.md#cvatvideodataset-export) for format details.

**Methods:**

`write`(cvat_task_labels,Â cvat_tracks,Â ...[,Â ...]) | Writes the annotations to disk.  
---|---  
  
write(_cvat_task_labels_ , _cvat_tracks_ , _metadata_ , _xml_path_ , _id =None_, _name =None_)#
    

Writes the annotations to disk.

Parameters:
    

  * **cvat_task_labels** â a `CVATTaskLabels` instance

  * **cvat_tracks** â a list of `CVATTrack` instances

  * **metadata** â the [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the video

  * **xml_path** â the path to write the annotations XML file

  * **id** (_None_) â an ID for the task

  * **name** (_None_) â a name for the task




class fiftyone.utils.cvat.CVATBackendConfig(_name_ , _label_schema_ , _media_field ='filepath'_, _url =None_, _username =None_, _email =None_, _password =None_, _headers =None_, _task_size =None_, _segment_size =None_, _image_quality =75_, _use_cache =True_, _use_zip_chunks =True_, _chunk_size =None_, _task_assignee =None_, _job_assignees =None_, _job_reviewers =None_, _project_name =None_, _project_id =None_, _task_name =None_, _occluded_attr =None_, _group_id_attr =None_, _issue_tracker =None_, _organization =None_, _frame_start =None_, _frame_stop =None_, _frame_step =None_, _coerce_text_attrs =True_, _** kwargs_)#
    

Bases: [`AnnotationBackendConfig`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackendConfig "fiftyone.utils.annotations.AnnotationBackendConfig")

Class for configuring `CVATBackend` instances.

Parameters:
    

  * **name** â the name of the backend

  * **label_schema** â a dictionary containing the description of label fields, classes and attribute to annotate

  * **media_field** (_"filepath"_) â string field name containing the paths to media files on disk to upload

  * **url** (_None_) â the url of the CVAT server

  * **username** (_None_) â the CVAT username

  * **email** (_None_) â the CVAT email

  * **password** (_None_) â the CVAT password

  * **headers** (_None_) â an optional dict of headers to add to all CVAT API requests

  * **task_size** (_None_) â an optional maximum number of images to upload per task. Videos are always uploaded one per task

  * **segment_size** (_None_) â maximum number of images per job. Not applicable to videos

  * **image_quality** (_75_) â an int in `[0, 100]` determining the image quality to upload to CVAT

  * **use_cache** (_True_) â whether to use a cache when uploading data. Using a cache reduces task creation time as data will be processed on-the-fly and stored in the cache when requested

  * **use_zip_chunks** (_True_) â when annotating videos, whether to upload video frames in smaller chunks. Setting this option to `False` may result in reduced video quality in CVAT due to size limitations on ZIP files that can be uploaded to CVAT

  * **chunk_size** (_None_) â the number of frames to upload per ZIP chunk

  * **task_assignee** (_None_) â the username(s) to which the task(s) were assigned. This argument can be a list of usernames when annotating videos as each video is uploaded to a separate task

  * **job_assignees** (_None_) â a list of usernames to which jobs were assigned

  * **job_reviewers** (_None_) â a list of usernames to which job reviews were assigned. Only available in CVAT v1 servers

  * **project_name** (_None_) â an optional project name to which to upload the created CVAT task. If a project with this name is found, it will be used, otherwise a new project with this name is created. By default, no project is used

  * **project_id** (_None_) â an optional ID of an existing CVAT project to which to upload the annotation tasks. By default, no project is used

  * **task_name** (_None_) â an optional task name to use for the created CVAT task

  * **occluded_attr** (_None_) â an optional attribute name containing existing occluded values and/or in which to store downloaded occluded values for all objects in the annotation run

  * **group_id_attr** (_None_) â an optional attribute name containing existing group ids and/or in which to store downloaded group ids for all objects in the annotation run

  * **issue_tracker** (_None_) â URL(s) of an issue tracker to link to the created task(s). This argument can be a list of URLs when annotating videos or when using `task_size` and generating multiple tasks

  * **organization** (_None_) â the name of the organization to use when sending requests to CVAT

  * **frame_start** (_None_) â 

nonnegative integer(s) defining the first frame of videos to upload when creating video tasks. Supported values are:

>     * `integer`: the first frame to upload for each video
> 
>     * `list`: a list of first frame integers corresponding to videos in the given samples
> 
>     * `dict`: a dictionary mapping sample filepaths to first frame integers to use for the corresponding videos

  * **frame_stop** (_None_) â 

nonnegative integer(s) defining the last frame of videos to upload when creating video tasks. Supported values are:

>     * `integer`: the last frame to upload for each video
> 
>     * `list`: a list of last frame integers corresponding to videos in the given samples
> 
>     * `dict`: a dictionary mapping sample filepaths to last frame integers to use for the corresponding videos

  * **frame_step** (_None_) â 

positive integer(s) defining which frames to sample when creating video tasks. Supported values are:

>     * `integer`: the frame step to apply to each video task
> 
>     * `list`: a list of frame step integers corresponding to videos in the given samples
> 
>     * `dict`: a dictionary mapping sample filepaths to frame step integers to use for the corresponding videos

Note that this argument cannot be provided when uploading existing tracks

  * **coerce_text_attrs** (_True_) â whether to coerce CVAT text attributes to numeric types during annotation download. Set to False to preserve text attribute values as strings




**Attributes:**

`username` |   
---|---  
`email` |   
`password` |   
`headers` |   
`cls` | The fully-qualified name of this `BaseRunConfig` class.  
`method` | The name of the annotation backend.  
`run_cls` | The `BaseRun` class associated with this config.  
`type` | The type of run.  
  
**Methods:**

`load_credentials`([url,Â username,Â password,Â ...]) | Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.  
---|---  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_config_cls`(type) | Returns the config class for the given run type.  
`build`() | Builds the `BaseRun` instance associated with this config.  
`builder`() | Returns a ConfigBuilder instance for this class.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`default`() | Returns the default config instance.  
`from_dict`(d) | Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_kwargs`(**kwargs) | Constructs a Config object from keyword arguments.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`load_default`() | Loads the default config instance from file.  
`parse_array`(d,Â key[,Â default]) | Parses a raw array attribute.  
`parse_bool`(d,Â key[,Â default]) | Parses a boolean value.  
`parse_categorical`(d,Â key,Â choices[,Â default]) | Parses a categorical JSON field, which must take a value from among the given choices.  
`parse_dict`(d,Â key[,Â default]) | Parses a dictionary attribute.  
`parse_int`(d,Â key[,Â default]) | Parses an integer attribute.  
`parse_mutually_exclusive_fields`(fields) | Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.  
`parse_number`(d,Â key[,Â default]) | Parses a number attribute.  
`parse_object`(d,Â key,Â cls[,Â default]) | Parses an object attribute.  
`parse_object_array`(d,Â key,Â cls[,Â default]) | Parses an array of objects.  
`parse_object_dict`(d,Â key,Â cls[,Â default]) | Parses a dictionary whose values are objects.  
`parse_path`(d,Â key[,Â default]) | Parses a path attribute.  
`parse_raw`(d,Â key[,Â default]) | Parses a raw (arbitrary) JSON field.  
`parse_string`(d,Â key[,Â default]) | Parses a string attribute.  
`serialize`(*args,Â **kwargs) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`validate_all_or_nothing_fields`(fields) | Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
property username#
    

property email#
    

property password#
    

property headers#
    

load_credentials(_url =None_, _username =None_, _password =None_, _email =None_, _headers =None_)#
    

Loads any necessary credentials from the given keyword arguments or the relevant FiftyOne config.

Parameters:
    

****kwargs** â subclass-specific credentials

attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

static base_config_cls(_type_)#
    

Returns the config class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunConfig` subclass

build()#
    

Builds the `BaseRun` instance associated with this config.

Returns:
    

a `BaseRun` instance

classmethod builder()#
    

Returns a ConfigBuilder instance for this class.

property cls#
    

The fully-qualified name of this `BaseRunConfig` class.

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod default()#
    

Returns the default config instance.

By default, this method instantiates the class from an empty dictionary, which will only succeed if all attributes are optional. Otherwise, subclasses should override this method to provide the desired default configuration.

classmethod from_dict(_d_)#
    

Constructs a `BaseRunConfig` from a serialized JSON dict representation of it.

Parameters:
    

**d** â a JSON dict

Returns:
    

a `BaseRunConfig`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_kwargs(_** kwargs_)#
    

Constructs a Config object from keyword arguments.

Parameters:
    

****kwargs** â keyword arguments that define the fields expected by cls

Returns:
    

an instance of cls

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

classmethod load_default()#
    

Loads the default config instance from file.

Subclasses must implement this method if they intend to support default instances.

property method#
    

The name of the annotation backend.

static parse_array(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw array attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default list to return if key is not present



Returns:
    

a list of raw (untouched) values

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_bool(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a boolean value.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default bool to return if key is not present



Returns:
    

True/False

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_categorical(_d_ , _key_ , _choices_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a categorical JSON field, which must take a value from among the given choices.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **choices** â either an iterable of possible values or an enum-like class whose attributes define the possible values

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field, which is equal to a value from choices

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the key was present in the dictionary but its value was not an allowed choice, or if no default value was provided and the key was not found in the dictionary

static parse_dict(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default dict to return if key is not present



Returns:
    

a dictionary

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_int(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an integer attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default integer value to return if key is not present



Returns:
    

an int

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_mutually_exclusive_fields(_fields_)#
    

Parses a mutually exclusive dictionary of pre-parsed fields, which must contain exactly one field with a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Returns:
    

the (field, value) that was set

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if zero or more than one truthy value was found

static parse_number(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a number attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default numeric value to return if key is not present



Returns:
    

a number (e.g. int, float)

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an object attribute.

The value of d[key] can be either an instance of cls or a serialized dict from an instance of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of d[key]

  * **default** â a default cls instance to return if key is not present



Returns:
    

an instance of cls

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_array(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses an array of objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the elements of list d[key]

  * **default** â the default list to return if key is not present



Returns:
    

a list of cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_object_dict(_d_ , _key_ , _cls_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a dictionary whose values are objects.

The values in d[key] can be either instances of cls or serialized dicts from instances of cls.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **cls** â the class of the values of dictionary d[key]

  * **default** â the default dict of cls instances to return if key is not present



Returns:
    

a dictionary whose values are cls instances

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_path(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a path attribute.

The path is converted to an absolute path if necessary via `os.path.abspath(os.path.expanduser(value))`.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a path string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

static parse_raw(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a raw (arbitrary) JSON field.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default value to return if key is not present



Returns:
    

the raw (untouched) value of the given field

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if no default value was provided and the key was not found in the dictionary

static parse_string(_d_ , _key_ , _default =<eta.core.config.NoDefault object>_)#
    

Parses a string attribute.

Parameters:
    

  * **d** â a JSON dictionary

  * **key** â the key to parse

  * **default** â a default string to return if key is not present



Returns:
    

a string

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if the field value was the wrong type or no default value was provided and the key was not found in the dictionary

property run_cls#
    

The `BaseRun` class associated with this config.

serialize(_* args_, _** kwargs_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

property type#
    

The type of run.

static validate_all_or_nothing_fields(_fields_)#
    

Validates a dictionary of pre-parsed fields checking that either all or none of the fields have a truthy value.

Parameters:
    

**fields** â a dictionary of pre-parsed fields

Raises:
    

[**ConfigError**](api__fiftyone.zoo.md#fiftyone.zoo.ConfigError "fiftyone.zoo.ConfigError") â if some values are truth and some are not

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.cvat.CVATBackend(_* args_, _** kwargs_)#
    

Bases: [`AnnotationBackend`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationBackend "fiftyone.utils.annotations.AnnotationBackend")

Class for interacting with the CVAT annotation backend.

**Attributes:**

`supported_media_types` | The list of media types that this backend supports.  
---|---  
`supported_label_types` | The list of label types supported by the backend.  
`supported_scalar_types` | The list of scalar field types supported by the backend.  
`supported_attr_types` | The list of attribute types supported by the backend.  
`supports_clips_views` | Whether this backend supports annotating clips views.  
`supports_keyframes` | Whether this backend supports uploading only keyframes when editing existing video track annotations.  
`supports_video_sample_fields` | Whether this backend supports annotating video labels at a sample-level.  
`requires_label_schema` | Whether this backend requires a pre-defined label schema for its annotation runs.  
  
**Methods:**

`recommend_attr_tool`(name,Â value) | Recommends an attribute tool for an attribute with the given name and value.  
---|---  
`requires_attr_values`(attr_type) | Determines whether the list of possible values are required for attributes of the given type.  
`upload_annotations`(samples,Â anno_key[,Â ...]) | Uploads the samples and relevant existing labels from the label schema to the annotation backend.  
`download_annotations`(results) | Downloads the annotations from the annotation backend for the given results.  
`cleanup`(samples,Â key) | Cleans up the results of the run with the given key from the collection.  
`connect_to_api`() | Returns an API instance connected to the annotation backend.  
`delete_run`(samples,Â key[,Â cleanup]) | Deletes the results associated with the given run key from the collection.  
`delete_runs`(samples[,Â cleanup]) | Deletes all runs from the collection.  
`ensure_requirements`() | Ensures that any necessary packages to execute this run are installed.  
`ensure_usage_requirements`() | Ensures that any necessary packages to use existing results for this run are installed.  
`from_config`(config) | Instantiates a Configurable class from a <cls>Config instance.  
`from_dict`(d) | Instantiates a Configurable class from a <cls>Config dict.  
`from_json`(json_path) | Instantiates a Configurable class from a <cls>Config JSON file.  
`from_kwargs`(**kwargs) | Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.  
`get_fields`(samples,Â anno_key) | Gets the fields that were involved in the given run.  
`get_run_info`(samples,Â key) | Gets the `BaseRunInfo` for the given key on the collection.  
`has_cached_run_results`(samples,Â key) | Determines whether `BaseRunResults` for the given key are cached on the collection.  
`list_runs`(samples[,Â type,Â method]) | Returns the list of run keys on the given collection.  
`load_run_results`(samples,Â key[,Â cache,Â ...]) | Loads the `BaseRunResults` for the given key on the collection.  
`load_run_view`(samples,Â key[,Â select_fields]) | Loads the view on which the specified run was performed.  
`parse`(class_name[,Â module_name]) | Parses a Configurable subclass name string.  
`register_run`(samples,Â key[,Â overwrite,Â cleanup]) | Registers a run of this method under the given key on the given collection.  
`rename`(samples,Â key,Â new_key) | Performs any necessary operations required to rename this run's key.  
`run_info_cls`() | The `BaseRunInfo` class associated with this class.  
`save_run_info`(samples,Â run_info[,Â ...]) | Saves the run information on the collection.  
`save_run_results`(samples,Â key,Â run_results) | Saves the run results on the collection.  
`update_run_config`(samples,Â key,Â config) | Updates the `BaseRunConfig` for the given run on the collection.  
`update_run_key`(samples,Â key,Â new_key) | Replaces the key for the given run with a new key.  
`use_api`(api) | Registers an API instance to use for subsequent operations.  
`validate`(config) | Validates that the given config is an instance of <cls>Config.  
`validate_run`(samples,Â key[,Â overwrite]) | Validates that the collection can accept this run.  
  
property supported_media_types#
    

The list of media types that this backend supports.

For example, CVAT supports `["image", "video"]`.

property supported_label_types#
    

The list of label types supported by the backend.

Backends may support any subset of the following label types:

  * `"classification"`

  * `"classifications"`

  * `"detection"`

  * `"detections"`

  * `"instance"`

  * `"instances"`

  * `"polyline"`

  * `"polylines"`

  * `"polygon"`

  * `"polygons"`

  * `"keypoint"`

  * `"keypoints"`

  * `"segmentation"`

  * `"scalar"`




property supported_scalar_types#
    

The list of scalar field types supported by the backend.

For example, CVAT supports the following types:

  * [`fiftyone.core.fields.IntField`](api__fiftyone.core.fields.md#fiftyone.core.fields.IntField "fiftyone.core.fields.IntField")

  * [`fiftyone.core.fields.FloatField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FloatField "fiftyone.core.fields.FloatField")

  * [`fiftyone.core.fields.StringField`](api__fiftyone.core.fields.md#fiftyone.core.fields.StringField "fiftyone.core.fields.StringField")

  * [`fiftyone.core.fields.BooleanField`](api__fiftyone.core.fields.md#fiftyone.core.fields.BooleanField "fiftyone.core.fields.BooleanField")




property supported_attr_types#
    

The list of attribute types supported by the backend.

This list defines the valid string values for the `type` field of an attributes dict of the label schema provided to the backend.

For example, CVAT supports `["text", "select", "radio", "checkbox"]`.

property supports_clips_views#
    

Whether this backend supports annotating clips views.

property supports_keyframes#
    

Whether this backend supports uploading only keyframes when editing existing video track annotations.

property supports_video_sample_fields#
    

Whether this backend supports annotating video labels at a sample-level.

property requires_label_schema#
    

Whether this backend requires a pre-defined label schema for its annotation runs.

recommend_attr_tool(_name_ , _value_)#
    

Recommends an attribute tool for an attribute with the given name and value.

For example, a backend may recommend a tool as follows for a boolean value:
    
    
    {
        "type": "radio",
        "values": [False, True],
    }
    

or a tool as follows for a generic value:
    
    
    {"type": "text"}
    

Parameters:
    

  * **name** â the name of the attribute

  * **value** â the attribute value, which may be `None`



Returns:
    

an attribute type dict

requires_attr_values(_attr_type_)#
    

Determines whether the list of possible values are required for attributes of the given type.

Parameters:
    

**attr_type** â the attribute type string

Returns:
    

True/False

upload_annotations(_samples_ , _anno_key_ , _launch_editor =False_)#
    

Uploads the samples and relevant existing labels from the label schema to the annotation backend.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **anno_key** â the annotation key

  * **launch_editor** (_False_) â whether to launch the annotation backendâs editor after uploading the samples



Returns:
    

an `AnnotationResults`

download_annotations(_results_)#
    

Downloads the annotations from the annotation backend for the given results.

The returned labels should be represented as either scalar values or [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances.

For image datasets, the return dictionary should have the following nested structure:
    
    
    # Scalar fields
    results[label_type][sample_id] = scalar
    
    # Label fields
    results[label_type][sample_id][label_id] = label
    

For video datasets, the returned labels dictionary should have the following nested structure:
    
    
    # Scalar fields
    results[label_type][sample_id][frame_id] = scalar
    
    # Label fields
    results[label_type][sample_id][frame_id][label_id] = label
    

The valid values for `label_type` are:

  * âclassificationsâ: single or multilabel classifications

  * âdetectionsâ: detections or instance segmentations

  * âpolylinesâ: polygons or polylines

  * âsegmentationâ: semantic segmentations

  * âscalarâ: scalar values




Parameters:
    

**results** â an `AnnotationResults`

Returns:
    

the labels results dict

cleanup(_samples_ , _key_)#
    

Cleans up the results of the run with the given key from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key




connect_to_api()#
    

Returns an API instance connected to the annotation backend.

Existing API instances are reused, if available.

Some annotation backends may not expose this functionality.

Returns:
    

an `AnnotationAPI`, or `None` if the backend does not expose an API

classmethod delete_run(_samples_ , _key_ , _cleanup =True_)#
    

Deletes the results associated with the given run key from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **cleanup** (_True_) â whether to execute the runâs `BaseRun.cleanup()` method




classmethod delete_runs(_samples_ , _cleanup =True_)#
    

Deletes all runs from the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **cleanup** (_True_) â whether to execute the runâs `BaseRun.cleanup()` methods




ensure_requirements()#
    

Ensures that any necessary packages to execute this run are installed.

Runs should respect `fiftyone.config.requirement_error_level` when handling errors.

ensure_usage_requirements()#
    

Ensures that any necessary packages to use existing results for this run are installed.

Runs should respect `fiftyone.config.requirement_error_level` when handling errors.

classmethod from_config(_config_)#
    

Instantiates a Configurable class from a <cls>Config instance.

classmethod from_dict(_d_)#
    

Instantiates a Configurable class from a <cls>Config dict.

Parameters:
    

**d** â a dict to construct a <cls>Config

Returns:
    

an instance of cls

classmethod from_json(_json_path_)#
    

Instantiates a Configurable class from a <cls>Config JSON file.

Parameters:
    

**json_path** â path to a JSON file for type <cls>Config

Returns:
    

an instance of cls

classmethod from_kwargs(_** kwargs_)#
    

Instantiates a Configurable class from keyword arguments defining the attributes of a <cls>Config.

Parameters:
    

****kwargs** â keyword arguments that define the fields of a <cls>Config dict

Returns:
    

an instance of cls

get_fields(_samples_ , _anno_key_)#
    

Gets the fields that were involved in the given run.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key



Returns:
    

a list of fields

classmethod get_run_info(_samples_ , _key_)#
    

Gets the `BaseRunInfo` for the given key on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key



Returns:
    

a `BaseRunInfo`

classmethod has_cached_run_results(_samples_ , _key_)#
    

Determines whether `BaseRunResults` for the given key are cached on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key



Returns:
    

True/False

classmethod list_runs(_samples_ , _type =None_, _method =None_, _** kwargs_)#
    

Returns the list of run keys on the given collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **type** (_None_) â 

a specific run type to match, which can be:

    * a string [`fiftyone.core.runs.BaseRunConfig.type`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRunConfig.type "fiftyone.core.runs.BaseRunConfig.type")

    * a [`fiftyone.core.runs.BaseRun`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRun "fiftyone.core.runs.BaseRun") class or its fully-qualified class name string

  * **method** (_None_) â a specific [`fiftyone.core.runs.BaseRunConfig.method`](api__fiftyone.core.runs.md#fiftyone.core.runs.BaseRunConfig.method "fiftyone.core.runs.BaseRunConfig.method") string to match

  * ****kwargs** â optional config parameters to match



Returns:
    

a list of run keys

classmethod load_run_results(_samples_ , _key_ , _cache =True_, _load_view =True_, _** kwargs_)#
    

Loads the `BaseRunResults` for the given key on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **cache** (_True_) â whether to cache the results on the collection

  * **load_view** (_True_) â whether to load the run view in the results (True) or the full dataset (False)

  * ****kwargs** â keyword arguments for the runâs `BaseRunConfig.load_credentials()` method



Returns:
    

a `BaseRunResults`, or None if the run did not save results

classmethod load_run_view(_samples_ , _key_ , _select_fields =False_)#
    

Loads the view on which the specified run was performed.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **select_fields** (_False_) â whether to exclude fields involved in other runs of the same type



Returns:
    

a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

static parse(_class_name_ , _module_name =None_)#
    

Parses a Configurable subclass name string.

Assumes both the Configurable class and the Config class are defined in the same module. The module containing the classes will be loaded if necessary.

Parameters:
    

  * **class_name** â a string containing the name of the Configurable class, e.g. âClassNameâ, or a fully-qualified class name, e.g. âeta.core.config.ClassNameâ

  * **module_name** â a string containing the fully-qualified module name, e.g. âeta.core.configâ, or None if class_name includes the module name. Set module_name = __name__ to load a class from the calling module



Returns:
    

the Configurable class config_cls: the Config class associated with cls

Return type:
    

[cls](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.cls "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityConfig.cls")

register_run(_samples_ , _key_ , _overwrite =True_, _cleanup =True_)#
    

Registers a run of this method under the given key on the given collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **overwrite** (_True_) â whether to allow overwriting an existing run of the same type

  * **cleanup** (_True_) â whether to execute an existing runâs `BaseRun.cleanup()` method when overwriting it




rename(_samples_ , _key_ , _new_key_)#
    

Performs any necessary operations required to rename this runâs key.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **new_key** â a new run key




classmethod run_info_cls()#
    

The `BaseRunInfo` class associated with this class.

classmethod save_run_info(_samples_ , _run_info_ , _overwrite =True_, _cleanup =True_)#
    

Saves the run information on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **run_info** â a `BaseRunInfo`

  * **overwrite** (_True_) â whether to overwrite an existing run with the same key

  * **cleanup** (_True_) â whether to execute an existing runâs `BaseRun.cleanup()` method when overwriting it




classmethod save_run_results(_samples_ , _key_ , _run_results_ , _overwrite =True_, _cache =True_)#
    

Saves the run results on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **run_results** â a `BaseRunResults`, or None

  * **overwrite** (_True_) â whether to overwrite an existing result with the same key

  * **cache** (_True_) â whether to cache the results on the collection




classmethod update_run_config(_samples_ , _key_ , _config_)#
    

Updates the `BaseRunConfig` for the given run on the collection.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **config** â a `BaseRunConfig`




classmethod update_run_key(_samples_ , _key_ , _new_key_)#
    

Replaces the key for the given run with a new key.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **new_key** â a new run key




use_api(_api_)#
    

Registers an API instance to use for subsequent operations.

Parameters:
    

**api** â an `AnnotationAPI`

classmethod validate(_config_)#
    

Validates that the given config is an instance of <cls>Config.

Raises:
    

**ConfigurableError** â if config is not an instance of <cls>Config

validate_run(_samples_ , _key_ , _overwrite =True_)#
    

Validates that the collection can accept this run.

The run may be invalid if, for example, a run of a different type has already been run under the same key and thus overwriting it would cause ambiguity on how to cleanup the results.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **key** â a run key

  * **overwrite** (_True_) â whether to allow overwriting an existing run of the same type



Raises:
    

**ValueError** â if the run is invalid

class fiftyone.utils.cvat.CVATAnnotationResults(_samples_ , _config_ , _anno_key_ , _id_map_ , _server_id_map_ , _project_ids_ , _task_ids_ , _job_ids_ , _frame_id_map_ , _labels_task_map_ , _backend =None_)#
    

Bases: [`AnnotationResults`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationResults "fiftyone.utils.annotations.AnnotationResults")

Class that stores all relevant information needed to monitor the progress of an annotation run sent to CVAT and download the results.

**Methods:**

`launch_editor`() | Launches the CVAT editor and loads the first task for this annotation run.  
---|---  
`get_status`() | Gets the status of the assigned tasks and jobs.  
`print_status`() | Prints the status of the assigned tasks and jobs.  
`delete_tasks`(task_ids) | Deletes the given tasks from both the CVAT server and this run.  
`cleanup`() | Deletes all tasks and created projects associated with this run.  
`attributes`() | Returns the list of class attributes that will be serialized by `serialize()`.  
`base_results_cls`(type) | Returns the results class for the given run type.  
`connect_to_api`() | Returns an API instance connected to the annotation backend.  
`copy`() | Returns a deep copy of the object.  
`custom_attributes`([dynamic,Â private]) | Returns a customizable list of class attributes.  
`from_dict`(d,Â samples,Â config,Â key) | Builds a `BaseRunResults` from a JSON dict representation of it.  
`from_json`(path,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON file.  
`from_str`(s,Â *args,Â **kwargs) | Constructs a Serializable object from a JSON string.  
`get_class_name`() | Returns the fully-qualified class name string of this object.  
`save`() | Saves the results to the database.  
`save_config`() | Saves these results config to the database.  
`serialize`([reflective]) | Serializes the object into a dictionary.  
`to_str`([pretty_print]) | Returns a string representation of this object.  
`use_api`(api) | Registers an API instance to use for subsequent operations.  
`write_json`(path[,Â pretty_print]) | Serializes the object and writes it to disk.  
  
**Attributes:**

`backend` | The `BaseRun` for these results.  
---|---  
`cls` | The fully-qualified name of this `BaseRunResults` class.  
`config` | The `BaseRunConfig` for these results.  
`key` | The run key for these results.  
`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.  
  
launch_editor()#
    

Launches the CVAT editor and loads the first task for this annotation run.

get_status()#
    

Gets the status of the assigned tasks and jobs.

Returns:
    

a dict of status information

print_status()#
    

Prints the status of the assigned tasks and jobs.

delete_tasks(_task_ids_)#
    

Deletes the given tasks from both the CVAT server and this run.

Parameters:
    

**task_ids** â an iterable of task IDs

cleanup()#
    

Deletes all tasks and created projects associated with this run.

attributes()#
    

Returns the list of class attributes that will be serialized by `serialize()`.

Returns:
    

a list of attributes

property backend#
    

The `BaseRun` for these results.

static base_results_cls(_type_)#
    

Returns the results class for the given run type.

Parameters:
    

**type** â a `BaseRunConfig.type`

Returns:
    

a `BaseRunResults` subclass

property cls#
    

The fully-qualified name of this `BaseRunResults` class.

property config#
    

The `BaseRunConfig` for these results.

connect_to_api()#
    

Returns an API instance connected to the annotation backend.

Existing API instances are reused, if available.

Some annotation backends may not expose this functionality.

Returns:
    

an `AnnotationAPI`, or `None` if the backend does not expose an API

copy()#
    

Returns a deep copy of the object.

Returns:
    

a Serializable instance

custom_attributes(_dynamic =False_, _private =False_)#
    

Returns a customizable list of class attributes.

By default, all attributes in vars(self) are returned, minus private attributes (those starting with â_â).

Parameters:
    

  * **dynamic** â whether to include dynamic properties, e.g., those defined by getter/setter methods or the @property decorator. By default, this is False

  * **private** â whether to include private properties, i.e., those starting with â_â. By default, this is False



Returns:
    

a list of class attributes

classmethod from_dict(_d_ , _samples_ , _config_ , _key_)#
    

Builds a `BaseRunResults` from a JSON dict representation of it.

Parameters:
    

  * **d** â a JSON dict

  * **samples** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for the run

  * **config** â the `BaseRunConfig` for the run

  * **key** â the run key



Returns:
    

a `BaseRunResults`

classmethod from_json(_path_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON file.

Subclasses may override this method, but, by default, this method simply reads the JSON and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **path** â the path to the JSON file on disk

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod from_str(_s_ , _* args_, _** kwargs_)#
    

Constructs a Serializable object from a JSON string.

Subclasses may override this method, but, by default, this method simply parses the string and calls from_dict(), which subclasses must implement.

Parameters:
    

  * **s** â a JSON string representation of a Serializable object

  * ***args** â optional positional arguments for self.from_dict()

  * ****kwargs** â optional keyword arguments for self.from_dict()



Returns:
    

an instance of the Serializable class

classmethod get_class_name()#
    

Returns the fully-qualified class name string of this object.

property key#
    

The run key for these results.

property samples#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") associated with these results.

save()#
    

Saves the results to the database.

save_config()#
    

Saves these results config to the database.

serialize(_reflective =False_)#
    

Serializes the object into a dictionary.

Serialization is applied recursively to all attributes in the object, including element-wise serialization of lists and dictionary values.

Parameters:
    

**reflective** â whether to include reflective attributes when serializing the object. By default, this is False

Returns:
    

a JSON dictionary representation of the object

to_str(_pretty_print =True_, _** kwargs_)#
    

Returns a string representation of this object.

Parameters:
    

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is True

  * ****kwargs** â optional keyword arguments for self.serialize()



Returns:
    

a string representation of the object

use_api(_api_)#
    

Registers an API instance to use for subsequent operations.

Parameters:
    

**api** â an `AnnotationAPI`

write_json(_path_ , _pretty_print =False_, _** kwargs_)#
    

Serializes the object and writes it to disk.

Parameters:
    

  * **path** â the output path

  * **pretty_print** â whether to render the JSON in human readable format with newlines and indentations. By default, this is False

  * ****kwargs** â optional keyword arguments for self.serialize()




class fiftyone.utils.cvat.CVATAnnotationAPI(_name_ , _url_ , _username =None_, _email =None_, _password =None_, _headers =None_, _organization =None_)#
    

Bases: [`AnnotationAPI`](api__fiftyone.utils.annotations.md#fiftyone.utils.annotations.AnnotationAPI "fiftyone.utils.annotations.AnnotationAPI")

A class to facilitate connection to and management of tasks in CVAT.

On initialization, this class constructs a session based on the provided server url and credentials.

This API provides methods to easily get, put, post, patch, and delete tasks and jobs through the formatted urls specified by the CVAT REST API.

Additionally, samples and label schemas can be uploaded and annotations downloaded through this class.

Parameters:
    

  * **name** â the name of the backend

  * **url** â url of the CVAT server

  * **username** (_None_) â the CVAT username

  * **email** (_None_) â the CVAT email

  * **password** (_None_) â the CVAT password

  * **headers** (_None_) â an optional dict of headers to add to all requests

  * **organization** (_None_) â the name of the organization to use when sending requests to CVAT




**Attributes:**

`server_version` |   
---|---  
`base_url` |   
`base_api_url` |   
`login_url` |   
`about_url` |   
`users_url` |   
`projects_url` |   
`tasks_url` |   
`assignee_key` |   
  
**Methods:**

`projects_page_url`(page_number) |   
---|---  
`project_url`(project_id) |   
`tasks_page_url`(page_number) |   
`task_url`(task_id) |   
`task_status_url`(task_id) |   
`task_data_url`(task_id) |   
`task_data_download_url`(task_id,Â frame_id[,Â ...]) |   
`task_data_meta_url`(task_id) |   
`task_annotation_url`(task_id) |   
`task_annotation_formatted_url`(task_id,Â ...) |   
`labels_url`(task_id) |   
`jobs_url`(task_id) |   
`job_url`(task_id,Â job_id) |   
`job_annotation_url`(job_id) |   
`taskless_job_url`(job_id) |   
`base_task_url`(task_id) |   
`base_job_url`(task_id,Â job_id) |   
`task_id_search_url`(task_id) |   
`user_search_url`(username) |   
`project_search_url`(project_name) |   
`project_id_search_url`(project_id) |   
`close`() | Closes the API session.  
`get`(url,Â **kwargs) | Sends a GET request to the given CVAT API URL.  
`patch`(url,Â **kwargs) | Sends a PATCH request to the given CVAT API URL.  
`post`(url,Â **kwargs) | Sends a POST request to the given CVAT API URL.  
`put`(url,Â **kwargs) | Sends a PUT request to the given CVAT API URL.  
`delete`(url,Â **kwargs) | Sends a DELETE request to the given CVAT API URL.  
`get_user_id`(username) | Retrieves the CVAT user ID for the given username.  
`get_project_id`(project_name) | Retrieves the CVAT project ID for the first instance of the given project name.  
`get_project_name`(project_id) | Retrieves the CVAT project name for the given project ID.  
`get_empty_projects`(project_ids) | Check all given project ids to determine if they are empty or if they contain at least one task.  
`create_project`(name[,Â schema]) | Creates a project on the CVAT server using the given label schema.  
`list_projects`() | Returns the list of project IDs.  
`project_exists`(project_id) | Checks if the given project exists.  
`delete_project`(project_id) | Deletes the given project from the CVAT server.  
`delete_projects`(project_ids[,Â progress]) | Deletes the given projects from the CVAT server.  
`get_project_tasks`(project_id) | Returns the IDs of the tasks in the given project.  
`create_task`(name[,Â schema,Â segment_size,Â ...]) | Creates a task on the CVAT server using the given label schema.  
`list_tasks`() | Returns the list of task IDs.  
`task_exists`(task_id) | Checks if the given task exists.  
`delete_task`(task_id) | Deletes the given task from the CVAT server.  
`delete_tasks`(task_ids[,Â progress]) | Deletes the given tasks from the CVAT server.  
`launch_editor`([url]) | Launches the CVAT editor in your default web browser.  
`upload_data`(task_id,Â paths[,Â image_quality,Â ...]) | Uploads a list of media to the task with the given ID.  
`upload_samples`(samples,Â anno_key,Â backend) | Uploads the given samples to CVAT according to the given backend's annotation and server configuration.  
`download_annotations`(results[,Â ...]) | Download the annotations from the CVAT server for the given results instance and parses them into the appropriate FiftyOne types.  
  
property server_version#
    

property base_url#
    

property base_api_url#
    

property login_url#
    

property about_url#
    

property users_url#
    

property projects_url#
    

projects_page_url(_page_number_)#
    

project_url(_project_id_)#
    

property tasks_url#
    

tasks_page_url(_page_number_)#
    

task_url(_task_id_)#
    

task_status_url(_task_id_)#
    

task_data_url(_task_id_)#
    

task_data_download_url(_task_id_ , _frame_id_ , _data_type ='frame'_, _quality ='original'_)#
    

task_data_meta_url(_task_id_)#
    

task_annotation_url(_task_id_)#
    

task_annotation_formatted_url(_task_id_ , _anno_filepath_ , _anno_format ='CVAT 1.1'_)#
    

labels_url(_task_id_)#
    

jobs_url(_task_id_)#
    

job_url(_task_id_ , _job_id_)#
    

job_annotation_url(_job_id_)#
    

taskless_job_url(_job_id_)#
    

base_task_url(_task_id_)#
    

base_job_url(_task_id_ , _job_id_)#
    

task_id_search_url(_task_id_)#
    

user_search_url(_username_)#
    

project_search_url(_project_name_)#
    

project_id_search_url(_project_id_)#
    

property assignee_key#
    

close()#
    

Closes the API session.

get(_url_ , _** kwargs_)#
    

Sends a GET request to the given CVAT API URL.

Parameters:
    

  * **url** â the url

  * ****kwargs** â additional request parameters



Returns:
    

the request response

patch(_url_ , _** kwargs_)#
    

Sends a PATCH request to the given CVAT API URL.

Parameters:
    

  * **url** â the url

  * ****kwargs** â additional request parameters



Returns:
    

the request response

post(_url_ , _** kwargs_)#
    

Sends a POST request to the given CVAT API URL.

Parameters:
    

  * **url** â the url

  * ****kwargs** â additional request parameters



Returns:
    

the request response

put(_url_ , _** kwargs_)#
    

Sends a PUT request to the given CVAT API URL.

Parameters:
    

  * **url** â the url

  * ****kwargs** â additional request parameters



Returns:
    

the request response

delete(_url_ , _** kwargs_)#
    

Sends a DELETE request to the given CVAT API URL.

Parameters:
    

  * **url** â the url to send the request to

  * ****kwargs** â additional request parameters



Returns:
    

the request response

get_user_id(_username_)#
    

Retrieves the CVAT user ID for the given username.

Parameters:
    

**username** â the username

Returns:
    

the user ID, or None if the user was not found

get_project_id(_project_name_)#
    

Retrieves the CVAT project ID for the first instance of the given project name.

Parameters:
    

**project_name** â the name of the project

Returns:
    

the project ID, or None if no project with the given name was found

get_project_name(_project_id_)#
    

Retrieves the CVAT project name for the given project ID.

Parameters:
    

**project_id** â the ID of the project

Returns:
    

the project name, or None if no project with the given ID was found

get_empty_projects(_project_ids_)#
    

Check all given project ids to determine if they are empty or if they contain at least one task.

Parameters:
    

**project_ids** â a list of project ids to check

Returns:
    

a list of empty project ids

create_project(_name_ , _schema =None_)#
    

Creates a project on the CVAT server using the given label schema.

Parameters:
    

  * **name** â a name for the project

  * **schema** (_None_) â the label schema to use for the created project



Returns:
    

the ID of the created project in CVAT

list_projects()#
    

Returns the list of project IDs.

Returns:
    

the list of project IDs

project_exists(_project_id_)#
    

Checks if the given project exists.

Parameters:
    

**project_id** â the project ID

Returns:
    

True/False

delete_project(_project_id_)#
    

Deletes the given project from the CVAT server.

Parameters:
    

**project_id** â the project ID

delete_projects(_project_ids_ , _progress =None_)#
    

Deletes the given projects from the CVAT server.

Parameters:
    

  * **project_ids** â an iterable of project IDs

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




get_project_tasks(_project_id_)#
    

Returns the IDs of the tasks in the given project.

Parameters:
    

**project_id** â a project ID

Returns:
    

the list of task IDs

create_task(_name_ , _schema =None_, _segment_size =None_, _image_quality =75_, _task_assignee =None_, _project_id =None_, _issue_tracker =None_)#
    

Creates a task on the CVAT server using the given label schema.

Parameters:
    

  * **name** â a name for the task

  * **schema** (_None_) â the label schema to use for the created task

  * **segment_size** (_None_) â maximum number of images to load into a job. Not applicable to videos

  * **image_quality** (_75_) â an int in `[0, 100]` determining the image quality to upload to CVAT

  * **task_assignee** (_None_) â the username to assign the created task(s)

  * **project_id** (_None_) â the ID of a project to which upload the task

  * **issue_tracker** (_None_) â the URL of an issue tracker to link the task



Returns:
    

a tuple of

  * **task_id** : the ID of the created task in CVAT

  * **class_id_map** : a dictionary mapping the IDs assigned to classes by CVAT

  * **attr_id_map** : a dictionary mapping the IDs assigned to attributes by CVAT for every class




list_tasks()#
    

Returns the list of task IDs.

Returns:
    

the list of task IDs

task_exists(_task_id_)#
    

Checks if the given task exists.

Parameters:
    

**task_id** â the task ID

Returns:
    

True/False

delete_task(_task_id_)#
    

Deletes the given task from the CVAT server.

Parameters:
    

**task_id** â the task ID

delete_tasks(_task_ids_ , _progress =None_)#
    

Deletes the given tasks from the CVAT server.

Parameters:
    

  * **task_ids** â an iterable of task IDs

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




launch_editor(_url =None_)#
    

Launches the CVAT editor in your default web browser.

Parameters:
    

**url** (_None_) â an optional URL to open. By default, the base URL of the server is opened

upload_data(_task_id_ , _paths_ , _image_quality =75_, _use_cache =True_, _use_zip_chunks =True_, _chunk_size =None_, _job_assignees =None_, _job_reviewers =None_, _frame_start =None_, _frame_stop =None_, _frame_step =None_)#
    

Uploads a list of media to the task with the given ID.

Parameters:
    

  * **task_id** â the task ID

  * **paths** â a list of media paths to upload

  * **image_quality** (_75_) â an int in `[0, 100]` determining the image quality to upload to CVAT

  * **use_cache** (_True_) â whether to use a cache when uploading data. Using a cache reduces task creation time as data will be processed on-the-fly and stored in the cache when requested

  * **use_zip_chunks** (_True_) â when annotating videos, whether to upload video frames in smaller chunks. Setting this option to `False` may result in reduced video quality in CVAT due to size limitations on ZIP files that can be uploaded to CVAT

  * **chunk_size** (_None_) â the number of frames to upload per ZIP chunk

  * **job_assignees** (_None_) â a list of usernames to assign jobs

  * **job_reviewers** (_None_) â a list of usernames to assign job reviews

  * **frame_start** (_None_) â an optional first frame to start uploading from

  * **frame_stop** (_None_) â an optional last frame to upload

  * **frame_step** (_None_) â an optional positive integer specifying the spacing between frames to upload



Returns:
    

a list of the job IDs created for the task

upload_samples(_samples_ , _anno_key_ , _backend_)#
    

Uploads the given samples to CVAT according to the given backendâs annotation and server configuration.

Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **anno_key** â the annotation key

  * **backend** â a `CVATBackend` to use to perform the upload



Returns:
    

a `CVATAnnotationResults`

download_annotations(_results_ , _coerce_text_attrs =True_)#
    

Download the annotations from the CVAT server for the given results instance and parses them into the appropriate FiftyOne types.

Parameters:
    

  * **results** â a `CVATAnnotationResults`

  * **coerce_text_attrs** (_True_) â whether to coerce text attributes to numeric types. Set to False to preserve text attribute values as strings



Returns:
    

the annotations dict

class fiftyone.utils.cvat.CVATLabel(_label_dict_ , _class_map_ , _attr_id_map_ , _server_id_map_ , _attributes =None_, _attr_type_map =None_)#
    

Bases: `object`

A label returned by the CVAT API.

Parameters:
    

  * **label_dict** â the dictionary containing the label information loaded from the CVAT API

  * **class_map** â a dictionary mapping label IDs to class strings

  * **attr_id_map** â a dictionary mapping attribute IDs attribute names for every label

  * **server_id_map** â a dictionary mapping server IDs to FiftyOne label IDs

  * **attributes** (_None_) â an optional list of additional attributes




class fiftyone.utils.cvat.CVATShape(_label_dict_ , _class_map_ , _attr_id_map_ , _server_id_map_ , _metadata_ , _index =None_, _immutable_attrs =None_, _occluded_attrs =None_, _group_id_attrs =None_, _group_id =None_, _attr_type_map =None_)#
    

Bases: `CVATLabel`

A shape returned by the CVAT API.

Parameters:
    

  * **label_dict** â the dictionary containing the label information loaded from the CVAT API

  * **class_map** â a dictionary mapping label IDs to class strings

  * **attr_id_map** â a dictionary mapping attribute IDs attribute names for every label

  * **server_id_map** â a dictionary mapping server IDs to FiftyOne label IDs

  * **metadata** â a dictionary containing the width and height of the frame

  * **index** (_None_) â the tracking index of the shape

  * **immutable_attrs** (_None_) â immutable attributes inherited by this shape from its track

  * **occluded_attrs** (_None_) â a dictionary mapping class names to the corresponding attribute linked to the CVAT occlusion widget, if any

  * **group_id_attrs** (_None_) â a dictionary mapping class names to the corresponding attribute linked to the CVAT group id, if any

  * **group_id** (_None_) â an optional group id value for this shape when it cannot be parsed from the label dict




**Methods:**

`to_detection`() | Converts this shape to a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").  
---|---  
`to_instance`() | Converts this shape to a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") with instance mask.  
`to_polyline`([closed,Â filled]) | Converts this shape to a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").  
`to_polylines`([closed,Â filled]) | Converts this shape to a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines").  
`to_keypoint`() | Converts this shape to a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").  
`polyline_to_detection`(polyline,Â frame_size) | Converts a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") to a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") with a segmentation mask.  
`polylines_to_segmentation`(polylines,Â ...) | Converts a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") to a [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation").  
  
to_detection()#
    

Converts this shape to a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection").

Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

to_instance()#
    

Converts this shape to a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") with instance mask.

Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

to_polyline(_closed =False_, _filled =False_)#
    

Converts this shape to a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline").

Returns:
    

a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

to_polylines(_closed =False_, _filled =False_)#
    

Converts this shape to a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines").

Returns:
    

a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

to_keypoint()#
    

Converts this shape to a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint").

Returns:
    

a [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")

classmethod polyline_to_detection(_polyline_ , _frame_size_)#
    

Converts a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline") to a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection") with a segmentation mask.

Parameters:
    

  * **polyline** â a [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * **frame_size** â the `(width, height)` of the frame



Returns:
    

a [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

classmethod polylines_to_segmentation(_polylines_ , _frame_size_ , _mask_targets_)#
    

Converts a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines") to a [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation").

Parameters:
    

  * **polylines** â a [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

  * **mask_targets** â a dict mapping integer pixel values to label strings

  * **frame_size** â the `(width, height)` of the frame



Returns:
    

a [`fiftyone.core.labels.Segmentation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Segmentation "fiftyone.core.labels.Segmentation")

class fiftyone.utils.cvat.CVATTag(_label_dict_ , _class_map_ , _attr_id_map_ , _server_id_map_ , _attributes =None_, _attr_type_map =None_)#
    

Bases: `CVATLabel`

A tag returned by the CVAT API.

Parameters:
    

  * **label_dict** â the dictionary containing the label information loaded from the CVAT API

  * **class_map** â a dictionary mapping label IDs to class strings

  * **attr_id_map** â a dictionary mapping attribute IDs attribute names for every label

  * **server_id_map** â a dictionary mapping server IDs to FiftyOne label IDs

  * **attributes** (_None_) â an optional list of additional attributes




**Methods:**

`to_classification`() | Converts the tag to a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification").  
---|---  
  
to_classification()#
    

Converts the tag to a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification").

Returns:
    

a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

fiftyone.utils.cvat.load_cvat_image_annotations(_xml_path_)#
    

Loads the CVAT image annotations from the given XML file.

See [this page](user_guide__import_datasets.md#cvatimagedataset-import) for format details.

Parameters:
    

**xml_path** â the path to the annotations XML file

Returns:
    

a tuple of

  * **info** : a dict of dataset info

  * **cvat_task_labels** : a `CVATTaskLabels` instance

  * **cvat_images** : a list of `CVATImage` instances




fiftyone.utils.cvat.load_cvat_video_annotations(_xml_path_)#
    

Loads the CVAT video annotations from the given XML file.

See [this page](user_guide__import_datasets.md#cvatvideodataset-import) for format details.

Parameters:
    

**xml_path** â the path to the annotations XML file

Returns:
    

a tuple of

  * **info** : a dict of dataset info

  * **cvat_task_labels** : a `CVATTaskLabels` instance

  * **cvat_tracks** : a list of `CVATTrack` instances




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
