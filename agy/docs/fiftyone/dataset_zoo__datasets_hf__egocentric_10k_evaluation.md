---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/egocentric_10k_evaluation.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Egocentric_10K_Evaluation)

# Dataset Card for Egocentric_10K_Evaluation#

![image/png](https://huggingface.co/datasets/Voxel51/Egocentric_10K_Evaluation/resolve/main/egocentric10k_eval.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 30000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/Egocentric_10K_Evaluation")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Egocentric-10K-Evaluation is a benchmark evaluation set and analysis protocol for large-scale egocentric (first-person) video datasets, focused on measuring hand visibility and active manipulation in real-world, in-the-wild scenarios, especially relevant for robotics, computer vision, and AI agent training on manipulation tasks.[1][2][3]

  * **Curated by:** builddotai

  * **Shared by :** builddotai

  * **License:** Apache 2.0




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/builddotai/Egocentric-10K-Evaluation




## Uses#

### Direct Use#

This dataset is intended for benchmarking egocentric video data with respect to hand presence and active object manipulation, enabling standardized analysis, dataset comparison, and the development/evaluation of perception and robotics models centered on real-world human skill tasks.

## Dataset Structure#

Egocentric-10K-Evaluation consists of 10,000 sampled frames from factory egocentric video and comparable samples from other major datasets (Ego4D, EPIC-KITCHENS); each sample includes JSON metadata, hand label annotations (count 0, 1, or 2), and a binary label for presence/absence of active manipulation. The splits are standardized; additional metadata includes dataset, worker, and video index references.

## Dataset Creation#

### Curation Rationale#

To create a standardized benchmark for hand visibility and manipulation, facilitating research on manipulation-heavy tasks in robotics and AI using real industrial and skill-focused footage.

### Source Data#

#### Data Collection and Processing#

The evaluation set comprises frames drawn from the primary Egocentric-10K dataset (real-world factory footage collected via head-mounted cameras), as well as standardized samples from open egocentric datasets Ego4D and EPIC-KITCHENS for comparison. Data is provided in 1080p, 30 FPS H.265 MP4 format, with structured JSON metadata and hand/manipulation annotations.

#### Who are the source data producers?#

Egocentric-10Kâs original video data was produced by real factory workers wearing head-mounted cameras, performing natural work-line activities. Annotation was performed following strict guidelines as described in the evaluation schema.

### Annotations#

#### Annotation process#

Each sampled frame is annotated for number of visible hands (0/1/2; detailed rules provided) and whether the hands are engaged in active manipulation (âyesâ/ânoâ per explicit definition). The annotation schema and rules are detailed in the benchmark documentation.

## Citation#

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
