---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/sku110k_test.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/sku110k_test)

# Dataset Card for harpreetsahota/sku110k_test#

![image](https://huggingface.co/datasets/Voxel51/sku110k_test/resolve/main/sku110k.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 2936 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/sku110k_test")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Card for SKU-110K (test split)#

## Dataset Details#

### Dataset Description#

The SKU-110K dataset is a large-scale benchmark for object detection in densely packed retail scenes. It consists of 11,762 images of retail shelves from thousands of supermarkets worldwide, encompassing diverse geographic locations including the United States, Europe, and East Asia. The dataset contains over 1.73 million bounding box annotations, with an average of approximately 147 objects per image. All images have been resized to a resolution of one million pixels.

The dataset addresses the challenge of precise detection in densely packed scenes where objects are closely positioned, often overlapping, and typically oriented within a range of [-15Â°, 15Â°]. This makes it particularly valuable for developing and evaluating object detection algorithms for real-world retail applications where traditional detection methods often struggle due to extreme object density and occlusion.

  * **Curated by:** Eran Goldman, Roei Herzig, Aviv Eisenschtat, Jacob Goldberger, and Tal Hassner

  * **Funded by:** Trax (based on license information)

  * **Shared by:** Research team from Bar-Ilan University and Trax

  * **Language(s) (NLP):** Not applicable (computer vision dataset)

  * **License:** Academic and non-commercial use only (proprietary license by Trax)




### Dataset Sources#

  * **Repository:** https://github.com/eg4000/SKU110K_CVPR19

  * **Paper:** âPrecise Detection in Densely Packed Scenesâ - CVPR 2019

  * **ArXiv:** https://arxiv.org/abs/1904.00853




## Uses#

### Direct Use#

The SKU-110K dataset is designed for the following use cases:

  * **Object Detection Research:** Training and evaluating object detection models, particularly for densely packed scenes

  * **Retail Analytics:** Developing algorithms for automated shelf monitoring, inventory management, and planogram compliance

  * **Benchmark Evaluation:** Comparing performance of detection algorithms in challenging, high-density scenarios

  * **Dense Object Detection:** Research on handling extreme object density, occlusion, and scale variation

  * **Academic Research:** Educational purposes and non-commercial research projects




The dataset is particularly suitable for:

  * Studying detection performance in scenes with 50-200+ objects per image

  * Developing algorithms robust to varying lighting conditions, viewpoints, and scales

  * Research on handling closely packed objects with minimal spacing




## Dataset Structure#

The dataset is organized into three splits with CSV annotation files:

### Split Statistics#

Split | Images | Annotations | Avg. Objects/Image  
---|---|---|---  
Train | 8,233 | 1,208,482 | ~147  
Validation | 588 | 90,968 | ~155  
Test | 2,941 | 431,546 | ~147  
**Total** | **11,762** | **1,730,996** | **~147**  
  
### Annotation Format#

The CSV annotation files contain the following columns:

  * `image_name`: Filename of the image (e.g., âtest_0.jpgâ)

  * `x1`: X-coordinate of the top-left corner of the bounding box (pixels)

  * `y1`: Y-coordinate of the top-left corner of the bounding box (pixels)

  * `x2`: X-coordinate of the bottom-right corner of the bounding box (pixels)

  * `y2`: Y-coordinate of the bottom-right corner of the bounding box (pixels)

  * `class`: Class label (all objects labeled as âobjectâ - no fine-grained categories)

  * `image_width`: Width of the image in pixels

  * `image_height`: Height of the image in pixels




**Note:** Each annotation appears on a separate line in the CSV file, meaning images with multiple objects have multiple rows.

### FiftyOne Dataset Structure#

The dataset has been converted to FiftyOne format with the following enhancements:

#### Base Structure#

  * **Dataset Name:** `sku110k_test` (test split)

  * **Sample Structure:** Each sample represents one image with associated detections

  * **Image Path:** `SKU110K_fixed/images/{image_name}`

  * **Detection Field:** `ground_truth` (FiftyOne Detections object)




#### Bounding Box Format#

Bounding boxes are stored in FiftyOneâs normalized format:

  * `[x, y, width, height]` where all values are in range [0, 1]

  * `x`: Normalized x-coordinate of top-left corner (x1 / image_width)

  * `y`: Normalized y-coordinate of top-left corner (y1 / image_height)

  * `width`: Normalized width ((x2 - x1) / image_width)

  * `height`: Normalized height ((y2 - y1) / image_height)




#### Enriched Fields#

The FiftyOne dataset includes the following enrichments:

  1. **Bounding Box Areas** (`area` field on each detection)

     * Computed as: `width Ã height` (in normalized coordinates)

     * Range: [0, 1] representing the proportion of image covered

  2. **Detection Counts** (`num_detections` field at sample level)

     * Integer count of objects detected in each image

     * Useful for filtering and analyzing image complexity

  3. **RADIO Embeddings** (`radio_embeddings` field at sample level)

     * Global semantic features extracted using C-RADIO v3-h model

     * High-dimensional vectors capturing visual semantics

     * Enables similarity search and clustering

  4. **UMAP Visualization** (Brain key: `radio_viz`)

     * 2D projection of RADIO embeddings for visualization

     * Allows exploration of visual similarity patterns

     * Interactive visualization in FiftyOne App

  5. **Attention Heatmaps** (`radio_heatmap` field at sample level)

     * Spatial attention maps from C-RADIO v3-h model

     * Generated with smoothing (sigma=0.51)

     * Format: NCHW (channels first)

     * Highlights salient regions in each image




## Dataset Creation#

### Curation Rationale#

The SKU-110K dataset was created to address a critical gap in object detection research: the lack of large-scale datasets for densely packed scenes. While existing datasets like COCO and Pascal VOC contain object detection annotations, they typically feature relatively sparse scenes with well-separated objects. Real-world retail environments present unique challenges:

  * **Extreme Density:** Shelves contain 50-200+ products in close proximity

  * **Heavy Occlusion:** Objects frequently overlap and obscure one another

  * **Scale Variation:** Products vary greatly in size within the same scene

  * **Orientation Patterns:** Most objects aligned within [-15Â°, 15Â°] range




The dataset enables research on precise localization and detection algorithms capable of handling these challenging conditions, with applications in automated retail analytics, inventory management, and planogram compliance.

### Source Data#

#### Data Collection and Processing#

  * **Collection Method:** Images captured from thousands of supermarket stores worldwide

  * **Geographic Diversity:** United States, Europe, and East Asia

  * **Scene Variation:** Diverse scales, viewpoints, lighting conditions, and noise levels

  * **Image Processing:** All images resized to one million pixels for consistency

  * **Quality Control:** Images selected to represent challenging, densely packed scenarios

  * **Annotation Tool:** Manual annotation using bounding box annotation software

  * **Format:** CSV files with one annotation per line




The dataset focuses on âin-the-wildâ conditions with natural variations in:

  * Camera angles and distances

  * Lighting (fluorescent, natural, mixed)

  * Shelf arrangements and product placement

  * Image quality and noise levels




#### Who are the source data producers?#

The source images were captured from retail stores operated by various supermarket chains across multiple continents. The images represent real retail environments and were collected through Trax, a retail technology company specializing in computer vision solutions for in-store execution.

### Annotations#

#### Annotation process#

  * **Annotation Type:** Manual bounding box annotation

  * **Annotation Guidelines:** Annotators were instructed to draw tight bounding boxes around each visible product on retail shelves

  * **Class Labels:** All objects labeled uniformly as âobjectâ (no product-level categorization)

  * **Annotation Density:** Average of 147 bounding boxes per image, with some images containing 200+ annotations

  * **Quality Assurance:** Manual review and validation process to ensure annotation accuracy

  * **Tools Used:** Professional annotation tools for computer vision tasks

  * **Completeness:** All visible products in each image were annotated




**Note:** The dataset does not include fine-grained product categories or SKU-level identification. All objects are labeled with a single âobjectâ class, making this a class-agnostic detection task focused on localization precision rather than classification.

#### Who are the annotators?#

The annotations were created by trained professional annotators working with the research team. Specific demographic information about the annotators is not publicly available. The annotation process was conducted with quality control measures to ensure consistency and accuracy across the large annotation volume (1.7M+ bounding boxes).

#### Personal and Sensitive Information#

The dataset consists of images of retail shelf scenes containing packaged products. The images do not intentionally capture or focus on people. However, users should be aware that:

  * Retail environments are public spaces where incidental capture of individuals may occur

  * Product brands and packaging visible in images are proprietary to their respective manufacturers

  * Store layouts and product arrangements may be considered proprietary information




The dataset is provided with restrictions on redistribution and commercial use to protect potential proprietary interests.

## Citation#

### BibTeX#
    
    
    @inproceedings{goldman2019dense,
      author    = {Eran Goldman and Roei Herzig and Aviv Eisenschtat and Jacob Goldberger and Tal Hassner},
      title     = {Precise Detection in Densely Packed Scenes},
      booktitle = {Proc. Conf. Comput. Vision Pattern Recognition (CVPR)},
      year      = {2019}
    }
    

### APA#

Goldman, E., Herzig, R., Eisenschtat, A., Goldberger, J., & Hassner, T. (2019). Precise Detection in Densely Packed Scenes. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ (pp. 5227-5236).

## More Information#

### Additional Resources#

  * **GitHub Repository:** https://github.com/eg4000/SKU110K_CVPR19

  * **ArXiv Paper:** https://arxiv.org/abs/1904.00853

  * **FiftyOne Documentation:** https://docs.voxel51.com/

  * **RADIO Model:** https://github.com/harpreetsahota204/NVLabs_CRADIOV3




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
