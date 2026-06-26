---
source_url: https://docs.voxel51.com/model_zoo/models/google_medsiglip_448.html
---

# google/medsiglip-448#

[ ![From Plugin](https://img.shields.io/badge/Plugin-medsiglip-orange) ](../../plugins/plugins_ecosystem/medsiglip.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [medsiglip](plugins__plugins_ecosystem__medsiglip.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

MedSigLIP is a variant of SigLIP that is trained to encode medical images and text into a common embedding space..

**Details**

  * Model name: `google/medsiglip-448`

  * Model source: <https://huggingface.co/google/medsiglip-448>

  * Model author: Google

  * Model license: health-ai-developer-foundations

  * Exposes embeddings? yes

  * Tags: `classification, logits, embeddings, torch, clip, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, accelerate`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/medsiglip")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("google/medsiglip-448")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
