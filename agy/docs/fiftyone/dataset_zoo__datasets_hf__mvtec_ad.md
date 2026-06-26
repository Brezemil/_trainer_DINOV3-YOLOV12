---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/mvtec_ad.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/mvtec-ad)

# Dataset Card for MVTec AD#

![image/png](https://huggingface.co/datasets/Voxel51/mvtec-ad/resolve/main/dataset_preview.jpg)

This dataset originates from MVTec but is provided in a different format. You can easily load it using [FiftyOne](https://github.com/voxel51/fiftyone) The total number of samples remains the same as the original: 5,354.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/mvtec-ad")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

MVTec AD is a dataset for benchmarking anomaly detection methods with a focus on industrial inspection. It contains over 5000 high-resolution images divided into fifteen different object and texture categories. Each category comprises a set of defect-free training images and a test set of images with various kinds of defects as well as images without defects.

Pixel-precise annotations of all anomalies are also provided.

The data is released under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

In particular, it is not allowed to use the dataset for commercial purposes. If you are unsure whether or not your application violates the non-commercial use clause of the license, please contact the datasetâs authors.

If you have any questions or comments about the dataset, feel free to contact the datasetâs authors via email at re-request@mvtec.com

  * **Language(s) (NLP):** EN

  * **License:** CC BY-NC-SA 4.0




### Dataset Sources#

  * **Dataset Homepage** https://www.mvtec.com/company/research/datasets/mvtec-ad

  * **Demo:** https://try.fiftyone.ai/datasets/mvtec-ad/samples

  * **Paper:** [The MVTec Anomaly Detection Dataset: A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection](https://link.springer.com/content/pdf/10.1007/s11263-020-01400-4.pdf)




## Dataset Creation#

### Source Data#

Data downloaded and converted from [MVTec website](https://www.mvtec.com/company/research/datasets/mvtec-ad)

## Citation#

**BibTeX:**
    
    
    @article{Bergmann2021MVTecAnomalyDetection,
      title={The MVTec Anomaly Detection Dataset: A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection},
      author={Bergmann, Paul and Batzner, Kilian and Fauser, Michael and Sattlegger, David and Steger, Carsten},
      journal={International Journal of Computer Vision},
      volume={129},
      number={4},
      pages={1038--1059},
      year={2021},
      doi={10.1007/s11263-020-01400-4}
    }
    
    @inproceedings{Bergmann2019MVTecAD,
      title={MVTec AD â A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection},
      author={Bergmann, Paul and Fauser, Michael and Sattlegger, David and Steger, Carsten},
      booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
      pages={9584--9592},
      year={2019},
      doi={10.1109/CVPR.2019.00982}
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
