---
source_url: https://docs.voxel51.com/api/fiftyone.utils.places.html
---

# fiftyone.utils.places#

Utilities for working with the [Places dataset](http://places2.csail.mit.edu/index.html).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`download_places_dataset_split`(dataset_dir,Â split) | Utility that downloads splits of the Places dataset <http://places2.csail.mit.edu/index.html>.  
---|---  
  
**Classes:**

`PlacesDatasetImporter`(dataset_dir[,Â ...]) | Class for importing datasets written by :meth:download_places_dataset_split`.  
---|---  
  
fiftyone.utils.places.download_places_dataset_split(_dataset_dir_ , _split_ , _raw_dir =None_)#
    

Utility that downloads splits of the Places dataset <http://places2.csail.mit.edu/index.html>.

Any existing files are not re-downloaded.

Parameters:
    

  * **dataset_dir** â the directory to download the dataset

  * **split** â the split to download. Supported values are `("train", "validation", "test")`

  * **raw_dir** (_None_) â a directory in which full annotations files may be stored to avoid re-downloads in the future



Returns:
    

  * num_samples: the total number of downloaded images

  * classes: the list of all classes

  * did_download: whether any content was downloaded (True) or if all necessary files were already downloaded (False)




Return type:
    

a tuple of

class fiftyone.utils.places.PlacesDatasetImporter(_dataset_dir_ , _shuffle =False_, _seed =None_, _max_samples =None_)#
    

Bases: [`LabeledImageDatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.LabeledImageDatasetImporter "fiftyone.utils.data.importers.LabeledImageDatasetImporter")

Class for importing datasets written by :meth:download_places_dataset_split`.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **shuffle** (_False_) â whether to randomly shuffle the order in which the samples are imported

  * **seed** (_None_) â a random seed to use when shuffling

  * **max_samples** (_None_) â a maximum number of samples to load. By default, all samples are imported




**Attributes:**

`has_image_metadata` | Whether this importer produces [`fiftyone.core.metadata.ImageMetadata`](api__fiftyone.core.metadata.md#fiftyone.core.metadata.ImageMetadata "fiftyone.core.metadata.ImageMetadata") instances for each image.  
---|---  
`has_dataset_info` | Whether this importer produces a dataset info dictionary.  
`label_cls` | The [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class(es) returned by this importer.  
  
**Methods:**

`setup`() | Performs any necessary setup before importing the first sample in the dataset.  
---|---  
`close`(*args) | Performs any necessary actions after the last sample has been imported.  
`get_dataset_info`() | Returns the dataset info for the dataset.  
  
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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
