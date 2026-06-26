---
source_url: https://docs.voxel51.com/model_zoo/models/qwen3_vl_2b_instruct_torch.html
---

# qwen3-vl-2b-instruct-torch#

Compact vision-language model for object detection via 2D grounding.

**Details**

  * Model name: `qwen3-vl-2b-instruct-torch`

  * Model source: <https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct>

  * Model author: Qwen Team, Alibaba

  * Model license: Apache 2.0

  * Model size: 4.19 GB

  * Exposes embeddings? no

  * Tags: `detection, vlm, torch, transformer, zero-shot`




**Requirements**

  * Packages: `torch, torchvision, transformers>=4.51.0, accelerate, qwen-vl-utils`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset(
     5    "coco-2017",
     6    split="validation",
     7    dataset_name=fo.get_default_dataset_name(),
     8    max_samples=50,
     9    shuffle=True,
    10)
    11
    12model = foz.load_zoo_model("qwen3-vl-2b-instruct-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
