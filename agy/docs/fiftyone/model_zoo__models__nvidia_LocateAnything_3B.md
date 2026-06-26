---
source_url: https://docs.voxel51.com/model_zoo/models/nvidia_LocateAnything_3B.html
---

# nvidia/LocateAnything-3B#

[ ![From Plugin](https://img.shields.io/badge/Plugin-fiftyone--locate--anything-orange) ](../../plugins/plugins_ecosystem/fiftyone_locate_anything.html)

Note

This is a [remotely-sourced model](model_zoo__remote.md#model-zoo-remote) from the [fiftyone-locate-anything](plugins__plugins_ecosystem__fiftyone_locate_anything.md) plugin, maintained by the community. It is not part of FiftyOne core and may have special installation requirements. Please review the plugin documentation and license before use.

NVIDIA LocateAnything-3B: open-vocabulary grounding VLM (3B params, Qwen2.5-3B + MoonViT + Parallel Box Decoder). Image and (frame-sampled) video. 7 operations: detect, grounding, point, scene_text, layout, text_grounding, gui_box. Returns fo.Detections or fo.Keypoints (image), {frame: label} (video)..

**Details**

  * Model name: `nvidia/LocateAnything-3B`

  * Model source: <https://huggingface.co/nvidia/LocateAnything-3B>

  * Model author: NVIDIA

  * Model license: NVIDIA License (non-commercial research only). See <https://huggingface.co/nvidia/LocateAnything-3B>

  * Exposes embeddings? no

  * Tags: `detection, keypoints, grounding, ocr, layout, gui, torch, zero-shot, image, video, VLM, open-vocabulary`




**Requirements**

  * Packages: `huggingface-hub, torch, torchvision, transformers>=4.57.1,<4.58, tokenizers>=0.22.0, Pillow, timm, lmdb, peft, opencv-python-headless>=4.10`

  * CPU support

    * yes

  * GPU support

    * yes




**Example usage**
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4foz.register_zoo_model_source("https://github.com/Burhan-Q/fiftyone-locate-anything")
     5
     6dataset = foz.load_zoo_dataset(
     7    "coco-2017",
     8    split="validation",
     9    dataset_name=fo.get_default_dataset_name(),
    10    max_samples=50,
    11    shuffle=True,
    12)
    13
    14model = foz.load_zoo_model("nvidia/LocateAnything-3B")
    15
    16dataset.apply_model(model, label_field="predictions")
    17
    18session = fo.launch_app(dataset)
    
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
