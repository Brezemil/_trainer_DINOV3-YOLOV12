---
source_url: https://docs.voxel51.com/model_zoo/models/microsoft_kosmos_2_5.html
---

# microsoft/kosmos-2.5#

[ ![From Plugin](https://img.shields.io/badge/Plugin-kosmos2__5-orange) ](../../plugins/plugins_ecosystem/kosmos2_5.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [kosmos2_5](plugins__plugins_ecosystem__kosmos2_5.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Kosmos-2.5 is a multimodal literate model for machine reading of text-intensive images..

**Details**

  * Model name: `microsoft/kosmos-2.5`

  * Model source: <https://huggingface.co/microsoft/kosmos-2.5>

  * Model author: Microsoft

  * Model license: MIT

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/kosmos2_5")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("microsoft/kosmos-2.5")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
