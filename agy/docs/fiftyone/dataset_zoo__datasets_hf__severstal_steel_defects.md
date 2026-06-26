---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/severstal_steel_defects.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/severstal_steel_defects)

# Dataset Card for severstal_steel_defects#

![image/png](https://huggingface.co/datasets/Voxel51/severstal_steel_defects/resolve/main/severstal.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 18074 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/severstal_steel_defects")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Severstal: Steel Defect Detection is a surface defect segmentation dataset released for a 2019 Kaggle competition by Severstal, a Russian steel and mining company. The task is to localize and classify defects on flat sheet steel from high-frequency camera images. Each image may contain no defects, a single defect class, or multiple defect classes (ClassId 1-4). Annotations were originally provided as run-length encoded (RLE) masks in train.csv.

  * **Curated by:** Severstal (Kaggle contributors: Alexey Grishin, BorisV, iBardintsev, inversion, Oleg)

  * **Funded by:** Severstal PAO

  * **Shared by:** Severstal, via Kaggle (2019)

  * **Language(s) (NLP):** N/A (image data; metadata in English)




### Dataset Sources#

  * **Repository:** https://www.kaggle.com/competitions/severstal-steel-defect-detection

  * **Paper:** None (competition dataset, no accompanying paper)




## Uses#

### Direct Use#

  * Training and benchmarking semantic / instance segmentation models for surface defect detection on flat sheet steel.

  * Multi-label image classification (defect present / absent per class).

  * Multi-class imbalanced-data research (class 3 dominates; class 2 is rare).

  * Pretraining or transfer-learning source for related industrial visual inspection tasks.




### Out-of-Scope Use#

  * Generalizing to non-steel manufacturing surfaces, 3D defects, or other imaging modalities without further validation.

  * Production deployment as-is: defect taxonomy is plant-specific to Severstalâs process and likely does not transfer to other mills.

  * The original Kaggle test split has no public ground truth, so it should not be treated as a held-out evaluation set outside the competition.




## Dataset Structure#

  * **Total samples:** 18,074 images

  * **Labeled objects:** 19,958 (pixel-level instance segmentation)

  * **Classes:** 4 defect classes (ClassId = 1, 2, 3, 4); class 3 most common, class 2 least common

  * **Unlabeled (no-defect) images:** ~11,408 (~63%)

  * **Original splits:** train (12,568) and test (5,506); test labels are not publicly released

  * **Image format:** grayscale steel surface images (stored as 3-channel), long aspect ratio

  * **Annotation format (source):** RLE-encoded masks in train.csv, one row per (ImageId, ClassId)




## Dataset Creation#

### Curation Rationale#

Severstal uses high-frequency cameras over its production line and wanted better automated defect localization and classification to improve quality control across heating, rolling, drying, and cutting stages. The Kaggle competition was framed as a way to improve their existing defect detection algorithm.

### Source Data#

#### Data Collection and Processing#

Images were captured by high-frequency cameras mounted on Severstalâs flat-sheet steel production line. The specific camera hardware, lighting setup, and sampling procedure are not publicly documented.

#### Who are the source data producers?#

Severstalâs steel production facilities (Russia).

### Annotations#

#### Annotation process#

Not publicly documented. Annotations are pixel-level masks per defect class provided as RLE strings.

## Bias, Risks, and Limitations#

  * Heavy class imbalance: class 3 dominates; class 2 is comparatively rare.

  * ~63% of images contain no defects, which biases training if not handled.

  * Defect taxonomy reflects Severstalâs internal categorization and may not match defect schemes used by other steel producers.

  * Train vs. test distribution shift was widely reported by competitors (significant public/private leaderboard shakeup), suggesting non-trivial domain shift within the dataset itself.

  * The public release contains no test-set ground truth.




### Recommendations#

Account for class imbalance (weighted loss, sampling, or a defect/no-defect classifier upstream of segmentation). When using the original splits, be aware that the test split labels are not public, so create your own held-out split for development.

## Citation#

**BibTeX:**
    
    
    @misc{severstal-steel-defect-detection,
      author = {Alexey Grishin and BorisV and iBardintsev and inversion and Oleg},
      title  = {Severstal: Steel Defect Detection},
      year   = {2019},
      publisher = {Kaggle},
      url    = {https://kaggle.com/competitions/severstal-steel-defect-detection}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
