---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/s5mars.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/S5Mars)

# Dataset Card for S5Mards Dataset#

![image/png](https://huggingface.co/datasets/Voxel51/S5Mars/resolve/main/s5mars.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 6000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/S5Mars")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

### Dataset Description#

S5Mars (Semi-SuperviSed learning on Mars Semantic Segmentation) is a high-resolution Mars terrain semantic segmentation dataset containing 6,000 images captured by the Mars Science Laboratory (MSL) Curiosity rover. The dataset features sparse, high-confidence annotations designed to support semi-supervised learning approaches for Martian terrain analysis.

The dataset addresses the challenge of limited high-quality annotations for Mars imagery by providing carefully curated, confidence-based sparse annotations. This enables research into semi-supervised learning methods that can leverage both labeled and unlabeled Mars terrain data for autonomous rover navigation and planning.

Each image is annotated with pixel-level semantic segmentation masks covering 9 terrain classes commonly encountered in Martian landscapes.

  * **Curated by:** Jiahang Zhang, Lilang Lin, Zejia Fan, Wenjing Wang, Jiaying Liu (Peking University)

  * **License:** Research use

  * **Language(s):** N/A (Image dataset)




### Dataset Sources#

  * **Repository:** [JHang2020/S5Mars_SSL](https://github.com/JHang2020/S5Mars_SSL)

  * **Paper:** [S5Mars: Semi-Supervised Learning for Mars Semantic Segmentation](https://ieeexplore.ieee.org/document/10499211) (IEEE TGRS 2024)

  * **Original Data Download:** [Google Drive](https://drive.google.com/file/d/130R5z9v2NChVuseNDsH0zSTMolteELkO/view)




## Uses#

### Direct Use#

This dataset is suitable for:

  * **Mars terrain semantic segmentation** : Training and evaluating models for pixel-level classification of Martian terrain

  * **Semi-supervised learning research** : Developing methods that leverage sparse annotations with unlabeled data

  * **Autonomous rover navigation** : Building perception systems for safe path planning on Mars

  * **Transfer learning** : Pre-training or fine-tuning models for planetary science applications

  * **Domain adaptation** : Studying domain shift between Earth and Mars imagery




### Out-of-Scope Use#

  * Real-time mission-critical rover navigation without additional validation

  * Medical or safety-critical applications

  * Any use requiring absolute ground truth accuracy (annotations are sparse and confidence-based)




## Dataset Structure#

### Image Data#

  * **Total images:** 6,000

  * **Resolution:** 1200 Ã 1200 pixels

  * **Format:** JPEG

  * **Source:** Mars Science Laboratory (MSL) Curiosity rover imagery

  * **Difficulty splits:**

    * `easy/`: 3,000 images with clearer terrain boundaries

    * `hard/`: 3,000 images with more challenging segmentation scenarios




### Annotations#

  * **Format:** PNG semantic segmentation masks (1200 Ã 1200 pixels)

  * **Annotation style:** Sparse, confidence-based labeling




### Semantic Classes#

Pixel Value | Class Name | Description  
---|---|---  
0 | background | Unlabeled/null regions  
1 | sky | Martian sky  
2 | ridge | Ridge formations  
3 | soil | Martian soil  
4 | sand | Sandy terrain  
5 | bedrock | Exposed bedrock  
6 | rock | Individual rocks  
7 | rover | Rover components visible in frame  
8 | trace | Rover wheel tracks/traces  
9 | hole | Holes or depressions  
  
### Data Splits#

Split | Samples | Description  
---|---|---  
Train | 5,000 | Training set  
Validation | 500 | Validation set  
Test | 500 | Held-out test set  
  
### FiftyOne Dataset Format#

This dataset is provided in [FiftyOne](https://docs.voxel51.com/) format for easy visualization, exploration, and integration with ML workflows.

#### Sample Fields#

Field | Type | Description  
---|---|---  
`filepath` | `string` | Absolute path to the image file  
`tags` | `list[string]` | Data split membership: `["train"]`, `["val"]`, or `["test"]`  
`difficulty` | `string` | Image difficulty category: `"easy"` or `"hard"`  
`ground_truth` | `fo.Segmentation` | Semantic segmentation mask  
`metadata` | `fo.ImageMetadata` | Image dimensions, size, etc.  
  
#### Mask Targets#

The `ground_truth` segmentation field uses the following `mask_targets` mapping:
    
    
    dataset.mask_targets = {
        "ground_truth": {
            1: "sky",
            2: "ridge",
            3: "soil",
            4: "sand",
            5: "bedrock",
            6: "rock",
            7: "rover",
            8: "trace",
            9: "hole",
        }
    }
    

**Note:** Pixel value `0` represents background/unlabeled regions and is rendered as invisible in FiftyOneâs App.

#### Loading the Dataset#
    
    
    import fiftyone as fo
    
    # Load the dataset
    dataset = fo.load_dataset("s5mars")
    
    # View dataset info
    print(dataset)
    
    # Filter by split
    train_view = dataset.match_tags("train")
    test_view = dataset.match_tags("test")
    
    # Filter by difficulty
    easy_view = dataset.match(F("difficulty") == "easy")
    hard_view = dataset.match(F("difficulty") == "hard")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Creation#

### Curation Rationale#

Deep learning has become a powerful tool for Mars exploration, with terrain semantic segmentation being fundamental for rover autonomous planning and safe driving. However, there is a lack of sufficient detailed and high-confidence data annotations required by most deep learning methods.

S5Mars addresses this gap by providing:

  1. High-resolution imagery from actual Mars rover missions

  2. Sparse but high-confidence annotations based on annotator certainty

  3. A benchmark for semi-supervised learning approaches tailored to Mars imagery




### Source Data#

#### Data Collection and Processing#

Images were collected from the Mars Science Laboratory (MSL) Curiosity roverâs navigation and science cameras. The dataset includes both âeasyâ and âhardâ subsets, categorized based on the complexity of terrain boundaries and segmentation difficulty.

#### Who are the source data producers?#

  * **Original imagery:** NASA/JPL-Caltech Mars Science Laboratory mission

  * **Dataset curation:** Researchers at Peking University




### Annotations#

#### Annotation process#

Annotations follow a sparse, confidence-based labeling strategy:

  * Annotators label regions where they have high confidence in the terrain classification

  * Ambiguous or uncertain regions are left unlabeled (pixel value 0)

  * This approach ensures high label quality at the cost of completeness




#### Who are the annotators?#

Annotations were created by the research team at Peking University as part of the S5Mars project.

#### Personal and Sensitive Information#

This dataset contains no personal or sensitive information. All images are of Martian terrain captured by NASAâs publicly available rover imagery.

## Bias, Risks, and Limitations#

  * **Sparse annotations:** Not all pixels are labeled; unlabeled regions should not be treated as negative examples

  * **Class imbalance:** Sky and common terrain types dominate; rare classes like âroverâ and âholeâ have fewer samples

  * **Sensor-specific:** Images are from MSL Curiosity rover cameras; may not generalize to other Mars missions

  * **Lighting conditions:** Martian lighting varies; model performance may vary across different times of day

  * **Annotation subjectivity:** Terrain class boundaries can be ambiguous (e.g., soil vs. sand)




### Recommendations#

  * Use semi-supervised learning approaches to leverage unlabeled regions

  * Consider class-weighted losses to handle imbalance

  * Validate on the held-out test set before deployment

  * For critical applications, combine with additional human review




## Citation#

**BibTeX:**
    
    
    @ARTICLE{10499211,
      author={Zhang, Jiahang and Lin, Lilang and Fan, Zejia and Wang, Wenjing and Liu, Jiaying},
      journal={IEEE Transactions on Geoscience and Remote Sensing}, 
      title={S5Mars: Semi-Supervised Learning for Mars Semantic Segmentation}, 
      year={2024},
      volume={62},
      pages={1-15},
      doi={10.1109/TGRS.2024.33870211}
    }
    

**APA:**

Zhang, J., Lin, L., Fan, Z., Wang, W., & Liu, J. (2024). S5Mars: Semi-Supervised Learning for Mars Semantic Segmentation. _IEEE Transactions on Geoscience and Remote Sensing_ , 62, 1-15.

## Glossary#

  * **MSL:** Mars Science Laboratory, NASAâs Mars rover mission featuring the Curiosity rover

  * **Semi-supervised learning:** Machine learning approach using both labeled and unlabeled data

  * **Semantic segmentation:** Pixel-level classification task assigning a class label to each pixel

  * **Sparse annotation:** Labeling strategy where only confident regions are annotated




## Dataset Card Contact#

For questions about the original dataset, please refer to the [GitHub repository](https://github.com/JHang2020/S5Mars_SSL) or contact the paper authors.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
