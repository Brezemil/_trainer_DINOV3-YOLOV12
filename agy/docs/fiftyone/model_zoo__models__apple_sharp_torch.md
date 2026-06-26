---
source_url: https://docs.voxel51.com/model_zoo/models/apple_sharp_torch.html
---

# apple-sharp-torch#

Fast single-image to 3D Gaussian splat model generating photorealistic novel views in under one second.

**Details**

  * Model name: `apple-sharp-torch`

  * Model source: [apple/ml-sharp](https://github.com/apple/ml-sharp)

  * Model author: Lars Mescheder, et al.

  * Model license: Apple Sample Code License

  * Model size: 2.62 GB

  * Exposes embeddings? no

  * Tags: `3d, gaussian-splatting, novel-view, torch, transformer`




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
    12model = foz.load_zoo_model("apple-sharp-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
