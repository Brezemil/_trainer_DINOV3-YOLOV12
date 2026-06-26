---
source_url: https://docs.voxel51.com/model_zoo/models/Qwen_Qwen3_VL_8B_Instruct.html
---

# Qwen/Qwen3-VL-8B-Instruct#

[ ![From Plugin](https://img.shields.io/badge/Plugin-qwen3vl__video-orange) ](../../plugins/plugins_ecosystem/qwen3vl_video.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [qwen3vl_video](plugins__plugins_ecosystem__qwen3vl_video.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Qwen3-VL is a multimodal vision-language model that processes and understands both text and visual input, enabling it to analyze images, video, and perform advanced reasoning and tasks involving both modalities..

**Details**

  * Model name: `Qwen/Qwen3-VL-8B-Instruct`

  * Model source: <https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct>

  * Model author: Qwen

  * Model license: Apache-2.0

  * Exposes embeddings? yes

  * Tags: `classification, detections, torch, temporal-detections, zero-shot, video, embeddings`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, qwen-vl-utils, decord`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/qwen3vl_video")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("Qwen/Qwen3-VL-8B-Instruct")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
