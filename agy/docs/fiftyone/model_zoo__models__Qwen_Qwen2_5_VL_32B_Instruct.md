---
source_url: https://docs.voxel51.com/model_zoo/models/Qwen_Qwen2_5_VL_32B_Instruct.html
---

# Qwen/Qwen2.5-VL-32B-Instruct#

[ ![From Plugin](https://img.shields.io/badge/Plugin-qwen2__5__vl-orange) ](../../plugins/plugins_ecosystem/qwen2_5_vl.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [qwen2_5_vl](plugins__plugins_ecosystem__qwen2_5_vl.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Qwen2.5-VL is the multimodal large language model series developed by Qwen team, Alibaba Cloud..

**Details**

  * Model name: `Qwen/Qwen2.5-VL-32B-Instruct`

  * Model source: <https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct>

  * Model author: QwenLM

  * Model license: Apache-2.0 license

  * Exposes embeddings? no

  * Tags: `detection, segmentation, ocr, VLM, zero-shot`




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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/qwen2_5_vl")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("Qwen/Qwen2.5-VL-32B-Instruct")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
