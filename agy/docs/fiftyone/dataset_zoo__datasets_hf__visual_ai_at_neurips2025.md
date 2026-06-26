---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/visual_ai_at_neurips2025.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/visual_ai_at_neurips2025)

# Dataset Card for neurips-2025-vision-papers#

![image/png](https://huggingface.co/datasets/Voxel51/visual_ai_at_neurips2025/resolve/main/visual_ai_neurips2025.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 1134 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/visual_ai_at_neurips2025")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset contains NeurIPS 2025 accepted papers focused on computer vision and related fields, enriched with arXiv metadata and first-page images. It includes papers from multiple vision-related categories including Computer Vision (cs.CV), Multimedia (cs.MM), Image and Video Processing (eess.IV), Graphics (cs.GR), and Robotics (cs.RO). Each entry includes paper metadata, abstracts, author information, and a high-resolution (500 DPI) PNG image of the paperâs first page.

  * **Curated by:** Harpreet Sahota

  * **Language(s) (NLP):** en

  * **License:** Apache 2.0




### Dataset Sources#

  * **Original Data Source:** NeurIPS 2025 Conference (https://neurips.cc/virtual/2025/calendar)

  * **arXiv API:** https://arxiv.org/




## Uses#

### Direct Use#

This dataset is suitable for:

  * Analyzing trends in computer vision research at NeurIPS 2025

  * Vision-Language Model (VLM) analysis of paper content

  * OCR and text extraction from academic papers

  * Building search and recommendation systems for academic papers

  * Studying paper formatting, structure, and visual presentation

  * Training models to understand academic paper layouts




### Out-of-Scope Use#

This dataset should not be used for:

  * Representing the complete NeurIPS 2025 corpus (only vision-related papers with arXiv IDs)

  * Papers without arXiv IDs are not included

  * Full paper content analysis (only first pages are included)

  * Citation analysis (references are not included)




## Dataset Structure#

The dataset contains the following fields:

  * **filepath** : Path to the first-page PNG image (500 DPI)

  * **type** : Paper presentation type (e.g., âPosterâ, âOralâ)

  * **name** : Paper title

  * **virtualsite_url** : URL to the paper on NeurIPS virtual site

  * **abstract** : Paper abstract

  * **arxiv_id** : arXiv identifier (e.g., â2301.12345v2â)

  * **arxiv_authors** : List of paper authors from arXiv

  * **arxiv_category** : Classification field with paper category (cs.CV, cs.MM, eess.IV, cs.GR, or cs.RO)




## Dataset Creation#

### Curation Rationale#

This dataset was created to provide a focused collection of vision-related papers from NeurIPS 2025 with high-quality first-page images for multimodal analysis. The motivation was to enable researchers and practitioners to:

  1. Analyze paper content using Vision-Language Models

  2. Study trends in computer vision research

  3. Build tools for academic paper understanding




### Source Data#

#### Data Collection and Processing#

  1. **Initial Collection** : Paper metadata scraped from NeurIPS 2025 virtual conference site

  2. **arXiv Matching** : Papers matched with arXiv using title and author matching algorithms

  3. **Category Filtering** : Filtered to include only vision-related categories (cs.CV, cs.MM, eess.IV, cs.GR, cs.RO) with valid arXiv IDs

  4. **PDF Download** : First pages downloaded from arXiv (https://arxiv.org/pdf/{arxiv_id}.pdf)

  5. **Image Conversion** : PDFs converted to PNG images at 500 DPI using pdf2image

  6. **Quality** : 500 DPI ensures readability of 10pt font common in academic papers




#### Who are the source data producers?#

  * **NeurIPS 2025 Conference** : Original paper metadata and acceptance decisions

  * **arXiv** : Paper PDFs and metadata

  * **Paper Authors** : Original paper content




### Annotations#

#### Annotation process#

The `arxiv_category` field represents the primary arXiv category assigned by paper authors during submission. No additional manual annotations were added.

## Bias, Risks, and Limitations#

**Limitations:**

  * Only includes papers with arXiv IDs (some NeurIPS papers may not be on arXiv)

  * Only includes first page (no full paper content)

  * Limited to specific vision-related categories

  * arXiv matching may have errors or mismatches

  * Images are high resolution (500 DPI) resulting in larger file sizes




**Biases:**

  * Excludes papers without arXiv presence

  * May underrepresent certain research areas or institutions with different publication practices

  * Category classification reflects author self-assignment on arXiv




### Recommendations#

Users should be made aware that:

  * This is not a complete representation of NeurIPS 2025 papers

  * arXiv matching was automated and may contain errors

  * Only first pages are available (for full papers, refer to arXiv or NeurIPS proceedings)

  * High DPI images require significant storage space




## Citation#

**NeurIPS 2025:**
    
    
    @inproceedings{neurips2025,
      title={Neural Information Processing Systems},
      year={2025},
      organization={NeurIPS}
    }
    

## Dataset Card Contact#

Harpreet Sahota

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
