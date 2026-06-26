---
source_url: https://docs.voxel51.com/model_zoo/models/jinaai_jina_embeddings_v4.html
---

# jinaai/jina-embeddings-v4#

[ ![From Plugin](https://img.shields.io/badge/Plugin-jina__embeddings__v4-orange) ](../../plugins/plugins_ecosystem/jina_embeddings_v4.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [jina_embeddings_v4](plugins__plugins_ecosystem__jina_embeddings_v4.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

jina-embeddings-v4 is a universal embedding model for multimodal and multilingual retrieval. The model is specially designed for complex document retrieval, including visually rich documents with charts, tables, and illustrations..

**Details**

  * Model name: `jinaai/jina-embeddings-v4`

  * Model source: <https://huggingface.co/jinaai/jina-embeddings-v4>

  * Model author: Jina AI

  * Model license: Apache 2.0

  * Exposes embeddings? yes

  * Tags: `embeddings, torch, visual-document-retrieval, zero-shot`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, peft`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/jina_embeddings_v4")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("jinaai/jina-embeddings-v4")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
