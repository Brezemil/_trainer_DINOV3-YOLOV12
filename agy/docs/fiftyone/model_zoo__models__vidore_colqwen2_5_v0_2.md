---
source_url: https://docs.voxel51.com/model_zoo/models/vidore_colqwen2_5_v0_2.html
---

# vidore/colqwen2.5-v0.2#

[ ![From Plugin](https://img.shields.io/badge/Plugin-colqwen2__5__v0__2-orange) ](../../plugins/plugins_ecosystem/colqwen2_5_v0_2.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [colqwen2_5_v0_2](plugins__plugins_ecosystem__colqwen2_5_v0_2.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

ColQwen is a model based on a novel model architecture and training strategy based on Vision Language Models (VLMs) to efficiently index documents from their visual features. It is a Qwen2.5-VL-3B extension that generates ColBERT- style multi-vector representations of text and images..

**Details**

  * Model name: `vidore/colqwen2.5-v0.2`

  * Model source: <https://huggingface.co/vidore/colqwen2.5-v0.2>

  * Model author: Vidore

  * Model license: Apache 2.0

  * Exposes embeddings? yes

  * Tags: `classification, logits, embeddings, torch, visual-document-retrieval, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, colpali-engine`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/colqwen2_5_v0_2")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("vidore/colqwen2.5-v0.2")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
