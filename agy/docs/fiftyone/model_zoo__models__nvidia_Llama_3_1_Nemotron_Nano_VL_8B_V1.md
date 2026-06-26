---
source_url: https://docs.voxel51.com/model_zoo/models/nvidia_Llama_3_1_Nemotron_Nano_VL_8B_V1.html
---

# nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1#

[ ![From Plugin](https://img.shields.io/badge/Plugin-Nemotron__Nano__VL-orange) ](../../plugins/plugins_ecosystem/nemotron_nano_vl.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [Nemotron_Nano_VL](plugins__plugins_ecosystem__nemotron_nano_vl.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Llama Nemotron Nano VL is a leading document intelligence vision language model (VLMs) that enables the ability to query and summarize images from the physical or virtual world..

**Details**

  * Model name: `nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1`

  * Model source: <https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1>

  * Model author: NVIDIA

  * Model license: NVIDIA Open License Agreement

  * Exposes embeddings? no

  * Tags: `detection, ocr, VLM, classification, zero-shot, visual-agent`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, timm, einops, open-clip-torch`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/Nemotron_Nano_VL")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
