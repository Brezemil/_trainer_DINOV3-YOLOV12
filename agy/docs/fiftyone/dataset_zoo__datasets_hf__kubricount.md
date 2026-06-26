---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/kubricount.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/KubriCount)

# Dataset Card for KubriCount (subset)#

![image/png](https://huggingface.co/datasets/Voxel51/KubriCount/resolve/main/kubricount.gif)

KubriCount is a large-scale synthetic benchmark for **multi-grained visual counting** , introduced in the paper [_Count Anything at Any Granularity_](https://arxiv.org/abs/2605.10887) (Liu, Wu & Xie, SJTU 2026). It reframes open-world counting as a prompt-following problem across five explicit semantic granularity levels, supported by the most comprehensively annotated counting dataset published to date.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 6736 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/KubriCount")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Description#

Most counting datasets treat âwhat to countâ as a single category-level matching problem. KubriCount exposes this limitation by requiring models to follow fine-grained prompts that specify _which_ semantic level the user intends â from counting a specific object identity all the way up to an abstract concept â while excluding controlled distractors that differ by exactly one semantic factor.

Each scene is a 1024Ã1024 synthetic image produced by a four-stage automatic pipeline: controllable 3D rendering via [Kubric](https://github.com/google-research/kubric) \+ Blender, mask-conditioned image editing (Nano-Banana-Pro) to reduce the sim-to-real gap, and VLM-based quality filtering (Gemini-3-Pro) to guarantee annotation fidelity.

  * **Curated by:** Chang Liu, Haoning Wu, Weidi Xie â School of Artificial Intelligence, Shanghai Jiao Tong University

  * **License:** Apache-2.0

  * **Paper:** [arXiv:2605.10887](https://arxiv.org/abs/2605.10887)




### Dataset Sources#

  * **Repository:** [Verg-Avesta/KubriCount](https://github.com/Verg-Avesta/KubriCount)

  * **HuggingFace Dataset:** [liuchang666/KubriCount](https://huggingface.co/datasets/liuchang666/KubriCount)

  * **Project Page:** [verg-avesta.github.io/KubriCount](https://verg-avesta.github.io/KubriCount/)




* * *

## Counting Granularity Levels#

KubriCount defines five levels of counting granularity. Each level specifies a **target** set and, for levels 2â5, a controlled **distractor** set that differs by exactly one semantic factor:

Level | Granularity | Prompt example | Distractor  
---|---|---|---  
L1 | Identity | âCount all the dogs.â | None  
L2 (size) | Attribute | âCount large cherries.â | Small cherries  
L2 (color) | Attribute | âCount mustard sofas.â | Dark gray sofas  
L3 | Category | âCount the cans.â | Bags  
L4 | Instance type | âCount backpack A.â | Backpack B  
L5 | Concept | âCount the lobsters.â | Octopuses  
  
Levels 2â5 generate **two annotation queries per scene** by swapping the target and distractor roles, which is why the total query count (198,702) exceeds the scene count (110,507).

* * *

## Dataset Statistics#

Split | Scenes | Queries | Purpose  
---|---|---|---  
train | 99,639 | 179,140 | Seen categories (normal + dense configurations, ~4:1 ratio)  
testA | 5,462 | 9,837 | Unseen assets from training categories  
testB | 5,406 | 9,725 | Entirely unseen categories  
**Total** | **110,507** | **198,702** |   
  
  * **Categories:** 157 across 16 super-categories

  * **Total annotated objects:** ~7.3 million

  * **Objects per image:** 1â250 (capped at 250 by Kubricâs 256-instance limit)

  * **Image resolution:** 1024 Ã 1024 px




* * *

## FiftyOne Dataset Structure#

The dataset is loaded into FiftyOne as a **flat image dataset** â one sample per counting query. Scenes with two queries (L2âL5) produce two samples pointing to the same `filepath`.

### Sample Fields#

Field | FiftyOne Type | Description  
---|---|---  
`filepath` | `StringField` | Path to `edited_00000.png` â the final benchmark image  
`image_id` | `StringField` | Relative path key matching the HuggingFace annotation files  
`split` | `StringField` | `"train"`, `"testA"`, or `"testB"`  
`level` | `IntField` | Counting granularity level: 1â5  
`category` | `StringField` | Text label for the target objects to count  
`count` | `IntField` | Ground truth object count  
`target_points` | `fo.Keypoints` | One `fo.Keypoint` per target object, each with a single normalized center point `(x/W, y/H)`  
`example_boxes` | `fo.Detections` | 2â8 few-shot exemplar bounding boxes in `[x, y, w, h]` relative coords  
`segmentation` | `fo.Segmentation` | `mask_path` pointing to `segmentation_00000.png` on disk â the instance segmentation map  
`negative_category` | `StringField` | Distractor label (empty string for L1)  
`negative_count` | `IntField` | Ground truth distractor count (0 for L1)  
`negative_points` | `fo.Keypoints` | One `fo.Keypoint` per distractor object (None for L1)  
`negative_example_boxes` | `fo.Detections` | Few-shot exemplar boxes for the distractor class (None for L1)  
`tags` | `ListField` | e.g. `["testA", "level5"]`  
  
### Design Notes#

  * **`target_points` as a counting sanity check:** for any sample, `len(sample.target_points.keypoints) == sample.count`. This invariant holds by construction and can be used to verify import correctness.

  * **`example_boxes` are not exhaustive:** these are 2â8 manually selected exemplar crops used as few-shot visual prompts, not full ground-truth box coverage of all objects.

  * **`segmentation` is an instance map:** pixel values encode per-instance IDs as rendered by Kubric. It is not a semantic segmentation map.

  * **Dual queries per scene (L2âL5):** two FiftyOne samples share the same `filepath` but have swapped `category` / `negative_category` fields, representing the two valid counting queries for that scene.




## Dataset Creation#

### Generation Pipeline#

KubriCount is constructed in four automatic stages:

  1. **3D asset curation** â ~58K assets across 157 categories sourced from ShapeNetCore-v2 and controllable 3D generation (TRELLIS family). ~5K HDRI environment maps sourced from Poly Haven and Text2Light.

  2. **Prototype synthesis** â Kubric + PyBullet + Blender renders scenes with exact instance metadata (RGB, instance masks, 2D/3D boxes, center points). Level-specific composition rules control target/distractor selection.

  3. **Consistent image editing** â Nano-Banana-Pro refines textures and harmonizes lighting while preserving topology (no instances added, removed, merged, or split). Level-aware constraints prevent edits that would corrupt the counting criterion.

  4. **Automatic data filtering** â Gemini-3-Pro inspects each edited image against the prototype and masks, issuing PASS/FAIL. ~20% are rejected on the first pass; iterative re-editing reduces the final rejection rate to ~5%.




### Splits#

Dataset splits are enforced at the 3D asset level before synthesis:

  * **Train:** seen categories, full asset pool

  * **TestA:** unseen assets within training categories (~10% holdout per category)

  * **TestB:** unseen categories (~10% of total assets)




Both test splits use only unseen HDRI backgrounds and evaluate on the normal (non-dense) scene configuration.

### Annotations#

All annotations are derived automatically from the Kubric rendering engine â there are no human annotators. The engine produces pixel-perfect instance masks, 2D/3D bounding boxes, and center points as part of the rendering process. VLM-based filtering (not annotation) is applied post-hoc to ensure label fidelity.

## Citation#
    
    
    @article{liu2026count,
      title={Count Anything at Any Granularity},
      author={Liu, Chang and Wu, Haoning and Xie, Weidi},
      journal={arXiv preprint arXiv:2605.10887},
      year={2026}
    }
    

**APA:**

Liu, C., Wu, H., & Xie, W. (2026). Count Anything at Any Granularity. _arXiv preprint arXiv:2605.10887_.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
