---
source_url: https://docs.voxel51.com/model_zoo/models/owlvit_base_patch32_torch.html
---

# owlvit-base-patch32-torch#

Finds any object you name in pictures using efficient 32x32 image patches without needing specific training.

**Details**

  * Model name: `owlvit-base-patch32-torch`

  * Model source: <https://huggingface.co/docs/transformers/tasks/zero_shot_object_detection>

  * Model author: Thomas Wolf, et al.

  * Model license: Apache 2.0

  * Model size: 1.14 GB

  * Exposes embeddings? no

  * Tags: `detection, logits, torch, transformers, zero-shot, official`




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
    12
    13classes = ["person", "dog", "cat", "bird", "car", "tree", "chair"]
    14
    15model = foz.load_zoo_model(
    16    "owlvit-base-patch32-torch",
    17    classes=classes,
    18)
    19
    20dataset.apply_model(model, label_field="predictions")
    21
    22session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
