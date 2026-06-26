---
source_url: https://docs.voxel51.com/model_zoo/models/group_vit_segmentation_transformer_torch.html
---

# group-vit-segmentation-transformer-torch#

Hugging Face Transformers model for zero-shot semantic segmentation.

**Details**

  * Model name: `group-vit-segmentation-transformer-torch`

  * Model source: <https://huggingface.co/docs/transformers/en/tasks/mask_generation>

  * Model author: Thomas Wolf, et al.

  * Model license: Apache 2.0

  * Model size: 212.80 MB

  * Exposes embeddings? yes

  * Tags: `segmentation, embeddings, torch, transformers, zero-shot, official`




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
    12model = foz.load_zoo_model("group-vit-segmentation-transformer-torch",
    13    text_prompt="A photo of a",
    14    classes=["person", "dog", "cat", "bird", "car", "tree", "other"])
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
