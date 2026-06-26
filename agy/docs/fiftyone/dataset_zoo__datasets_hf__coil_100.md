---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/coil_100.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/COIL-100)

# Dataset Card for COIL-100#

![image/png](https://huggingface.co/datasets/Voxel51/COIL-100/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 7200 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/COIL-100")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

There are 7,200 images of 100 objects. Each object was turned on a turnable through 360 degrees to vary object pose with respect to a fixed color camera. Images of the objects were taken at pose intervals of 5 degrees. This corresponds to 72 poses per object. There images were then size normalized. Objects have a wide variety of complex geometric and reflectance characteristics.

  * **Curated by:** Center for Research on Intelligent Systems at the Department of Computer Science , Columbia University

  * **Language(s) (NLP):** en

  * **License:** apache-2.0




### Dataset Sources [optional]#

  * **Paper:** https://www1.cs.columbia.edu/CAVE/publications/pdfs/Nene_TR96_2.pdf

  * **Homepage:** https://www.cs.columbia.edu/CAVE/software/softlib/coil-100.php




## Uses#

This dataset is intended for non-commercial research purposes only.

### Data Collection and Processing#

COIL-100 was collected by the Center for Research on Intelligent Systems at the Department of Computer Science , Columbia University. The database contains color images of 100 objects. The objects were placed on a motorized turntable against a black background and images were taken at pose internals of 5 degrees. This dataset was used in a real-time 100 object recognition system whereby a system sensor could identify the object and display its angular pose.

## Citation#

**BibTeX:**
    
    
    @article{nene1996columbia,
      title={Columbia object image library (coil-100)},
      author={Nene, Sameer A and Nayar, Shree K and Murase, Hiroshi},
      year={1996},
      publisher={Technical report CUCS-006-96}
    }
    

## Dataset Card Authors#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
