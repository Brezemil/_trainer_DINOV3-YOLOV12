---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/huggingface_hub.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-huggingface-plugins/tree/main/plugins/huggingface_hub)

# Hugging Face Hub Plugin#

A plugin that allows you to push FiftyOne datasets to the Hugging Face Hub, and load datasets from the Hub into FiftyOne.

## Installation#

First, install the latest version of FiftyOne and Hugging Face libraries:
    
    
    pip install -U fiftyone transformers huggingface_hub
    

This plugin will only work with FiftyOne version `0.23.8` or later.

Then, download the plugin:
    
    
    fiftyone plugins download https://github.com/voxel51/fiftyone-huggingface-plugins \
        --plugin-names @voxel51/huggingface_hub
    

## Usage#

  1. Launch the App:



    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    session = fo.launch_app(dataset)
    

  2. Press ``` or click the `Browse operations` action to open the Operators list

  3. Select any of the operators listed below!




## Operators#

### push_to_huggingface_hub#

You can use this operator to push the current dataset or view to the Hugging Face Hub.

This operator is essentially a wrapper around the `push_to_hub()` utility function in the FiftyOne Hugging Face SDK utils.

### load_from_huggingface_hub#

You can use this operator to load a dataset from the Hugging Face Hub into FiftyOne.

This operator is essentially a wrapper around the `load_from_hub()` utility function in the FiftyOne Hugging Face SDK utils.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
