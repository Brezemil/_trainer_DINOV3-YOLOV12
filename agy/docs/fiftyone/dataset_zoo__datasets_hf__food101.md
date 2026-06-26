---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/food101.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Food101)

# Dataset Card for Food-101#

![image](https://huggingface.co/datasets/Voxel51/Food101/resolve/main/food-101.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 35000 samples.

**Note:** This dataset is subset of the full Food101 dataset. The recipe notebook for creating this dataset can be found [here](https://colab.research.google.com/drive/11ZDZxaRTVR3DjANNR4p5CnCYqlTYmpfT)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Food101")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The Food-101 dataset is a large-scale dataset for food recognition, consisting of 101,000 images across 101 different food categories.

Here are the key details:

  * Contains a total of 101,000 images

  * Each food class has 1,000 images, with 750 training images and 250 test images per class

  * All images were rescaled to have a maximum side length of 512 pixels

  * **Curated by:** Lukas Bossard, Matthieu Guillaumin, Luc Van Gool

  * **Funded by:** Computer Vision Lab, ETH Zurich, Switzerland

  * **Shared by:** Harpreet Sahota, Hacker-in-Residence at Voxel51

  * **Language(s) (NLP):** en

  * **License:** The dataset images come from Foodspotting and are not owned by the creators of the Food-101 dataset (ETH Zurich). Any use beyond scientific fair use must be negotiated with the respective picture owners according to the Foodspotting terms of use




### Dataset Sources#

  * **Repository:** https://huggingface.co/datasets/ethz/food101

  * **Website:** https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/

  * **Paper:** https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/static/bossard_eccv14_food-101.pdf




## Citation#

**BibTeX:**
    
    
    @inproceedings{bossard14,
      title = {Food-101 -- Mining Discriminative Components with Random Forests},
      author = {Bossard, Lukas and Guillaumin, Matthieu and Van Gool, Luc},
      booktitle = {European Conference on Computer Vision},
      year = {2014}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
