---
source_url: https://docs.voxel51.com/model_zoo/models/Apple_SHARP.html
---

# Apple/SHARP#

[ ![From Plugin](https://img.shields.io/badge/Plugin-apple__sharp-orange) ](../../plugins/plugins_ecosystem/apple_sharp.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [apple_sharp](plugins__plugins_ecosystem__apple_sharp.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

SHARP is an approach to photorealistic view synthesis from a single image. Given a single photograph, SHARP regresses the parameters of a 3D Gaussian representation of the depicted scene..

**Details**

  * Model name: `Apple/SHARP`

  * Model source: <https://huggingface.co/apple/Sharp>

  * Model author: Apple

  * Model license: Apple Model License for Research

  * Exposes embeddings? no

  * Tags: `threed`




**Requirements**

  * Packages: `sharp@git+https://github.com/apple/ml-sharp, torch, torchvision`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/apple_sharp")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("Apple/SHARP")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
