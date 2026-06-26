---
source_url: https://docs.voxel51.com/model_zoo/models/efficientnet_b0_imagenet_torch.html
---

# efficientnet-b0-imagenet-torch#

Efficient image classifier optimized for mobile devices with excellent accuracy-efficiency tradeoff.

**Details**

  * Model name: `efficientnet-b0-imagenet-torch`

  * Model source: <https://huggingface.co/google/efficientnet-b0>

  * Model author: Mingxing Tan and Quoc V. Le

  * Model license: Apache 2.0

  * Model size: 81.80 MB

  * Exposes embeddings? yes

  * Tags: `classification, imagenet, torch, transformers, efficientnet, official, embeddings`




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
    11model = foz.load_zoo_model("efficientnet-b0-imagenet-torch")
    12
    13dataset.apply_model(model, label_field="predictions")
    14
    15session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
