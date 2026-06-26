---
source_url: https://docs.voxel51.com/dataset_zoo/datasets/open_images_v6.html
---

# Open Images V6#

Open Images V6 is a dataset of ~9 million images, roughly 2 million of which are annotated and available via this zoo dataset.

The dataset contains annotations for classification, detection, segmentation, and visual relationship tasks for the 600 boxable classes.

Note

Weâve collaborated with the [Open Images Team at Google](https://storage.googleapis.com/openimages/web/download.html) to make FiftyOne a recommended tool for downloading, visualizing, and evaluating on the Open Images Dataset!

Check out [this guide](integrations__open_images.md#open-images) for more details on using FiftyOne to work with Open Images.

**Details**

  * Dataset name: `open-images-v6`

  * Dataset source: <https://storage.googleapis.com/openimages/web/index.html>

  * Dataset license: CC-BY-2.0

  * Dataset size: 561 GB

  * Tags: `image, detection, segmentation, classification`

  * Supported splits: `train, test, validation`

  * ZooDataset class: [`OpenImagesV6Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.OpenImagesV6Dataset "fiftyone.zoo.datasets.base.OpenImagesV6Dataset")




**Notes**

  * Not all images contain all types of labels

  * All images have been rescaled so that their largest side is at most 1024 pixels




**Full split stats**

  * Train split: 1,743,042 images (513 GB)

  * Test split: 125,436 images (36 GB)

  * Validation split: 41,620 images (12 GB)




**Partial downloads**

Open Images is a massive dataset, so FiftyOne provides parameters that can be used to efficiently download specific subsets of the dataset to suit your needs. When new subsets are specified, FiftyOne will use existing downloaded data first if possible before resorting to downloading additional data from the web.

The following parameters are available to configure a partial download of Open Images V6 by passing them to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset"):

  * **split** (_None_) and **splits** (_None_): a string or list of strings, respectively, specifying the splits to load. Supported values are `("train", "test", "validation")`. If neither is provided, all available splits are loaded

  * **label_types** (_None_): a label type or list of label types to load. Supported values are `("detections", "classifications", "relationships", "segmentations")`. By default, all labels types are loaded

  * **classes** (_None_): a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded. You can use [`get_classes()`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.get_classes "fiftyone.utils.openimages.get_classes") and [`get_segmentation_classes()`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.get_segmentation_classes "fiftyone.utils.openimages.get_segmentation_classes") to see the available classes and segmentation classes, respectively

  * **attrs** (_None_): a string or list of strings specifying required relationship attributes to load. This parameter is only applicable if `label_types` contains `"relationships"`. If provided, only samples containing at least one instance of a specified attribute will be loaded. You can use [`get_attributes()`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.get_attributes "fiftyone.utils.openimages.get_attributes") to see the available attributes

  * **image_ids** (_None_): a list of specific image IDs to load. The IDs can be specified either as `<split>/<image-id>` or `<image-id>` strings. Alternatively, you can provide the path to a TXT (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **include_id** (_True_): whether to include the Open Images ID of each sample in the loaded labels

  * **only_matching** (_False_): whether to only load labels that match the `classes` or `attrs` requirements that you provide (True), or to load all labels for samples that match the requirements (False)

  * **num_workers** (_None_): the number of processes to use when downloading individual images. By default, `multiprocessing.cpu_count()` is used

  * **shuffle** (_False_): whether to randomly shuffle the order in which samples are chosen for partial downloads

  * **seed** (_None_): a random seed to use when shuffling

  * **max_samples** (_None_): a maximum number of samples to load per split. If `label_types`, `classes`, and/or `attrs` are also specified, first priority will be given to samples that contain all of the specified label types, classes, and/or attributes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements




Note

See [`OpenImagesV6Dataset`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.OpenImagesV6Dataset "fiftyone.zoo.datasets.base.OpenImagesV6Dataset") and [`OpenImagesV6DatasetImporter`](api__fiftyone.utils.openimages.md#fiftyone.utils.openimages.OpenImagesV6DatasetImporter "fiftyone.utils.openimages.OpenImagesV6DatasetImporter") for complete descriptions of the optional keyword arguments that you can pass to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset").

**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4#
     5# Load 50 random samples from the validation split
     6#
     7# Only the required images will be downloaded (if necessary).
     8# By default, all label types are loaded
     9#
    10
    11dataset = foz.load_zoo_dataset(
    12    "open-images-v6",
    13    split="validation",
    14    max_samples=50,
    15    shuffle=True,
    16)
    17
    18session = fo.launch_app(dataset)
    19
    20#
    21# Load detections and classifications for 25 samples from the
    22# validation split that contain fedoras and pianos
    23#
    24# Images that contain all `label_types` and `classes` will be
    25# prioritized first, followed by images that contain at least one of
    26# the required `classes`. If there are not enough images matching
    27# `classes` in the split to meet `max_samples`, only the available
    28# images will be loaded.
    29#
    30# Images will only be downloaded if necessary
    31#
    32
    33dataset = foz.load_zoo_dataset(
    34    "open-images-v6",
    35    split="validation",
    36    label_types=["detections", "classifications"],
    37    classes=["Fedora", "Piano"],
    38    max_samples=25,
    39)
    40
    41session.dataset = dataset
    42
    43#
    44# Download the entire validation split and load detections
    45#
    46# Subsequent partial loads of the validation split will never require
    47# downloading any images
    48#
    49
    50dataset = foz.load_zoo_dataset(
    51    "open-images-v6",
    52    split="validation",
    53    label_types=["detections"],
    54)
    55
    56session.dataset = dataset
    
    
    
    #
    # Load 50 random samples from the validation split
    #
    # Only the required images will be downloaded (if necessary).
    # By default, all label types are loaded
    #
    
    fiftyone zoo datasets load open-images-v6 \
        --split validation \
        --kwargs \
            max_samples=50
    
    fiftyone app launch open-images-v6-validation-50
    
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
    
    fiftyone zoo datasets load open-images-v6 \
        --split validation \
        --kwargs \
            label_types=segmentations,classifications \
            classes=Fedora,Piano \
            max_samples=25
    
    fiftyone app launch open-images-v6-validation-25
    
    #
    # Download the entire validation split and load detections
    #
    # Subsequent partial loads of the validation split will never require
    # downloading any images
    #
    
    fiftyone zoo datasets load open-images-v6 \
        --split validation
    
    fiftyone app launch open-images-v6-validation
    

![open-images-v6](../../_images/open-images-v6.png)
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
