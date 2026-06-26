---
source_url: https://docs.voxel51.com/model_zoo/models/yolo_nas_torch.html
---

# yolo-nas-torch#

AI-designed detector family offering three model variants for diverse deployment scenarios.

**Details**

  * Model name: `yolo-nas-torch`

  * Model source: [Deci-AI/super-gradients](https://github.com/Deci-AI/super-gradients)

  * Model author: Shay Aharon, et al.

  * Model license: Apache 2.0

  * Exposes embeddings? no

  * Tags: `detection, torch, yolo, official`




**Requirements**

  * Packages: `torch, torchvision, super-gradients`

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
    12model = foz.load_zoo_model("yolo-nas-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
