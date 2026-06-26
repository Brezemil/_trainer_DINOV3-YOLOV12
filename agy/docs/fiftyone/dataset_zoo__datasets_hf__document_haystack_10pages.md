---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/document_haystack_10pages.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/document-haystack-10pages)

# Dataset Card for document-haystack-10pages#

![image/png](https://huggingface.co/datasets/Voxel51/document-haystack-10pages/resolve/main/document_haystacks_fo.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 250 samples. Itâs the 10-page subset of the [full dataset](https://huggingface.co/datasets/AmazonScience/document-haystack).

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/document-haystack-10pages")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Document Haystack is a comprehensive benchmark designed to evaluate the performance of Vision Language Models (VLMs) on long, visually complex documents. This FiftyOne dataset contains the 10-page subset, which serves as an entry point for testing retrieval capabilities on shorter documents.

The benchmark expands on the âNeedle in a Haystackâ concept by embedding needles â short key-value statements in pure text or as multimodal text+image snippets â within real-world documents. These needles test whether models can locate specific information hidden within complex documents with textual, visual, or mixed content.

**Key Features:**

  * 25 real-world base documents (annual reports, financial filings, etc.)

  * 10 pages per document variant

  * 10 needles per document (strategically placed across pages)

  * Two needle types: text-only and text+image

  * 250 total samples (125 per needle type)

  * 250 retrieval questions

  * **Curated by:** Amazon AGI (Goeric Huybrechts, Srikanth Ronanki, Sai Muralidhar Jayanthi, Jack Fitzgerald, Srinivasan Veeravanallur)

  * **Language:** English

  * **License:** CC-BY-NC-4.0




### Dataset Sources#

  * **Original Repository:** https://github.com/amazon-science/document-haystack

  * **Original Dataset:** https://huggingface.co/datasets/AmazonScience/document-haystack

  * **Paper:** [Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark](https://arxiv.org/abs/2507.15882)




## Dataset Structure#

### FiftyOne Schema#

Each sample in this FiftyOne dataset represents a single page image with the following fields:

#### Sample-Level Fields#

Field | Type | Description  
---|---|---  
`filepath` | string | Path to the page image (JPG, 200 DPI)  
`document_name` | Classification | Name of the source document (e.g., âAIGâ, âAmericanAirlinesâ)  
`page_number` | int | Page number within the document (1-5)  
`needle_type` | Classification | Type of needles: âtextâ or âtext_imageâ  
  
#### Needle Information Fields#

These fields contain lists of information about needles on each page:

Field | Type | Description  
---|---|---  
`needle_texts` | list[string] | Full needle statements (e.g., âThe secret currency is a âeuroâ.â)  
`needle_keys` | Classifications | Extracted keys (e.g., âcurrencyâ, âsportâ)  
`needle_answers` | Classifications | Extracted answers (e.g., âeuroâ, âbasketballâ)  
`needle_questions` | list[string] | Questions for retrieving each needle  
`needle_font_sizes` | list[int] | Font sizes of needles  
`needle_text_colors` | list[string] | Text colors  
`needle_bg_colors` | list[string] | Background colors  
`needle_fonts` | list[string] | Font families  
`needle_scales` | list[int] | Scale values (for text+image needles)  
`needle_locations` | Keypoints | Spatial locations of needles with (x, y) coordinates in [0, 1]  
  
### Needle Categories#

Needles span diverse categories including:

  * Sports

  * Animals

  * Currencies

  * Fruits

  * Musical instruments

  * Office supplies

  * Flowers

  * Landmarks

  * And moreâ¦




### Needle Format#

Each needle follows the pattern: **âThe secret KEY is VALUE.â**

  * **Text needles:** Both KEY and VALUE are text (e.g., âThe secret sport is basketball.â)

  * **Text+Image needles:** VALUE is shown as an image (e.g., âThe secret sport is [image of basketball]â)




Questions follow the pattern: **âWhat is the secret KEY in the document?â**

## Uses#

### Direct Use#

This dataset is designed for:

  1. **Evaluating VLM retrieval capabilities** \- Test how well models can locate specific information within documents

  2. **Benchmarking long-context understanding** \- Even at 10 pages, this tests modelsâ ability to process extended visual content

  3. **Comparing text vs. multimodal retrieval** \- Direct comparison between text-only and text+image needle performance

  4. **Visual dataset exploration** \- Use FiftyOneâs visualization tools to understand needle placement patterns

  5. **Model development** \- Train and validate models for document understanding tasks




### Out-of-Scope Use#

  * This dataset is for **research and evaluation purposes only** (CC-BY-NC-4.0 license)

  * Not intended for commercial use without proper licensing

  * Not suitable for training models to extract sensitive information from documents

  * The 5-page subset is not representative of truly long-context scenarios (use 50-200 page subsets for that)




## Dataset Creation#

### Curation Rationale#

The Document Haystack benchmark was created to address the lack of suitable benchmarks for evaluating VLMs on long, visually complex documents. While many benchmarks focus on perception tasks, processing long documents with both text and visual elements remains under-explored.

The 5-page subset serves as:

  * An accessible entry point for initial model testing

  * A faster iteration benchmark for development

  * A baseline for comparing against longer document performance




### Source Data#

#### Data Collection and Processing#

  * **Base documents:** Real-world documents including annual reports, financial filings, and corporate documents from 25 different organizations

  * **Page extraction:** Documents converted to 200 DPI page images

  * **Needle insertion:** Key-value pairs strategically placed across pages with controlled randomization

    * Needles placed in non-overlapping page ranges

    * Same locations used for both text and text+image variants

    * Various visual properties (fonts, colors, sizes) to test robustness

  * **Text extraction:** OCR/parsing for text-only variants




#### Who are the source data producers?#

The original documents are publicly available corporate documents (annual reports, financial statements, etc.). The benchmark itself was created by researchers at Amazon AGI.

### Annotations#

#### Annotation Process#

Annotations include:

  * **Needle placement metadata:** Precise coordinates, font properties, colors

  * **Ground truth answers:** Extracted key-value pairs for each needle

  * **Retrieval questions:** Automatically generated questions following the template âWhat is the secret KEY in the document?â




The placement is automated but controlled to ensure:

  * Even distribution across document pages

  * Non-overlapping placement

  * Visibility and retrievability




#### Who are the Annotators?#

Annotations were automatically generated as part of the benchmark creation process by the Amazon AGI research team.

### Personal and Sensitive Information#

The dataset consists of publicly available corporate documents (annual reports, financial filings). No personal or sensitive information beyond what is publicly available in these corporate documents is present.

Needles are synthetic key-value pairs and do not contain real sensitive information.

## Bias, Risks, and Limitations#

**Limitations:**

  * **Document diversity:** Limited to 25 base documents from corporate/financial domain

  * **English-only:** All documents and needles are in English

  * **5-page constraint:** Not representative of truly long documents (50-200 pages)

  * **Synthetic task:** Needle retrieval is a proxy task for real document understanding

  * **Visual styling:** Needles use specific visual properties that may not represent all real-world scenarios




**Biases:**

  * Corporate document focus may not generalize to other document types

  * Needle categories reflect common Western concepts

  * Single language limits cross-lingual evaluation




**Risks:**

  * Models optimized for this benchmark may overfit to the needle retrieval pattern

  * Performance on this task may not correlate with general document understanding




### Recommendations#

Users should:

  * Use this dataset alongside other document understanding benchmarks

  * Test on multiple page lengths (5, 10, 25, 50+ pages) for comprehensive evaluation

  * Consider domain shift when applying models to non-corporate documents

  * Validate that good performance translates to real-world document tasks

  * Be aware this tests retrieval, not deeper comprehension or reasoning




## Citation#

If you use this dataset, please cite the original Document Haystack paper:

**BibTeX:**
    
    
    @article{huybrechts2025document,
      title={Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark},
      author={Huybrechts, Goeric and Ronanki, Srikanth and Jayanthi, Sai Muralidhar and Fitzgerald, Jack and Veeravanallur, Srinivasan},
      journal={arXiv preprint arXiv:2507.15882},
      year={2025}
    }
    

**APA:**

Huybrechts, G., Ronanki, S., Jayanthi, S. M., Fitzgerald, J., & Veeravanallur, S. (2025). Document Haystack: A Long Context Multimodal Image/Document Understanding Vision LLM Benchmark. arXiv preprint arXiv:2507.15882.

## More Information#

### FiftyOne Integration#

This dataset leverages FiftyOneâs capabilities for:

  * Visual exploration of needle locations via Keypoints

  * Filtering and querying by document properties

  * Classification-based analysis of keys and answers

  * Integration with FiftyOne Brain for embeddings and similarity




### Related Datasets#

The full Document Haystack benchmark includes variants with:

  * 5, 10, 25, 50, 75, 100, 150, and 200 pages

  * 400 document variants total

  * 8,250 retrieval questions




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
