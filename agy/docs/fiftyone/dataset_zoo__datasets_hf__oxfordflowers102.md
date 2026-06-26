---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/oxfordflowers102.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/OxfordFlowers102)

# Dataset Card for Oxford Flowers 102#

![image/png](https://huggingface.co/datasets/Voxel51/OxfordFlowers102/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 8189 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/OxfordFlowers102")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

102 category dataset, consisting of 102 flower categories. The flowers chosen to be flower commonly occuring in the United Kingdom. Each class consists of between 40 and 258 images. The details of the categories and the number of images for each class can be found on this [category statistics page](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/categories.html). The images have large scale, pose and light variations. In addition, there are categories that have large variations within the category and several very similar categories.

  * **Curated by:** Nilsback, M-E. and Zisserman, A.

  * **Language(s) (NLP):** en

  * **License:** other




### Dataset Sources#

  * **Homepage:** https://www.robots.ox.ac.uk/~vgg/data/flowers/102/

  * **Paper:** https://www.robots.ox.ac.uk/~vgg/publications/2008/Nilsback08/

  * **Demo:** https://try.fiftyone.ai/datasets/oxford-flowers-102/samples




## Citation#

**BibTeX:**
    
    
    @InProceedings{Nilsback08,
      author       = "Maria-Elena Nilsback and Andrew Zisserman",
      title        = "Automated Flower Classification over a Large Number of Classes",
      booktitle    = "Indian Conference on Computer Vision, Graphics and Image Processing",
      month        = "Dec",
      year         = "2008",
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
