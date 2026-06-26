---
source_url: https://docs.voxel51.com/model_zoo/models/llamaindex_vdr_2b_v1.html
---

# llamaindex/vdr-2b-v1#

[ ![From Plugin](https://img.shields.io/badge/Plugin-visual__document__retrieval-orange) ](../../plugins/plugins_ecosystem/visual_document_retrieval.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [visual_document_retrieval](plugins__plugins_ecosystem__visual_document_retrieval.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

vdr-2b-v1 is an english only embedding model designed for visual document retrieval. It encodes document page screenshots into dense single-vector representations, this will effectively allow to search and query visually rich multilingual documents without the need for any OCR, data extraction pipelines, and chunking..

**Details**

  * Model name: `llamaindex/vdr-2b-v1`

  * Model source: <https://huggingface.co/llamaindex/vdr-2b-v1>

  * Model author: LlamaIndex

  * Model license: Apache-2.0 license

  * Exposes embeddings? yes

  * Tags: `embeddings, ocr, VLM, document-retrieval`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision, qwen-vl-utils, accelerate`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/visual_document_retrieval")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("llamaindex/vdr-2b-v1")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
