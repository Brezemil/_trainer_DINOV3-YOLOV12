---
source_url: https://docs.voxel51.com/getting_started/manufacturing/08_extended_exploration.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/08_extended_exploration.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/manufacturing/08_extended_exploration.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/manufacturing/08_extended_exploration.ipynb)

# Loading and Exploring Datasets#

This notebook is a modification of the original Getting Started Notebook for the **Visual Anomaly and Novelty Detection (VAND) 2025 Challenge** at CVPR! This challenge, sponsored by **Voxel51** , **Anomalib** , and **MVTec** , focuses on advancing **Visual Anomaly Detection** in real-world industrial scenarios. Here youâll work with the newly released **MVTec AD 2** dataset, featuring challenging real-world conditions, distribution shifts, and unexpected defect types. ![csm_mad2_objects_overview](https://cdn.voxel51.com/getting_started_manufacturing/notebook8/csm_mad2_objects_overview.webp) **Track 1 Dataset (MVTec AD 2)** : [Explore here](https://www.mvtec.com/company/research/datasets/mvtec-ad-2) **Challenge Registration & Info**: [Join the challenge](https://voxel51.com/computer-vision-events/vand-3-0-challenge-at-cvpr-2025/) **Join the Community** : [FiftyOne Discord](https://discord.com/invite/fiftyone-community) â `#cvpr-challenge-vand3-0` **Related Documentation**

  * Anomalib: [GitHub Repo](https://github.com/open-edge-platform/anomalib)
  * MVTec AD2: [Download Link](https://www.mvtec.com/company/research/datasets/mvtec-ad-2)
  * FiftyOne: <https://docs.voxel51.com/>

Letâs dive into anomaly detection with top-tier tools and datasets!

## Load MVTec AD 2 Using Anomalib#

This section performs an essential step in preparing or visualizing the dataset. Note: You will need to use the Anomalib library for this notebook.
    
    
    [ ]:
    
    
    
    # Using Anomalib you can also import MVTec AD 2
    from anomalib.data import MVTecAD2
    
    OBJECTS_LIST = [
        'can',
        'fruit_jelly',
        'sheet_metal',
        'wallplugs',
        'fabric',
        'woriceod',
        'vial',
        'walnuts',
    ]
    OBJECT = "sheet_metal" ## object to select
    
    # Create datamodule with public test set
    datamodule = MVTecAD2(
        root="path/to/mvtec_ad_2",  # <-- replace with your dataset path
        category=OBJECT,            # <-- set the object/category as needed
        train_batch_size=32,
        eval_batch_size=32,
    )
    
    # Access different test sets
    datamodule.setup()
    public_loader = datamodule.test_dataloader()  # returns loader based on test_type
    #private_loader = datamodule.test_dataloader(test_type="private")
    #mixed_loader = datamodule.test_dataloader(test_type="private_mixed")
    

## Dataset Loading and Preprocessing Functions#

This block defines several utility functions and logic to structure and load the **MVTec AD 2** dataset into a FiftyOne dataset, enriching it with custom fields like defect category, shift type, and segmentation masks. **Key Components:**

  * `explore_dataset_structure`: Recursively walks through the dataset directory and prints its structure as a DataFrame.
  * `extract_shifting_info`: Determines the type of distribution shift (e.g., overexposed, underexposed) from the image filename.
  * `load_segmentation_mask`: Loads a mask image as a NumPy array in grayscale.
  * `find_segmentation_mask`: Finds the path to the ground truth segmentation mask corresponding to a bad image.
  * `get_fiftyone_dataset`: Creates a new FiftyOne dataset named `"mvtecad2"` and populates it with:
    * Image samples and their metadata
    * Classification labels for category and defect
    * Folder type and shift type information
    * Segmentation masks for defective samples if available

The resulting dataset can be explored using FiftyOneâs App for deeper analysis and visualization of anomalies and their spatial locations.
    
    
    [ ]:
    
    
    
    import os
    import cv2
    import numpy as np
    import pandas as pd
    import fiftyone as fo
    import fiftyone.core.dataset as fod
    import fiftyone.core.metadata as fom
    from fiftyone.core.labels import Segmentation, Classification
    from glob import glob
    
    def explore_dataset_structure(base_path):
        """Returns dataset folder structure as a dictionary and prints it."""
        dataset_metadata = []
        for root, dirs, files in os.walk(base_path):
            level = root.replace(base_path, '').count(os.sep)
            folder_name = os.path.basename(root)
            dataset_metadata.append({'Level': level, 'Folder': folder_name, 'Path': root, 'Num_Files': len(files)})
        df = pd.DataFrame(dataset_metadata)
        print(df)
        return df
    
    def extract_shifting_info(image_name):
        """Extracts shifting type from image filename."""
        if 'regular' in image_name:
            return 'regular'
        elif 'overexposed' in image_name:
            return 'overexposed'
        elif 'underexposed' in image_name:
            return 'underexposed'
        elif 'shift' in image_name:
            return f'shift_{image_name.split("_")[-1].split(".")[0]}'
        return 'unknown'
    
    def load_segmentation_mask(mask_path):
        """Loads the segmentation mask as a NumPy array."""
        if os.path.exists(mask_path):
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            if mask is not None:
                return mask
        return None
    
    def find_segmentation_mask(image_path):
        """Finds the corresponding segmentation mask for a given bad image."""
        mask_path = image_path.replace("/bad/", "/ground_truth/bad/")
        if os.path.exists(mask_path):
            return mask_path
        return None
    
    def get_fiftyone_dataset(base_path):
        """Creates and loads dataset into FiftyOne."""
        dataset_name = "mvtecad2"
        if dataset_name in fo.list_datasets():
            fo.delete_dataset(dataset_name)
    
        dataset = fod.Dataset(name=dataset_name, persistent=True)
        dataset.add_sample_field("category_label", fo.EmbeddedDocumentField, embedded_doc_type=Classification)
        dataset.add_sample_field("folder_type", fo.StringField)
        dataset.add_sample_field("defect_label", fo.EmbeddedDocumentField, embedded_doc_type=Classification)
        dataset.add_sample_field("shift_type", fo.StringField)
        dataset.add_sample_field("segmentation", fo.EmbeddedDocumentField, embedded_doc_type=Segmentation)
    
        for category_label in os.listdir(base_path):
            category_path = os.path.join(base_path, category_label)
            print("Category", category_label, category_path)
            if os.path.isdir(category_path):
                for folder_type in os.listdir(category_path):
                    folder_path = os.path.join(category_path, folder_type)
                    print("Folder_Type", folder_type, folder_path)
                    if os.path.isdir(folder_path):
                        for defect_label in os.listdir(folder_path):
                            defect_path = os.path.join(folder_path, defect_label)
                            print("Defect", defect_label, defect_path)
                            if os.path.isdir(defect_path):
                                for img in glob(os.path.join(defect_path, '*.png')):
                                    img_name = os.path.basename(img)
                                    shift_type = extract_shifting_info(img_name)
                                    print("Image_Sample", img_name, shift_type)
                                    metadata = fom.ImageMetadata()
                                    sample = fo.Sample(filepath=os.path.abspath(img),
                                                       tags=[defect_label],
                                                       metadata=metadata,
                                                       category_label=Classification(label=str(category_label)),
                                                       folder_type=folder_type,
                                                       defect_label=Classification(label=str(defect_label)),
                                                       shift_type=shift_type)
    
                                    # Add segmentation mask if applicable
                                    if defect_label == 'bad' and 'test_public' in folder_type:
                                        mask_path = find_segmentation_mask(img)
                                        if mask_path:
                                            mask_array = load_segmentation_mask(mask_path)
                                            if mask_array is not None:
                                                sample["segmentation"] = Segmentation(mask=mask_array)
    
                                    dataset.add_sample(sample)
    
                        # Ensure `ground_truth/bad` folder is processed correctly
                        ground_truth_path = os.path.join(folder_path, "ground_truth", "bad")
                        if os.path.exists(ground_truth_path):
                            for mask_file in glob(os.path.join(ground_truth_path, '*.png')):
                                mask_name = os.path.basename(mask_file).replace("_mask", "")  # Remove _mask suffix if present
                                corresponding_img = os.path.abspath(os.path.join(folder_path, "bad", mask_name))
                                print("GT", mask_name, corresponding_img)
                                # Debugging Output
                                print(f"GT Processing: Mask {mask_name} â Image {corresponding_img}")
    
                                if os.path.exists(corresponding_img):
                                    mask_array = load_segmentation_mask(mask_file)
                                    if mask_array is not None:
                                        matched_samples = dataset.match({"filepath": corresponding_img})
                                        if len(matched_samples) > 0:
                                            sample = matched_samples.first()
                                            sample["segmentation"] = Segmentation(mask=mask_array)
                                            sample.save()
                                            print(f"â Segmentation mask added for {corresponding_img}")
                                        else:
                                            print(f"â  Warning: No matching sample found for {corresponding_img}")
                                else:
                                    print(f"â  Warning: Corresponding image not found for mask {mask_file}")
        return dataset
    

## Load and Explore the MVTec AD 2 Dataset#

This section defines the path to the **MVTec AD 2** dataset, explores its structure, and loads it into a FiftyOne dataset using the previously defined helper functions. **What it does:**

  * Sets the base path to the dataset (update the path if needed).
  * Calls `explore_dataset_structure()` to print a high-level view of the folder hierarchy and file counts.
  * Uses `get_fiftyone_dataset()` to construct and populate a FiftyOne dataset with images, metadata, labels, and segmentation masks.
  * Reloads and prints summary information about the loaded dataset to confirm successful ingestion.


    
    
    [ ]:
    
    
    
    # Code explanation: Add description here
    # Define base dataset path
    dataset_base_path = "/path/to/mvtec_ad_2"  # Change this to your actual dataset path
    
    #dataset_base_path = "./dataset"  # Change this to your actual dataset path
    
    # Explore dataset structure
    dataset_structure_df = explore_dataset_structure(dataset_base_path)
    
    # Load dataset into FiftyOne
    dataset = get_fiftyone_dataset(dataset_base_path)
    dataset.reload()
    print(dataset)
    print("Dataset loaded into FiftyOne")
    

## Launching FiftyOne App#

Launch the FiftyOne App to explore the dataset in an interactive interface.
    
    
    [ ]:
    
    
    
    # ð Launch the FiftyOne App session to interactively explore the dataset
    # ð Code explanation: TBD
    session = fo.launch_app(dataset, port=5149, auto=False)
    

## Explore image quality in MVTec AD 2#

Install `image-quality-issues` plugin in your FiftyOne Environment
    
    
    [ ]:
    
    
    
    !fiftyone plugins download https://github.com/jacobmarks/image-quality-issues/
    

## Check dataset schema#
    
    
    [ ]:
    
    
    
    # Get the schema
    schema = dataset.get_field_schema()
    
    # Print the schema
    for field, field_type in schema.items():
        print(f"{field}: {field_type}")
    

## Creating a Grouped Dataset with Segmentation Masks#

This section defines a function to create a **grouped dataset** in FiftyOne, where each sample has two views:

  * The **original image**
  * Its corresponding **segmentation mask**

**Whatâs included:**

  * Imports essential libraries: `os`, `numpy`, `OpenCV (cv2)`, and `FiftyOne`.
  * `create_grouped_dataset()`:
    * Deletes an existing grouped dataset (if it exists).
    * Loads the original dataset and iterates through samples.
    * Copies metadata fields such as category, defect type, and shift type.
    * Saves segmentation masks (real or blank) to a `masks/` subfolder next to each image.
    * Uses FiftyOneâs native grouping feature to associate each image with its mask under a shared `Group`.

This setup is especially useful for workflows involving **paired data** âlike image and segmentation mask combinations, enabling visual comparison and structured exploration within the FiftyOne App. Ideal for exploring tasks with the MVTec AD 2.
    
    
    [ ]:
    
    
    
    import os
    import numpy as np
    import fiftyone as fo
    import cv2
    
    def create_grouped_dataset(original_dataset_name, grouped_dataset_name):
        """
        Creates a grouped dataset using FiftyOne's native grouping feature.
        Each group contains:
          - The original image
          - Its corresponding segmentation mask (real or blank)
        Metadata fields are mirrored if present. Masks are saved in a 'masks/' subfolder.
        """
        # Remove existing dataset if it exists
        if grouped_dataset_name in fo.list_datasets():
            fo.delete_dataset(grouped_dataset_name)
    
        grouped_dataset = fo.Dataset(name=grouped_dataset_name, persistent=True, overwrite=True)
        grouped_dataset.add_group_field("group", default="image")
    
        original_dataset = fo.load_dataset(original_dataset_name)
        grouped_samples = []
    
        for sample in original_dataset.iter_samples(autosave=True, progress=True):
            group = fo.Group()
    
            # Mirror metadata fields if they exist
            category_label = getattr(sample, "category_label", None)
            folder_type = getattr(sample, "folder_type", None)
            defect_label = getattr(sample, "defect_label", None)
            shift_type = getattr(sample, "shift_type", None)
    
            sample["category_label"] = category_label
            sample["folder_type"] = folder_type
            sample["defect_label"] = defect_label
            sample["shift_type"] = shift_type
            sample.save()
    
            # Create image sample
            image_sample = fo.Sample(
                filepath=sample.filepath,
                group=group.element("image"),
                category_label=category_label,
                folder_type=folder_type,
                defect_label=defect_label,
                shift_type=shift_type,
            )
            if sample.metadata is not None:
                image_sample.metadata = sample.metadata
    
            # Get the segmentation mask if present
            segmentation_mask = None
            if hasattr(sample, "segmentation") and sample.segmentation is not None:
                segmentation_mask = getattr(sample.segmentation, "mask", None)
    
            # Prepare mask path
            image_dir = os.path.dirname(sample.filepath)
            mask_dir = os.path.join(image_dir, "masks")
            os.makedirs(mask_dir, exist_ok=True)
            base_filename = os.path.splitext(os.path.basename(sample.filepath))[0]
            mask_filename = f"{base_filename}_mask.png"
            segmentation_filepath = os.path.join(mask_dir, mask_filename)
    
            if isinstance(segmentation_mask, np.ndarray):
                # Save the provided segmentation mask
                cv2.imwrite(segmentation_filepath, segmentation_mask)
                print(f"Saved real mask: {segmentation_filepath}")
                mask_to_use = segmentation_mask
            else:
                # Create a blank mask for images without a mask
                img = cv2.imread(sample.filepath, cv2.IMREAD_UNCHANGED)
                height, width = img.shape[:2]
                mask_to_use = np.zeros((height, width), dtype=np.uint8)
                cv2.imwrite(segmentation_filepath, mask_to_use)
                print(f"Saved zero mask: {segmentation_filepath}")
    
            segmentation_sample = fo.Sample(
                filepath=segmentation_filepath,
                group=group.element("segmentation"),
                segmentation=fo.Segmentation(mask=mask_to_use),
                category_label=category_label,
                folder_type=folder_type,
                defect_label=defect_label,
                shift_type=shift_type,
            )
            if sample.metadata is not None:
                segmentation_sample.metadata = sample.metadata
    
            grouped_samples.extend([image_sample, segmentation_sample])
    
        grouped_dataset.add_samples(grouped_samples)
        return grouped_dataset
    

## Generate and Load the Grouped Dataset#

In this step, we create and load a grouped version of the MVTec AD 2 dataset using the `create_grouped_dataset()` function defined earlier. **What it does:**

  * Calls the function with the original dataset name (`"mvtecad2"`) and the desired grouped dataset name (`"mvtecad2_grouped"`).
  * Reloads the dataset to ensure itâs updated in memory.
  * Prints the dataset summary to confirm successful creation.

This grouped dataset allows us to explore each image alongside its corresponding segmentation mask using FiftyOneâs powerful group-based visualization.
    
    
    [ ]:
    
    
    
    grouped_dataset = create_grouped_dataset("mvtecad2", "mvtecad2_grouped")
    grouped_dataset.reload()
    print(grouped_dataset)
    print("Grouped dataset created in FiftyOne")
    
    
    
    [ ]:
    
    
    
    import os
    
    os.environ["FIFTYONE_ALLOW_LEGACY_ORCHESTRATORS"] = "true"
    session = fo.launch_app(grouped_dataset, port=5160, auto=False)
    

## Dynamic Grouping of Samples by Category#

This section demonstrates how to dynamically group a subset of the dataset based on ground truth labels using FiftyOne. **What it does:**

  * Randomly selects 100 samples from the dataset using a fixed seed for reproducibility.
  * Groups the selected samples by the `category_label.label` field (e.g., bottle, cable, etc.).
  * Prints the media type of the resulting grouped view and the number of groups.
  * Updates the FiftyOne App session to display this grouped view, making it easier to explore anomalies by category.

Grouping by labels enables intuitive visual inspection and comparative analysis across different object categories.
    
    
    [ ]:
    
    
    
    # Take 100 samples and group by ground truth label
    view_group_by = dataset.take(100, seed=51).group_by("category_label.label")
    
    print(view_group_by.media_type)  # group
    print(len(view_group_by))  # 8
    
    session.view = view_group_by
    

## Compute Visual Embeddings with CLIP and UMAP#

In this step, we leverage FiftyOne Brain and a pre-trained CLIP model to compute a visual embedding space for the dataset. **What it does:**

  * Imports the `fiftyone.brain` module for computing embeddings and visual insights.
  * Loads a pre-trained CLIP model (`ViT-B/32`) from the FiftyOne Model Zoo.
  * Computes visual embeddings for the dataset using CLIP and projects them into 2D using **UMAP**.
  * Stores the results under the brain key `"clip_vis"` and embedding field `"clip_embeddings"`.

This enables powerful visual exploration and clustering of semantically similar images in the FiftyOne App using the Brain panel.
    
    
    [ ]:
    
    
    
    import fiftyone.brain as fob
    import fiftyone.zoo.models as fozm
    
    # Load a pre-trained model (e.g., CLIP)
    model = fozm.load_zoo_model("clip-vit-base32-torch")
    
    fob.compute_visualization(
        dataset, embeddings="clip_embeddings", method="umap", brain_key="clip_vis"
    )
    
    
    
    [ ]:
    
    
    
    print(dataset)
    

## Exporting the Dataset in FiftyOne Format#

This section exports the annotated dataset to disk in the native **FiftyOneDataset** format. **What it does:**

  * Defines a target export directory named `"MVTec_AD2_FO"`.
  * Uses `dataset.export()` to write all samples, labels, and metadata to that directory.

This export can be reused later to reload the dataset easily or to share it with collaborators in a structured format supported by FiftyOne.
    
    
    [ ]:
    
    
    
    export_dir = "MVTec_AD2_FO"
    dataset.export(
        export_dir=export_dir,
        dataset_type=fo.types.FiftyOneDataset,
    )
    
    
    
    [ ]:
    
    
    
    from fiftyone.utils.huggingface import push_to_hub
    
    push_to_hub(dataset, "MVTecAD2_FO")
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
