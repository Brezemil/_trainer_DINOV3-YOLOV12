---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/consolidated_receipt_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/consolidated_receipt_dataset)

# Dataset Card for Consolidated Receipt Dataset#

![image/png](https://huggingface.co/datasets/Voxel51/consolidated_receipt_dataset/resolve/main/cord_v1.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 800 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/consolidated_receipt_dataset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

CORD (Consolidated Receipt Dataset) is a large-scale dataset designed for post-OCR parsing tasks, specifically focused on receipt understanding. The dataset contains over 11,000 Indonesian receipts collected from shops and restaurants, featuring images with OCR annotations (bounding boxes and text) and multi-level semantic labels for parsing. This FiftyOne implementation provides an accessible interface for exploring the training split with 800 annotated receipt images.

The dataset bridges the gap between OCR and NLP tasks by providing both visual and semantic annotations, making it suitable for end-to-end document intelligence systems. Each receipt includes detailed annotations with 30 semantic classes organized into 5 superclasses (menu, void_menu, subtotal, void_total, and total), along with metadata including line grouping, regions of interest, and key-value pair flags.

  * **Curated by:** NAVER CLOVA AI Research (Seunghyun Park, Seung Shin, Bado Lee, Junyeop Lee, Jaeheung Surh, Minjoon Seo, Hwalsuk Lee)

  * **Funded by:** NAVER Corporation

  * **Shared by:** NAVER CLOVA AI via Hugging Face Datasets

  * **Language(s) (NLP):** Indonesian (id)

  * **License:** CC-BY-4.0 (Creative Commons Attribution 4.0 International License)




### Dataset Sources#

  * **Repository:** https://github.com/clovaai/cord

  * **Hugging Face:** https://huggingface.co/datasets/naver-clova-ix/cord-v1

  * **Paper:** Park et al. (2019) âCORD: A Consolidated Receipt Dataset for Post-OCR Parsingâ - Document Intelligence Workshop at NeurIPS 2019

  * **Related Paper:** Hwang et al. (2019) âPost-OCR parsing: building simple and robust parser via BIO taggingâ - Document Intelligence Workshop at NeurIPS 2019




## Uses#

### Direct Use#

This FiftyOne dataset is suitable for:

  * **Document understanding research** : Training and evaluating models for receipt parsing and information extraction

  * **OCR post-processing** : Developing systems that parse structured information from OCR outputs

  * **Key-value extraction** : Building models to identify and extract key information (prices, items, totals) from receipts

  * **Visual document analysis** : Training vision-language models for document understanding tasks

  * **Multi-modal learning** : Combining visual features (bounding boxes) with text for improved parsing

  * **Benchmark evaluation** : Comparing different approaches to document intelligence on standardized data




The FiftyOne format enables interactive exploration, filtering by categories, visualization of bounding boxes with text annotations, and easy integration with computer vision and ML workflows.

### Out-of-Scope Use#

  * **Real-time production OCR** : The dataset assumes OCR has already been performed; it does not include raw pre-OCR data

  * **Multi-language receipt parsing** : Dataset contains only Indonesian receipts; performance on other languages/scripts is not guaranteed

  * **Privacy-sensitive applications** : While receipts were collected ethically, the dataset should not be used for identifying individuals or businesses

  * **Commercial transaction analysis** : Store and payment information have been removed due to legal requirements

  * **General document understanding** : The dataset is specifically designed for receipts; may not generalize to other document types




## Dataset Structure#

### FiftyOne Dataset Schema#

The dataset is organized with the following structure:

**Sample-level fields:**

  * `filepath`: Path to the saved receipt image (PNG format, average size 864Ã1296 pixels)

  * `image_id`: Unique identifier for each receipt (0-799 for training split)

  * `width`: Image width in pixels

  * `height`: Image height in pixels

  * `num_items`: Count of menu items on the receipt (integer, typically 1-30)

  * `subtotal_price`: Subtotal amount before tax/service (string with comma separators, e.g., â1,346,000â)

  * `service_price`: Service charge amount (string, can be None)

  * `tax_price`: Tax amount (string, can be None)

  * `etc`: Additional charges or rounding adjustments (string, can be None or negative)

  * `total_price`: Final total price (string with comma separators, e.g., â1,591,600â)




**Detection fields (` detections`):** Each sample contains a `Detections` object with bounding boxes for individual text elements:

  * `label`: Semantic category from 30 classes (e.g., âmenu.nmâ, âmenu.priceâ, âmenu.cntâ, âsub_total.subtotal_priceâ, âtotal.total_priceâ)

  * `bounding_box`: Normalized coordinates [x, y, width, height] in range [0, 1]

  * `text`: OCR text content for that bounding box

  * `is_key`: Boolean flag indicating if the text is a key (True) or value (False)

  * `group_id`: Integer linking related text elements together (e.g., all fields for one menu item)




**Semantic Categories (30 classes):**

  1. **Menu items (14 subclasses)** : menu.nm, menu.cnt, menu.unitprice, menu.price, menu.sub_nm, menu.sub_price, etc.

  2. **Void menu (2 subclasses)** : void_menu.nm, void_menu.price

  3. **Subtotal (6 subclasses)** : subtotal.subtotal_price, subtotal.service_price, subtotal.tax_price, subtotal.discount_price, subtotal.othersvc_price, subtotal.etc

  4. **Total (8 subclasses)** : total.total_price, total.cashprice, total.changeprice, total.creditcardprice, total.emoneyprice, total.menutype_cnt, total.menuqty_cnt, total.total_etc




### Data Splits#

  * **Training set** : 800 samples (implemented in this FiftyOne dataset)

  * **Development set** : 100 samples (available in original dataset)

  * **Test set** : 100 samples (available in original dataset)




## Dataset Creation#

### Curation Rationale#

The CORD dataset was created to address the gap between OCR and semantic parsing tasks in document intelligence. While OCR and parsing have traditionally been studied separately, real-world applications require integrated post-OCR parsing systems. Receipts were chosen as the document type because:

  1. They have complex hierarchical structure requiring multi-level semantic understanding

  2. They contain both key-value pairs and tabular information

  3. They represent a common real-world use case for document intelligence

  4. They require handling of various text alignments, fonts, and layouts




The dataset aims to advance research in unified OCR-NLP systems by providing fine-grained annotations that connect visual features (bounding boxes) with semantic labels and hierarchical groupings.

### Source Data#

#### Data Collection and Processing#

The dataset consists of 11,000+ Indonesian receipts collected from shops and restaurants. For the publicly released version (v1), 1,000 receipts were selected and annotated with:

  * OCR bounding boxes (quadrilateral coordinates)

  * Text transcriptions for each bounding box

  * Semantic labels (30 classes across 5 superclasses)

  * Line grouping information (`row_id`)

  * Group identifiers linking related text elements

  * Key-value flags (`is_key`)

  * Region of interest annotations

  * Additional metadata (repeating symbols, cut lines)




Note: Certain sensitive information categories (`store_info`, `payment_info`, and some `etc` fields) were removed from the public dataset due to Indonesian privacy regulations.

#### Who are the source data producers?#

The source data was collected from real Indonesian retail businesses (shops and restaurants). The images represent actual printed or digital receipts from commercial transactions. Annotation was performed by NAVER CLOVA AI research team with quality control processes to ensure consistency.

### Annotations#

#### Annotation process#

The annotation process involved:

  1. **Image collection** : Gathering receipt images from Indonesian businesses

  2. **OCR annotation** : Manual verification and correction of bounding boxes and text

  3. **Semantic labeling** : Assigning categories from the 30-class taxonomy

  4. **Hierarchical grouping** : Linking related elements via `group_id` and `row_id`

  5. **Key-value flagging** : Identifying whether text serves as key or value

  6. **Quality control** : Multiple passes to ensure consistency and correctness




The dataset uses quadrilateral (quad) bounding boxes to accurately capture rotated or skewed text. For the FiftyOne implementation, these are converted to axis-aligned bounding boxes using min/max coordinates.

#### Who are the annotators?#

Annotations were created by the NAVER CLOVA AI research team with domain expertise in document understanding and OCR systems.

#### Personal and Sensitive Information#

The dataset has undergone anonymization to remove sensitive information:

  * Store names and contact information have been removed

  * Payment card details have been excluded

  * Personal customer information is not present

  * The `store_info` and `payment_info` categories were completely removed from the public release




The dataset contains only transaction-level information (menu items, prices, totals) without identifying information about businesses or customers.

## Bias, Risks, and Limitations#

**Technical Limitations:**

  * **Language specificity** : Dataset contains only Indonesian text; models trained on this data may not transfer well to other languages

  * **Domain specificity** : Limited to retail receipts; may not generalize to other document types (invoices, forms, etc.)

  * **OCR dependency** : Assumes accurate OCR; the dataset does not address OCR errors or poor image quality

  * **Data structure inconsistency** : Some samples have `sub_total` and `total` as lists rather than dictionaries, requiring defensive parsing




**Sociotechnical Limitations:**

  * **Geographic bias** : All receipts are from Indonesia; layout conventions, pricing formats, and language may not represent global diversity

  * **Business type bias** : Limited to shops and restaurants; may not represent receipts from other sectors

  * **Temporal bias** : Dataset collected in 2019; may not reflect current receipt formats or digital payment systems

  * **Format bias** : Physical and digital receipt formats may have evolved since collection




**Risks:**

  * Models trained on this data should not be used to identify specific businesses or individuals

  * The dataset should not be assumed to work for privacy-sensitive commercial applications without additional validation

  * Price format conventions (comma separators for thousands) are specific to Indonesian formatting




### Recommendations#

Users should:

  * Be aware of the Indonesian-language specificity when applying models to other languages

  * Validate performance on their specific receipt types before production deployment

  * Implement additional privacy safeguards if handling real customer data

  * Consider the temporal gap (2019 collection date) when working with modern receipt formats

  * Handle data structure inconsistencies (list vs. dict for `sub_total`/`total` fields) in their parsing code

  * Not assume the dataset represents all receipt types or global formatting conventions




## Citation#

**BibTeX:**
    
    
    @article{park2019cord,
      title={CORD: A Consolidated Receipt Dataset for Post-OCR Parsing},
      author={Park, Seunghyun and Shin, Seung and Lee, Bado and Lee, Junyeop and Surh, Jaeheung and Seo, Minjoon and Lee, Hwalsuk},
      booktitle={Document Intelligence Workshop at Neural Information Processing Systems},
      year={2019}
    }
    
    @article{hwang2019post,
      title={Post-OCR parsing: building simple and robust parser via BIO tagging},
      author={Hwang, Wonseok and Kim, Seonghyeon and Yim, Jinyeong and Seo, Minjoon and Park, Seunghyun and Park, Sungrae and Lee, Junyeop and Lee, Bado and Lee, Hwalsuk},
      booktitle={Document Intelligence Workshop at Neural Information Processing Systems},
      year={2019}
    }
    

**APA:**

Park, S., Shin, S., Lee, B., Lee, J., Surh, J., Seo, M., & Lee, H. (2019). CORD: A Consolidated Receipt Dataset for Post-OCR Parsing. In Document Intelligence Workshop at Neural Information Processing Systems.

## More Information#

For additional information:

  * Original dataset repository: https://github.com/clovaai/cord

  * Hugging Face dataset: https://huggingface.co/datasets/naver-clova-ix/cord-v1

  * CORD v2 (with corrections and sub_group_id): https://huggingface.co/datasets/naver-clova-ix/cord-v2

  * Related work: Donut (OCR-free Document Understanding Transformer) also uses CORD for evaluation




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
