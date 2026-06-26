---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/refcoco_m.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/RefCOCO-M)

# Dataset Card for RefCOCO-M#

![image/png](https://huggingface.co/datasets/Voxel51/RefCOCO-M/resolve/main/refcoc-m.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1190 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/RefCOCO-M")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

RefCOCO-M is a cleaned and improved version of the RefCOCO (UNC) validation split for referring expression segmentation. It addresses key limitations of the original RefCOCO dataset by replacing hand-drawn polygon masks with pixel-accurate instance masks and removing problematic prompts. The dataset contains 1,190 images, 2,080 instance masks, and 5,598 referring expressions. This FiftyOne format version preserves all referring expressions as individual detections with instance segmentation masks.

The original RefCOCO masks were hand-drawn polygons that were often coarse or inaccurate, with inflated boundaries and missing fine structure. RefCOCO-M provides high-quality masks with much finer pixel-level accuracy, greatly improving both training and evaluation for models focused on visual grounding and referring expression comprehension.

  * **Curated by:** Moondream AI

  * **Language(s) (NLP):** en

  * **License:** MIT




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/moondream/refcoco-m




## Uses#

### Direct Use#

This dataset is intended for training and evaluating referring expression segmentation models, where the task is to segment an object in an image given a natural language description. It serves as an updated benchmark for various models in visual reasoning, segmentation, and Vision-Language tasks, including tasks like segmentation by referring expression, part-level grounding, and fine-grained object localization. RefCOCO-M offers clearer and higher-quality annotations, benefiting both model development and validation for state-of-the-art model benchmarking.

## Dataset Structure#

This FiftyOne dataset contains images with instance segmentation annotations. Each sample includes:

**Sample-level fields:**

  * `filepath`: Path to the image file

  * `image_id`: COCO image identifier (int64)

  * `file_name`: Original COCO 2014 filename (string)

  * `detections`: FiftyOne Detections field containing all referring expressions




**Detection-level fields (within` detections`):**

  * `label`: The referring expression text (e.g., âleft guyâ, âperson on leftâ)

  * `bounding_box`: Normalized bounding box coordinates [x, y, width, height] in [0, 1] range

  * `mask`: Instance segmentation mask cropped to the bounding box region (2D binary numpy array)

  * `confidence`: Always 1.0

  * `category`: COCO category label (e.g., âpersonâ)

  * `supercategory`: COCO supercategory label

  * `ref_id`: Unique instance identifier linking referring expressions to the same object




**Key characteristics:**

  * Multiple referring expressions for the same object instance share the same `ref_id`, `bounding_box`, and `mask`

  * Each referring expression is stored as a separate detection for evaluation purposes

  * Masks are pixel-accurate and cropped to their respective bounding boxes

  * Total of 5,598 detections across 1,190 images (average ~4.7 referring expressions per image)




## Dataset Creation#

### Curation Rationale#

RefCOCO has been a long-standing benchmark for referring expression segmentation, but suffers from poor mask quality (hand-drawn polygons with coarse boundaries and missing fine structure) and harmful referring expressions. RefCOCO-M addresses these issues by re-segmenting instances with modern models to provide pixel-accurate masks and filtering inappropriate content, ensuring clarity and consistency in the annotations.

### Source Data#

#### Data Collection and Processing#

The dataset is derived from the RefCOCO (UNC) validation split. A re-segmentation pipeline using an ensemble of modern segmentation models was applied to each instance, keeping only high-confidence masks. This process removed 47% of masks due to unrecoverable quality issues. A separate model filtered an additional 0.5% of samples containing harmful language (slurs, sexualized language, and degrading phrases), removing 46 samples total. The images and referring expressions remain identical to the original RefCOCO validation set where retained.

#### Who are the source data producers?#

The original RefCOCO dataset was derived from COCO 2014 images with referring expressions collected through crowdsourcing. RefCOCO-M maintains the same images and referring expressions from the original validation set.

### Annotations#

#### Annotation process#

The original referring expressions from RefCOCO validation set are preserved. Instance masks were automatically re-generated using an ensemble of modern segmentation models to produce pixel-accurate annotations with tighter boundaries and finer details compared to the original hand-drawn polygons.

#### Who are the annotators?#

The referring expressions are from the original RefCOCO dataset crowdsourcing effort. The improved masks were generated automatically using an ensemble of modern segmentation models.

#### Personal and Sensitive Information#

The dataset has been filtered to remove samples containing harmful language including slurs, sexualized language, and degrading phrases. 46 samples were removed during the safety filtering process.

## Citation#
    
    
    @misc{moondream2025refcocom,
      author = {Moondream AI},
      title = {RefCOCO-M: Refined Referring Expression Segmentation},
      year = {2025},
      publisher = {Hugging Face},
      howpublished = {\url{https://huggingface.co/datasets/moondream/refcoco-m}}
    }
    

## Glossary#

  * **Referring Expression** : A natural language phrase that describes a specific object instance in an image

  * **Instance Segmentation** : Pixel-level segmentation that identifies and delineates individual object instances

  * **RLE (Run-Length Encoding)** : A compressed format for storing binary masks used in COCO format

  * **IoU (Intersection over Union)** : Standard metric for evaluating segmentation quality, computed as the ratio of overlapping area to total area covered by predicted and ground-truth masks

  * **Visual Grounding** : The task of localizing objects or regions in an image based on natural language descriptions




## More Information#

RefCOCO-M facilitates better evaluation of models such as Moondream VLMs and comparable architectures, providing more challenging and fine-grained annotation cues for practical use and fairness in comparisons. The dataset is actively maintained on Hugging Face, supporting open-source and reproducible research.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
