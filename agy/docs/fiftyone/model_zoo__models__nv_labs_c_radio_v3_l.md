---
source_url: https://docs.voxel51.com/model_zoo/models/nv_labs_c_radio_v3_l.html
---

# nv_labs/c-radio_v3-l#

[ ![From Plugin](https://img.shields.io/badge/Plugin-NVLabs__CRADIOV3-orange) ](../../plugins/plugins_ecosystem/nvlabs_cradiov3.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [NVLabs_CRADIOV3](plugins__plugins_ecosystem__nvlabs_cradiov3.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

C-RADIOv3-L model (ViT-L/16)).

**Details**

  * Model name: `nv_labs/c-radio_v3-l`

  * Model source: [NVlabs/RADIO](https://github.com/NVlabs/RADIO)

  * Model author: NVIDIA

  * Model license: NVIDIA Source Code License-NC

  * Exposes embeddings? yes

  * Tags: `embeddings, heatmap`




**Requirements**

  * Packages: `torch, torchvision`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/NVLabs_CRADIOV3")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("nv_labs/c-radio_v3-l")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
