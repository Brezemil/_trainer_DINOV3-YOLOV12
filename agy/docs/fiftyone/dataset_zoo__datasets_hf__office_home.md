---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/office_home.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Office-Home)

# Dataset Card for Office-Home#

![image/png](https://huggingface.co/datasets/Voxel51/Office-Home/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 15588 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Office-Home")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

The Office-Home dataset has been created to evaluate domain adaptation algorithms for object recognition using deep learning. It consists of images from 4 different domains: Artistic images, Clip Art, Product images and Real-World images. For each domain, the dataset contains images of 65 object categories found typically in Office and Home settings.

  * **Curated by:** [Jose Eusebio](https://www.linkedin.com/in/jmeusebio)

  * **Language(s) (NLP):** en

  * **License:** other




### Dataset Sources#

  * **Homepage:** https://www.hemanthdv.org/officeHomeDataset.html

  * **Paper:** [Deep Hashing Network for Unsupervised Domain Adaptation](https://openaccess.thecvf.com/content_cvpr_2017/papers/Venkateswara_Deep_Hashing_Network_CVPR_2017_paper.pdf)




## Dataset Creation#

### Source Data#

#### Data Collection and Processing#

The images in the dataset were collected using a python web-crawler that crawled through several search engines and online image directories. This initial run searched for around 120 different objects and produced over 100,000 images across the different categories and domains. These images were then filtered to ensure that the desired object was in the picture. Categories were also filtered to make sure that each category had at least a certain number of images. The latest version of the dataset contains around 15,500 images from 65 different categories.

Domain | Min: # | Min: # | Min: # | Acc.  
---|---|---|---|---  
Art | 15 | 117 (\times) 85 pix. | 4384 (\times) 2686 pix. | 44.99 (\pm) 1.85  
Clipart | 39 | 18 (\times) 18 pix. | 2400 (\times) 2400 pix. | 53.95 (\pm) 1.45  
Product | 38 | 75 (\times) 63 pix. | 2560 (\times) 2560 pix. | 66.41 (\pm) 1.18  
Product | 23 | 88 (\times) 80 pix. | 6500 (\times) 4900 pix. | 59.70 (\pm) 1.04  
  
Caption: Statistics for the Office-Home dataset. Min: # is the minimum number of images of each object for the specified domain. Min: Size and Max: Size are the minimum and maximum image sizes in the domain. Acc: is the classification accuracy using a linear SVM (LIBLINEAR) classifier with 5-fold cross-validation using deep features extracted from the VGG-F deep network.

The 65 object categories in the dataset are:
    
    
    Alarm Clock, Backpack, Batteries, Bed, Bike, Bottle, Bucket, Calculator, Calendar, Candles,
    Chair, Clipboards, Computer, Couch, Curtains, Desk Lamp, Drill, Eraser, Exit Sign, Fan,
    File Cabinet, Flipflops, Flowers, Folder, Fork, Glasses, Hammer, Helmet, Kettle, Keyboard,
    Knives, Lamp Shade, Laptop, Marker, Monitor, Mop, Mouse, Mug, Notebook, Oven, Pan,
    Paper Clip, Pen, Pencil, Postit Notes, Printer, Push Pin, Radio, Refrigerator, ruler,
    Scissors, Screwdriver, Shelf, Sink, Sneakers, Soda, Speaker, Spoon, Table, Telephone,
    Toothbrush, Toys, Trash Can, TV, Webcam
    

## Citation#

**BibTeX:**
    
    
    @inproceedings{venkateswara2017deep,
      title={Deep hashing network for unsupervised domain adaptation},
      author={Venkateswara, Hemanth and Eusebio, Jose and Chakraborty, Shayok and Panchanathan, Sethuraman},
      booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
      pages={5018--5027},
      year={2017}
    }
    

## Fair Use Notice#

This dataset contains some copyrighted material whose use has not been specifically authorized by the copyright owners. In an effort to advance scientific research, we make this material available for academic research. We believe this constitutes a fair use of any such copyrighted material as provided for in section 107 of the US Copyright Law. In accordance with Title 17 U.S.C. Section 107, the material on this site is distributed without profit for non-commercial research and educational purposes. For more information on fair use please click here. If you wish to use copyrighted material on this site or in our dataset for purposes of your own that go beyond non-commercial research and academic purposes, you must obtain permission directly from the copyright owner. (adapted from [Christopher Thomas](http://people.cs.pitt.edu/~chris/photographer/))

## Dataset Card Author#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
