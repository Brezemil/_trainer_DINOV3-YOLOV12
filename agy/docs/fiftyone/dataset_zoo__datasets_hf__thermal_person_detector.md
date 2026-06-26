---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/thermal_person_detector.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Thermal-Person-Detector)

# Dataset Card for ThermalPersonDetector#

A thermal image dataset for detecting people in a scene. The dataset contains only one class `person`

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 8778 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("dgural/Thermal-Person-Detector")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

Here are a few use cases for this project:

Sports Analytics: The âPersonDetectionâ model could be used to analyze individual athletesâ performances in various sports such as skateboarding, basketball, or soccer, by detecting and tracking the movements of players.

Surveillance Security: It could be utilized in CCTV systems and security cameras. By recognizing people in real-time, it could alert security personnel when unauthorized individuals are detected in restricted areas.

Social Distancing Detection: In light of the Covid-19 pandemic, this model could be used to enforce social distancing measures by tracking the number of people and their relative distances in public spaces like parks, malls, or transportation systems.

Smart Home Management: It can be deployed in smart homes devices to recognize the home occupants and subsequently adapt the environment to their preferences such as lighting, temperature or even play their favorite music upon entry.

Motion Capture and Gaming: In the gaming and animation industry, this model could be used for real-time motion capture, allowing developers to create more realistic and immersive human characters.

  * **Language(s) (NLP):** en

  * **License:** CC 4.0




## Dataset Structure#

One ground_truth field with a person class

[More Information Needed]

### Source Data#

[Roboflow Univers](https://universe.roboflow.com/smart2/persondection-61bc2)

#### Who are the source data producers?#

[SMART2](https://universe.roboflow.com/smart2)

[More Information Needed]

#### Who are the annotators?#

SMART2

**BibTeX:**
    
    
    @misc{
    persondection-61bc2_dataset,
    title = { PersonDection Dataset },
    type = { Open Source Dataset },
    author = { SMART2 },
    howpublished = { \url{ https://universe.roboflow.com/smart2/persondection-61bc2 } },
    url = { https://universe.roboflow.com/smart2/persondection-61bc2 },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2023 },
    month = { may },
    note = { visited on 2024-07-19 },
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
