---
source_url: https://docs.voxel51.com/model_zoo/models/showlab_ShowUI_2B.html
---

# showlab/ShowUI-2B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-ShowUI-orange) ](../../plugins/plugins_ecosystem/showui.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [ShowUI](plugins__plugins_ecosystem__showui.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

ShowUI is a lightweight (2B) vision-language-action model designed for GUI agents..

**Details**

  * Model name: `showlab/ShowUI-2B`

  * Model source: <https://huggingface.co/showlab/ShowUI-2B>

  * Model author: Show Lab

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/ShowUI")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("showlab/ShowUI-2B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
