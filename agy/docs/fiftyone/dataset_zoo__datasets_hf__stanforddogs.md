---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/stanforddogs.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/StanfordDogs)

# Dataset Card for StanfordDogs#

![image/png](https://huggingface.co/datasets/Voxel51/StanfordDogs/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 20580 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/StanfordDogs")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The Stanford Dogs dataset contains images of 120 breeds of dogs from around the world. This dataset has been built using images and annotation from ImageNet for the task of fine-grained image categorization. Contents of this dataset:

  * Number of categories: 120

  * Number of images: 20,580

  * Annotations: Class labels, Bounding boxes



  * **Language(s) (NLP):** en

  * **License:** [More Information Needed]




### Dataset Sources [optional]#

  * **Paper:** [Novel dataset for Fine-Grained Image Categorization](http://people.csail.mit.edu/khosla/papers/fgvc2011.pdf)

  * **Homepage:** http://vision.stanford.edu/aditya86/ImageNetDogs/




## Uses#

Fine-grained visual classification

## Citation#

**BibTeX:**
    
    
    @inproceedings{KhoslaYaoJayadevaprakashFeiFei_FGVC2011,
      author = "Aditya Khosla and Nityananda Jayadevaprakash and Bangpeng Yao and Li Fei-Fei",
      title = "Novel Dataset for Fine-Grained Image Categorization",
      booktitle = "First Workshop on Fine-Grained Visual Categorization, IEEE Conference on Computer Vision and Pattern Recognition",
      2011,
      month = "June",
      address = "Colorado Springs, CO",
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

## Dataset Contacts#

aditya86@cs.stanford.edu and bangpeng@cs.stanford.edu

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
