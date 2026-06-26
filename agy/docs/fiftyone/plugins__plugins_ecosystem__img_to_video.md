---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/img_to_video.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/danielgural/img_to_video_plugin)

# Image to Video Plugin#

![imagetovideo](https://raw.githubusercontent.com/danielgural/img_to_video_plugin/main/assets/stable_video_diffusion.gif)

This plugin is a Python plugin that allows for you to generate videos from images!

Bring any image to life in seconds!

# Installation#
    
    
    fiftyone plugins download https://github.com/danielgural/img_to_video_plugin
    

If you want to use Replicate models, you will need to pip install replicate and set the environment variable REPLICATE_API_TOKEN with your API token.

# Operators#

## `img2video`#

Accepts in sample or samples to generate videos using a image to video model. Currently the only supported model is [Stable Video Diffusion](https://replicate.com/stability-ai/stable-video-diffusion/api?tab=python) on [replicate](https://replicate.com/) Refer to [inputs](https://replicate.com/stability-ai/stable-video-diffusion/api?tab=python) for more information on the inputs into the model.

![bear](https://raw.githubusercontent.com/danielgural/img_to_video_plugin/main/assets/bear.gif)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
