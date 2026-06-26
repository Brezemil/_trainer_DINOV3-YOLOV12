---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/coursera_lecture_dataset_train.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Coursera_lecture_dataset_train)

# Dataset Card for Lecture Training Set for Coursera MOOC - Hands Data Centric Visual AI#

This dataset is the **training dataset for the in-class lectures** of the Hands-on Data Centric Visual AI Coursera course.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 16638 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Coursera_lecture_dataset_train")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset is a modified subset of the [LVIS dataset](https://www.lvisdataset.org/).

The dataset here only contains detections, some of which have been artificially perturbed and altered to demonstrate data centric AI techniques and methodologies for the course.

This dataset has the following labels:

  * âjacketâ

  * âcoatâ

  * âjeanâ

  * âtrousersâ

  * âshort_pantsâ

  * âtrash_canâ

  * âbucketâ

  * âflowerpotâ

  * âhelmetâ

  * âbaseball_capâ

  * âhatâ

  * âsunglassesâ

  * âgogglesâ

  * âdoughnutâ

  * âpastryâ

  * âonionâ

  * âtomatoâ




### Dataset Sources [optional]#

  * **Repository:** https://www.lvisdataset.org/

  * **Paper:** https://arxiv.org/abs/1908.03195




## Uses#

The labels in this dataset have been perturbed to illustrate data centric AI techniques for the Hands-on Data Centric AI Coursera MOOC.

## Dataset Structure#

Each image in the dataset comes with detailed annotations in FiftyOne detection format. A typical annotation looks like this:
    
    
    <Detection: {
        'id': '66a2f24cce2f9d11d98d39f3',
        'attributes': {},
        'tags': [],
        'label': 'trousers',
        'bounding_box': [
            0.5562343750000001,
            0.4614166666666667,
            0.1974375,
            0.29300000000000004,
        ],
        'mask': None,
        'confidence': None,
        'index': None,
    }>
    

## Dataset Creation#

### Curation Rationale#

The selected labels for this dataset is due to the fact that these objects can be confusing to a model. Thus, making them a great choice for demonstrating data centric AI techniques.

[More Information Needed]

### Source Data#

This is a subset of the [LVIS dataset.](https://www.lvisdataset.org/)

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
