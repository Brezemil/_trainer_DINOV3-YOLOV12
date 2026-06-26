---
source_url: https://docs.voxel51.com/getting_started/manufacturing/10_ppe_detection.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/10_ppe_detection.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/10_ppe_detection.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/manufacturing/10_ppe_detection.ipynb)

# Exploring Verified Auto Labeling#

Welcome to this hands-on workshop where we will learn how to load and explore datasets using FiftyOne. This notebook will guide you through programmatic interaction via the **FiftyOne SDK** and visualization using the **FiftyOne App**. ![verified_autolabeling](https://cdn.voxel51.com/getting_started_manufacturing/notebook10/verified_autolabeling.webp)

## Learning Objectives:#

  * Load datasets into FiftyOne from different sources.
  * Understand the structure and metadata of datasets.
  * Calculate patches and gain insights using embeddings.
  * Understand what VAL - Verified Auto Labeling means and bring this to the analysis.

In this example, we use dataset loading from directory and a Kaggle dataset. [Dataset Link](https://www.kaggle.com/datasets/mugheesahmad/sh17-dataset-for-ppe-detection) Download, extract and add the dataset in the root folder of this repo. I have called it âppeâ
    
    
    [ ]:
    
    
    
    import fiftyone as fo
    import shutil
    import os
    
    dataset_dir = "ppe"
    
    import fiftyone as fo
    
    import fiftyone as fo
    
    name = "sh17-dataset_FO_patches"
    data_path = "ppe/images"
    labels_path = "ppe/labels"
    classes = [
        "Person",         # 0
        "Ear",            # 1
        "Earmuffs",       # 2
        "Face",           # 3
        "Face-guard",     # 4
        "Face-mask-medical", # 5
        "Foot",           # 6
        "Tools",          # 7
        "Glasses",        # 8
        "Gloves",         # 9
        "Helmet",         # 10
        "Hands",          # 11
        "Head",           # 12
        "Medical-suit",   # 13
        "Shoes",          # 14
        "Safety-suit",    # 15
        "Safety-vest"     # 16
    ]
    
    # Import dataset by explicitly providing paths to the source media and labels
    dataset = fo.Dataset.from_dir(
        dataset_type=fo.types.YOLOv4Dataset,
        data_path=data_path,
        labels_path=labels_path,
        classes=classes,
        name=name,
    )
    
    
    
    [ ]:
    
    
    
    session = fo.launch_app(dataset, auto=False, port= 5152)
    

## Calculate the embeddings of patches and visualize it#

Once you have the dataset in YOLO format FiftyOne will convert the dataset in FiftyOne format and you can calculate the embeddings selecting a model from the Build-In options que have in the FiftyOne Model Zoo. You can select multiple from multiple options, like CLIP, DINOv2, DINOv3, MobileNet, etc. [More about FiftyOne Model Zoo](https://docs.voxel51.com/model_zoo/index.html)
    
    
    [ ]:
    
    
    
    import fiftyone.zoo as foz
    # Specify the field containing the patches (e.g., detections)
    patches_field = "ground_truth"
    
    # Option 1: Use a pre-trained model from the FiftyOne Model Zoo
    model = foz.load_zoo_model("mobilenet-v2-imagenet-torch")
    
    # Compute embeddings for the patches using the specified model
    dataset.compute_patch_embeddings(
        patches_field=patches_field,
        model=model,
        embeddings_field="patches_embedding",
        num_workers=0
        )
    
    
    
    [ ]:
    
    
    
    import fiftyone.brain as fob
    
    fob.compute_visualization(
        dataset,
        patches_field=patches_field,            # your field
        embeddings="patches_embedding",         # patch embedding field
        brain_key="dectection_patch_embeddings",# name for this embedding run
        num_workers=0
    )
    
    
    
    [ ]:
    
    
    
    dataset.persistent=True
    
    
    
    [ ]:
    
    
    
    print(dataset)
    

### Unlock VAL with FiftyOne Enterprise#

Experience the power of VAL (Visual Auto Labeling) with FiftyOne Enterprise!

  * Check the latest blog about VAL [BLOG VAL](https://voxel51.com/blog/zero-shot-auto-labeling-rivals-human-performance#1b3993879a50) to see VAL in action.
  * Want to learn more or get access? [Book a personalized demo](https://voxel51.com/sales) with our Customer Success Teamâtheyâre excited to show you how VAL can accelerate your workflows.
  * Ready to try FiftyOne? [Explore datasets in the cloud](https://try.fiftyone.ai/datasets).


    
    
    [ ]:
    
    
    
    # Open in App (tabs)
    session = fo.launch_app(dataset, port=5151, auto=False)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
