---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/hard_hat_detection.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/hard-hat-detection)

# Dataset Card for hard-hat-detection#

This dataset, contains 5000 images with bounding box annotations in the PASCAL VOC format for these 3 classes:

  * Helmet

  * Person

  * Head




![image/png](https://huggingface.co/datasets/Voxel51/hard-hat-detection/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 5000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'split', 'max_samples', etc
    dataset = fouh.load_from_hub("dgural/hard-hat-detection")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Improve workplace safety by detecting people and hard hats on 5k images with bbox annotations.

  * **Language(s) (NLP):** en

  * **License:** cc0-1.0




### Dataset Sources#

  * **Repository:** https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/data




### Source Data#

Dataset taken from https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/data and created by [andrewmvd](https://www.kaggle.com/andrewmvd)

## Citation#

**BibTeX:**

@misc{make ml, title={Hard Hat Dataset}, url={https://makeml.app/datasets/hard-hat-workers}, journal={Make ML}}

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
