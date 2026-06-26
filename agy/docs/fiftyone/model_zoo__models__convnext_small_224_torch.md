---
source_url: https://docs.voxel51.com/model_zoo/models/convnext_small_224_torch.html
---

# convnext-small-224-torch#

Small modernized CNN delivering strong accuracy through architectural innovations.

**Details**

  * Model name: `convnext-small-224-torch`

  * Model source: <https://huggingface.co/facebook/convnext-small-224>

  * Model author: Zhuang Liu, et al.

  * Model license: Apache 2.0

  * Model size: 383.39 MB

  * Exposes embeddings? yes

  * Tags: `classification, imagenet, torch, transformers, convnext, official, embeddings`




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
    12model = foz.load_zoo_model("convnext-small-224-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
