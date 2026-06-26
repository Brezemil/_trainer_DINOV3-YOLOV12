---
source_url: https://docs.voxel51.com/integrations/openclip.html
---

# OpenCLIP Integration#

FiftyOne integrates natively with the [OpenCLIP](https://github.com/mlfoundations/open_clip) library, an open source implementation of OpenAIâs CLIP (Contrastive Language-Image Pre-training) model that you can use to run inference on your FiftyOne datasets with a few lines of code!

## Setup#

To get started with OpenCLIP, install the `open_clip_torch` package:
    
    
    1pip install open_clip_torch
    2
    3# May also be needed
    4pip install timm --upgrade
    

## Model zoo#

You can load the original ViT-B-32 OpenAI pretrained model from the [FiftyOne Model Zoo](https://docs.voxel51.com/model_zoo/index.html#model-zoo) as follows:
    
    
    1import fiftyone.zoo as foz
    2
    3model = foz.load_zoo_model("open-clip-torch")
    

You can also specify different model architectures and pretrained weights by passing in optional parameters. Pretrained models can be loaded directly from OpenCLIP or from [Hugging Faceâs Model Hub](https://huggingface.co/docs/hub/models-the-hub):
    
    
     1rn50 = foz.load_zoo_model(
     2    "open-clip-torch",
     3    clip_model="RN50",
     4    pretrained="cc12m",
     5)
     6
     7meta_clip = foz.load_zoo_model(
     8    "open-clip-torch",
     9    clip_model="ViT-B-32-quickgelu",
    10    pretrained="metaclip_400m",
    11)
    12
    13eva_clip = foz.load_zoo_model(
    14    "open-clip-torch",
    15    clip_model="EVA02-B-16",
    16    pretrained="merged2b_s8b_b131k",
    17)
    18
    19clipa = foz.load_zoo_model(
    20    "open-clip-torch",
    21    clip_model="hf-hub:UCSC-VLAA/ViT-L-14-CLIPA-datacomp1B",
    22    pretrained="",
    23)
    24
    25siglip = foz.load_zoo_model(
    26    "open-clip-torch",
    27    clip_model="hf-hub:timm/ViT-B-16-SigLIP",
    28    pretrained="",
    29)
    

## Inference#

When running inference with OpenCLIP, you can specify a text prompt to help guide the model towards a solution as well as only specify a certain number of classes to output during zero shot classification.

Note

While OpenCLIP models are typically set to train mode by default, the FiftyOne integration sets the model to eval mode before running inference.

For example we can run inference as such:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5
     6model = foz.load_zoo_model(
     7    "open-clip-torch",
     8    text_prompt="A photo of a",
     9    classes=["person", "dog", "cat", "bird", "car", "tree", "chair"],
    10)
    11
    12dataset.apply_model(model, label_field="clip_predictions")
    13
    14session = fo.launch_app(dataset)
    

![zero-shot-classification-example](../_images/zsc-openclip.png)

## Embeddings#

Another application of OpenCLIP is [embeddings visualization](brain.md#brain-embeddings-visualization).

For example, letâs compare the embeddings of the original OpenAI CLIP model to MetaCLIP. Weâll also perform a quick zero shot classification to color the embeddings:
    
    
     1import fiftyone.brain as fob
     2
     3meta_clip = foz.load_zoo_model(
     4    "open-clip-torch",
     5    clip_model="ViT-B-32-quickgelu",
     6    pretrained="metaclip_400m",
     7    text_prompt="A photo of a",
     8)
     9
    10dataset.apply_model(meta_clip, label_field="meta_clip_classification")
    11
    12fob.compute_visualization(
    13    dataset,
    14    model=meta_clip,
    15    brain_key="meta_clip",
    16)
    17
    18openai_clip = foz.load_zoo_model(
    19    "open-clip-torch",
    20    text_prompt="A photo of a",
    21)
    22
    23dataset.apply_model(openai_clip, label_field="openai_clip_classifications")
    24
    25fob.compute_visualization(
    26    dataset,
    27    model=openai_clip,
    28    brain_key="openai_clip",
    29)
    

Here is the final result!

![clip-compare](../_images/clip-compare.gif)

## Text similarity search#

OpenCLIP can also be used for [text similarity search](brain.md#brain-similarity-text).

To use a specific pretrained-checkpoint pair for text similarity search, pass these in as a dictionary via the `model_kwargs` argument to [`compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity").

For example, for MetaCLIP, we can do the following:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3import fiftyone.brain as fob
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7model_kwargs = {
     8    "clip_model": "ViT-B-32-quickgelu",
     9    "pretrained": "metaclip_400m",
    10    "text_prompt": "A photo of a",
    11}
    12
    13fob.compute_similarity(
    14    dataset,
    15    model="open-clip-torch",
    16    model_kwargs=model_kwargs,
    17    brain_key="sim_metaclip",
    18)
    

You can then search by text similarity in Python via the [`sort_by_similarity()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.sort_by_similarity "fiftyone.core.collections.SampleCollection.sort_by_similarity") stage as follows:
    
    
    1query = "kites flying in the sky"
    2
    3view = dataset.sort_by_similarity(query, k=25, brain_key="sim_metaclip")
    

Note

Did you know? You can also perform text similarity queries directly [in the App](user_guide__app.md#app-text-similarity)!

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
