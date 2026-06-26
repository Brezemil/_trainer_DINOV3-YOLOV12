---
source_url: https://docs.voxel51.com/model_zoo/models/deepseek_ai_DeepSeek_OCR.html
---

# deepseek-ai/DeepSeek-OCR#

[ ![From Plugin](https://img.shields.io/badge/Plugin-deepseek__ocr-orange) ](../../plugins/plugins_ecosystem/deepseek_ocr.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [deepseek_ocr](plugins__plugins_ecosystem__deepseek_ocr.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

DeepSeek-OCR is an open-source vision-language model (VLM) developed by DeepSeek to perform optical character recognition (OCR) and context compression for long and complex documents.

**Details**

  * Model name: `deepseek-ai/DeepSeek-OCR`

  * Model source: <https://huggingface.co/deepseek-ai/DeepSeek-OCR>

  * Model author: DeepSeek

  * Model license: MIT

  * Exposes embeddings? no

  * Tags: `detection, ocr, VLM`




**Requirements**

  * Packages: `huggingface-hub, transformers==4.46.3, tokenizers==0.20.3, torch, torchvision, addict, einops`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/deepseek_ocr")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("deepseek-ai/DeepSeek-OCR")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
