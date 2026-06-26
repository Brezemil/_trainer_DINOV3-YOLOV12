---
source_url: https://docs.voxel51.com/api/fiftyone.utils.data.exporters.html
---

# fiftyone.utils.data.exporters#

Dataset exporters.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`export_samples`(samples[,Â export_dir,Â ...]) | Exports the given samples to disk.  
---|---  
`write_dataset`(samples,Â sample_parser,Â ...[,Â ...]) | Writes the samples to disk as a dataset in the specified format.  
`build_dataset_exporter`(dataset_type[,Â ...]) | Builds the `DatasetExporter` instance for the given parameters.  
  
**Classes:**

`ExportPathsMixin`() | Mixin for `DatasetExporter` classes that provides convenience methods for parsing the `data_path`, `labels_path`, and `export_media` parameters supported by many exporters.  
---|---  
`MediaExporter`(export_mode[,Â export_path,Â ...]) | Base class for `DatasetExporter` utilities that provide support for populating a directory or manifest of media files.  
`ImageExporter`(*args[,Â default_ext]) | Utility class for `DatasetExporter` instances that export images.  
`VideoExporter`(*args[,Â default_ext]) | Utility class for `DatasetExporter` instances that export videos.  
`DatasetExporter`([export_dir]) | Base interface for exporting datasets.  
`BatchDatasetExporter`([export_dir]) | Base interface for exporters that export entire [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instances in a single batch.  
`GenericSampleDatasetExporter`([export_dir]) | Interface for exporting datasets of arbitrary [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances.  
`GroupDatasetExporter`([export_dir]) | Interface for exporting grouped datasets.  
`UnlabeledImageDatasetExporter`([export_dir]) | Interface for exporting datasets of unlabeled image samples.  
`UnlabeledVideoDatasetExporter`([export_dir]) | Interface for exporting datasets of unlabeled video samples.  
`UnlabeledMediaDatasetExporter`([export_dir]) | Interface for exporting datasets of unlabeled samples.  
`LabeledImageDatasetExporter`([export_dir]) | Interface for exporting datasets of labeled image samples.  
`LabeledVideoDatasetExporter`([export_dir]) | Interface for exporting datasets of labeled video samples.  
`LegacyFiftyOneDatasetExporter`(export_dir[,Â ...]) | Legacy exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.  
`FiftyOneDatasetExporter`(export_dir[,Â ...]) | Exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.  
`ImageDirectoryExporter`(export_dir[,Â ...]) | Exporter that writes a directory of images to disk.  
`VideoDirectoryExporter`(export_dir[,Â ...]) | Exporter that writes a directory of videos to disk.  
`MediaDirectoryExporter`(export_dir[,Â ...]) | Exporter that writes a directory of media files of arbitrary type to disk.  
`FiftyOneImageClassificationDatasetExporter`([...]) | Exporter that writes an image classification dataset to disk in a simple JSON format.  
`ImageClassificationDirectoryTreeExporter`(...) | Exporter that writes an image classification directory tree to disk.  
`VideoClassificationDirectoryTreeExporter`(...) | Exporter that writes a video classification directory tree to disk.  
`FiftyOneImageDetectionDatasetExporter`([...]) | Exporter that writes an image detection dataset to disk in a simple JSON format.  
`FiftyOneTemporalDetectionDatasetExporter`([...]) | Exporter that writes a temporal video detection dataset to disk in a simple JSON format.  
`ImageSegmentationDirectoryExporter`([...]) | Exporter that writes an image segmentation dataset to disk.  
`FiftyOneImageLabelsDatasetExporter`(export_dir) | Exporter that writes a labeled image dataset to disk with labels stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).  
`FiftyOneVideoLabelsDatasetExporter`(export_dir) | Exporter that writes a labeled video dataset with labels stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).  
  
fiftyone.utils.data.exporters.export_samples(_samples_ , _export_dir =None_, _dataset_type =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _dataset_exporter =None_, _label_field =None_, _frame_labels_field =None_, _progress =None_, _num_samples =None_, _** kwargs_)#
    

