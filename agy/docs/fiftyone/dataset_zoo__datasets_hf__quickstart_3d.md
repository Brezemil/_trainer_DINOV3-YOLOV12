---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/quickstart_3d.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/quickstart-3d)

# Dataset Card for quickstart-3d#

![image/png](https://huggingface.co/datasets/Voxel51/quickstart-3d/resolve/main/dataset_preview.gif)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 200 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/quickstart-3d")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Language(s) (NLP):** en

  * **License:** [More Information Needed]




### Dataset Sources#

  * **Homepage:** https://docs.voxel51.com/user_guide/dataset_zoo/datasets.html#quickstart-3d

  * **Demo:** https://try.fiftyone.ai/datasets/quickstart-3d/samples




## Citation#

**BibTeX:**

@article{moore2020fiftyone, title={FiftyOne}, author={Moore, B. E. and Corso, J. J.}, journal={GitHub. Note: https://github.com/voxel51/fiftyone}, year={2020} }

## Dataset Card Author#

[Jacob Marks](https://huggingface.co/jamarks)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
