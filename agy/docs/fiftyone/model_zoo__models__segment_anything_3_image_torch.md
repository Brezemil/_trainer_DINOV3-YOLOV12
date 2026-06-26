---
source_url: https://docs.voxel51.com/model_zoo/models/segment_anything_3_image_torch.html
---

# segment-anything-3-image-torch#

Open-vocabulary instance segmentation that finds and segments all objects matching a text concept like âpersonâ or âyellow school busâ.

**Details**

  * Model name: `segment-anything-3-image-torch`

  * Model source: [facebookresearch/sam3](https://github.com/facebookresearch/sam3)

  * Model author: Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, et al.

  * Model license: SAM License

  * Model size: 3.45 GB

  * Exposes embeddings? no

  * Tags: `segmentation, instance-segmentation, zero-shot, open-vocabulary, text-prompted, transformer, official`




**Requirements**

  * Packages: `torch, torchvision, sam3`

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
    12model = foz.load_zoo_model("segment-anything-3-image-torch")
    13
    14dataset.apply_model(model, label_field="predictions")
    15
    16session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
