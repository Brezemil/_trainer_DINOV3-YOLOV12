---
source_url: https://docs.voxel51.com/model_zoo/models/segformer_b5_ade20k_torch.html
---

# segformer-b5-ade20k-torch#

Largest SegFormer model delivering the best semantic segmentation performance in its family.

**Details**

  * Model name: `segformer-b5-ade20k-torch`

  * Model source: <https://huggingface.co/nvidia/segformer-b5-finetuned-ade-640-640>

  * Model author: Enze Xie, et al.

  * Model license: MIT

  * Model size: 323.14 MB

  * Exposes embeddings? yes

  * Tags: `segmentation, torch, segformer, official, embeddings`




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
    12model = foz.load_zoo_model("segformer-b5-ade20k-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
