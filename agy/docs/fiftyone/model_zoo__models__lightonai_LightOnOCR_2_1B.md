---
source_url: https://docs.voxel51.com/model_zoo/models/lightonai_LightOnOCR_2_1B.html
---

# lightonai/LightOnOCR-2-1B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-LightOnOCR--2-orange) ](../../plugins/plugins_ecosystem/lightonocr_2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [LightOnOCR-2](plugins__plugins_ecosystem__lightonocr_2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

LightOnOCR is a 2.1B-parameter vision-language model optimized for optical character recognition. It uses a chat-based interface to extract text from images with high accuracy across various document types, handwritten text, and scene text..

**Details**

  * Model name: `lightonai/LightOnOCR-2-1B`

  * Model source: <https://huggingface.co/lightonai/LightOnOCR-2-1B>

  * Model author: LightOn AI

  * Model license: Apache-2.0

  * Exposes embeddings? no

  * Tags: `ocr, text-extraction, VLM, document-understanding`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, pillow`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/LightOnOCR-2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("lightonai/LightOnOCR-2-1B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
