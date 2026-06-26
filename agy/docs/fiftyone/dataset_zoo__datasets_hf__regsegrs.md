---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/regsegrs.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/RegSegRS)

# Dataset Card for RefSegRS#

![image/png](https://huggingface.co/datasets/Voxel51/RegSegRS/resolve/main/refseg_rs.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 4420 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/RefSegRS")
    
    # Launch the App
    session = fo.launch_app(dataset)
    
    
    

### NOTE: This dataset is .tif media, for best results view in Safari browser or a browser which supports displaying .tif#

## Dataset Details#

### Dataset Description#

RefSegRS is a referring remote sensing image segmentation (RRSIS) dataset that enables pixel-level segmentation of objects in remote sensing imagery based on natural language descriptions. The dataset addresses the task of localizing and segmenting desired objects from remote sensing images using referring expressions that include categories, attributes, and spatial relationships.

The dataset is built on top of the SkyScapes dataset, consisting of cropped and downsampled aerial RGB images with corresponding segmentation masks and natural language referring expressions. Images are captured from a top-down view with 13 cm spatial resolution, featuring urban scenes with various objects including vehicles, roads, buildings, vegetation, and infrastructure elements.

  * **Curated by:** Zhenghang Yuan, Lichao Mou, Yuansheng Hua, and Xiao Xiang Zhu (Technical University of Munich)

  * **Language(s) (NLP):** English

  * **License:** CC-BY-4.0




### Dataset Sources#

  * **HF Repository:** https://huggingface.co/datasets/JessicaYuan/RefSegRS

  * **Project Repository:** https://github.com/zhu-xlab/rrsis

  * **Paper (arXiv):** https://arxiv.org/abs/2306.08625

  * **Related Work:** This dataset is part of research on combining remote sensing imagery with natural language processing, related to visual grounding, visual question answering (VQA), and image captioning for remote sensing data.




## Dataset Structure#

The RefSegRS dataset contains **4,420 image-language-label triplets** organized into three splits:

  * **Training set:** 2,172 triplets

  * **Validation set:** 431 triplets

  * **Test set:** 1,817 triplets




### Image Specifications#

  * **Format:** TIFF (RGB, 3 channels)

  * **Dimensions:** 512 Ã 512 pixels

  * **Original resolution:** 13 cm spatial resolution

  * **Source:** Cropped from SkyScapes dataset tiles (original 5616 Ã 3744 pixels) using 1200 Ã 1200 pixel sliding windows with 600-pixel stride, then downsampled




### Segmentation Masks#

  * **Format:** TIFF (binary masks)

  * **Dimensions:** 512 Ã 512 pixels

  * **Values:** Binary (0 for background, 1 for target object)

  * **Generation:** Automatically generated from SkyScapes pixel-wise annotations based on referring expressions




### Object Categories#

The dataset includes 20 object categories from the SkyScapes dataset:

  * **Vegetation:** low vegetation, tree

  * **Roads:** paved road, non-paved road, bikeway, sidewalk, lane marking

  * **Parking:** paved parking place, non-paved parking place

  * **Vehicles:** car, trailer, van, truck, large truck, bus

  * **Infrastructure:** building, entrance/exit, danger area

  * **Other:** clutter, impervious surface




### Referring Expressions#

Natural language descriptions are generated using templates that include:

  * **Categories:** Direct object names (e.g., âvehicleâ, âroadâ)

  * **Attributes:** Object properties (e.g., âlight-duty vehicleâ, âheavy-duty vehicleâ, âlong truckâ)

  * **Spatial relationships:** Positional descriptions (e.g., âvehicle in the parking areaâ, âlight-duty vehicle driving on the roadâ, âbuilding with a parking lotâ)




Common expressions include: âcarâ, âroadâ, âimpervious surfaceâ, âroad markingâ, âvehicle in the parking areaâ, âbuilding along the roadâ, âsidewalk along with treeâ

### FiftyOne Dataset Structure#

When loaded into FiftyOne, the dataset has the following structure:

**Sample fields:**

  * `filepath`: Absolute path to the image file

  * `tags`: List containing the split name (âtrainâ, âtestâ, or âvalâ)

  * `metadata`: Image metadata (dimensions, size, MIME type)

  * `segmentation`: FiftyOne Segmentation object with absolute path to the mask file

  * `phrase`: String containing the natural language referring expression

  * `created_at`: Timestamp of sample creation

  * `last_modified_at`: Timestamp of last modification




## Dataset Creation#

### Curation Rationale#

The RefSegRS dataset was created to address the lack of referring image segmentation datasets for remote sensing imagery. While referring image segmentation has been extensively studied for natural images, almost no research attention had been given to this task in the context of remote sensing.

The dataset enables:

  * End users without domain expertise to obtain precise information from remote sensing imagery using natural language

  * Targeted image analysis where users can specify objects of interest based on their individual needs

  * Improved efficiency and user interactivity in remote sensing image interpretation




The dataset specifically addresses challenges unique to remote sensing imagery:

  * Small and scattered objects (vehicles, road markings) that occupy fewer pixels

  * Wide range of object categories in top-down views

  * Objects with great scale variations

  * Spatial relationships between objects in urban scenes




### Source Data#

#### Data Collection and Processing#

**Image Collection:**

  1. Source images from the SkyScapes dataset (16 RGB tiles, each 5616 Ã 3744 pixels, 13 cm spatial resolution)

  2. Crop tiles into 1200 Ã 1200 pixel images using sliding window with 600-pixel stride

  3. Downsample to 512 Ã 512 pixels to match deep neural network input requirements




**Referring Expression Generation:**

  * Expressions generated using predefined templates based on how end users typically refer to objects

  * Templates include: category alone, category with attributes, and spatial relationships with other entities

  * Manual filtering performed to remove uninformative image-language-label triplets




**Mask Generation:**

  1. Pixel-wise annotations sourced from SkyScapes dataset (each pixel labeled with one of 20 classes)

  2. Automatic generation of binary ground truth masks based on natural language expressions

  3. Two types of conceptual relationships established:

     * **Identity:** Direct mapping (e.g., âroad markingâ â¡ âlane markingâ)

     * **Inclusion:** Hierarchical grouping (e.g., âlight-duty vehicleâ includes âcarâ and âvanâ)




#### Who are the source data producers?#

The source imagery comes from the **SkyScapes dataset** , which provides aerial RGB imagery with pixel-wise semantic annotations of urban scenes.

The RefSegRS dataset was curated by researchers at:

  * **Technical University of Munich** (Chair of Data Science in Earth Observation)

  * **Shenzhen University** (College of Civil and Transportation Engineering)

  * **Munich Center for Machine Learning**




### Annotations#

#### Annotation process#

The annotations in RefSegRS consist of two components:

**1\. Segmentation Masks:**

  * Automatically generated from existing SkyScapes pixel-wise semantic annotations

  * Binary masks created by setting pixels within the target category to 1 and outside to 0

  * For composite categories (e.g., âvehicleâ), masks combine multiple sub-categories (âcarâ, âvanâ, âtruckâ, etc.)




**2\. Referring Expressions:**

  * Generated using predefined templates that reflect natural user language patterns

  * Templates incorporate:

    * Category names (direct specification)

    * Attributes (size, type, material properties)

    * Spatial relationships (location, proximity to other objects)

  * Manual filtering applied to remove uninformative or ambiguous triplets

  * Final dataset: 4,420 curated image-language-label triplets




**Quality Control:**

  * Manual review to ensure referring expressions accurately describe the corresponding masks

  * Filtering of uninformative samples to maintain dataset quality




#### Who are the annotators?#

  * **Segmentation masks:** Derived from the SkyScapes datasetâs existing pixel-wise annotations

  * **Referring expressions:** Generated automatically using templates, then manually filtered by the research team at Technical University of Munich




## Citation#

**BibTeX:**
    
    
    @article{yuan2023rrsis,
      title={RRSIS: Referring Remote Sensing Image Segmentation},
      author={Yuan, Zhenghang and Mou, Lichao and Hua, Yuansheng and Zhu, Xiao Xiang},
      journal={arXiv preprint arXiv:2306.08625},
      year={2023}
    }
    

**APA:**

Yuan, Z., Mou, L., Hua, Y., & Zhu, X. X. (2024). RRSIS: Referring Remote Sensing Image Segmentation. _IEEE Transactions on Geoscience and Remote Sensing_. arXiv:2306.08625v2

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
