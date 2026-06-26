---
source_url: https://docs.voxel51.com/model_zoo/models/google_paligemma2_10b_mix_448.html
---

# google/paligemma2-10b-mix-448#

[ ![From Plugin](https://img.shields.io/badge/Plugin-paligemma2-orange) ](../../plugins/plugins_ecosystem/paligemma2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [paligemma2](plugins__plugins_ecosystem__paligemma2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

PaliGemma 2 mix checkpoints are fine-tuned on a diverse set of tasks and are ready to use out of the box. These tasks include short and long captioning, optical character recognition, question answering, object detection and segmentation, and more..

**Details**

  * Model name: `google/paligemma2-10b-mix-448`

  * Model source: <https://huggingface.co/google/paligemma2-10b-mix-448>

  * Model author: Google DeepMind

  * Model license: gemma (<https://ai.google.dev/gemma/terms>)

  * Exposes embeddings? no

  * Tags: `detection, segmentation, ocr, VLM, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers>=4.50, torch, torchvision, accelerate, jax, flax`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/paligemma2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("google/paligemma2-10b-mix-448")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
