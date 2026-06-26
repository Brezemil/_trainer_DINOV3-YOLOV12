---
source_url: https://docs.voxel51.com/model_zoo/models/apple_FastVLM_1_5B.html
---

# apple/FastVLM-1.5B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-fast__vlm-orange) ](../../plugins/plugins_ecosystem/fast_vlm.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [fast_vlm](plugins__plugins_ecosystem__fast_vlm.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

FastVLM is a vision-language model from Apple that excels at visual question answering and image classification tasks. It supports both zero-shot classification and open-ended VQA with customizable prompts..

**Details**

  * Model name: `apple/FastVLM-1.5B`

  * Model source: <https://huggingface.co/apple/FastVLM-1.5B>

  * Model author: Apple

  * Model license: Apple-AMLR

  * Exposes embeddings? no

  * Tags: `vision-language, vqa, multimodal, transformers, torch`




**Requirements**

  * Packages: `torch, transformers`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/fast_vlm")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("apple/FastVLM-1.5B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
