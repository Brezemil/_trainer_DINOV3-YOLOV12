---
source_url: https://docs.voxel51.com/model_zoo/models/squeezenet_1%401_1_1_imagenet_torch.html
---

# [squeezenet-1@1.1.1-imagenet-torch](mailto:squeezenet-1%401.1.1-imagenet-torch)#

Tiny image classifier that fits in just five megabytes for embedded devices.

**Details**

  * Model name: `squeezenet-1@1.1.1-imagenet-torch`

  * Model source: <https://pytorch.org/vision/main/models.html>

  * Model author: Forrest Iandola

  * Model license: BSD 2-Clause

  * Model size: 4.74 MB

  * Exposes embeddings? no

  * Tags: `classification, imagenet, torch, squeezenet, official`




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
     5    "imagenet-sample",
     6    dataset_name=fo.get_default_dataset_name(),
     7    max_samples=50,
     8    shuffle=True,
     9)
    10
    11model = foz.load_zoo_model("squeezenet-1@1.1.1-imagenet-torch")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
