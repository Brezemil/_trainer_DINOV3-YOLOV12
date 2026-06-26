---
source_url: https://docs.voxel51.com/model_zoo/models/moondream_moondream3_preview.html
---

# moondream/moondream3-preview#

[ ![From Plugin](https://img.shields.io/badge/Plugin-moondream3-orange) ](../../plugins/plugins_ecosystem/moondream3.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [moondream3](plugins__plugins_ecosystem__moondream3.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Moondream 3 (Preview) is an vision language model with a mixture-of-experts architecture (9B total parameters, 2B active)..

**Details**

  * Model name: `moondream/moondream3-preview`

  * Model source: <https://huggingface.co/moondream/moondream3-preview>

  * Model author: Moondream AI

  * Model license: Business Source License 1.1 with an Additional Use Grant (No Third-Party Service)

  * Exposes embeddings? no

  * Tags: `detection, segmentation, ocr, VLM, zero-shot`




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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/moondream3")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("moondream/moondream3-preview")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
