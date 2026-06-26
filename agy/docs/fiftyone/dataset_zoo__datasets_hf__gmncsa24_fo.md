---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/gmncsa24_fo.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/GMNCSA24-FO)

# Dataset Card for Elderly Action Recognition Challenge#

This dataset is a modified version of the GMNCSA24 dataset, tailored for video classification tasks focusing on Activities of Daily Living (ADL) and fall detection in older populations. It is designed to support research in human activity recognition and safety monitoring. The dataset includes annotated video samples for various ADL and fall scenarios, making it ideal for training and evaluating machine learning models in healthcare and assistive technology applications.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63f516f6b51da4d61da6bca8/YsJoRwVLM3lqmzuyyZILR.png)

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 335 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    from fiftyone.utils.huggingface import load_from_hub
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = load_from_hub("Voxel51/GMNCSA24-FO")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

  * **Original Dataset:** [GMNCSA24 Repo](https://github.com/ekramalam/GMDCSA24-A-Dataset-for-Human-Fall-Detection-in-Videos/blob/master/LICENSE)

  * **Curated by:** [Paula Ramos](https://huggingface.co/pjramg)

  * **Language(s):** en

  * **License:** [MIT License]




### Dataset Sources [optional]#

  * **Repository:** [https://github.com/ekramalam/GMDCSA24-A-Dataset-for-Human-Fall-Detection-in-Videos]

  * **Paper [optional]:** [E. Alam, A. Sufian, P. Dutta, M. Leo, I. A. Hameed âGMDCSA24: A Dataset for Human Fall Detection in Videosâ, Data in Brief (communicated)]

  * **Blog [optional]:** [Journey with FiftyOn: Part III](https://medium.com/@paularamos_phd/journey-into-visual-ai-exploring-fiftyone-together-part-iii-preparing-a-computer-vision-e5709684ee34)

  * **Notebook:** [fiftyOne Example](https://github.com/voxel51/fiftyone-examples/blob/master/examples/elderly_action_recognition.ipynb)

  * **Readme_DataPrepartation** [Awesome_FiftyOne](https://github.com/paularamo/awesome-fiftyone/tree/main/ear-challenge)




## Uses#

[Elderly Action Recognition Challenge](https://voxel51.com/computer-vision-events/elderly-action-recognition-challenge-wacv-2025/)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
