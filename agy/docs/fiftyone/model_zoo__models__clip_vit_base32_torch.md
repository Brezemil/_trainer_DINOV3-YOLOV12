---
source_url: https://docs.voxel51.com/model_zoo/models/clip_vit_base32_torch.html
---

# clip-vit-base32-torch#

Understands both images and text together, enabling search and classification using natural language descriptions.

**Details**

  * Model name: `clip-vit-base32-torch`

  * Model source: [openai/CLIP](https://github.com/openai/CLIP)

  * Model author: Alec Radford, et al.

  * Model license: MIT

  * Model size: 337.58 MB

  * Exposes embeddings? yes

  * Tags: `classification, logits, embeddings, torch, clip, zero-shot, transformer, official`




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
    12model = foz.load_zoo_model("clip-vit-base32-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    17
    18#
    19# Make zero-shot predictions with custom classes
    20#
    21
    22model = foz.load_zoo_model(
    23    "clip-vit-base32-torch",
    24    text_prompt="A photo of a",
    25    classes=["person", "dog", "cat", "bird", "car", "tree", "chair"],
    26)
    27
    28dataset.apply_model(model, label_field="predictions")
    29session.refresh()
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
