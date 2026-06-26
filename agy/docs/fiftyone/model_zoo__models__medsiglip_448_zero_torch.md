---
source_url: https://docs.voxel51.com/model_zoo/models/medsiglip_448_zero_torch.html
---

# medsiglip-448-zero-torch#

Medical SigLIP for zero-shot image classification and embeddings.

**Details**

  * Model name: `medsiglip-448-zero-torch`

  * Model source: <https://huggingface.co/google/medsiglip-448>

  * Model author: Google Research

  * Model license: Custom (HAI-DEF gated on Hugging Face)

  * Exposes embeddings? yes

  * Tags: `classification, torch, official, medical, zero-shot, embeddings`




**Requirements**

  * Packages: `torch, torchvision, transformers, huggingface_hub`

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
    12model = foz.load_zoo_model("medsiglip-448-zero-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
