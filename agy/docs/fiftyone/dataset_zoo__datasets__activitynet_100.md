---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/activitynet_100.html
---

# ActivityNet 100#

ActivityNet is a large-scale video dataset for human activity understanding supporting the tasks of global video classification, trimmed activity classification, and temporal activity detection.

This version contains videos and temporal activity detections for the 100 class version of the dataset.

Note

Check out [this guide](integrations__activitynet.md#activitynet) for more details on using FiftyOne to work with ActivityNet.

**Notes**

  * ActivityNet 100 and 200 differ in the number of activity classes and videos per split

  * Partial downloads will download videos (if still available) from YouTube

  * Full splits can be loaded by first downloading the official source files from the [ActivityNet maintainers](https://docs.google.com/forms/d/e/1FAIpQLSeKaFq9ZfcmZ7W0B0PbEhfbTHY41GeEgwsa7WobJgGUhn4DTQ/viewform)

  * The test set does not have annotations




**Details**

  * Dataset name: `activitynet-100`

  * Dataset source: <http://activity-net.org/index.html>

  * Dataset license: CC-BY-4.0

  * Dataset size: 223 GB

  * Tags: `video, classification, action-recognition, temporal-detection`

  * Supported splits: `train, validation, test`

  * ZooDataset class: [`ActivityNet100Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.ActivityNet100Dataset "fiftyone.zoo.datasets.base.ActivityNet100Dataset")




**Full split stats**

  * Train split: 4,819 videos (7,151 instances)

  * Test split: 2,480 videos (labels withheld)

  * Validation split: 2,383 videos (3,582 instances)




**Partial downloads**

FiftyOne provides parameters that can be used to efficiently download specific subsets of the ActivityNet dataset to suit your needs. When new subsets are specified, FiftyOne will use existing downloaded data first if possible before resorting to downloading additional data from YouTube.

The following parameters are available to configure a partial download of ActivityNet 100 by passing them to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset"):

  * **split** (_None_) and **splits** (_None_): a string or list of strings, respectively, specifying the splits to load. Supported values are `("train", "test", "validation")`. If none are provided, all available splits are loaded

  * **source_dir** (_None_): the directory containing the manually downloaded ActivityNet files used to avoid downloading videos from YouTube

  * **classes** (_None_): a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **max_duration** (_None_): only videos with a duration in seconds that is less than or equal to the `max_duration` will be downloaded. By default, all videos are downloaded

  * **copy_files** (_True_): whether to move (False) or create copies (True) of the source files when populating `dataset_dir`. This is only relevant when a `source_dir` is provided

  * **num_workers** (_None_): the number of processes to use when downloading individual videos. By default, `multiprocessing.cpu_count()` is used

  * **shuffle** (_False_): whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_): a random seed to use when shuffling

  * **max_samples** (_None_): a maximum number of samples to load per split. If `classes` are also specified, only up to the number of samples that contain at least one specified class will be loaded. By default, all matching samples are loaded




Note

See [`ActivityNet100Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.ActivityNet100Dataset "fiftyone.zoo.datasets.base.ActivityNet100Dataset") and [`ActivityNetDatasetImporter`](api__fiftyone.utils.activitynet.md#fiftyone.utils.activitynet.ActivityNetDatasetImporter "fiftyone.utils.activitynet.ActivityNetDatasetImporter") for complete descriptions of the optional keyword arguments that you can pass to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset").

**Full split downloads**

Many videos have been removed from YouTube since the creation of ActivityNet. As a result, if you do not specify any partial download parameters defined in the previous section, you must first download the official source files from the ActivityNet maintainers in order to load a full split into FiftyOne.

To download the source files, you must fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeKaFq9ZfcmZ7W0B0PbEhfbTHY41GeEgwsa7WobJgGUhn4DTQ/viewform).

Refer to [this page](integrations__activitynet.md#activitynet-full-split-downloads) to see how to load full splits by passing the `source_dir` parameter to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset").

**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4#
     5# Load 10 random samples from the validation split
     6#
     7# Only the required videos will be downloaded (if necessary)
     8#
     9
    10dataset = foz.load_zoo_dataset(
    11    "activitynet-100",
    12    split="validation",
    13    max_samples=10,
    14    shuffle=True,
    15)
    16
    17session = fo.launch_app(dataset)
    18
    19#
    20# Load 10 samples from the validation split that
    21# contain the actions "Bathing dog" and "Walking the dog"
    22#
    23# Videos that contain all `classes` will be prioritized first, followed
    24# by videos that contain at least one of the required `classes`. If
    25# there are not enough videos matching `classes` in the split to meet
    26# `max_samples`, only the available videos will be loaded.
    27#
    28# Videos will only be downloaded if necessary
    29#
    30# Subsequent partial loads of the validation split will never require
    31# downloading any videos
    32#
    33
    34dataset = foz.load_zoo_dataset(
    35    "activitynet-100",
    36    split="validation",
    37    classes=["Bathing dog", "Walking the dog"],
    38    max_samples=10,
    39)
    40
    41session.dataset = dataset
    
    
    
    #
    # Load 10 random samples from the validation split
    #
    # Only the required videos will be downloaded (if necessary)
    #
    
    fiftyone zoo datasets load activitynet-100 \
        --split validation \
        --kwargs max_samples=10
    
    fiftyone app launch activitynet-100-validation-10
    
    #
    # Load 10 samples from the validation split that
    # contain the actions "Archery" and "Cricket"
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
    
    fiftyone zoo datasets load activitynet-100 \
        --split validation \
        --kwargs \
            classes=Archery,Cricket \
            max_samples=10
    
    fiftyone app launch activitynet-100-validation-10
    

Note

In order to work with video datasets, youâll need to have [ffmpeg installed](installation__troubleshooting.md#troubleshooting-video).

![activitynet-100-validation](../../_images/activitynet-100-validation.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
