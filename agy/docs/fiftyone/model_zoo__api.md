---
source_url: https://docs.voxel51.com/model_zoo/api.html
---

# Model Zoo API Reference#

You can interact with the Model Zoo either via the Python library or the CLI.

The Model Zoo is accessible via the [`fiftyone.zoo`](api__fiftyone.zoo.md#module-fiftyone.zoo "fiftyone.zoo") package.

The [fiftyone zoo models](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models) command provides convenient utilities for working with models in the FiftyOne Model Zoo.

## Listing zoo models#

You can list the available zoo models via [`list_zoo_models()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.list_zoo_models "fiftyone.zoo.models.list_zoo_models"):
    
    
    1import fiftyone.zoo as foz
    2
    3available_models = foz.list_zoo_models()
    4
    5print(available_models)
    
    
    
    ['alexnet-imagenet-torch',
    'deeplabv3-cityscapes-tf',
    'deeplabv3-mnv2-cityscapes-tf',
    ...
    'wide-resnet50-2-imagenet-torch',
    'yolo-v2-coco-tf1'
    ]
    

To view the zoo models that you have downloaded, you can use [`list_downloaded_zoo_models()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.list_downloaded_zoo_models "fiftyone.zoo.models.list_downloaded_zoo_models"):
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4downloaded_models = foz.list_downloaded_zoo_models()
    5fo.pprint(downloaded_models)
    
    
    
    {
        'alexnet-imagenet-torch': (
            '/Users/Brian/fiftyone/__models__/alexnet-owt-4df8aa71.pth',
            <fiftyone.zoo.models.ZooModel object at 0x122d2fa58>,
        ),
        'densenet121-imagenet-torch': (
            '/Users/Brian/fiftyone/__models__/densenet121-a639ec97.pth',
            <fiftyone.zoo.models.ZooModel object at 0x122d608d0>,
        ),
        ...
    }
    

You can access information about the available zoo models via the [fiftyone zoo models list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-list) command.

For example, to list the available zoo models and whether you have downloaded them, you can execute:
    
    
    fiftyone zoo models list
    

Models that have been downloaded are indicated by a checkmark in the `downloaded` column, and their location on disk is indicated by the `model_path` column.

## Getting information about zoo models#

Each zoo model is represented by a [`ZooModel`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.ZooModel "fiftyone.zoo.models.ZooModel") subclass, which contains information about the model, its package requirements and CPU/GPU support, and more. You can access this object for a given model via the [`get_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.get_zoo_model "fiftyone.zoo.models.get_zoo_model") method.

For example, letâs print some information about a Faster R-CNN PyTorch model:
    
    
     1import fiftyone.zoo as foz
     2
     3zoo_model = foz.get_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
     4
     5print("***** Model description *****")
     6print(zoo_model.description)
     7
     8print("\n***** License *****")
     9print(zoo_model.license)
    10
    11print("\n***** Tags *****")
    12print(zoo_model.tags)
    13
    14print("\n***** Requirements *****")
    15print(zoo_model.requirements)
    
    
    
    ***** Model description *****
    Faster R-CNN model with ResNet-50 FPN backbone trained on COCO. Source: https://pytorch.org/docs/stable/torchvision/models.html
    
    ***** License *****
    BSD 3-Clause
    
    ***** Tags *****
    ['detection', 'coco', 'torch']
    
    ***** Requirements *****
    {
        "packages": [
            "torch",
            "torchvision"
        ],
        "cpu": {
            "support": true
        },
        "gpu": {
            "support": true
        }
    }
    

When a zoo model is downloaded, you can use [`find_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.find_zoo_model "fiftyone.zoo.models.find_zoo_model") to locate the downloaded model on disk:

For example, letâs get the path on disk to the Faster R-CNN model referenced above (assuming it is downloaded):
    
    
    1import fiftyone.zoo as foz
    2
    3model_path = foz.find_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
    

You can view detailed information about a model (either downloaded or not) via the [fiftyone zoo models info](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-info) command.

For example, you can view information about a Faster R-CNN PyTorch model:
    
    
    fiftyone zoo models info faster-rcnn-resnet50-fpn-coco-torch
    
    
    
    ***** Model description *****
    {
        "base_name": "faster-rcnn-resnet50-fpn-coco-torch",
        "base_filename": "fasterrcnn_resnet50_fpn_coco-258fb6c6.pth",
        "author": "Shaoqing Ren, et al.",
        "version": null,
        "url": null,
        "source": "https://pytorch.org/vision/main/models.html",
        "license": "BSD 3-Clause",
        "description": "Faster R-CNN model from `Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks <https://arxiv.org/abs/1506.01497>`_ with ResNet-50 FPN backbone trained on COCO",
        "size_bytes": 167502836,
        "manager": {
            "type": "fiftyone.core.models.ModelManager",
            "config": {
                "url": "https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth"
            }
        },
        "default_deployment_config_dict": {
            "type": "fiftyone.zoo.models.torch.TorchvisionImageModel",
            "config": {
                "entrypoint_fcn": "torchvision.models.detection.faster_rcnn.fasterrcnn_resnet50_fpn",
                "entrypoint_args": {
                    "weights": "FasterRCNN_ResNet50_FPN_Weights.DEFAULT"
                },
                "output_processor_cls": "fiftyone.utils.torch.DetectorOutputProcessor",
                "labels_path": "{{eta-resources}}/ms-coco-labels.txt",
                "confidence_thresh": 0.3
            }
        },
        "requirements": {
            "packages": [
                "torch",
                "torchvision"
            ],
            "cpu": {
                "support": true
            },
            "gpu": {
                "support": true
            }
        },
        "tags": [
            "detection",
            "coco",
            "torch",
            "faster-rcnn",
            "resnet"
        ],
        "date_added": "2020-12-11T13:45:51"
    }
    
    ***** Model location *****
    /Users/Brian/fiftyone/__models__/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth
    

## Downloading zoo models#

You can download zoo models from the web via [`download_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.download_zoo_model "fiftyone.zoo.models.download_zoo_model").

For example, letâs download a Faster R-CNN PyTorch model:
    
    
    1import fiftyone.zoo as foz
    2
    3model_path = foz.download_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
    
    
    
    Downloading model from 'https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth'...
     100% |ââââââââââââââââââââââââââââââââââ|    1.2Gb/1.2Gb [4.7s elapsed, 0s remaining, 294.7Mb/s]
    

You can download zoo models from the web via the [fiftyone zoo models download](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-download) command.

For example, you can download a Faster R-CNN PyTorch model as follows:
    
    
    fiftyone zoo models download faster-rcnn-resnet50-fpn-coco-torch
    
    
    
    Downloading model from 'https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth'...
     100% |ââââââââââââââââââââââââââââââââââ|    1.2Gb/1.2Gb [4.7s elapsed, 0s remaining, 294.7Mb/s]
    

## Installing zoo model requirements#

Some models in the FiftyOne Model Zoo may require packages that are not installed by default when FiftyOne is installed.

You can check to see if your current environment satisfies the requirements for a particular zoo model via [`ensure_zoo_model_requirements()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.ensure_zoo_model_requirements "fiftyone.zoo.models.ensure_zoo_model_requirements"):
    
    
    1import fiftyone.zoo as foz
    2
    3# Raises an error if the requirements are not satisfied
    4foz.ensure_zoo_model_requirements("faster-rcnn-resnet50-fpn-coco-torch")
    

You can also use [`install_zoo_model_requirements()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.install_zoo_model_requirements "fiftyone.zoo.models.install_zoo_model_requirements") to install any necessary packages for a particular model:
    
    
    1import fiftyone.zoo as foz
    2
    3foz.install_zoo_model_requirements("faster-rcnn-resnet50-fpn-coco-torch")
    

Some models in the FiftyOne Model Zoo may require packages that are not installed by default when FiftyOne is installed.

You can view the requirements for a zoo model via the [fiftyone zoo models requirements](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-requirements) command:
    
    
    fiftyone zoo models requirements faster-rcnn-resnet50-fpn-coco-torch
    
    
    
    ***** Model requirements *****
    {
        "packages": [
            "torch",
            "torchvision"
        ],
        "cpu": {
            "support": true
        },
        "gpu": {
            "support": true
        }
    }
    
    ***** Current machine *****
    GPU: no
    

You can use the `--ensure` flag to check to see if your current environment satisfies the requirements for a particular zoo model:
    
    
    # Raises an error if the requirements are not satisfied
    fiftyone zoo models requirements --ensure faster-rcnn-resnet50-fpn-coco-torch
    

You can also use the `--install` flag to install any necessary packages for a particular zoo model:
    
    
    fiftyone zoo models requirements --install faster-rcnn-resnet50-fpn-coco-torch
    

## Loading zoo models#

You can load a zoo model via [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model").

By default, the model will be automatically downloaded from the web the first time you access it if it is not already downloaded:
    
    
    1import fiftyone.zoo as foz
    2
    3# The model will be downloaded from the web the first time you access it
    4model = foz.load_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
    

You can also provide additional arguments to [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model") to customize the import behavior:
    
    
    1# Load the zoo model and install any necessary requirements in order to
    2# use it (logging warnings if any issues arise)
    3model = foz.load_zoo_model(
    4    "faster-rcnn-resnet50-fpn-coco-torch",
    5    install_requirements=True,
    6    error_level=1,
    7)
    

Note

By default, FiftyOne will attempt to ensure that any requirements such as Python packages or CUDA versions are satisfied before loading the model, and an error will be raised if a requirement is not satisfied.

You can customize this behavior via the `error_level` argument to [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model"), or you can permanently adjust this behavior by setting the `requirement_error_level` parameter of your [FiftyOne config](user_guide__config.md#configuring-fiftyone).

An `error_level` of `0` will raise an error if a requirement is not satisfied, `1` will log a warning if the requirement is not satisfied, and `2` will ignore unsatisfied requirements.

If you are using a `conda` environment, it is recommended you use an `error_level` of `1` or `2`, since FiftyOne uses `pip` to check for requirements.

## Applying zoo models#

You can run inference on a dataset (or a subset of it specified by a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")) with a zoo model by loading it and then calling [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"):

For example, the snippet below loads the `faster-rcnn-resnet50-fpn-coco-torch` model from the Model Zoo and applies it to 10 random images from the `quickstart` dataset from the Dataset Zoo:
    
    
     1import fiftyone.zoo as foz
     2
     3# Load zoo model
     4model = foz.load_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
     5
     6# Load zoo dataset
     7dataset = foz.load_zoo_dataset("quickstart")
     8samples = dataset.take(10)
     9
    10# Run inference
    11samples.apply_model(model, label_field="faster_rcnn")
    

You can run inference on a dataset with a zoo model via the [fiftyone zoo models apply](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-apply) command.

For example, the snippet below loads the `quickstart` dataset from the Dataset Zoo and applies the `faster-rcnn-resnet50-fpn-coco-torch` model from the Model Zoo to it:
    
    
    # Load zoo dataset
    fiftyone zoo datasets load quickstart
    
    # Apply zoo model
    fiftyone zoo models apply \
        faster-rcnn-resnet50-fpn-coco-torch \   # model
        quickstart \                            # dataset
        faster_rcnn                             # label field
    

## Generating embeddings with zoo models#

Many models in the Model Zoo expose embeddings for their predictions. You can determine if a model supports embeddings by loading it and checking the [`Model.has_embeddings`](api__fiftyone.core.models.md#fiftyone.core.models.Model.has_embeddings "fiftyone.core.models.Model.has_embeddings") attribute:
    
    
    1import fiftyone.zoo as foz
    2
    3# Load zoo model
    4model = foz.load_zoo_model("inception-v3-imagenet-torch")
    5
    6# Check if model exposes embeddings
    7model.has_embeddings  # True
    

For models that expose embeddings, you can generate embeddings for all samples in a dataset (or a subset of it specified by a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")) by calling [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings"):
    
    
     1import fiftyone.zoo as foz
     2
     3# Load zoo model
     4model = foz.load_zoo_model("inception-v3-imagenet-torch")
     5model.has_embeddings  # True
     6
     7# Load zoo dataset
     8dataset = foz.load_zoo_dataset("quickstart")
     9samples = dataset.take(10)
    10
    11# Generate embeddings for each sample and return them in a
    12# `num_samples x dim` array
    13embeddings = samples.compute_embeddings(model)
    14
    15# Generate embeddings for each sample and store them in a sample field
    16samples.compute_embeddings(model, embeddings_field="embeddings")
    

You can also use [`compute_patch_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_patch_embeddings "fiftyone.core.collections.SampleCollection.compute_patch_embeddings") to generate embeddings for image patches defined by another label field, e.g,. the detections generated by a detection model.

For models that expose embeddings, you can generate embeddings for all samples in a dataset via the [fiftyone zoo models embed](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-embed) command.

For example, the snippet below loads the `quickstart` dataset from the Dataset Zoo and generates embeddings for each sample using the `inception-v3-imagenet-torch` model from the Model Zoo:
    
    
    # Load zoo dataset
    fiftyone zoo datasets load quickstart
    
    # Generate embeddings via zoo model
    fiftyone zoo models embed \
        inception-v3-imagenet-torch \           # model
        quickstart \                            # dataset
        embeddings                              # embeddings field
    

## Controlling where zoo models are downloaded#

By default, zoo models are downloaded into subdirectories of `fiftyone.config.model_zoo_dir` corresponding to their names.

You can customize this backend by modifying the `model_zoo_dir` setting of your [FiftyOne config](user_guide__config.md#configuring-fiftyone).

Directly edit your FiftyOne config at `~/.fiftyone/config.json`:
    
    
    # Print your current config
    fiftyone config
    
    # Locate your config (and edit the `model_zoo_dir` field)
    fiftyone constants FIFTYONE_CONFIG_PATH
    

Set the `FIFTYONE_MODEL_ZOO_DIR` environment variable:
    
    
    # Customize where zoo models are downloaded
    export FIFTYONE_MODEL_ZOO_DIR=/your/custom/directory
    

Set the `model_zoo_dir` config setting from Python code:
    
    
    1import fiftyone as fo
    2
    3# Customize where zoo models are downloaded
    4fo.config.model_zoo_dir = "/your/custom/directory"
    

## Deleting zoo models#

You can delete the local copy of a zoo model via [`delete_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.delete_zoo_model "fiftyone.zoo.models.delete_zoo_model"):
    
    
    1import fiftyone.zoo as foz
    2
    3foz.delete_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
    

You can delete the local copy of a zoo model via the [fiftyone zoo models delete](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-delete) command:
    
    
    fiftyone zoo models delete faster-rcnn-resnet50-fpn-coco-torch
    

## Adding models to the zoo#

We frequently add new models to the Model Zoo, which will automatically become accessible to you when you update your FiftyOne package.

Note

FiftyOne is open source! You are welcome to contribute models to the public model zoo by submitting a pull request to [the GitHub repository](https://github.com/voxel51/fiftyone).

You can also add your own models to your local model zoo, enabling you to work with these models via the [`fiftyone.zoo`](api__fiftyone.zoo.md#module-fiftyone.zoo "fiftyone.zoo") package and the CLI using the same syntax that you would with publicly available models.

To add model(s) to your local zoo, you simply write a JSON manifest file in the format below to tell FiftyOne about the model(s). For example, the manifest below adds a second copy of the `yolo-v2-coco-tf1` model to the zoo under the alias `yolo-v2-coco-tf1-high-conf` that only returns predictions whose confidence is at least 0.5:
    
    
    {
        "models": [
            {
                "base_name": "yolo-v2-coco-tf1-high-conf",
                "base_filename": "yolo-v2-coco-high-conf.weights",
                "version": null,
                "description": "A YOLOv2 model with confidence threshold set to 0.5",
                "manager": {
                    "type": "fiftyone.core.models.ModelManager",
                    "config": {
                        "google_drive_id": "1ajuPZws47SOw3xJc4Wvk1yuiB3qv8ycr"
                    }
                },
                "default_deployment_config_dict": {
                    "type": "fiftyone.utils.eta.ETAModel",
                    "config": {
                        "type": "eta.detectors.YOLODetector",
                        "config": {
                            "config_dir": "{{eta}}/tensorflow/darkflow/cfg/",
                            "config_path": "{{eta}}/tensorflow/darkflow/cfg/yolo.cfg",
                            "confidence_thresh": 0.5
                        }
                    }
                },
                "requirements": {
                    "cpu": {
                        "support": true,
                        "packages": ["tensorflow<2"]
                    },
                    "gpu": {
                        "support": true,
                        "packages": ["tensorflow-gpu<2"]
                    }
                },
                "tags": ["detection", "coco", "tf1"],
                "date_added": "2020-12-11 13:45:51"
            }
        ]
    }
    

Note

Adjusting the hard-coded threshold of the above model is possible via JSON-only changes in this case because the underlying [eta.detectors.YOLODetector](https://github.com/voxel51/eta/blob/develop/eta/detectors/yolo.py) class exposes this as a parameter.

In practice, there is no need to hard-code confidence thresholds in models, since the [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") method supports supplying an optional confidence threshold that is applied post-facto to the predictions generated by any model.

Models manifest JSON files should have a `models` key that contains a list of serialized [`ZooModel class definitions`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.ZooModel "fiftyone.zoo.models.ZooModel") that describe how to download and load the model.

Finally, expose your new models(s) to FiftyOne by adding your manifest to the `model_zoo_manifest_paths` parameter of your [FiftyOne config](user_guide__config.md#configuring-fiftyone). One way to do this is to set the `FIFTYONE_MODEL_ZOO_MANIFEST_PATHS` environment variable:
    
    
    export FIFTYONE_MODEL_ZOO_MANIFEST_PATHS=/path/to/custom/manifest.json
    

Now you can load and apply the `yolo-v2-coco-tf1-high-conf` model as you would any other zoo model:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # Load custom model
    model = foz.load_zoo_model("yolo-v2-coco-tf1-high-conf")
    
    # Apply model to a dataset
    dataset = fo.load_dataset(...)
    dataset.apply_model(model, label_field="predictions")
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
