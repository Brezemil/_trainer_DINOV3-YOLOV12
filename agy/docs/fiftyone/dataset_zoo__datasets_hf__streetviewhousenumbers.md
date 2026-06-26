---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/streetviewhousenumbers.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/StreetViewHouseNumbers)

# Dataset Card for Street View House Numbers#

![image](https://huggingface.co/datasets/Voxel51/StreetViewHouseNumbers/resolve/main/SVHN.gif)

The Street View House Numbers (SVHN) dataset is a large real-world image dataset used for developing machine learning and object recognition algorithms. It contains over 600,000 labeled images of house numbers taken from Google Street View.

The images are cropped to a fixed resolution of 32x32 pixels, centered around a single character but may contain some distractors at the sides.

SVHN is similar to the MNIST dataset but incorporates significantly more labeled data and comes from a harder, unsolved, real-world problem of recognizing digits and numbers in natural scene images.

The dataset here is provided as original images with character level bounding boxes

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 33402 samples.

The recipe notebook for creating this dataset can be found [here](https://colab.research.google.com/drive/1rwlDeLbsz498nrjemaRC7Tn8IMFZw8x7?usp=sharing)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/StreetViewHouseNumbers")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

  * **Curated by:** Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, Andrew Y. Ng

  * **Funded by:** Google Inc., Stanford University

  * **Shared by:** [More Information Needed]

  * **License:** non-commercial use only




For questions regarding the dataset, please contact streetviewhousenumbers@gmail.com

### Dataset Sources#

  * **Repository:** http://ufldl.stanford.edu/housenumbers

  * **Paper:** http://ufldl.stanford.edu/housenumbers/nips2011_housenumbers.pdf




## Citation#

**BibTeX:**
    
    
    @inproceedings{netzer2011reading,
      title={Reading digits in natural images with unsupervised feature learning},
      author={Netzer, Yuval and Wang, Tao and Coates, Adam and Bissacco, Alessandro and Wu, Bo and Ng, Andrew Y},
      booktitle={NIPS workshop on deep learning and unsupervised feature learning},
      volume={2011},
      number={2},
      pages={5},
      year={2011}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
