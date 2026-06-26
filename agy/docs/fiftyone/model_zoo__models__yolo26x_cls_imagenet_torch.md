---
source_url: https://docs.voxel51.com/model_zoo/models/yolo26x_cls_imagenet_torch.html
---

# yolo26x-cls-imagenet-torch#

Maximum accuracy image classifier.

**Details**

  * Model name: `yolo26x-cls-imagenet-torch`

  * Model source: <https://docs.ultralytics.com/models/yolo26/>

  * Model author: Glenn Jocher, et al.

  * Model license: AGPL-3.0

  * Model size: 56.85 MB

  * Exposes embeddings? no

  * Tags: `classification, imagenet, torch, yolo, official`




**Requirements**

  * Packages: `torch>=1.7.0, torchvision>=0.8.1, ultralytics>=8.4.0`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset(
     5    "imagenet-sample",
     6    dataset_name=fo.get_default_dataset_name(),
     7    max_samples=50,
     8    shuffle=True,
     9)
    10
    11model = foz.load_zoo_model("yolo26x-cls-imagenet-torch")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
