---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/wlasl.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/WLASL)

# Dataset Card for WLASL#

![image/png](https://huggingface.co/datasets/Voxel51/WLASL/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) video dataset with 11980 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/WLASL")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

WLASL is the largest video dataset for Word-Level American Sign Language (ASL) recognition, which features 2,000 common different words in ASL. The authors hope WLASL will facilitate the research in sign language understanding and eventually benefit the communication between deaf and hearing communities.

  * **Curated by:** Dongxu Li and Hongdong Li

  * **Language(s) (NLP):** en

  * **License:** other




### Dataset Sources#

  * **Repository:** https://github.com/dxli94/WLASL

  * **Paper:** https://arxiv.org/abs/1910.11006

  * **Homepage:** https://dxli94.github.io/WLASL/

  * **Demo:** https://try.fiftyone.ai/datasets/asl-dataset/samples




## Uses#

All the WLASL data is intended for academic and computational use only. No commercial usage is allowed. Licensed under the [Computational Use of Data Agreement](https://github.com/microsoft/Computational-Use-of-Data-Agreement/releases/tag/v1.0) (C-UDA)

## Citation#

**BibTeX:**
    
    
    @misc{li2020wordlevel,
          title={Word-level Deep Sign Language Recognition from Video: A New Large-scale Dataset and Methods Comparison}, 
          author={Dongxu Li and Cristian Rodriguez Opazo and Xin Yu and Hongdong Li},
          year={2020},
          eprint={1910.11006},
          archivePrefix={arXiv},
          primaryClass={cs.CV}
    }
    
    @inproceedings{li2020transferring,
     title={Transferring cross-domain knowledge for video sign language recognition},
     author={Li, Dongxu and Yu, Xin and Xu, Chenchen and Petersson, Lars and Li, Hongdong},
     booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
     pages={6205--6214},
     year={2020}
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
