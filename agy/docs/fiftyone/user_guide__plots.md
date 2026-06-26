---
source_url: https://docs.voxel51.com/user_guide/plots.html
---

# Interactive Plots#

FiftyOne provides a powerful [`fiftyone.core.plots`](api__fiftyone.core.plots.md#module-fiftyone.core.plots "fiftyone.core.plots") framework that contains a variety of interactive plotting methods that enable you to visualize your datasets and uncover patterns that are not apparent from inspecting either the [raw media files](user_guide__app.md#fiftyone-app) or [aggregate statistics](https://docs.voxel51.com/user_guide/using_aggregations.html#using-aggregations).

With FiftyOne, you can visualize geolocated data on maps, generate interactive evaluation reports such as confusion matrices and PR curves, create dashboards of custom statistics, and even generate low-dimensional representations of your data that you can use to identify data clusters corresponding to model failure modes, annotation gaps, and more.

What do we mean by **interactive plots**? First, FiftyOne plots are [powered by Plotly](https://plotly.com/python), which means they are responsive JavaScript-based plots that can be zoomed, panned, and lasso-ed. Second, FiftyOne plots can be linked to the [FiftyOne App](user_guide__app.md#fiftyone-app), so that selecting points in a plot will automatically load the corresponding samples/labels in the App (and vice versa) for you to visualize! Linking plots to their source media is a paradigm that should play a critical part in any visual dataset analysis pipeline.

The builtin plots provided by FiftyOne are chosen to help you analyze and improve the quality of your datasets and models, with minimal customization required on your part to get started. At the same time, data/model interpretability is not a narrowly-defined space that can be fully automated. Thatâs why FiftyOneâs plotting framework is highly customizable and extensible, all by writing pure Python (no JavaScript knowledge required).

Note

Check out the [tutorials page](https://docs.voxel51.com/tutorials/index.html#tutorials) for in-depth walkthroughs that apply the available interactive plotting methods to perform evaluation, identify model failure modes, recommend new samples for annotation, and more!

## Overview#

All [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") instances provide a [`plots attribute`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute that you can use to attach [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances to the FiftyOne App.

When [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances are attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"), they are automatically updated whenever [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view") changes for any reason, whether you modify your view in the App, or programmatically change it by setting [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"), or if multiple plots are connected and another plot triggers a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") update!

Note

Interactive plots are currently only supported in Jupyter notebooks. In the meantime, you can still use FiftyOneâs plotting features in other environments, but you must manually call [`plot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.show "fiftyone.core.plots.base.Plot.show") to update the state of a plot to match the state of a connected [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"), and any callbacks that would normally be triggered in response to interacting with a plot will not be triggered.

See this section for more information.

The two main classes of [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") are explained next.

### Interactive plots#

[`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") is a class of plots that are bidirectionally linked to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") via the IDs of either samples or individual labels in the dataset. When the user performs a selection in the plot, the [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view") is automatically updated to select the corresponding samples/labels, and, conversely, when [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view") changes, the contents of the current view is automatically selected in the plot.

Examples of [`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") types include scatterplots, location scatterplots, and interactive heatmaps.

![interactive-plots](../_images/mnist-interactive1.gif)

### View plots#

[`ViewPlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot "fiftyone.core.plots.base.ViewPlot") is a class of plots whose state is automatically updated whenever the current [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view") changes. View plots can be used to construct dynamic dashboards that update to reflect the contents of your current view.

More view plot types are being continually added to the library over time. Current varieties include [`CategoricalHistogram`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram "fiftyone.core.plots.views.CategoricalHistogram"), [`NumericalHistogram`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram "fiftyone.core.plots.views.NumericalHistogram"), and [`ViewGrid`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid "fiftyone.core.plots.views.ViewGrid").

![view-plots](../_images/view-plots.gif)

## Working in notebooks#

The recommended way to work with FiftyOneâs interactive plots is in [Jupyter notebooks](https://jupyter.org) or [JupyterLab](https://jupyterlab.readthedocs.io/en/stable).

In these environments, you can leverage the full power of plots by attaching them to the FiftyOne App and bidirectionally interacting with the plots and the App to identify interesting subsets of your data.

Note

Support for interactive plots in non-notebook contexts and in [Google Colab](https://colab.research.google.com) and [Databricks](https://docs.databricks.com/en/notebooks/index.html) is coming soon! In the meantime, you can still use FiftyOneâs plotting features in these environments, but you must manually call [`plot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.show "fiftyone.core.plots.base.Plot.show") to update the state of a plot to match the state of a connected [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"), and any callbacks that would normally be triggered in response to interacting with a plot will not be triggered.

You can get setup to work in a Jupyter environment by running the commands below for your environment:

To use interactive plots in Jupyter notebooks, ensure that you have sufficiently new versions of the `notebook` and `ipywidgets` packages installed:
    
    
    pip install "notebook>=6" "ipywidgets>=8,<9"
    

To use interactive plots in JupyterLab, ensure that you have sufficiently new versions of the `jupyterlab` and `ipywidgets` packages installed:
    
    
    pip install "jupyterlab>=4" "ipywidgets>=8,<9"
    

If you run into any issues in JupyterLab, especially if you are trying to use JupyterLab 2.X rather than 3.0+, you may need to manually install the `jupyterlab-plotly` extension. Refer to [this troubleshooting guide](https://plotly.com/python/troubleshooting) for more details.

If you wish to use the `matplotlib` backend for any interactive plots, refer to this section for setup instructions.

## Visualizing embeddings#

The [FiftyOne Brain](brain.md#fiftyone-brain) provides a powerful [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") method that can be used to generate low-dimensional representations of the samples/object patches in a dataset that can be visualized using interactive FiftyOne plots.

To learn more about the available embedding methods, dimensionality reduction techniques, and their applications to dataset analysis, refer to [this page](brain.md#brain-embeddings-visualization). In this section, weâll just cover the basic mechanics of creating scatterplots and interacting with them.

Note

The visualizations in this section are rendered under the hood via the [`scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.scatterplot "fiftyone.core.plots.base.scatterplot") method, which you can directly use to generate interactive plots for arbitrary 2D or 3D representations of your data.

### Standalone plots#

Letâs use [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") to generate a 2D visualization of the images in the test split of the [MNIST dataset](dataset_zoo__datasets__mnist.md#dataset-zoo-mnist) and then visualize it using the [`results.visualize()`](api__fiftyone.brain.visualization.md#fiftyone.brain.visualization.VisualizationResults.visualize "fiftyone.brain.visualization.VisualizationResults.visualize") method of the returned results object, where each point is colored by its ground truth label:
    
    
     1import cv2
     2import numpy as np
     3
     4import fiftyone as fo
     5import fiftyone.brain as fob
     6import fiftyone.zoo as foz
     7
     8dataset = foz.load_zoo_dataset("mnist", split="test")
     9
    10# Construct a `num_samples x num_pixels` array of images
    11images = np.array([
    12    cv2.imread(f, cv2.IMREAD_UNCHANGED).ravel()
    13    for f in dataset.values("filepath")
    14])
    15
    16# Compute 2D embeddings
    17results = fob.compute_visualization(dataset, embeddings=images, seed=51)
    18
    19# Visualize embeddings, colored by ground truth label
    20plot = results.visualize(labels="ground_truth.label")
    21plot.show(height=720)
    

![mnist-scatterplot](../_images/mnist-scatterplot.png)

  
As you can see, the 2D embeddings are naturally clustered according to their ground truth label!

### Interactive plots#

The full power of [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization") comes when you associate the scatterpoints with the samples or objects in a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") and then attach it to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session").

The example below demonstrates setting up an interactive scatterplot for the test split of the [MNIST dataset](dataset_zoo__datasets__mnist.md#dataset-zoo-mnist) that is attached to the App.

In this setup, the scatterplot renders each sample using its corresponding 2D embedding generated by [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization"), colored by the sampleâs ground truth label.

Since the `labels` argument to [`results.visualize()`](api__fiftyone.brain.visualization.md#fiftyone.brain.visualization.VisualizationResults.visualize "fiftyone.brain.visualization.VisualizationResults.visualize") is categorical, each class is rendered as its own trace and you can click on the legend entries to show/hide individual classes, or double-click to show/hide all other classes.

When points are lasso-ed in the plot, the corresponding samples are automatically selected in the sessionâs current [`view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"). Likewise, whenever you modify the sessionâs view, either in the App or by programmatically setting [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"), the corresponding locations will be selected in the scatterplot.

Each block in the example code below denotes a separate cell in a Jupyter notebook:
    
    
     1import cv2
     2import numpy as np
     3
     4import fiftyone as fo
     5import fiftyone.brain as fob
     6import fiftyone.zoo as foz
     7
     8dataset = foz.load_zoo_dataset("mnist", split="test")
     9
    10# Construct a `num_samples x num_pixels` array of images
    11images = np.array([
    12    cv2.imread(f, cv2.IMREAD_UNCHANGED).ravel()
    13    for f in dataset.values("filepath")
    14])
    15
    16# Compute 2D embeddings
    17results = fob.compute_visualization(dataset, embeddings=images, seed=51)
    18
    19session = fo.launch_app(dataset)
    
    
    
    1# Visualize embeddings, colored by ground truth label
    2plot = results.visualize(labels="ground_truth.label")
    3plot.show(height=720)
    4
    5session.plots.attach(plot)
    

To give a taste of the possible interactions, letâs hide all zero digit images and select the other digits near the zero cluster; this isolates the non-zero digit images in the App that are likely to be confused as zeros:

![mnist-interactive1](../_images/mnist-interactive1.gif)

  
Alternatively, letâs hide all classes except the zero digits, and then select the zero digits that are _not_ in the zero cluster; this isolates the zero digit images in the App that are likely to be confused as other digits:

![mnist-interactive2](../_images/mnist-interactive2.gif)

## Geolocation plots#

You can use [`location_scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.location_scatterplot "fiftyone.core.plots.base.location_scatterplot") to generate interactive plots of datasets with geolocation data.

You can store arbitrary location data in [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) format on your datasets using the [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") and [`GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations") label types. See [this section](https://docs.voxel51.com/user_guide/using_datasets.html#geolocation) for more information.

The [`location_scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.location_scatterplot "fiftyone.core.plots.base.location_scatterplot") method only supports simple `[longitude, latitude]` coordinate points, which can be stored in the `point` attribute of a [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field.

Note

Did you know? You can create [location-based views](https://docs.voxel51.com/user_guide/using_views.html#geolocation-views) that filter your data by their location!

### Standalone plots#

In the simplest case, you can use this method to generate a location scatterplot for a list of `[longitude, latitude]` coordinates, using the optional `labels` and `sizes` parameters to control the color and sizes of each point, respectively.

The example below demonstrates this usage using the [quickstart-geo](dataset_zoo__datasets__quickstart_geo.md#dataset-zoo-quickstart-geo) dataset from the zoo, which contains [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") data in its `location` field:
    
    
     1import fiftyone as fo
     2import fiftyone.brain as fob
     3import fiftyone.zoo as foz
     4from fiftyone import ViewField as F
     5
     6dataset = foz.load_zoo_dataset("quickstart-geo")
     7fob.compute_uniqueness(dataset)
     8
     9# A list of ``[longitude, latitude]`` coordinates
    10locations = dataset.values("location.point.coordinates")
    11
    12# Scalar `uniqueness` values for each sample
    13uniqueness = dataset.values("uniqueness")
    14
    15# The number of ground truth objects in each sample
    16num_objects = dataset.values(F("ground_truth.detections").length())
    17
    18# Create scatterplot
    19plot = fo.location_scatterplot(
    20    locations=locations,
    21    labels=uniqueness,      # color points by their `uniqueness` values
    22    sizes=num_objects,      # scale point sizes by number of objects
    23    labels_title="uniqueness",
    24    sizes_title="objects",
    25)
    26plot.show()
    

![location-scatterplot](../_images/location-scatterplot.gif)

  
You can also change the style to `style="density"` in order to view the data as a density plot:
    
    
    1# Create density plot
    2plot = fo.location_scatterplot(
    3    locations=locations,
    4    labels=uniqueness,      # color points by their `uniqueness` values
    5    sizes=num_objects,      # scale influence by number of objects
    6    style="density",
    7    radius=10,
    8)
    9plot.show()
    

![location-densityplot](../_images/location-densityplot.gif)

### Interactive plots#

The real power of [`location_scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.location_scatterplot "fiftyone.core.plots.base.location_scatterplot") comes when you associate the location coordinates with the samples in a [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") and then attach it to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session").

The example below demonstrates setting up an interactive location scatterplot for the [quickstart-geo](dataset_zoo__datasets__quickstart_geo.md#dataset-zoo-quickstart-geo) dataset that is attached to the App.

In this setup, the location plot renders each sample using its corresponding `[longitude, latitude]` coordinates from the datasetâs only [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field, `location`. When points are lasso-ed in the plot, the corresponding samples are automatically selected in the sessionâs current [`view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"). Likewise, whenever you modify the Sessionâs view, either in the App or by programmatically setting [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"), the corresponding locations will be selected in the scatterplot.

Each block in the example code below denotes a separate cell in a Jupyter notebook:
    
    
    1import fiftyone as fo
    2import fiftyone.brain as fob
    3import fiftyone.zoo as foz
    4
    5dataset = foz.load_zoo_dataset("quickstart-geo")
    6fob.compute_uniqueness(dataset)
    7
    8session = fo.launch_app(dataset)
    
    
    
     1from fiftyone import ViewField as F
     2
     3# Computes the number of ground truth objects in each sample
     4num_objects = F("ground_truth.detections").length()
     5
     6# Create the scatterplot
     7plot = fo.location_scatterplot(
     8    samples=dataset,
     9    labels="uniqueness",    # color points by their `uniqueness` values
    10    sizes=num_objects,      # scale point sizes by number of objects
    11    sizes_title="objects",
    12)
    13plot.show(height=720)
    14
    15session.plots.attach(plot)
    

![location-scatterplot-interactive](../_images/location-scatterplot-interactive.gif)

## Regression plots#

When you use evaluation methods such as [`evaluate_regressions()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_regressions "fiftyone.core.collections.SampleCollection.evaluate_regressions") to evaluate model predictions, the regression plots that you can generate by calling the [`plot_results()`](api__fiftyone.utils.eval.regression.md#fiftyone.utils.eval.regression.RegressionResults.plot_results "fiftyone.utils.eval.regression.RegressionResults.plot_results") method are responsive plots that can be attached to App instances to interactively explore specific cases of your modelâs performance.

Note

See [this page](user_guide__evaluation.md#evaluating-regressions) for an in-depth guide to using FiftyOne to evaluate regression models.

The example below demonstrates using an interactive regression plot to explore the results of some fake regression data on the [quickstart](dataset_zoo__datasets__quickstart.md#dataset-zoo-quickstart) dataset.

In this setup, you can lasso scatter points to select the corresponding samples in the App.

Likewise, whenever you modify the Sessionâs view, either in the App or by programmatically setting [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"), the regression plot is automatically updated to select the scatter points that are included in the current view.

Each block in the example code below denotes a separate cell in a Jupyter notebook:
    
    
     1import random
     2import numpy as np
     3
     4import fiftyone as fo
     5import fiftyone.zoo as foz
     6from fiftyone import ViewField as F
     7
     8dataset = foz.load_zoo_dataset("quickstart").select_fields().clone()
     9
    10# Populate some fake regression + weather data
    11for idx, sample in enumerate(dataset, 1):
    12    ytrue = random.random() * idx
    13    ypred = ytrue + np.random.randn() * np.sqrt(ytrue)
    14    confidence = random.random()
    15    sample["ground_truth"] = fo.Regression(value=ytrue)
    16    sample["predictions"] = fo.Regression(value=ypred, confidence=confidence)
    17    sample["weather"] = random.choice(["sunny", "cloudy", "rainy"])
    18    sample.save()
    19
    20# Evaluate the predictions in the `predictions` field with respect to the
    21# values in the `ground_truth` field
    22results = dataset.evaluate_regressions(
    23    "predictions",
    24    gt_field="ground_truth",
    25    eval_key="eval",
    26)
    27
    28session = fo.launch_app(dataset)
    
    
    
    1# Plot a scatterplot of the results colored by `weather` and scaled by
    2# `confidence`
    3plot = results.plot_results(labels="weather", sizes="predictions.confidence")
    4plot.show()
    5
    6session.plots.attach(plot)
    

![regression-evaluation](../_images/regression-evaluation.gif)

## Line plots#

You can use [`lines()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.lines "fiftyone.core.plots.base.lines") to generate interactive line plots whose points represent data associated with the samples, frames, or labels of a dataset. These plots can then be attached to App instances to interactively explore specific slices of your dataset based on their corresponding line data.

The example below demonstrates using an interactive lines plot to view the frames of the [quickstart-video](dataset_zoo__datasets__quickstart_video.md#dataset-zoo-quickstart-video) dataset that contain the most vehicles. In this setup, you can lasso scatter points to select the corresponding frames in a [frames view](https://docs.voxel51.com/user_guide/using_views.html#frame-views) in the App.

Each block in the example code below denotes a separate cell in a Jupyter notebook:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart-video").clone()
     6
     7# Ensure dataset has sampled frames available so we can use frame selection
     8dataset.to_frames(sample_frames=True)
     9
    10session = fo.launch_app(dataset)
    
    
    
     1view = dataset.filter_labels("frames.detections", F("label") == "vehicle")
     2
     3# Plot the number of vehicles in each frame of a video dataset
     4plot = fo.lines(
     5    x="frames.frame_number",
     6    y=F("frames.detections.detections").length(),
     7    labels="id",
     8    samples=view,
     9    xaxis_title="frame number",
    10    yaxis_title="num vehicles",
    11)
    12plot.show()
    13
    14# When points are selected in the plot, load the corresponding frames in
    15# frames views in the App
    16plot.selection_mode = "frames"
    17
    18session.plots.attach(plot)
    

![lines](../_images/lines.gif)

## Confusion matrices#

When you use evaluation methods such as [`evaluate_classifications()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_classifications "fiftyone.core.collections.SampleCollection.evaluate_classifications") and [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections") to evaluate model predictions, the confusion matrices that you can generate by calling the [`plot_confusion_matrix()`](api__fiftyone.utils.eval.classification.md#fiftyone.utils.eval.classification.ClassificationResults.plot_confusion_matrix "fiftyone.utils.eval.classification.ClassificationResults.plot_confusion_matrix") method are responsive plots that can be attached to App instances to interactively explore specific cases of your modelâs performance.

Note

See [this page](user_guide__evaluation.md#evaluating-models) for an in-depth guide to using FiftyOne to evaluate models.

The example below demonstrates using an interactive confusion matrix to explore the results of an evaluation on the `predictions` field of the [quickstart](dataset_zoo__datasets__quickstart.md#dataset-zoo-quickstart) dataset.

In this setup, you can click on individual cells of the confusion matrix to select the corresponding ground truth and/or predicted [`Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") in the App. For example, if you click on a diagonal cell of the confusion matrix, you will see the true positive examples of that class in the App.

Likewise, whenever you modify the Sessionâs view, either in the App or by programmatically setting [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"), the confusion matrix is automatically updated to show the cell counts for only those detections that are included in the current view.

Each block in the example code below denotes a separate cell in a Jupyter notebook:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7# Evaluate detections in the `predictions` field
     8results = dataset.evaluate_detections("predictions", gt_field="ground_truth")
     9
    10# The top-10 most common classes
    11counts = dataset.count_values("ground_truth.detections.label")
    12classes = sorted(counts, key=counts.get, reverse=True)[:10]
    13
    14session = fo.launch_app(dataset)
    
    
    
    1# Plot confusion matrix
    2plot = results.plot_confusion_matrix(classes=classes)
    3plot.show(height=600)
    4
    5session.plots.attach(plot)
    

![detection-evaluation](../_images/detection-evaluation.gif)

When you pass an `eval_key` to [`evaluate_detections()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.evaluate_detections "fiftyone.core.collections.SampleCollection.evaluate_detections"), confusion matrices attached to App instances have a different default behavior: when you select cell(s), the corresponding [evaluation patches](user_guide__evaluation.md#evaluation-patches) for the run are shown in the App. This allows you to visualize each TP, FP, and FN example in a fine-grained manner:
    
    
    1results = dataset.evaluate_detections(
    2    "predictions", gt_field="ground_truth", eval_key="eval"
    3)
    
    
    
    1# Since these results have an `eval_key`, selecting cells in this plot will
    2# load evaluation patch views
    3plot = results.plot_confusion_matrix(classes=classes)
    4plot.show(height=600)
    5
    6session.plots.attach(plot)
    

![detection-evaluation-patches](../_images/detection-evaluation-patches.gif)

If you prefer a different selection behavior, you can simply change the plotâs selection mode.

## View plots#

[`ViewPlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot "fiftyone.core.plots.base.ViewPlot") is a class of plots whose state is automatically updated whenever the current [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view") changes.

Current varieties of view plots include [`CategoricalHistogram`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram "fiftyone.core.plots.views.CategoricalHistogram"), [`NumericalHistogram`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram "fiftyone.core.plots.views.NumericalHistogram"), and [`ViewGrid`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid "fiftyone.core.plots.views.ViewGrid").

Note

New [`ViewPlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot "fiftyone.core.plots.base.ViewPlot") subclasses will be continually added over time, and it is also straightforward to implement your own custom view plots. Contributions are welcome at [voxel51/fiftyone](https://github.com/voxel51/fiftyone)!

The example below demonstrates the use of [`ViewGrid`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid "fiftyone.core.plots.views.ViewGrid") to construct a dashboard of histograms of various aspects of a dataset, which can then be attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") in order to automatically see how the statistics change when the sessionâs [`view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view") is modified.

Each block in the example code below denotes a separate cell in a Jupyter notebook:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6dataset.compute_metadata()
     7
     8# Define some interesting plots
     9plot1 = fo.NumericalHistogram(F("metadata.size_bytes") / 1024, bins=50, xlabel="image size (KB)")
    10plot2 = fo.NumericalHistogram("predictions.detections.confidence", bins=50, range=[0, 1])
    11plot3 = fo.CategoricalHistogram("ground_truth.detections.label", order="frequency")
    12plot4 = fo.CategoricalHistogram("predictions.detections.label", order="frequency")
    13
    14session = fo.launch_app(dataset)
    
    
    
    1# Construct a custom dashboard of plots
    2plot = fo.ViewGrid([plot1, plot2, plot3, plot4], init_view=dataset)
    3plot.show(height=720)
    4
    5session.plots.attach(plot)
    

![view-plots](../_images/view-plots.gif)

## Attaching plots to the App#

All [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") instances provide a [`plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute that you can use to attach [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances to the FiftyOne App.

When [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances are attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"), they are automatically updated whenever [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view") changes for any reason, whether you modify your view in the App, or programmatically change it by setting [`session.view`](api__fiftyone.core.session.md#fiftyone.core.session.Session.view "fiftyone.core.session.Session.view"), or if multiple plots are connected and another plot triggers a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") update!

Note

Interactive plots are currently only supported in Jupyter notebooks. In the meantime, you can still use FiftyOneâs plotting features in other environments, but you must manually call [`plot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.show "fiftyone.core.plots.base.Plot.show") to update the state of a plot to match the state of a connected [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"), and any callbacks that would normally be triggered in response to interacting with a plot will not be triggered.

See this section for more information.

### Attaching a plot#

The code below demonstrates the basic pattern of connecting a [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"):
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart-geo")
     5
     6session = fo.launch_app(dataset)
     7
     8# Create a responsive location plot
     9plot = fo.location_scatterplot(samples=dataset)
    10plot.show()  # show the plot
    11
    12# Attach the plot to the session
    13# Updates will automatically occur when the plot/session are updated
    14session.plots.attach(plot)
    

You can view details about the plots attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") by printing it:
    
    
    1print(session)
    
    
    
    Dataset:          quickstart-geo
    Media type:       image
    Num samples:      500
    Selected samples: 0
    Selected labels:  0
    Session URL:      http://localhost:5151/
    Connected plots:
        plot1: fiftyone.core.plots.plotly.InteractiveScatter
    

By default, plots are given sequential names `plot1`, `plot2`, etc., but you can customize their names via the optional `name` parameter of [`session.plots.attach()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.attach "fiftyone.core.plots.manager.PlotManager.attach").

You can retrieve a [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instance from its connected session by its name:
    
    
    1same_plot = session.plots["plot1"]
    2same_plot is plot  # True
    

### Connecting and disconnecting plots#

By default, when plots are attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"), they are _connected_ , which means that any necessary state updates will happen automatically. If you wish to temporarily suspend updates for an individual plot, you can use [`plot.disconnect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.disconnect "fiftyone.core.plots.base.ResponsivePlot.disconnect"):
    
    
    1# Disconnect an individual plot
    2# Plot updates will no longer update the session, and vice versa
    3plot.disconnect()
    4
    5# Note that `plot1` is now disconnected
    6print(session)
    
    
    
    Dataset:          quickstart-geo
    Media type:       image
    Num samples:      500
    Selected samples: 0
    Selected labels:  0
    Session URL:      http://localhost:5151/
    Disconnected plots:
        plot1: fiftyone.core.plots.plotly.InteractiveScatter
    

You can reconnect a plot by calling [`plot.connect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.connect "fiftyone.core.plots.base.ResponsivePlot.connect"):
    
    
    1# Reconnect an individual plot
    2plot.connect()
    3
    4# Note that `plot1` is connected again
    5print(session)
    
    
    
    Dataset:          quickstart-geo
    Media type:       image
    Num samples:      500
    Selected samples: 0
    Selected labels:  0
    Session URL:      http://localhost:5151/
    Connected plots:
        plot1: fiftyone.core.plots.plotly.InteractiveScatter
    

You can disconnect and reconnect all plots currently attached to a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") via [`session.plots.disconnect()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.disconnect "fiftyone.core.plots.manager.PlotManager.disconnect") and [`session.plots.connect()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.connect "fiftyone.core.plots.manager.PlotManager.connect"), respectively.

### Detaching plots#

If you would like to permanently detach a plot from a [`Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session"), use [`session.plots.pop()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.pop "fiftyone.core.plots.manager.PlotManager.pop") or [`session.plots.remove()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.remove "fiftyone.core.plots.manager.PlotManager.remove"):
    
    
    1# Detach plot from its session
    2plot = session.plots.pop("plot1")
    3
    4# Note that `plot1` no longer appears
    5print(session)
    
    
    
    Dataset:          quickstart-geo
    Media type:       image
    Num samples:      500
    Selected samples: 0
    Selected labels:  0
    Session URL:      http://localhost:5151/
    

### Freezing plots#

Working with interactive plots in notebooks is an amazingly productive experience. However, when you find something particularly interesting that you want to save, or you want to share a notebook with a colleague without requiring them to rerun all of the cells to reproduce your results, you may want to _freeze_ your responsive plots.

You can conveniently freeze your currently active App instance and any attached plots by calling [`session.freeze()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.freeze "fiftyone.core.session.Session.freeze"):
    
    
    1# Replace current App instance and all attached plots with static images
    2session.freeze()
    

After calling this method, your current App instance and all connected plots will be replaced by static images that will be visible when you save + reopen your notebook later.

You can also freeze an individual plot by calling [`plot.freeze()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.freeze "fiftyone.core.plots.base.ResponsivePlot.freeze"):
    
    
    1# Replace a plot with a static image
    2plot.freeze()
    

You can âreviveâ frozen App and plot instances by simply rerunning the notebook cells in which they were defined and shown.

Note

[`session.freeze()`](api__fiftyone.core.session.md#fiftyone.core.session.Session.freeze "fiftyone.core.session.Session.freeze") and [`plot.freeze()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.freeze "fiftyone.core.plots.base.ResponsivePlot.freeze") are only applicable when working in notebook contexts.

## Saving plots#

You can use [`plot.save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.save "fiftyone.core.plots.base.Plot.save") to save any [`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") or [`ViewPlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot "fiftyone.core.plots.base.ViewPlot") as a static image or HTML.

Consult the documentation of your plotâs [`save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.save "fiftyone.core.plots.base.Plot.save") method for details on configuring the export.

For example, you can save a histogram view plot:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3
     4dataset = foz.load_zoo_dataset("quickstart")
     5
     6plot = fo.CategoricalHistogram(
     7    "ground_truth.detections.label",
     8    order="frequency",
     9    log=True,
    10    init_view=dataset,
    11)
    12
    13plot.save("./histogram.jpg", scale=2.0)
    

![save-histogram](../_images/save-histogram.jpg)

  
Or you can save an embedding scatterplot:
    
    
    1import fiftyone.brain as fob
    2
    3results = fob.compute_visualization(dataset)
    4
    5plot = results.visualize(labels="uniqueness", axis_equal=True)
    6plot.save("./embeddings.png", height=300, width=800)
    

![save-embeddings](../_images/save-embeddings.png)

  
You can also save plots generated using the matplotlib backend:
    
    
    1plot = results.visualize(
    2    labels="uniqueness",
    3    backend="matplotlib",
    4    ax_equal=True,
    5    marker_size=5,
    6)
    7plot.save("./embeddings-matplotlib.png", dpi=200)
    

![save-embeddings-matplotlib](../_images/save-embeddings-matplotlib.png)

## Advanced usage#

### Customizing plot layouts#

The [`plot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.show "fiftyone.core.plots.base.Plot.show") method used to display plots in FiftyOne supports optional keyword arguments that you can use to customize the look-and-feel of plots.

In general, consult the documentation of the relevant [`plot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.show "fiftyone.core.plots.base.Plot.show") method for details on the supported parameters.

If you are using the default plotly backend, [`plot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.show "fiftyone.core.plots.base.Plot.show") will accept any valid keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)").

The examples below demonstrate some common layout customizations that you may wish to perform:
    
    
    1# Increase the default height of the figure, in pixels
    2plot.show(height=720)
    3
    4# Equivalent of `axis("equal")` in matplotlib
    5plot.show(yaxis_scaleanchor="x")
    

Note

Refer to the [plotly layout documentation](https://plotly.com/python/reference/layout) for a full list of the supported options.

### Plot selection modes#

When working with scatterplots and interactive heatmaps that are linked to frames or labels, you may prefer to see different views loaded in the App when you make a selection in the plot. For example, you may want to see the corresponding objects in a [patches view](https://docs.voxel51.com/user_guide/using_views.html#object-patches-views), or you may wish to see the samples containing the objects but with all other labels also visible.

You can use the [`selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode "fiftyone.core.plots.base.InteractivePlot.selection_mode") property of [`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") instances to change the behavior of App updates when selections are made in connected plots.

When a plot is linked to frames, the available [`selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode "fiftyone.core.plots.base.InteractivePlot.selection_mode") options are:

  * `"select"` (_default_): show video samples with labels only for the selected frames

  * `"match"`: show unfiltered video samples containing at least one selected frame

  * `"frames"`: show only the selected frames in a frames view




When a plot is linked to labels, the available [`selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode "fiftyone.core.plots.base.InteractivePlot.selection_mode") options are:

  * `"patches"` (_default_): show the selected labels in a patches view

  * `"select"`: show only the selected labels

  * `"match"`: show unfiltered samples containing at least one selected label




For example, by default, clicking on cells in a confusion matrix for a [detection evaluation](user_guide__evaluation.md#evaluating-detections-coco) will show the corresponding ground truth and predicted objects in an [evaluation patches view](user_guide__evaluation.md#evaluation-patches) view in the App. Run the code blocks below in Jupyter notebook cells to see this:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7results = dataset.evaluate_detections(
     8    "predictions", gt_field="ground_truth", eval_key="eval"
     9)
    10
    11# Get the 10 most common classes in the dataset
    12counts = dataset.count_values("ground_truth.detections.label")
    13classes = sorted(counts, key=counts.get, reverse=True)[:10]
    14
    15session = fo.launch_app(dataset)
    
    
    
    1plot = results.plot_confusion_matrix(classes=classes)
    2plot.show(height=600)
    3
    4session.plots.attach(plot, name="eval")
    

However, you can change this behavior by updating the [`selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode "fiftyone.core.plots.base.InteractivePlot.selection_mode") property of the plot like so:
    
    
    1# Selecting cells will now show unfiltered samples containing selected objects
    2plot.selection_mode = "match"
    
    
    
    1# Selecting cells will now show filtered samples containing only selected objects
    2plot.selection_mode = "select"
    

Similarly, selecting scatter points in an [object embeddings visualization](brain.md#brain-embeddings-visualization) will show the corresponding objects in the App as a [patches view](https://docs.voxel51.com/user_guide/using_views.html#object-patches-views):
    
    
    1# Continuing from the code above
    2session.freeze()
    
    
    
     1import fiftyone.brain as fob
     2
     3results = fob.compute_visualization(
     4    dataset, patches_field="ground_truth", brain_key="gt_viz"
     5)
     6
     7# Restrict visualization to the 10 most common classes
     8view = dataset.filter_labels("ground_truth", F("label").is_in(classes))
     9results.use_view(view)
    10
    11session.show()
    
    
    
    1plot = results.visualize(labels="ground_truth.detections.label")
    2plot.show(height=800)
    3
    4session.plots.attach(plot, name="gt_viz")
    

However, you can change this behavior by updating the [`selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode "fiftyone.core.plots.base.InteractivePlot.selection_mode") property of the plot:
    
    
    1# Selecting points will now show unfiltered samples containing selected objects
    2plot.selection_mode = "match"
    
    
    
    1# Selecting points will now show filtered samples containing only selected objects
    2plot.selection_mode = "select"
    

Note

The App will immediately update when you set the [`selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode "fiftyone.core.plots.base.InteractivePlot.selection_mode") property of an [`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") connected to the App.

### Plotting backend#

Most plotting methods in the [`fiftyone.core.plots()`](api__fiftyone.core.plots.md#module-fiftyone.core.plots "fiftyone.core.plots") module provide an optional `backend` parameter that you can use to control the plotting backend used to render plots.

The default plotting backend is `plotly`, which is highly recommended due to its better performance, look-and-feel, and greater support for interactivity.

However, most plot types also support the `matplotlib` backend. If you chose this backend, plots will be rendered as matplotlib figures. Many matplotlib-powered plot types support interactivity, but you must enable this behavior:
    
    
     1import fiftyone as fo
     2import fiftyone.zoo as foz
     3from fiftyone import ViewField as F
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6results = dataset.evaluate_detections("predictions", gt_field="ground_truth")
     7
     8# Get the 10 most common classes in the dataset
     9counts = dataset.count_values("ground_truth.detections.label")
    10classes = sorted(counts, key=counts.get, reverse=True)[:10]
    
    
    
    1# Use the default plotly backend
    2plot = results.plot_confusion_matrix(classes=classes)
    3plot.show(height=512)
    

![plotly-backend](../_images/plotly-backend.png)
    
    
    1import matplotlib.pyplot as plt
    2
    3# Use the matplotlib backend instead
    4figure = results.plot_confusion_matrix(
    5    classes=classes, backend="matplotlib", figsize=(10, 10)
    6)
    7plt.show(block=False)
    

![matplotlib-backend](../_images/matplotlib-backend.png)

### Interactive matplotlib plots#

If you are using the matplotlib backend, many FiftyOne plots still support interactivity in notebooks, but you must enable this behavior by running the appropriate magic command in your notebook _before_ you generate your first plot.

If you forget or choose not to run a magic command, the plots will still display, but they will not be interactive.

Follow the instructions for your environment below to enable interactive matplotlib plots:

The recommended way to enable interactive matplotlib plots in Jupyter notebooks is to use the `%matplotlib notebook` magic command, which enables the `nbagg backend` that was [introduced in matplotlib v1.4](https://matplotlib.org/stable/users/prev_whats_new/whats_new_1.4.html#the-nbagg-backend):
    
    
    %matplotlib notebook
    

Alternatively, you can install the [ipympl package](https://github.com/matplotlib/ipympl), which uses the Jupyter widgets framework to make matplotlib plots interactive:
    
    
    pip install ipympl
    

Then you can enable interactive matplotlib plots in a notebook by including the following magic command:
    
    
    %matplotlib widget
    

You can use interactive matplotlib plots in JupyterLab by installing the [ipympl package](https://github.com/matplotlib/ipympl):
    
    
    pip install ipympl
    

Then you can enable interactive matplotlib plots in a notebook by including the following magic command:
    
    
    %matplotlib widget
    

If you run into any issues in JupyterLab, refer to [these instructions](https://github.com/matplotlib/ipympl#installation).

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
