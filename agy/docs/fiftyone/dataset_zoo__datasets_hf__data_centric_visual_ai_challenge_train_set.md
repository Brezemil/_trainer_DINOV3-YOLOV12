---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/data_centric_visual_ai_challenge_train_set.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/Data-Centric-Visual-AI-Challenge-Train-Set)

# Dataset Card for Data-Centric-Visual-AI-Train-Set#

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 30,000 samples.

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/Data-Centric-Visual-AI-Challenge-Train-Set")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

# Dataset Overview#

Welcome to our Data Curation Challenge for Object Detection! This page provides essential information about the dataset youâll be working with.

These images are a subset from [Open Images v7 ](https://storage.googleapis.com/openimages/web/factsfigures_v7.html).

Full information about the dataset can be found [here](https://storage.googleapis.com/openimages/web/download_v7.html).

## Dataset Description#

Our dataset is a custom collection of images specifically curated for this competition. It focuses on everyday objects, people, and transportation, with a particular emphasis on clothing and accessories.

Key details:

  * Total images: 30,000

  * Image format: JPEG

  * Annotation format: FiftyOne detection format




## Object Classes#

The dataset includes 25 object classes across several categories:

  1. Transportation: Airplane, Truck, Van, Ambulance, Helicopter, Motorcycle, Bicycle, Unicycle, Bus, Taxi, Balloon

  2. Electronics: Computer monitor, Laptop, Mobile phone, Tablet phone

  3. Sports Equipment: Tennis ball, Tennis racket, Table tennis racket, Golf ball, Ball, Rugby ball, Football, Kite, Volleyball (Ball)

  4. Food: Hamburger, Hot dog




## Annotations#

Each image in the dataset comes with detailed annotations in FiftyOne detection format. A typical annotation looks like this:
    
    
    <Detection: {
        'id': '66a037ceef34f40a421a9810',
        'attributes': {},
        'tags': [],
        'label': 'Jeans',
        'bounding_box': [0.446875, 0.36773, 0.16562500000000002, 0.321763],
        'mask': None,
        'confidence': None,
        'index': None,
        'IsOccluded': True,
        'IsTruncated': False,
        'IsGroupOf': False,
        'IsDepiction': False,
        'IsInside': False,
    }>
    

Key annotation features:

  * Bounding box coordinates (normalized)

  * Object class labels

  * Occlusion and truncation flags

  * Group, depiction, and inside flags




## Your Task#

Your challenge is to curate a subset of this dataset that:

  1. Reduces the overall size of the dataset

  2. Maintains or improves the performance of an object detection model (YOLOv8m)




Remember, the goal is to find the optimal balance between dataset size and model performance, as measured by our evaluation metric:

Score = (mAP * log(N)) / N

Where mAP is the Mean Average Precision on our hidden test set, and N is the number of images in your curated dataset.

## Additional Notes#

  * Ensure you comply with all dataset usage terms and conditions

  * Do not use external data sources for this challenge




Good luck, and happy curating!

## Citations#

The Open Images v4 paper can be found [here](https://arxiv.org/abs/1811.00982)
    
    
    @article{OpenImages,
      author = {Alina Kuznetsova and Hassan Rom and Neil Alldrin and Jasper Uijlings and Ivan Krasin and Jordi Pont-Tuset and Shahab Kamali and Stefan Popov and Matteo Malloci and Alexander Kolesnikov and Tom Duerig and Vittorio Ferrari},
      title = {Open Images Dataset V6: A Large-Scale Dataset for Object Detection in the Wild.}, {Open Images Dataset V7: A Large-Scale Dataset for Object Detection in the Wild.}
      year = {2020},
      journal = {IJCV}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
