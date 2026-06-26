---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/describable_textures_dataset.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Describable-Textures-Dataset)

# Dataset Card for Describable Textures Dataset#

![image/png](https://huggingface.co/datasets/Voxel51/Describable-Textures-Dataset/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 5640 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Describable-Textures-Dataset")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

âOur ability of vividly describing the content of images is a clear demonstration of the power of human visual system. Not only we can recognise objects in images (e.g. a cat, a person, or a car), but we can also describe them to the most minute details, extracting an impressive amount of information at a glance. But visual perception is not limited to the recognition and description of objects. Prior to high-level semantic understanding, most textural patterns elicit a rich array of visual impressions. We could describe a texture as âpolka dotted, regular, sparse, with blue dots on a white backgroundâ; or as ânoisy, line-like, and irregularâ.

Our aim is to reproduce this capability in machines. Scientifically, the aim is to gain further insight in how textural information may be processed, analysed, and represented by an intelligent system. Compared to classic task of textural analysis such as material recognition, such perceptual properties are much richer in variety and structure, inviting new technical challenges.

DTD is a texture database, consisting of 5640 images, organized according to a list of 47 terms (categories) inspired from human perception. There are 120 images for each category. Image sizes range between 300x300 and 640x640, and the images contain at least 90% of the surface representing the category attribute. The images were collected from Google and Flickr by entering our proposed attributes and related terms as search queries. The images were annotated using Amazon Mechanical Turk in several iterations. For each image we provide key attribute (main category) and a list of joint attributes.

The data is split in three equal parts, in train, validation and test, 40 images per class, for each split. We provide the ground truth annotation for both key and joint attributes, as well as the 10 splits of the data we used for evaluation.â

  * **Curated by:** M.Cimpoi, S. Maji, I. Kokkinos, S. Mohamed, A. Vedaldi,

  * **Funded by:** NSF Grant #1005411, JHU-HLTCOE, Google Research, ERC grant VisRec no. 228180, ANR-10-JCJC-0205

  * **Language(s) (NLP):** en

  * **License:** other




### Dataset Sources#

  * **Homepage:** https://www.robots.ox.ac.uk/~vgg/data/dtd/

  * **Paper:** https://www.robots.ox.ac.uk/~vgg/publications/2014/Cimpoi14/cimpoi14.pdf

  * **Demo:** https://try.fiftyone.ai/datasets/describable-textures-dataset/samples




## Dataset Creation#

### Curation Rationale#

âPatterns and textures are key characteristics of many natural objects: a shirt can be striped, the wings of a butterfly can be veined, and the skin of an animal can be scaly. Aiming at supporting this dimension in image understanding, we address the problem of describing textures with semantic attributes. We identify a vocabulary of forty-seven texture terms and use them to describe a large dataset of patterns collected âin the wildâ. The resulting Describable Textures Dataset (DTD) is a basis to seek the best representation for recognizing describable texture attributes in images. â - dataset authors

### Source Data#

Google and Flickr

## Citation#

**BibTeX:**
    
    
    @InProceedings{cimpoi14describing,
    	      Author    = {M. Cimpoi and S. Maji and I. Kokkinos and S. Mohamed and and A. Vedaldi},
    	      Title     = {Describing Textures in the Wild},
    	      Booktitle = {Proceedings of the {IEEE} Conf. on Computer Vision and Pattern Recognition ({CVPR})},
    	      Year      = {2014}}
    

## More Information#

This research is based on work done at the 2012 CLSP Summer Workshop, and was partially supported by NSF Grant #1005411, ODNI via the JHU-HLTCOE and Google Research. Mircea Cimpoi was supported by the ERC grant VisRec no. 228180 and Iasonas Kokkinos by ANR-10-JCJC-0205.

The development of the describable textures dataset started in June and July 2012 at the Johns Hopkins Centre for Language and Speech Processing (CLSP) Summer Workshop. The authors are most grateful to Prof. Sanjeev Khudanpur and Prof. Greg Hager.

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
