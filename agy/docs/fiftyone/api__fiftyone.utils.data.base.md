---
source_url: https://docs.voxel51.com/api/fiftyone.utils.data.base.html
---

# fiftyone.utils.data.base#

Data utilities.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`map_values`(sample_collection,Â path,Â map[,Â ...]) | Maps the values in the given field to new values for each sample in the collection.  
---|---  
`parse_images_dir`(dataset_dir[,Â recursive]) | Parses the contents of the given directory of images.  
`parse_videos_dir`(dataset_dir[,Â recursive]) | Parses the contents of the given directory of videos.  
`parse_image_classification_dir_tree`(dataset_dir) | Parses the contents of the given image classification dataset directory tree, which should have the following format.  
`download_image_classification_dataset`(...[,Â ...]) | Downloads the classification dataset specified by the given CSV file, which should have the following format.  
`download_images`(image_urls,Â output_dir[,Â ...]) | Downloads the images from the given URLs.  
  
fiftyone.utils.data.base.map_values(_sample_collection_ , _path_ , _map_ , _progress =False_)#
    

Maps the values in the given field to new values for each sample in the collection.

This function performs the same operation as [`map_values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.map_values "fiftyone.core.collections.SampleCollection.map_values") but it immediately saves the mapped values to the database rather than creating a view.

Examples:
    
    
    import random
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    import fiftyone.utils.data as foud
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    values = [random.choice(ANIMALS) for _ in range(len(dataset))]
    dataset.set_values("str_field", values)
    dataset.set_values("list_field", [[v] for v in values])
    
    dataset.set_field("ground_truth.detections.tags", [F("label")]).save()
    
    # Map all animals to string "animal"
    mapping = {a: "animal" for a in ANIMALS}
    
    #
    # Map values in top-level fields
    #
    
    foud.map_values(dataset, "str_field", mapping)
    
    print(dataset.count_values("str_field"))
    # {"animal": 200}
    
    foud.map_values(dataset, "list_field", mapping)
    
    print(dataset.count_values("list_field"))
    # {"animal": 200}
    
    #
    # Map values in nested fields
    #
    
    foud.map_values(dataset, "ground_truth.detections.label", mapping)
    
    print(dataset.count_values("ground_truth.detections.label"))
    # {"animal": 183, ...}
    
    foud.map_values(dataset, "ground_truth.detections.tags", mapping)
    
    print(dataset.count_values("ground_truth.detections.tags"))
    # {"animal": 183, ...}
    

Parameters:
    

  * **sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **path** â the field or `embedded.field.name` to map

  * **map** â a dict mapping values to new values

  * **progress** (_False_) â whether to render a progress bar (True/False), use the default value `fiftyone.config.show_progress_bars` (None), or a progress callback function to invoke instead




fiftyone.utils.data.base.parse_images_dir(_dataset_dir_ , _recursive =True_)#
    

Parses the contents of the given directory of images.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories



Returns:
    

a list of image paths

fiftyone.utils.data.base.parse_videos_dir(_dataset_dir_ , _recursive =True_)#
    

Parses the contents of the given directory of videos.

Parameters:
    

  * **dataset_dir** â the dataset directory

  * **recursive** (_True_) â whether to recursively traverse subdirectories



Returns:
    

a list of video paths

fiftyone.utils.data.base.parse_image_classification_dir_tree(_dataset_dir_)#
    

Parses the contents of the given image classification dataset directory tree, which should have the following format:
    
    
    <dataset_dir>/
        <classA>/
            <image1>.<ext>
            <image2>.<ext>
            ...
        <classB>/
            <image1>.<ext>
            <image2>.<ext>
            ...
    

Parameters:
    

**dataset_dir** â the dataset directory

Returns:
    

a list of `(image_path, target)` pairs classes: a list of class label strings

Return type:
    

[samples](api__fiftyone.brain.internal.core.elasticsearch.md#fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityIndex.samples "fiftyone.brain.internal.core.elasticsearch.ElasticsearchSimilarityIndex.samples")

fiftyone.utils.data.base.download_image_classification_dataset(_csv_path_ , _dataset_dir_ , _classes =None_, _num_workers =None_)#
    

Downloads the classification dataset specified by the given CSV file, which should have the following format:
    
    
    <label1>,<image_url1>
    <label2>,<image_url2>
    ...
    

The image filenames are the basenames of the URLs, which are assumed to be unique.

The dataset is written to disk in [`fiftyone.types.FiftyOneImageClassificationDataset`](api__fiftyone.types.md#fiftyone.types.FiftyOneImageClassificationDataset "fiftyone.types.FiftyOneImageClassificationDataset") format.

Parameters:
    

  * **csv_path** â a CSV file containing the labels and image URLs

  * **dataset_dir** â the directory to write the dataset

  * **classes** (_None_) â an optional list of classes. By default, this will be inferred from the contents of `csv_path`

  * **num_workers** (_None_) â a suggested number of threads to use to download images




fiftyone.utils.data.base.download_images(_image_urls_ , _output_dir_ , _num_workers =None_)#
    

Downloads the images from the given URLs.

The filenames in `output_dir` are the basenames of the URLs, which are assumed to be unique.

Parameters:
    

  * **image_urls** â a list of image URLs to download

  * **output_dir** â the directory to write the images

  * **num_workers** (_None_) â a suggested number of threads to use



Returns:
    

the list of downloaded image paths

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
