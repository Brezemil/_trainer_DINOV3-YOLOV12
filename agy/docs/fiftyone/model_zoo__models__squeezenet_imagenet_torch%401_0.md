---
source_url: https://docs.voxel51.com/model_zoo/models/squeezenet_imagenet_torch%401_0.html
---

# [squeezenet-imagenet-torch@1.0](mailto:squeezenet-imagenet-torch%401.0)#

Ultra-compact image classifier perfect for severely resource-constrained hardware and applications.

**Details**

  * Model name: `squeezenet-imagenet-torch@1.0`

  * Model source: <https://pytorch.org/vision/main/models.html>

  * Model author: Forrest Iandola

  * Model license: BSD 2-Clause

  * Model size: 4.79 MB

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
    11model = foz.load_zoo_model("squeezenet-imagenet-torch@1.0")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
