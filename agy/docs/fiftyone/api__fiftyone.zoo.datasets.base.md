---
source_url: https://docs.voxel51.com/api/fiftyone.zoo.datasets.base.html
---

# fiftyone.zoo.datasets.base#

FiftyOne Zoo Datasets provided natively by the library.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`FiftyOneDataset`() | Base class for zoo datasets that are provided natively by FiftyOne.  
---|---  
`ActivityNet100Dataset`([source_dir,Â classes,Â ...]) | ActivityNet is a large-scale video dataset for human activity understanding supporting the tasks of global video classification, trimmed activity classification, and temporal activity detection.  
`ActivityNet200Dataset`([source_dir,Â classes,Â ...]) | ActivityNet is a large-scale video dataset for human activity understanding supporting the tasks of global video classification, trimmed activity classification, and temporal activity detection.  
`BDD100KDataset`([source_dir,Â copy_files]) | The Berkeley Deep Drive (BDD) dataset is one of the largest and most diverse video datasets for autonomous vehicles.  
`Caltech101Dataset`() | The Caltech-101 dataset of images.  
`Caltech256Dataset`() | The Caltech-256 dataset of images.  
`CityscapesDataset`([source_dir,Â fine_annos,Â ...]) | Cityscapes is a large-scale dataset that contains a diverse set of stereo video sequences recorded in street scenes from 50 different cities, with high quality pixel-level annotations of 5,000 frames in addition to a larger set of 20,000 weakly annotated frames.  
`COCO2014Dataset`([label_types,Â classes,Â ...]) | COCO is a large-scale object detection, segmentation, and captioning dataset.  
`COCO2017Dataset`([label_types,Â classes,Â ...]) | COCO is a large-scale object detection, segmentation, and captioning dataset.  
`SamaCOCODataset`([label_types,Â classes,Â ...]) | Sama-COCO is a large-scale object detection, segmentation, and captioning dataset based on COCO2017.  
`FIWDataset`() | Families in the Wild is a public benchmark for recognizing families via facial images.  
`HMDB51Dataset`([fold]) | HMDB51 is an action recognition dataset containing a total of 6,766 clips distributed across 51 action classes.  
`ImageNetSampleDataset`() | A small sample of images from the ImageNet 2012 dataset.  
`Kinetics400Dataset`([classes,Â num_workers,Â ...]) | Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version.  
`Kinetics600Dataset`([classes,Â num_workers,Â ...]) | Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version.  
`Kinetics700Dataset`([classes,Â num_workers,Â ...]) | Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version.  
`Kinetics7002020Dataset`([classes,Â ...]) | Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version.  
`KITTIDataset`() | KITTI contains a suite of vision tasks built using an autonomous driving platform.  
`KITTIMultiviewDataset`() | KITTI contains a suite of vision tasks built using an autonomous driving platform.  
`LabeledFacesInTheWildDataset`() | Labeled Faces in the Wild is a public benchmark for face verification, also known as pair matching.  
`OpenImagesV6Dataset`([label_types,Â classes,Â ...]) | Open Images V6 is a dataset of ~9 million images, roughly 2 million of which are annotated and available via this zoo dataset.  
`OpenImagesV7Dataset`([label_types,Â classes,Â ...]) | Open Images V7 is a dataset of ~9 million images, roughly 2 million of which are annotated and available via this zoo dataset.  
`PlacesDataset`() | Places is a scene recognition dataset of 10 million images comprising ~400 unique scene categories.  
`QuickstartDataset`() | A small dataset with ground truth bounding boxes and predictions.  
`QuickstartGeoDataset`() | A small dataset with geolocation data.  
`QuickstartVideoDataset`() | A small video dataset with dense annotations.  
`QuickstartGroupsDataset`() | A small dataset with grouped image and point cloud data.  
`Quickstart3DDataset`() | A small 3D dataset with meshes, point clouds, and oriented bounding boxes.  
`UCF101Dataset`([fold]) | UCF101 is an action recognition data set of realistic action videos, collected from YouTube, having 101 action categories.  
  
class fiftyone.zoo.datasets.base.FiftyOneDataset#
    

Bases: [`ZooDataset`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDataset "fiftyone.zoo.datasets.ZooDataset")

Base class for zoo datasets that are provided natively by FiftyOne.

**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
**Attributes:**

