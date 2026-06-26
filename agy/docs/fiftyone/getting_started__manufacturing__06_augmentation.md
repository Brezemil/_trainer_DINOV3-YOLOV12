---
source_url: https://docs.voxel51.com/getting_started/manufacturing/06_augmentation.html
---

[ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/06_augmentation.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/06_augmentation.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/manufacturing/06_augmentation.ipynb)

# Albumentations Integration for Anomaly Detection#

In this notebook, we will explore **FiftyOneâs integration with Albumentations** , a powerful image augmentation library. Augmentations can significantly enhance **anomaly detection** models by improving robustness and generalization. ![albumentation](https://cdn.voxel51.com/getting_started_manufacturing/notebook6/albumentation.webp)

## Learning Objectives:#

  * Understand the importance of **data augmentation** for anomaly detection.
  * Use **Albumentations** to apply transformations to datasets in FiftyOne.
  * Explore different augmentation techniques for improving model performance.



## Why Use Augmentations for Anomaly Detection?#

Anomaly detection models often struggle due to **limited data availability** and **environmental variations**. Data augmentation helps by:

  * **Simulating real-world variations** (e.g., lighting changes, noise, blur).
  * **Increasing dataset diversity** , reducing overfitting.
  * **Improving model robustness** to unseen conditions.

Albumentations allows us to apply **realistic transformations** , such as:

  * **Brightness and contrast adjustments** (simulate different lighting conditions).
  * **Color jittering** (alter hue, saturation, and intensity).
  * **Gaussian noise, blur, and distortions** (improve generalization).

**Relevant Documentation:**

  * [Albumentations Documentation](https://albumentations.ai/docs/)
  * [Why Data Augmentation Matters](https://docs.voxel51.com/integrations/albumentations.html)


    
    
    [ ]:
    
    
    
    !pip install -U albumentations==1.4.24 fiftyone
    
    
    
    [ ]:
    
    
    
    !fiftyone plugins download https://github.com/jacobmarks/fiftyone-albumentations-plugin
    
    
    
    [ ]:
    
    
    
    import gdown
    
    url = "https://drive.google.com/uc?id=1nAuFIyl2kM-TQXduSJ9Fe_ZEIVog4tth" # original
    gdown.download(url, output="mvtec_ad.zip", quiet=False)
    
    !unzip mvtec_ad.zip
    
    import fiftyone as fo
    
    dataset_name = "MVTec_AD"
    
    # Check if the dataset exists
    if dataset_name in fo.list_datasets():
        print(f"Dataset '{dataset_name}' exists. Loading...")
        dataset = fo.load_dataset(dataset_name)
    else:
        print(f"Dataset '{dataset_name}' does not exist. Creating a new one...")
        dataset_ = fo.Dataset.from_dir(
            dataset_dir="/content/mvtec-ad",
            dataset_type=fo.types.FiftyOneDataset
        )
        dataset = dataset_.clone("MVTec_AD")
    
    
    
    [ ]:
    
    
    
    # Try this for already loaded dataset
    # dataset = fo.load_dataset('mvtec-ad-staging')
    OBJECTS_LIST = [
        'pill',
        'zipper',
        'tile',
        'bottle',
        'transistor',
        'wood',
        'cable',
        'capsule',
        'carpet',
        'grid',
        'hazelnut',
        'leather',
        'metal_nut',
        'screw',
        'toothbrush'
    ]
    OBJECT = "screw" ## object to select
    
    
    
    [ ]:
    
    
    
    from fiftyone import ViewField as F # helper for defining views
    
    # Define the new dataset name for split set
    dataset_name_split = "mvtec-screw"
    
    if dataset_name_split in fo.list_datasets():
        print(f"Dataset '{dataset_name_split}' exists. Loading...")
        mvtec_screw = fo.load_dataset(dataset_name_split)
    else:
        print(f"Dataset '{dataset_name_split}' does not exist. Creating a new one...")
        ## get the test split of the dataset
        test_split = dataset.match(F("category.label") == 'screw')
    
        # Clone the dataset into a new one called "mvtec_bottle"
        mvtec_screw = test_split.clone("mvtec-screw", persistent=True)
    
    
    
    [ ]:
    
    
    
    print(mvtec_screw)
    
    
    
    [ ]:
    
    
    
    session = fo.launch_app(mvtec_screw, port=5156, auto=False)
    print(session.url)
    

### How to manipulate Plugins#

[Here](https://docs.voxel51.com/plugins/using_plugins.html#managing-plugins) is a guide you can follow to check your plugins, enable, disable or delete those. IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
