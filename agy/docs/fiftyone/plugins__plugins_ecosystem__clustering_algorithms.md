---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/clustering_algorithms.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/danielgural/clustering_algorithms)

# Automated Clustering#

![cluster Detection](https://raw.githubusercontent.com/danielgural/clustering_algorithms/main/assets/cluster.gif)

This plugin is a Python plugin that allows for you to find the clusters in your dataset!

Find those pesky clusters in just a few minutes!

# Installation#
    
    
    fiftyone plugins download https://github.com/danielgural/clustering_algorithms
    

# Operators#

## `cluster_samples`#

Finds clusters in your dataset based on embeddings from [FiftyOne Model Zoo](https://docs.voxel51.com/user_guide/model_zoo/models.html). Choose which algorithm you want to use to find clusters in your dataset.

Make sure to take advantage of optional inputs such as finding clusters within a specific class, tagging clusters, or optionally regenerating embeddings from a different model!

[Cluster Detection Algorithms Used From sklearn](https://scikit-learn.org/stable/modules/clustering.html)

## Supported Embedding Models#

Model Name | Framework  
---|---  
alexnet-imagenet-torch | Torch  
classification-transformer-torch | Torch  
clip-vit-base32-torch | Torch  
densenet121-imagenet-torch | Torch  
densenet161-imagenet-torch | Torch  
densenet169-imagenet-torch | Torch  
densenet201-imagenet-torch | Torch  
detection-transformer-torch | Torch  
dinov2-vitb14-torch | Torch  
dinov2-vitg14-torch | Torch  
dinov2-vitl14-torch | Torch  
dinov2-vits14-torch | Torch  
googlenet-imagenet-torch | Torch  
inception-resnet-v2-imagenet-tf1 | TF1  
inception-v3-imagenet-torch | Torch  
inception-v4-imagenet-tf1 | TF1  
mobilenet-v2-imagenet-tf1 | TF1  
mobilenet-v2-imagenet-torch | Torch  
open-clip-torch | Torch  
resnet-v1-50-imagenet-tf1 | TF1  
resnet-v2-50-imagenet-tf1 | TF1  
resnet101-imagenet-torch | Torch  
resnet152-imagenet-torch | Torch  
resnet18-imagenet-torch | Torch  
resnet34-imagenet-torch | Torch  
resnet50-imagenet-torch | Torch  
resnext101-32x8d-imagenet-torch | Torch  
resnext50-32x4d-imagenet-torch | Torch  
vgg11-bn-imagenet-torch | Torch  
vgg11-imagenet-torch | Torch  
vgg13-bn-imagenet-torch | Torch  
vgg13-imagenet-torch | Torch  
vgg16-bn-imagenet-torch | Torch  
vgg16-imagenet-tf1 | TF1  
vgg16-imagenet-torch | Torch  
vgg19-bn-imagenet-torch | Torch  
vgg19-imagenet-torch | Torch  
wide-resnet101-2-imagenet-torch | Torch  
wide-resnet50-2-imagenet-torch | Torch  
zero-shot-classification-transformer-torch | Torch  
zero-shot-detection-transformer-torch | Torch  
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
