---
source_url: https://docs.voxel51.com/model_zoo/models/facebook_VGGT_1B.html
---

# facebook/VGGT-1B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-vggt-orange) ](../../plugins/plugins_ecosystem/vggt.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [vggt](plugins__plugins_ecosystem__vggt.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

Visual Geometry Grounded Transformer (VGGT) is a feed-forward neural network that directly infers all key 3D attributes of a scene..

**Details**

  * Model name: `facebook/VGGT-1B`

  * Model source: huggingface.co/facebook/vggt-1b

  * Model author: Meta AI

  * Model license: CC BY-NC 4.0

  * Exposes embeddings? no

  * Tags: `depth, threed, keypoints`




**Requirements**

  * Packages: `vggt@git+https://github.com/facebookresearch/vggt.git, torch, torchvision, open3d`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/vggt")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("facebook/VGGT-1B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
