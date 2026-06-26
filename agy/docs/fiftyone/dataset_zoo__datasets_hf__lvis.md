---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/lvis.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/LVIS)

# Dataset Card for LVIS-35k#

![image](https://huggingface.co/datasets/Voxel51/LVIS/resolve/main/LVIS.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 35000 samples.

**NOTE:** This is only a 35k sample subset of the full dataset. The notebook recipe for creating this, and the full, dataset can be found [here](https://colab.research.google.com/drive/1SmdZPWtLhNis_cCRnO9WKKZQ9OaP_C_d)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/LVIS")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

LVIS (pronounced âel-visâ) is a dataset for large vocabulary instance segmentation, introduced by researchers from Facebook AI.

  * It contains annotations for over 1000 object categories across 164k images. The full dataset is planned to have ~2 million high-quality instance segmentation masks.

  * The categories in LVIS follow a natural long-tail distribution, with a few common categories and many rare ones with few training examples. This long tail poses a challenge for current state-of-the-art object detection methods which struggle with low-sample categories.

  * The vocabulary was constructed iteratively, starting from 8.8k concrete noun synsets in WordNet and filtering down to the final set[4].

  * LVIS can be used for instance segmentation, semantic segmentation, and object detection tasks. The dataset aims to focus the research community on the open challenge of long-tail object recognition.




In summary, LVIS is a large-scale, high-quality dataset that targets the difficult problem of learning segmentation models for various object categories, including many rare ones. It is freely available for research use.

  * **Curated by:** Agrim Gupta, Piotr DollÃ¡r, Ross Girshick

  * **Funded by:** Facebook AI Research (FAIR)

  * **Shared by:** Harpreet Sahota, Hacker-in-Residence at Voxel51

  * **Language(s) (NLP):** en

  * **License:** [Custom License](https://github.com/lvis-dataset/lvis-api/blob/master/LICENSE)




### Dataset Sources [optional]#

  * **Website:** https://www.lvisdataset.org/

  * **Repository:** https://github.com/lvis-dataset/lvis-api

  * **Paper:** https://arxiv.org/abs/1908.03195




## Citation#

**BibTeX:**
    
    
    @inproceedings{gupta2019lvis,
      title={{LVIS}: A Dataset for Large Vocabulary Instance Segmentation},
      author={Gupta, Agrim and Dollar, Piotr and Girshick, Ross},
      booktitle={Proceedings of the {IEEE} Conference on Computer Vision and Pattern Recognition},
      year={2019}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
