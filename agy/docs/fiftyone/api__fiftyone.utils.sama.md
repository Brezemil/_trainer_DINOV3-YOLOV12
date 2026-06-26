---
source_url: https://docs.voxel51.com/api/fiftyone.utils.sama.html
---

# fiftyone.utils.sama#

Sama utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_sama_coco_dataset_split`(...[,Â ...]) | Utility that downloads full or partial data splits of the [COCO dataset](https://cocodataset.org) with annotation splits found at <https://www.sama.com/sama-coco-dataset>.  
---|---  
  
fiftyone.utils.sama.download_sama_coco_dataset_split(_dataset_dir_ , _split_ , _label_types =None_, _classes =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_, _raw_dir =None_, _scratch_dir =None_)#
    

Utility that downloads full or partial data splits of the [COCO dataset](https://cocodataset.org) with annotation splits found at <https://www.sama.com/sama-coco-dataset>.

See [this page](user_guide__export_datasets.md#cocodetectiondataset-export) for the format in which `dataset_dir` will be arranged.

Any existing files are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory to download the dataset

  * **split** â the split to download. Supported values are `("train", "validation", "test")`

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
