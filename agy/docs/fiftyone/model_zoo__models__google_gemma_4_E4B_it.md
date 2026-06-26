---
source_url: https://docs.voxel51.com/model_zoo/models/google_gemma_4_E4B_it.html
---

# google/gemma-4-E4B-it#

[ ![From Plugin](https://img.shields.io/badge/Plugin-gemma4-orange) ](../../plugins/plugins_ecosystem/gemma4.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [gemma4](plugins__plugins_ecosystem__gemma4.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Gemma 4 E4B is a 4.5B effective parameter multimodal model supporting text, image, video, and audio. Image operations: detect, point, classify, vqa. Video operations: description, temporal_localization, tracking, ocr, comprehensive, custom..

**Details**

  * Model name: `google/gemma-4-E4B-it`

  * Model source: <https://huggingface.co/google/gemma-4-E4B-it>

  * Model author: Google DeepMind

  * Model license: gemma (<https://ai.google.dev/gemma/terms>)

  * Exposes embeddings? no

  * Tags: `detection, classification, keypoints, vqa, temporal-detections, torch, zero-shot, image, video, VLM`




**Requirements**

  * Packages: `huggingface-hub, transformers>=4.52.0, torch, torchvision, accelerate, torchcodec`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/Burhan-Q/gemma4")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("google/gemma-4-E4B-it")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
