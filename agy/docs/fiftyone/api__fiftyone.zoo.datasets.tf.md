---
source_url: https://docs.voxel51.com/api/fiftyone.zoo.datasets.tf.html
---

# fiftyone.zoo.datasets.tf#

FiftyOne Zoo Datasets provided by `tensorflow_datasets`.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`TFDSDataset`() | Base class for zoo datasets that are provided via the `tensorflow_datasets` package.  
---|---  
`MNISTDataset`() | The MNIST database of handwritten digits.  
`FashionMNISTDataset`() | The Fashion-MNIST database of Zalando's fashion article images.  
`CIFAR10Dataset`() | The CIFAR-10 dataset of images.  
`CIFAR100Dataset`() | The CIFAR-100 dataset of images.  
`ImageNet2012Dataset`([source_dir]) | The ImageNet 2012 dataset.  
`VOC2007Dataset`() | The dataset for the PASCAL Visual Object Classes Challenge 2007 (VOC2007) for the detection competition.  
`VOC2012Dataset`() | The dataset for the PASCAL Visual Object Classes Challenge 2012 (VOC2012) for the detection competition.  
  
class fiftyone.zoo.datasets.tf.TFDSDataset#
    

Bases: [`ZooDataset`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDataset "fiftyone.zoo.datasets.ZooDataset")

Base class for zoo datasets that are provided via the `tensorflow_datasets` package.

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

class fiftyone.zoo.datasets.tf.MNISTDataset#
    

Bases: `TFDSDataset`

The MNIST database of handwritten digits.

The dataset consists of 70,000 28 x 28 grayscale images in 10 classes. There are 60,000 training images and 10,000 test images.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("mnist", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

21.00 MB

Source
    

<http://yann.lecun.com/exdb/mnist>

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

class fiftyone.zoo.datasets.tf.FashionMNISTDataset#
    

Bases: `TFDSDataset`

The Fashion-MNIST database of Zalandoâs fashion article images.

The dataset consists of 70,000 28 x 28 grayscale images in 10 classes. There are 60,000 training images and 10,000 test images.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("fashion-mnist", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

36.42 MB

Source
    

[zalandoresearch/fashion-mnist](https://github.com/zalandoresearch/fashion-mnist)

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

class fiftyone.zoo.datasets.tf.CIFAR10Dataset#
    

Bases: `TFDSDataset`

The CIFAR-10 dataset of images.

The dataset consists of 60,000 32 x 32 color images in 10 classes, with 6,000 images per class. There are 50,000 training images and 10,000 test images.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("cifar10", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

132.40 MB

Source
    

<https://www.cs.toronto.edu/~kriz/cifar.html>

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

class fiftyone.zoo.datasets.tf.CIFAR100Dataset#
    

Bases: `TFDSDataset`

The CIFAR-100 dataset of images.

The dataset consists of 60,000 32 x 32 color images in 100 classes, with 600 images per class. There are 50,000 training images and 10,000 test images.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("cifar100", split="test")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

132.03 MB

Source
    

<https://www.cs.toronto.edu/~kriz/cifar.html>

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

class fiftyone.zoo.datasets.tf.ImageNet2012Dataset(_source_dir =None_)#
    

Bases: `TFDSDataset`

The ImageNet 2012 dataset.

ImageNet, also known as ILSVRC 2012, is an image dataset organized according to the WordNet hierarchy. Each meaningful concept in WordNet, possibly described by multiple words or word phrases, is called a âsynonym setâ or âsynsetâ. There are more than 100,000 synsets in WordNet, the majority of them are nouns (80,000+). ImageNet provides on average 1,000 images to illustrate each synset. Images of each concept are quality-controlled and human-annotated. In its completion, we hope ImageNet will offer tens of millions of cleanly sorted images for most of the concepts in the WordNet hierarchy.

Note that labels were never publicly released for the test set, so only the training and validation sets are provided.

In order to load the ImageNet dataset, you must download the source data manually. The directory should be organized in the following format:
    
    
    source_dir/
        ILSVRC2012_devkit_t12.tar.gz    # both splits
        ILSVRC2012_img_train.tar        # train split
        ILSVRC2012_img_val.tar          # validation split
    

You can register at <http://www.image-net.org/download-images> in order to get links to download the data.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # The path to the source files that you manually downloaded
    source_dir = "/path/to/dir-with-imagenet-files"
    
    dataset = foz.load_zoo_dataset(
        "imagenet-2012",
        split="validation",
        source_dir=source_dir,
    )
    
    session = fo.launch_app(dataset)
    

Dataset size
    

144.02 GB

Source
    

<http://image-net.org>

Parameters:
    

**source_dir** (_None_) â the directory containing the manually downloaded ImageNet files

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

class fiftyone.zoo.datasets.tf.VOC2007Dataset#
    

Bases: `TFDSDataset`

The dataset for the PASCAL Visual Object Classes Challenge 2007 (VOC2007) for the detection competition.

A total of 9,963 images are included in this dataset, where each image contains a set of objects, out of 20 different classes, making a total of 24,640 annotated objects.

Note that, as per the official dataset, the test set of VOC2007 does not contain annotations.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("voc-2007", split="validation")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

868.85 MB

Source
    

<http://host.robots.ox.ac.uk/pascal/VOC/voc2007>

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

class fiftyone.zoo.datasets.tf.VOC2012Dataset#
    

Bases: `TFDSDataset`

The dataset for the PASCAL Visual Object Classes Challenge 2012 (VOC2012) for the detection competition.

A total of 11,540 images are included in this dataset, where each image contains a set of objects, out of 20 different classes, making a total of 27,450 annotated objects.

Note that, as per the official dataset, the test set of VOC2012 does not contain annotations.

Example usage:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("voc-2012", split="validation")
    
    session = fo.launch_app(dataset)
    

Dataset size
    

3.59 GB

Source
    

<http://host.robots.ox.ac.uk/pascal/VOC/voc2012>

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

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
