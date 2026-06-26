---
source_url: https://docs.voxel51.com/model_zoo/models/ByteDance_Seed_UI_TARS_1_5_7B.html
---

# ByteDance-Seed/UI-TARS-1.5-7B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-UI__TARS-orange) ](../../plugins/plugins_ecosystem/ui_tars.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [UI_TARS](plugins__plugins_ecosystem__ui_tars.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

UI-TARS-1.5 is an open-source multimodal agent capable of effectively performing diverse tasks within virtual worlds..

**Details**

  * Model name: `ByteDance-Seed/UI-TARS-1.5-7B`

  * Model source: <https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B>

  * Model author: ByteDance

  * Model license: Apache 2.0

  * Exposes embeddings? no

  * Tags: `detection, ocr, VLM, classification, zero-shot, visual-agent`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, qwen-vl-utils, accelerate`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/UI_TARS")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("ByteDance-Seed/UI-TARS-1.5-7B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
