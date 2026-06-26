---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/depth_pro_plugin.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/harpreetsahota204/depthpro-plugin)

# Depth Pro Plugin#

A FiftyOne plugin for applying the Apple Depth Pro model to your dataset

## Plugin Overview#

## Installation#

If you havenât already, install FiftyOne:
    
    
    pip install -U fiftyone
    

Then, install the plugin:
    
    
    fiftyone plugins download https://github.com/harpreetsahota204/depthpro-plugin
    

Then, install requirements for the plug-in:
    
    
    fiftyone plugins requirements @harpreetsahota/depth_pro_plugin --install
    

### Depth Types#

The plugin supports two types of depth outputs:

**Regular Depth**

Direct physical distance measurement in meters. Preferred for autonomous driving, precise measurements, and safety-critical applications. Better for accurate obstacle detection and motion planning.

  * Linear depth representation

  * Better for absolute distance measurements

  * Creating 3D reconstructions

  * Common in autonomous driving




**Inverse Depth**

Reciprocal of depth (1/distance). Better for visualizing near-field details, indoor environments, and SLAM applications. Provides more detail in close ranges where depth changes are significant.

  * Better visualization of nearby objects

  * More detail in close range

  * Doing visual SLAM or Structure from Motion

  * Visualizing indoor environments




## Usage in FiftyOne App#

You can compute the depth map directly through the FiftyOne App:

  1. Launch the FiftyOne App with your dataset

  2. Open the âOperators Browserâ by clicking on the Operator Browser icon above the sample grid or by typing backtick (`)

  3. Type âdepth_pro_estimatorâ

  4. Configure the following parameters:

     * **Depth Type** : Choose between:

       * `inverse` \- Reciprocal of depth (1/distance)

       * `regular` \- Direct physical distance measurement in meters.

     * **Field Name** : Enter the name for the heatmap field (e.g., âdepth_mapâ)

  5. Click âExecuteâ to compute depth estimation for your dataset




## Operators#

### `depth_pro_estimator`#

Computes a depth math using the Apple Depth Pro model.

## Operator usage via SDK#

Once the plugin has been installed, you can instantiate the operator as follows:
    
    
    import fiftyone.operators as foo
    
    depthpro = foo.get_operator("@harpreetsahota/depth_pro_plugin/depth_pro_estimator")
    

You can then compute the depth map on your dataset by running the operator with your desired parameters:
    
    
    # Run the operator on your dataset
    depthpro(
        dataset,
        depth_field="depth_map", 
        depth_type="inverse",
        delegate=True
        )
    

If youâre running in a notebook, itâs recommended to launch a [Delegated operation](https://docs.voxel51.com/plugins/using_plugins.html#delegated-operations) by running `fiftyone delegated launch` in terminal, then run as follows:
    
    
    await depthpro(
        dataset,
        depth_field="depth_map",
        depth_type="inverse",
        delegate=True
        )
    

# Citation#

You can read the paper [here](https://arxiv.org/abs/2410.02073).
    
    
    @article{Bochkovskii2024:arxiv,
      author     = {Aleksei Bochkovskii and Ama\"{e}l Delaunoy and Hugo Germain and Marcel Santos and
                   Yichao Zhou and Stephan R. Richter and Vladlen Koltun}
      title      = {Depth Pro: Sharp Monocular Metric Depth in Less Than a Second},
      journal    = {arXiv},
      year       = {2024},
      url        = {https://arxiv.org/abs/2410.02073},
    }
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
