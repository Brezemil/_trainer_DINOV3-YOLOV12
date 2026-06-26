---
source_url: https://docs.voxel51.com/model_zoo/models/moonshotai_Kimi_VL_A3B_Instruct.html
---

# moonshotai/Kimi-VL-A3B-Instruct#

[ ![From Plugin](https://img.shields.io/badge/Plugin-Kimi__VL__A3B-orange) ](../../plugins/plugins_ecosystem/kimi_vl_a3b.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [Kimi_VL_A3B](plugins__plugins_ecosystem__kimi_vl_a3b.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Kimi-VL is an efficient open-source Mixture-of-Experts (MoE) vision-language model (VLM) that offers advanced multimodal reasoning, long-context understanding, and strong agent capabilitiesâall while activating only 2.8B parameters in its language decoder.

**Details**

  * Model name: `moonshotai/Kimi-VL-A3B-Instruct`

  * Model source: <https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct>

  * Model author: Moonshot AI

  * Model license: MIT license

  * Exposes embeddings? no

  * Tags: `agentic, detection, ocr, VLM, classification, zero-shot, visual-agent`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, accelerate, tiktoken, protobuf, blobfile`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/Kimi_VL_A3B")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("moonshotai/Kimi-VL-A3B-Instruct")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
