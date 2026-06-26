---
source_url: https://docs.voxel51.com/model_zoo/models/fcn_resnet101_coco_torch.html
---

# fcn-resnet101-coco-torch#

Creates detailed pixel-level labels for images, identifying and outlining twenty-one different object categories.

**Details**

  * Model name: `fcn-resnet101-coco-torch`

  * Model source: <https://pytorch.org/vision/main/models.html>

  * Model author: Jonathan Long, et al.

  * Model license: BSD 3-Clause

  * Model size: 207.71 MB

  * Exposes embeddings? no

  * Tags: `segmentation, coco, torch, fcn, resnet, official`




**Requirements**

  * Packages: `torch, torchvision`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset(
     5    "coco-2017",
     6    split="validation",
     7    dataset_name=fo.get_default_dataset_name(),
     8    max_samples=50,
     9    shuffle=True,
    10)
    11
    12model = foz.load_zoo_model("fcn-resnet101-coco-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
