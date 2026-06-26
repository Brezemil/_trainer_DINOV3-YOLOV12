---
source_url: https://docs.voxel51.com/model_zoo/models/depth_anything_v3_mono_large_torch.html
---

# depth-anything-v3-mono-large-torch#

Depth Anything V3 monocular model with relative depth and sky segmentation.

**Details**

  * Model name: `depth-anything-v3-mono-large-torch`

  * Model source: [ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)

  * Model author: Lihe Yang, et al.

  * Model license: CC BY-NC 4.0

  * Model size: 1.24 GB

  * Exposes embeddings? no

  * Tags: `depth, 3d, torch, transformer, sky`




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
    12model = foz.load_zoo_model("depth-anything-v3-mono-large-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
