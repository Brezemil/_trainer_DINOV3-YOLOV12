---
source_url: https://docs.voxel51.com/model_zoo/design.html
---

# Model Interface#

All models in the Model Zoo are exposed via the [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") class, which defines a common interface for loading models and generating predictions with defined input and output data formats.

Note

If you write a wrapper for your custom model that implements the [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") interface, then you can pass your models to built-in methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") and [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings") too!

FiftyOne provides classes that make it easy to deploy models in custom frameworks easy. For example, if you have a PyTorch model that processes images, you can likely use [`TorchImageModel`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModel "fiftyone.utils.torch.TorchImageModel") to run it using FiftyOne.

## Prediction#

Inside built-in methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"), predictions of a [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") instance are generated using the following pattern:
    
    
     1import numpy as np
     2from PIL import Image
     3
     4import fiftyone as fo
     5
     6def read_rgb_image(path):
     7    """Utility function that loads an image as an RGB numpy array."""
     8    return np.asarray(Image.open(path).convert("rgb"))
     9
    10# Load a `Model` instance that processes images
    11model = ...
    12
    13# Load a FiftyOne dataset
    14dataset = fo.load_dataset(...)
    15
    16# A sample field in which to store the predictions
    17label_field = "predictions"
    18
    19# Perform prediction on all images in the dataset
    20with model:
    21    for sample in dataset:
    22        # Load image
    23        img = read_rgb_image(sample.filepath)
    24
    25        # Perform prediction
    26        labels = model.predict(img)
    27
    28        # Save labels
    29        sample.add_labels(labels, label_field=label_field)
    30        sample.save()
    
    
    
     1import eta.core.video as etav
     2
     3import fiftyone as fo
     4
     5# Load a `Model` instance that processes videos
     6model = ...
     7
     8# Load a FiftyOne dataset
     9dataset = fo.load_dataset(...)
    10
    11# A sample field in which to store the predictions
    12label_field = "predictions"
    13
    14# Perform prediction on all videos in the dataset
    15with model:
    16    for sample in dataset:
    17        # Perform prediction
    18        with etav.FFmpegVideoReader(sample.filepath) as video_reader:
    19            labels = model.predict(video_reader)
    20
    21        # Save labels
    22        sample.add_labels(labels, label_field=label_field)
    23        sample.save()
    

By convention, [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") instances must implement the context manager interface, which handles any necessary setup and teardown required to use the model.

Predictions are generated via the [`Model.predict()`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") interface method, which takes an image/video as input and returns the predictions.

In order to be compatible with built-in methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"), models should support the following basic signature of running inference and storing the output labels:
    
    
    1labels = model.predict(arg)
    2sample.add_labels(labels, label_field=label_field)
    

where the model should, at minimum, support `arg` values that are:

  * _Image models:_ uint8 numpy arrays (HWC)

  * _Video models:_ `eta.core.video.VideoReader` instances




and the output `labels` can be any of the following:

  * A [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instance, in which case the labels are directly saved in the specified `label_field` of the sample



    
    
    1# Single sample-level label
    2sample[label_field] = labels
    

  * A dict mapping keys to [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the labels are added as follows:



    
    
    1# Multiple sample-level labels
    2for key, value in labels.items():
    3    sample[label_key(key)] = value
    

  * A dict mapping frame numbers to [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:



    
    
    1# Single set of per-frame labels
    2sample.frames.merge(
    3    {
    4        frame_number: {label_field: label}
    5        for frame_number, label in labels.items()
    6    }
    7)
    

  * A dict mapping frame numbers to dicts mapping keys to [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances. In this case, the provided labels are interpreted as frame-level labels that should be added as follows:



    
    
    1# Multiple per-frame labels
    2sample.frames.merge(
    3    {
    4        frame_number: {label_key(k): v for k, v in frame_dict.items()}
    5        for frame_number, frame_dict in labels.items()
    6    }
    7)
    

In the above snippets, the `label_key` function maps label dict keys to field names, and is defined from `label_field` as follows:
    
    
    1if isinstance(label_field, dict):
    2    label_key = lambda k: label_field.get(k, k)
    3elif label_field is not None:
    4    label_key = lambda k: label_field + "_" + k
    5else:
    6    label_key = lambda k: k
    

For models that support batching, the [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") interface also provides a [`predict_all()`](api__fiftyone.core.models.md#fiftyone.core.models.Model.predict_all "fiftyone.core.models.Model.predict_all") method that can provide an efficient implementation of predicting on a batch of data.

Note

Built-in methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") provide a `batch_size` parameter that can be used to control the batch size used when performing inference with models that support efficient batching.

Note

PyTorch models can implement the [`TorchModelMixin`](api__fiftyone.core.models.md#fiftyone.core.models.TorchModelMixin "fiftyone.core.models.TorchModelMixin") mixin, in which case [DataLoaders](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader) are used to efficiently feed data to the models during inference.

## Embeddings#

Models that can compute embeddings for their input data can expose this capability by implementing the [`EmbeddingsMixin`](api__fiftyone.core.models.md#fiftyone.core.models.EmbeddingsMixin "fiftyone.core.models.EmbeddingsMixin") mixin.

Inside built-in methods like [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings"), embeddings for a collection of samples are generated using an analogous pattern to the prediction code shown above, except that the embeddings are generated using [`Model.embed()`](api__fiftyone.core.models.md#fiftyone.core.models.EmbeddingsMixin.embed "fiftyone.core.models.EmbeddingsMixin.embed") in place of [`Model.predict()`](api__fiftyone.core.models.md#fiftyone.core.models.Model.predict "fiftyone.core.models.Model.predict").

By convention, [`Model.embed()`](api__fiftyone.core.models.md#fiftyone.core.models.EmbeddingsMixin.embed "fiftyone.core.models.EmbeddingsMixin.embed") should return a numpy array containing the embedding.

Note

Embeddings are typically 1D vectors, but this is not strictly required.

For models that support batching, the [`EmbeddingsMixin`](api__fiftyone.core.models.md#fiftyone.core.models.EmbeddingsMixin "fiftyone.core.models.EmbeddingsMixin") interface also provides a [`embed_all()`](api__fiftyone.core.models.md#fiftyone.core.models.Model.predict_all "fiftyone.core.models.Model.predict_all") method that can provide an efficient implementation of embedding a batch of data.

## Logits#

Models that generate logits for their predictions can expose them to FiftyOne by implementing the [`LogitsMixin`](api__fiftyone.core.models.md#fiftyone.core.models.LogitsMixin "fiftyone.core.models.LogitsMixin") mixin.

Inside built-in methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"), if the user requests logits, the modelâs [`store_logits`](api__fiftyone.core.models.md#fiftyone.core.models.LogitsMixin.store_logits "fiftyone.core.models.LogitsMixin.store_logits") property is set to indicate that the model should store logits in the [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances that it produces during inference.

## Custom models#

FiftyOne provides a [`TorchImageModel`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModel "fiftyone.utils.torch.TorchImageModel") class that you can use to load your own custom Torch model and pass it to built-in methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") and [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings").

For example, the snippet below loads a pretrained model from `torchvision` and uses it both as a classifier and to generate image embeddings:
    
    
     1import os
     2import eta
     3
     4import fiftyone as fo
     5import fiftyone.zoo as foz
     6import fiftyone.utils.torch as fout
     7
     8dataset = foz.load_zoo_dataset("quickstart")
     9
    10labels_path = os.path.join(
    11    eta.constants.RESOURCES_DIR, "imagenet-labels-no-background.txt"
    12)
    13config = fout.TorchImageModelConfig(
    14    {
    15        "entrypoint_fcn": "torchvision.models.mobilenet.mobilenet_v2",
    16        "entrypoint_args": {"weights": "MobileNet_V2_Weights.DEFAULT"},
    17        "output_processor_cls": "fiftyone.utils.torch.ClassifierOutputProcessor",
    18        "labels_path": labels_path,
    19        "image_min_dim": 224,
    20        "image_max_dim": 2048,
    21        "image_mean": [0.485, 0.456, 0.406],
    22        "image_std": [0.229, 0.224, 0.225],
    23        "embeddings_layer": "<classifier.1",
    24    }
    25)
    26model = fout.TorchImageModel(config)
    27
    28dataset.apply_model(model, label_field="imagenet")
    29embeddings = dataset.compute_embeddings(model)
    

The necessary configuration is provided via the [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig") class, which exposes a number of built-in mechanisms for defining the model to load and any necessary preprocessing and post-processing.

Under the hood, the torch model is loaded via:
    
    
    torch_model = entrypoint_fcn(**entrypoint_args)
    

which is assumed to return a [`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module "\(in PyTorch v2.12\)") whose `__call__()` method directly accepts Torch tensors (NCHW) as input.

The [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig") class provides a number of built-in mechanisms for specifying the required preprocessing for your model, such as resizing and normalization. In the above example, `image_min_dim`, `image_max_dim`, `image_mean`, and `image_std` are used.

The `output_processor_cls` parameter of [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig") must be set to the fully-qualified class name of an [`OutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.OutputProcessor "fiftyone.utils.torch.OutputProcessor") subclass that defines how to translate the modelâs raw output into the suitable FiftyOne [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") types, and is instantiated as follows:
    
    
    output_processor = output_processor_cls(classes=classes, **output_processor_args)
    

where your modelâs classes can be specified via any of the `classes`, `labels_string`, or `labels_path` parameters of [`TorchImageModelConfig`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModelConfig "fiftyone.utils.torch.TorchImageModelConfig").

The following built-in output processors are available for use:

  * [`ClassifierOutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.ClassifierOutputProcessor "fiftyone.utils.torch.ClassifierOutputProcessor")

  * [`DetectorOutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.DetectorOutputProcessor "fiftyone.utils.torch.DetectorOutputProcessor")

  * [`InstanceSegmenterOutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.InstanceSegmenterOutputProcessor "fiftyone.utils.torch.InstanceSegmenterOutputProcessor")

  * [`KeypointDetectorOutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.KeypointDetectorOutputProcessor "fiftyone.utils.torch.KeypointDetectorOutputProcessor")

  * [`SemanticSegmenterOutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.SemanticSegmenterOutputProcessor "fiftyone.utils.torch.SemanticSegmenterOutputProcessor")




or you can write your own [`OutputProcessor`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.OutputProcessor "fiftyone.utils.torch.OutputProcessor") subclass.

Finally, if you would like to pass your custom model to methods like [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings"), set the `embeddings_layer` parameter to the name of a layer whose output to expose as embeddings (or prepend `<` to use the input tensor instead).

Note

Did you know? You can also [register your custom model](model_zoo__api.md#model-zoo-add) under a name of your choice so that it can be loaded and used as follows:
    
    
    model = foz.load_zoo_model("your-custom-model")
    dataset.apply_model(model, label_field="predictions")
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
