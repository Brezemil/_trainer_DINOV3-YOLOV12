---
source_url: https://docs.voxel51.com/model_zoo/models/facebook_sam3.html
---

# facebook/sam3#

[ ![From Plugin](https://img.shields.io/badge/Plugin-sam3__images-orange) ](../../plugins/plugins_ecosystem/sam3_images.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [sam3_images](plugins__plugins_ecosystem__sam3_images.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

SAM3 (Segment Anything Model 3) performs promptable segmentation on images using text or visual prompts. Supports concept segmentation (find all instances), visual segmentation (specific instances), automatic segmentation, and visual embeddings..

**Details**

  * Model name: `facebook/sam3`

  * Model source: <https://huggingface.co/facebook/sam3>

  * Model author: Meta AI

  * Model license: SAM License

  * Exposes embeddings? yes

  * Tags: `embeddings, torch, zero-shot, segmentation, segment-anything, detections, instance-segmentation, visual-prompting`




**Requirements**

  * Packages: `huggingface-hub, transformers, torch, torchvision`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/harpreetsahota204/sam3_images")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("facebook/sam3")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
