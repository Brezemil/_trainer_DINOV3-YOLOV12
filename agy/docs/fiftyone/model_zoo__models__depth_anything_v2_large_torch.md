---
source_url: https://docs.voxel51.com/model_zoo/models/depth_anything_v2_large_torch.html
---

# depth-anything-v2-large-torch#

High-accuracy Depth Anything V2 model for detailed monocular depth estimation.

**Details**

  * Model name: `depth-anything-v2-large-torch`

  * Model source: <https://huggingface.co/depth-anything/Depth-Anything-V2-Large-hf>

  * Model author: Lihe Yang, et al.

  * Model license: Apache 2.0

  * Model size: 1.25 GB

  * Exposes embeddings? no

  * Tags: `depth, 3d, torch, transformers`




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
    12model = foz.load_zoo_model("depth-anything-v2-large-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
