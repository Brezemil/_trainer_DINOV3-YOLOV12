---
source_url: https://docs.voxel51.com/model_zoo/models/PerceptronAI_Isaac_0_1.html
---

# PerceptronAI/Isaac-0.1#

[ ![From Plugin](https://img.shields.io/badge/Plugin-isaac0__1-orange) ](../../plugins/plugins_ecosystem/isaac0_1.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [isaac0_1](plugins__plugins_ecosystem__isaac0_1.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Isaac 0.1 is an open-source, 2B-parameter model built for real-world applications. Isaac 0.1 is the first in Perceptron AIâs family of models built to be the intelligence layer for the physical world..

**Details**

  * Model name: `PerceptronAI/Isaac-0.1`

  * Model source: <https://huggingface.co/PerceptronAI/Isaac-0.1>

  * Model author: PerceptronAI

  * Model license: Creative Commons Attribution Non Commercial 4.0

  * Exposes embeddings? no

  * Tags: `detection, ocr, VLM, classification, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, perceptron`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/isaac0_1")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("PerceptronAI/Isaac-0.1")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
