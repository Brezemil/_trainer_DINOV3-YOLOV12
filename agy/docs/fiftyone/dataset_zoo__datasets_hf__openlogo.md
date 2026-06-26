---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/openlogo.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/OpenLogo)

# Dataset Card for Dataset Name#

![image/png](https://huggingface.co/datasets/Voxel51/OpenLogo/resolve/main/openlogo.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 27083 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/OpenLogo")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The QMUL-OpenLogo dataset is a large-scale logo detection benchmark designed for evaluating open logo detection algorithms in realistic deployment scenarios. Unlike traditional logo detection datasets that assume exhaustive fine-grained labeling for all classes, QMUL-OpenLogo simulates real-world conditions where new logo classes arrive progressively and require detection with little or no labeled training data.

The dataset was created by aggregating and refining 7 existing logo detection datasets to establish a comprehensive benchmark for open logo detection. It contains 27,083 images across 352 logo classes, with a distinctive train/test split that designates only 32 classes as âsupervisedâ (with labeled bounding boxes) while the remaining 320 classes are âunsupervisedâ (having only clean logo design images).

  * **Curated by:** Queen Mary University of London (QMUL) and Vision Semantics Limited

  * **Funded by:** China Scholarship Council, Vision Semantics Ltd, Royal Society Newton Advanced Fellowship Programme (NA150459), Innovate UK Industrial Challenge Project

  * **Shared by:** Available at https://qmul-openlogo.github.io/

  * **Language(s) (NLP):** Not applicable (computer vision dataset)

  * **License:** [More Information Needed]




### Dataset Sources#

  * **Repository:** https://qmul-openlogo.github.io/

  * **Paper:** âOpen Logo Detection Challengeâ by Su et al. (arXiv:1807.01964v3)




## Dataset Structure#

The QMUL-OpenLogo dataset follows a unique structure designed for open logo detection evaluation:

### Original Format#

The dataset aggregates 7 existing logo detection datasets:

  * FlickrLogos-27, FlickrLogos-32, Logo32plus, BelgaLogos, WebLogo-2M (test), Logo-In-The-Wild, SportsLogo




### Key Statistics#

  * **Total images** : 27,083

  * **Logo classes** : 352

  * **Logo instances** : Variable (10-1,902 per class, mean 88.25)

  * **Scale variation** : 0.0014%-100% of image area (mean 6.09%)

  * **Highly imbalanced distribution** : Significant variation in samples per class




### Data Splits#

The dataset uses a novel split designed for open logo detection:

**Supervised Classes (32 classes)** :

  * Train: 1,280 images (40 per class from FlickrLogo32)

  * Val: 1,019 images

  * Test: 9,168 images

  * Logo designs: 32 clean design images (1 per class)




**Unsupervised Classes (320 classes)** :

  * Train: 0 images (no labeled training data)

  * Val: 1,562 images

  * Test: 14,054 images

  * Logo designs: 320 clean design images (1 per class)




### FiftyOne Dataset Structure#

This dataset has been converted to FiftyOne format with the following fields:

  * **filepath** : Path to the image file

  * **split** : Train/val/test designation

  * **supervision_level** : âsupervisedâ or âunsupervisedâ based on availability of labeled training data

  * **width/height** : Image dimensions

  * **ground_truth** : Detection objects with bounding boxes and labels

  * **num_logos** : Count of logos in the image

  * **logo_classes** : List of unique logo classes present




The FiftyOne dataset enables interactive visualization, filtering by supervision level, and analysis through the FiftyOne web interface.

Detailed technical information about the dataset creation methodology and evaluation protocol can be found in the accompanying research paper (1807.01964v3.pdf).

## Dataset Creation#

### Curation Rationale#

The QMUL-OpenLogo dataset was created to address a significant gap in existing logo detection benchmarks. Traditional benchmarks assume artificial deployment scenarios where large training datasets with fine-grained bounding box annotations are available for each class. However, in realistic logo detection scenarios, new logo classes come progressively and require detection with little or no budget for exhaustively labeling training data.

The dataset aims to provide a more realistic and challenging evaluation setting that better reflects real-world deployment constraints where scalability and adaptability to new classes are crucial.

### Source Data#

The source data consists of images from 7 existing publicly available logo detection datasets, carefully merged and refined to create a cohesive benchmark.

#### Data Collection and Processing#

**Source Dataset Integration** : The following datasets were aggregated:

  1. FlickrLogos-27 (27 classes, 810 images)

  2. FlickrLogos-32 (32 classes, 2,240 images)

  3. Logo32plus (32 classes, 7,830 images)

  4. BelgaLogos (37 classes, 1,321 images)

  5. WebLogo-2M Test only (194 classes, 4,318 images)

  6. Logo-In-The-Wild (1,196 classes, 9,393 images)

  7. SportsLogo (20 classes, 1,978 images)




**Class Refinement Process** :

  * Logo classes were made consistent across datasets (e.g., merging Adidas trefoil/text variations from LITW into single classes)

  * Erroneous annotations were cleaned (incorrect bounding box coordinates, size inconsistencies)

  * Classes with fewer than 10 images were removed to ensure sufficient test data

  * Manual verification of 1-3 random images per class was performed

  * Final result: 352 logo classes from 27,083 images




#### Who are the source data producers?#

The original data producers are the creators of the 7 source datasets, representing diverse research groups and data collection efforts. The QMUL team performed the aggregation, refinement, and standardization process to create the unified benchmark.

### Annotations#

The dataset contains bounding box annotations inherited and refined from the source datasets.

#### Annotation process#

The annotation process involved:

  * **Integration** : Combining annotations from multiple source datasets with varying formats

  * **Standardization** : Making logo class definitions consistent across datasets

  * **Quality control** : Removing erroneous annotations and verifying class labels

  * **Clean-up** : Filtering out classes with insufficient data (<10 images)

  * **Validation** : Manual verification of sample images per class




The annotations maintain the PASCAL VOC format for bounding boxes with class labels.

#### Who are the annotators?#

The original annotations were created by the respective research teams for each source dataset. The QMUL team performed quality control, merging, and verification processes.

#### Personal and Sensitive Information#

The dataset primarily focuses on commercial logos and brand imagery collected from existing research datasets. Considerations include:

  * **Commercial imagery** : Contains copyrighted logos and brand materials

  * **Incidental content** : May contain people, locations, or other identifiable information as part of the natural scene context

  * **Web-sourced content** : Some source datasets used web-collected imagery which may contain various types of content




No specific anonymization process is described. Users should be aware that aggregated web imagery may contain incidental personal or sensitive information.

## Citation#

**BibTeX:**
    
    
    @article{su2018open,
      title={Open Logo Detection Challenge},
      author={Su, Hang and Zhu, Xiatian and Gong, Shaogang},
      journal={arXiv preprint arXiv:1807.01964},
      year={2018},
      institution={Queen Mary University of London, Vision Semantics Limited}
    }
    

**APA:**

Su, H., Zhu, X., & Gong, S. (2018). Open Logo Detection Challenge. arXiv preprint arXiv:1807.01964.

## More Information#

This dataset represents a significant contribution to realistic logo detection evaluation. Key insights from the research:

  * **Novel evaluation protocol** : Introduces the concept of open logo detection with supervised/unsupervised class splits

  * **Context Adversarial Learning (CAL)** : The paper proposes CAL for generating context-consistent synthetic training data

  * **Performance benchmarks** : Establishes baseline performance using YOLO9000, YOLOv2, and Faster R-CNN

  * **Challenging nature** : Demonstrates that current state-of-the-art methods struggle with realistic deployment scenarios




Detailed technical information about the dataset creation, evaluation protocol, and experimental results can be found in the research paper `1807.01964v3.pdf` included with this dataset.

The benchmark is particularly valuable for:

  * Developing scalable logo detection methods

  * Testing synthetic data generation approaches

  * Evaluating open-set detection capabilities

  * Researching incremental learning for object detection




## Dataset Card Authors#

This dataset card was created based on information from the original research paper âOpen Logo Detection Challengeâ and analysis of the dataset structure.

## Dataset Card Contact#

For questions about the original dataset:

  * **Primary contact** : Queen Mary University of London, School of EECS

  * **Website** : https://qmul-openlogo.github.io/

  * **Paper authors** : Hang Su, Xiatian Zhu, Shaogang Gong




For questions about the FiftyOne conversion and processing scripts in this repository, refer to the accompanying documentation and README files.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
