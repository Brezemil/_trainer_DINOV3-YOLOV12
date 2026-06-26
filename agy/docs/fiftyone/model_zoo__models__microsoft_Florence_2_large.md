---
source_url: https://docs.voxel51.com/model_zoo/models/microsoft_Florence_2_large.html
---

# microsoft/Florence-2-large#

[ ![From Plugin](https://img.shields.io/badge/Plugin-florence2-orange) ](../../plugins/plugins_ecosystem/florence2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [florence2](plugins__plugins_ecosystem__florence2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Florence-2 is a vision foundation model with a unified, prompt-based representation for a variety of computer vision and vision-language tasks (https://arxiv.org/abs/2311.06242)..

**Details**

  * Model name: `microsoft/Florence-2-large`

  * Model source: <https://huggingface.co/microsoft/Florence-2-large>

  * Model author: Microsoft

  * Model license: MIT

  * Exposes embeddings? no

  * Tags: `detection, segmentation, ocr, VLM, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, einops, timm, accelerate`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/florence2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("microsoft/Florence-2-large")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
