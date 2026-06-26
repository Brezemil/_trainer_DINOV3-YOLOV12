---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/dacl10k.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/dacl10k)

# Dataset Card for dacl10k#

dacl10k stands for damage classification 10k images and is a multi-label semantic segmentation dataset for 19 classes (13 damages and 6 objects) present on bridges.

The dacl10k dataset includes images collected during concrete bridge inspections acquired from databases at authorities and engineering offices, thus, it represents real-world scenarios. Concrete bridges represent the most common building type, besides steel, steel composite, and wooden bridges.

This dataset is used in the challenge associated with the â[1st Workshop on Vision-Based Structural Inspections in Civil Engineering](https://dacl.ai/workshop.html)â at [WACV2024](https://wacv2024.thecvf.com/workshops/).

![image/png](https://huggingface.co/datasets/Voxel51/dacl10k/resolve/main/dataset_preview.jpg)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 8922 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/dacl10k")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Curated by:** Johannes Flotzinger, Philipp J. RÃ¶sch, Thomas Braml

  * **Funded by:** The project was funded by the Bavarian Ministry of Economic Affairs (MoBaP research project, IUK-1911-0004// IUK639/003)

  * **Language(s) (NLP):** en

  * **License:** cc-by-4.0




### Dataset Sources [optional]#

  * **Repository:** https://github.com/phiyodr/dacl10k-toolkit

  * **Paper:** https://arxiv.org/abs/2309.00460

  * **Demo:** https://try.fiftyone.ai/datasets/dacl10k/samples

  * **Homepage:** https://dacl.ai/workshop.html




## Uses#

  * identifying reinforced concrete defects

  * informing restoration works, traffic load limitations or bridge closures




[More Information Needed]

## Dataset Structure#

The dacl10k dataset includes images collected during concrete bridge inspections acquired from databases at authorities and engineering offices, thus, it represents real-world scenarios. Concrete bridges represent the most common building type, besides steel, steel composite, and wooden bridges. dacl10k distinguishes 13 bridge defects as well as 6 bridge components that play a key role in the building assessment. Based on the assessment, actions (e.g., restoration works, traffic load limitations, and bridge closures) are determined. The inspection itself and the resulting actions often impede the traffic and thus private persons and the economy. Furthermore, an ideal timing for restoration helps achieving long-term value added and can save a lot of money. It is important to note that dacl10k includes images from bridge inspections but is not restricted to this building type. Classes of the concrete and general defect group in dacl10k can appear on any building made of concrete. Therefore, it is relevant for most of the other civil engineering structures, too.

## Citation#

**BibTeX:**
    
    
    @misc{flotzinger2023dacl10k,
          title={dacl10k: Benchmark for Semantic Bridge Damage Segmentation}, 
          author={Johannes Flotzinger and Philipp J. RÃ¶sch and Thomas Braml},
          year={2023},
          eprint={2309.00460},
          archivePrefix={arXiv},
          primaryClass={cs.CV}
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