Exports the given samples to disk.

You can perform exports with this method via the following basic patterns:

  1. Provide `export_dir` and `dataset_type` to export the content to a directory in the default layout for the specified format, as documented in [this page](user_guide__export_datasets.md#exporting-datasets)

  2. Provide `dataset_type` along with `data_path`, `labels_path`, and/or `export_media` to directly specify where to export the source media and/or labels (if applicable) in your desired format. This syntax provides the flexibility to, for example, perform workflows like labels-only exports

  3. Provide a `dataset_exporter` to which to feed samples to perform a fully-customized export




In all workflows, the remaining parameters of this method can be provided to further configure the export.

See [this page](user_guide__export_datasets.md#exporting-datasets) for more information about the available export formats and examples of using this method.

See [this guide](user_guide__export_datasets.md#custom-dataset-exporter) for more details about exporting datasets in custom formats by defining your own `fiftyone.utils.data.exporters.DatasetExporter`.

This method will automatically coerce the data to match the requested export in the following cases:

  * When exporting in either an unlabeled image or image classification format, if a spatial label field is provided ([`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")), then the **image patches** of the provided samples will be exported

  * When exporting in labeled image dataset formats that expect list-type labels ([`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications"), [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints"), or [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")), if a label field contains labels in non-list format (e.g., [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")), the labels will be automatically upgraded to single-label lists

  * When exporting in labeled image dataset formats that expect [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") labels, if a [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification") field is provided, the labels will be automatically upgraded to detections that span the entire images




Parameters:
    

  * **samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **export_dir** (_None_) â the directory to which to export the samples in format `dataset_type`

  * **dataset_type** (_None_) â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type to write

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported media for certain export formats. Can be any of the following:

    * a folder name like `"data"` or `"data/"` specifying a subfolder of `export_dir` in which to export the media

    * an absolute directory path in which to export the media. In this case, the `export_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of a JSON manifest file in `export_dir` generated when `export_media` is `"manifest"`

    * an absolute filepath specifying the location to write the JSON manifest file when `export_media` is `"manifest"`. In this case, `export_dir` has no effect on the location of the data

If None, a default value of this parameter will be chosen based on the value of the `export_media` parameter. Note that this parameter is not applicable to certain export formats such as binary types like TF records

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the exported labels. Only applicable when exporting in certain labeled dataset formats. Can be any of the following:

    * a type-specific folder name like `"labels"` or `"labels/"` or a filename like `"labels.json"` or `"labels.xml"` specifying the location in `export_dir` in which to export the labels

    * an absolute directory or filepath in which to export the labels. In this case, the `export_dir` has no effect on the location of the labels

For labeled datasets, the default value of this parameter will be chosen based on the export format so that the labels will be exported into `export_dir`

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media. This option is only useful when exporting labeled datasets whose label format stores sufficient information to locate the associated media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, an appropriate default value of this parameter will be chosen based on the value of the `data_path` parameter. Note that some dataset formats may not support certain values for this parameter (e.g., when exporting in binary formats such as TF records, âsymlinkâ is not an option)

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **dataset_exporter** (_None_) â a `DatasetExporter` to use to write the dataset

  * **label_field** (_None_) â the name of the label field to export, or a dictionary mapping field names to output keys describing the label fields to export. Only applicable if `dataset_exporter` is a `LabeledImageDatasetExporter` or `LabeledVideoDatasetExporter`, or if you are exporting image patches

  * **frame_labels_field** (_None_) â the name of the frame label field to export, or a dictionary mapping field names to output keys describing the frame label fields to export. Only applicable if `dataset_exporter` is a `LabeledVideoDatasetExporter`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **num_samples** (_None_) â the number of samples in `samples`. If omitted, this is computed (if possible) via `len(samples)` if needed for progress tracking

  * ****kwargs** â optional keyword arguments to pass to the dataset exporterâs constructor. If you are exporting image patches, this can also contain keyword arguments for [`fiftyone.utils.patches.ImagePatchesExtractor`](api__fiftyone.utils.patches.md#fiftyone.utils.patches.ImagePatchesExtractor "fiftyone.utils.patches.ImagePatchesExtractor")




fiftyone.utils.data.exporters.write_dataset(_samples_ , _sample_parser_ , _dataset_exporter_ , _sample_collection =None_, _progress =None_, _num_samples =None_)#
    

Writes the samples to disk as a dataset in the specified format.

Parameters:
    

  * **samples** â an iterable of samples that can be parsed by `sample_parser`

  * **sample_parser** â a [`fiftyone.utils.data.parsers.SampleParser`](api__fiftyone.utils.data.parsers.md#fiftyone.utils.data.parsers.SampleParser "fiftyone.utils.data.parsers.SampleParser") to use to parse the samples

  * **dataset_exporter** â a `DatasetExporter` to use to write the dataset

  * **sample_collection** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") from which `samples` were extracted. If `samples` is itself a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection"), this parameter defaults to `samples`. This parameter is optional and is only passed to `DatasetExporter.log_collection()`

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead

  * **num_samples** (_None_) â the number of samples in `samples`. If omitted, this is computed (if possible) via `len(samples)` if needed for progress tracking




fiftyone.utils.data.exporters.build_dataset_exporter(_dataset_type_ , _strip_none =True_, _warn_unused =True_, _** kwargs_)#
    

Builds the `DatasetExporter` instance for the given parameters.

Parameters:
    

  * **dataset_type** â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type

  * **strip_none** (_True_) â whether to exclude None-valued items from `kwargs`

  * **warn_unused** (_True_) â whether to issue warnings for any non-None unused parameters encountered

  * ****kwargs** â keyword arguments to pass to the dataset exporterâs constructor via `DatasetExporter(**kwargs)`



Returns:
    

  * the `DatasetExporter` instance

  * a dict of unused keyword arguments




Return type:
    

a tuple of

class fiftyone.utils.data.exporters.ExportPathsMixin#
    

Bases: `object`

Mixin for `DatasetExporter` classes that provides convenience methods for parsing the `data_path`, `labels_path`, and `export_media` parameters supported by many exporters.

class fiftyone.utils.data.exporters.MediaExporter(_export_mode_ , _export_path =None_, _rel_dir =None_, _chunk_size =None_, _supported_modes =None_, _default_ext =None_, _ignore_exts =False_)#
    

Bases: `object`

Base class for `DatasetExporter` utilities that provide support for populating a directory or manifest of media files.

This class is designed for populating a single, flat directory or manifest of media files, and automatically takes care of things like name clashes as necessary.

The export strategy used is defined by the `export_mode` parameter, and users of this class can restrict the available options via the `supported_modes` parameter.

Parameters:
    

  * **export_mode** â 

the export mode to use. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media. This option is only useful when exporting labeled datasets whose label format stores sufficient information to locate the associated media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

  * **export_path** (_None_) â 

the location to export the media. Can be any of the following:

    * When `export_media` is True, âmoveâ, or âsymlinkâ, a directory in which to export the media

    * When `export_mode` is âmanifestâ, the path to write a JSON file mapping UUIDs to input filepaths

    * When `export_media` is False, this parameter has no effect

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `export_path` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **chunk_size** (_None_) â an optional chunk size to use when exporting media files. If provided, media files will be nested in subdirectories of the output directory with at most this many media files per subdirectory. Has no effect if a `rel_dir` is provided

  * **supported_modes** (_None_) â an optional tuple specifying a subset of the `export_mode` values that are allowed

  * **default_ext** (_None_) â the file extension to use when generating default output paths

  * **ignore_exts** (_False_) â whether to omit file extensions when generating UUIDs for files




**Methods:**

`setup`() | Performs necessary setup to begin exporting media.  
---|---  
`export`(media_or_path[,Â outpath]) | Exports the given media.  
`close`() | Performs any necessary actions to complete the export.  
  
setup()#
    

Performs necessary setup to begin exporting media.

`DatasetExporter` classes using this class should invoke this method in `DatasetExporter.setup()`.

export(_media_or_path_ , _outpath =None_)#
    

Exports the given media.

Parameters:
    

  * **media_or_path** â the media or path to the media on disk

  * **outpath** (_None_) â a manually-specified location to which to export the media. By default, the media will be exported into `export_path`



Returns:
    

  * the path to the exported media

  * the UUID of the exported media




Return type:
    

a tuple of

close()#
    

Performs any necessary actions to complete the export.

class fiftyone.utils.data.exporters.ImageExporter(_* args_, _default_ext =None_, _** kwargs_)#
    

Bases: `MediaExporter`

Utility class for `DatasetExporter` instances that export images.

See `MediaExporter` for details.

**Methods:**

`close`() | Performs any necessary actions to complete the export.  
---|---  
`export`(media_or_path[,Â outpath]) | Exports the given media.  
`setup`() | Performs necessary setup to begin exporting media.  
  
close()#
    

Performs any necessary actions to complete the export.

export(_media_or_path_ , _outpath =None_)#
    

Exports the given media.

Parameters:
    

  * **media_or_path** â the media or path to the media on disk

  * **outpath** (_None_) â a manually-specified location to which to export the media. By default, the media will be exported into `export_path`



Returns:
    

  * the path to the exported media

  * the UUID of the exported media




Return type:
    

a tuple of

setup()#
    

Performs necessary setup to begin exporting media.

`DatasetExporter` classes using this class should invoke this method in `DatasetExporter.setup()`.

class fiftyone.utils.data.exporters.VideoExporter(_* args_, _default_ext =None_, _** kwargs_)#
    

Bases: `MediaExporter`

Utility class for `DatasetExporter` instances that export videos.

See `MediaExporter` for details.

**Methods:**

`close`() | Performs any necessary actions to complete the export.  
---|---  
`export`(media_or_path[,Â outpath]) | Exports the given media.  
`setup`() | Performs necessary setup to begin exporting media.  
  
close()#
    

Performs any necessary actions to complete the export.

export(_media_or_path_ , _outpath =None_)#
    

Exports the given media.

Parameters:
    

  * **media_or_path** â the media or path to the media on disk

  * **outpath** (_None_) â a manually-specified location to which to export the media. By default, the media will be exported into `export_path`



Returns:
    

  * the path to the exported media

  * the UUID of the exported media




Return type:
    

a tuple of

setup()#
    

Performs necessary setup to begin exporting media.

`DatasetExporter` classes using this class should invoke this method in `DatasetExporter.setup()`.

class fiftyone.utils.data.exporters.DatasetExporter(_export_dir =None_)#
    

Bases: `object`

Base interface for exporting datasets.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

class fiftyone.utils.data.exporters.BatchDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Base interface for exporters that export entire [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instances in a single batch.

This interface allows for greater efficiency for export formats that handle aggregating over the samples themselves.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
---|---  
`export_samples`(sample_collection[,Â progress]) | Exports the given sample collection.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




export_samples(_sample_collection_ , _progress =None_)#
    

Exports the given sample collection.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.GenericSampleDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Interface for exporting datasets of arbitrary [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`export_sample`(sample) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
export_sample(_sample_)#
    

Exports the given sample to the dataset.

Parameters:
    

**sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.GroupDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Interface for exporting grouped datasets.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Methods:**

`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
---|---  
`export_group`(group) | Exports the given group to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




export_group(_group_)#
    

Exports the given group to the dataset.

Parameters:
    

**group** â a dict mapping group slice names to [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances

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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.UnlabeledImageDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Interface for exporting datasets of unlabeled image samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`export_sample`(image_or_path[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

export_sample(_image_or_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.UnlabeledVideoDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Interface for exporting datasets of unlabeled video samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`export_sample`(video_path[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

export_sample(_video_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.UnlabeledMediaDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Interface for exporting datasets of unlabeled samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_metadata` | Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`export_sample`(filepath[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.

export_sample(_filepath_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **filepath** â a media path

  * **metadata** (_None_) â a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance for the sample. Only required when `requires_metadata()` is `True`




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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.LabeledImageDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Interface for exporting datasets of labeled image samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`export_sample`(image_or_path,Â label[,Â metadata]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the exporter directly exports labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can export a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the exporter can handle label dictionaries with value-types specified by this dictionary. Not all keys need be present in the exported label dicts

  * `None`. In this case, the exporter makes no guarantees about the labels that it can export




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

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.LabeledVideoDatasetExporter(_export_dir =None_)#
    

Bases: `DatasetExporter`

Interface for exporting datasets of labeled video samples.

See [this page](user_guide__export_datasets.md#writing-a-custom-dataset-exporter) for information about implementing/using dataset exporters.

Parameters:
    

**export_dir** (_None_) â the directory to write the export. This may be optional for some exporters

**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`export_sample`(video_path,Â label,Â frames[,Â ...]) | Exports the given sample to the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
  
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




export_sample(_video_path_ , _label_ , _frames_ , _metadata =None_)#
    

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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

class fiftyone.utils.data.exporters.LegacyFiftyOneDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _chunk_size =None_, _abs_paths =False_, _export_saved_views =True_, _export_runs =True_, _export_workspaces =True_, _pretty_print =False_)#
    

Bases: `GenericSampleDatasetExporter`

Legacy exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.

Warning

The [`fiftyone.types.FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") format was upgraded in `fiftyone==0.8` and this exporter is now deprecated. The new exporter is `FiftyOneDatasetExporter`.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `False`: donât export media

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **chunk_size** (_None_) â an optional chunk size to use when exporting media files. If provided, media files will be nested in subdirectories of the output directory with at most this many media files per subdirectory. Has no effect if a `rel_dir` is provided

  * **abs_paths** (_False_) â whether to store absolute paths to the media in the exported labels

  * **export_saved_views** (_True_) â whether to include saved views in the export. Only applicable when exporting full datasets

  * **export_runs** (_True_) â whether to include annotation/brain/evaluation runs in the export. Only applicable when exporting full datasets

  * **export_workspaces** (_True_) â whether to include saved workspaces in the export. Only applicable when exporting full datasets

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(sample) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
  
setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

export_sample(_sample_)#
    

Exports the given sample to the dataset.

Parameters:
    

**sample** â a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample")

close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

class fiftyone.utils.data.exporters.FiftyOneDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _chunk_size =None_, _export_saved_views =True_, _export_runs =True_, _export_workspaces =True_, _use_dirs =False_, _ordered =True_)#
    

Bases: `BatchDatasetExporter`

Exporter that writes an entire FiftyOne dataset to disk in a serialized JSON format along with its source media.

See [this page](user_guide__export_datasets.md#fiftyonedataset-export) for format details.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `False`: donât export media

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each media. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **chunk_size** (_None_) â an optional chunk size to use when exporting media files. If provided, media files will be nested in subdirectories of the output directory with at most this many media files per subdirectory. Has no effect if a `rel_dir` is provided

  * **export_saved_views** (_True_) â whether to include saved views in the export. Only applicable when exporting full datasets

  * **export_runs** (_True_) â whether to include annotation/brain/evaluation runs in the export. Only applicable when exporting full datasets

  * **export_workspaces** (_True_) â whether to include saved workspaces in the export. Only applicable when exporting full datasets

  * **use_dirs** (_False_) â whether to export metadata into directories of per sample/frame files

  * **ordered** (_True_) â whether to preserve the order of the exported collections




**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_samples`(sample_collection[,Â progress]) | Exports the given sample collection.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`export_sample`(*args,Â **kwargs) | Exports the given sample to the dataset.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_samples(_sample_collection_ , _progress =None_)#
    

Exports the given sample collection.

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




close(_* args_)#
    

Performs any necessary actions after the last sample has been exported.

This method is called when the exporterâs context manager interface is exited, `DatasetExporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetExporter.__exit__()`

export_sample(_* args_, _** kwargs_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * ***args** â subclass-specific positional arguments

  * ****kwargs** â subclass-specific keyword arguments




log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.data.exporters.ImageDirectoryExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _image_format =None_)#
    

Bases: `UnlabeledImageDatasetExporter`

Exporter that writes a directory of images to disk.

See [this page](user_guide__export_datasets.md#imagedirectory-export) for format details.

The filenames of input image paths will be maintained in the export directory, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_image_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_image_or_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **image_or_path** â an image or the path to the image on disk

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

class fiftyone.utils.data.exporters.VideoDirectoryExporter(_export_dir_ , _export_media =None_, _rel_dir =None_)#
    

Bases: `UnlabeledVideoDatasetExporter`

Exporter that writes a directory of videos to disk.

See [this page](user_guide__export_datasets.md#videodirectory-export) for format details.

The filenames of the input videos will be maintained in the export directory, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(video_path[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_video_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_video_path_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **video_path** â the path to a video on disk

  * **metadata** (_None_) â a [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instance for the sample. Only required when `requires_video_metadata()` is `True`




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

class fiftyone.utils.data.exporters.MediaDirectoryExporter(_export_dir_ , _export_media =None_, _rel_dir =None_)#
    

Bases: `UnlabeledMediaDatasetExporter`

Exporter that writes a directory of media files of arbitrary type to disk.

See [this page](user_guide__export_datasets.md#mediadirectory-export) for format details.

The filenames of the input media files will be maintained in the export directory, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

defines how to export the raw media contained in the dataset. The supported values are:

    * `True` (default): copy all media files into the export directory

    * `"move"`: move media files into the export directory

    * `"symlink"`: create symlinks to each media file in the export directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each output file. This identifier is joined with `export_dir` to generate an output path for each exported media. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")




**Attributes:**

`requires_metadata` | Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(filepath[,Â metadata]) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
property requires_metadata#
    

Whether this exporter requires [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample being exported.

setup()#
    

Performs any necessary setup before exporting the first sample in the dataset.

This method is called when the exporterâs context manager interface is entered, `DatasetExporter.__enter__()`.

export_sample(_filepath_ , _metadata =None_)#
    

Exports the given sample to the dataset.

Parameters:
    

  * **filepath** â a media path

  * **metadata** (_None_) â a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance for the sample. Only required when `requires_metadata()` is `True`




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

class fiftyone.utils.data.exporters.FiftyOneImageClassificationDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _include_confidence =False_, _include_attributes =False_, _classes =None_, _image_format =None_, _pretty_print =False_)#
    

Bases: `LabeledImageDatasetExporter`, `ExportPathsMixin`

Exporter that writes an image classification dataset to disk in a simple JSON format.

See [this page](user_guide__export_datasets.md#fiftyoneimageclassificationdataset-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

  * **include_confidence** (_False_) â 

whether to include classification confidences in the export. The supported values are:

    * `False` (default): do not include confidences

    * `True`: always include confidences

    * `None`: include confidences only if they exist

  * **include_attributes** (_False_) â 

whether to include dynamic attributes of the classifications in the export. Supported values are:

    * `False` (default): do not include attributes

    * `True`: always include a (possibly empty) attributes dict

    * `None`: include attributes only if they exist

    * a name or iterable of names of specific attributes to include

  * **classes** (_None_) â the list of possible class labels

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




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

class fiftyone.utils.data.exporters.ImageClassificationDirectoryTreeExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _image_format =None_)#
    

Bases: `LabeledImageDatasetExporter`

Exporter that writes an image classification directory tree to disk.

See [this page](user_guide__export_datasets.md#imageclassificationdirectorytree-export) for format details.

The filenames of the input images are maintained, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path,Â classification) | Exports the given sample to the dataset.  
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

export_sample(_image_or_path_ , _classification_ , _metadata =None_)#
    

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

class fiftyone.utils.data.exporters.VideoClassificationDirectoryTreeExporter(_export_dir_ , _export_media =None_, _rel_dir =None_)#
    

Bases: `LabeledVideoDatasetExporter`

Exporter that writes a video classification directory tree to disk.

See [this page](user_guide__export_datasets.md#videoclassificationdirectorytree-export) for format details.

The filenames of the input images are maintained, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(video_path,Â classification,Â _) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
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

export_sample(_video_path_ , _classification_ , ___ , _metadata =None_)#
    

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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.data.exporters.FiftyOneImageDetectionDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _classes =None_, _include_confidence =None_, _include_attributes =None_, _image_format =None_, _pretty_print =False_)#
    

Bases: `LabeledImageDatasetExporter`, `ExportPathsMixin`

Exporter that writes an image detection dataset to disk in a simple JSON format.

See [this page](user_guide__export_datasets.md#fiftyoneimagedetectiondataset-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

  * **classes** (_None_) â the list of possible class labels

  * **include_confidence** (_None_) â 

whether to include detection confidences in the export. The supported values are:

    * `None` (default): include confidences only if they exist

    * `True`: always include confidences

    * `False`: do not include confidences

  * **include_attributes** (_None_) â 

whether to include dynamic attributes of the detections in the export. Supported values are:

    * `None` (default): include attributes only if they exist

    * `True`: always include a (possibly empty) attributes dict

    * `False`: do not include attributes

    * a name or iterable of names of specific attributes to include

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Attributes:**

`requires_image_metadata` | Whether this exporter requires [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) exported by this exporter.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(image_or_path,Â detections[,Â ...]) | Exports the given sample to the dataset.  
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

export_sample(_image_or_path_ , _detections_ , _metadata =None_)#
    

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

class fiftyone.utils.data.exporters.FiftyOneTemporalDetectionDatasetExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _abs_paths =False_, _use_timestamps =False_, _classes =None_, _include_confidence =None_, _include_attributes =None_, _pretty_print =False_)#
    

Bases: `LabeledVideoDatasetExporter`, `ExportPathsMixin`

Exporter that writes a temporal video detection dataset to disk in a simple JSON format.

See [this page](user_guide__export_datasets.md#fiftyonetemporaldetectiondataset-export) for format details.

Each input video is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `data_path` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **abs_paths** (_False_) â whether to store absolute paths to the videos in the exported labels

  * **use_timestamps** (_False_) â whether to export the support of each temporal detection in seconds rather than frame numbers

  * **classes** (_None_) â the list of possible class labels

  * **include_confidence** (_None_) â 

whether to include detection confidences in the export. The supported values are:

    * `None` (default): include confidences only if they exist

    * `True`: always include confidences

    * `False`: do not include confidences

  * **include_attributes** (_None_) â 

whether to include dynamic attributes of the detections in the export. Supported values are:

    * `None` (default): include attributes only if they exist

    * `True`: always include a (possibly empty) attributes dict

    * `False`: do not include attributes

    * a name or iterable of names of specific attributes to include

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`export_sample`(video_path,Â temporal_detections,Â _) | Exports the given sample to the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been exported.  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
  
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

export_sample(_video_path_ , _temporal_detections_ , ___ , _metadata =None_)#
    

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

log_collection(_sample_collection_)#
    

Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.

Subclasses can optionally implement this method if their export format can record information such as the [`fiftyone.core.collections.SampleCollection.info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.info "fiftyone.core.collections.SampleCollection.info") of the collection being exported.

By convention, this method must be optional; i.e., if it is not called before the first call to `export_sample()`, then the exporter must make do without any information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") (which may not be available, for example, if the samples being exported are not stored in a collection).

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported

class fiftyone.utils.data.exporters.ImageSegmentationDirectoryExporter(_export_dir =None_, _data_path =None_, _labels_path =None_, _export_media =None_, _rel_dir =None_, _image_format =None_, _mask_format ='.png'_, _mask_size =None_, _mask_targets =None_, _thickness =1_)#
    

Bases: `LabeledImageDatasetExporter`, `ExportPathsMixin`

Exporter that writes an image segmentation dataset to disk.

See [this page](user_guide__export_datasets.md#imagesegmentationdirectory-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

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

    * a folder name like `"labels"` or `"labels/"` specifying the location in `export_dir` in which to export the masks

    * an absolute directory in which to export the masks. In this case, the `export_dir` has no effect on the location of the masks

If None, the masks will be exported into `export_dir` using the default folder name

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True`: copy all media files into the output directory

    * `False`: donât export media

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

    * `"manifest"`: create a `data.json` in the output directory that maps UUIDs used in the labels files to the filepaths of the source media, rather than exporting the actual media

If None, the default value of this parameter will be chosen based on the value of the `data_path` parameter

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `data_path` and `labels_path` to generate output paths for each exported image and mask. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **mask_format** (_".png"_) â the image format to use when writing masks to disk

  * **mask_size** (_None_) â the `(width, height)` at which to render segmentation masks when exporting instances or polylines. If not provided, masks will be rendered to match the resolution of each input image

  * **mask_targets** (_None_) â a dict mapping integer pixel values in `[0, 255]` to label strings defining which object classes to render and which pixel values to use for each class. If omitted, all objects are rendered with pixel value 255

  * **thickness** (_1_) â the thickness, in pixels, at which to render (non-filled) polylines




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

class fiftyone.utils.data.exporters.FiftyOneImageLabelsDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _image_format =None_, _pretty_print =False_)#
    

Bases: `LabeledImageDatasetExporter`

Exporter that writes a labeled image dataset to disk with labels stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).

See [this page](user_guide__export_datasets.md#fiftyoneimagelabelsdataset-export) for format details.

If the path to an image is provided, the image is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each image. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported image. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **image_format** (_None_) â the image format to use when writing in-memory images to disk. By default, `fiftyone.config.default_image_ext` is used

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




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

class fiftyone.utils.data.exporters.FiftyOneVideoLabelsDatasetExporter(_export_dir_ , _export_media =None_, _rel_dir =None_, _pretty_print =False_)#
    

Bases: `LabeledVideoDatasetExporter`

Exporter that writes a labeled video dataset with labels stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).

See [this page](user_guide__export_datasets.md#fiftyonevideolabelsdataset-export) for format details.

If the path to a video is provided, the video is directly copied to its destination, maintaining the original filename, unless a name conflict would occur, in which case an index of the form `"-%d" % count` is appended to the base filename.

Parameters:
    

  * **export_dir** â the directory to write the export

  * **export_media** (_None_) â 

controls how to export the raw media. The supported values are:

    * `True` (default): copy all media files into the output directory

    * `"move"`: move all media files into the output directory

    * `"symlink"`: create symlinks to the media files in the output directory

  * **rel_dir** (_None_) â an optional relative directory to strip from each input filepath to generate a unique identifier for each video. When exporting media, this identifier is joined with `export_dir` to generate an output path for each exported video. This argument allows for populating nested subdirectories that match the shape of the input paths. The path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **pretty_print** (_False_) â whether to render the JSON in human readable format with newlines and indentations




**Attributes:**

`requires_video_metadata` | Whether this exporter requires [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each sample being exported.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported at the sample-level.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) that can be exported by this exporter at the frame-level.  
  
**Methods:**

`setup`() | Performs any necessary setup before exporting the first sample in the dataset.  
---|---  
`log_collection`(sample_collection) | Logs any relevant information about the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose samples will be exported.  
`export_sample`(video_path,Â label,Â frames[,Â ...]) | Exports the given sample to the dataset.  
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

export_sample(_video_path_ , _label_ , _frames_ , _metadata =None_)#
    

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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
