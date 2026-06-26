---
source_url: https://docs.voxel51.com/integrations/pytorch_hub.html
---

# PyTorch Hub Integration#

FiftyOne integrates natively with [PyTorch Hub](https://pytorch.org/hub), so you can load any Hub model and run inference on your FiftyOne datasets with just a few lines of code!

## Loading a model#

### Image models#

You can use the builtin [`load_torch_hub_image_model()`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.load_torch_hub_image_model "fiftyone.utils.torch.load_torch_hub_image_model") utility to load models from the PyTorch Hub:
    
    
    1import fiftyone.utils.torch as fout
    2
    3model = fout.load_torch_hub_image_model(
    4    "pytorch/vision",
    5    "resnet18",
    6    hub_kwargs=dict(weights="ResNet18_Weights.DEFAULT"),
    7)
    

The function returns a [`TorchImageModel`](api__fiftyone.utils.torch.md#fiftyone.utils.torch.TorchImageModel "fiftyone.utils.torch.TorchImageModel") instance that wraps the raw Torch model in FiftyOneâs [Model interface](model_zoo__design.md#model-zoo-design-overview), which means that you can directly pass the model to builtin methods like [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"), [`compute_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_embeddings "fiftyone.core.collections.SampleCollection.compute_embeddings"), [`compute_patch_embeddings()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.compute_patch_embeddings "fiftyone.core.collections.SampleCollection.compute_patch_embeddings"), [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization"), and [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity").
    
    
    1import fiftyone.zoo as foz
    2
    3dataset = foz.load_zoo_dataset("quickstart")
    4
    5dataset.limit(10).apply_model(model, label_field="resnet18")
    6
    7# Logits
    8print(dataset.first().resnet18.shape)  # (1000,)
    

Note

In the above example, the `resnet18` field is populated with raw logits. Refer to [this page](model_zoo__design.md#model-zoo-custom-models) to see how to configure output processors to automatically parse model outputs into FiftyOne [label types](https://docs.voxel51.com/user_guide/using_datasets.html#using-labels).

### Utilities#

FiftyOne also provides lower-level utilities for direct access to information about PyTorch Hub models:
    
    
     1import fiftyone.utils.torch as fout
     2
     3# Load a raw Hub model
     4model = fout.load_torch_hub_raw_model(
     5    "facebookresearch/dinov2",
     6    "dinov2_vits14",
     7)
     8print(type(model))
     9# <class 'dinov2.models.vision_transformer.DinoVisionTransformer'>
    10
    11# Locate the `requirements.txt` for the model on disk
    12req_path = fout.find_torch_hub_requirements("facebookresearch/dinov2")
    13print(req_path)
    14# '~/.cache/torch/hub/facebookresearch_dinov2_main/requirements.txt'
    15
    16# Load the package requirements for the model
    17requirements = fout.load_torch_hub_requirements("facebookresearch/dinov2")
    18print(requirements)
    19# ['torch==2.0.0', 'torchvision==0.15.0', ...]
    

### Example: YOLOv5#

Hereâs how to load [Ultralytics YOLOv5](https://docs.ultralytics.com/yolov5) and use it to generate object detections:
    
    
     1from PIL import Image
     2import numpy as np
     3
     4import fiftyone as fo
     5import fiftyone.zoo as foz
     6import fiftyone.utils.torch as fout
     7
     8class YOLOv5OutputProcessor(fout.OutputProcessor):
     9    """Transforms ``ultralytics/yolov5`` outputs to FiftyOne format."""
    10
    11    def __call__(self, result, frame_size, confidence_thresh=None):
    12        batch = []
    13        for df in result.pandas().xywhn:
    14            if confidence_thresh is not None:
    15                df = df[df["confidence"] >= confidence_thresh]
    16
    17            batch.append(self._to_detections(df))
    18
    19        return batch
    20
    21    def _to_detections(self, df):
    22        return fo.Detections(
    23            detections=[
    24                fo.Detection(
    25                    label=row.name,
    26                    bounding_box=[
    27                        row.xcenter - 0.5 * row.width,
    28                        row.ycenter - 0.5 * row.height,
    29                        row.width,
    30                        row.height,
    31                    ],
    32                    confidence=row.confidence,
    33                )
    34                for row in df.itertuples()
    35            ]
    36        )
    37
    38dataset = foz.load_zoo_dataset("quickstart")
    39
    40model = fout.load_torch_hub_image_model(
    41    "ultralytics/yolov5",
    42    "yolov5s",
    43    hub_kwargs=dict(pretrained=True),
    44    output_processor=YOLOv5OutputProcessor(),
    45    raw_inputs=True,
    46)
    47
    48# Generate predictions for a single image
    49img = np.asarray(Image.open(dataset.first().filepath))
    50predictions = model.predict(img)
    51print(predictions)  # <Detections: {...}>
    52
    53# Generate predictions for all images in a collection
    54dataset.limit(10).apply_model(model, label_field="yolov5")
    55dataset.count("yolov5.detections")  # 26
    

Note

Did you know? Ultralytics YOLOv5 is natively available in the [FiftyOne Model Zoo](model_zoo__models__yolov5m_coco_torch.md#model-zoo-yolov5m-coco-torch). You should also check out the [Ultralytics integration](integrations__ultralytics.md#ultralytics-integration)!

### Example: DINOv2#

Hereâs how to load [DINOv2](https://github.com/facebookresearch/dinov2) and use it to compute embeddings:
    
    
     1from PIL import Image
     2import numpy as np
     3
     4import fiftyone as fo
     5import fiftyone.zoo as foz
     6import fiftyone.utils.torch as fout
     7
     8dataset = foz.load_zoo_dataset("quickstart")
     9
    10model = fout.load_torch_hub_image_model(
    11    "facebookresearch/dinov2",
    12    "dinov2_vits14",
    13    image_patch_size=14,
    14    embeddings_layer="head",
    15)
    16assert model.has_embeddings
    17
    18# Embed a single image
    19img = np.asarray(Image.open(dataset.first().filepath))
    20embedding = model.embed(img)
    21print(embedding.shape)  # (384,)
    22
    23# Embed all images in a collection
    24embeddings = dataset.limit(10).compute_embeddings(model)
    25print(embeddings.shape)  # (10, 384)
    

Note

Did you know? DINOv2 is natively available in the [FiftyOne Model Zoo](model_zoo__models__dinov2_vitb14_torch.md#model-zoo-dinov2-vitb14-torch)!

## Adding Hub models to your local zoo#

You can add PyTorch Hub models to your [local model zoo](model_zoo__api.md#model-zoo-add) and then load and use them via the [`fiftyone.zoo`](api__fiftyone.zoo.md#module-fiftyone.zoo "fiftyone.zoo") package and the CLI using the same syntax that you would with the [publicly available models](https://docs.voxel51.com/model_zoo/index.html#model-zoo):
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4dataset = fo.load_dataset("...")
    5model = foz.load_zoo_model("your-custom-model")
    6
    7dataset.apply_model(model, ...)
    8dataset.compute_embeddings(model, ...)
    

### Example: DINOv2#

Hereâs how to add [DINOv2](https://github.com/facebookresearch/dinov2) to your local model zoo and then load it to compute embeddings.

  1. Create a custom manifest file and add DINOv2 to it:



    
    
    {
        "models": [
            {
                "base_name": "dinov2-vits14",
                "description": "DINOv2: Learning Robust Visual Features without Supervision. Model: ViT-S/14 distilled",
                "source": "https://github.com/facebookresearch/dinov2",
                "default_deployment_config_dict": {
                    "type": "fiftyone.utils.torch.TorchImageModel",
                    "config": {
                        "entrypoint_fcn": "fiftyone.utils.torch.load_torch_hub_raw_model",
                        "entrypoint_args": {
                            "repo_or_dir": "facebookresearch/dinov2",
                            "model": "dinov2_vits14"
                        },
                        "image_patch_size": 14,
                        "embeddings_layer": "head"
                    }
                }
            }
        ]
    }
    

  2. Expose your manifest to FiftyOne by setting this environment variable:



    
    
    export FIFTYONE_MODEL_ZOO_MANIFEST_PATHS=/path/to/custom-manifest.json
    

  3. Now you can load and use the model using [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model"):



    
    
     1import numpy as np
     2from PIL import Image
     3
     4import fiftyone as fo
     5import fiftyone.zoo as foz
     6
     7dataset = foz.load_zoo_dataset("quickstart")
     8
     9model = foz.load_zoo_model("dinov2-vits14")
    10assert model.has_embeddings
    11
    12# Embed a single image
    13img = np.asarray(Image.open(dataset.first().filepath))
    14embedding = model.embed(img)
    15print(embedding.shape)  # (384,)
    16
    17# Embed all images in a collection
    18embeddings = dataset.limit(10).compute_embeddings(model)
    19print(embeddings.shape)  # (10, 384)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
