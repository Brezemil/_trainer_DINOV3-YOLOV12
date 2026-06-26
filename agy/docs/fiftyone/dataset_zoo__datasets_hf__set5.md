---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/set5.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Set5)

# Dataset Card for Set5#

![image/png](https://huggingface.co/datasets/Voxel51/Set5/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 135 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Set5")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The Set5 dataset is a dataset consisting of 5 images (âbabyâ, âbirdâ, âbutterflyâ, âheadâ, âwomanâ) commonly used for testing performance of Image Super-Resolution models.

  * **Curated by:** Bevilacqua, Marco and Roumy, Antoine and Guillemot, Christine and Alberi-Morel, Marie-Line

  * **Language(s) (NLP):** en

  * **License:** other




### Dataset Sources#

  * **Repository:** https://github.com/ChaofWang/Awesome-Super-Resolution/blob/master/dataset.md

  * **Paper:** [Low-Complexity Single-Image Super-Resolution based on Nonnegative Neighbor Embedding](https://people.rennes.inria.fr/Aline.Roumy/publi/12bmvc_Bevilacqua_lowComplexitySR.pdf)

  * **Homepage:** https://people.rennes.inria.fr/Aline.Roumy/results/SR_BMVC12.html




## Uses#

Super-resolution

## Dataset Creation#

## Citation#

**BibTeX:**
    
    
    @inproceedings{bevilacqua2012low,
      title={Low-Complexity Single-Image Super-Resolution based on Nonnegative Neighbor Embedding},
      author={Bevilacqua, Marco and Roumy, Antoine and Guillemot, Christine and Alberi-Morel, Marie-Line},
      booktitle={Proceedings of the British Machine Vision Conference (BMVC)},
      year={2012}
    }
    

## Dataset Card Author#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
