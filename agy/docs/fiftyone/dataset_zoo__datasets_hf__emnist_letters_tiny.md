---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/emnist_letters_tiny.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/emnist-letters-tiny)

# Dataset Card for EMNIST-Letters-10k#

A random subset of the train and test splits from the letters portion of [EMNIST](https://pytorch.org/vision/0.18/generated/torchvision.datasets.EMNIST.html)

![image/png](https://huggingface.co/datasets/Voxel51/emnist-letters-tiny/resolve/main/dataset_preview.png)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 10000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/emnist-letters-tiny")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by:** [More Information Needed]

  * **Funded by [optional]:** [More Information Needed]

  * **Shared by [optional]:** [More Information Needed]

  * **Language(s) (NLP):** en

  * **License:** [More Information Needed]




### Dataset Sources#

  * **Homepage:** https://www.nist.gov/itl/products-and-services/emnist-dataset

  * **Paper :** https://arxiv.org/abs/1702.05373v1




## Citation#

**BibTeX:**
    
    
    @misc{cohen2017emnistextensionmnisthandwritten,
          title={EMNIST: an extension of MNIST to handwritten letters}, 
          author={Gregory Cohen and Saeed Afshar and Jonathan Tapson and AndrÃ© van Schaik},
          year={2017},
          eprint={1702.05373},
          archivePrefix={arXiv},
          primaryClass={cs.CV},
          url={https://arxiv.org/abs/1702.05373}, 
    }
    

## Dataset Card Author#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
