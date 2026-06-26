---
source_url: https://docs.voxel51.com/model_zoo/models/ModernVBERT_bimodernvbert.html
---

# ModernVBERT/bimodernvbert#

[ ![From Plugin](https://img.shields.io/badge/Plugin-bimodernvbert-orange) ](../../plugins/plugins_ecosystem/bimodernvbert.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [bimodernvbert](plugins__plugins_ecosystem__bimodernvbert.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

The ModernVBERT suite is a suite of compact 250M-parameter vision-language encoders. BiModernVBERT is the bi-encoder version that is fine-tuned for visual document retrieval tasks..

**Details**

  * Model name: `ModernVBERT/bimodernvbert`

  * Model source: <https://huggingface.co/ModernVBERT/bimodernvbert>

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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/bimodernvbert")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("ModernVBERT/bimodernvbert")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
