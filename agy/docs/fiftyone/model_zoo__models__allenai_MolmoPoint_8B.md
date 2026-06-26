---
source_url: https://docs.voxel51.com/model_zoo/models/allenai_MolmoPoint_8B.html
---

# allenai/MolmoPoint-8B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-molmo__point-orange) ](../../plugins/plugins_ecosystem/molmo_point.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [molmo_point](plugins__plugins_ecosystem__molmo_point.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

MolmoPoint-8B is a vision-language model that locates and tracks objects in images and videos by pointing. For images, it returns normalized keypoint coordinates per instance. For videos, it supports frame-level tracking (follows objects over time) and sparse pointing (identifies objects across sampled frames)..

**Details**

  * Model name: `allenai/MolmoPoint-8B`

  * Model source: <https://huggingface.co/allenai/MolmoPoint-8B>

  * Model author: Allen AI

  * Model license: Apache-2.0

  * Exposes embeddings? no

  * Tags: `keypoints, pointing, tracking, video, VLM, zero-shot, image-text-to-text`




**Requirements**

  * Packages: `torch, transformers, pillow, huggingface-hub, molmo-utils`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/molmo_point")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("allenai/MolmoPoint-8B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
