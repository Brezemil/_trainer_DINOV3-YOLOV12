---
source_url: https://docs.voxel51.com/model_zoo/models/vit_base_patch16_224_imagenet_torch.html
---

# vit-base-patch16-224-imagenet-torch#

Modern image classifier that recognizes objects and provides useful features for various computer vision tasks.

**Details**

  * Model name: `vit-base-patch16-224-imagenet-torch`

  * Model source: <https://huggingface.co/docs/transformers/tasks/image_classification>

  * Model author: Thomas Wolf, et al.

  * Model license: Apache 2.0

  * Model size: 330.31 MB

  * Exposes embeddings? yes

  * Tags: `classification, logits, embeddings, torch, transformers, official`




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
     5    "imagenet-sample",
     6    dataset_name=fo.get_default_dataset_name(),
     7    max_samples=50,
     8    shuffle=True,
     9)
    10
    11model = foz.load_zoo_model("vit-base-patch16-224-imagenet-torch")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
