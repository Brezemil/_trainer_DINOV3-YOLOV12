---
source_url: https://docs.voxel51.com/model_zoo/models/mnasnet0_5_imagenet_torch.html
---

# mnasnet0.5-imagenet-torch#

Ultra-lightweight image classifier designed by AI for running directly on phones and IoT devices.

**Details**

  * Model name: `mnasnet0.5-imagenet-torch`

  * Model source: <https://pytorch.org/vision/main/models.html>

  * Model author: Mingxing Tan, et al.

  * Model license: BSD 3-Clause

  * Model size: 8.59 MB

  * Exposes embeddings? yes

  * Tags: `classification, embeddings, logits, imagenet, torch, mnasnet, official`




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
    11model = foz.load_zoo_model("mnasnet0.5-imagenet-torch")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
