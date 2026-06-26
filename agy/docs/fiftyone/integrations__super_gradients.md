---
source_url: https://docs.voxel51.com/integrations/super_gradients.html
---

# Super Gradients Integration#

FiftyOne integrates natively with Deci AIâs [SuperGradients](https://github.com/Deci-AI/super-gradients) library, so you can run inference with YOLO-NAS architectures on your FiftyOne datasets with just a few lines of code!

## Setup#

To get started with [SuperGradients](https://github.com/Deci-AI/super-gradients), just install the `super-gradients` package:
    
    
    pip install super-gradients
    

## Inference#

You can directly pass SuperGradients YOLO-NAS models to your FiftyOne datasetâs [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model") method:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4from super_gradients.training import models
     5
     6dataset = foz.load_zoo_dataset("quickstart", max_samples=25)
     7dataset.select_fields().keep_fields()
     8
     9model = models.get("yolo_nas_m", pretrained_weights="coco")
    10# model = models.get("yolo_nas_l", pretrained_weights="coco")
    11# model = models.get("yolo_nas_s", pretrained_weights="coco")
    12
    13dataset.apply_model(model, label_field="yolo_nas", confidence_thresh=0.7)
    14
    15session = fo.launch_app(dataset)
    

## Model zoo#

SuperGradients YOLO-NAS is also available directly from the [FiftyOne Model Zoo](model_zoo__models__yolo_nas_torch.md#model-zoo-yolo-nas-torch)!
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4model = foz.load_zoo_model("yolo-nas-torch")
    5
    6dataset = foz.load_zoo_dataset("quickstart")
    7dataset.apply_model(model, label_field="yolo_nas")
    8
    9session = fo.launch_app(dataset)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
