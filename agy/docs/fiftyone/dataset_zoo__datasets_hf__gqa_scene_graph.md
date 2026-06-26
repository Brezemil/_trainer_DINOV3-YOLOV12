---
source_url: https://docs.voxel51.com/dataset_zoo/datasets_hf/gqa_scene_graph.html
---

Note

This is a **Hugging Face dataset**. For large datasets, ensure `huggingface_hub>=1.1.3` to avoid rate limits. Learn more in the [Hugging Face integration docs](https://docs.voxel51.com/integrations/huggingface.html#loading-datasets-from-the-hub).

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/Voxel51/GQA-Scene-Graph)

# Dataset Card for GQA-35k#

![image](https://huggingface.co/datasets/Voxel51/GQA-Scene-Graph/resolve/main/gqa.png)

The GQA (Visual Reasoning in the Real World) dataset is a large-scale visual question answering dataset that includes scene graph annotations for each image.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 35000 samples.

Note: This is a 35,000 sample subset which does not contain questions, only the scene graph annotations as detection-level attributes.

You can find the recipe notebook for creating the dataset [here](https://colab.research.google.com/drive/1IjyvUSFuRtW2c5ErzSnz1eB9syKm0vo4?usp=sharing)

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

## Usage#
    
    
    import fiftyone as fo
    import fiftyone.utils.huggingface as fouh
    
    # Load the dataset
    # Note: other available arguments include 'max_samples', etc
    dataset = fouh.load_from_hub("Voxel51/GQA-Scene-Graph")
    
    # Launch the App
    session = fo.launch_app(dataset)
    

## Dataset Details#

### Dataset Description#

## Scene Graph Annotations#

  * Each of the 113K images in GQA is associated with a detailed scene graph describing the objects, attributes and relations present.

  * The scene graphs are based on a cleaner version of the Visual Genome scene graphs.

  * For each image, the scene graph is provided as a dictionary (sceneGraph) containing:

    * Image metadata like width, height, location, weather

    * A dictionary (objects) mapping each object ID to its name, bounding box coordinates, attributes, and relations[6]

    * Relations are represented as triples specifying the predicate (e.g. âholdingâ, âonâ, âleft ofâ) and the target object ID[6]

  * **Curated by:** Drew Hudson & Christopher Manning

  * **Shared by:** [Harpreet Sahota](https://x.com/datascienceharp), Hacker-in-Residence at Voxel51

  * **Language(s) (NLP):** en

  * **License:**

  * GQA annotations (scene graphs, questions, programs) licensed under CC BY 4.0

  * Images sourced from Visual Genome may have different licensing terms




### Dataset Sources#

  * **Repository:** https://cs.stanford.edu/people/dorarad/gqa/

  * **Paper :** https://arxiv.org/pdf/1902.09506

  * **Demo:** https://cs.stanford.edu/people/dorarad/gqa/vis.html




## Dataset Structure#

Hereâs the information presented as a markdown table:

Field | Type | Description  
---|---|---  
location | str | Optional. The location of the image, e.g. kitchen, beach.  
weather | str | Optional. The weather in the image, e.g. sunny, cloudy.  
objects | dict | A dictionary from objectId to its object.  
Â Â Â Â object | dict | A visual element in the image (node).  
Â Â Â Â Â Â Â Â name | str | The name of the object, e.g. person, apple or sky.  
Â Â Â Â Â Â Â Â x | int | Horizontal position of the object bounding box (top left).  
Â Â Â Â Â Â Â Â y | int | Vertical position of the object bounding box (top left).  
Â Â Â Â Â Â Â Â w | int | The object bounding box width in pixels.  
Â Â Â Â Â Â Â Â h | int | The object bounding box height in pixels.  
Â Â Â Â Â Â Â Â attributes | [str] | A list of all the attributes of the object, e.g. blue, small, running.  
Â Â Â Â Â Â Â Â relations | [dict] | A list of all outgoing relations (edges) from the object (source).  
Â Â Â Â Â Â Â Â Â Â Â Â relation | dict | A triple representing the relation between source and target objects.  
  
Note: Iâve used non-breaking spaces (`&nbsp;`) to indent the nested fields in the âFieldâ column to represent the hierarchy. This helps to visually distinguish the nested structure within the table.

## Citation#

**BibTeX:**
    
    
    @article{Hudson_2019,
       title={GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering},
       ISBN={9781728132938},
       url={http://dx.doi.org/10.1109/CVPR.2019.00686},
       DOI={10.1109/cvpr.2019.00686},
       journal={2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
       publisher={IEEE},
       author={Hudson, Drew A. and Manning, Christopher D.},
       year={2019},
       month={Jun}
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
