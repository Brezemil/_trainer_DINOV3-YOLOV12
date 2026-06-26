---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/form_understanding_in_noisy_scanned_documents_plus.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/form_understanding_in_noisy_scanned_documents_plus)

# Dataset Card for Form Understanding in Noisy Scanned Documents Plus#

![image/png](https://huggingface.co/datasets/Voxel51/form_understanding_in_noisy_scanned_documents_plus/resolve/main/funds_plus.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1026 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/form_understanding_in_noisy_scanned_documents_plus")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

FUNSD+ (Form Understanding in Noisy Scanned Documents Plus) is an enhanced version of the original FUNSD dataset designed for form understanding tasks. The dataset provides ground truth data for extracting structured information from scanned forms, including entity recognition and relationship extraction between form fields and their values.

FUNSD+ addresses inconsistencies in labeling found in the original FUNSD dataset and significantly expands the document count from 199 to 1,113 documents. The dataset contains annotations for headers, questions (field labels), answers (field values), and their relationships, making it suitable for training and evaluating models for key-value extraction, document layout analysis, and form understanding tasks.

Each sample includes:

  * Scanned form images

  * Word-level OCR tokens with bounding boxes

  * Entity labels (header, question, answer, other)

  * Grouped words forming semantic units

  * Linked groups showing relationships between questions and answers

  * **Curated by:** Konfuzio (Helm & Nagel GmbH)

  * **Shared by [optional]:** Konfuzio via Hugging Face

  * **Language(s) (NLP):** English (`en`)

  * **License:** [FUNSD+ Custom License](https://huggingface.co/datasets/konfuzio/funsd_plus/blob/main/LICENSE)




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/konfuzio/funsd_plus

  * **Homepage:** https://konfuzio.com/en/funsd-plus/

  * **Paper:**

    * Original FUNSD: [FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents](https://arxiv.org/abs/1905.13538) (Jaume et al., 2019)

    * Related: [Going Full-TILT Boogie on Document Understanding with Text-Image-Layout Transformer](https://arxiv.org/abs/2010.05322) (Vu and Nguyen, 2020)

  * **Demo:** https://app.konfuzio.com/d/303962/




## Uses#

### Direct Use#

The FUNSD+ dataset is intended for:

  1. **Form Understanding** : Training and evaluating models for extracting structured information from scanned forms

  2. **Key-Value Extraction** : Identifying relationships between field labels (questions) and their corresponding values (answers)

  3. **Document Layout Analysis** : Understanding spatial and semantic layout of form documents

  4. **Named Entity Recognition** : Detecting and classifying text entities in documents (headers, questions, answers)

  5. **OCR Post-Processing** : Improving OCR results by understanding document structure

  6. **Multi-modal Document Understanding** : Combining visual (layout) and textual information for document comprehension

  7. **Benchmarking** : Comparing performance of document AI models on a standardized dataset




The dataset can be used directly for training transformer-based models like LayoutLM, LayoutLMv2, LayoutLMv3, BERT-based models, and other architectures designed for document understanding.

### Out-of-Scope Use#

  * **Non-English Documents** : The dataset contains only English-language forms and may not generalize well to other languages

  * **Modern Digital Forms** : Optimized for scanned/noisy documents rather than born-digital forms

  * **Handwritten Forms** : The dataset focuses on printed/typed text, not handwriting recognition

  * **Privacy-Sensitive Applications** : Users must not attempt to identify individuals in the dataset (per license terms)

  * **Unstructured Documents** : Not suitable for documents without form-like structure (e.g., essays, articles, books)




## Dataset Structure#

The dataset contains the following fields for each sample:

  * **`image`** (PIL Image): Scanned form image in PNG format

    * Typical size: ~1000x1000 to ~1400x1400 pixels

    * Format: RGB or grayscale

  * **`words`** (list of strings): OCR-extracted text tokens

    * Length: Variable (typically 50-300 words per document)

    * Contains individual words/tokens from the form

  * **`bboxes`** (list of lists): Bounding boxes for each word

    * Format: `[x_min, y_min, x_max, y_max]` in absolute pixel coordinates

    * Coordinates correspond to word positions in the image

  * **`labels`** (list of integers): Entity type labels for each word

    * `0`: Other (non-semantic text)

    * `1`: Header (document titles, form names)

    * `2`: Question (field labels, prompts)

    * `3`: Answer (field values, responses)

  * **`grouped_words`** (list of lists): Indices grouping words into semantic units

    * Groups related words that form complete entities

    * Example: `[[0, 1, 2], [3], [4, 5]]` groups words 0-1-2 together, word 3 alone, words 4-5 together

  * **`linked_groups`** (list of lists): Indices showing relationships between word groups

    * Represents question-answer pairs and other semantic relationships

    * Example: `[[0, 1]]` links group 0 (question) to group 1 (answer)




### Dataset Splits#

Split | Number of Samples | Size (MB)  
---|---|---  
Train | 1,026 | ~183  
Test | 113 | ~21  
**Total** | **1,139** | **~204**  
  
### Comparison with Original FUNSD#

| FUNSD | FUNSD+  
---|---|---  
Documents | 199 | 1,113  
Headers | 563 | 1,604  
Questions | 4,343 | 14,695  
Answers | 3,623 | 12,154  
Questions with no answers | 720 (16.6%) | 2,691 (18.3%)  
Answers without questions | 0 | 114 (0.9%)  
  
## Dataset Creation#

### Curation Rationale#

The FUNSD+ dataset was created to address several limitations in the original FUNSD dataset:

  1. **Scale** : Expand from 199 to 1,113 documents to provide more training data for deep learning models

  2. **Annotation Quality** : Fix inconsistencies in labeling found in the original FUNSD dataset

  3. **Key-Value Extraction** : Improve the datasetâs effectiveness for training models to extract question-answer pairs from forms

  4. **Robustness** : Provide more diverse examples of form layouts and structures

  5. **Benchmarking** : Create a more comprehensive benchmark for evaluating form understanding models




### Source Data#

#### Data Collection and Processing#

The dataset consists of scanned business forms and documents. Based on the original FUNSD methodology:

  * Forms were scanned at various resolutions and quality levels to simulate real-world noisy documents

  * OCR was performed to extract text and bounding boxes

  * Images were processed to standard formats (PNG)

  * Annotations were created for entity types and relationships




#### Who are the source data producers?#

The source data consists of business forms and documents. The original FUNSD dataset was created by Guillaume Jaume et al. FUNSD+ was curated and expanded by Konfuzio (Helm & Nagel GmbH), specifically by Davide Zagami and Christopher Helm.

### Annotations#

The dataset includes human-annotated labels for:

  * Entity types (header, question, answer, other)

  * Word groupings into semantic units

  * Relationships between entities (question-answer pairs)




#### Annotation process#

Following the original FUNSD annotation guidelines, annotators labeled:

  1. Individual words with entity type labels

  2. Semantic groupings of words

  3. Relationships between questions and answers




FUNSD+ includes revised annotations that fix inconsistencies from the original FUNSD dataset, particularly improving the accuracy of key-value pair annotations.

[More Information Needed for specific annotation tools, guidelines, inter-annotator agreement, etc.]

#### Who are the annotators?#

Annotations were performed by Konfuzio team members and potentially external annotators. [More Information Needed for specific annotator demographics and qualifications]

#### Personal and Sensitive Information#

Per the dataset license, users agree to not attempt to determine the identity of individuals in this dataset. The forms may contain business information, but efforts have been made to use non-sensitive documents. Users should be aware that some forms may contain names, addresses, or other potentially identifying information and should handle the data accordingly.

## Bias, Risks, and Limitations#

**Technical Limitations:**

  * **Language** : English-only; may not generalize to other languages

  * **Domain** : Business forms; may not transfer well to other document types

  * **OCR Quality** : Pre-extracted OCR may contain errors

  * **Annotation Inconsistencies** : While improved over FUNSD, some annotation inconsistencies may remain (18.3% of questions have no answers)




**Biases:**

  * **Geographic Bias** : Forms may predominantly reflect US/Western business practices

  * **Temporal Bias** : Forms reflect document styles from specific time periods

  * **Domain Bias** : Limited to business forms; not representative of all document types




**Risks:**

  * Models trained on this dataset may not perform well on documents with significantly different layouts or languages

  * The dataset size, while larger than FUNSD, may still be limiting for some deep learning approaches

  * Presence of potentially identifying information requires careful handling




### Recommendations#

Users should:

  * Be aware that models trained on FUNSD+ may not generalize to non-form documents or non-English text

  * Consider the dataset size limitations when training large models

  * Comply with the license terms, particularly regarding not attempting to identify individuals

  * Evaluate models on domain-specific test sets if deploying to production

  * Be cautious about annotation quality, particularly for edge cases (questions without answers, etc.)

  * Consider data augmentation to improve model robustness




## Citation#

**BibTeX:**
    
    
    @misc{zagami_helm_2022,
      title = {FUNSD+: A larger and revised FUNSD dataset},
      author = {Zagami, Davide and Helm, Christopher},
      year = {2022},
      month = {Oct},
      journal = {FUNSD+ | A larger and revised FUNSD dataset},
      publisher = {Helm & Nagel GmbH},
      url = {https://konfuzio.com/funsd-plus/}
    }
    
    @inproceedings{jaume2019funsd,
      title={FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents},
      author={Jaume, Guillaume and Ekenel, Hazim Kemal and Thiran, Jean-Philippe},
      booktitle={2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)},
      volume={2},
      pages={1--6},
      year={2019},
      organization={IEEE}
    }
    

**APA:**

Zagami, D., & Helm, C. (2022, October 18). _FUNSD+: A larger and revised FUNSD dataset_. Helm & Nagel GmbH. https://konfuzio.com/funsd-plus/

Jaume, G., Ekenel, H. K., & Thiran, J. P. (2019). FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents. In _2019 International Conference on Document Analysis and Recognition Workshops (ICDARW)_ (Vol. 2, pp. 1-6). IEEE.

## More Information#

  * **Konfuzio Homepage** : https://konfuzio.com/

  * **Konfuzio Python SDK** : https://github.com/konfuzio-ai/konfuzio-sdk

  * **Interactive Demo** : https://app.konfuzio.com/d/303962/

  * **Original FUNSD Dataset** : https://guillaumejaume.github.io/FUNSD/

  * **Visual Example** : ![FUNSD+ Preview](https://konfuzio.com/wp-content/uploads/2022/10/image-3-1536x819.png)




## Dataset Card Contact#

  * **Konfuzio Contact** : https://konfuzio.com/en/contact/

  * **Dataset Issues** : https://huggingface.co/datasets/konfuzio/funsd_plus/discussions




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
