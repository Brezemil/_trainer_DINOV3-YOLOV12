---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/plotly_map_panel.html
---

Note

This is a **community plugin** , an external project maintained by its respective author. Community plugins are not part of FiftyOne core and may change independently. Please review each pluginâs documentation and license before use.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/allenleetc/plotly-map-panel)

# Plotly Map Panel#

An example map panel using PlotlyView.

This example demonstrates mapping functionality built on PlotlyView as an alternative to fiftyoneâs built-in [Map Panel](https://docs.voxel51.com/user_guide/app.html#map-panel) that relies on [Mapbox](https://www.mapbox.com/).

![Screenshot 2024-11-13 at 12 11 13â¯AM](https://github.com/user-attachments/assets/7515a199-dee8-457a-a73c-b21dd1138a26) Map data from [OpenStreetMap](http://openstreetmap.org/copyright) 

## Installation#
    
    
    fiftyone plugins download https://github.com/allenleetc/plotly-map-panel
    

Refer to the [main README](https://github.com/voxel51/fiftyone-plugins) for more information about managing downloaded plugins and developing plugins locally.

## Usage#

[Install fiftyone](https://docs.voxel51.com/getting_started/install.html#fiftyone-installation) and then run the following code to create a test dataset.
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset('https://github.com/allenleetc/world-airports',
                                   dataset_name='world-airports',
                                   persistent=True)
                                   
    session = fo.launch_app(dataset,auto=False)
    

  2. Press the `+` button next to the âSamplesâ tab

  3. Select the `Plotly Map` panel

  4. Select dataset fields in the pulldown menus and explore the dataset!




## Todo#

  * Optionally disable dynamic colorscale adjustment based on view selection

  * Select geo scope based on data encountered

  * Use background layers

  * Experiment with polygon drawing

  * (Maybe) extend marker slider to larger markers




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
