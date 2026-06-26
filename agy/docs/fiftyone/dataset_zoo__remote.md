---
source_url: https://docs.voxel51.com/dataset_zoo/remote.html
---

# Remotely-Sourced Zoo Datasets#

This page describes how to work with and create zoo datasets whose download/preparation methods are hosted via GitHub repositories or public URLs.

Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Note

Check out [voxel51/coco-2017](https://github.com/voxel51/coco-2017) and [voxel51/caltech101](https://github.com/voxel51/caltech101) for examples of remotely-sourced datasets.

## Working with remotely-sourced datasets#

Working with remotely-sourced zoo datasets is just like [built-in zoo datasets](https://docs.voxel51.com/dataset_zoo/index.html#dataset-zoo), as both varieties support the [full zoo API](dataset_zoo__api.md#dataset-zoo-api).

When specifying remote sources, you can provide any of the following:

  * A GitHub repo URL like `https://github.com/<user>/<repo>`

  * A GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * A GitHub ref string like `<user>/<repo>[/<ref>]`

  * A publicly accessible URL of an archive (eg zip or tar) file




Hereâs the basic recipe for working with remotely-sourced zoo datasets:

Use [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset") to download and load a remotely-sourced zoo dataset into a FiftyOne dataset:
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = foz.load_zoo_dataset(
    5    "https://github.com/voxel51/coco-2017",
    6    split="validation",
    7)
    8
    9session = fo.launch_app(dataset)
    

Once youâve downloaded all or part of a remotely-sourced zoo dataset, it will subsequently appear as an available zoo dataset under the name in the datasetâs fiftyone.yml when you call [`list_zoo_datasets()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.list_zoo_datasets "fiftyone.zoo.datasets.list_zoo_datasets"):
    
    
    1available_datasets = foz.list_zoo_datasets()
    2
    3print(available_datasets)
    4# [..., "voxel51/coco-2017", ...]
    

You can also download a remotely-sourced zoo dataset without (yet) loading it into a FiftyOne dataset by calling [`download_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.download_zoo_dataset "fiftyone.zoo.datasets.download_zoo_dataset"):
    
    
    1dataset = foz.download_zoo_dataset(
    2    "https://github.com/voxel51/coco-2017",
    3    split="validation",
    4)
    

You can delete the local copy of a remotely-sourced zoo dataset (or individual split(s) of it) via [`delete_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.delete_zoo_dataset "fiftyone.zoo.datasets.delete_zoo_dataset") by providing either the datasetâs name or the remote source from which you downloaded it:
    
    
    1# These are equivalent
    2foz.delete_zoo_dataset("voxel51/coco-2017", split="validation")
    3foz.delete_zoo_dataset(
    4    "https://github.com/voxel51/coco-2017", split="validation"
    5)
    6
    7# These are equivalent
    8foz.delete_zoo_dataset("voxel51/coco-2017")
    9foz.delete_zoo_dataset("https://github.com/voxel51/coco-2017")
    

Use [fiftyone zoo datasets load](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-load) to load a remotely-sourced zoo dataset into a FiftyOne dataset:
    
    
    fiftyone zoo datasets load \
        https://github.com/voxel51/coco-2017 \
        --split validation \
        --dataset-name 'voxel51/coco-2017-validation'
    
    fiftyone app launch 'voxel51/coco-2017-validation'
    

Once youâve downloaded all or part of a remotely-sourced zoo dataset, it will subsequently appear as an available zoo dataset under the name in the datasetâs fiftyone.yml when you call [fiftyone zoo datasets list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-list):
    
    
    fiftyone zoo datasets list
    
    # contains row(s) for a dataset 'voxel51/coco-2017'
    

You can also download a remotely-sourced zoo dataset without (yet) loading it into a FiftyOne dataset by calling [fiftyone zoo datasets download](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-download):
    
    
    fiftyone zoo datasets download \
        https://github.com/voxel51/coco-2017 \
        --split validation
    

You can delete the local copy of a remotely-sourced zoo dataset (or individual split(s) of it) via [fiftyone zoo datasets delete](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-delete) by providing either the datasetâs name or the remote source from which you downloaded it:
    
    
    # These are equivalent
    fiftyone zoo datasets delete voxel51/coco-2017 --split validation
    fiftyone zoo datasets delete \
        https://github.com/voxel51/coco-2017 --split validation
    
    # These are equivalent
    fiftyone zoo datasets delete voxel51/coco-2017
    fiftyone zoo datasets delete https://github.com/voxel51/coco-2017
    

## Creating remotely-sourced datasets#

A remotely-sourced dataset is defined by a directory with the following contents:
    
    
    fiftyone.yml
    __init__.py
        def download_and_prepare(dataset_dir, split=None, **kwargs):
            pass
    
        def load_dataset(dataset, dataset_dir, split=None, **kwargs):
            pass
    

Each component is described in detail below.

Note

By convention, datasets also contain an optional `README.md` file that provides additional information about the dataset and example syntaxes for downloading and working with it.

### fiftyone.yml#

The datasetâs `fiftyone.yml` or `fiftyone.yaml` file defines relevant metadata about the dataset:

Field | Required? | Description  
---|---|---  
`name` | **yes** | The name of the dataset. Once youâve downloaded all or part of a remotely-sourced zoo dataset, it will subsequently appear as an available zoo dataset under this name when using the [zoo API](dataset_zoo__api.md#dataset-zoo-api)  
`type` |  | Declare that the directory defines a `dataset`. This can be omitted for backwards compatibility, but it is recommended to specify this  
`author` |  | The author of the dataset  
`version` |  | The version of the dataset  
`url` |  | The source (eg GitHub repository) where the directory containing this file is hosted  
`source` |  | The original source of the dataset  
`license` |  | The license under which the dataset is distributed  
`description` |  | A brief description of the dataset  
`fiftyone.version` |  | A semver version specifier (or `*`) describing the required FiftyOne version for the dataset to load properly  
`supports_partial_downloads` |  | Specify `true` or `false` whether parts of the dataset can be downloaded/loaded by providing `kwargs` to [`download_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.download_zoo_dataset "fiftyone.zoo.datasets.download_zoo_dataset") or [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset") as described here. If omitted, this is assumed to be `false`  
`tags` |  | A list of tags for the dataset. Useful in conjunction with [`list_zoo_datasets()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.list_zoo_datasets "fiftyone.zoo.datasets.list_zoo_datasets")  
`splits` |  | A list of the datasetâs supported splits. This should be omitted if the dataset does not contain splits  
`size_samples` |  | The total number of samples in the dataset, or a list of per-split sizes  
  
Here are two example dataset YAML files:
    
    
     1name: voxel51/coco-2017
     2type: dataset
     3author: The COCO Consortium
     4version: 1.0.0
     5url: https://github.com/voxel51/coco-2017
     6source: http://cocodataset.org/#home
     7license: https://cocodataset.org/#termsofuse
     8description: The COCO-2017 dataset
     9fiftyone:
    10  version: "*"
    11supports_partial_downloads: true
    12tags:
    13 - image
    14 - detection
    15 - segmentation
    16splits:
    17 - train
    18 - validation
    19 - test
    20size_samples:
    21 - train: 118287
    22 - test: 40670
    23 - validation: 5000
    
    
    
     1name: voxel51/caltech101
     2type: dataset
     3author: Fei-Fei Li, Marco Andreeto, Marc'Aurelio Ranzato, Pietro Perona
     4version: 1.0.0
     5url: https://github.com/voxel51/caltech101
     6source: https://data.caltech.edu/records/mzrjq-6wc02
     7license: Creative Commons Attribution 4.0 International
     8description: The Caltech 101 dataset
     9fiftyone:
    10  version: "*"
    11supports_partial_downloads: false
    12tags:
    13 - image
    14 - classification
    15size_samples: 9145
    

### Download and prepare#

All datasetâs `__init__.py` files must define a `download_and_prepare()` method with the signature below:
    
    
     1def download_and_prepare(dataset_dir, split=None, **kwargs):
     2    """Downloads the dataset and prepares it for loading into FiftyOne.
     3
     4    Args:
     5        dataset_dir: the directory in which to construct the dataset
     6        split (None): a specific split to download, if the dataset supports
     7            splits. The supported split values are defined by the dataset's
     8            YAML file
     9        **kwargs: optional keyword arguments that your dataset can define to
    10            configure what/how the download is performed
    11
    12    Returns:
    13        a tuple of
    14
    15        -   ``dataset_type``: a ``fiftyone.types.Dataset`` type that the
    16            dataset is stored in locally, or None if the dataset provides
    17            its own ``load_dataset()`` method
    18        -   ``num_samples``: the total number of downloaded samples for the
    19            dataset or split
    20        -   ``classes``: a list of classes in the dataset, or None if not
    21            applicable
    22    """
    23
    24    # Download files and organize them in `dataset_dir`
    25    ...
    26
    27    # Define how the data is stored
    28    dataset_type = fo.types.ImageClassificationDirectoryTree
    29    dataset_type = None  # custom ``load_dataset()`` method
    30
    31    # Indicate how many samples have been downloaded
    32    # May be less than the total size if partial downloads have been used
    33    num_samples = 10000
    34
    35    # Optionally report what classes exist in the dataset
    36    classes = None
    37    classes = ["cat", "dog", ...]
    38
    39    return dataset_type, num_samples, classes
    

This method is called under-the-hood when a user calls [`download_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.download_zoo_dataset "fiftyone.zoo.datasets.download_zoo_dataset") or [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset"), and its job is to download any relevant files from the web and organize and/or prepare them as necessary into a format thatâs ready to be loaded into a FiftyOne dataset.

The `dataset_type` that `download_and_prepare()` returns defines how it the dataset is ultimately loaded into FiftyOne:

  * **Built-in importer** : in many cases, FiftyOne already contains a [built-in importer](user_guide__import_datasets.md#supported-import-formats) that can be leveraged to load data on disk into FiftyOne. Remotely-sourced datasets can take advantage of this by simply returning the appropriate `dataset_type` from `download_and_prepare()`, which is then used to load the data into FiftyOne as follows:



    
    
    1# If the dataset has splits, `dataset_dir` will be the split directory
    2dataset_importer_cls = dataset_type.get_dataset_importer_cls()
    3dataset_importer = dataset_importer_cls(dataset_dir=dataset_dir, **kwargs)
    4
    5dataset.add_importer(dataset_importer, **kwargs)
    

  * **Custom loader** : if `dataset_type=None` is returned, then `__init__.py` must also contain a `load_dataset()` method as described below that handles loading the data into FiftyOne as follows:



    
    
    1load_dataset(dataset, dataset_dir, **kwargs)
    

### Load dataset#

Datasets that donât use a built-in importer must also define a `load_dataset()` method in their `__init__.py` with the signature below:
    
    
     1def load_dataset(dataset, dataset_dir, split=None, **kwargs):
     2    """Loads the dataset into the given FiftyOne dataset.
     3
     4    Args:
     5        dataset: a :class:`fiftyone.core.dataset.Dataset` to which to import
     6        dataset_dir: the directory to which the dataset was downloaded
     7        split (None): a split to load. The supported values are
     8            ``("train", "validation", "test")``
     9        **kwargs: optional keyword arguments that your dataset can define to
    10            configure what/how the load is performed
    11    """
    12
    13    # Load data into samples
    14    samples = [...]
    15
    16    # Add samples to the dataset
    17    dataset.add_samples(samples)
    

This methodâs job is to load the filepaths and any relevant labels into [`Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") objects and then call [`add_samples()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_samples "fiftyone.core.dataset.Dataset.add_samples") or a similar method to add them to the provided [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").

## Partial downloads#

Remotely-sourced datasets can support partial downloads, which is useful for a variety of reasons, including:

  * A dataset may contain labels for multiple task types but the user is only interested in a subset of them

  * The dataset may be very large and the user only wants to download a small subset of the samples to get familiar with the dataset




Datasets that support partial downloads should declare this in their fiftyone.yml:
    
    
    supports_partial_downloads: true
    

The partial download behavior itself is defined via `**kwargs` in the datasetâs `__init__.py` methods:
    
    
    1def download_and_prepare(dataset_dir, split=None, **kwargs):
    2    pass
    3
    4def load_dataset(dataset, dataset_dir, split=None, **kwargs):
    5    pass
    

When [`download_zoo_dataset(url, ..., **kwargs)`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.download_zoo_dataset "fiftyone.zoo.datasets.download_zoo_dataset") is called, any `kwargs` declared by `download_and_prepare()` are passed through to it.

When [`load_zoo_dataset(name_or_url, ..., **kwargs)`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset") is called, any `kwargs` declared by `download_and_prepare()` and `load_dataset()` are passed through to them, respectively.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
