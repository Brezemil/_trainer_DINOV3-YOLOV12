---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/nutrigreen.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/NutriGreen)

# Dataset Card for nutrigreen_dataset#

![image/png](https://huggingface.co/datasets/Voxel51/NutriGreen/resolve/main/nutrigreen_dataset.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 7271 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/NutriGreen")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Card for NutriGreen Image Dataset#

## Dataset Details#

### Dataset Description#

The NutriGreen Image Dataset is a collection of images representing branded packaged food products, designed for training segmentation models to detect various labels on food packaging. Each image is annotated with three distinct label types: Nutri-Score (indicating nutritional quality with grades A-E), V-label (denoting vegan or vegetarian products), and EU organic certification (BIO) logo.

The dataset was created using a semi-automatic annotation pipeline that combines domain expert annotation with automated annotation using deep learning models.

  * **Curated by:** Jan Drole, Igor Pravst, Tome Eftimov, Barbara KorouÅ¡iÄ Seljak (JoÅ¾ef Stefan Institute, University of Ljubljana, Nutrition Institute)

  * **Funded by:** Do.IT project (Ministry of Public Administration of the Republic of Slovenia, MJU C3130-21-151067), Slovenian Research and Innovation Agency national research programs P2-0098 âComputer Systems and Structuresâ and P3-0395 âNutrition and Public Health,â FoodMarketMap project within FOODITY (EU Horizon Europe grant agreement NÂ° 101086105)

  * **Shared by:** Authors via Zenodo and described in Frontiers in Nutrition

  * **Language(s) (NLP):** en (English) - product packaging text

  * **License:** Creative Commons Attribution Share Alike 4.0 International (CC-BY-SA)




#### Dataset Sources#

  * **Repository:** https://zenodo.org/records/8374047

  * **Paper:** Drole J, Pravst I, Eftimov T and KorouÅ¡iÄ Seljak B (2024) NutriGreen image dataset: a collection of annotated nutrition, organic, and vegan food products. Front. Nutr. 11:1342823. doi: 10.3389/fnut.2024.1342823




## Uses#

### Direct Use#

This dataset is designed for:

  * Training and evaluating object detection and segmentation models for food label recognition

  * Developing computer vision systems for automatic identification of nutritional quality labels (Nutri-Score), vegan/vegetarian labels (V-label), and organic certification (BIO) on food packaging

  * Benchmarking computer vision systems for food packaging analysis with FiftyOne

  * Supporting applications that help consumers make informed food choices based on nutritional and ethical considerations

  * Research into food labeling effectiveness and consumer decision-making

  * Interactive dataset exploration and visualization using FiftyOne




### Out-of-Scope Use#

The dataset should not be used for:

  * Making definitive health or nutritional claims without expert consultation

  * Replacing professional nutritional advice

  * Commercial applications without proper attribution under CC-BY-SA license terms

  * Training models to verify the authenticity or accuracy of the labels themselves (the dataset assumes labels on products are correctly applied)




## Dataset Structure#

### FiftyOne Format#

This dataset is available in **FiftyOne format** , which provides a standardized structure for computer vision datasets with powerful querying, visualization, and analysis capabilities.

**Dataset Metadata:**
    
    
    Name:        nutrigreen_dataset
    Media type:  image
    Num samples: 7271
    Persistent:  False
    Tags:        []
    

**Sample Fields:**

Each sample in the dataset contains the following fields:

  * **`id`** (`ObjectIdField`): Unique identifier for each sample

  * **`filepath`** (`StringField`): Path to the image file on disk

  * **`tags`** (`ListField[StringField]`): List of custom tags for organizing and filtering samples

  * **`metadata`** (`EmbeddedDocumentField[ImageMetadata]`): Image metadata including:

    * Image dimensions (width, height)

    * Number of channels

    * File size

    * MIME type

  * **`created_at`** (`DateTimeField`): Timestamp when the sample was added to the dataset

  * **`last_modified_at`** (`DateTimeField`): Timestamp of the last modification to the sample

  * **`ground_truth`** (`EmbeddedDocumentField[Detections]`): Ground truth annotations containing:

    * **Detections** : List of bounding box annotations, each with:

      * `label`: Label class (e.g., âNutriScoreAâ, âBIOâ, âVlabelâ)

      * `bounding_box`: Normalized coordinates `[x, y, width, height]` in relative format (0-1)

      * `confidence`: Optional confidence score (for model predictions)

      * Additional custom attributes as needed




**Note on Sample Count:** The FiftyOne dataset contains **7,271 samples** , which differs from the original 10,472 images reported in the publication. This discrepancy may be due to:

  * Filtering of images without valid annotations

  * Removal of duplicate images

  * Exclusion of the 3,201 images labeled as âno labelsâ

  * Data preprocessing or quality control steps




### Label Distribution#

The original dataset comprises **10,472 total images** with the following label distribution:

**Nutri-Score labels (nutritional quality):**

  * Grade A (highest nutritional quality): 1,250 images

  * Grade B: 1,107 images

  * Grade C: 867 images

  * Grade D: 1,001 images

  * Grade E (lowest nutritional quality): 967 images




**Other labels:**

  * V-Label (vegan/vegetarian): 870 images

  * BIO (EU organic): 2,328 images

  * No labels: 3,201 images




**Multi-label images:** Many images contain multiple labels. For example:

  * 202 images have both Nutri-Score A and BIO labels

  * 135 images have both Nutri-Score B and BIO labels

  * 146 images have both V-label and BIO labels




**Co-occurrence patterns:** The co-occurrence analysis shows that BIO and V-label products tend to have higher Nutri-Score grades (A and B) compared to lower grades (C, D, E), reflecting that many organic and vegan/vegetarian products are classified as healthier options.

### Original Format#

The dataset is also available in its original **YOLO format** :

**File structure:**

  * **data.csv** (485.4 kB): Contains annotation data in YOLO format with normalized bounding box coordinates

    * Format: `<class_id> <x_center> <y_center> <width> <height>` (normalized to image dimensions)

    * Each .txt file corresponds to an image and lists all detected labels with their coordinates

  * **dataset.zip** (5.1 GB): Complete image collection

  * Images are named using product barcode identifiers from Open Food Facts




**YOLO Annotation Format:**
    
    
    # Example: nutriScoreA (137).txt
    0 0.195542 0.797331 0.235056 0.11176
    

Where:

  * `0` = class ID (mapped to label name)

  * `0.195542` = x_center (normalized)

  * `0.797331` = y_center (normalized)

  * `0.235056` = width (normalized)

  * `0.11176` = height (normalized)




## Dataset Creation#

### Curation Rationale#

The dataset was created to address the lack of annotated food product image datasets that include standardized labels for nutritional quality and food characteristics. While existing food image recognition datasets focus on dish or ingredient recognition, this dataset specifically targets the detection of regulatory and voluntary labeling schemes on packaged food products.

The dataset supports:

  * Development of consumer-facing applications for informed food choices

  * Research into food labeling effectiveness and policy

  * Training of automated systems for food product analysis

  * Benchmarking of computer vision approaches for packaging label detection




### Source Data#

#### Data Collection and Processing#

**1\. Image Collection from Open Food Facts:**

Images were retrieved using the Open Food Facts API with the following process:

  * **API Query:** Used GET requests with specific filter tags:

    * `labels_tags=vegan` for vegan products

    * `labels_tags=bio` for organic products

    * `page_size=1,000` for batch retrieval

    * Nutri-Score filters for products with nutritional grades

  * **Barcode-based Retrieval:** Each product is identified by a unique barcode number

    * Barcodes â¤8 characters: Direct URL access at `https://openfoodfacts-images.s3.eu-west-3.amazonaws.com/data/{barcode}`

    * Barcodes >8 characters: Partitioned into subfolders using regex pattern `^(..)(..)(..)(.*)$`

      * Example: Barcode 3435660768163 â folder structure 343/566/076/8163

  * **Initial Categorization:** Retrieved images were categorized by label type (Nutri-Score A-E, BIO, V-label)

    * Note: At retrieval stage, images had metadata tags but no pixel-level segmentation annotations




**2\. Annotation Pipeline:**

The dataset was created through a multi-stage process:

**Stage 1: Manual Annotation (Ground Truth Creation)**

  * **Sample:** 300 images randomly selected per label type (2,100 images total across 7 labels)

  * **Tool:** MakeSense.ai open-source annotation tool

  * **Process:**

    * Annotators created rectangular bounding boxes around each label symbol

    * Boxes were drawn to tightly fit the entire symbol with minimal excess space

    * Each annotation was assigned to the appropriate label class

  * **Output:** Annotations exported in YOLO format (.txt files with normalized coordinates)




**Stage 2: Automated Annotation (Silver Standard)**

  * Seven separate YOLOv5 (x) models were trained, one per label type

  * These models automatically annotated the remaining images not in the manual annotation set

  * This created a âsilver standardâ with potential errors from automated detection




**Stage 3: Expert Validation (Gold Standard)**

  * All automated annotations were reviewed by two food science domain experts

  * Errors and false detections were corrected

  * Note: Validation focused on whether label logos were visible in images, not requiring specialized domain knowledge for this aspect




**Stage 4: Multi-label Annotation**

  * New models trained on validated gold standard data

  * Applied to all images to capture cases where multiple labels appear on single products

  * All multi-label annotations underwent final expert validation

  * **Result:** Final gold standard dataset with comprehensive multi-label annotations




**3\. Conversion to FiftyOne Format:**

The validated annotations were converted to FiftyOne format with the following mapping:

  * YOLO .txt files â FiftyOne `Detections` objects

  * Class IDs â Label strings (e.g., 0 â âNutriScoreAâ)

  * Normalized YOLO coordinates (x_center, y_center, width, height) â FiftyOne bounding boxes (x_top_left, y_top_left, width, height)

  * Image metadata extracted and stored in `metadata` field

  * Timestamps added for dataset management




#### Who are the source data producers?#

**Image Sources:** The source images come from **Open Food Facts** , an open-source, crowdsourced database of food product information. Contributors include:

  * Nutrition enthusiasts

  * Health advocates

  * Concerned consumers worldwide

  * The Open Food Facts community of volunteers




Open Food Facts is a collaborative initiative that allows anyone to contribute product information by entering data from product labels or uploading photos. The platformâs active community helps maintain accuracy and currency of information.

**Geographic Coverage:** Open Food Facts includes data from a wide range of countries and regions, though the specific geographic distribution of products in NutriGreen is not explicitly documented. The presence of EU organic logos and European labeling standards suggests significant European product representation.

**Image License:** Images are used under the Creative Commons Attribution ShareAlike license (CC-BY-SA) from Open Food Facts, allowing sharing, remixing, and commercial use with proper attribution.

### Annotations#

#### Annotation process#

The annotation process followed a semi-automatic pipeline with three quality levels:

**1\. Manual Annotation (Ground Truth):**

  * **Annotators:** Domain experts from the research team

  * **Tool:** MakeSense.ai open-source web-based annotation tool

  * **Sample size:** 300 images per label class

  * **Method:**

    * Rectangular bounding box annotation

    * Box placement to minimize excess space while fully containing the label

    * Class assignment for each annotated region

  * **Quality control:** Annotations reviewed during the process

  * **Export format:** YOLO format (.txt files with normalized coordinates)




**2\. Automated Annotation:**

  * Automatic annotation of remaining images using trained models

  * Generated âsilver standardâ annotations with potential errors

  * Models applied per-label-type initially, then across all labels for multi-label detection




**3\. Expert Validation:**

  * **Validators:** Two food science experts from the research team

  * **Task:** Review all automated annotations for accuracy

  * **Process:**

    * Verify presence of label logos in images

    * Correct false positives and false negatives

    * Validate bounding box accuracy

    * Confirm appropriate label class assignments

  * **Special cases handled:**

    * Images with secondary products visible in background

    * Partially visible or occluded labels

    * Multiple instances of the same label type

  * **Result:** Gold standard annotations




**Quality Assurance:**

  * Two independent expert validators

  * Complete review of all automated annotations

  * Iterative refinement through multi-stage validation

  * Systematic handling of edge cases and ambiguous instances




### FiftyOne Workflow Example#
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    # Load dataset
    dataset = fo.load_dataset("nutrigreen_dataset")
    
    # Explore dataset statistics
    print(dataset.stats(include_media=True))
    
    # Analyze label distribution
    label_counts = dataset.count_values("ground_truth.detections.label")
    print("Label distribution:", label_counts)
    
    # Find challenging samples (small objects)
    small_labels = dataset.filter_labels(
        "ground_truth",
        (F("bounding_box")[2] * F("bounding_box")[3]) < 0.01
    )
    
    # Create a view with only multi-label samples
    multi_label_view = dataset.match(
        F("ground_truth.detections").length() > 1
    )
    
    # Launch app for interactive exploration
    session = fo.launch_app(dataset)
    
    # Export to other formats if needed
    dataset.export(
        export_dir="/path/to/export",
        dataset_type=fo.types.COCODetectionDataset,
    )
    

## Citation#

**BibTeX:**
    
    
    @article{drole2024nutrigreen,
      title={NutriGreen image dataset: a collection of annotated nutrition, organic, and vegan food products},
      author={Drole, Jan and Pravst, Igor and Eftimov, Tome and KorouÅ¡i{\'c} Seljak, Barbara},
      journal={Frontiers in Nutrition},
      volume={11},
      pages={1342823},
      year={2024},
      publisher={Frontiers Media SA},
      doi={10.3389/fnut.2024.1342823}
    }
    
    @dataset{drole2023nutrigreen,
      author={Drole, Jan and Pravst, Igor and Eftimov, Tome and Seljak, Barbara KorouÅ¡iÄ},
      title={NutriGreen Image Dataset: A Collection of Annotated Nutrition, Organic, and Vegan Food Products},
      year={2023},
      publisher={Zenodo},
      version={1.0},
      doi={10.5281/zenodo.8374047},
      url={https://doi.org/10.5281/zenodo.8374047}
    }
    

**APA:**

Drole, J., Pravst, I., Eftimov, T., & KorouÅ¡iÄ Seljak, B. (2024). NutriGreen image dataset: a collection of annotated nutrition, organic, and vegan food products. _Frontiers in Nutrition_ , _11_ , 1342823. https://doi.org/10.3389/fnut.2024.1342823

Drole, J., Pravst, I., Eftimov, T., & Seljak, B. K. (2023). _NutriGreen Image Dataset: A Collection of Annotated Nutrition, Organic, and Vegan Food Products_ (Version 1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.8374047

## More Information#

### Related Resources#

**FiftyOne Resources:**

  * FiftyOne Documentation: https://docs.voxel51.com/

  * FiftyOne GitHub: https://github.com/voxel51/fiftyone

  * FiftyOne Dataset Zoo: https://docs.voxel51.com/user_guide/dataset_zoo/

  * FiftyOne Tutorials: https://docs.voxel51.com/tutorials/




**Data Source:**

  * Open Food Facts: https://world.openfoodfacts.org/

  * Open Food Facts API Documentation: https://openfoodfacts.github.io/api-documentation/




_FiftyOne format conversion and dataset card updates by the user community_

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
