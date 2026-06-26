---
source_url: https://docs.voxel51.com/model_zoo/models/nanonets_Nanonets_OCR2_3B.html
---

# nanonets/Nanonets-OCR2-3B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-nanonets__ocr2-orange) ](../../plugins/plugins_ecosystem/nanonets_ocr2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [nanonets_ocr2](plugins__plugins_ecosystem__nanonets_ocr2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Nanonets-OCR2 are image-to-markdown OCR models that go far beyond traditional text extraction. It transforms documents into structured markdown with intelligent content recognition and semantic tagging, making it ideal for downstream processing by Large Language Models (LLMs)..

**Details**

  * Model name: `nanonets/Nanonets-OCR2-3B`

  * Model source: <https://huggingface.co/nanonets/Nanonets-OCR2-3B>

  * Model author: Nanonets

  * Model license: Apache 2.0

  * Exposes embeddings? no

  * Tags: `detection, ocr, VLM`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/nanonets_ocr2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("nanonets/Nanonets-OCR2-3B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
