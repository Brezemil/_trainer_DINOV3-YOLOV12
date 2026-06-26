---
source_url: https://docs.voxel51.com/model_zoo/models/PerceptronAI_Isaac_0_2_2B_Preview.html
---

# PerceptronAI/Isaac-0.2-2B-Preview#

[ ![From Plugin](https://img.shields.io/badge/Plugin-isaac--0__2-orange) ](../../plugins/plugins_ecosystem/isaac_0_2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [isaac-0_2](plugins__plugins_ecosystem__isaac_0_2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Isaac 0.2 2B (Preview) is an open-source, 2B-parameter model built for real-world applications. Isaac 0.2 is part of Perceptron AIâs family of models built to be the intelligence layer for the physical world..

**Details**

  * Model name: `PerceptronAI/Isaac-0.2-2B-Preview`

  * Model source: <https://huggingface.co/PerceptronAI/Isaac-0.2-2B-Preview>

  * Model author: PerceptronAI

  * Model license: Creative Commons Attribution Non Commercial 4.0

  * Exposes embeddings? no

  * Tags: `detection, ocr, VLM, classification, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, accelerate, torch, torchvision, perceptron`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/perceptron-ai-inc/fiftyone-isaac-0_2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("PerceptronAI/Isaac-0.2-2B-Preview")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
