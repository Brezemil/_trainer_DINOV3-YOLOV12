---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/maptrace_20k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/maptrace_20k)

# Dataset Card for MapTrace-20k#

![image/png](https://huggingface.co/datasets/Voxel51/maptrace_20k/resolve/main/maptrace20k.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 20000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/maptrace_20k")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

MapTrace is a synthetic dataset for path tracing on maps. The dataset contains annotated paths designed to train vision-language models on route-tracing tasks. Each sample consists of a map image annotated with start (green) and end (red) positions, along with a natural language prompt and ground truth path coordinates.

The `maptrace_20k` split used here contains paths on stylized maps such as those found in brochures, park directories, or shopping malls.

  * **Curated by:** Google

  * **Language(s) (NLP):** English

  * **License:** CC-BY-4.0




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/google/MapTrace




## Uses#

### Direct Use#

This dataset is intended for training and evaluating vision-language models on spatial reasoning and path-tracing tasks. Models are expected to interpret map images with marked start/end locations and output coordinate sequences representing valid paths between those points.

## Dataset Structure#

### Original Schema (Hugging Face)#

The `maptrace_20k` split contains the following fields:

  * `image`: The image bytes of the map, annotated with start and end positions

  * `label`: A string representation of a list of (x, y) coordinate tuples defining the target path (normalized between 0 and 1)

  * `input`: A natural language prompt asking the model to find the path




### FiftyOne Schema#

The FiftyOne dataset converts the original format into the following structure:

**Sample Fields:**

  * `filepath`: Path to the PNG image file

  * `input` (StringField): The natural language prompt describing the task

  * `ground_truth` (Keypoints): The path represented as keypoints with the following properties:

    * Each keypoint is labeled alphabetically (A, B, C, â¦, Z, AA, AB, etc.)

    * Points are normalized coordinates in [0, 1] range

    * The number of keypoints varies per sample




**Dataset-Level Attributes:**

  * `default_skeleton`: A `KeypointSkeleton` that connects sequential keypoints (AâBâCâDâ¦) to visualize the path as a connected polyline in the FiftyOne App




## Dataset Creation#

### Source Data#

#### Data Collection and Processing#

The dataset is synthetically generated. Maps are created using text-to-image generation models from natural language map descriptions. Paths are then annotated on these synthetic map images with start positions marked in green and end positions marked in red.

## Citation#

**BibTeX:**
    
    
    @misc{panagopoulou2025maptracescalabledatageneration,
          title={MapTrace: Scalable Data Generation for Route Tracing on Maps}, 
          author={Artemis Panagopoulou and Aveek Purohit and Achin Kulshrestha and Soroosh Yazdani and Mohit Goyal},
          year={2025},
          eprint={2512.19609},
          archivePrefix={arXiv},
          primaryClass={cs.CV},
          url={https://arxiv.org/abs/2512.19609}, 
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
