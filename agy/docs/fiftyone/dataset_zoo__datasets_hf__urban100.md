---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/urban100.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Urban100)

# Dataset Card for Urban100#

![image/png](https://huggingface.co/datasets/Voxel51/Urban100/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2200 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("jamarks/Urban100")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The Urban100 dataset contains 100 images of urban scenes. It commonly used as a test set to evaluate the performance of super-resolution models.

  * **Curated by:** Jia-Bin Huang, Abhishek Singh, Narendra Ahuja

  * **Language(s) (NLP):** en

  * **License:** other




### Dataset Sources#

  * **Repository:** https://github.com/jbhuang0604/SelfExSR

  * **Paper:** https://openaccess.thecvf.com/content_cvpr_2015/papers/Huang_Single_Image_Super-Resolution_2015_CVPR_paper.pdf

  * **Demo:** https://try.fiftyone.ai/datasets/urban100/samples




## Citation#

**BibTeX:**
    
    
    @InProceedings{Huang_2015_CVPR,
    author = {Huang, Jia-Bin and Singh, Abhishek and Ahuja, Narendra},
    title = {Single Image Super-Resolution From Transformed Self-Exemplars},
    booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2015}
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
