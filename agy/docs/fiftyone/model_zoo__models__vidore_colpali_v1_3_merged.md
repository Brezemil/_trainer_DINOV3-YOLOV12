---
source_url: https://docs.voxel51.com/model_zoo/models/vidore_colpali_v1_3_merged.html
---

# vidore/colpali-v1.3-merged#

[ ![From Plugin](https://img.shields.io/badge/Plugin-colpali__v1__3-orange) ](../../plugins/plugins_ecosystem/colpali_v1_3.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [colpali_v1_3](plugins__plugins_ecosystem__colpali_v1_3.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

ColPali is a model based on a novel model architecture and training strategy based on Vision Language Models (VLMs) to efficiently index documents from their visual features. It is a PaliGemma-3B extension that generates ColBERT- style multi-vector representations of text and images.

**Details**

  * Model name: `vidore/colpali-v1.3-merged`

  * Model source: <https://huggingface.co/vidore/colpali-v1.3-merged>

  * Model author: Vidore

  * Model license: gemma

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/colpali_v1_3")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("vidore/colpali-v1.3-merged")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
