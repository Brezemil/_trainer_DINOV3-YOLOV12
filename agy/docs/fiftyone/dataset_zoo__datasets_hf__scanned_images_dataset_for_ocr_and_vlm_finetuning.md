---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/scanned_images_dataset_for_ocr_and_vlm_finetuning.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/scanned-images-dataset-for-ocr-and-vlm-finetuning)

# Dataset Card for scanned_images_dataset#

![image/png](https://huggingface.co/datasets/Voxel51/scanned-images-dataset-for-ocr-and-vlm-finetuning/resolve/main/scanned_documents.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset containing **3,482 scanned document images** across 10 diverse document categories. Designed for OCR training and Vision-Language Model (VLM) fine-tuning, this dataset features real-world scanned documents with varied layouts, scanning quality, and document types.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/scanned-images-dataset-for-ocr-and-vlm-finetuning")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset is a curated collection of scanned document images representing 10 common document types found in office, academic, and professional settings. The images exhibit real-world characteristics including varied scanning quality, different layouts, mixed content types (text, tables, images), and both printed and handwritten text.

The dataset is particularly valuable for:

  * Training OCR models on diverse document layouts

  * Fine-tuning Vision-Language Models for document understanding

  * Developing document classification systems

  * Testing robustness to real-world scanning artifacts and quality variations

  * **Original Source:** [Kaggle - Scanned Images Dataset for OCR and VLM finetuning](https://www.kaggle.com/datasets/suvroo/scanned-images-dataset-for-ocr-and-vlm-finetuning)

  * **Curated by:** suvroo (original), Harpreet Sahota (FiftyOne port)

  * **Language(s):** English (primary), with potential multilingual content

  * **License:** Original license from Kaggle source




### Dataset Sources#

  * **Original Repository:** [Kaggle Dataset](https://www.kaggle.com/datasets/suvroo/scanned-images-dataset-for-ocr-and-vlm-finetuning)

  * **Dataset Download:** [GTS.AI Mirror](https://gts.ai/dataset-download/scanned-images-dataset-for-ocr-and-vlm-finetuning/)




## Uses#

### Direct Use#

This dataset is suitable for:

  * **OCR Model Training** : Train text extraction on real-world scanned documents with varied quality

  * **Document Classification** : Develop models to classify documents by type (email, memo, form, etc.)

  * **Vision-Language Model Fine-tuning** : Adapt VLMs for document understanding tasks

  * **Layout Analysis** : Detect and understand document structure (headers, paragraphs, tables)

  * **Document Quality Assessment** : Train models to handle various scanning qualities

  * **Multi-column Text Recognition** : Practice on complex layouts (news articles, scientific papers)

  * **Form Understanding** : Extract structured information from forms and tables

  * **Handwriting Recognition** : Some documents contain handwritten elements

  * **Real-world OCR Benchmarking** : Evaluate model performance on authentic scanned documents




### Out-of-Scope Use#

  * **Privacy-Sensitive Applications** : Documents may contain personally identifiable information

  * **Production Document Processing** : Without text annotations, this dataset is primarily for classification and pre-training

  * **Language-Specific OCR** : While primarily English, multilingual content may be present but not systematically labeled

  * **High-Precision Applications** : Scanning artifacts and quality variations may limit use in applications requiring perfect text extraction




## Dataset Structure#

### FiftyOne Schema#

Each sample in the dataset has the following structure:
    
    
    {
        'id': str,                      # Unique sample ID
        'media_type': 'image',          # Always 'image'
        'filepath': str,                # Absolute path to document image
        'tags': [],                     # Empty list (no tags)
        'metadata': {                   # Image metadata
            'size_bytes': int,          # File size (typically 200KB-800KB)
            'mime_type': 'image/jpeg',  # MIME type
            'width': int,               # Image width (varies, typically 1200-2500px)
            'height': int,              # Image height (varies, typically 1500-3200px)
            'num_channels': 1,          # Grayscale (1 channel)
        },
        'ground_truth': {               # Document classification label
            'id': str,                  # Label ID
            'tags': [],                 # Empty list
            'label': str,               # Document category (see below)
            'confidence': None,         # Not applicable
            'logits': None,             # Not applicable
        }
    }
    

### Document Categories#

The dataset contains 10 document categories with the following distribution:

Category | Count | Description  
---|---|---  
**Email** | 599 | Email correspondence and communications  
**Memo** | 620 | Internal memorandums and office notes  
**Letter** | 567 | Formal and informal letters  
**Form** | 431 | Forms, applications, and structured documents  
**Report** | 265 | Business and technical reports  
**Scientific** | 261 | Scientific papers and research documents  
**ADVE** (Advertisement) | 230 | Advertisements and promotional materials  
**Note** | 201 | Handwritten and typed notes  
**News** | 188 | News articles and clippings  
**Resume** | 120 | RÃ©sumÃ©s and CVs  
**Total** | **3,482** |   
  
### Image Characteristics#

  * **Format** : JPEG

  * **Color Mode** : Grayscale (1 channel)

  * **Resolution** : Varies (typically 72 DPI)

  * **Typical Dimensions** : 1200-2500 Ã 1500-3200 pixels

  * **File Size** : 200KB - 800KB per image

  * **Orientation** : Mostly portrait, some landscape




### Document Features#

The scanned documents exhibit:

  * **Multi-column layouts** (news articles, scientific papers)

  * **Tables and forms** with structured data

  * **Mixed content** (text, images, logos)

  * **Varied text styles** (printed, handwritten, typewritten)

  * **Real scanning artifacts** (skew, noise, shadows, folds)

  * **Different scanning qualities** (low to high resolution)

  * **Multiple fonts and sizes**

  * **Headers, footers, and page numbers**




## Dataset Creation#

### Curation Rationale#

This dataset was created to provide a diverse collection of real-world scanned documents for training and evaluating OCR systems and Vision-Language Models. The variety in document types, layouts, and scanning quality makes it valuable for developing robust document understanding systems that can handle real-world conditions.

### Source Data#

#### Data Collection and Processing#

The dataset consists of scanned images from various document types commonly found in professional and academic settings. Documents were scanned at varying quality levels to represent real-world scenarios.

This FiftyOne port was created by:

  1. Downloading the original dataset from Kaggle

  2. Organizing images into 10 category directories

  3. Using FiftyOneâs `ImageClassificationDirectoryTree` format to import with automatic label assignment

  4. Computing metadata for all images (dimensions, file size, color channels)




The directory structure maps directly to classification labels:
    
    
    scanned-images-dataset-for-ocr-and-vlm-finetuning/
     ADVE/          (230 images)
     Email/         (599 images)
     Form/          (431 images)
     Letter/        (567 images)
     Memo/          (620 images)
     News/          (188 images)
     Note/          (201 images)
     Report/        (265 images)
     Resume/        (120 images)
     Scientific/    (261 images)
    

#### Who are the source data producers?#

The documents appear to be collected from various sources representing typical office, business, and academic materials. Specific provenance information is not available from the original dataset.

### Annotations#

#### Annotation Process#

The dataset includes **document type classification labels** derived from the directory structure. Each image is labeled with one of 10 document categories based on its location in the folder hierarchy.

**No text-level annotations** (OCR transcriptions, bounding boxes, or entity labels) are included. The dataset is designed for:

  * Document classification tasks

  * Pre-training OCR and VLM models

  * Layout analysis research

  * Unsupervised or self-supervised learning




#### Personal and Sensitive Information#

**Privacy Warning** : This dataset contains scanned documents that may include:

  * Personal names and addresses

  * Email addresses and contact information

  * Company names and business information

  * Academic affiliations

  * Potentially sensitive correspondence




Users should:

  * Review documents before use in production systems

  * Implement appropriate privacy safeguards

  * Consider anonymization or redaction for sensitive applications

  * Comply with relevant privacy regulations (GDPR, CCPA, etc.)




## Bias, Risks, and Limitations#

### Known Limitations#

  * **No Text Annotations** : Dataset lacks OCR transcriptions, making it unsuitable for supervised text extraction training without additional annotation

  * **Language Bias** : Primarily English documents; limited representation of other languages

  * **Domain Coverage** : May not represent all document types (e.g., forms from specific industries)

  * **Quality Variation** : Scanning quality varies significantly, which could impact model training if not handled properly

  * **Imbalanced Categories** : Category sizes range from 120 (Resume) to 620 (Memo) samples

  * **Privacy Concerns** : Contains potentially identifiable information without systematic anonymization

  * **Temporal Bias** : Document styles and formats may reflect specific time periods

  * **Geographic Bias** : Document formats may be specific to certain regions




### Recommendations#

  * **Use for Classification or Pre-training** : Best suited for document type classification or unsupervised pre-training

  * **Combine with Annotated Datasets** : For OCR training, combine with datasets that include text annotations

  * **Privacy Review** : Audit documents for sensitive information before deployment

  * **Augment for Balance** : Apply data augmentation or resampling to address class imbalance

  * **Quality Filtering** : Consider filtering or stratifying by scan quality for specific applications

  * **Validate on Target Domain** : Test on your specific document types before production use

  * **Consider Licensing** : Verify usage rights for your specific application




## Citation#

If you use this dataset, please cite:

**Original Dataset:**
    
    
    @misc{scanned-images-ocr-vlm,
      author = {suvroo},
      title = {Scanned Images Dataset for OCR and VLM finetuning},
      year = {2024},
      publisher = {Kaggle},
      url = {https://www.kaggle.com/datasets/suvroo/scanned-images-dataset-for-ocr-and-vlm-finetuning}
    }
    

**FiftyOne Port:**
    
    
    @misc{scanned-images-ocr-vlm-fiftyone,
      author = {Harpreet Sahota},
      title = {Scanned Images Dataset for OCR and VLM finetuning (FiftyOne)},
      year = {2026},
      publisher = {Hugging Face},
      url = {https://huggingface.co/datasets/voxel51/scanned-images-dataset-for-ocr-and-vlm-finetuning}
    }
    

## Dataset Card Contact#

For questions or issues with this FiftyOne port, please open an issue on the Hugging Face dataset repository.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
