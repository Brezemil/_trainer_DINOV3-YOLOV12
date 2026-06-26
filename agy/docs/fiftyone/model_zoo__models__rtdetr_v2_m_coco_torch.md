---
source_url: https://docs.voxel51.com/model_zoo/models/rtdetr_v2_m_coco_torch.html
---

# rtdetr-v2-m-coco-torch#

Balanced real-time object detector offering improved accuracy for production use.

**Details**

  * Model name: `rtdetr-v2-m-coco-torch`

  * Model source: <https://huggingface.co/PekingU/rtdetr_v2_r50vd>

  * Model author: Wenyu Lv, et al.

  * Model license: Apache 2.0

  * Model size: 328.41 MB

  * Exposes embeddings? yes

  * Tags: `detection, coco, embeddings, torch, transformers, rtdetr, official`




**Requirements**

  * Packages: `torch, torchvision, transformers`

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
    12model = foz.load_zoo_model("rtdetr-v2-m-coco-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
