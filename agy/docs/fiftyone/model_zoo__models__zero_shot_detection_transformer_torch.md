---
source_url: https://docs.voxel51.com/model_zoo/models/zero_shot_detection_transformer_torch.html
---

# zero-shot-detection-transformer-torch#

Hugging Face Transformers model for zero-shot object detection.

**Details**

  * Model name: `zero-shot-detection-transformer-torch`

  * Model source: <https://huggingface.co/docs/transformers/tasks/zero_shot_object_detection>

  * Model author: Thomas Wolf, et al.

  * Model license: Apache 2.0

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
    12classes = ["person", "dog", "cat", "bird", "car", "tree", "chair"]
    13
    14model = foz.load_zoo_model(
    15    "zero-shot-detection-transformer-torch",
    16    classes=classes,
    17)
    18
    19dataset.apply_model(model, label_field="predictions")
    20
    21session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
