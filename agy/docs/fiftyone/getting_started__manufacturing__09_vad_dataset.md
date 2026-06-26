---
source_url: https://docs.voxel51.com/getting_started/manufacturing/09_vad_dataset.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/09_vad_dataset.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/09_vad_dataset.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/manufacturing/09_vad_dataset.ipynb)

# Loading and Exploring Datasets#

[Explore more about VAD](https://github.com/abc-125/vad?tab=readme-ov-file) Welcome to this hands-on workshop where we will learn how to load and explore datasets using FiftyOne. This notebook will guide you through programmatic interaction via the **FiftyOne SDK** and visualization using the **FiftyOne App**. ![vad-image](https://cdn.voxel51.com/getting_started_manufacturing/notebook9/vad-image.webp)

## Learning Objectives:#

  * Load datasets into FiftyOne from different sources.
  * Understand the structure and metadata of datasets.
  * Use FiftyOneâs querying and filtering capabilities.
  * Interactively explore datasets in the FiftyOne App.

In this example, we use Hugging Face Hub for dataset loading, but you are encouraged to explore other sources like local files, cloud storage, or custom dataset loaders.

## In this notebook, we covered:#

  1. Loading datasets from Hugging Face Hub (extendable to other sources).
  2. Exploring dataset structure and metadata.
  3. Applying filtering and querying techniques to analyze data.
  4. Utilizing the FiftyOne App for interactive visualization.
  5. Clone dataset views and export your Data in FiftyOne Format



## Requirements and FiftyOne Installation#

First thing you need to do is create a Python environment in your system, if you are not familiar with that please take a look of this [ReadmeFile](https://github.com/voxel51/fiftyone-examples?tab=readme-ov-file#-prerequisites-for-beginners-), where we will explain how to create the environment. After that be sure you activate the created environment and install FiftyOne there.

## Install FiftyOne#
    
    
    [ ]:
    
    
    
    !pip install fiftyone huggingface_hub gdown
    

## Loading a Dataset into FiftyOne#

### Alternative - Download from Google Drive#

If you find any issues downloading the dataset from Hugging Face, please uncomment and use the following code cell.
    
    
    [ ]:
    
    
    
    import gdown
    # Download the coffee dataset from Google Drive
    url = "https://drive.google.com/uc?id=1LbHHJHCdkvhzVqekAIRdWjBWaBHxPjuu"
    
    gdown.download(url, output="vad.zip", quiet=False)
    !unzip vad.zip
    
    
    
    [ ]:
    
    
    
    import os
    import fiftyone as fo
    import fiftyone.utils.data as foud
    from fiftyone import Sample
    from pathlib import Path
    
    # Path to your dataset root (adjust if necessary)
    DATASET_DIR = "vad"
    
    # Create or load a FiftyOne dataset
    dataset_name = "vad-dataset"
    if dataset_name in fo.list_datasets():
        fo.delete_dataset(dataset_name)
    
    dataset = fo.Dataset(dataset_name)
    
    # Helper: load all images with metadata from dir structure
    def add_samples_from_dir(dataset, root_dir):
        for split in ["train", "test"]:
            split_dir = Path(root_dir) / split
            for label in os.listdir(split_dir):
                label_dir = split_dir / label
                if not label_dir.is_dir():
                    continue
    
                for img_file in label_dir.glob("*"):
                    if img_file.suffix.lower() not in [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"]:
                        continue
    
                    sample = Sample(
                        filepath=str(img_file.resolve()),
                        metadata=None,  # will be auto-populated
                        tags=[split],
                    )
                    sample["split"] = split
                    sample["label"] = label
                    dataset.add_sample(sample)
    
    # Ingest all samples
    add_samples_from_dir(dataset, DATASET_DIR)
    
    # Optionally compute metadata (dimensions, etc.)
    dataset.compute_metadata()
    
    
    
    [ ]:
    
    
    
    # Launch the FiftyOne App
    session = fo.launch_app(dataset, port= 5152, auto=False)
    
    
    
    [ ]:
    
    
    
    # Convert `label` string field to a proper Classification label
    for sample in dataset:
        sample["ground_truth"] = fo.Classification(label=sample["label"])
        sample.save()
    
    # Optionally delete the old string label field if not needed
    # dataset.delete_sample_field("label")
    
    # Refresh the app session
    session.refresh()
    
    
    
    [ ]:
    
    
    
    dataset.persistent = True
    

## Exploring the Dataset#

Once the dataset is loaded, we can inspect its structure using FiftyOneâs SDK. We will explore:

  * The number of samples in the dataset.
  * Available metadata and labels.
  * How images/videos are structured.

**Relevant Documentation:** [Inspecting Datasets in FiftyOne](https://docs.voxel51.com/user_guide/using_datasets.html#using-fiftyone-datasets) You can also call the [first Sample](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.first) of the Dataset to see what the Fields looks like:
    
    
    [ ]:
    
    
    
    print(dataset)
    print(dataset.first())  # Inspect the first or last sample
    

## Querying and Filtering#

FiftyOne provides a powerful querying engine to filter and analyze datasets efficiently. We can apply filters to:

  * Retrieve specific labels (e.g., all images with âcatâ labels).
  * Apply confidence thresholds to object detections.
  * Filter data based on metadata (e.g., image size, timestamp).

**Relevant Documentation:** [Dataset views](https://docs.voxel51.com/user_guide/using_views.html#dataset-views), [Querying Samples](https://docs.voxel51.com/user_guide/using_views.html#querying-samples), [Common filters](https://docs.voxel51.com/user_guide/using_views.html#common-filters)

### Examples:#

  * Show all images containing a particular class.
  * Retrieve samples with object detection confidence above a threshold.
  * Filter out low-quality images based on metadata.


    
    
    [ ]:
    
    
    
    import fiftyone.core.expressions as foe
    
    # Query images where the defect is labeled as "scratch"
    view = dataset.match(foe.ViewField("split") == "test")
    print(view)
    
    # Launch FiftyOne App with the filtered dataset
    session = fo.launch_app(view, port=5152, auto=False)
    
    
    
    [ ]:
    
    
    
    filter = view.match(foe.ViewField("ground_truth.label") == "bad_unseen_defects")
    session.view = filter
    print(filter)
    
    
    
    [ ]:
    
    
    
    # Launch FiftyOne App with the filtered dataset
    session = fo.launch_app(filter, port=5152, auto=False)
    

## Interactive Exploration with the FiftyOne App#

The **FiftyOne App** allows users to interactively browse, filter, and analyze datasets. This visual interface is an essential tool for understanding dataset composition and refining data exploration workflows. Key features of the FiftyOne App:

  * Interactive filtering of images/videos.
  * Object detection visualization.
  * Dataset statistics and metadata overview.

**Relevant Documentation:** [Using the FiftyOne App](https://voxel51.com/docs/fiftyone/user_guide/app.html)

### Intereacting with Plugins to understand the dataset#

FiftyOne provides a powerful [plugin framework](https://docs.voxel51.com/plugins/index.html) that allows for extending and customizing the functionality of the tool to suit your specific needs. In this case we will use the [@voxel51/dashboard](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/dashboard/README.md) plugin, a plugin that enables users to construct custom dashboards that display statistics of interest about the current dataset (and beyond)
    
    
    [ ]:
    
    
    
    !fiftyone plugins download https://github.com/voxel51/fiftyone-plugins --plugin-names @voxel51/dashboard
    

## New dataset#

Creates a new dataset containing a copy of the contents of the view.
    
    
    [ ]:
    
    
    
    new_dataset= view.clone()
    print(new_dataset)
    

## Exporting Dataset to FiftyOneDataset#

FiftyOne supports various dataset formats. In this notebook, weâve worked with a custom dataset from Hugging Face Hub. Now, we export it into a FiftyOne-compatible dataset to leverage additional capabilities. For more details on the dataset types supported by FiftyOne, refer to this [documentation](https://docs.voxel51.com/api/fiftyone.types.dataset_types.html?highlight=dataset%20type#module-fiftyone.types.dataset_types)
    
    
    [ ]:
    
    
    
    export_dir = "VAD_test"
    new_dataset.export(
        export_dir=export_dir,
        dataset_type=fo.types.FiftyOneDataset,
    )
    

### Next Steps:#

Try modifying the dataset loading parameters, apply different filters, and explore the FiftyOne Appâs visualization features! IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
