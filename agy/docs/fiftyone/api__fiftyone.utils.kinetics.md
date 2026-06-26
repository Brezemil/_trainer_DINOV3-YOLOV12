---
source_url: https://docs.voxel51.com/api/fiftyone.utils.kinetics.html
---

# fiftyone.utils.kinetics#

Utilities for working with the Kinetics dataset <https://deepmind.com/research/open-source/kinetics>.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_kinetics_split`(dataset_dir,Â split) | Utility that downloads full or partial splits of the [Kinetics dataset](https://deepmind.com/research/open-source/kinetics).  
---|---  
  
**Classes:**

`KineticsDatasetManager`(info) | Class that manages the sample IDs and labels that need to be downloaded as well as performing the actual downloading.  
---|---  
`KineticsDatasetDownloader`([num_workers]) | Clas that downloads and extracts Kinetics tars from AWS.  
`KineticsDownloadConfig`(split[,Â classes,Â ...]) | Config class for a Kinetics download run.  
`KineticsDatasetInfo`(kinetics_dir,Â ...) | Class that contains information such as paths, labels, and sample IDs for a Kinetics download.  
`Kinetics400DatasetInfo`(kinetics_dir,Â ...) | Kinetics 400-specific dataset info.  
`ClasswiseS3KineticsDatasetInfo`(kinetics_dir,Â ...) |   
`Kinetics600DatasetInfo`(kinetics_dir,Â ...) | Kinetics 600-specific dataset info.  
`Kinetics7002020DatasetInfo`(kinetics_dir,Â ...) | Kinetics 700-2020-specific dataset info.  
`Kinetics700DatasetInfo`(kinetics_dir,Â ...) | Kinetics 700-specific dataset info.  
  
fiftyone.utils.kinetics.download_kinetics_split(_dataset_dir_ , _split_ , _classes =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_, _retry_errors =False_, _scratch_dir =None_, _version ='700-2020'_)#
    

