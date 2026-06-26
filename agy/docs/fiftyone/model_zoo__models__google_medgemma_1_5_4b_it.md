---
source_url: https://docs.voxel51.com/model_zoo/models/google_medgemma_1_5_4b_it.html
---

# google/medgemma-1.5-4b-it#

[ ![From Plugin](https://img.shields.io/badge/Plugin-medgemma__1__5-orange) ](../../plugins/plugins_ecosystem/medgemma_1_5.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [medgemma_1_5](plugins__plugins_ecosystem__medgemma_1_5.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

MedGemma 1.5 4B is an updated version of the MedGemma 1 4B model. MedGemma is a collection of Gemma 3 variants that are trained for performance on medical text and image comprehension.

**Details**

  * Model name: `google/medgemma-1.5-4b-it`

  * Model source: <https://huggingface.co/google/medgemma-1.5-4b-it>

  * Model author: Google DeepMind

  * Model license: health-ai-developer-foundations (<https://developers.google.com/health-ai-developer-foundations/terms>)

  * Exposes embeddings? no

  * Tags: `VLM, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, accelerate`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/medgemma_1_5")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("google/medgemma-1.5-4b-it")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
