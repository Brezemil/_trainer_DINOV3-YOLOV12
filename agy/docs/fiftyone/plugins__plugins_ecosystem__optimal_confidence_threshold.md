---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/optimal_confidence_threshold.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/danielgural/optimal_confidence_threshold)

# Optimal Confidence Threshold Finder#

![Optimal Confidence](https://raw.githubusercontent.com/danielgural/optimal_confidence_threshold/main/assets/conf_output.png)

This plugin is a Python plugin that allows for you to find the optimal confidence threshold for deploying your models!

Find the magic number in one click!

# Installation#
    
    
    fiftyone plugins download https://github.com/danielgural/optimal_confidence_threshold
    

# Operators#

## `optimal_conf_threshold`#

Finding the optimal confidence threshold can always be tricky. One way to consider doing so is finding the number that maximizes your F1 score. This plugin implements a method of running an optimized version of FiftyOneâs `evaluate_detections` [method](https://docs.voxel51.com/api/fiftyone.core.dataset.html?highlight=evaluate%20detections#fiftyone.core.dataset.Dataset.evaluate_detections). This will calculate the F1 score at different thresholds until the best one is found! Here is how it works!

![Confidence Inputs](https://raw.githubusercontent.com/danielgural/optimal_confidence_threshold/main/assets/conf_inputs.png)

Input the following:

  * Lower bound to search between

  * Upper bound to search between

  * Number of thresholds to check, this will increase complexity

  * Ground Truth field

  * Prediction field




The plugin will then sweep your range for the optimal confidence threshold until the answer is popped out!

![Optimal Confidence](https://raw.githubusercontent.com/danielgural/optimal_confidence_threshold/main/assets/conf_output.png)

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
