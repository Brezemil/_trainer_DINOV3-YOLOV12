---
source_url: https://docs.voxel51.com/model_zoo/models/siglip_base_patch16_224_torch.html
---

# siglip-base-patch16-224-torch#

Hugging Face Transformers model for zero-shot image classification.

**Details**

  * Model name: `siglip-base-patch16-224-torch`

  * Model source: <https://huggingface.co/docs/transformers/tasks/zero_shot_image_classification>

  * Model author: Thomas Wolf, et al.

  * Model license: Apache 2.0

  * Model size: 775.11 MB

  * Exposes embeddings? yes

  * Tags: `classification, logits, embeddings, torch, transformers, zero-shot, official`




**Requirements**

  * Packages: `torch, torchvision, transformers>=4.51`

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
    16    "siglip-base-patch16-224-torch",
    17    classes=classes,
    18)
    19
    20dataset.apply_model(model, label_field="predictions")
    21
    22session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
