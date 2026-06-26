---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/waveui_25k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/WaveUI-25k)

# Dataset Card for WaveUI-25k#

![image/png](https://huggingface.co/datasets/Voxel51/WaveUI-25k/resolve/main/waveui25k.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 24977 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/WaveUI-25k")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

WaveUI-25k is a curated dataset of approximately 25,000 labeled user interface (UI) elements, assembled to support research and development in UI understanding, navigation, and automation. The dataset is designed for training and evaluating AI agents-particularly those that need to interact with web and mobile UIs-by providing richly annotated examples of real-world UI components. Each example includes detailed metadata to facilitate tasks such as click prediction, coordinate localization, and UI automation.

  * **Curated by:** AgentSea

  * **Shared by:** AgentSea

  * **Language(s) (NLP):** en (with coverage of other languages as they appear in UI text)

  * **License:** Not Listed




### Dataset Sources#

  * **Repository:** Hugging Face: https://huggingface.co/datasets/agentsea/wave-ui-25k

  * **Paper:** No dedicated paper for WaveUI-25k, but the main sources are:

    * WebUI: Wu et al., 2023

    * RoboFlow Website Screenshots: Roboflow Universe

    * GroundUI-18K: Zheng et al., 2024




## Uses#

### Direct Use#

  * Training and evaluating AI agents for GUI navigation, click prediction, and coordinate localization.

  * Enhancing machine learning models for UI automation, such as robotic process automation (RPA) and multimodal agents.

  * Improving UI understanding for both web and mobile interfaces.

  * Supporting research in visual-language models (VLMs) and multimodal large language models (MLLMs) that interact with graphical interfaces.




### Out-of-Scope Use#

  * Any use that involves extracting or inferring personal, sensitive, or private information from UI screenshots, as the dataset is not intended for privacy-invasive applications.

  * Use cases requiring exhaustive coverage of all possible UI types or highly specialized, domain-specific UI elements, as the dataset is a filtered subset and may not be comprehensive for all domains.

  * Malicious use, such as training agents to exploit security flaws in UIs.




## Dataset Structure#

Each entry in WaveUI-25k represents UI elements and includes the following fields:

# WaveUI-25k Dataset Structure#

**Core Fields:**

  * **`metadata`** : EmbeddedDocumentField - Image properties (size, dimensions)

  * **`instruction`** : StringField - UI element type description

  * **`source`** : StringField - Data origin (webui, roboflow)

  * **`platform`** : StringField - Web, mobile, or desktop

  * **`name`** : StringField - Element name

  * **`language`** : StringField - Text language

  * **`purpose`** : StringField - Elementâs intended function

  * **`expectation`** : StringField - Expected interaction outcome

  * **`detections`** : EmbeddedDocumentField containing:

    * **`label`** : Element type (button, link)

    * **`bounding_box`** : a list of relative bounding box coordinates in [0, 1] in the following format: `[<top-left-x>, <top-left-y>, <width>, <height>]`

    * **`text`** : OCR content

    * **`description`** : Detailed element description




The dataset provides comprehensive annotations of UI elements for machine learning applications. The dataset is stored in FiftyOne format, with a total size of approximately 10.6 GB and 24,978 samples.

## Dataset Creation#

### Curation Rationale#

The motivation behind WaveUI-25k is to provide a high-quality, unified, and richly annotated dataset for advancing the training of AI agents capable of understanding and navigating complex user interfaces. Previous datasets either lacked detailed annotations or suffered from inconsistent labeling, limiting their utility for sophisticated agent training. WaveUI-25k addresses these gaps by harmonizing, cleaning, and enriching data from multiple leading sources.

### Source Data#

#### Data Collection and Processing#

  * The dataset is a unified compilation of three major sources: WebUI, RoboFlow Website Screenshots, and GroundUI-18K.

  * Preprocessing steps included schema harmonization, removal of duplicates, filtering out overlapping and low-quality examples, and exclusion of text elements not relevant to the scope.

  * Additional annotation was performed to add detailed fields such as purpose and expectation, using a combination of programmatic methods and large language models for enrichment.




#### Who are the source data producers?#

  * WebUI: Crawled web pages with automatically extracted metadata, produced by academic researchers (Wu et al., 2023).

  * RoboFlow Website Screenshots: Synthetic screenshots and annotations generated by the Roboflow team.

  * GroundUI-18K: Annotated images for UI grounding, produced by academic researchers (Zheng et al., 2024).




### Annotations#

#### Annotation process#

  * The original datasets provided basic annotations (e.g., bounding boxes, element types).

  * AgentSeaâs team further annotated the selected 25k subset, adding fields such as name, description, purpose, and expectation.

  * Annotation was performed using a combination of manual review, programmatic filtering, and enrichment via large language models.




#### Who are the annotators?#

  * AgentSeaâs applied AI team, with assistance from automated tools and LLMs for metadata enrichment.




#### Personal and Sensitive Information#

  * The dataset does not intentionally include personal, sensitive, or private information. Most data is synthetic or anonymized, and efforts were made to filter out any potentially sensitive content during curation.




## Bias, Risks, and Limitations#

  * The dataset may underrepresent certain UI designs, languages, or domains not well-covered by the source datasets.

  * Automated annotation and filtering may introduce errors or inconsistencies.

  * The dataset is not intended for applications involving personal or sensitive data extraction.

  * There may be biases inherent to the source datasets, such as overrepresentation of certain website genres or UI patterns.




### Recommendations#

Users should be aware of the above risks and limitations and validate model performance on their specific target domains. Additional annotation or domain adaptation may be necessary for specialized use cases.

## Citation#

**BibTeX:**
    
    
    @misc{agentsea_waveui25k_2024,
      title = {WaveUI-25k},
      author = {AgentSea},
      howpublished = {\url{https://huggingface.co/datasets/agentsea/wave-ui-25k}},
      year = {2024}
    }
    

## More Information#

  * The dataset is available for download and exploration on Hugging Face.

  * For further questions, contact AgentSea via their Hugging Face page or LinkedIn.




## Dataset Card Authors#

  * AgentSea Applied AI Team




## Dataset Card Contact#

  * AgentSea (see Hugging Face repository for contact details)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
