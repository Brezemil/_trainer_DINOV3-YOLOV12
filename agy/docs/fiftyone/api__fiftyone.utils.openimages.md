---
source_url: https://docs.voxel51.com/api/fiftyone.utils.openimages.html
---

# fiftyone.utils.openimages#

Utilities for working with the Open Images <https://storage.googleapis.com/openimages/web/index.html> dataset.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`OpenImagesDatasetImporter`(dataset_dir[,Â ...]) | Base class for importing datasets in Open Images format.  
---|---  
`OpenImagesV6DatasetImporter`(dataset_dir[,Â ...]) | Base class for importing datasets in Open Images V6 format.  
`OpenImagesV7DatasetImporter`(dataset_dir[,Â ...]) | Base class for importing datasets in Open Images V7 format.  
  
**Functions:**

`get_attributes`([version,Â dataset_dir]) | Gets the list of relationship attributes in the Open Images dataset.  
---|---  
`get_classes`([version,Â dataset_dir]) | Gets the boxable classes that exist in classifications, detections, points, and relationships in the Open Images dataset.  
`get_segmentation_classes`([version,Â dataset_dir]) | Gets the list of classes (350) that are labeled with segmentations in the Open Images V6/V7 dataset.  
`get_point_classes`([version,Â dataset_dir]) | Gets the list of classes that are labeled with points in the Open Images V7 dataset.  
`download_open_images_split`(dataset_dir,Â split) | Utility that downloads full or partial splits of the [Open Images dataset](https://storage.googleapis.com/openimages/web/index.html).  
  
class fiftyone.utils.openimages.OpenImagesDatasetImporter(_dataset_dir_ , _label_types =None_, _classes =None_, _attrs =None_, _image_ids =None_, _include_id =True_, _only_matching =False_, _load_hierarchy =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter")

Base class for importing datasets in Open Images format.

See `fiftyone.types.OpenImagesDataset` for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "classifications", "points", "relationships", "segmentations")`. âpointsâ are only supported for open-images-v7. By default, all supported label types for version are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **attrs** (_None_) â a string or list of strings specifying required relationship attributes to load. Only applicable when `label_types` includes ârelationshipsâ. If provided, only samples containing at least one instance of a specified attribute will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **include_id** (_True_) â whether to load the Open Images ID for each sample along with the labels

  * **only_matching** (_False_) â whether to only load labels that match the `classes` or `attrs` requirements that you provide (True), or to load all labels for samples that match the requirements (False)

  * **load_hierarchy** (_True_) â whether to load the classes hierarchy and add it to the datasetâs `info` dictionary

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load. If `label_types`, `classes`, and/or `attrs` are also specified, first priority will be given to samples that contain all of the specified label types, classes, and/or attributes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




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

class fiftyone.utils.openimages.OpenImagesV6DatasetImporter(_dataset_dir_ , _label_types =None_, _classes =None_, _attrs =None_, _image_ids =None_, _include_id =True_, _only_matching =False_, _load_hierarchy =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `OpenImagesDatasetImporter`

Base class for importing datasets in Open Images V6 format.

See `fiftyone.types.OpenImagesDataset` for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "classifications", "relationships", "segmentations")`. By default, all supported label types for version are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **attrs** (_None_) â a string or list of strings specifying required relationship attributes to load. Only applicable when `label_types` includes ârelationshipsâ. If provided, only samples containing at least one instance of a specified attribute will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **include_id** (_True_) â whether to load the Open Images ID for each sample along with the labels

  * **only_matching** (_False_) â whether to only load labels that match the `classes` or `attrs` requirements that you provide (True), or to load all labels for samples that match the requirements (False)

  * **load_hierarchy** (_True_) â whether to load the classes hierarchy and add it to the datasetâs `info` dictionary

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load. If `label_types`, `classes`, and/or `attrs` are also specified, first priority will be given to samples that contain all of the specified label types, classes, and/or attributes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
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

class fiftyone.utils.openimages.OpenImagesV7DatasetImporter(_dataset_dir_ , _label_types =None_, _classes =None_, _attrs =None_, _image_ids =None_, _include_id =True_, _only_matching =False_, _load_hierarchy =True_, _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: `OpenImagesDatasetImporter`

Base class for importing datasets in Open Images V7 format.

See `fiftyone.types.OpenImagesDataset` for format details.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "classifications", "points", "relationships", "segmentations")`. By default, all supported label types for version are loaded

  * **classes** (_None_) â a string or list of strings specifying required classes to load. If provided, only samples containing at least one instance of a specified class will be loaded

  * **attrs** (_None_) â a string or list of strings specifying required relationship attributes to load. Only applicable when `label_types` includes ârelationshipsâ. If provided, only samples containing at least one instance of a specified attribute will be loaded

  * **image_ids** (_None_) â 

an optional list of specific image IDs to load. Can be provided in any of the following formats:

    * a list of `<image-id>` strings

    * a list of `<split>/<image-id>` strings

    * the path to a text (newline-separated), JSON, or CSV file containing the list of image IDs to load in either of the first two formats

  * **include_id** (_True_) â whether to load the Open Images ID for each sample along with the labels

  * **only_matching** (_False_) â whether to only load labels that match the `classes` or `attrs` requirements that you provide (True), or to load all labels for samples that match the requirements (False)

  * **load_hierarchy** (_True_) â whether to load the classes hierarchy and add it to the datasetâs `info` dictionary

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load. If `label_types`, `classes`, and/or `attrs` are also specified, first priority will be given to samples that contain all of the specified label types, classes, and/or attributes, followed by samples that contain at least one of the specified labels types or classes. The actual number of samples loaded may be less than this maximum value if the dataset does not contain sufficient samples matching your requirements. By default, all matching samples are loaded




**Methods:**

`close`(*args) | Performs any necessary actions after the last sample has been imported.  
---|---  
`get_dataset_info`() | Returns the dataset info for the dataset.  
`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
  
**Attributes:**

`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
---|---  
`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
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

fiftyone.utils.openimages.get_attributes(_version ='v7'_, _dataset_dir =None_)#
    

Gets the list of relationship attributes in the Open Images dataset.

Parameters:
    

  * **version** (_"v7"_) â the version of the Open Images dataset. Supported values are `("v6", "v7")`

  * **dataset_dir** (_None_) â an optional root directory the in which the dataset is downloaded



Returns:
    

a sorted list of attribute names

fiftyone.utils.openimages.get_classes(_version ='v7'_, _dataset_dir =None_)#
    

Gets the boxable classes that exist in classifications, detections, points, and relationships in the Open Images dataset.

This method can be called in isolation without downloading the dataset.

Parameters:
    

  * **version** (_"v7"_) â the version of the Open Images dataset. Supported values are `("v6", "v7")`

  * **dataset_dir** (_None_) â an optional root directory the in which the dataset is downloaded



Returns:
    

a sorted list of class name strings

fiftyone.utils.openimages.get_segmentation_classes(_version ='v6'_, _dataset_dir =None_)#
    

Gets the list of classes (350) that are labeled with segmentations in the Open Images V6/V7 dataset.

This method can be called in isolation without downloading the dataset.

Parameters:
    

  * **version** (_"v6"_) â the version of the Open Images dataset. Supported values are `("v6")`

  * **dataset_dir** (_None_) â an optional root directory the in which the dataset is downloaded



Returns:
    

a sorted list of segmentation class name strings

fiftyone.utils.openimages.get_point_classes(_version ='v7'_, _dataset_dir =None_)#
    

Gets the list of classes that are labeled with points in the Open Images V7 dataset.

This method can be called in isolation without downloading the dataset.

Parameters:
    

  * **version** (_"v7"_) â the version of the Open Images dataset. Supported values are `("v7")`

  * **dataset_dir** (_None_) â an optional root directory in which the dataset is downloaded



Returns:
    

a sorted list of segmentation class name strings

fiftyone.utils.openimages.download_open_images_split(_dataset_dir_ , _split_ , _version ='v6'_, _label_types =None_, _classes =None_, _attrs =None_, _image_ids =None_, _num_workers =None_, _shuffle =None_, _seed =None_, _max_samples =None_)#
    

Utility that downloads full or partial splits of the [Open Images dataset](https://storage.googleapis.com/openimages/web/index.html).

See `fiftyone.types.OpenImagesDataset` for the format in which `dataset_dir` will be arranged.

Any existing files are not re-downloaded.

This method specifically downloads the subsets of annotations corresponding to the 600 boxable classes of Open Images. [See here](https://storage.googleapis.com/openimages/web/download.html) for other download options.

Parameters:
    

  * **dataset_dir** â the directory to download the dataset

  * **split** â the split to download. Supported values are `("train", "validation", "test")`

  * **version** (_"v7"_) â the version of the Open Images dataset to download. Supported values are `("v6", "v7")`

  * **label_types** (_None_) â a label type or list of label types to load. The supported values are `("detections", "classifications", "relationships", "segmentations")` for `"v6"` and `("detections", "classifications", "points", "relationships", "segmentations")` for `"v7"`. By default, all label types are loaded

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



Returns:
    

  * num_samples: the total number of downloaded images, or `None` if everything was already downloaded

  * classes: the list of all classes, or `None` if everything was already downloaded

  * did_download: whether any content was downloaded (True) or if all necessary files were already downloaded (False)




Return type:
    

a tuple of

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
