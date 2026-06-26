---
source_url: https://docs.voxel51.com/model_zoo/models/FriedFeid_oVDA_c16.html
---

# FriedFeid/oVDA-c16#

[ ![From Plugin](https://img.shields.io/badge/Plugin-online__video__depth__anything-orange) ](../../plugins/plugins_ecosystem/online_video_depth_anything.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [online_video_depth_anything](plugins__plugins_ecosystem__online_video_depth_anything.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Online Video Depth Anything (cache_size=16). Estimates temporally-consistent monocular depth for videos using a DINOv2 backbone with a rolling temporal cache. Outputs per-frame fo.Heatmap depth maps normalised to [0, 1]..

**Details**

  * Model name: `FriedFeid/oVDA-c16`

  * Model source: <https://huggingface.co/FriedFeid/oVDA>

  * Model author: Heidelberg University

  * Model license: NC-SA-UHDV1.0

  * Exposes embeddings? no

  * Tags: `depth-estimation, video, temporal, heatmap`




**Requirements**

  * Packages: `torch, torchvision, einops, natsort, easydict, huggingface_hub`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/online_video_depth_anything")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("FriedFeid/oVDA-c16")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
