---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/3dvs2026_papers.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/3dvs2026_papers)

# Dataset Card for 3dvs2026_papers#

![image/png](https://huggingface.co/datasets/Voxel51/3dvs2026_papers/resolve/main/3dvpapers.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 176 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/3dvs2026_papers")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

**3DV 2026 Papers in FiftyOne** is a multimodal dataset of all 177 accepted papers from the 13th International Conference on 3D Vision (3DV 2026), held in Vancouver, March 20â23, 2026. The dataset pairs per-page PNG images of each paperâs PDF (and supplementary material) with structured metadata and VLM-generated annotations, loaded into a FiftyOne grouped dataset for interactive exploration and analysis.

Each paper is represented as a FiftyOne _group_ where every page image is its own _slice_. The dataset is designed to support conference navigation: browsing papers by topic, finding visually similar work, and surfacing the most distinctive or representative papers through embedding-based analysis.

  * **Curated by:** Harpreet Sahota

  * **Language(s):** English

  * **License:** The paper content belongs to the respective authors. Dataset structure, annotations, and code are released under MIT.




### Dataset Sources#

  * **Companion notebook:** `3DV_Papers_in_Fiftyone.ipynb`

  * **Conference:** [3DV 2026](https://3dvconf.github.io/2026/) â OpenReview submissions at [openreview.net](https://openreview.net)




* * *

## Uses#

### Direct Use#

  * **Conference navigation:** Browse and filter papers by research topic, session, affiliation, or contribution type in the FiftyOne App

  * **Visual similarity search:** Find papers with visually or semantically similar content using the Jina v4 embedding index

  * **Paper discovery:** Rank papers by uniqueness or representativeness to surface distinctive work or archetypal contributions in each area

  * **Schedule planning:** Cross-reference session metadata (`oral_date`, `oral_start_time`, `poster_session`) with topic and uniqueness scores to build a personalised conference agenda




### Out-of-Scope Use#

  * This dataset is not intended for training machine learning models on paper content

  * The VLM-generated annotations (topic labels, affiliations, contribution flags) are model predictions and may contain errors â do not treat them as ground truth




* * *

## Dataset Structure#

The dataset is a FiftyOne **grouped dataset**. Each group corresponds to one paper; each sample within the group is one page image.

**Slice naming:**

  * `page_01`, `page_02`, â¦ `page_NN` â pages from the main PDF (8â22 pages per paper)

  * `supp_page_01`, `supp_page_02`, â¦ â pages from supplementary material (1â83 pages; absent for papers without supplements)




**Dataset statistics:**

  * 176 papers with images (1 of 177 accepted papers had no available PDF)

  * 3,019 total page images across all slices

  * 22 oral papers, 154 poster-only papers




**Fields on every sample:**

Field | Type | Description  
---|---|---  
`paper_id` | string | Submission ID from OpenReview  
`title` | string | Paper title  
`authors` | list[string] | Author names  
`abstract` | string | Full abstract text  
`affiliations` | list[string] | Author institutions (VLM-extracted, ASCII-normalised)  
`poster_session` | int | Poster session number (1â6)  
`poster_start_time` | string | Poster session start time  
`oral_date` | string | Date of oral presentation (null for poster-only papers)  
`oral_start_time` | string | Oral session start time (null for poster-only papers)  
`pdf_link` | string | OpenReview PDF URL  
`supplementary_link` | string | OpenReview supplementary URL  
`project_page` | string | Project page or GitHub URL (null if none found)  
`has_code` | string | `"Yes"` / `"No"` derived from `project_page`  
`number_of_authors` | int | Author count  
`topic_classifications` | Classifications | VLM-assigned topic label (one of 10 categories)  
`introduces_dataset` | string | `"Yes"` / `"No"` â paper introduces a new dataset  
`introduces_model` | string | `"Yes"` / `"No"` â paper introduces a new model or architecture  
`introduces_method` | string | `"Yes"` / `"No"` â paper introduces a new method or algorithm  
`introduces_benchmark` | string | `"Yes"` / `"No"` â paper includes a benchmark or evaluation  
`jinav4_embeddings` | vector | Per-page Jina v4 2048-dim embedding  
`all_page_embeddings_pooled` | vector | Paper-level mean-pooled embedding (reference pages excluded)  
`jina_represent` | float | Representativeness score (proximity to cluster centre)  
`jina_uniqueness` | float | Uniqueness score (distance from nearest neighbours)  
  
**Topic taxonomy (10 categories):**

  * 3D Reconstruction and Novel View Synthesis

  * 3D Generation and Editing

  * Human Avatars and Motion

  * Hand-Object and Human-Scene Interaction

  * Semantic 3D Understanding

  * Autonomous Driving & Outdoor Perception

  * Depth and Stereo Estimation

  * Dynamic and 4D Scenes

  * Geometric Vision Fundamentals

  * Novel Sensors and Specialized Domains




* * *

## Dataset Creation#

### Curation Rationale#

3DV 2026 received a record 404 submissions with a 43.8% acceptance rate, producing more good work than any attendee can absorb across 3.5 conference days. This dataset was created to support systematic, data-driven conference navigation: rather than relying on title skimming, attendees can explore the full research landscape through interactive visualisation, similarity search, and ranking.

### Source Data#

#### Data Collection and Processing#

  1. **Metadata scraping:** Paper titles, authors, abstracts, PDF links, and supplementary links were collected from OpenReview for all 177 accepted papers. Session scheduling metadata (oral/poster dates and times) was extracted from the official 3DV 2026 conference programme.

  2. **PDF rendering:** Each accepted paperâs main PDF and supplementary material were downloaded from OpenReview and converted to per-page PNG images at 1700Ã2200px using `pdf2image`.

  3. **FiftyOne grouped dataset construction:** Images were loaded into a FiftyOne grouped dataset (`parse_fiftyone_dataset.py`) where each paper is a group and each page is a named slice. All metadata fields were attached to every sample.




#### Who are the source data producers?#

The paper content was produced by the authors of each accepted 3DV 2026 paper. Conference scheduling and programme information was produced by the 3DV 2026 organising committee (General Chairs: Manolis Savva, Angjoo Kanazawa, Christian Theobalt).

### Annotations#

#### Annotation process#

All annotations were generated automatically using Qwen3.5-9B, a reasoning vision-language model, applied to the first page image of each paper (`page_01`) via the FiftyOne Model Zoo. Three annotation passes were run:

  1. **Topic classification** (`classify` operation): The model assigned each paper to exactly one of 10 predefined topic categories based on the visible title, abstract, and teaser figure. Prompt: structured JSON response `[{"label": "topic_name"}]`.

  2. **Affiliation extraction** (`vqa` operation): The model extracted the list of author institutions appearing below the author names. ASCII normalisation was requested (e.g. Ã¼âu) to avoid encoding inconsistencies. Response format: Python list of strings.

  3. **Project page detection** (`vqa` operation): The model identified any project page, GitHub repository, or supplementary site linked on the first page. Response format: URL delimited by triple backticks, or prose indicating no link was found.

  4. **Contribution classification** (`vqa` operation): The model determined whether each paper introduces a new dataset, model/architecture, method/algorithm, or benchmark. Response format: JSON object with boolean fields.




All model responses were parsed using two utility functions (`parse_model_list_response`, `parse_model_url_response`) that strip the `<think>...</think>` reasoning chain and extract the structured answer.

**Embedding annotations** were generated using Jina Embeddings v4 (`jinaai/jina-embeddings-v4`, retrieval task) via the FiftyOne Model Zoo, producing 2048-dim vectors for every page. Paper-level vectors were computed by mean-pooling per-paper page embeddings, excluding pages tagged `reference-page` (identified as a visual outlier cluster in the UMAP). Representativeness and uniqueness scores were computed using `fob.compute_representativeness` and `fob.compute_uniqueness` from the FiftyOne Brain.

#### Who are the annotators?#

Annotations were generated by Qwen3.5-9B (VLM, Qwen team / Alibaba Cloud) and Jina Embeddings v4 (Jina AI). No human annotators were used.

#### Personal and Sensitive Information#

The dataset contains publicly available author names, institutional affiliations, and paper abstracts sourced from OpenReview. This information was submitted voluntarily by paper authors as part of the academic peer review process and is publicly accessible on the OpenReview platform.

* * *

## Bias, Risks, and Limitations#

  * **VLM annotation accuracy:** Topic labels, affiliation extractions, and contribution flags are model predictions. The topic taxonomy is coarse (10 categories) and papers near topic boundaries may be mislabelled. Affiliation strings may be incomplete or incorrectly normalised for some papers.

  * **Reference page exclusion:** Pages tagged `reference-page` were identified interactively by inspecting the UMAP visualisation. This process may have missed some reference pages or incorrectly excluded non-reference pages.

  * **Geographic and institutional bias:** The dataset reflects the accepted papers at one conference edition. Representation of institutions, countries, and research topics is determined by the 3DV 2026 submission and review process, not by this dataset.

  * **PDF availability:** 1 of 177 accepted papers had no PDF available on OpenReview at collection time and is absent from the image data.




### Recommendations#

Topic labels should be treated as a navigational aid rather than a ground truth taxonomy. Users building on the VLM-generated annotations should validate a sample before relying on them for quantitative analysis.

* * *

## Citation#

If you use this dataset or the accompanying code, please cite:

**BibTeX:**
    
    
    @misc{sahota2026_3dvs_fiftyone,
      author       = {Sahota, Harpreet},
      title        = {3DV 2026 Papers in FiftyOne},
      year         = {2026},
      howpublished = {\url{github.com/harpreetsahota204/awesome_3dvision_2026_conference}},
      note         = {Dataset of accepted papers from the 13th International Conference on 3D Vision}
    }
    

* * *

## Dataset Card Authors#

Harpreet Sahota

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
