---
source_url: https://docs.voxel51.com/model_zoo/models/google_siglip2_giant_opt_patch16_256.html
---

# google/siglip2-giant-opt-patch16-256#

[ ![From Plugin](https://img.shields.io/badge/Plugin-siglip2-orange) ](../../plugins/plugins_ecosystem/siglip2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [siglip2](plugins__plugins_ecosystem__siglip2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

SigLIP 2 extends the pretraining objective of SigLIP with prior, independently developed techniques into a unified recipe, for improved semantic understanding, localization, and dense features..

**Details**

  * Model name: `google/siglip2-giant-opt-patch16-256`

  * Model source: <https://huggingface.co/google/siglip2-giant-opt-patch16-256>

  * Model author: Google

  * Model license: Apache-2.0

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/siglip2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("google/siglip2-giant-opt-patch16-256")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
