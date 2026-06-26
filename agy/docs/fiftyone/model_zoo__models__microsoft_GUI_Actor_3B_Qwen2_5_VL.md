---
source_url: https://docs.voxel51.com/model_zoo/models/microsoft_GUI_Actor_3B_Qwen2_5_VL.html
---

# microsoft/GUI-Actor-3B-Qwen2.5-VL#

[ ![From Plugin](https://img.shields.io/badge/Plugin-gui__actor-orange) ](../../plugins/plugins_ecosystem/gui_actor.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [gui_actor](plugins__plugins_ecosystem__gui_actor.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

GUI-Actor is Coordinate-Free Visual Grounding for GUI Agents.

**Details**

  * Model name: `microsoft/GUI-Actor-3B-Qwen2.5-VL`

  * Model source: <https://huggingface.co/microsoft/GUI-Actor-3B-Qwen2.5-VL>

  * Model author: Microsoft

  * Model license: MIT

  * Exposes embeddings? no

  * Tags: `keypoints, visual-agent`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, qwen-vl-utils, accelerate`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/gui_actor")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("microsoft/GUI-Actor-3B-Qwen2.5-VL")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
