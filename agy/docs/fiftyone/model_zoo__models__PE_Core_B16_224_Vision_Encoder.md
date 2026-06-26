---
source_url: https://docs.voxel51.com/model_zoo/models/PE_Core_B16_224_Vision_Encoder.html
---

# PE-Core-B16-224-Vision-Encoder#

The ViT from the base variant of the PE Core line of models..

**Details**

  * Model name: `PE-Core-B16-224-Vision-Encoder`

  * Model source: [facebookresearch/perception_models](https://github.com/facebookresearch/perception_models/)

  * Model author: Daniel Bolya, et al.

  * Model license: Apache 2.0

  * Model size: 1.67 GB

  * Exposes embeddings? yes

  * Tags: `embeddings, torch`




**Requirements**

  * Packages: `torch, torchvision, perception_models`

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
    12model = foz.load_zoo_model("PE-Core-B16-224-Vision-Encoder")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
