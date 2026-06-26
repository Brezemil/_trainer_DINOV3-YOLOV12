---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/coursera_homework_dataset_test.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Coursera_homework_dataset_test)

# Dataset Card for Homework Test Set for Coursera MOOC - Hands Data Centric Visual AI#

This dataset is the **test dataset for the homework** in the Hands-on Data Centric Visual AI Coursera course.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 4572 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Coursera_homework_dataset_test")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

This dataset is a modified subset of the [LVIS dataset](https://www.lvisdataset.org/).

The dataset here only contains detections, **NONE** of which have been artificially perturbed.

This dataset has the following labels:

  * âboltâ

  * âknobâ

  * âtagâ

  * âbuttonâ

  * âbottle_capâ

  * âbeltâ

  * âstrapâ

  * ânecktieâ

  * âshirtâ

  * âsweaterâ

  * âstreetlightâ

  * âpoleâ

  * âreflectorâ

  * âheadlightâ

  * âtaillightâ

  * âtraffic_lightâ

  * ârearview_mirrorâ




### Dataset Sources#

  * **Repository:** https://www.lvisdataset.org/

  * **Paper:** https://arxiv.org/abs/1908.03195




## Uses#

Unlike the [training dataset](https://huggingface.co/datasets/Voxel51/Coursera_homework_dataset_train) for the course, the labels in this dataset **HAVE NOT** been perturbed.

## Dataset Structure#

Each image in the dataset comes with detailed annotations in FiftyOne detection format. A typical annotation looks like this:
    
    
    <Detection: {
        'id': '66a2f24cce2f9d11d98d3a21',
        'attributes': {},
        'tags': [],
        'label': 'shirt',
        'bounding_box': [
            0.25414,
            0.35845238095238097,
            0.041960000000000004,
            0.051011904761904765,
        ],
        'mask': None,
        'confidence': None,
        'index': None,
    }>
    

## Dataset Creation#

### Curation Rationale#

The selected labels for this dataset is because these objects can be confusing to a model. Thus, making them a great choice for demonstrating data centric AI techniques.

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
