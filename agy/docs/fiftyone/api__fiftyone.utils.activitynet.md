---
source_url: https://docs.voxel51.com/api/fiftyone.utils.activitynet.html
---

# fiftyone.utils.activitynet#

Utilities for working with the ActivityNet dataset <http://activity-net.org/index.html>.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_activitynet_split`(dataset_dir,Â split) | Utility that downloads full or partial splits of the [ActivityNet dataset](http://activity-net.org/index.html).  
---|---  
  
**Classes:**

`ActivityNetDatasetImporter`([dataset_dir,Â ...]) | Class for importing ActivityNet dataset splits downloaded via `download_activitynet_split()`.  
---|---  
`ActivityNetDownloadConfig`(split[,Â ...]) | Configuration class for downloading full or partial splits from the ActivityNet dataset.  
`ActivityNetDatasetManager`(foz_dir,Â version) | Class that manages the sample IDs and labels that need to be downloaded to load the specified subset of an ActivityNet dataset.  
`ActivityNetInfo`(raw_annotations) | Necessary information used to parse and format annotations.  
`ActivityNetSplitInfo`(split_dir[,Â version,Â ...]) | Class that contains information related to paths, labels, and sample IDs of a single ActivityNet split.  
`ActivityNetDatasetInfo`(foz_dir) | Class that stores information related to paths, labels, and sample IDs for an ActivityNet dataset download.  
`ActivityNet100DatasetInfo`(foz_dir) | ActivityNet 100 dataset info.  
`ActivityNet200DatasetInfo`(foz_dir) | ActivityNet 200 dataset info.  
  
fiftyone.utils.activitynet.download_activitynet_split(_dataset_dir_ , _split_ , _source_dir =None_, _classes =None_, _max_duration =None_, _copy_files =True_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_, _version ='200'_)#
    

