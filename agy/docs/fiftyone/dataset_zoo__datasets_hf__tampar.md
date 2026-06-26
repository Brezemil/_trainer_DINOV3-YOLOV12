---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/tampar.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/TAMPAR)

# Dataset Card for TAMPAR#

![image/png](https://huggingface.co/datasets/Voxel51/TAMPAR/resolve/main/tampar-skeletons.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 485 samples.

The samples here are from the test set.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("voxel51/TAMPAR")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

TAMPAR is a novel real-world dataset of parcels

  * with >900 annotated real-world images with >2,700 visible parcel side surfaces,

  * 6 different tampering types, and

  * 6 different distortion strengths




This dataset was collected as part of the WACV â24 [paper](https://arxiv.org/abs/2311.03124) _âTAMPAR: Visual Tampering Detection for Parcels Logistics in Postal Supply Chainsâ_

  * **Curated by:** Alexander Naumann, Felix Hertlein, Laura DÃ¶rr and Kai Furmans

  * **Funded by:** FZI Research Center for Information Technology, Karlsruhe, Germany

  * **Shared by:** [Harpreet Sahota](https://huggingface.co/harpreetsahota), Hacker-in-Residence at Voxel51

  * **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode)




### Dataset Sources#

  * **Repository:** https://github.com/a-nau/tampar

  * **Paper:** https://arxiv.org/abs/2311.03124

  * **Demo:** https://a-nau.github.io/tampar/




## Uses#

### Direct Use#

Multisensory setups within logistics facilities and a simple cell phone camera during the last-mile delivery, where only a single RGB image is taken and compared against a reference from an existing database to detect potential appearance changes that indicate tampering.

## Dataset Structure#

COCO Format Annotations

## Citation#
    
    
    @inproceedings{naumannTAMPAR2024,
        author    = {Naumann, Alexander and Hertlein, Felix and D\"orr, Laura and Furmans, Kai},
        title     = {TAMPAR: Visual Tampering Detection for Parcels Logistics in Postal Supply Chains},
        booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
        month     = {January},
        year      = {2024},
        note      = {to appear in}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
