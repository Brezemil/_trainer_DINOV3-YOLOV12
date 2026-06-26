---
source_url: https://docs.voxel51.com/api/fiftyone.utils.data.importers.html
---

# fiftyone.utils.data.importers#

Dataset importers.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`import_samples`(dataset,Â dataset_importer[,Â ...]) | Adds the samples from the given `DatasetImporter` to the dataset.  
---|---  
`merge_samples`(dataset,Â dataset_importer[,Â ...]) | Merges the samples from the given `DatasetImporter` into the dataset.  
`build_dataset_importer`(dataset_type[,Â ...]) | Builds the `DatasetImporter` instance for the given parameters.  
`parse_dataset_info`(dataset,Â info[,Â overwrite]) | Parses the info returned by `DatasetImporter.get_dataset_info()` and stores it on the relevant properties of the dataset.  
  
**Classes:**

`ImportPathsMixin`() | Mixin for `DatasetImporter` classes that provides convenience methods for parsing the `data_path` and `labels_path` parameters supported by many importers.  
---|---  
`DatasetImporter`([dataset_dir,Â shuffle,Â ...]) | Base interface for importing datasets stored on disk into FiftyOne.  
`BatchDatasetImporter`([dataset_dir,Â shuffle,Â ...]) | Base interface for importers that load all of their samples in a single call to `import_samples()`.  
`GenericSampleDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets that contain arbitrary [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances.  
`GroupDatasetImporter`([dataset_dir,Â shuffle,Â ...]) | Interface for importing datasets that contain arbitrary grouped [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances.  
`UnlabeledImageDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of unlabeled image samples.  
`UnlabeledVideoDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of unlabeled video samples.  
`UnlabeledMediaDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of unlabeled media samples.  
`LabeledImageDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of labeled image samples.  
`LabeledVideoDatasetImporter`([dataset_dir,Â ...]) | Interface for importing datasets of labeled video samples.  
`LegacyFiftyOneDatasetImporter`(dataset_dir[,Â ...]) | Legacy importer for FiftyOne datasets stored on disk in a serialized JSON format.  
`FiftyOneDatasetImporter`(dataset_dir[,Â ...]) | Importer for FiftyOne datasets stored on disk in serialized JSON format.  
`ImageDirectoryImporter`(dataset_dir[,Â ...]) | Importer for a directory of images stored on disk.  
`VideoDirectoryImporter`(dataset_dir[,Â ...]) | Importer for a directory of videos stored on disk.  
`MediaDirectoryImporter`(dataset_dir[,Â ...]) | Importer for a directory of media files stored on disk.  
`FiftyOneImageClassificationDatasetImporter`([...]) | Importer for image classification datasets stored on disk in a simple JSON format.  
`ImageClassificationDirectoryTreeImporter`(...) | Importer for an image classification directory tree stored on disk.  
`VideoClassificationDirectoryTreeImporter`(...) | Importer for a viideo classification directory tree stored on disk.  
`FiftyOneImageDetectionDatasetImporter`([...]) | Importer for image detection datasets stored on disk in a simple JSON format.  
`FiftyOneTemporalDetectionDatasetImporter`([...]) | Importer for temporal video detection datasets stored on disk in a simple JSON format.  
`ImageSegmentationDirectoryImporter`([...]) | Importer for image segmentation datasets stored on disk.  
`FiftyOneImageLabelsDatasetImporter`(dataset_dir) | Importer for labeled image datasets whose labels are stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).  
`FiftyOneVideoLabelsDatasetImporter`(dataset_dir) | Importer for labeled video datasets whose labels are stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).  
  
fiftyone.utils.data.importers.import_samples(_dataset_ , _dataset_importer_ , _label_field =None_, _tags =None_, _expand_schema =True_, _dynamic =False_, _add_info =True_, _generator =False_, _progress =None_)#
    

Adds the samples from the given `DatasetImporter` to the dataset.

See [this guide](user_guide__import_datasets.md#custom-dataset-importer) for more details about importing datasets in custom formats by defining your own `DatasetImporter`.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **dataset_importer** â a `DatasetImporter`

  * **label_field** (_None_) â controls the field(s) in which imported labels are stored. Only applicable if `dataset_importer` is a `LabeledImageDatasetImporter` or `LabeledVideoDatasetImporter`. If the importer produces a single [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance per sample/frame, this argument specifies the name of the field to use; the default is `"ground_truth"`. If the importer produces a dictionary of labels per sample, this argument can be either a string prefix to prepend to each label key or a dict mapping label keys to field names; the default in this case is to directly use the keys of the imported label dictionaries as field names

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **expand_schema** (_True_) â whether to dynamically add new sample fields encountered to the dataset schema. If False, an error is raised if a sampleâs schema is not a subset of the dataset schema

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **add_info** (_True_) â whether to add dataset info from the importer (if any) to the dataset

  * **generator** (_False_) â whether to yield ID batches as a generator as samples are added to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

fiftyone.utils.data.importers.merge_samples(_dataset_ , _dataset_importer_ , _label_field =None_, _tags =None_, _key_field ='filepath'_, _key_fcn =None_, _skip_existing =False_, _insert_new =True_, _fields =None_, _omit_fields =None_, _merge_lists =True_, _merge_embedded_docs =False_, _overwrite =True_, _expand_schema =True_, _dynamic =False_, _add_info =True_, _progress =None_)#
    

Merges the samples from the given `DatasetImporter` into the dataset.

See [this guide](user_guide__import_datasets.md#custom-dataset-importer) for more details about importing datasets in custom formats by defining your own `DatasetImporter`.

By default, samples with the same absolute `filepath` are merged, but you can customize this behavior via the `key_field` and `key_fcn` parameters. For example, you could set `key_fcn = lambda sample: os.path.basename(sample.filepath)` to merge samples with the same base filename.

The behavior of this method is highly customizable. By default, all top-level fields from the imported samples are merged in, overwriting any existing values for those fields, with the exception of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields), in which case the elements of the lists themselves are merged. In the case of label list fields, labels with the same `id` in both collections are updated rather than duplicated.

To avoid confusion between missing fields and fields whose value is `None`, `None`-valued fields are always treated as missing while merging.

This method can be configured in numerous ways, including:

  * Whether existing samples should be modified or skipped

  * Whether new samples should be added or omitted

  * Whether new fields can be added to the dataset schema

  * Whether list fields should be treated as ordinary fields and merged as a whole rather than merging their elements

  * Whether to merge only specific fields, or all but certain fields

  * Mapping input fields to different field names of this dataset




Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **dataset_importer** â a `DatasetImporter`

  * **label_field** (_None_) â controls the field(s) in which imported labels are stored. Only applicable if `dataset_importer` is a `LabeledImageDatasetImporter` or `LabeledVideoDatasetImporter`. If the importer produces a single [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance per sample/frame, this argument specifies the name of the field to use; the default is `"ground_truth"`. If the importer produces a dictionary of labels per sample, this argument can be either a string prefix to prepend to each label key or a dict mapping label keys to field names; the default in this case is to directly use the keys of the imported label dictionaries as field names

  * **tags** (_None_) â an optional tag or iterable of tags to attach to each sample

  * **key_field** (_"filepath"_) â the sample field to use to decide whether to join with an existing sample

  * **key_fcn** (_None_) â a function that accepts a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instance and computes a key to decide if two samples should be merged. If a `key_fcn` is provided, `key_field` is ignored

  * **skip_existing** (_False_) â whether to skip existing samples (True) or merge them (False)

  * **insert_new** (_True_) â whether to insert new samples (True) or skip them (False)

  * **fields** (_None_) â an optional field or iterable of fields to which to restrict the merge. If provided, fields other than these are omitted from `samples` when merging or adding samples. One exception is that `filepath` is always included when adding new samples, since the field is required. This can also be a dict mapping field names of the input collection to field names of this dataset

  * **omit_fields** (_None_) â an optional field or iterable of fields to exclude from the merge. If provided, these fields are omitted from imported samples, if present. One exception is that `filepath` is always included when adding new samples, since the field is required

  * **merge_lists** (_True_) â whether to merge the elements of list fields (e.g., `tags`) and label list fields (e.g., [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") fields) rather than merging the entire top-level field like other field types. For label lists fields, existing `fiftyone.core.label.Label` elements are either replaced (when `overwrite` is True) or kept (when `overwrite` is False) when their `id` matches a label from the provided samples

  * **merge_embedded_docs** (_False_) â whether to merge the attributes of embedded documents (True) rather than merging the entire top-level field (False)

  * **overwrite** (_True_) â whether to overwrite (True) or skip (False) existing fields and label elements

  * **expand_schema** (_True_) â whether to dynamically add new fields encountered to the dataset schema. If False, an error is raised if a sampleâs schema is not a subset of the dataset schema

  * **dynamic** (_False_) â whether to declare dynamic attributes of embedded document fields that are encountered

  * **add_info** (_True_) â whether to add dataset info from the importer (if any) to the dataset

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.data.importers.build_dataset_importer(_dataset_type_ , _strip_none =True_, _warn_unused =True_, _name =None_, _** kwargs_)#
    

Builds the `DatasetImporter` instance for the given parameters.

Parameters:
    

  * **dataset_type** â the [`fiftyone.types.Dataset`](api__fiftyone.types.md#fiftyone.types.Dataset "fiftyone.types.Dataset") type

  * **strip_none** (_True_) â whether to exclude None-valued items from `kwargs`

  * **warn_unused** (_True_) â whether to issue warnings for any non-None unused parameters encountered

  * **name** (_None_) â the name of the dataset being imported into, if known

  * ****kwargs** â keyword arguments to pass to the dataset importerâs constructor via `DatasetImporter(**kwargs)`



Returns:
    

  * the `DatasetImporter` instance

  * a dict of unused keyword arguments




Return type:
    

a tuple of

fiftyone.utils.data.importers.parse_dataset_info(_dataset_ , _info_ , _overwrite =True_)#
    

Parses the info returned by `DatasetImporter.get_dataset_info()` and stores it on the relevant properties of the dataset.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **info** â an info dict

  * **overwrite** (_True_) â whether to overwrite existing dataset info fields




class fiftyone.utils.data.importers.ImportPathsMixin#
    

Bases: `object`

Mixin for `DatasetImporter` classes that provides convenience methods for parsing the `data_path` and `labels_path` parameters supported by many importers.

class fiftyone.utils.data.importers.DatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `object`

Base interface for importing datasets stored on disk into FiftyOne.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

subclass-specific information for the sample

Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

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

class fiftyone.utils.data.importers.BatchDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `DatasetImporter`

Base interface for importers that load all of their samples in a single call to `import_samples()`.

This interface allows for greater efficiency for import formats that handle aggregating over the samples themselves.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Methods:**

`import_samples`(dataset[,Â tags,Â progress]) | Imports the samples into the given dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
  
import_samples(_dataset_ , _tags =None_, _progress =None_)#
    

Imports the samples into the given dataset.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **tags** (_None_) â an optional list of tags to attach to each sample

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.GenericSampleDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `DatasetImporter`

Interface for importing datasets that contain arbitrary [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instance

Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_sample_field_schema` | Whether this importer produces a sample field schema.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

