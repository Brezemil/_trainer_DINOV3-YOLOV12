---
source_url: https://docs.voxel51.com/model_zoo/models/open_clip_torch.html
---

# open-clip-torch#

Connects images with text descriptions enabling search by words and automatic content filtering systems.

**Details**

  * Model name: `open-clip-torch`

  * Model source: [mlfoundations/open_clip](https://github.com/mlfoundations/open_clip)

  * Model author: Gabriel Ilharco, et al.

  * Model license: MIT

  * Exposes embeddings? yes

  * Tags: `classification, logits, embeddings, torch, clip, zero-shot, transformer`




**Requirements**

  * Packages: `torch, torchvision, open_clip_torch`

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
    12model = foz.load_zoo_model("open-clip-torch")
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
    23    "open-clip-torch",
    24    text_prompt="A photo of a",
    25    classes=["person", "dog", "cat", "bird", "car", "tree", "chair"],
    26)
    27
    28dataset.apply_model(model, label_field="predictions")
    29session.refresh()
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
