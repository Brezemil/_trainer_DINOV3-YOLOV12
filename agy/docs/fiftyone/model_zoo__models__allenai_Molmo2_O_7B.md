---
source_url: https://docs.voxel51.com/model_zoo/models/allenai_Molmo2_O_7B.html
---

# allenai/Molmo2-O-7B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-molmo2-orange) ](../../plugins/plugins_ecosystem/molmo2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [molmo2](plugins__plugins_ecosystem__molmo2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Molmo2 is a family of open vision-language models developed by the Allen Institute for AI (Ai2) that support image, video and multi-image understanding and grounding..

**Details**

  * Model name: `allenai/Molmo2-O-7B`

  * Model source: <https://huggingface.co/allenai/Molmo2-O-7B>

  * Model author: Allen Institute for AI (Ai2)

  * Model license: Apache-2.0

  * Exposes embeddings? no

  * Tags: `torch, keypoints, zero-shot, video`




**Requirements**

  * Packages: `huggingface-hub, transformers==4.57.1, torch, torchvision, molmo_utils, decord2, einops, accelerate`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/molmo2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("allenai/Molmo2-O-7B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
