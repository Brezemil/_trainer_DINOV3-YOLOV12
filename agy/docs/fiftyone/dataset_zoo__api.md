---
source_url: https://docs.voxel51.com/dataset_zoo/api.html
---

# Dataset Zoo API#

You can interact with the Dataset Zoo either via the Python library or the CLI:

The Dataset Zoo is accessible via the [`fiftyone.zoo`](api__fiftyone.zoo.md#module-fiftyone.zoo "fiftyone.zoo") package.

The [fiftyone zoo datasets](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets) command provides convenient utilities for working with datasets in the FiftyOne Dataset Zoo.

## Listing zoo datasets#

You can list the available zoo datasets via [`list_zoo_datasets()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.list_zoo_datasets "fiftyone.zoo.datasets.list_zoo_datasets"):
    
    
    1import fiftyone.zoo as foz
    2
    3available_datasets = foz.list_zoo_datasets()
    4
    5print(available_datasets)
    
    
    
    ['bdd100k',
    'caltech101',
    'cifar10',
    ...
    'voc-2012']
    

To view the zoo datasets that you have downloaded, you can use [`list_downloaded_zoo_datasets()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.list_downloaded_zoo_datasets "fiftyone.zoo.datasets.list_downloaded_zoo_datasets"):
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4downloaded_datasets = foz.list_downloaded_zoo_datasets()
    5fo.pprint(downloaded_datasets)
    
    
    
    {
        ...
        'cifar10': (
            '~/fiftyone/cifar10',
            <fiftyone.zoo.datasets.ZooDatasetInfo object at 0x141a63048>,
        ),
        'kitti': (
            '~/fiftyone/kitti',
            <fiftyone.zoo.datasets.ZooDatasetInfo object at 0x141a62940>,
        ),
        ...
    }
    

You can access information about the available zoo datasets via the [fiftyone zoo datasets list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-list) command.

For example, to list the available zoo datasets and whether you have downloaded them, you can execute:
    
    
    fiftyone zoo datasets list
    

Dataset splits that have been downloaded are indicated by a checkmark in the `downloaded` column, and their location on disk is indicated by the `dataset_dir` column.

The `base` column indicates datasets that are available directly via FiftyOne without requiring an ML backend.

The `torch` and `tensorflow` columns indicate whether the particular dataset split is provided via the respective ML backend. The `(*)` indicates your default ML backend, which will be used in case a given split is available through multiple ML backends.

## Getting information about zoo datasets#

Each zoo dataset is represented by a [`ZooDataset`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDataset "fiftyone.zoo.datasets.ZooDataset") subclass, which contains information about the dataset, its available splits, and more. You can access this object for a given dataset via the [`get_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.get_zoo_dataset "fiftyone.zoo.datasets.get_zoo_dataset") method.

For example, letâs print some information about the CIFAR-10 dataset:
    
    
     1import textwrap
     2import fiftyone.zoo as foz
     3
     4zoo_dataset = foz.get_zoo_dataset("cifar10")
     5
     6print("***** Dataset description *****")
     7print(textwrap.dedent("    " + zoo_dataset.__doc__))
     8
     9print("***** Tags *****")
    10print("%s\n" % ", ".join(zoo_dataset.tags))
    11
    12print("***** Supported splits *****")
    13print("%s\n" % ", ".join(zoo_dataset.supported_splits))
    
    
    
    ***** Dataset description *****
    The CIFAR-10 dataset consists of 60000 32 x 32 color images in 10
    classes, with 6000 images per class. There are 50000 training images and
    10000 test images.
    
    Dataset size:
        132.40 MiB
    
    Source:
        https://www.cs.toronto.edu/~kriz/cifar.html
    
    ***** Tags *****
    image, classification
    
    ***** Supported splits *****
    test, train
    

When a zoo dataset is downloaded, a [`ZooDatasetInfo`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDatasetInfo "fiftyone.zoo.datasets.ZooDatasetInfo") instance is created in its root directory that contains additional information about the dataset, including which splits have been downloaded (if applicable).

You can load the [`ZooDatasetInfo`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDatasetInfo "fiftyone.zoo.datasets.ZooDatasetInfo") instance for a downloaded dataset via [`load_zoo_dataset_info()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset_info "fiftyone.zoo.datasets.load_zoo_dataset_info").

For example, letâs print some information about the CIFAR-10 dataset (assuming it is downloaded):
    
    
     1import fiftyone.zoo as foz
     2
     3dataset_dir = foz.find_zoo_dataset("cifar10")
     4info = foz.load_zoo_dataset_info("cifar10")
     5
     6print("***** Dataset location *****")
     7print(dataset_dir)
     8
     9print("\n***** Dataset info *****")
    10print(info)
    
    
    
    ***** Dataset location *****
    ~/fiftyone/cifar10
    
    ***** Dataset info *****
    {
        "name": "cifar10",
        "zoo_dataset": "fiftyone.zoo.datasets.torch.CIFAR10Dataset",
        "dataset_type": "fiftyone.types.dataset_types.ImageClassificationDataset",
        "num_samples": 10000,
        "downloaded_splits": {
            "test": {
                "split": "test",
                "num_samples": 10000
            }
        },
        "classes": [
            "airplane",
            "automobile",
            "bird",
            "cat",
            "deer",
            "dog",
            "frog",
            "horse",
            "ship",
            "truck"
        ]
    }
    

You can view detailed information about a dataset (either downloaded or not) via the [fiftyone zoo datasets info](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-info) command.

For example, you can view information about the CIFAR-10 dataset:
    
    
    fiftyone zoo datasets info cifar10
    
    
    
    ***** Dataset description *****
    The CIFAR-10 dataset consists of 60000 32 x 32 color images in 10
    classes, with 6000 images per class. There are 50000 training images and
    10000 test images.
    
    Dataset size:
        132.40 MiB
    
    Source:
        https://www.cs.toronto.edu/~kriz/cifar.html
    
    ***** Tags *****
    image, classification
    
    ***** Supported splits *****
    test, train
    
    ***** Dataset location *****
    ~/fiftyone/cifar10
    
    ***** Dataset info *****
    {
        "name": "cifar10",
        "zoo_dataset": "fiftyone.zoo.datasets.torch.CIFAR10Dataset",
        "dataset_type": "fiftyone.types.dataset_types.ImageClassificationDataset",
        "num_samples": 60000,
        "downloaded_splits": {
            "test": {
                "split": "test",
                "num_samples": 10000
            },
            "train": {
                "split": "train",
                "num_samples": 50000
            }
        },
        "classes": [
            "airplane",
            "automobile",
            "bird",
            "cat",
            "deer",
            "dog",
            "frog",
            "horse",
            "ship",
            "truck"
        ]
    }
    

## Downloading zoo datasets#

You can download zoo datasets (or individual split(s) of them) from the web via [`download_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.download_zoo_dataset "fiftyone.zoo.datasets.download_zoo_dataset").

For example, letâs download the `train` split of CIFAR-10:
    
    
    1import fiftyone.zoo as foz
    2
    3dataset = foz.download_zoo_dataset("cifar10", split="train")
    
    
    
    Downloading split 'train' to '~/fiftyone/cifar10/train'
    Downloading https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz to ~/fiftyone/cifar10/tmp-download/cifar-10-python.tar.gz
    170500096it [00:04, 34734776.49it/s]
    Extracting ~/fiftyone/cifar10/tmp-download/cifar-10-python.tar.gz to ~/fiftyone/cifar10/tmp-download
    Writing samples to '~/fiftyone/cifar10/train' in 'fiftyone.types.dataset_types.ImageClassificationDataset' format...
     100% |âââââââââââââââââââââââââââââââââââââââââââââ| 50000/50000 [24.3s elapsed, 0s remaining, 1.7K samples/s]
    Writing labels to '~/fiftyone/cifar10/train/labels.json'
    Dataset created
    Dataset info written to '~/fiftyone/cifar10/info.json'
    

You can download zoo datasets (or individual splits of them) from the web via the [fiftyone zoo datasets download](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-download) command.

For example, you can download the test split of the CIFAR-10 dataset as follows:
    
    
    fiftyone zoo datasets download cifar10 --splits test
    
    
    
    Downloading split 'test' to '~/fiftyone/cifar10/test'
    Downloading https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz to ~/fiftyone/cifar10/tmp-download/cifar-10-python.tar.gz
    170500096it [00:04, 34514685.48it/s]
    Extracting ~/fiftyone/cifar10/tmp-download/cifar-10-python.tar.gz to ~/fiftyone/cifar10/tmp-download
    Writing samples to '~/fiftyone/cifar10/test' in 'fiftyone.types.dataset_types.ImageClassificationDataset' format...
     100% |ââââââââââââââââââââââââââââââââââââââââââââââ| 10000/10000 [5.4s elapsed, 0s remaining, 1.9K samples/s]
    Writing labels to '~/fiftyone/cifar10/test/labels.json'
    Dataset created
    Dataset info written to '~/fiftyone/cifar10/info.json'
    

## Loading zoo datasets#

You can load a zoo dataset (or individual split(s) of them) via [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset").

By default, the dataset will be automatically downloaded from the web the first time you access it if it is not already downloaded:
    
    
     1import fiftyone.zoo as foz
     2
     3# The dataset will be downloaded from the web the first time you access it
     4dataset = foz.load_zoo_dataset("cifar10", split="test")
     5
     6# View summary info about the dataset
     7print(dataset)
     8
     9# Print the first few samples in the dataset
    10print(dataset.head())
    

You can also provide additional arguments to [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset") to customize the import behavior:
    
    
    1# Import a random subset of 10 samples from the zoo dataset
    2dataset = foz.load_zoo_dataset(
    3    "cifar10",
    4    split="test",
    5    dataset_name="cifar10-test-sample",
    6    shuffle=True,
    7    max_samples=10,
    8)
    

The additional arguments are passed directly to the [`DatasetImporter`](api__fiftyone.utils.data.importers.md#fiftyone.utils.data.importers.DatasetImporter "fiftyone.utils.data.importers.DatasetImporter") that performs the actual import.

After a zoo dataset has been downloaded from the web, you can load it as a FiftyOne dataset via the [fiftyone zoo datasets load](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-load) command.

For example, you can load the test split of the CIFAR-10 dataset as follows:
    
    
    fiftyone zoo datasets load cifar10 --splits test
    
    
    
    Split 'test' already downloaded
    Loading 'cifar10' split 'test'
     100% |ââââââââââââââââââââââââââââââââââââââââââââââ| 10000/10000 [3.6s elapsed, 0s remaining, 2.9K samples/s]
    Dataset 'cifar10-test' created
    

You can also provide [additional arguments](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-load) to customize the import behavior. For example, you can load a random subset of 10 samples from the zoo dataset:
    
    
    fiftyone zoo datasets load cifar10 --splits test \
        --dataset-name cifar10-test-sample --shuffle --max-samples 10
    
    
    
    Split 'test' already downloaded
    Loading 'cifar10' split 'test'
     100% |ââââââââââââââââââââââââââââââââââââââââââââââ| 10/10 [3.2ms elapsed, 0s remaining, 2.9K samples/s]
    Dataset 'cifar10-test' created
    

## Loading zoo datasets with manual downloads#

Some zoo datasets such as [`BDD100K`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.BDD100KDataset "fiftyone.zoo.datasets.base.BDD100KDataset") and [`Cityscapes`](api__fiftyone.zoo.datasets.base.md#fiftyone.zoo.datasets.base.CityscapesDataset "fiftyone.zoo.datasets.base.CityscapesDataset") require that you create accounts on a website and manually download the source files. In such cases, the [`ZooDataset`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDataset "fiftyone.zoo.datasets.ZooDataset") class will provide additional argument(s) that let you specify the paths to these files that you have manually downloaded on disk.

You can load these datasets into FiftyOne by first calling [`download_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.download_zoo_dataset "fiftyone.zoo.datasets.download_zoo_dataset") with the appropriate keyword arguments (which are passed to the underlying [`ZooDataset`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDataset "fiftyone.zoo.datasets.ZooDataset") constructor) to wrangle the raw download into FiftyOne format, and then calling [`load_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.load_zoo_dataset "fiftyone.zoo.datasets.load_zoo_dataset") or using [fiftyone zoo datasets load](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-load) to load the dataset into FiftyOne.

For example, the following snippet shows how to load the BDD100K dataset from the zoo:
    
    
    1import fiftyone.zoo as foz
    2
    3# First parse the manually downloaded files in `source_dir`
    4foz.download_zoo_dataset(
    5    "bdd100k", source_dir="/path/to/dir-with-bdd100k-files"
    6)
    7
    8# Now load into FiftyOne
    9dataset = foz.load_zoo_dataset("bdd100k", split="validation")
    

## Controlling where zoo datasets are downloaded#

By default, zoo datasets are downloaded into subdirectories of `fiftyone.config.dataset_zoo_dir` corresponding to their names.

You can customize this backend by modifying the `dataset_zoo_dir` setting of your [FiftyOne config](user_guide__config.md#configuring-fiftyone).

Directly edit your FiftyOne config at `~/.fiftyone/config.json`:
    
    
    # Print your current config
    fiftyone config
    
    # Locate your config (and edit the `dataset_zoo_dir` field)
    fiftyone constants FIFTYONE_CONFIG_PATH
    

Set the `FIFTYONE_DATASET_ZOO_DIR` environment variable:
    
    
    # Customize where zoo datasets are downloaded
    export FIFTYONE_DATASET_ZOO_DIR=/your/custom/directory
    

Set the `dataset_zoo_dir` config setting from Python code:
    
    
    1import fiftyone as fo
    2
    3# Customize where zoo datasets are downloaded
    4fo.config.dataset_zoo_dir = "/your/custom/directory"
    

## Deleting zoo datasets#

You can delete the local copy of a zoo dataset (or individual split(s) of them) via [`delete_zoo_dataset()`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.delete_zoo_dataset "fiftyone.zoo.datasets.delete_zoo_dataset"):
    
    
    1import fiftyone.zoo as foz
    2
    3foz.delete_zoo_dataset("cifar10", split="test")
    

You can delete the local copy of a zoo dataset (or individual split(s) of them) via the [fiftyone zoo datasets delete](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-delete) command:
    
    
    fiftyone zoo datasets delete cifar10 --splits test
    

## Adding datasets to the zoo#

We frequently add new built-in datasets to the Dataset Zoo, which will automatically become accessible to you when you update your FiftyOne package.

Note

FiftyOne is open source! You are welcome to contribute datasets to the public dataset zoo by submitting a pull request to [the GitHub repository](https://github.com/voxel51/fiftyone).

You can also add your own datasets to your local dataset zoo, enabling you to work with these datasets via the [`fiftyone.zoo.datasets`](api__fiftyone.zoo.datasets.md#module-fiftyone.zoo.datasets "fiftyone.zoo.datasets") package and the CLI using the same syntax that you would with publicly available datasets.

To add dataset(s) to your local zoo, you simply write a JSON manifest file in the format below to tell FiftyOne about the dataset. For example, the manifest below adds a second copy of the `quickstart` dataset to the zoo under the alias `quickstart-copy`:
    
    
    {
        "custom": {
            "quickstart-copy": "fiftyone.zoo.datasets.base.QuickstartDataset"
        }
    }
    

In the above, `custom` specifies the source of the dataset, which can be an arbitrary string and simply controls the column of the [fiftyone zoo datasets list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-datasets-list) listing in which the dataset is annotated; `quickstart-copy` is the name of the new dataset; and `fiftyone.zoo.datasets.base.QuickstartDataset` is the fully-qualified class name of the [`ZooDataset class`](api__fiftyone.zoo.datasets.md#fiftyone.zoo.datasets.ZooDataset "fiftyone.zoo.datasets.ZooDataset") for the dataset, which specifies how to download and load the dataset into FiftyOne. This class can be defined anywhere that is importable at runtime in your environment.

Finally, expose your new dataset(s) to FiftyOne by adding your manifest to the `dataset_zoo_manifest_paths` parameter of your [FiftyOne config](user_guide__config.md#configuring-fiftyone). One way to do this is to set the `FIFTYONE_DATASET_ZOO_MANIFEST_PATHS` environment variable:
    
    
    export FIFTYONE_DATASET_ZOO_MANIFEST_PATHS=/path/to/custom/manifest.json
    

Now you can access the `quickstart-copy` dataset as you would any other zoo dataset:
    
    
    # Will contain `quickstart-copy`
    fiftyone zoo datasets list
    
    # Load custom dataset into FiftyOne
    fiftyone zoo datasets load quickstart-copy
    

## Customizing your ML backend#

Behind the scenes, FiftyOne uses either [TensorFlow Datasets](https://www.tensorflow.org/datasets) or [TorchVision Datasets](https://pytorch.org/vision/stable/datasets.html) libraries to download and wrangle some zoo datasets, depending on which ML library you have installed. In order to load datasets using TF, you must have the [tensorflow-datasets](https://pypi.org/project/tensorflow-datasets) package installed on your machine. In order to load datasets using PyTorch, you must have the [torch](https://pypi.org/project/torch) and [torchvision](https://pypi.org/project/torchvision) packages installed.

Note that the ML backends may expose different datasets.

For datasets that require an ML backend, FiftyOne will use whichever ML backend is necessary to download the requested zoo dataset. If a dataset is available through both backends, it will use the backend specified by the `fo.config.default_ml_backend` setting in your FiftyOne config.

You can customize this backend by modifying the `default_ml_backend` setting of your [FiftyOne config](user_guide__config.md#configuring-fiftyone).

Directly edit your FiftyOne config at `~/.fiftyone/config.json`:
    
    
    # Print your current config
    fiftyone config
    
    # Locate your config (and edit the `default_ml_backend` field)
    fiftyone constants FIFTYONE_CONFIG_PATH
    

Set the `FIFTYONE_DEFAULT_ML_BACKEND` environment variable:
    
    
    # Use the `tensorflow` backend
    export FIFTYONE_DEFAULT_ML_BACKEND=tensorflow
    

Set the `default_ml_backend` config setting from Python code:
    
    
    1import fiftyone as fo
    2
    3# Use the `torch` backend
    4fo.config.default_ml_backend = "torch"
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
