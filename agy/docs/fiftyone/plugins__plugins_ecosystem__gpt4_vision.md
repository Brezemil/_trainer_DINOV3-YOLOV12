---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/gpt4_vision.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/jacobmarks/gpt4-vision-plugin)

# GPT-4 Vision Plugin#

![gpt4_vision](https://github.com/jacobmarks/gpt4-vision-plugin/assets/12500356/722c95d7-4c60-4138-8c9d-c5c26074297b)

## Plugin Overview#

On November 6, 2023, OpenAI made [GPT-4 Vision](https://platform.openai.com/docs/guides/vision) available to developers via an API. The model has the natural language capabilities of GPT-4, as well as the (decent) ability to understand images. It can be prompted with multimodal inputs, including text and a single image or multiple images.

This plugin allows you to integrate GPT-4 Vision natively into your AI and computer vision workflows !

# Installation#

If you havenât already, install FiftyOne:
    
    
    pip install fiftyone
    

Then, install the plugin:
    
    
    fiftyone plugins download https://github.com/jacobmarks/gpt4-vision-plugin
    

To use GPT-4 Vision, you will also need to set the environment variable `OPENAI_API_KEY` with your API key. For information on estimating costs, see [here](https://platform.openai.com/docs/guides/vision/calculating-costs)

## Getting your Data into FiftyOne#

To use GPT-4 Vision, you will need to have a dataset of images in FiftyOne. If you donât have a dataset, you can create one from a directory of images:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset.from_images_dir("/path/to/images")
    
    ## optionally name the dataset and persist to disk
    dataset.name = "my-dataset"
    dataset.persistent = True
    
    ## view the dataset in the App
    session = fo.launch_app(dataset)
    

# Operators#

## `query_gpt4_vision`#

Inputs:

  * `query_text`: The text to prompt GPT-4 Vision with

  * `max_tokens`: The maximum number of tokens to generate




The pluginâs execution context will take all currently selected samples, encode them, and pass them to GPT-4 Vision. The plugin will then output the response from GPT-4 Vision

Happy exploring!

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
