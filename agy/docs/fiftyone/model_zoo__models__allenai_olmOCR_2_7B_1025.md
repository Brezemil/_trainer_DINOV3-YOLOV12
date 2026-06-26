---
source_url: https://docs.voxel51.com/model_zoo/models/allenai_olmOCR_2_7B_1025.html
---

# allenai/olmOCR-2-7B-1025#

[ ![From Plugin](https://img.shields.io/badge/Plugin-olmOCR--2-orange) ](../../plugins/plugins_ecosystem/olmocr_2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [olmOCR-2](plugins__plugins_ecosystem__olmocr_2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

olmOCR-2 is an advanced OCR model from AllenAI that uses Qwen2.5-VL architecture for document text extraction. Returns markdown output with YAML front matter containing document metadata (language, rotation, tables, diagrams). Converts equations to LaTeX and tables to HTML..

**Details**

  * Model name: `allenai/olmOCR-2-7B-1025`

  * Model source: <https://huggingface.co/allenai/olmOCR-2-7B-1025>

  * Model author: AllenAI

  * Model license: Apache 2.0

  * Exposes embeddings? no

  * Tags: `ocr, document-understanding, VLM, vision-language`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, Pillow, numpy`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/olmOCR-2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("allenai/olmOCR-2-7B-1025")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
