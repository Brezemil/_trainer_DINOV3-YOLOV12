---
source_url: https://docs.voxel51.com/model_zoo/models/openbmb_MiniCPM_V_4_5.html
---

# openbmb/MiniCPM-V-4_5#

[ ![From Plugin](https://img.shields.io/badge/Plugin-minicpm--v-orange) ](../../plugins/plugins_ecosystem/minicpm_v.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [minicpm-v](plugins__plugins_ecosystem__minicpm_v.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

MiniCPM-V 4.5 is the latest and most capable model in the MiniCPM-V series. The model is built on Qwen3-8B and SigLIP2-400M with a total of 8B parameters..

**Details**

  * Model name: `openbmb/MiniCPM-V-4_5`

  * Model source: <https://huggingface.co/openbmb/MiniCPM-V-4_5>

  * Model author: Open Lab for Big Model Base

  * Model license: MiniCPM Model License

  * Exposes embeddings? no

  * Tags: `detection, keypoints, ocr, VLM, classification, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/minicpm-v")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("openbmb/MiniCPM-V-4_5")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
