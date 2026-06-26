---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/concept_space_traversal.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/jacobmarks/concept-space-traversal-plugin)

# Concept Space Traversal Plugin#

![concept_traversal](https://github.com/jacobmarks/concept-space-traversal-plugin/assets/12500356/50e833a1-9198-41dc-852e-7def33061138)

This plugin allows you to âtraverseâ the concept space of a similarity index by adding text prompts (with configurable strength) to a base image.

**Note:** This plugin requires a similarity index that supports prompts (i.e. embeds text and images) to be present on the dataset. You can create one with:
    
    
    import fiftyone as fo
    import fiftyone.brain as fob
    
    dataset = fo.load_dataset("my_dataset")
    fob.compute_similarity(
        dataset,
        brain_key="my_brain_key",
        model="clip-vit-base32-torch",
        metric="cosine",
        )
    

# Watch On Youtube#

[![Video Thumbnail](https://img.youtube.com/vi/XwstS_YCxoc/0.jpg)](https://www.youtube.com/watch?v=XwstS_YCxoc&list=PLuREAXoPgT0RZrUaT0UpX_HzwKkoB-S9j&index=10)

# Installation#
    
    
    fiftyone plugins download https://github.com/jacobmarks/concept-space-traversal-plugin
    

Refer to the [main README](https://github.com/voxel51/fiftyone-plugins) for more information about managing downloaded plugins and developing plugins locally.

# Operators#

## `open_traversal_panel`#

  * Opens the concept space traversal panel on click

  * Only activated when the dataset has a similarity index




## `traverser`#

  * Runs the Traverser on the dataset




## `get_sample_url`#

  * Returns the resource URL of the media file associated with a sample, from the sampleâs ID.




# Development#

This plugin was a joint creation between myself and [Ibrahim Manjra](https://github.com/imanjra). Couldnât have done it without his JavaScript wizardry!

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
