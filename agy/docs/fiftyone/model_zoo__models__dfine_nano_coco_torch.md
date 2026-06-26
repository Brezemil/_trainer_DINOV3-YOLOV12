---
source_url: https://docs.voxel51.com/model_zoo/models/dfine_nano_coco_torch.html
---

# dfine-nano-coco-torch#

D-FINE Nano from D-FINE: Redefine Regression Task in DETRs as Fine-grained Distribution Refinement trained on COCO. Ultra-lightweight real-time object detector..

**Details**

  * Model name: `dfine-nano-coco-torch`

  * Model source: [Peterande/D-FINE](https://github.com/Peterande/D-FINE)

  * Model author: Yansong Peng, et al.

  * Model license: Apache 2.0

  * Model size: 14.00 MB

  * Exposes embeddings? yes

  * Tags: `detection, coco, embeddings, torch, transformers, detr, official`




**Requirements**

  * Packages: `torch, torchvision, transformers`

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
    12model = foz.load_zoo_model("dfine-nano-coco-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
