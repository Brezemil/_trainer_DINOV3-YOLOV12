---
source_url: https://docs.voxel51.com/model_zoo/models/vikhyatk_moondream2.html
---

# vikhyatk/moondream2#

[ ![From Plugin](https://img.shields.io/badge/Plugin-moondream2-orange) ](../../plugins/plugins_ecosystem/moondream2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [moondream2](plugins__plugins_ecosystem__moondream2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Moondream is a small vision language model designed to run efficiently on edge devices..

**Details**

  * Model name: `vikhyatk/moondream2`

  * Model source: <https://huggingface.co/vikhyatk/moondream2>

  * Model author: Moondream AI

  * Model license: Apache-2.0

  * Exposes embeddings? no

  * Tags: `detection, segmentation, ocr, VLM, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, einops, bitsandbytes`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/moondream2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("vikhyatk/moondream2")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
