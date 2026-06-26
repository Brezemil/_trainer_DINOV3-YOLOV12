---
source_url: https://docs.voxel51.com/model_zoo/models/nomic_ai_nomic_embed_multimodal_7b.html
---

# nomic-ai/nomic-embed-multimodal-7b#

[ ![From Plugin](https://img.shields.io/badge/Plugin-nomic--embed--multimodal-orange) ](../../plugins/plugins_ecosystem/nomic_embed_multimodal.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [nomic-embed-multimodal](plugins__plugins_ecosystem__nomic_embed_multimodal.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

nomic-embed-multimodal-7b is a dense state-of-the-art multimodal embedding model that excels at visual document retrieval tasks..

**Details**

  * Model name: `nomic-ai/nomic-embed-multimodal-7b`

  * Model source: <https://huggingface.co/nomic-ai/nomic-embed-multimodal-7b>

  * Model author: Nomic AI

  * Model license: Apache-2.0

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/nomic-embed-multimodal")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("nomic-ai/nomic-embed-multimodal-7b")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
