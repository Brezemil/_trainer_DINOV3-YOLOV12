---
source_url: https://docs.voxel51.com/model_zoo/models/XiaomiMiMo_MiMo_VL_7B_RL.html
---

# XiaomiMiMo/MiMo-VL-7B-RL#

[ ![From Plugin](https://img.shields.io/badge/Plugin-MiMo__VL-orange) ](../../plugins/plugins_ecosystem/mimo_vl.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [MiMo_VL](plugins__plugins_ecosystem__mimo_vl.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

MiMo-VL-7B is a compact yet powerful vision-language model developed through extensive pre-training and reinforcement learning to achieve state-of-the-art performance on a variety of visual-language tasks..

**Details**

  * Model name: `XiaomiMiMo/MiMo-VL-7B-RL`

  * Model source: <https://huggingface.co/XiaomiMiMo/MiMo-VL-7B-RL>

  * Model author: XiaomiMiMo

  * Model license: MIT

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/MiMo_VL")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("XiaomiMiMo/MiMo-VL-7B-RL")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
