---
source_url: https://docs.voxel51.com/model_zoo/models/swin_v2_large_torch.html
---

# swin-v2-large-torch#

Large hierarchical transformer with enhanced capacity for demanding applications.

**Details**

  * Model name: `swin-v2-large-torch`

  * Model source: <https://huggingface.co/microsoft/swinv2-large-patch4-window12to16-192to256-22kto1k-ft>

  * Model author: Ze Liu, et al.

  * Model license: MIT

  * Model size: 2.93 GB

  * Exposes embeddings? yes

  * Tags: `classification, imagenet, torch, transformers, swin-transformer, official, embeddings`




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
    12model = foz.load_zoo_model("swin-v2-large-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
