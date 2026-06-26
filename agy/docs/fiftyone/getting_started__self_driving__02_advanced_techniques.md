---
source_url: https://docs.voxel51.com/getting_started/self_driving/02_advanced_techniques.html
---

|  [ ![](https://cdn.voxel51.com/colab-logo-256px.png) Run in Google Colab ](https://colab.research.google.com/github/voxel51/fiftyone/blob/main/docs/source/getting_started/self_driving/02_advanced_techniques.ipynb) |  [ ![](https://cdn.voxel51.com/github-logo-256px.png) View source on GitHub ](https://github.com/voxel51/fiftyone/blob/main/docs/source/getting_started/self_driving/02_advanced_techniques.ipynb) |  [ ![](https://cdn.voxel51.com/cloud-icon-256px.png) Download notebook ](https://raw.githubusercontent.com/voxel51/fiftyone/main/docs/source/getting_started/self_driving/02_advanced_techniques.ipynb)

# Step 2: Advanced Self Driving Dataset Techniques#

Letâs begin looking at some advance methods we can do with our self driving dataset by flattening our group dataset. By default, a grouped dataset returns only one active slice when you grab a sample. If you want to look at all cameras at once, we can call select_group_slices and pass a media type or a list of group names to get the flattened samples back. Run the code below if you have not run [Loading Dataset](getting_started__self_driving__01_loading_datasets.md), otherwise you can use the dataset from before!
    
    
    [ ]:
    
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    # Run if you skipped Step 1
    all_sensor_dataset = foz.load_zoo_dataset("quickstart-groups")
    
    # Run if you completed Step 1
    all_sensor_dataset = fo.load_dataset("nuscenes_sensors")
    
    
    
    [ ]:
    
    
    
    # Get all the image samples from the dataset
    flattened_dataset = all_sensor_dataset.select_group_slices(media_type="image")
    

## Leveraging Embeddings#

One of the strongest ways we can interact with our self driving car dataset is by using embeddings. By utilizing the FiftyOne Brain, we can compute embeddings on our dataset and do some awesome things. Letâs check them out!

### Compute Visualization#

By computing the visualization of the embeddings on our dataset, we can map the distribution of our dataset into a 2D space for us to analyze and curate! This works great on AV datasets as you can âseeâ the individual drives on each sensor as well as where they deviate. Letâs take a look:
    
    
    [ ]:
    
    
    
    import fiftyone.brain as fob
    
    results = fob.compute_visualization(
        flattened_dataset,
        brain_key="embedding_viz",
        model="clip-vit-base32-torch"
    )
    

### Compute Similarity#

Computing similarity is another awesome way to get more insights into your dataset, especially if you are trying to find the right scenario! By computing similarity with a vision-language model, you can use semantic search to find scenarios like ârainy crosswalksâ, âpedestrians in the roadâ, or more!
    
    
    [ ]:
    
    
    
    fob.compute_similarity(
        flattened_dataset,
        model="clip-vit-base32-torch",
        brain_key="img_sim",
    )
    
    session = fo.launch_app(flattened_dataset)
    

![compute_similarity](https://cdn.voxel51.com/getting_started_self_driving/notebook1/compute_similarity2.webp) You can also use the FiftyOne Brain to find :

  * Most unique samples
  * Likely label mistakes
  * Your hardest samples
  * Most Representative Samples



## Using the Model Zoo#

We can use a ton of models right out of the box to get more insights into our dataset. Utilizing the FiftyOne Model Zoo, we can load in some models to bring even more information to help with curation or downstream tasks. Letâs try one of the most popular models right now in Metaâs SAM2!
    
    
    [ ]:
    
    
    
    # SAM2 Install Instructions:
    
    !git clone https://github.com/facebookresearch/sam2.git && cd sam2
    
    !pip install -e .
    
    
    
    [ ]:
    
    
    
    import fiftyone.zoo as foz
    
    model = foz.load_zoo_model("segment-anything-2-hiera-tiny-image-torch")
    # Prompt with boxes
    flattened_dataset.apply_model(
        model,
        label_field="sam2",
    )
    

Afterwards, you will be able to see some semantic segmentations of our image of the best things SAM2 decided to segment. You can also prompt SAM2 with your own bounding boxes for greater accuracy. If you arenât happy with the accuracy, donât worry, we will be using an even better model later! Letâs try using a depth model to help us determine how far away other cars and objects are in our image samples!
    
    
    [ ]:
    
    
    
    model = foz.load_zoo_model("depth-estimation-transformer-torch")
    
    flattened_dataset.apply_model(model, label_field="depth")
    

Each of our samples in our dataset now have a depth heatmap and a semantic segmentation on them. You can store as many different label types as you like on any sample in FiftyOne! By leveraging FiftyOne Model Zoo and the FiftyOne Brain, you can greatly enhance any self driving workflow you do! IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
