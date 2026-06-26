---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/set14.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Set14)

# Dataset Card for Set14#

![image/png](https://huggingface.co/datasets/Voxel51/Set14/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 378 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Set14")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The Set14 dataset is a dataset consisting of 14 images commonly used for testing performance of Image Super-Resolution models.

  * **Language(s) (NLP):** en

  * **License:** other




### Dataset Sources [optional]#

  * **Paper:** https://link.springer.com/chapter/10.1007/978-3-642-27413-8_47

  * **Demo:** https://try.fiftyone.ai/datasets/set14/samples




## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
