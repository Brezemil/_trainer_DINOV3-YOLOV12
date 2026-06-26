---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/navitrace.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/NaviTrace)

# Dataset Card for NaviTrace#

![image/png](https://huggingface.co/datasets/Voxel51/NaviTrace/resolve/main/navitrace.gif)

NaviTrace is a Visual Question Answering benchmark for evaluating how well vision-language models (VLMs) understand embodiment-specific navigation in real-world scenes. Each sample presents a first-person image of an outdoor environment paired with a natural language navigation instruction. The task is to predict a 2D navigation trace â a sequence of waypoints in image space â that a given embodiment type would follow to complete the instruction.

The dataset contains **1,002 scenarios** with over **3,000 expert-annotated traces** across four embodiment types: Human, Legged Robot, Wheeled Robot, and Bicycle.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1002 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/NaviTrace")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Sourced#

  * **Curated by:** Tim Windecker, Manthan Patel, Moritz Reuss, Richard Schwarzkopf, Cesar Cadena, Rudolf Lioutikov, Marco Hutter, Jonas Frey (ETH Zurich, KIT, FZI)

  * **Language:** English

  * **Repository:** [leggedrobotics/navitrace](https://huggingface.co/datasets/leggedrobotics/navitrace)

  * **Paper:** [NaviTrace: Evaluating Embodied Navigation of Vision-Language Models](https://arxiv.org/abs/2510.26909) (arXiv:2510.26909)

  * **Leaderboard:** [leggedrobotics.github.io/navitrace_webpage](https://leggedrobotics.github.io/navitrace_webpage/)




* * *

## Uses#

### Direct Use#

  * Benchmarking VLMs on embodied navigation trace prediction

  * Evaluating spatial grounding and goal localization in vision-language models

  * Studying how embodiment type affects navigation decisions (e.g., stairs vs. ramps for wheeled vs. legged robots)

  * Fine-tuning models on the validation split for navigation-aware reasoning




### Out-of-Scope Use#

  * Real-time robot control or closed-loop navigation â traces are 2D image-space paths, not 3D or metric coordinates

  * Temporal or multi-step planning â each scenario is a single static image

  * Aerial embodiments â only ground-level embodiments are covered




* * *

### Embodiments#

Each scenario annotates traces for one or more of the following embodiment types:

Embodiment | Description  
---|---  
**Human** | Standard pedestrian; can use stairs and ramps  
**Legged Robot** | Quadruped (e.g., ANYmal); similar to human but shorter  
**Wheeled Robot** | Delivery robot; prefers smooth surfaces and ramps, cannot use stairs  
**Bicycle** | Cyclist; follows traffic rules, avoids stairs, prefers bike lanes  
  
### Task Categories#

Scenarios are tagged with one or more of the following navigation challenge categories:

  * **Geometric Terrain** â decisions based on 3D structure (stairs, cliffs, closed doors)

  * **Semantic Terrain** â decisions requiring semantic understanding (sidewalk vs. road, terrain stiffness)

  * **Accessibility** â barrier-free access concerns (ramps, automatic doors)

  * **Visibility** â occlusions, poor lighting, or ambiguous information

  * **Social Norms** â normative constraints from rules or signage (crosswalks, pedestrian-only zones)

  * **Dynamic Obstacle Avoidance** â moving obstacles such as pedestrians or vehicles

  * **Stationary Obstacle Avoidance** â fixed obstacles like debris or road closures




### Scene Metadata#

Each scenario includes scene-level metadata covering geographic location, environment type, lighting, and weather. The dataset is geographically concentrated in Switzerland (including Zurich and ETH campus), with additional samples from the USA, Japan, Germany, South Korea, Sweden, Spain, Portugal, Austria, England, and Italy. Faces and license plates are anonymized using EgoBlur.

* * *

## FiftyOne Structure#

### Sample Fields#

Field | FiftyOne Type | Description  
---|---|---  
`filepath` | `StringField` | Path to the JPEG image (1365Ã1024 px)  
`split` | `StringField` | `"validation"` or `"test"`  
`sample_id` | `StringField` | UUID identifying the scenario  
`task` | `StringField` | Navigation instruction (e.g., `"Go to the garden"`)  
`embodiments` | `ListField(StringField)` | Embodiment types present in this scenario  
`category` | `ListField(StringField)` | Navigation challenge categories for this scenario  
`context` | `StringField` | Free-text scene description written by annotators  
`city` | `StringField` | City where the image was captured  
`country` | `StringField` | Country where the image was captured  
`lighting_conditions` | `StringField` | `Daylight`, `Low Light`, `Night`, or `Indoor Lighting`  
`natural_structured` | `StringField` | `Natural`, `Structured`, or `Mixed`  
`task_type` | `StringField` | `Goal` (reach a location) or `Direction` (follow a path)  
`urban_rural` | `StringField` | `Urban`, `Rural`, or `Mixed`  
`weather_conditions` | `StringField` | `Clear`, `Cloudy`, `Rainy`, `Snowy`, `Foggy`, or `Unknown`  
  
### Label Fields#

Field | FiftyOne Type | Description  
---|---|---  
`segmentation_mask` | `fo.Segmentation` | Per-pixel semantic class mask (Mask2Former on Mapillary Vistas)  
`human` | `fo.Polylines` | Ground-truth navigation trace(s) for a Human  
`legged_robot` | `fo.Polylines` | Ground-truth navigation trace(s) for a Legged Robot  
`wheeled_robot` | `fo.Polylines` | Ground-truth navigation trace(s) for a Wheeled Robot  
`bicycle` | `fo.Polylines` | Ground-truth navigation trace(s) for a Bicycle  
`has_human` | `BooleanField` | Whether a human trace is present  
`has_legged_robot` | `BooleanField` | Whether a legged robot trace is present  
`has_wheeled_robot` | `BooleanField` | Whether a wheeled robot trace is present  
`has_bicycle` | `BooleanField` | Whether a bicycle trace is present  
  
### Polyline Details#

Each `fo.Polylines` label field may contain one or more `fo.Polyline` objects. Multiple polylines within a field represent equally valid alternative paths annotated for the same scenario (annotator-provided alternatives). Points are normalized to `[0, 1]` in `(x, y)` image coordinates, where `(0, 0)` is the top-left and `(1, 1)` is the bottom-right. All traces originate near the bottom-center of the image (`[0.5, 0.95]`), representing the embodimentâs start position. Polylines have `closed=True` and `filled=False`.

### Trace Coverage#

Field | Samples with traces  
---|---  
`human` | 500 / 1002 (validation split)  
`legged_robot` | 501 / 1002  
`wheeled_robot` | 276 / 1002  
`bicycle` | 232 / 1002  
  
Note: coverage reflects the validation split, as test split ground truths are withheld.

* * *

## Citation#
    
    
    @article{windecker2025navitrace,
      title={NaviTrace: Evaluating Embodied Navigation of Vision-Language Models},
      author={Windecker, Tim and Patel, Manthan and Reuss, Moritz and Schwarzkopf, Richard and Cadena, Cesar and Lioutikov, Rudolf and Hutter, Marco and Frey, Jonas},
      journal={arXiv preprint arXiv:2510.26909},
      year={2025}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
