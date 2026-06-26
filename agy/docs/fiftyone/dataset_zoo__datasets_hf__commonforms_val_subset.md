---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/commonforms_val_subset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/commonforms_val_subset)

# Dataset Card for CommonForms_val#

![image/png](https://huggingface.co/datasets/Voxel51/commonforms_val_subset/resolve/main/commonforms_val.gif)

CommonForms_val is a validation subset of the CommonForms dataset for form field detection. It contains 10,000 annotated document images with bounding boxes for three types of form fields: text inputs, choice buttons (checkboxes/radio buttons), and signature fields. This dataset is designed for training and evaluating object detection models on the task of automatically detecting fillable form fields in document images.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 10,000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/commonforms_val_subset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

CommonForms_val is a validation subset extracted from the CommonForms dataset, a web-scale dataset for form field detection introduced in the paper âCommonForms: A Large, Diverse Dataset for Form Field Detectionâ (Barrow, 2025). The dataset frames form field detection as an object detection problem: given an image of a document page, predict the location and type of form fields.

The full CommonForms dataset was constructed by filtering Common Crawl to find PDFs with fillable elements, starting with 8 million documents and arriving at ~55,000 documents with over 450,000 pages. This validation subset contains 2,500 pages with 34,643 annotated form field instances across diverse languages and domains.

Key characteristics:

  * **Multilingual** : Approximately one-third of pages are non-English

  * **Multi-domain** : 14 classified domains, with no single domain exceeding 25% of the dataset

  * **High-quality annotations** : Automatically extracted from interactive PDF forms with fillable fields

  * **Three form field types** : Text inputs (68.9%), choice buttons (30.7%), and signature fields (0.4%)

  * **Curated by:** Joe Barrow (Independent Researcher)

  * **Funded by:** LambdaLabs (compute grant for model training)

  * **Shared by:** Joe Barrow

  * **Language(s) (NLP):** Multilingual (en, and ~33% non-English including various European and other languages)

  * **License:** [Check original repository - https://huggingface.co/datasets/jbarrow/CommonForms]




### Dataset Sources [optional]#

  * **Repository:** https://github.com/jbarrow/commonforms

  * **Paper:** https://arxiv.org/abs/2509.16506

  * **Demo:** https://detect.semanticdocs.org

  * **Original Dataset:** https://huggingface.co/datasets/jbarrow/CommonForms




## Uses#

### Direct Use#

This dataset is intended for:

  1. **Training and evaluating object detection models** for form field detection in document images

  2. **Benchmarking form field detection systems** against the validation set

  3. **Research in document understanding** and intelligent document processing

  4. **Developing automated form preparation tools** that can convert static PDFs into fillable forms

  5. **Computer vision research** on high-resolution document analysis

  6. **Multi-class object detection** with imbalanced classes (signature fields are rare)




The dataset is particularly useful for:

  * Training YOLO, Faster R-CNN, or other object detection architectures

  * Fine-tuning vision transformers for document understanding

  * Evaluating model performance across different form field types

  * Studying the impact of high-resolution inputs on detection quality




### Out-of-Scope Use#

This dataset should **not** be used for:

  1. **OCR or text recognition tasks** \- The dataset only contains bounding boxes for form fields, not text content

  2. **Form understanding or semantic analysis** \- No information about field labels, relationships, or form structure

  3. **Handwriting detection** \- Only detects empty form fields, not filled content

  4. **Privacy-sensitive applications without review** \- Forms may contain templates with sensitive field types (medical, financial, etc.)

  5. **Production deployment without validation** \- This is a validation subset; models should be tested on appropriate test sets

  6. **Fine-grained form field classification** \- Only three broad categories are available (text, choice, signature)




## Dataset Structure#

### FiftyOne Dataset Structure#

This dataset is stored in FiftyOne format, which provides a powerful structure for computer vision datasets:

**Sample-level fields:**

  * `filepath` (string): Path to the document image file

  * `image_id` (int): Unique identifier for the image from the original dataset

  * `file_name` (string): Original filename (e.g., â0001104-0.pngâ)

  * `dataset_id` (int): Sample ID in the original dataset

  * `ground_truth` (Detections): FiftyOne Detections object containing all form field annotations




**Detection-level fields (within` ground_truth`):**

  * `label` (string): Form field type - one of:

    * `text_input`: Text boxes and input fields (68.9% of annotations)

    * `choice_button`: Checkboxes and radio buttons (30.7% of annotations)

    * `signature`: Signature fields (0.4% of annotations)

  * `bounding_box` (list): Normalized coordinates [x, y, width, height] in range [0, 1]

    * Format: [top-left-x, top-left-y, width, height] relative to image dimensions

  * `area` (float): Area of the bounding box in absolute pixels

  * `iscrowd` (bool): COCO-style crowd flag (always False in this dataset)

  * `object_id` (int): Unique identifier for the annotation

  * `category_id` (int): Numeric category (0=text_input, 1=choice_button, 2=signature)




### Image Specifications#

  * **Image dimensions:** Variable, ranging from 1680Ã1680 to 3360Ã3528 pixels

  * **Mean dimensions:** 1748Ã2201 pixels

  * **Format:** RGB PNG images

  * **Resolution:** High-resolution document scans optimized for form field detection

  * **Unique dimensions:** 61 different image size combinations




### Annotation Format#

Annotations follow COCO object detection format converted to FiftyOne:

  * **Original format:** COCO [x, y, width, height] in absolute pixel coordinates

  * **FiftyOne format:** Normalized [x, y, width, height] in relative coordinates [0, 1]

  * **Bounding box validation:** Invalid boxes (negative dimensions, out-of-bounds) are filtered during conversion




## Dataset Creation#

### Curation Rationale#

The CommonForms dataset was created to address the lack of large-scale, publicly available datasets for form field detection. Existing commercial solutions (Adobe Acrobat, Apple Preview) have limitations:

  * They cannot detect choice buttons (checkboxes/radio buttons)

  * They are closed-source and not reproducible

  * No public benchmarks exist for comparison




The key insight is that âquantity has a quality all its ownâ - by leveraging existing fillable PDF forms from Common Crawl as a training signal, high-quality form field detection can be achieved without manual annotation. This validation subset enables:

  1. **Reproducible benchmarking** of form field detection systems

  2. **Open-source model development** for automated form preparation

  3. **Research advancement** in document understanding and intelligent document processing

  4. **Cost-effective training** \- models trained on this data cost less than $500 in compute




### Source Data#

#### Data Collection and Processing#

**Source:** Common Crawl PDF corpus (~8 million PDFs) prepared by the PDF Association

**Filtering Process:**

  1. Started with 8 million PDF documents from Common Crawl

  2. Applied rigorous cleaning to identify well-prepared forms with fillable elements

  3. Filtered to PDFs containing interactive form fields (text boxes, checkboxes, signature fields)

  4. Quality filtering to ensure form fields were properly annotated in the source PDFs

  5. Final dataset: ~55,000 documents with 450,000+ pages




**Processing Steps:**

  1. PDF rendering to high-resolution images (optimized for form field detection)

  2. Extraction of form field annotations from PDF metadata

  3. Conversion to COCO object detection format

  4. Train/validation/test split creation

  5. This subset represents the validation split




**Quality Assurance:**

  * Ablation studies showed the cleaning process improves data efficiency vs. using all PDFs

  * Annotations are automatically extracted from interactive PDF forms (no manual annotation)

  * High-resolution inputs (1216px+) were found crucial for quality detection




**Data Characteristics:**

  * **Multilingual:** ~33% non-English pages

  * **Multi-domain:** 14 domains classified, no domain exceeds 25%

  * **Diverse layouts:** Wide variety of form designs and structures

  * **Real-world forms:** Government forms, applications, surveys, contracts, etc.




#### Who are the source data producers?#

The source data consists of PDF forms published on the public web and crawled by Common Crawl. The original form creators include:

  * **Government agencies** (federal, state, local)

  * **Educational institutions**

  * **Healthcare organizations**

  * **Financial institutions**

  * **Legal services**

  * **Corporate entities**

  * **Non-profit organizations**




The forms were created by professional document designers, administrative staff, and organizations worldwide. The diversity of sources contributes to the datasetâs robustness across different form styles, languages, and domains.

**Note:** The forms are templates (unfilled) extracted from publicly available PDFs on the internet.

### Annotations#

#### Annotation process#

**Automatic Annotation from PDF Metadata:**

The annotations in this dataset are **automatically extracted** from interactive PDF forms, not manually annotated. The process:

  1. **Source:** PDF form field metadata embedded in interactive PDFs

  2. **Extraction:** Form field locations and types are programmatically extracted from PDF structure

  3. **Mapping:** PDF form field types are mapped to three detection categories:

     * PDF text fields â `text_input`

     * PDF checkbox/radio button fields â `choice_button`

     * PDF signature fields â `signature`

  4. **Coordinate conversion:** PDF coordinates converted to image pixel coordinates

  5. **Format standardization:** Converted to COCO object detection format




**Advantages:**

  * **Scale:** Enables annotation of 450k+ pages without manual labor

  * **Consistency:** Annotations are objective and derived from PDF structure

  * **Cost:** No annotation costs

  * **Quality:** Reflects real-world form field placement by professional designers




**Limitations:**

  * Annotation quality depends on source PDF quality

  * Some PDFs may have incorrectly defined form fields

  * Only detects explicitly defined form fields (not visual-only fields)




#### Who are the annotators?#

The annotations are **automatically generated** from PDF metadata - there are no human annotators. The âannotatorsâ are effectively the original form designers who created the interactive PDF forms with fillable fields.

The dataset curation and extraction pipeline was developed by Joe Barrow (Independent Researcher).

## Citation#

**BibTeX:**
    
    
    @misc{barrow2025commonforms,
      title = {CommonForms: A Large, Diverse Dataset for Form Field Detection},
      author = {Barrow, Joe},
      year = {2025},
      eprint = {2509.16506},
      archivePrefix = {arXiv},
      primaryClass = {cs.CV},
      doi = {10.48550/arXiv.2509.16506},
      url = {https://arxiv.org/abs/2509.16506}
    }
    

**APA:**

Barrow, J. (2025). CommonForms: A Large, Diverse Dataset for Form Field Detection. _arXiv preprint arXiv:2509.16506_. https://doi.org/10.48550/arXiv.2509.16506

## More Information#

### Related Resources#

  * **GitHub Repository:** https://github.com/jbarrow/commonforms

  * **Hosted Demo:** https://detect.semanticdocs.org

  * **Models:**

    * FFDNet-S: https://huggingface.co/jbarrow/FFDNet-S

    * FFDNet-L: https://huggingface.co/jbarrow/FFDNet-L

  * **Full Dataset:** https://huggingface.co/datasets/jbarrow/CommonForms (486,969 samples)




### Use Cases in the Wild#

The CommonForms models and dataset enable:

  * Automated PDF form preparation

  * Document digitization workflows

  * Accessibility improvements for forms

  * Form field extraction for document understanding systems




## Dataset Card Authors#

  * **Primary Author:** Harpreet Sahota (FiftyOne dataset curation)

  * **Original Dataset:** Joe Barrow (joseph.d.barrow@gmail.com)

  * **Dataset Card Completion:** AI-assisted with human review




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