get_sample_field_schema()#
    

Returns a dictionary describing the field schema of the samples loaded by this importer.

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or `str(field)` representations of them

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.GroupDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `GenericSampleDatasetImporter`

Interface for importing datasets that contain arbitrary grouped [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported across all group slices.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next group in the dataset.

Returns:
    

a dict mapping slice names to [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") instances

Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`group_field` | The name of the group field to populate on each sample.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`has_sample_field_schema` | Whether this importer produces a sample field schema.  
  
**Methods:**

`get_group_media_types`() | Returns a dictionary describing the group slices of the samples loaded by this importer.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property group_field#
    

The name of the group field to populate on each sample.

get_group_media_types()#
    

Returns a dictionary describing the group slices of the samples loaded by this importer.

Returns:
    

a dict mapping slice names to media types

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

get_sample_field_schema()#
    

Returns a dictionary describing the field schema of the samples loaded by this importer.

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or `str(field)` representations of them

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.UnlabeledImageDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `DatasetImporter`

Interface for importing datasets of unlabeled image samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(image_path, image_metadata)` tuple, where

  * `image_path`: the path to the image on disk

  * `image_metadata`: an [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for the image, or `None` if `has_image_metadata()` is `False`




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.UnlabeledVideoDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `DatasetImporter`

Interface for importing datasets of unlabeled video samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(video_path, video_metadata)` tuple, where

  * `video_path`: the path to the video on disk

  * `video_metadata`: an [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for the video, or `None` if `has_video_metadata()` is `False`




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.UnlabeledMediaDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `DatasetImporter`

Interface for importing datasets of unlabeled media samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(filepath, metadata)` tuple, where

  * `filepath`: the path to the media on disk

  * `metadata`: a [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instance for the media, or `None` if `has_metadata()` is `False`




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_metadata` | Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.LabeledImageDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `DatasetImporter`

Interface for importing datasets of labeled image samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(image_path, image_metadata, label)` tuple, where

  * `image_path`: the path to the image on disk

  * `image_metadata`: an [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for the image, or `None` if `has_image_metadata()` is `False`

  * `label`: an instance of `label_cls()`, or a dictionary mapping field names to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances, or `None` if the sample is unlabeled




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the labels that it may return




close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.LabeledVideoDatasetImporter(_dataset_dir =None_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `DatasetImporter`

Interface for importing datasets of labeled video samples.

Typically, dataset importers should implement the parameters documented on this class, although this is not mandatory.

See [this page](user_guide__import_datasets.md#writing-a-custom-dataset-importer) for information about implementing/using dataset importers.

__len__()#
    

The total number of samples that will be imported.

Raises:
    

**TypeError** â if the total number is not known

__next__()#
    

Returns information about the next sample in the dataset.

Returns:
    

an `(video_path, video_metadata, labels, frames)` tuple, where

  * `video_path`: the path to the video on disk

  * `video_metadata`: an [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for the video, or `None` if `has_video_metadata()` is `False`

  * `labels`: sample-level labels for the video, which can be any of the following:

    * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance

    * a dictionary mapping label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances

    * `None` if the sample has no sample-level labels

  * `frames`: frame-level labels for the video, which can be any of the following:

    * a dictionary mapping frame numbers to dictionaries that map label fields to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances for each video frame

    * `None` if the sample has no frame-level labels




Raises:
    

**StopIteration** â if there are no more samples to import

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. This may be optional for some importers

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
---|---  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
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




close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

class fiftyone.utils.data.importers.LegacyFiftyOneDatasetImporter(_dataset_dir_ , _rel_dir =None_, _import_saved_views =True_, _import_runs =True_, _import_workspaces =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `GenericSampleDatasetImporter`

Legacy importer for FiftyOne datasets stored on disk in a serialized JSON format.

Warning

The [`fiftyone.types.FiftyOneDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneDataset "fiftyone.types.FiftyOneDataset") format was upgraded in `fiftyone==0.8` and this importer is now deprecated.

However, to maintain backwards compatibility, `FiftyOneDatasetImporter` will check for instances of datasets of this type at runtime and defer to this class to load them.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **rel_dir** (_None_) â a relative directory to prepend to each filepath if it is not absolute. This path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **import_saved_views** (_True_) â whether to include saved views in the import. Only applicable when importing full datasets

  * **import_runs** (_True_) â whether to include annotation/brain/evaluation runs in the import. Only applicable when importing full datasets

  * **import_workspaces** (_True_) â whether to include saved workspaces in the import. Only applicable when importing full datasets

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_sample_field_schema` | Whether this importer produces a sample field schema.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_sample_field_schema`() | Returns a dictionary describing the field schema of the samples loaded by this importer.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`import_extras`(sample_collection) |   
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_sample_field_schema#
    

Whether this importer produces a sample field schema.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

get_sample_field_schema()#
    

Returns a dictionary describing the field schema of the samples loaded by this importer.

Returns:
    

a dict mapping field names to [`fiftyone.core.fields.Field`](api__fiftyone.core.fields.md#fiftyone.core.fields.Field "fiftyone.core.fields.Field") instances or `str(field)` representations of them

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

import_extras(_sample_collection_)#
    

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

class fiftyone.utils.data.importers.FiftyOneDatasetImporter(_dataset_dir_ , _rel_dir =None_, _import_saved_views =True_, _import_runs =True_, _import_workspaces =True_, _ordered =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `BatchDatasetImporter`

Importer for FiftyOne datasets stored on disk in serialized JSON format.

See [this page](user_guide__import_datasets.md#fiftyonedataset-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **rel_dir** (_None_) â a relative directory to prepend to the `filepath` of each sample if the filepath is not absolute. This path is converted to an absolute path (if necessary) via [`fiftyone.core.storage.normalize_path()`](api__fiftyone.core.storage.md#fiftyone.core.storage.normalize_path "fiftyone.core.storage.normalize_path")

  * **import_saved_views** (_True_) â whether to include saved views in the import. Only applicable when importing full datasets

  * **import_runs** (_True_) â whether to include annotation/brain/evaluation runs in the import. Only applicable when importing full datasets

  * **import_workspaces** (_True_) â whether to include saved workspaces in the import. Only applicable when importing full datasets

  * **ordered** (_True_) â whether to preserve document order when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`import_samples`(dataset[,Â tags,Â progress]) | Imports the samples into the given dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
  
setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

import_samples(_dataset_ , _tags =None_, _progress =None_)#
    

Imports the samples into the given dataset.

Parameters:
    

  * **dataset** â a [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset")

  * **tags** (_None_) â an optional list of tags to attach to each sample

  * **progress** (_None_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead



Returns:
    

a list of IDs of the samples that were added to the dataset

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

class fiftyone.utils.data.importers.ImageDirectoryImporter(_dataset_dir_ , _recursive =True_, _compute_metadata =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `UnlabeledImageDatasetImporter`

Importer for a directory of images stored on disk.

See [this page](user_guide__import_datasets.md#imagedirectory-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

class fiftyone.utils.data.importers.VideoDirectoryImporter(_dataset_dir_ , _recursive =True_, _compute_metadata =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `UnlabeledVideoDatasetImporter`

Importer for a directory of videos stored on disk.

See [this page](user_guide__import_datasets.md#videodirectory-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

class fiftyone.utils.data.importers.MediaDirectoryImporter(_dataset_dir_ , _recursive =True_, _compute_metadata =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `UnlabeledMediaDatasetImporter`

Importer for a directory of media files stored on disk.

See [this page](user_guide__import_datasets.md#mediadirectory-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each media file when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_metadata` | Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

property has_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.Metadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.Metadata "fiftyone.core.metadata.Metadata") instances for each sample.

setup()#
    

Performs any necessary setup before importing the first sample in the dataset.

This method is called when the importerâs context manager interface is entered, `DatasetImporter.__enter__()`.

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

class fiftyone.utils.data.importers.FiftyOneImageClassificationDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledImageDatasetImporter`, `ImportPathsMixin`

Importer for image classification datasets stored on disk in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyoneimageclassificationdataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

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

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

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

class fiftyone.utils.data.importers.ImageClassificationDirectoryTreeImporter(_dataset_dir_ , _compute_metadata =False_, _classes =None_, _unlabeled ='_unlabeled'_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledImageDatasetImporter`

Importer for an image classification directory tree stored on disk.

See [this page](user_guide__import_datasets.md#imageclassificationdirectorytree-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **classes** (_None_) â an optional string or list of strings specifying a subset of classes to load

  * **unlabeled** (_"_unlabeled"_) â the name of the subdirectory containing unlabeled images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_image_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

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

class fiftyone.utils.data.importers.VideoClassificationDirectoryTreeImporter(_dataset_dir_ , _compute_metadata =False_, _classes =None_, _unlabeled ='_unlabeled'_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledVideoDatasetImporter`

Importer for a viideo classification directory tree stored on disk.

See [this page](user_guide__import_datasets.md#videoclassificationdirectorytree-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **classes** (_None_) â an optional string or list of strings specifying a subset of classes to load

  * **unlabeled** (_"_unlabeled"_) â the name of the subdirectory containing unlabeled images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
  
property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

property has_dataset_info#
    

Whether this importer produces a dataset info dictionary.

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

class fiftyone.utils.data.importers.FiftyOneImageDetectionDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledImageDatasetImporter`, `ImportPathsMixin`

Importer for image detection datasets stored on disk in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyoneimagedetectiondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

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

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

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

class fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledVideoDatasetImporter`, `ImportPathsMixin`

Importer for temporal video detection datasets stored on disk in a simple JSON format.

See [this page](user_guide__import_datasets.md#fiftyonetemporaldetectiondataset-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

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

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **include_all_data** (_False_) â whether to generate samples for all videos in the data directory (True) rather than only creating samples for videos with labels (False)

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

class fiftyone.utils.data.importers.ImageSegmentationDirectoryImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _load_masks =False_, _force_grayscale =False_, _compute_metadata =False_, _include_all_data =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledImageDatasetImporter`, `ImportPathsMixin`

Importer for image segmentation datasets stored on disk.

See [this page](user_guide__import_datasets.md#imagesegmentationdirectory-import) for format details.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory. If omitted, `data_path` and/or `labels_path` must be provided

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

    * a dict mapping filenames to absolute filepaths

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a folder name like `"labels"` or `"labels/"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels/`

  * **load_masks** (_False_) â whether to load the masks into the database (True) or simply record the paths to the masks (False)

  * **force_grayscale** (_False_) â whether to load RGB masks as grayscale by storing only the first channel

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **include_all_data** (_False_) â whether to generate samples for all images in the data directory (True) rather than only creating samples for images with masks (False)

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
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
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

close(_* args_)#
    

Performs any necessary actions after the last sample has been imported.

This method is called when the importerâs context manager interface is exited, `DatasetImporter.__exit__()`.

Parameters:
    

***args** â the arguments to `DatasetImporter.__exit__()`

get_dataset_info()#
    

Returns the dataset info for the dataset.

By convention, this method should be called after all samples in the dataset have been imported.

Returns:
    

a dict of dataset info

class fiftyone.utils.data.importers.FiftyOneImageLabelsDatasetImporter(_dataset_dir_ , _compute_metadata =False_, _prefix =None_, _labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledImageDatasetImporter`

Importer for labeled image datasets whose labels are stored in [ETA ImageLabels format](https://github.com/voxel51/eta/blob/develop/docs/image_labels_guide.md).

See [this page](user_guide__import_datasets.md#fiftyoneimagelabelsdataset-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image when importing

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded label dictionary

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the image labels to field names into which to expand them

  * **multilabel** (_False_) â whether to store frame attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical frame attributes (True) or cast them to strings (False)

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

class fiftyone.utils.data.importers.FiftyOneVideoLabelsDatasetImporter(_dataset_dir_ , _compute_metadata =False_, _prefix =None_, _labels_dict =None_, _frame_labels_dict =None_, _multilabel =False_, _skip_non_categorical =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `LabeledVideoDatasetImporter`

Importer for labeled video datasets whose labels are stored in [ETA VideoLabels format](https://github.com/voxel51/eta/blob/develop/docs/video_labels_guide.md).

See [this page](user_guide__import_datasets.md#fiftyonevideolabelsdataset-import) for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **prefix** (_None_) â a string prefix to prepend to each label name in the expanded sample/frame label dictionaries

  * **labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the sample labels to field names into which to expand them. By default, all sample labels are loaded

  * **frame_labels_dict** (_None_) â a dictionary mapping names of attributes/objects in the frame labels to field names into which to expand them. By default, all frame labels are loaded

  * **multilabel** (_False_) â whether to store frame attributes in a single [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications") instance

  * **skip_non_categorical** (_False_) â whether to skip non-categorical frame attributes (True) or cast them to strings (False)

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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
