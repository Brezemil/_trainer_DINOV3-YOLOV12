---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/kolektor_surface_defect.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Kolektor_Surface_Defect)

# Dataset Card for Kolektor Surface-Defect Dataset#

![image/png](https://huggingface.co/datasets/Voxel51/Kolektor_Surface_Defect/resolve/main/kolektorsdd.png)

KolektorSDD (Kolektor Surface-Defect Dataset) is a grayscale industrial surface-inspection dataset of electrical commutators.

This FiftyOne dataset uses the **box-annotation release** intended for the ICPR 2021 and COMIND 2021 papers ([download](https://go.vicos.si/kolektorsddboxes)): one sample per surface image, with defect regions annotated as axis-aligned bounding boxes stored as filled rectangles in the label masks.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 399 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/Kolektor_Surface_Defect")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

  * **Curated by:** Domen Tabernik, Samo Å ela, Jure SkvarÄ, Danijel SkoÄaj (University of Ljubljana / ViCoS Lab); images provided and annotated by Kolektor Group d.o.o.

  * **Paper (dataset):** [Segmentation-Based Deep-Learning Approach for Surface-Defect Detection](https://doi.org/10.1007/s10845-019-01476-x)

  * **Box annotations used in:** [End-to-end training of a two-stage neural network for defect detection](https://arxiv.org/abs/2007.07676) (ICPR 2020) and [Mixed supervision for surface-defect detection](http://prints.vicos.si/publications/385) (Computers in Industry, 2021)

  * **Project page:** https://www.vicos.si/resources/kolektorsdd/

  * **Download (this release):** https://go.vicos.si/kolektorsddboxes

  * **License:** [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/) (non-commercial; contact [Danijel SkoÄaj](https://www.vicos.si/people/danijel_skocaj/) for commercial use)




### What the data contains#

Images were captured in a controlled industrial environment. Each sample is one non-overlapping view of a commutator surface. Defects are microscopic fractures or cracks in the plastic embedding.

Property | Value  
---|---  
Total images | 399  
Physical items (boards) | 50 (`kos01`â`kos50`)  
Surfaces per item | 8 (`Part0`â`Part7`)  
Defective images | 52  
Non-defective images | 347  
Image type | Grayscale JPG  
Original size | 500 px wide Ã 1240â1270 px tall  
Recommended eval size | 512 Ã 1408 px (per dataset authors)  
  
Defect visibility: for 48 items the defect appears in exactly one image; for 2 items it appears in two images.

A separate **fine pixel-annotation release** exists for the JIM2019 paper ([download](https://go.vicos.si/kolektorsdd)). That version is not what this card describes.

### Raw download layout#
    
    
    kolektorsdd/
      kos01/
        Part0.jpg
        Part0_label.bmp
        Part1.jpg
        Part1_label.bmp
        ...
      kos02/
        ...
    

  * `Part*.jpg` â surface image

  * `Part*_label.bmp` â defect annotation mask (non-zero = defect region)




In this box-annotation release, each defective mask is a **filled axis-aligned bounding box** around the defect, not a precise pixel-wise segmentation of the crack shape.

### Train/test splits#

The authors evaluate with **3-fold cross-validation** , keeping all 8 images of the same physical item in the same fold. Official split files: [KolektorSDD-training-splits.zip](https://data.vicos.si/datasets/KSDD/KolektorSDD-training-splits.zip).

This FiftyOne dataset does **not** assign fold/split labels. Add them externally if needed.

* * *

## FiftyOne Dataset Structure#

Property | Value  
---|---  
Hub dataset | `harpreetsahota/Kolektor_Surface_Defect`  
Local dataset name | `kolektorsdd`  
Media type | `image`  
Samples | 399  
  
### Sample fields#

Field | Type | Description  
---|---|---  
`filepath` | `StringField` | Path to source `Part*.jpg`  
`board_id` | `StringField` | Board directory name, e.g. `"kos01"`  
`has_defect` | `BooleanField` | `True` if the mask contains any foreground pixel  
`ground_truth` | `EmbeddedDocumentField(Segmentation)` | Binarized mask (`0` = background, `1` = defect)  
  
The local parser (`parse_to_fo.py`) reads each BMP label and stores a `{0, 1}` mask on the sample. For defective images in this release, the foreground region is a filled bounding box rather than a tight defect outline.

* * *

## Citation#

**BibTeX (dataset):**
    
    
    @article{Tabernik2019JIM,
      author  = {Tabernik, Domen and {\v{S}}ela, Samo and Skvar{\v{c}}, Jure and Sko{\v{c}}aj, Danijel},
      journal = {Journal of Intelligent Manufacturing},
      title   = {{Segmentation-Based Deep-Learning Approach for Surface-Defect Detection}},
      year    = {2019},
      month   = {May},
      day     = {15},
      issn    = {1572-8145},
      doi     = {10.1007/s10845-019-01476-x}
    }
    

**BibTeX (box annotations / mixed supervision):**
    
    
    @article{Bozic2021COMIND,
      author  = {Bo{\v{z}}i{\v{c}}, Jakob and Tabernik, Domen and Sko{\v{c}}aj, Danijel},
      journal = {Computers in Industry},
      title   = {{Mixed supervision for surface-defect detection: from weakly to fully supervised learning}},
      year    = {2021}
    }
    

**APA:**

Tabernik, D., Å ela, S., SkvarÄ, J., & SkoÄaj, D. (2019). Segmentation-Based Deep-Learning Approach for Surface-Defect Detection. _Journal of Intelligent Manufacturing_. https://doi.org/10.1007/s10845-019-01476-x

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
