---
source_url: https://docs.voxel51.com/model_zoo/models/nv_labs_c_radio_v4_h.html
---

# nv_labs/c-radio_v4-h#

[ ![From Plugin](https://img.shields.io/badge/Plugin-cradiov4-orange) ](../../plugins/plugins_ecosystem/cradiov4.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [cradiov4](plugins__plugins_ecosystem__cradiov4.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

C-RADIOv4-H (631M params) - Visual feature extraction model using multi-teacher distillation from SigLIP2, DINOv3, and SAM3. Generates image embeddings and spatial attention features..

**Details**

  * Model name: `nv_labs/c-radio_v4-h`

  * Model source: <https://huggingface.co/nvidia/C-RADIOv4-H>

  * Model author: NVIDIA

  * Model license: NVIDIA Open Model License Agreement

  * Exposes embeddings? yes

  * Tags: `embeddings, heatmap`




**Requirements**

  * Packages: `torch, torchvision, transformers, timm, open-clip-torch`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/CRADIOv4")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("nv_labs/c-radio_v4-h")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
