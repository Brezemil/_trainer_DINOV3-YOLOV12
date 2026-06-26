---
source_url: https://docs.voxel51.com/model_zoo/models/dinov2_vits14_reg_torch.html
---

# dinov2-vits14-reg-torch#

Compact stable model for image search that runs efficiently on phones and edge devices.

**Details**

  * Model name: `dinov2-vits14-reg-torch`

  * Model source: [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

  * Model author: Maxime Oquab, et al.

  * Model license: Apache 2.0

  * Model size: 84.20 MB

  * Exposes embeddings? yes

  * Tags: `embeddings, torch, dinov2, transformer, official`




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
     5    "coco-2017",
     6    split="validation",
     7    dataset_name=fo.get_default_dataset_name(),
     8    max_samples=50,
     9    shuffle=True,
    10)
    11
    12model = foz.load_zoo_model("dinov2-vits14-reg-torch")
    13
    14embeddings = dataset.compute_embeddings(model)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
