---
source_url: https://docs.voxel51.com/model_zoo/models/rfdetr_seg_xlarge_coco_torch.html
---

# rfdetr-seg-xlarge-coco-torch#

RF-DETR Seg XLarge instance segmentation model trained on COCO. Very high accuracy..

**Details**

  * Model name: `rfdetr-seg-xlarge-coco-torch`

  * Model source: [roboflow/rf-detr](https://github.com/roboflow/rf-detr)

  * Model author: Roboflow

  * Model license: Apache 2.0

  * Model size: 144.96 MB

  * Exposes embeddings? no

  * Tags: `instances, coco, torch, transformer, rfdetr, official`




**Requirements**

  * Packages: `torch, torchvision, rfdetr`

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
    12model = foz.load_zoo_model("rfdetr-seg-xlarge-coco-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
