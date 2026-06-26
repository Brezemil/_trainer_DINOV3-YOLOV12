---
source_url: https://docs.voxel51.com/model_zoo/models/dinov2_vitl14_torch.html
---

# dinov2-vitl14-torch#

Large model that creates detailed image fingerprints for advanced search and automatic grouping.

**Details**

  * Model name: `dinov2-vitl14-torch`

  * Model source: [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2)

  * Model author: Maxime Oquab, et al.

  * Model license: Apache 2.0

  * Model size: 1.13 GB

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
    12model = foz.load_zoo_model("dinov2-vitl14-torch")
    13
    14embeddings = dataset.compute_embeddings(model)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
