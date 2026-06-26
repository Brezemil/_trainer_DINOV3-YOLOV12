---
source_url: https://docs.voxel51.com/model_zoo/models/google_Gemini_Vision.html
---

# google/Gemini-Vision#

[ ![From Plugin](https://img.shields.io/badge/Plugin-gemini--vision--plugin-orange) ](../../plugins/plugins_ecosystem/gemini_vision_plugin.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [gemini-vision-plugin](plugins__plugins_ecosystem__gemini_vision_plugin.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Gemini Vision remote model for VQA via Google Gemini API.

**Details**

  * Model name: `google/Gemini-Vision`

  * Model source:

  * Model author: Google

  * Model license: Apache-2.0

  * Exposes embeddings? no

  * Tags: `gemini, vision, vqa, multimodal`




**Requirements**

  * CPU support

    * no

  * GPU support

    * no




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/AdonaiVera/gemini-vision-plugin")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("google/Gemini-Vision")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
