---
source_url: https://docs.voxel51.com/model_zoo/models/zai_org_GLM_OCR.html
---

# zai-org/GLM-OCR#

[ ![From Plugin](https://img.shields.io/badge/Plugin-glm__ocr-orange) ](../../plugins/plugins_ecosystem/glm_ocr.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [glm_ocr](plugins__plugins_ecosystem__glm_ocr.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

GLM-OCR is a vision-language model for document understanding. Supports text recognition, formula recognition, table recognition, and custom structured extraction via JSON prompts..

**Details**

  * Model name: `zai-org/GLM-OCR`

  * Model source: <https://huggingface.co/zai-org/GLM-OCR>

  * Model author: zai-org

  * Model license: Apache-2.0

  * Exposes embeddings? no

  * Tags: `ocr, document-understanding, visual-document-retrieval`




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
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/glm_ocr")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("zai-org/GLM-OCR")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
