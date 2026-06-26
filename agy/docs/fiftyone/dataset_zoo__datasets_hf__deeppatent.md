---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/deeppatent.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/DeepPatent)

# Dataset Card for DeepPatent#

![image](https://huggingface.co/datasets/Voxel51/DeepPatent/resolve/main/deeppatent.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 46179 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/DeepPatent")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

DeepPatent is a large-scale dataset of technical drawings extracted from U.S. design patent documents. The dataset contains patent drawings organized by patent groups (based on publication dates) and individual patent numbers, with each patent containing multiple drawing images showing different views and aspects of the patented designs.

This implementation organizes the data into a FiftyOne grouped dataset structure, where each patent serves as a group containing multiple drawing slices.

  * **Curated by:** Michal Kucer, Diane Oyen, Juan Castorena, Jian Wu (Original 2022 dataset)

  * **Language(s):** English (metadata and patent documentation)

  * **License:** BSD-3 License




### Dataset Sources#

  * **Repository:** https://github.com/GoFigure-LANL/DeepPatent-dataset

  * **Paper:** Kucer, M., Oyen, D., Castorena, J., & Wu, J. (2022). DeepPatent: Large Scale Patent Drawing Recognition and Retrieval. _IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)_.

  * **Related Work:** DeepPatent2 - Extended dataset with over 2.7 million technical drawings (Ajayi et al., 2023)




## Uses#

### Direct Use#

The DeepPatent dataset can be directly used for:

  * **Patent Drawing Recognition:** Training models to recognize and classify patent drawings

  * **Image Retrieval:** Building search systems for finding similar patent drawings

  * **Technical Drawing Understanding:** Research on understanding technical illustrations and design documents

  * **Multi-view Learning:** Studying relationships between different views of the same design

  * **Design Patent Analysis:** Analyzing trends and patterns in design patents over time




### Out-of-Scope Use#

  * Commercial patent infringement or unauthorized use of patented designs

  * Any use that violates USPTO terms of service or patent law

  * Training models for generating counterfeit or infringing designs




## Dataset Structure#

### FiftyOne Grouped Dataset Organization#

The dataset is structured as a FiftyOne grouped dataset with the following organization:

**Group Structure:**

  * **Group Key:** `patent_number` (e.g., âUSD0806350-20180102â)

  * **Group Field:** `group` (automatically managed by FiftyOne)

  * **Slices:** Drawing numbers (e.g., âD00000â, âD00001â, âD00002â, etc.)




**Sample Fields:**

  * `filepath`: Full path to the patent drawing image (PNG format)

  * `patent_group`: Date-based patent group identifier (e.g., âI20180102â for patents published on January 2, 2018)

  * `patent_number`: Complete patent identifier including number and date (e.g., âUSD0806350-20180102â)

  * `drawing_number`: Simplified drawing number extracted from filename (e.g., âD00001â)

  * `filename`: Original image filename

  * `group`: FiftyOne group information linking related drawings

  * `metadata`: Image metadata (width, height, channels, MIME type, etc.)




**Dataset Characteristics:**

  * **Total Samples:** 351,506 patent drawing images

  * **Total Patents:** Variable number of unique patents (each patent is one group)

  * **Images per Patent:** Highly variable (ranging from 5 to over 1,400 drawings per patent)

  * **Drawing Number Slices:** Varies based on the maximum number of drawings in any patent

  * **Image Format:** PNG

  * **Date Range:** Covers multiple years of U.S. design patent publications (2018-2020 visible in this subset)




**Grouping Benefits:**

  * All drawings from the same patent are linked together via the group structure

  * Easy access to all views/drawings for a specific patent

  * Efficient querying by patent characteristics

  * Natural organization for multi-view and sequential learning tasks




## Dataset Creation#

### Curation Rationale#

The DeepPatent dataset was created to address the lack of large-scale datasets for technical drawing understanding and patent analysis. Design patents represent a unique domain of technical illustrations that combine artistic design with functional representation, making them valuable for computer vision research.

### Source Data#

#### Data Collection and Processing#

  * **Source:** U.S. Patent and Trademark Office (USPTO) design patent documents

  * **Collection Method:** Automated extraction of drawing figures from published design patent PDFs

  * **Time Period:** Multiple years of patent publications (at least 2018-2020 in this subset)

  * **Processing:** Drawing images extracted, organized by patent number and publication date

  * **Drawing Numbering:** Original USPTO drawing numbers simplified (e.g., âD00012-1465â â âD00012â)




#### Who are the source data producers?#

The source data producers are:

  * **Primary Source:** U.S. Patent and Trademark Office (USPTO)

  * **Patent Applicants:** Individual inventors, companies, and design firms who filed design patents

  * **Dataset Curators:** Research team led by Michal Kucer, Diane Oyen, Juan Castorena, and Jian Wu




### Annotations#

The dataset primarily consists of unannotated patent drawing images with metadata. The original paper (Kucer et al., 2022) may have included additional annotations for specific tasks like recognition and retrieval.

**Available Metadata:**

  * Patent publication dates (encoded in group names)

  * Patent numbers (unique identifiers)

  * Drawing sequence numbers

  * Image technical metadata (dimensions, format)




## Citation#

### BibTeX#
    
    
    @inproceedings{kucer2022deeppatent,
      title={DeepPatent: Large Scale Patent Drawing Recognition and Retrieval},
      author={Kucer, Michal and Oyen, Diane and Castorena, Juan and Wu, Jian},
      booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
      year={2022}
    }
    

### Related Work#

For the extended dataset with additional annotations:
    
    
    @article{ajayi2023deeppatent2,
      title={DeepPatent2: A Large-Scale Benchmarking Corpus for Technical Drawing Understanding},
      author={Ajayi, Kehinde and Wei, Xin and Gryder, Martin and Shields, Winston and Wu, Jian and Jones, Shawn M. and Kucer, Michal and Oyen, Diane},
      journal={arXiv preprint arXiv:2311.04098},
      year={2023}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
