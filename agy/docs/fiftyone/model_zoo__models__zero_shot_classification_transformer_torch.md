---
source_url: https://docs.voxel51.com/model_zoo/models/zero_shot_classification_transformer_torch.html
---

# zero-shot-classification-transformer-torch#

Finds any object you name in images without requiring training on those specific items.

**Details**

  * Model name: `zero-shot-classification-transformer-torch`

  * Model source: <https://huggingface.co/docs/transformers/tasks/zero_shot_image_classification>

  * Model author: Thomas Wolf, et al.

  * Model license: Apache 2.0

  * Exposes embeddings? yes

  * Tags: `classification, logits, embeddings, torch, transformers, zero-shot, official`




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
    15    "zero-shot-classification-transformer-torch",
    16    classes=classes,
    17)
    18
    19dataset.apply_model(model, label_field="predictions")
    20
    21session = fo.launch_app(dataset)
    22
    23# some models make require additional arguments
    24# check the Hugging Face docs to see if any are needed
    25
    26# for example, AltCLIP requires `padding=True` in its processor
    27model = foz.load_zoo_model(
    28    "zero-shot-classification-transformer-torch",
    29    classes=classes,
    30    name_or_path="BAAI/AltCLIP",
    31    transformers_processor_kwargs={
    32        "padding": True,
    33    }
    34)
    35
    36dataset.apply_model(model, label_field="predictions")
    37
    38session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
