---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/cvpr_2024_papers.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/CVPR_2024_Papers)

# Dataset Card for cvpr2024_papers#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2379 samples.

The dataset consists of images of the first page for accepted papers to CVPR 2024, plus their abstract and other metadata.

![image/png](https://huggingface.co/datasets/Voxel51/CVPR_2024_Papers/resolve/main/cvpr_papers_dataset.png)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'split', 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/CVPR_2024_Papers")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

This is a dataset of the accepted papers for CVPR 2024.

The 2024 Conference on Computer Vision and Pattern Recognition (CVPR) received 11,532 valid paper submissions, and only 2,719 were accepted, for an overall acceptance rate of about 23.6%.

However, this dataset only has 2,379 papers. This is because its how many we were able to (easily) find papers for.

### Dataset Description#

  * **Curated by:** [Harpreet Sahota, Hacker-in-Residence at Voxel51](https://huggingface.co/harpreetsahota)

  * **Language(s) (NLP):** en

  * **License:** [CC-BY-ND-4.0](https://spdx.org/licenses/CC-BY-ND-4.0)




## Uses#

You can use this dataset to learn about the trends in research at this yearâs CVPR, and so much more!

## Dataset Structure#

The dataset consists of the following:

  * An image of the first page of the paper

  * `title`: The title of the paper

  * `authors_list`: The list of authors

  * `abstract`: The abstract of the paper

  * `arxiv_link`: Link to the paper on arXiv

  * `other_link`: Link to the project page, if found

  * `category_name`: The primary category this paper according to [arXiv taxonomy](https://arxiv.org/category_taxonomy)

  * `all_categories`: All categories this paper falls into, according to arXiv taxonomy

  * `keywords`: Extracted using GPT-4o




## Dataset Creation#

Generic code for building this dataset can be found [here](https://github.com/harpreetsahota204/CVPR-2024-Papers).

This dataset was built using the following steps:

  * Scrape the CVPR 2024 website for accepted papers

  * Use DuckDuckGo to search for a link to the paperâs abstract on arXiv

  * Use arXiv.py (python wrapper for the arXiv API) to extract the abstract, categories, and download the pdf for each paper

  * Use pdf2image to save image of papers first page

  * Use GPT-4o to extract keywords from abstract




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
