---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/getting_started_labeled_validation.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/getting-started-labeled-validation)

# Dataset Card for validation_photos#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 143 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("TheSteve0/getting-started-labeled-validation")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by:** [More Information Needed]

  * **Funded by [optional]:** [More Information Needed]

  * **Shared by [optional]:** [More Information Needed]

  * **Language(s) (NLP):** en

  * **License:** [More Information Needed]




### Dataset Sources [optional]#

  * **Repository:** [More Information Needed]

  * **Paper [optional]:** [More Information Needed]

  * **Demo [optional]:** [More Information Needed]




## Uses#

### Direct Use#

[More Information Needed]

### Out-of-Scope Use#

[More Information Needed]

## Dataset Structure#

[More Information Needed]

## Dataset Creation#

### Curation Rationale#

[More Information Needed]

### Source Data#

#### Data Collection and Processing#

[More Information Needed]

#### Who are the source data producers?#

[More Information Needed]

### Annotations [optional]#

#### Annotation process#

[More Information Needed]

#### Who are the annotators?#

[More Information Needed]

#### Personal and Sensitive Information#

[More Information Needed]

## Bias, Risks, and Limitations#

[More Information Needed]

### Recommendations#

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations.

## Citation [optional]#

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]#

[More Information Needed]

## More Information [optional]#

[More Information Needed]

## Dataset Card Authors [optional]#

[More Information Needed]

## Dataset Card Contact#

[More Information Needed]

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