Utility that downloads full or partial splits of the [ActivityNet dataset](http://activity-net.org/index.html).

Parameters:
    

  * **dataset_dir** â the directory to download the dataset

  * **split** â the split to download. Supported values are `("train", "validation", "test")`

  * **source_dir** (_None_) â the directory containing the manually downloaded ActivityNet files

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **max_duration** (_None_) â only videos with a duration in seconds that is less than or equal to the `max_duration` will be downloaded. By default, all videos are downloaded

  * **copy_files** (_True_) â whether to move (False) or create copies (True) of the source files when populating `dataset_dir`. This is only relevant when a `source_dir` is provided

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual videos

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded

  * **version** (_"200"_) â the ActivityNet dataset version to download. The supported values are `("100", "200")`



Returns:
    

  * **num_samples** : the total number of downloaded videos, or `None` if everything was already downloaded

  * **classes** : the list of all classes, or `None` if everything was already downloaded

  * **did_download** : whether any content was downloaded (True) or if all necessary files were already downloaded (False)




Return type:
    

a tuple of

class fiftyone.utils.activitynet.ActivityNetDatasetImporter(_dataset_dir =None_, _data_path =None_, _labels_path =None_, _classes =None_, _max_duration =None_, _compute_metadata =False_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`FiftyOneTemporalDetectionDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter "fiftyone.utils.data.importers.FiftyOneTemporalDetectionDatasetImporter")

Class for importing ActivityNet dataset splits downloaded via `download_activitynet_split()`.

Parameters:
    

  * **dataset_dir** (_None_) â the dataset directory

  * **data_path** (_None_) â 

an optional parameter that enables explicit control over the location of the media. Can be any of the following:

    * a folder name like `"data"` or `"data"/` specifying a subfolder of `dataset_dir` where the media files reside

    * an absolute directory path where the media files reside. In this case, the `dataset_dir` has no effect on the location of the data

    * a filename like `"data.json"` specifying the filename of the JSON data manifest file in `dataset_dir`

    * an absolute filepath specifying the location of the JSON data manifest. In this case, `dataset_dir` has no effect on the location of the data

If None, this parameter will default to whichever of `data/` or `data.json` exists in the dataset directory

  * **labels_path** (_None_) â 

an optional parameter that enables explicit control over the location of the labels. Can be any of the following:

    * a filename like `"labels.json"` specifying the location of the labels in `dataset_dir`

    * an absolute filepath to the labels. In this case, `dataset_dir` has no effect on the location of the labels

If None, the parameter will default to `labels.json`

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **max_duration** (_None_) â only videos with a duration in seconds that is less than or equal to the max_duration will be loaded. By default, all videos are loaded

  * **compute_metadata** (_False_) â whether to produce [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video when importing

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to import. By default, all samples are imported




**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`frame_labels_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.  
`has_video_metadata` | Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.  
  
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

property frame_labels_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the frame labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return frame labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single frame label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return frame label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in each frame

  * `None`. In this case, the importer makes no guarantees about the frame labels that it may return




property has_video_metadata#
    

Whether this importer produces [`fiftyone.core.metadata.VideoMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.VideoMetadata "fiftyone.core.metadata.VideoMetadata") instances for each video.

property label_cls#
    

The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer within the sample-level labels that it produces.

This can be any of the following:

  * a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class. In this case, the importer is guaranteed to return sample-level labels of this type

  * a list or tuple of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer can produce a single sample-level label field of any of these types

  * a dict mapping keys to [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") classes. In this case, the importer will return sample-level label dictionaries with keys and value-types specified by this dictionary. Not all keys need be present in the imported labels

  * `None`. In this case, the importer makes no guarantees about the sample-level labels that it may return




class fiftyone.utils.activitynet.ActivityNetDownloadConfig(_split_ , _source_dir =None_, _classes =None_, _max_duration =None_, _copy_files =True_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `object`

Configuration class for downloading full or partial splits from the ActivityNet dataset.

**Attributes:**

`load_entire_split` |   
---|---  
  
**Methods:**

`validate`() |   
---|---  
`validate_split`() |   
`validate_max_duration`() |   
  
property load_entire_split#
    

validate()#
    

validate_split()#
    

validate_max_duration()#
    

class fiftyone.utils.activitynet.ActivityNetDatasetManager(_foz_dir_ , _version_)#
    

Bases: `object`

Class that manages the sample IDs and labels that need to be downloaded to load the specified subset of an ActivityNet dataset.

**Attributes:**

`info` |   
---|---  
`all_classes` |   
  
**Methods:**

`existing_split_sample_ids`(split) |   
---|---  
`split_sample_ids`(split) |   
`process_source`(source_dir,Â copy_files) |   
`download_necessary_samples`(config) |   
`write_data_json`(split) |   
`from_dataset_dir`(dataset_dir,Â version) |   
  
property info#
    

property all_classes#
    

existing_split_sample_ids(_split_)#
    

split_sample_ids(_split_)#
    

process_source(_source_dir_ , _copy_files_)#
    

download_necessary_samples(_config_)#
    

write_data_json(_split_)#
    

classmethod from_dataset_dir(_dataset_dir_ , _version_)#
    

class fiftyone.utils.activitynet.ActivityNetInfo(_raw_annotations_)#
    

Bases: `object`

Necessary information used to parse and format annotations.

**Methods:**

`get_matching_samples`([split,Â max_duration,Â ...]) |   
---|---  
`format_annotations`(sample_ids[,Â split]) |   
  
get_matching_samples(_split =None_, _max_duration =None_, _classes =None_, _ids =None_)#
    

format_annotations(_sample_ids_ , _split =None_)#
    

class fiftyone.utils.activitynet.ActivityNetSplitInfo(_split_dir_ , _version =None_, _raw_annotations =None_)#
    

Bases: `ActivityNetInfo`

Class that contains information related to paths, labels, and sample IDs of a single ActivityNet split.

**Attributes:**

`raw_anno_path` |   
---|---  
`data_dir` |   
`data_json_path` |   
`error_path` |   
  
**Methods:**

`update_existing_sample_ids`() |   
---|---  
`cleanup`() |   
`format_annotations`(sample_ids[,Â split]) |   
`get_matching_samples`([split,Â max_duration,Â ...]) |   
  
property raw_anno_path#
    

property data_dir#
    

property data_json_path#
    

property error_path#
    

update_existing_sample_ids()#
    

cleanup()#
    

format_annotations(_sample_ids_ , _split =None_)#
    

get_matching_samples(_split =None_, _max_duration =None_, _classes =None_, _ids =None_)#
    

class fiftyone.utils.activitynet.ActivityNetDatasetInfo(_foz_dir_)#
    

Bases: `ActivityNetInfo`

Class that stores information related to paths, labels, and sample IDs for an ActivityNet dataset download.

**Methods:**

`split_info`(split) |   
---|---  
`split_sample_ids`(split) |   
`existing_split_sample_ids`(split) |   
`split_dir`(split) |   
`data_dir`(split) |   
`data_json_path`(split) |   
`error_path`(split) |   
`update_existing_sample_ids`() |   
`cleanup_split`(split) |   
`get_dir_info`(dataset_dir) |   
`get_sample_split`(sample_id) |   
`get_sample_dataset_version`(sample_id) |   
`format_annotations`(sample_ids[,Â split]) |   
`get_matching_samples`([split,Â max_duration,Â ...]) |   
  
**Attributes:**

`splits` |   
---|---  
`version` |   
`dataset_dir` |   
`raw_anno_path` |   
  
split_info(_split_)#
    

property splits#
    

property version#
    

property dataset_dir#
    

property raw_anno_path#
    

split_sample_ids(_split_)#
    

existing_split_sample_ids(_split_)#
    

split_dir(_split_)#
    

data_dir(_split_)#
    

data_json_path(_split_)#
    

error_path(_split_)#
    

update_existing_sample_ids()#
    

cleanup_split(_split_)#
    

classmethod get_dir_info(_dataset_dir_)#
    

get_sample_split(_sample_id_)#
    

get_sample_dataset_version(_sample_id_)#
    

format_annotations(_sample_ids_ , _split =None_)#
    

get_matching_samples(_split =None_, _max_duration =None_, _classes =None_, _ids =None_)#
    

class fiftyone.utils.activitynet.ActivityNet100DatasetInfo(_foz_dir_)#
    

Bases: `ActivityNetDatasetInfo`

ActivityNet 100 dataset info.

**Attributes:**

`version` |   
---|---  
`dataset_dir` |   
`raw_anno_path` |   
`splits` |   
  
**Methods:**

`get_sample_dataset_version`(sample_id) |   
---|---  
`update_existing_sample_ids`() |   
`cleanup_split`(split) |   
`data_dir`(split) |   
`data_json_path`(split) |   
`error_path`(split) |   
`existing_split_sample_ids`(split) |   
`format_annotations`(sample_ids[,Â split]) |   
`get_dir_info`(dataset_dir) |   
`get_matching_samples`([split,Â max_duration,Â ...]) |   
`get_sample_split`(sample_id) |   
`split_dir`(split) |   
`split_info`(split) |   
`split_sample_ids`(split) |   
  
property version#
    

get_sample_dataset_version(_sample_id_)#
    

update_existing_sample_ids()#
    

cleanup_split(_split_)#
    

data_dir(_split_)#
    

data_json_path(_split_)#
    

property dataset_dir#
    

error_path(_split_)#
    

existing_split_sample_ids(_split_)#
    

format_annotations(_sample_ids_ , _split =None_)#
    

classmethod get_dir_info(_dataset_dir_)#
    

get_matching_samples(_split =None_, _max_duration =None_, _classes =None_, _ids =None_)#
    

get_sample_split(_sample_id_)#
    

property raw_anno_path#
    

split_dir(_split_)#
    

split_info(_split_)#
    

split_sample_ids(_split_)#
    

property splits#
    

class fiftyone.utils.activitynet.ActivityNet200DatasetInfo(_foz_dir_)#
    

Bases: `ActivityNetDatasetInfo`

ActivityNet 200 dataset info.

**Attributes:**

`version` |   
---|---  
`dataset_dir` |   
`raw_anno_path` |   
`splits` |   
  
**Methods:**

`get_sample_dataset_version`(sample_id) |   
---|---  
`update_existing_sample_ids`() |   
`cleanup_split`(split) |   
`data_dir`(split) |   
`data_json_path`(split) |   
`error_path`(split) |   
`existing_split_sample_ids`(split) |   
`format_annotations`(sample_ids[,Â split]) |   
`get_dir_info`(dataset_dir) |   
`get_matching_samples`([split,Â max_duration,Â ...]) |   
`get_sample_split`(sample_id) |   
`split_dir`(split) |   
`split_info`(split) |   
`split_sample_ids`(split) |   
  
property version#
    

get_sample_dataset_version(_sample_id_)#
    

update_existing_sample_ids()#
    

cleanup_split(_split_)#
    

data_dir(_split_)#
    

data_json_path(_split_)#
    

property dataset_dir#
    

error_path(_split_)#
    

existing_split_sample_ids(_split_)#
    

format_annotations(_sample_ids_ , _split =None_)#
    

classmethod get_dir_info(_dataset_dir_)#
    

get_matching_samples(_split =None_, _max_duration =None_, _classes =None_, _ids =None_)#
    

get_sample_split(_sample_id_)#
    

property raw_anno_path#
    

split_dir(_split_)#
    

split_info(_split_)#
    

split_sample_ids(_split_)#
    

property splits#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