Utility that downloads full or partial splits of the [Kinetics dataset](https://deepmind.com/research/open-source/kinetics).

The downloaded splits are stored on disk in [VideoClassificationDirectoryTree format](user_guide__import_datasets.md#videoclassificationdirectorytree-import).

Parameters:
    

  * **dataset_dir** â the directory to download the dataset

  * **split** â the split to download. Supported values are `("train", "validation", "test")`

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual videos

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded

  * **retry_errors** (_False_) â whether to retry downloading samples from YouTube that have previously raised an error

  * **scratch_dir** (_None_) â a scratch directory to use to store temporary files

  * **version** (_"700-2020"_) â the version of the Kinetics dataset to download (â400â, â600â, â700â, or â700-2020â)



Returns:
    

a tuple of

  * **num_samples** : the total number of downloaded videos, or `None` if everything was already downloaded

  * **classes** : the list of all classes, or `None` if everything was already downloaded

  * **did_download** : whether any content was downloaded (True) or if all necessary files were already downloaded (False)




class fiftyone.utils.kinetics.KineticsDatasetManager(_info_)#
    

Bases: `object`

Class that manages the sample IDs and labels that need to be downloaded as well as performing the actual downloading.

**Methods:**

`download`(config,Â downloader) |   
---|---  
`download_partial_split`(config,Â downloader) |   
  
download(_config_ , _downloader_)#
    

download_partial_split(_config_ , _downloader_)#
    

class fiftyone.utils.kinetics.KineticsDatasetDownloader(_num_workers =None_)#
    

Bases: `object`

Clas that downloads and extracts Kinetics tars from AWS.

**Methods:**

`download_entire_split`(info) |   
---|---  
`download_classes`(info,Â classes) |   
  
download_entire_split(_info_)#
    

download_classes(_info_ , _classes_)#
    

class fiftyone.utils.kinetics.KineticsDownloadConfig(_split_ , _classes =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_, _retry_errors =False_)#
    

Bases: `object`

Config class for a Kinetics download run.

**Attributes:**

`load_entire_split` |   
---|---  
  
**Methods:**

`validate`() |   
---|---  
`validate_split`() |   
  
property load_entire_split#
    

validate()#
    

validate_split()#
    

class fiftyone.utils.kinetics.KineticsDatasetInfo(_kinetics_dir_ , _scratch_dir_ , _split_)#
    

Bases: `object`

Class that contains information such as paths, labels, and sample IDs for a Kinetics download.

**Attributes:**

`splits` |   
---|---  
`version` |   
`supports_classwise_s3_downloads` |   
`raw_dir` |   
`raw_anno_path` |   
`urls_s3_file` |   
`urls_filename` |   
`urls_path` |   
`error_path` |   
`prev_errors` |   
`loaded_tar_path` |   
`prev_loaded_tars` |   
`multisplit_urls` |   
`split_dir` |   
  
**Methods:**

`raw_anno_path_split`(split) |   
---|---  
`class_dir`(c) |   
`class_existing_sample_ids`(c) |   
`class_sample_ids`(c) |   
`id_from_filename`(video_fn) |   
`filename_from_id`(video_id) |   
`segment_from_id`(video_id) |   
`url_from_id`(video_id) |   
`id_from_url`(video_url) |   
`get_video_class`(video_id) |   
`cleanup_partial_downloads`() |   
`cleanup_excess_videos`() |   
`update_existing_sample_ids`() |   
`get_incomplete_classes`() |   
`validate_classes`(classes) |   
`get_kinetics_dir`(dataset_dir) |   
`build_for_version`(version,Â dataset_dir,Â ...) |   
  
property splits#
    

property version#
    

property supports_classwise_s3_downloads#
    

property raw_dir#
    

property raw_anno_path#
    

raw_anno_path_split(_split_)#
    

property urls_s3_file#
    

property urls_filename#
    

property urls_path#
    

property error_path#
    

property prev_errors#
    

property loaded_tar_path#
    

property prev_loaded_tars#
    

property multisplit_urls#
    

property split_dir#
    

class_dir(_c_)#
    

class_existing_sample_ids(_c_)#
    

class_sample_ids(_c_)#
    

id_from_filename(_video_fn_)#
    

filename_from_id(_video_id_)#
    

segment_from_id(_video_id_)#
    

url_from_id(_video_id_)#
    

id_from_url(_video_url_)#
    

get_video_class(_video_id_)#
    

cleanup_partial_downloads()#
    

cleanup_excess_videos()#
    

update_existing_sample_ids()#
    

get_incomplete_classes()#
    

validate_classes(_classes_)#
    

classmethod get_kinetics_dir(_dataset_dir_)#
    

classmethod build_for_version(_version_ , _dataset_dir_ , _scratch_dir_ , _split_)#
    

class fiftyone.utils.kinetics.Kinetics400DatasetInfo(_kinetics_dir_ , _scratch_dir_ , _split_)#
    

Bases: `KineticsDatasetInfo`

Kinetics 400-specific dataset info.

**Attributes:**

`supports_classwise_s3_downloads` |   
---|---  
`version` |   
`multisplit_urls` |   
`error_path` |   
`loaded_tar_path` |   
`prev_errors` |   
`prev_loaded_tars` |   
`raw_anno_path` |   
`raw_dir` |   
`split_dir` |   
`splits` |   
`urls_filename` |   
`urls_path` |   
`urls_s3_file` |   
  
**Methods:**

`build_for_version`(version,Â dataset_dir,Â ...) |   
---|---  
`class_dir`(c) |   
`class_existing_sample_ids`(c) |   
`class_sample_ids`(c) |   
`cleanup_excess_videos`() |   
`cleanup_partial_downloads`() |   
`filename_from_id`(video_id) |   
`get_incomplete_classes`() |   
`get_kinetics_dir`(dataset_dir) |   
`get_video_class`(video_id) |   
`id_from_filename`(video_fn) |   
`id_from_url`(video_url) |   
`raw_anno_path_split`(split) |   
`segment_from_id`(video_id) |   
`update_existing_sample_ids`() |   
`url_from_id`(video_id) |   
`validate_classes`(classes) |   
  
property supports_classwise_s3_downloads#
    

property version#
    

property multisplit_urls#
    

classmethod build_for_version(_version_ , _dataset_dir_ , _scratch_dir_ , _split_)#
    

class_dir(_c_)#
    

class_existing_sample_ids(_c_)#
    

class_sample_ids(_c_)#
    

cleanup_excess_videos()#
    

cleanup_partial_downloads()#
    

property error_path#
    

filename_from_id(_video_id_)#
    

get_incomplete_classes()#
    

classmethod get_kinetics_dir(_dataset_dir_)#
    

get_video_class(_video_id_)#
    

id_from_filename(_video_fn_)#
    

id_from_url(_video_url_)#
    

property loaded_tar_path#
    

property prev_errors#
    

property prev_loaded_tars#
    

property raw_anno_path#
    

raw_anno_path_split(_split_)#
    

property raw_dir#
    

segment_from_id(_video_id_)#
    

property split_dir#
    

property splits#
    

update_existing_sample_ids()#
    

url_from_id(_video_id_)#
    

property urls_filename#
    

property urls_path#
    

property urls_s3_file#
    

validate_classes(_classes_)#
    

class fiftyone.utils.kinetics.ClasswiseS3KineticsDatasetInfo(_kinetics_dir_ , _scratch_dir_ , _split_)#
    

Bases: `KineticsDatasetInfo`

**Attributes:**

`supports_classwise_s3_downloads` |   
---|---  
`error_path` |   
`loaded_tar_path` |   
`multisplit_urls` |   
`prev_errors` |   
`prev_loaded_tars` |   
`raw_anno_path` |   
`raw_dir` |   
`split_dir` |   
`splits` |   
`urls_filename` |   
`urls_path` |   
`urls_s3_file` |   
`version` |   
  
**Methods:**

`class_url`(c) |   
---|---  
`unloaded_class_urls`(classes) |   
`build_for_version`(version,Â dataset_dir,Â ...) |   
`class_dir`(c) |   
`class_existing_sample_ids`(c) |   
`class_sample_ids`(c) |   
`cleanup_excess_videos`() |   
`cleanup_partial_downloads`() |   
`filename_from_id`(video_id) |   
`get_incomplete_classes`() |   
`get_kinetics_dir`(dataset_dir) |   
`get_video_class`(video_id) |   
`id_from_filename`(video_fn) |   
`id_from_url`(video_url) |   
`raw_anno_path_split`(split) |   
`segment_from_id`(video_id) |   
`update_existing_sample_ids`() |   
`url_from_id`(video_id) |   
`validate_classes`(classes) |   
  
property supports_classwise_s3_downloads#
    

class_url(_c_)#
    

unloaded_class_urls(_classes_)#
    

classmethod build_for_version(_version_ , _dataset_dir_ , _scratch_dir_ , _split_)#
    

class_dir(_c_)#
    

class_existing_sample_ids(_c_)#
    

class_sample_ids(_c_)#
    

cleanup_excess_videos()#
    

cleanup_partial_downloads()#
    

property error_path#
    

filename_from_id(_video_id_)#
    

get_incomplete_classes()#
    

classmethod get_kinetics_dir(_dataset_dir_)#
    

get_video_class(_video_id_)#
    

id_from_filename(_video_fn_)#
    

id_from_url(_video_url_)#
    

property loaded_tar_path#
    

property multisplit_urls#
    

property prev_errors#
    

property prev_loaded_tars#
    

property raw_anno_path#
    

raw_anno_path_split(_split_)#
    

property raw_dir#
    

segment_from_id(_video_id_)#
    

property split_dir#
    

property splits#
    

update_existing_sample_ids()#
    

url_from_id(_video_id_)#
    

property urls_filename#
    

property urls_path#
    

property urls_s3_file#
    

validate_classes(_classes_)#
    

property version#
    

class fiftyone.utils.kinetics.Kinetics600DatasetInfo(_kinetics_dir_ , _scratch_dir_ , _split_)#
    

Bases: `ClasswiseS3KineticsDatasetInfo`

Kinetics 600-specific dataset info.

**Attributes:**

`version` |   
---|---  
`error_path` |   
`loaded_tar_path` |   
`multisplit_urls` |   
`prev_errors` |   
`prev_loaded_tars` |   
`raw_anno_path` |   
`raw_dir` |   
`split_dir` |   
`splits` |   
`supports_classwise_s3_downloads` |   
`urls_filename` |   
`urls_path` |   
`urls_s3_file` |   
  
**Methods:**

`build_for_version`(version,Â dataset_dir,Â ...) |   
---|---  
`class_dir`(c) |   
`class_existing_sample_ids`(c) |   
`class_sample_ids`(c) |   
`class_url`(c) |   
`cleanup_excess_videos`() |   
`cleanup_partial_downloads`() |   
`filename_from_id`(video_id) |   
`get_incomplete_classes`() |   
`get_kinetics_dir`(dataset_dir) |   
`get_video_class`(video_id) |   
`id_from_filename`(video_fn) |   
`id_from_url`(video_url) |   
`raw_anno_path_split`(split) |   
`segment_from_id`(video_id) |   
`unloaded_class_urls`(classes) |   
`update_existing_sample_ids`() |   
`url_from_id`(video_id) |   
`validate_classes`(classes) |   
  
property version#
    

classmethod build_for_version(_version_ , _dataset_dir_ , _scratch_dir_ , _split_)#
    

class_dir(_c_)#
    

class_existing_sample_ids(_c_)#
    

class_sample_ids(_c_)#
    

class_url(_c_)#
    

cleanup_excess_videos()#
    

cleanup_partial_downloads()#
    

property error_path#
    

filename_from_id(_video_id_)#
    

get_incomplete_classes()#
    

classmethod get_kinetics_dir(_dataset_dir_)#
    

get_video_class(_video_id_)#
    

id_from_filename(_video_fn_)#
    

id_from_url(_video_url_)#
    

property loaded_tar_path#
    

property multisplit_urls#
    

property prev_errors#
    

property prev_loaded_tars#
    

property raw_anno_path#
    

raw_anno_path_split(_split_)#
    

property raw_dir#
    

segment_from_id(_video_id_)#
    

property split_dir#
    

property splits#
    

property supports_classwise_s3_downloads#
    

unloaded_class_urls(_classes_)#
    

update_existing_sample_ids()#
    

url_from_id(_video_id_)#
    

property urls_filename#
    

property urls_path#
    

property urls_s3_file#
    

validate_classes(_classes_)#
    

class fiftyone.utils.kinetics.Kinetics7002020DatasetInfo(_kinetics_dir_ , _scratch_dir_ , _split_)#
    

Bases: `ClasswiseS3KineticsDatasetInfo`

Kinetics 700-2020-specific dataset info.

**Attributes:**

`version` |   
---|---  
`error_path` |   
`loaded_tar_path` |   
`multisplit_urls` |   
`prev_errors` |   
`prev_loaded_tars` |   
`raw_anno_path` |   
`raw_dir` |   
`split_dir` |   
`splits` |   
`supports_classwise_s3_downloads` |   
`urls_filename` |   
`urls_path` |   
`urls_s3_file` |   
  
**Methods:**

`class_url`(c) |   
---|---  
`build_for_version`(version,Â dataset_dir,Â ...) |   
`class_dir`(c) |   
`class_existing_sample_ids`(c) |   
`class_sample_ids`(c) |   
`cleanup_excess_videos`() |   
`cleanup_partial_downloads`() |   
`filename_from_id`(video_id) |   
`get_incomplete_classes`() |   
`get_kinetics_dir`(dataset_dir) |   
`get_video_class`(video_id) |   
`id_from_filename`(video_fn) |   
`id_from_url`(video_url) |   
`raw_anno_path_split`(split) |   
`segment_from_id`(video_id) |   
`unloaded_class_urls`(classes) |   
`update_existing_sample_ids`() |   
`url_from_id`(video_id) |   
`validate_classes`(classes) |   
  
property version#
    

class_url(_c_)#
    

classmethod build_for_version(_version_ , _dataset_dir_ , _scratch_dir_ , _split_)#
    

class_dir(_c_)#
    

class_existing_sample_ids(_c_)#
    

class_sample_ids(_c_)#
    

cleanup_excess_videos()#
    

cleanup_partial_downloads()#
    

property error_path#
    

filename_from_id(_video_id_)#
    

get_incomplete_classes()#
    

classmethod get_kinetics_dir(_dataset_dir_)#
    

get_video_class(_video_id_)#
    

id_from_filename(_video_fn_)#
    

id_from_url(_video_url_)#
    

property loaded_tar_path#
    

property multisplit_urls#
    

property prev_errors#
    

property prev_loaded_tars#
    

property raw_anno_path#
    

raw_anno_path_split(_split_)#
    

property raw_dir#
    

segment_from_id(_video_id_)#
    

property split_dir#
    

property splits#
    

property supports_classwise_s3_downloads#
    

unloaded_class_urls(_classes_)#
    

update_existing_sample_ids()#
    

url_from_id(_video_id_)#
    

property urls_filename#
    

property urls_path#
    

property urls_s3_file#
    

validate_classes(_classes_)#
    

class fiftyone.utils.kinetics.Kinetics700DatasetInfo(_kinetics_dir_ , _scratch_dir_ , _split_)#
    

Bases: `Kinetics7002020DatasetInfo`

Kinetics 700-specific dataset info.

**Attributes:**

`version` |   
---|---  
`urls_s3_file` |   
`error_path` |   
`loaded_tar_path` |   
`multisplit_urls` |   
`prev_errors` |   
`prev_loaded_tars` |   
`raw_anno_path` |   
`raw_dir` |   
`split_dir` |   
`splits` |   
`supports_classwise_s3_downloads` |   
`urls_filename` |   
`urls_path` |   
  
**Methods:**

`build_for_version`(version,Â dataset_dir,Â ...) |   
---|---  
`class_dir`(c) |   
`class_existing_sample_ids`(c) |   
`class_sample_ids`(c) |   
`class_url`(c) |   
`cleanup_excess_videos`() |   
`cleanup_partial_downloads`() |   
`filename_from_id`(video_id) |   
`get_incomplete_classes`() |   
`get_kinetics_dir`(dataset_dir) |   
`get_video_class`(video_id) |   
`id_from_filename`(video_fn) |   
`id_from_url`(video_url) |   
`raw_anno_path_split`(split) |   
`segment_from_id`(video_id) |   
`unloaded_class_urls`(classes) |   
`update_existing_sample_ids`() |   
`url_from_id`(video_id) |   
`validate_classes`(classes) |   
  
property version#
    

property urls_s3_file#
    

classmethod build_for_version(_version_ , _dataset_dir_ , _scratch_dir_ , _split_)#
    

class_dir(_c_)#
    

class_existing_sample_ids(_c_)#
    

class_sample_ids(_c_)#
    

class_url(_c_)#
    

cleanup_excess_videos()#
    

cleanup_partial_downloads()#
    

property error_path#
    

filename_from_id(_video_id_)#
    

get_incomplete_classes()#
    

classmethod get_kinetics_dir(_dataset_dir_)#
    

get_video_class(_video_id_)#
    

id_from_filename(_video_fn_)#
    

id_from_url(_video_url_)#
    

property loaded_tar_path#
    

property multisplit_urls#
    

property prev_errors#
    

property prev_loaded_tars#
    

property raw_anno_path#
    

raw_anno_path_split(_split_)#
    

property raw_dir#
    

segment_from_id(_video_id_)#
    

property split_dir#
    

property splits#
    

property supports_classwise_s3_downloads#
    

unloaded_class_urls(_classes_)#
    

update_existing_sample_ids()#
    

url_from_id(_video_id_)#
    

property urls_filename#
    

property urls_path#
    

validate_classes(_classes_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
