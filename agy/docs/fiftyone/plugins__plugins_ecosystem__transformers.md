---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/transformers.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-huggingface-plugins/tree/main/plugins/transformers)

# Hugging Face Transformers Plugin#

A plugin that allows you to apply transformer models from the Hugging Face Hub to your FiftyOne datasets.

## Installation#

First, install the latest version of FiftyOne and Hugging Face libraries:
    
    
    pip install -U fiftyone transformers huggingface_hub
    

Then, download the plugin:
    
    
    fiftyone plugins download https://github.com/voxel51/fiftyone-huggingface-plugins \
        --plugin-names @voxel51/transformers
    

## Usage#

  1. Launch the App:



    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    session = fo.launch_app(dataset)
    

  2. Press ``` or click the `Browse operations` action to open the Operators list

  3. Select `apply_transformers_model`




Select the task type from the task dropdown and the model from the model dropdown. You can choose to apply the model to the entire dataset, your current view, or currently selected samples.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
