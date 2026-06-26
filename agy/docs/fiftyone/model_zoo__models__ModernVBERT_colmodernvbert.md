---
source_url: https://docs.voxel51.com/model_zoo/models/ModernVBERT_colmodernvbert.html
---

# ModernVBERT/colmodernvbert#

[ ![From Plugin](https://img.shields.io/badge/Plugin-colmodernvbert-orange) ](../../plugins/plugins_ecosystem/colmodernvbert.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [colmodernvbert](plugins__plugins_ecosystem__colmodernvbert.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

The ModernVBERT suite is a suite of compact 250M-parameter vision-language encoders. ColModernVBERT is the late-interaction version that is fine-tuned for visual document retrieval tasks, the most performant model on this task..

**Details**

  * Model name: `ModernVBERT/colmodernvbert`

  * Model source: <https://huggingface.co/ModernVBERT/colmodernvbert>

  * Model author: Paul Teiletche, et. al

  * Model license: MIT

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/colmodernvbert")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("ModernVBERT/colmodernvbert")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