`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
---|---  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`name` | The name of the dataset.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`tags` | A tuple of tags for the dataset.  
  
download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property name#
    

The name of the dataset.

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

property tags#
    

A tuple of tags for the dataset.

class fiftyone.zoo.datasets.base.ActivityNet100Dataset(_source_dir =None_, _classes =None_, _max_duration =None_, _copy_files =True_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

ActivityNet is a large-scale video dataset for human activity understanding supporting the tasks of global video classification, trimmed activity classification, and temporal activity detection.

This version contains videos and temporal activity detections for the 100 class version of the dataset.

Notes:

  * ActivityNet 100 and 200 differ in the number of activity classes and videos per split

  * Partial downloads will download videos (if still available) from YouTube

  * Full splits can be loaded by first downloading the official source files from the [ActivityNet maintainers](https://docs.google.com/forms/d/e/1FAIpQLSeKaFq9ZfcmZ7W0B0PbEhfbTHY41GeEgwsa7WobJgGUhn4DTQ/viewform)

  * The test set does not have annotations




Full split stats:

  * Train split: 4,819 videos (7,151 instances)

  * Test split: 2,480 videos (labels withheld)

  * Validation split: 2,383 videos (3,582 instances)




Partial downloads:

  * You can specify subsets of data to download via the `max_duration`, `classes`, and `max_samples` parameters




Full split downloads:

Many videos have been removed from YouTube since the creation of ActivityNet. As a result, if you do not specify any partial download parameters described below, you must first download the official source files from the ActivityNet maintainers in order to load a full split into FiftyOne.

To download the source files, you must fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeKaFq9ZfcmZ7W0B0PbEhfbTHY41GeEgwsa7WobJgGUhn4DTQ/viewform).

Refer to [this page](integrations__activitynet.md#activitynet-full-split-downloads) to see how to load full splits by passing the `source_dir` parameter to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset").

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 10 random samples from the validation split
    #
    # Only the required videos will be downloaded (if necessary)
    #
    
    dataset = foz.load_zoo_dataset(
        "activitynet-100",
        split="validation",
        max_samples=10,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load 10 samples from the validation split that
    # contain the actions "Bathing dog" and "Walking the dog"
    #
    # Videos that contain all `classes` will be prioritized first, followed
    # by videos that contain at least one of the required `classes`. If
    # there are not enough videos matching `classes` in the split to meet
    # `max_samples`, only the available videos will be loaded.
    #
    # Videos will only be downloaded if necessary
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any videos
    #
    
    dataset = foz.load_zoo_dataset(
        "activitynet-100",
        split="validation",
        classes=["Bathing dog", "Walking the dog"],
        max_samples=10,
    )
    
    session.dataset = dataset
    

Dataset size
    

223 GB

Source
    

<http://activity-net.org/index.html>

Parameters:
    

  * **source_dir** (_None_) â the directory containing the manually downloaded ActivityNet files used to avoid downloading videos from YouTube

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **max_duration** (_None_) â only videos with a duration in seconds that is less than or equal to the `max_duration` will be downloaded. By default, all videos are downloaded

  * **copy_files** (_True_) â whether to move (False) or create copies (True) of the source files when populating `dataset_dir`. This is only relevant when a `source_dir` is provided

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.ActivityNet200Dataset(_source_dir =None_, _classes =None_, _max_duration =None_, _copy_files =True_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

ActivityNet is a large-scale video dataset for human activity understanding supporting the tasks of global video classification, trimmed activity classification, and temporal activity detection.

This version contains videos and temporal activity detections for the 200 class version of the dataset.

Notes:

  * ActivityNet 200 is a superset of ActivityNet 100

  * ActivityNet 100 and 200 differ in the number of activity classes and videos per split

  * Partial downloads will download videos (if still available) from YouTube

  * Full splits can be loaded by first downloading the official source files from the [ActivityNet maintainers](https://docs.google.com/forms/d/e/1FAIpQLSeKaFq9ZfcmZ7W0B0PbEhfbTHY41GeEgwsa7WobJgGUhn4DTQ/viewform)

  * The test set does not have annotations




Full split stats:

  * Train split: 10,024 videos (15,410 instances)

  * Test split: 5,044 videos (labels withheld)

  * Validation split: 4,926 videos (7,654 instances)




Partial downloads:

  * You can specify subsets of data to download via the `max_duration`, `classes`, and `max_samples` parameters




Full split downloads:

Many videos have been removed from YouTube since the creation of ActivityNet. As a result, if you do not specify any partial download parameters described below, you must first download the official source files from the ActivityNet maintainers in order to load a full split into FiftyOne.

To download the source files, you must fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeKaFq9ZfcmZ7W0B0PbEhfbTHY41GeEgwsa7WobJgGUhn4DTQ/viewform).

Refer to [this page](integrations__activitynet.md#activitynet-full-split-downloads) to see how to load full splits by passing the `source_dir` parameter to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset").

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 10 random samples from the validation split
    #
    # Only the required videos will be downloaded (if necessary)
    #
    
    dataset = foz.load_zoo_dataset(
        "activitynet-200",
        split="validation",
        max_samples=10,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load 10 samples from the validation split that
    # contain the actions "Bathing dog" and "Walking the dog"
    #
    # Videos that contain all `classes` will be prioritized first, followed
    # by videos that contain at least one of the required `classes`. If
    # there are not enough videos matching `classes` in the split to meet
    # `max_samples`, only the available videos will be loaded.
    #
    # Videos will only be downloaded if necessary
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any videos
    #
    
    dataset = foz.load_zoo_dataset(
        "activitynet-200",
        split="validation",
        classes=["Bathing dog", "Walking the dog"],
        max_samples=10,
    )
    
    session.dataset = dataset
    

Dataset size
    

500 GB

Source
    

<http://activity-net.org/index.html>

Parameters:
    

  * **source_dir** (_None_) â the directory containing the manually downloaded ActivityNet files used to avoid downloading videos from YouTube

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **max_duration** (_None_) â only videos with a duration in seconds that is less than or equal to the max_duration will be downloaded. By default, all videos are downloaded

  * **copy_files** (_True_) â whether to move (False) or create copies (True) of the source files when populating `dataset_dir`. This is only relevant when a `source_dir` is provided

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.BDD100KDataset(_source_dir =None_, _copy_files =True_)#
    

Bases: `FiftyOneDataset`

The Berkeley Deep Drive (BDD) dataset is one of the largest and most diverse video datasets for autonomous vehicles.

The BDD100K dataset contains 100,000 video clips collected from more than 50,000 rides covering New York, San Francisco Bay Area, and other regions. The dataset contains diverse scene types such as city streets, residential areas, and highways. Furthermore, the videos were recorded in diverse weather conditions at different times of the day.

The videos are split into training (70K), validation (10K) and testing (20K) sets. Each video is 40 seconds long with 720p resolution and a frame rate of 30fps. The frame at the 10th second of each video is annotated for image classification, detection, and segmentation tasks.

This version of the dataset contains only the 100K images extracted from the videos as described above, together with the image classification, detection, and segmentation labels.

In order to load the BDD100K dataset, you must download the source data manually. The directory should be organized in the following format:
    
    
    source_dir/
        labels/
            bdd100k_labels_images_train.json
            bdd100k_labels_images_val.json
        images/
            100k/
                train/
                test/
                val/
    

You can register at <http://bdd-data.berkeley.edu> in order to get links to download the data.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # The path to the source files that you manually downloaded
    source_dir = "/path/to/dir-with-bdd100k-files"
    
    dataset = foz.load_zoo_dataset(
        "bdd100k",
        split="validation",
        source_dir=source_dir,
    )
    
    session = fo.launch_app(dataset)
    

Dataset size
    

7.10 GB

Source
    

<http://bdd-data.berkeley.edu>

Parameters:
    

  * **source_dir** (_None_) â the directory containing the manually downloaded BDD100K files

  * **copy_files** (_True_) â whether to move (False) or create copies (True) of the source files when populating the dataset directory




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.Caltech101Dataset#
    

Bases: `FiftyOneDataset`

The Caltech-101 dataset of images.

The dataset consists of pictures of objects belonging to 101 classes, plus one background clutter class (`BACKGROUND_Google`). Each image is labelled with a single object.

Each class contains roughly 40 to 800 images, totalling 9,144 images. Images are of variable sizes, with typical edge lengths of 200-300 pixels. This version contains image-level labels only.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("caltech101")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

138.60 MB

Source
    

<https://data.caltech.edu/records/mzrjq-6wc02>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.Caltech256Dataset#
    

Bases: `FiftyOneDataset`

The Caltech-256 dataset of images.

The dataset consists of pictures of objects belonging to 256 classes, plus one background clutter class (`clutter`). Each image is labelled with a single object.

Each class contains between 80 and 827 images, totalling 30,607 images. Images are of variable sizes, with typical edge lengths of 80-800 pixels.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("caltech256")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

1.16 GB

Source
    

<https://data.caltech.edu/records/nyy15-4j048>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.CityscapesDataset(_source_dir =None_, _fine_annos =None_, _coarse_annos =None_, _person_annos =None_)#
    

Bases: `FiftyOneDataset`

Cityscapes is a large-scale dataset that contains a diverse set of stereo video sequences recorded in street scenes from 50 different cities, with high quality pixel-level annotations of 5,000 frames in addition to a larger set of 20,000 weakly annotated frames.

The dataset is intended for:

  * Assessing the performance of vision algorithms for major tasks of semantic urban scene understanding: pixel-level, instance-level, and panoptic semantic labeling

  * Supporting research that aims to exploit large volumes of (weakly) annotated data, e.g. for training deep neural networks




In order to load the Cityscapes dataset, you must download the source data manually. The directory should be organized in the following format:
    
    
    source_dir/
        leftImg8bit_trainvaltest.zip
        gtFine_trainvaltest.zip             # optional
        gtCoarse.zip                        # optional
        gtBbox_cityPersons_trainval.zip     # optional
    

You can register at <https://www.cityscapes-dataset.com/register> in order to get links to download the data.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # The path to the source files that you manually downloaded
    source_dir = "/path/to/dir-with-cityscapes-files"
    
    dataset = foz.load_zoo_dataset(
        "cityscapes",
        split="validation",
        source_dir=source_dir,
    )
    
    session = fo.launch_app(dataset)
    

Dataset size
    

11.80 GB

Source
    

<https://www.cityscapes-dataset.com>

Parameters:
    

  * **source_dir** (_None_) â a directory containing the manually downloaded Cityscapes files

  * **fine_annos** (_None_) â whether to load the fine annotations (True), or not (False), or only if the ZIP file exists (None)

  * **coarse_annos** (_None_) â whether to load the coarse annotations (True), or not (False), or only if the ZIP file exists (None)

  * **person_annos** (_None_) â whether to load the personn detections (True), or not (False), or only if the ZIP file exists (None)




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.COCO2014Dataset(_label_types =None_, _classes =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

COCO is a large-scale object detection, segmentation, and captioning dataset.

This version contains images, bounding boxes, and segmentations for the 2014 version of the dataset.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the `label_types`, `classes`, and `max_samples` parameters

  * You can specify specific images to load via the `image_ids` parameter




See [this page](dataset_zoo__datasets__coco_2014.md#dataset-zoo-coco-2014) for more information about partial downloads of this dataset.

Full split stats:

  * Train split: 82,783 images

  * Test split: 40,775 images

  * Validation split: 40,504 images




Notes:

  * COCO defines 91 classes but the data only uses 80 classes

  * Some images from the train and validation sets donât have annotations

  * The test set does not have annotations

  * COCO 2014 and 2017 use the same images, but the splits are different




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 50 random samples from the validation split
    #
    # By default, only detections are loaded
    #
    
    dataset = foz.load_zoo_dataset(
        "coco-2014",
        split="validation",
        max_samples=50,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load segmentations for 25 samples from the validation split that
    # contain cats and dogs
    #
    # Images that contain all `classes` will be prioritized first, followed
    # by images that contain at least one of the required `classes`. If
    # there are not enough images matching `classes` in the split to meet
    # `max_samples`, only the available images will be loaded.
    #
    # Images will only be downloaded if necessary
    #
    
    dataset = foz.load_zoo_dataset(
        "coco-2014",
        split="validation",
        label_types=["segmentations"],
        classes=["cat", "dog"],
        max_samples=25,
    )
    
    session.dataset = dataset
    
    #
    # Download the entire validation split and load both detections and
    # segmentations
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any images
    #
    
    dataset = foz.load_zoo_dataset(
        "coco-2014",
        split="validation",
        label_types=["detections", "segmentations"],
    )
    
    session.dataset = dataset
    

Dataset size
    

37.57 GB

Source
    

<http://cocodataset.org/#home>

Parameters:
    

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "segmentations")`. By default, only âdetectionsâ are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` ints or strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `label_types` and/or `classes` are also specified, first priority will be given to samples that contain all of the specified label types and/or classes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.COCO2017Dataset(_label_types =None_, _classes =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

COCO is a large-scale object detection, segmentation, and captioning dataset.

This version contains images, bounding boxes, segmentations, and keypoints for the 2017 version of the dataset.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the `label_types`, `classes`, and `max_samples` parameters

  * You can specify specific images to load via the `image_ids` parameter




See [this page](dataset_zoo__datasets__coco_2017.md#dataset-zoo-coco-2017) for more information about partial downloads of this dataset.

Full split stats:

  * Train split: 118,287 images

  * Test split: 40,670 images

  * Validation split: 5,000 images




Notes:

  * COCO defines 91 classes but the data only uses 80 classes

  * Some images from the train and validation sets donât have annotations

  * The test set does not have annotations

  * COCO 2014 and 2017 use the same images, but the splits are different




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 50 random samples from the validation split
    #
    # By default, only detections are loaded
    #
    
    dataset = foz.load_zoo_dataset(
        "coco-2017",
        split="validation",
        max_samples=50,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load segmentations for 25 samples from the validation split that
    # contain cats and dogs
    #
    # Images that contain all `classes` will be prioritized first, followed
    # by images that contain at least one of the required `classes`. If
    # there are not enough images matching `classes` in the split to meet
    # `max_samples`, only the available images will be loaded.
    #
    # Images will only be downloaded if necessary
    #
    
    dataset = foz.load_zoo_dataset(
        "coco-2017",
        split="validation",
        label_types=["segmentations"],
        classes=["cat", "dog"],
        max_samples=25,
    )
    
    session.dataset = dataset
    
    #
    # Download the entire validation split and load both detections and
    # segmentations
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any images
    #
    
    dataset = foz.load_zoo_dataset(
        "coco-2017",
        split="validation",
        label_types=["detections", "segmentations"],
    )
    
    session.dataset = dataset
    

Dataset size
    

25.20 GB

Source
    

<http://cocodataset.org/#home>

Parameters:
    

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "segmentations")`. By default, only âdetectionsâ are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` ints or strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `label_types` and/or `classes` are also specified, first priority will be given to samples that contain all of the specified label types and/or classes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.SamaCOCODataset(_label_types =None_, _classes =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

Sama-COCO is a large-scale object detection, segmentation, and captioning dataset based on COCO2017. It is a relabeling of the original training and validation sets with tighter polygons and more individually annotated crowds.

This version contains images, bounding boxes and segmentations for Samaâs version of the 2017 version of the dataset.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the `label_types`, `classes`, and `max_samples` parameters

  * You can specify specific images to load via the `image_ids` parameter




See [this page](dataset_zoo__datasets__sama_coco.md#dataset-zoo-sama-coco) for more information about partial downloads of this dataset.

Full split stats:

  * Train split: 118,287 images

  * Test split: 40,670 images

  * Validation split: 5,000 images




Notes:

  * COCO defines 91 classes but the data only uses 80 classes

  * Some images from the train and validation sets donât have annotations

  * The test set does not have annotations

  * Sama-COCO may have some discrepancies with COCO-2017 in terms of the instances labeled




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 50 random samples from the validation split
    #
    # By default, only detections are loaded
    #
    
    dataset = foz.load_zoo_dataset(
        "sama-coco",
        split="validation",
        max_samples=50,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load segmentations for 25 samples from the validation split that
    # contain cats and dogs
    #
    # Images that contain all `classes` will be prioritized first, followed
    # by images that contain at least one of the required `classes`. If
    # there are not enough images matching `classes` in the split to meet
    # `max_samples`, only the available images will be loaded.
    #
    # Images will only be downloaded if necessary
    #
    
    dataset = foz.load_zoo_dataset(
        "sama-coco",
        split="validation",
        label_types=["segmentations"],
        classes=["cat", "dog"],
        max_samples=25,
    )
    
    session.dataset = dataset
    
    #
    # Download the entire validation split and load both detections and
    # segmentations
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any images
    #
    
    dataset = foz.load_zoo_dataset(
        "sama-coco",
        split="validation",
        label_types=["detections", "segmentations"],
    )
    
    session.dataset = dataset
    

Dataset size
    

25.67 GB

Source
    

<https://www.sama.com/sama-coco-dataset/>

Parameters:
    

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "segmentations")`. By default, only âdetectionsâ are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` ints or strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `label_types` and/or `classes` are also specified, first priority will be given to samples that contain all of the specified label types and/or classes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.FIWDataset#
    

Bases: `FiftyOneDataset`

Families in the Wild is a public benchmark for recognizing families via facial images. The dataset contains over 26,642 images of 5,037 faces collected from 978 families. A unique Family ID (FID) is assigned per family, ranging from F0001-F1018 (i.e., some families were merged or removed since its first release in 2016). The dataset is a continued work in progress. Any contributions are both welcome and appreciated!

Faces were cropped from imagery using the five-point face detector MTCNN from various phototypes (i.e., mostly family photos, along with several profile pics of individuals (facial shots). The number of members per family varies from 3-to-26, with the number of faces per subject ranging from 1 to >10.

Various levels and types of labels are associated with samples in this dataset. Family-level labels contain a list of members, each assigned a member ID (MID) unique to that respective family (e.g., F0011.MID2 refers to member 2 of family 11). Each member has annotations specifying gender and relationship to all other members in that respective family.

The relationships in FIW are:

> ID | Type  
> ---|---  
> 0 | not related or self  
> 1 | child  
> 2 | sibling  
> 3 | grandchild  
> 4 | parent  
> 5 | spouse  
> 6 | grandparent  
> 7 | great grandchild  
> 8 | great grandparent  
> 9 | TBD  
  
Within FiftyOne, each sample corresponds to a single face image and contains primitive labels of the Family ID, Member ID, etc. The relationship labels are stored as [multi-label classifications](https://docs.voxel51.com/user_guide/using_datasets.html#multilabel-classification), where each classification represents one relationship that the member has with another member in the family. The number of relationships will differ from one person to the next, but all faces of one person will have the same relationship labels.

Additionally, the labels for the [Kinship Verification task](https://competitions.codalab.org/competitions/21843) are also loaded into this dataset through FiftyOne. These labels are stored as classifications just like relationships, but the labels of kinship differ from those defined above. For example, rather than Parent, the label might be fd representing a Father-Daughter kinship or md for Mother-Daughter.

In order to make it easier to browse the dataset in the FiftyOne App, each sample also contains a face_id field containing a unique integer for each face of a member, always starting at 0. This allows you to filter the face_id field to 0 in the App to show only a single image of each person.

For your reference, the relationship labels are stored in disk in a matrix that provides the relationship of each member with other members of the family as well as names and genders. The i-th rows represent the i-th family memberâs relationship to the j-th other members.

For example, FID0001.csv contains:

> MID 1 2 3 Name Gender
>     
> 
> 1 0 4 5 name1 f 2 1 0 1 name2 f 3 5 4 0 name3 m

Here we have three family members, as listed under the MID column (far-left). Each MID reads across its row. We can see that MID1 is related to MID2 by 4 -> 1 (Parent -> Child), which of course can be viewed as the inverse, i.e., MID2 -> MID1 is 1 -> 4\. It can also be seen that MID1 and MID3 are spouses of one another, i.e., 5 -> 5.

Note

The spouse label will likely be removed in future version of this dataset. It serves no value to the problem of kinship.

For more information on the data (e.g., statistics, task evaluations, benchmarks, and more), see the recent journal:

> Robinson, JP, M. Shao, and Y. Fu. âSurvey on the Analysis and Modeling of Visual Kinship: A Decade in the Making.â IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI), 2021.

Note

For your convenience, FiftyOne provides [`get_pairwise_labels()`](api__fiftyone.utils.fiw.md#fiftyone.utils.fiw.get_pairwise_labels "fiftyone.utils.fiw.get_pairwise_labels") and [`get_identifier_filepaths_map()`](api__fiftyone.utils.fiw.md#fiftyone.utils.fiw.get_identifier_filepaths_map "fiftyone.utils.fiw.get_identifier_filepaths_map") utilities for FIW.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("fiw", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

173.00 MB

Source
    

<https://web.northeastern.edu/smilelab/fiw>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.HMDB51Dataset(_fold =1_)#
    

Bases: `FiftyOneDataset`

HMDB51 is an action recognition dataset containing a total of 6,766 clips distributed across 51 action classes.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("hmdb51", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

2.16 GB

Source
    

<https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database>

Parameters:
    

**fold** (_1_) â the test/train fold to use to arrange the files on disk. The supported values are `(1, 2, 3)`

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.ImageNetSampleDataset#
    

Bases: `FiftyOneDataset`

A small sample of images from the ImageNet 2012 dataset.

The dataset contains 1,000 images, one randomly chosen from each class of the validation split of the ImageNet 2012 dataset.

These images are provided according to the terms below:
    
    
    You have been granted access for non-commercial research/educational
    use. By accessing the data, you have agreed to the following terms.
    
    You (the "Researcher") have requested permission to use the ImageNet
    database (the "Database") at Princeton University and Stanford
    University. In exchange for such permission, Researcher hereby agrees
    to the following terms and conditions:
    
    1.  Researcher shall use the Database only for non-commercial research
        and educational purposes.
    2.  Princeton University and Stanford University make no
        representations or warranties regarding the Database, including but
        not limited to warranties of non-infringement or fitness for a
        particular purpose.
    3.  Researcher accepts full responsibility for his or her use of the
        Database and shall defend and indemnify Princeton University and
        Stanford University, including their employees, Trustees, officers
        and agents, against any and all claims arising from Researcher's
        use of the Database, including but not limited to Researcher's use
        of any copies of copyrighted images that he or she may create from
        the Database.
    4.  Researcher may provide research associates and colleagues with
        access to the Database provided that they first agree to be bound
        by these terms and conditions.
    5.  Princeton University and Stanford University reserve the right to
        terminate Researcher's access to the Database at any time.
    6.  If Researcher is employed by a for-profit, commercial entity,
        Researcher's employer shall also be bound by these terms and
        conditions, and Researcher hereby represents that he or she is
        fully authorized to enter into this agreement on behalf of such
        employer.
    7.  The law of the State of New Jersey shall apply to all disputes
        under this agreement.
    

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("imagenet-sample")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

98.26 MB

Source
    

<http://image-net.org>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.Kinetics400Dataset(_classes =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version. The videos include human-object interactions such as playing instruments, as well as human-human interactions such as shaking hands and hugging. Each action class has at least 400/600/700 video clips. Each clip is human annotated with a single action class and lasts around 10 seconds.

This dataset contains videos and action classifications for the 400 class version of the dataset.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the `classes` and `max_samples` parameters




See [this page](dataset_zoo__datasets__kinetics_400.md#dataset-zoo-kinetics-400) for more information about partial downloads of this dataset.

Original split stats:

  * Train split: 219,782 videos

  * Test split: 35,357 videos

  * Validation split: 18,035 videos




CVDF split stats:

  * Train split: 246,534 videos

  * Test split: 39,805 videos

  * Validation split: 19,906 videos




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 10 random samples from the validation split
    #
    # Only the required videos will be downloaded (if necessary).
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-400",
        split="validation",
        max_samples=10,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load 10 samples from the validation split that
    # contain the actions "springboard diving" and "surfing water"
    #
    # Videos that contain all `classes` will be prioritized first, followed
    # by videos that contain at least one of the required `classes`. If
    # there are not enough videos matching `classes` in the split to meet
    # `max_samples`, only the available videos will be loaded.
    #
    # Videos will only be downloaded if necessary
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any videos
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-400",
        split="validation",
        classes=["springboard diving", "surfing water"],
        max_samples=10,
    )
    
    session.dataset = dataset
    

Dataset size

  * Train split: 370 GB

  * Test split: 56 GB

  * Validation split: 30 GB




Source
    

<https://deepmind.com/research/open-source/kinetics>

Parameters:
    

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.Kinetics600Dataset(_classes =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version. The videos include human-object interactions such as playing instruments, as well as human-human interactions such as shaking hands and hugging. Each action class has at least 400/600/700 video clips. Each clip is human annotated with a single action class and lasts around 10 seconds.

This dataset contains videos and action classifications for the 600 class version of the dataset.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the `classes` and `max_samples` parameters




See [this page](dataset_zoo__datasets__kinetics_600.md#dataset-zoo-kinetics-600) for more information about partial downloads of this dataset.

Original split stats:

  * Train split: 370,582 videos

  * Test split: 56,618 videos

  * Validation split: 28,313 videos




CVDF split stats:

  * Train split: 427,549 videos

  * Test split: 72,924 videos

  * Validation split: 29,793 videos




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 10 random samples from the validation split
    #
    # Only the required videos will be downloaded (if necessary).
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-600",
        split="validation",
        max_samples=10,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load 10 samples from the validation split that
    # contain the actions "springboard diving" and "surfing water"
    #
    # Videos that contain all `classes` will be prioritized first, followed
    # by videos that contain at least one of the required `classes`. If
    # there are not enough videos matching `classes` in the split to meet
    # `max_samples`, only the available videos will be loaded.
    #
    # Videos will only be downloaded if necessary
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any videos
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-600",
        split="validation",
        classes=["springboard diving", "surfing water"],
        max_samples=10,
    )
    
    session.dataset = dataset
    

Dataset size

  * Train split: 648 GB

  * Test split: 88 GB

  * Validation split: 43 GB




Source
    

<https://deepmind.com/research/open-source/kinetics>

Parameters:
    

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.Kinetics700Dataset(_classes =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version. The videos include human-object interactions such as playing instruments, as well as human-human interactions such as shaking hands and hugging. Each action class has at least 400/600/700 video clips. Each clip is human annotated with a single action class and lasts around 10 seconds.

This dataset contains videos and action classifications for the 700 class version of the dataset.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the `classes` and `max_samples` parameters




See [this page](dataset_zoo__datasets__kinetics_700.md#dataset-zoo-kinetics-700) for more information about partial downloads of this dataset.

Original split stats:

  * Train split: 529,046 videos

  * Test split: 67,446 videos

  * Validation split: 33,925 videos




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 10 random samples from the validation split
    #
    # Only the required videos will be downloaded (if necessary).
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-700",
        split="validation",
        max_samples=10,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load 10 samples from the validation split that
    # contain the actions "springboard diving" and "surfing water"
    #
    # Videos that contain all `classes` will be prioritized first, followed
    # by videos that contain at least one of the required `classes`. If
    # there are not enough videos matching `classes` in the split to meet
    # `max_samples`, only the available videos will be loaded.
    #
    # Videos will only be downloaded if necessary
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any videos
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-700",
        split="validation",
        classes=["springboard diving", "surfing water"],
        max_samples=10,
    )
    
    session.dataset = dataset
    

Dataset size

  * Train split: 603 GB

  * Test split: 59 GB

  * Validation split: 48 GB




Source
    

<https://deepmind.com/research/open-source/kinetics>

Parameters:
    

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.Kinetics7002020Dataset(_classes =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version. The videos include human-object interactions such as playing instruments, as well as human-human interactions such as shaking hands and hugging. Each action class has at least 400/600/700 video clips. Each clip is human annotated with a single action class and lasts around 10 seconds.

This version contains videos and action classifications for the 700 class version of the dataset that was updated with new videos in 2020. This dataset is a superset of Kinetics 700.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the `classes` and `max_samples` parameters




See [this page](dataset_zoo__datasets__kinetics_700_2020.md#dataset-zoo-kinetics-700-2020) for more information about partial downloads of this dataset.

Original split stats:

  * Train split: 542,352 videos

  * Test split: 67,433 videos

  * Validation split: 34,125 videos




CVDF split stats:

  * Train split: 534,073 videos

  * Test split: 64,260 videos

  * Validation split: 33,914 videos




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    #
    # Load 10 random samples from the validation split
    #
    # Only the required videos will be downloaded (if necessary).
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-700-2020",
        split="validation",
        max_samples=10,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load 10 samples from the validation split that
    # contain the actions "springboard diving" and "surfing water"
    #
    # Videos that contain all `classes` will be prioritized first, followed
    # by videos that contain at least one of the required `classes`. If
    # there are not enough videos matching `classes` in the split to meet
    # `max_samples`, only the available videos will be loaded.
    #
    # Videos will only be downloaded if necessary
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any videos
    #
    
    dataset = foz.load_zoo_dataset(
        "kinetics-700-2020",
        split="validation",
        classes=["springboard diving", "surfing water"],
        max_samples=10,
    )
    
    session.dataset = dataset
    

Dataset size

  * Train split: 603 GB

  * Test split: 59 GB

  * Validation split: 48 GB




Source
    

<https://deepmind.com/research/open-source/kinetics>

Parameters:
    

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.KITTIDataset#
    

Bases: `FiftyOneDataset`

KITTI contains a suite of vision tasks built using an autonomous driving platform.

This dataset contains the left camera images and the associated 2D object detections.

The training split contains 7,481 annotated images, and the test split contains 7,518 unlabeled images.

A full description of the annotations can be found in the README of the object development kit on the KITTI homepage.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("kitti", split="train")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

12.57 GB

Source
    

<http://www.cvlibs.net/datasets/kitti>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.KITTIMultiviewDataset#
    

Bases: `FiftyOneDataset`

KITTI contains a suite of vision tasks built using an autonomous driving platform.

This dataset contains the following multiview data for each scene:

  * Left camera images annotated with 2D object detections

  * Right camera images annotated with 2D object detections

  * Velodyne LIDAR point clouds annotated with 3D object detections




The training split contains 7,481 annotated scenes, and the test split contains 7,518 unlabeled scenes.

A full description of the annotations can be found in the README of the object development kit on the KITTI homepage.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("kitti-multiview", split="train")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

53.34 GB

Source
    

<http://www.cvlibs.net/datasets/kitti>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.LabeledFacesInTheWildDataset#
    

Bases: `FiftyOneDataset`

Labeled Faces in the Wild is a public benchmark for face verification, also known as pair matching.

The dataset contains 13,233 images of 5,749 peopleâs faces collected from the web. Each face has been labeled with the name of the person pictured. 1,680 of the people pictured have two or more distinct photos in the data set. The only constraint on these faces is that they were detected by the Viola-Jones face detector.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("lfw", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

173.00 MB

Source
    

<http://vis-www.cs.umass.edu/lfw>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.OpenImagesV6Dataset(_label_types =None_, _classes =None_, _attrs =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

Open Images V6 is a dataset of ~9 million images, roughly 2 million of which are annotated and available via this zoo dataset.

The dataset contains annotations for classification, detection, segmentation, and visual relationship tasks for the 600 boxable object classes.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the``label_types``, `classes`, `attrs`, and `max_samples` parameters

  * You can specify specific images to load via the `image_ids` parameter




See [this page](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) for more information about partial downloads of this dataset.

Full split stats:

  * Train split: 1,743,042 images (513 GB)

  * Test split: 125,436 images (36 GB)

  * Validation split: 41,620 images (12 GB)




Notes:

  * Not all images contain all types of labels

  * All images have been rescaled so that their largest dimension is at most 1024 pixels




Example usage:
    
    
    #
    # Load 50 random samples from the validation split
    #
    # By default, all label types are loaded
    #
    
    dataset = foz.load_zoo_dataset(
        "open-images-v6",
        split="validation",
        max_samples=50,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load detections and classifications for 25 samples from the
    # validation split that contain fedoras and pianos
    #
    # Images that contain all `label_types` and `classes` will be
    # prioritized first, followed by images that contain at least one of
    # the required `classes`. If there are not enough images matching
    # `classes` in the split to meet `max_samples`, only the available
    # images will be loaded.
    #
    # Images will only be downloaded if necessary
    #
    
    dataset = foz.load_zoo_dataset(
        "open-images-v6",
        split="validation",
        label_types=["detections", "classifications"],
        classes=["Fedora", "Piano"],
        max_samples=25,
    )
    
    session.dataset = dataset
    
    #
    # Download the entire validation split and load detections
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any images
    #
    
    dataset = foz.load_zoo_dataset(
        "open-images-v6",
        split="validation",
        label_types=["detections"],
    )
    
    session.dataset = dataset
    

Dataset size
    

561 GB

Source
    

<https://storage.googleapis.com/openimages/web/index.html>

Parameters:
    

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "classifications", "relationships", "segmentations")`. By default, all label types are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **attrs** (_None_) â a string or list of strings specifying required relationship attributes to load. Only applicable when `label_types` includes ârelationshipsâ. If provided, only samples containing at least one instance of a specified attribute will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `label_types`, `classes`, and/or `attrs` are also specified, first priority will be given to samples that contain all of the specified label types, classes, and/or attributes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.OpenImagesV7Dataset(_label_types =None_, _classes =None_, _attrs =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Bases: `FiftyOneDataset`

Open Images V7 is a dataset of ~9 million images, roughly 2 million of which are annotated and available via this zoo dataset.

The dataset contains annotations for classification, detection, segmentation, point labels, and visual relationship tasks for the 600 boxable object classes.

This dataset supports partial downloads:

  * You can specify subsets of data to download via the``label_types``, `classes`, `attrs`, and `max_samples` parameters

  * You can specify specific images to load via the `image_ids` parameter




See [this page](dataset_zoo__datasets__open_images_v6.md#dataset-zoo-open-images-v6) for more information about partial downloads of this dataset.

Full split stats:

  * Train split: 1,743,042 images (513 GB)

  * Test split: 125,436 images (36 GB)

  * Validation split: 41,620 images (12 GB)




Notes:

  * Not all images contain all types of labels

  * All images have been rescaled so that their largest dimension is at most 1024 pixels




Example usage:
    
    
    #
    # Load 50 random samples from the validation split
    #
    # By default, all label types are loaded, including "points"
    #
    
    dataset = foz.load_zoo_dataset(
        "open-images-v7",
        split="validation",
        max_samples=50,
        shuffle=True,
    )
    
    session = fo.launch_app(dataset)
    
    #
    # Load detections, classifications, and points for 25 samples from the
    # validation split that contain fedoras and pianos
    #
    # Images that contain all `label_types` and `classes` will be
    # prioritized first, followed by images that contain at least one of
    # the required `classes`. If there are not enough images matching
    # `classes` in the split to meet `max_samples`, only the available
    # images will be loaded.
    #
    # Images will only be downloaded if necessary
    #
    
    dataset = foz.load_zoo_dataset(
        "open-images-v7",
        split="validation",
        label_types=["detections", "classifications", "points"],
        classes=["Fedora", "Piano"],
        max_samples=25,
    )
    
    session.dataset = dataset
    
    #
    # Download the entire validation split and load detections
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any images
    #
    
    dataset = foz.load_zoo_dataset(
        "open-images-v7",
        split="validation",
        label_types=["detections"],
    )
    
    session.dataset = dataset
    

Dataset size
    

561 GB

Source
    

<https://storage.googleapis.com/openimages/web/index.html>

Parameters:
    

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "classifications", "points", "relationships", "segmentations")`. By default, all label types are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **attrs** (_None_) â a string or list of strings specifying required relationship attributes to load. Only applicable when `label_types` includes ârelationshipsâ. If provided, only samples containing at least one instance of a specified attribute will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **num_workers** (_None_) â a suggested number of threads to use when downloading individual images

  * **shuffle** (_False_) â whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load per split. If `label_types`, `classes`, and/or `attrs` are also specified, first priority will be given to samples that contain all of the specified label types, classes, and/or attributes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.PlacesDataset#
    

Bases: `FiftyOneDataset`

Places is a scene recognition dataset of 10 million images comprising ~400 unique scene categories.

The images are labeled with scene semantic categories, comprising a large and diverse list of the types of environments encountered in the world.

Full split stats:

  * Train split: 1,803,460 images, with between 3,068 and 5,000 per category

  * Test split: 328,500 images, with 900 images per category

  * Validation split: 36,500 images, with 100 images per category




Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("places", split="validation")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

29 GB

Source
    

<http://places2.csail.mit.edu/download-private.html>

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

class fiftyone.zoo.datasets.base.QuickstartDataset#
    

Bases: `FiftyOneDataset`

A small dataset with ground truth bounding boxes and predictions.

The dataset consists of 200 images from the validation split of COCO-2017, with model predictions generated by an out-of-the-box Faster R-CNN model from [torchvision.models](https://pytorch.org/docs/stable/torchvision/models.html).

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

23.40 MB

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.QuickstartGeoDataset#
    

Bases: `FiftyOneDataset`

A small dataset with geolocation data.

The dataset consists of 500 images from the validation split of the BDD100K dataset in the New York City area with object detections and GPS timestamps.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-geo")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

33.50 MB

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.QuickstartVideoDataset#
    

Bases: `FiftyOneDataset`

A small video dataset with dense annotations.

The dataset consists of 10 video segments with dense object detections generated by human annotators.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

35.20 MB

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.QuickstartGroupsDataset#
    

Bases: `FiftyOneDataset`

A small dataset with grouped image and point cloud data.

The dataset consists of 200 scenes from the train split of the KITTI dataset, each containing left camera, right camera, point cloud, and 2D/3D object annotation data.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-groups")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

576 MB

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.Quickstart3DDataset#
    

Bases: `FiftyOneDataset`

A small 3D dataset with meshes, point clouds, and oriented bounding boxes.

The dataset consists of 200 3D mesh samples from the test split of the [ModelNet40](https://modelnet.cs.princeton.edu) dataset, with point clouds generated using a Poisson disk sampling method, and oriented bounding boxes generated based on the convex hull.

Objects have been rescaled and recentered from the original dataset.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-3d")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

215.7 MB

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

class fiftyone.zoo.datasets.base.UCF101Dataset(_fold =1_)#
    

Bases: `FiftyOneDataset`

UCF101 is an action recognition data set of realistic action videos, collected from YouTube, having 101 action categories. This data set is an extension of UCF50 data set which has 50 action categories.

With 13,320 videos from 101 action categories, UCF101 gives the largest diversity in terms of actions and with the presence of large variations in camera motion, object appearance and pose, object scale, viewpoint, cluttered background, illumination conditions, etc, it is the most challenging data set to date. As most of the available action recognition data sets are not realistic and are staged by actors, UCF101 aims to encourage further research into action recognition by learning and exploring new realistic action categories.

The videos in 101 action categories are grouped into 25 groups, where each group can consist of 4-7 videos of an action. The videos from the same group may share some common features, such as similar background, similar viewpoint, etc.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("ucf101", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

6.48 GB

Source
    

<https://www.crcv.ucf.edu/research/data-sets/ucf101>

Parameters:
    

**fold** (_1_) â the test/train fold to use to arrange the files on disk. The supported values are `(1, 2, 3)`

**Attributes:**

`name` | The name of the dataset.  
---|---  
`license` | The license or list,of,licenses under which the dataset is distributed, or None if unknown.  
`tags` | A tuple of tags for the dataset.  
`parameters` | An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.  
`supported_splits` | A tuple of supported splits for the dataset, or None if the dataset does not have splits.  
`has_patches` | Whether the dataset has patches that may need to be applied to already downloaded files.  
`has_splits` | Whether the dataset has splits.  
`has_tags` | Whether the dataset has tags.  
`importer_kwargs` | A dict of default kwargs to pass to this dataset's [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").  
`is_remote` | Whether the dataset is remotely-sourced.  
`requires_manual_download` | Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.  
`supports_partial_downloads` | Whether the dataset supports downloading partial subsets of its splits.  
  
**Methods:**

`download_and_prepare`(dataset_dir[,Â split,Â ...]) | Downloads the dataset and prepares it for use.  
---|---  
`get_info_path`(dataset_dir) | Returns the path to the `ZooDatasetInfo` for the dataset.  
`get_split_dir`(dataset_dir,Â split) | Returns the directory for the given split of the dataset.  
`has_info`(dataset_dir) | Determines whether the directory contains `ZooDatasetInfo`.  
`has_split`(split) | Whether the dataset has the given split.  
`has_tag`(tag) | Whether the dataset has the given tag.  
`load_info`(dataset_dir[,Â upgrade,Â ...]) | Loads the `ZooDatasetInfo` from the given dataset directory.  
  
property name#
    

The name of the dataset.

property license#
    

The license or list,of,licenses under which the dataset is distributed, or None if unknown.

property tags#
    

A tuple of tags for the dataset.

property parameters#
    

An optional dict of parameters describing the configuration of the zoo dataset when it was downloaded.

property supported_splits#
    

A tuple of supported splits for the dataset, or None if the dataset does not have splits.

download_and_prepare(_dataset_dir_ , _split =None_, _splits =None_, _cleanup =True_)#
    

Downloads the dataset and prepares it for use.

If the requested splits have already been downloaded, they are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **split** (_None_) â `split` nor `splits` are provided, the full dataset is downloaded

  * **splits** (_None_) â a list of splits to download, if applicable. If neither `split` nor `splits` are provided, the full dataset is downloaded

  * **cleanup** (_True_) â whether to cleanup any temporary files generated during download



Returns:
    

the `ZooDatasetInfo` for the dataset

static get_info_path(_dataset_dir_)#
    

Returns the path to the `ZooDatasetInfo` for the dataset.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

the path to the `ZooDatasetInfo`

get_split_dir(_dataset_dir_ , _split_)#
    

Returns the directory for the given split of the dataset.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **split** â the dataset split



Returns:
    

the directory that will/does hold the specified split

static has_info(_dataset_dir_)#
    

Determines whether the directory contains `ZooDatasetInfo`.

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

True/False

property has_patches#
    

Whether the dataset has patches that may need to be applied to already downloaded files.

has_split(_split_)#
    

Whether the dataset has the given split.

Parameters:
    

**split** â the dataset split

Returns:
    

True/False

property has_splits#
    

Whether the dataset has splits.

has_tag(_tag_)#
    

Whether the dataset has the given tag.

Parameters:
    

**tag** â the tag

Returns:
    

True/False

property has_tags#
    

Whether the dataset has tags.

property importer_kwargs#
    

A dict of default kwargs to pass to this datasetâs [`fiftyone.utils.data.importers.DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter").

property is_remote#
    

Whether the dataset is remotely-sourced.

static load_info(_dataset_dir_ , _upgrade =True_, _warn_deprecated =False_)#
    

Loads the `ZooDatasetInfo` from the given dataset directory.

Parameters:
    

  * **dataset_dir** â the directory in which to construct the dataset

  * **upgrade** (_True_) â whether to upgrade the JSON file on disk if any migrations were necessary

  * **warn_deprecated** (_False_) â whether to issue a warning if the dataset has a deprecated format



Returns:
    

the `ZooDatasetInfo` for the dataset

property requires_manual_download#
    

Whether this dataset requires some files to be manually downloaded by the user before the dataset can be loaded.

property supports_partial_downloads#
    

Whether the dataset supports downloading partial subsets of its splits.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
