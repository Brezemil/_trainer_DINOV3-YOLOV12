---
source_url: https://docs.voxel51.com/model_zoo/models/opendatalab_MinerU2_5_2509_1_2B.html
---

# opendatalab/MinerU2.5-2509-1.2B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-mineru__2__5-orange) ](../../plugins/plugins_ecosystem/mineru_2_5.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [mineru_2_5](plugins__plugins_ecosystem__mineru_2_5.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

MinerU2.5 is a 1.2B-parameter vision-language model for document parsing. It adopts a two-stage parsing strategy: first conducting efficient global layout analysis on downsampled images, then performing fine-grained content recognition on native-resolution crops for text, formulas, and tables..

**Details**

  * Model name: `opendatalab/MinerU2.5-2509-1.2B`

  * Model source: <https://huggingface.co/opendatalab/MinerU2.5-2509-1.2B>

  * Model author: OpenDataLab

  * Model license: AGPL-3.0

  * Exposes embeddings? no

  * Tags: `detection, ocr, VLM`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, mineru-vl-utils`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/mineru_2_5")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("opendatalab/MinerU2.5-2509-1.2B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
