---
source_url: https://docs.voxel51.com/api/fiftyone.core.plots.base.html
---

# fiftyone.core.plots.base#

Base plotting definitions.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`plot_confusion_matrix`(confusion_matrix,Â labels) | Plots a confusion matrix.  
---|---  
`plot_regressions`(ytrue,Â ypred[,Â samples,Â ...]) | Plots the given regression results.  
`plot_pr_curve`(precision,Â recall[,Â ...]) | Plots a precision-recall (PR) curve.  
`plot_pr_curves`(precisions,Â recall,Â classes) | Plots a set of per-class precision-recall (PR) curves.  
`plot_roc_curve`(fpr,Â tpr[,Â thresholds,Â ...]) | Plots a receiver operating characteristic (ROC) curve.  
`lines`([x,Â y,Â samples,Â ids,Â link_field,Â ...]) | Plots the given lines(s) data.  
`scatterplot`(points[,Â samples,Â ids,Â ...]) | Generates an interactive scatterplot of the given points.  
`location_scatterplot`([locations,Â samples,Â ...]) | Generates an interactive scatterplot of the given location coordinates with a map rendered in the background of the plot.  
  
**Classes:**

`Plot`() | Base class for all plots.  
---|---  
`ResponsivePlot`(link_type) | Base class for all responsive plots that can push/pull updates to a linked object.  
`ViewPlot`([init_view]) | Base class for plots that can be automatically populated given a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instance.  
`InteractivePlot`([link_type,Â init_view,Â ...]) | Base class for plots that support selection of their points.  
  
fiftyone.core.plots.base.plot_confusion_matrix(_confusion_matrix_ , _labels_ , _ids =None_, _samples =None_, _eval_key =None_, _gt_field =None_, _pred_field =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots a confusion matrix.

If `ids` are provided and you are working in a notebook environment with the default plotly backend, this method returns an interactive [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap") that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected cells in the confusion matrix.

Parameters:
    

  * **confusion_matrix** â a `num_true x num_preds` confusion matrix

  * **labels** â a `max(num_true, num_preds)` array-like of class labels

  * **ids** (_None_) â an array-like of same shape as `confusion_matrix` containing lists of IDs corresponding to each cell

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for which the confusion matrix was generated

  * **eval_key** (_None_) â the evaluation key of the evaluation

  * **gt_field** (_None_) â the name of the ground truth field

  * **pred_field** (_None_) â the name of the predictions field

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_confusion_matrix()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_confusion_matrix "fiftyone.core.plots.plotly.plot_confusion_matrix")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_confusion_matrix()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_confusion_matrix "fiftyone.core.plots.matplotlib.plot_confusion_matrix")



Returns:
    

one of the following

  * a [`fiftyone.core.plots.plotly.InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap "fiftyone.core.plots.plotly.InteractiveHeatmap"), if IDs are available and the plotly backend is used

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if no IDs are available but you are working in a Jupyter notebook with the plotly backend

  * a plotly or matplotlib figure, otherwise




fiftyone.core.plots.base.plot_regressions(_ytrue_ , _ypred_ , _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _classes =None_, _gt_field =None_, _pred_field =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots the given regression results.

If IDs are provided and you are working in a notebook environment with the default plotly backend, this method returns an interactive [`fiftyone.core.plots.plotly.InteractiveScatter`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter "fiftyone.core.plots.plotly.InteractiveScatter") that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected points in the plot.

Parameters:
    

  * **ytrue** â an array-like of ground truth values

  * **ypred** â an array-like of predicted values

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for which the results were generated. Only used by the âplotlyâ backend when IDs are provided

  * **ids** (_None_) â an array-like of sample or frame IDs corresponding to the regressions. If not provided but `samples` are provided, the appropriate IDs will be extracted from the samples

  * **labels** (_None_) â 

data to use to color the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric or string values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric or string values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric or string values

    * a list of array-likes of numeric or string values, if `link_field` refers to frames

  * **sizes** (_None_) â 

data to use to scale the sizes of the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric values

    * a list of array-likes of numeric or string values, if `link_field` refers to frames

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings

  * **gt_field** (_None_) â the name of the ground truth field

  * **pred_field** (_None_) â the name of the predictions field

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_confusion_matrix()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_confusion_matrix "fiftyone.core.plots.plotly.plot_confusion_matrix")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_confusion_matrix()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_confusion_matrix "fiftyone.core.plots.matplotlib.plot_confusion_matrix")



Returns:
    

one of the following

  * a [`fiftyone.core.plots.plotly.InteractiveScatter`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter "fiftyone.core.plots.plotly.InteractiveScatter"), if IDs are available and the plotly backend is used

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if no IDs are available but you are working in a Jupyter notebook with the plotly backend

  * a plotly or matplotlib figure, otherwise




fiftyone.core.plots.base.plot_pr_curve(_precision_ , _recall_ , _thresholds =None_, _label =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots a precision-recall (PR) curve.

Parameters:
    

  * **precision** â an array-like of precision values

  * **recall** â an array-like of recall values

  * **thresholds** (_None_) â an array-like of decision thresholds

  * **label** (_None_) â a label for the curve

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_pr_curve()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_pr_curve "fiftyone.core.plots.plotly.plot_pr_curve")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_pr_curve()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_pr_curve "fiftyone.core.plots.matplotlib.plot_pr_curve")



Returns:
    

one of the following

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if you are working in a Jupyter notebook and the plotly backend is used

  * a plotly or matplotlib figure, otherwise




fiftyone.core.plots.base.plot_pr_curves(_precisions_ , _recall_ , _classes_ , _thresholds =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots a set of per-class precision-recall (PR) curves.

Parameters:
    

  * **precisions** â a `num_classes x num_recalls` array-like of per-class precision values

  * **recall** â an array-like of recall values

  * **classes** â the list of classes

  * **thresholds** (_None_) â an `num_classes x num_recalls` array-like of decision thresholds

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_pr_curves()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_pr_curves "fiftyone.core.plots.plotly.plot_pr_curves")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_pr_curves()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_pr_curves "fiftyone.core.plots.matplotlib.plot_pr_curves")



Returns:
    

one of the following

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if you are working in a Jupyter notebook and the plotly backend is used

  * a plotly or matplotlib figure, otherwise




fiftyone.core.plots.base.plot_roc_curve(_fpr_ , _tpr_ , _thresholds =None_, _roc_auc =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots a receiver operating characteristic (ROC) curve.

Parameters:
    

  * **fpr** â an array-like of false positive rates

  * **tpr** â an array-like of true positive rates

  * **thresholds** (_None_) â an array-like of decision thresholds

  * **roc_auc** (_None_) â the area under the ROC curve

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.plot_roc_curve()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_roc_curve "fiftyone.core.plots.plotly.plot_roc_curve")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.plot_roc_curve()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_roc_curve "fiftyone.core.plots.matplotlib.plot_roc_curve")



Returns:
    

one of the following

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if you are working in a Jupyter notebook and the plotly backend is used

  * a plotly or matplotlib figure, otherwise




fiftyone.core.plots.base.lines(_x =None_, _y =None_, _samples =None_, _ids =None_, _link_field =None_, _sizes =None_, _backend ='plotly'_, _** kwargs_)#
    

Plots the given lines(s) data.

You can attach plots generated by this method to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected points in the plot. To enable this functionality, you must pass `samples` to this method.

You can use the `sizes` parameter to scale the sizes of the points.

Parameters:
    

  * **x** (_None_) â 

the x data to plot. Can be any of the following:

    * an array-like of values

    * a `num_lines x n` array-like or list of length `num_lines` of array-likes of values for multiple line traces

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract values for a single line

    * the name of a frame field or `frames.embedded.field.name` of `samples` from which to extract values for per-sample line traces

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") that resolves to a list (one line plot) or list of lists (multiple line plots) of numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

  * **y** (_None_) â 

the y data to plot. Can be any of the following:

    * an array-like of values

    * a `num_lines x n` array-like or list of length `num_lines` of array-likes of values for multiple line traces

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract values for a single line

    * the name of a frame field or `frames.embedded.field.name` of `samples` from which to extract values for per-sample line traces

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") that resolves to a list (one line plot) or list of lists (multiple line plots) of numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose data is being visualized

  * **ids** (_None_) â an array-like of IDs of same shape as `y`. If not provided but `samples` are provided, the appropriate IDs will be extracted from the samples

  * **link_field** (_None_) â 

a field of `samples` whose data corresponds to `y`. Can be any of the following:

    * `None`, if the line data correspond to samples (single trace) or frames (multiple traces)

    * `"frames"`, if the line data correspond to frames (multiple traces). This option exists only for consistency with other plotting methods; in practice, it will be automatically inferred whenever multiple traces are being plotted

    * the name of a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field, if the line data correspond to the labels in this field

  * **sizes** (_None_) â 

data to use to scale the sizes of the points. Can be any of the following:

    * an array-like of numeric values of same shape as `y`

    * the name of a sample field (single trace) or frame field (multiple traces) from which to extract numeric values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining sample-level (single trace) or frame-level (multiple traces) numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.lines()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.lines "fiftyone.core.plots.plotly.lines")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.lines()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.lines "fiftyone.core.plots.matplotlib.lines")



Returns:
    

one of the following

  * an `InteractivePlot`, if IDs are available

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if IDs are not available but you are working with the plotly backend in a Jupyter notebook

  * a plotly or matplotlib figure, otherwise




fiftyone.core.plots.base.scatterplot(_points_ , _samples =None_, _ids =None_, _link_field =None_, _labels =None_, _sizes =None_, _classes =None_, _backend ='plotly'_, _** kwargs_)#
    

Generates an interactive scatterplot of the given points.

You can attach plots generated by this method to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected points in the plot. To enable this functionality, you must pass `samples` to this method.

This method supports 2D or 3D visualizations, but interactive point selection is only available in 2D.

You can use the `labels` parameters to define a coloring for the points, and you can use the `sizes` parameter to scale the sizes of the points.

Parameters:
    

  * **points** â a `num_points x num_dims` array-like of points

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose data is being visualized

  * **ids** (_None_) â an array-like of IDs corresponding to the points. If not provided but `samples` are provided, the appropriate IDs will be extracted from the samples

  * **link_field** (_None_) â 

a field of `samples` whose data corresponds to `points`. Can be any of the following:

    * None, if the points correspond to samples

    * `"frames"`, if the points correspond to frames

    * the name of a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field, if the points linked to the labels in this field

  * **labels** (_None_) â 

data to use to color the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric or string values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric or string values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric or string values

    * a list of array-likes of numeric or string values, if `link_field` refers to a label list field like [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

  * **sizes** (_None_) â 

data to use to scale the sizes of the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric values

    * a list of array-likes of numeric or string values, if `link_field` refers to a label list field like [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

  * **classes** (_None_) â an list of classes whose points to plot. Only applicable when `labels` contains strings

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.scatterplot()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.scatterplot "fiftyone.core.plots.plotly.scatterplot")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.scatterplot()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.scatterplot "fiftyone.core.plots.matplotlib.scatterplot")



Returns:
    

one of the following

  * an `InteractivePlot`, if IDs are available

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if IDs are not available but you are working with the plotly backend in a Jupyter notebook

  * a plotly or matplotlib figure, otherwise




fiftyone.core.plots.base.location_scatterplot(_locations =None_, _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _classes =None_, _backend ='plotly'_, _** kwargs_)#
    

Generates an interactive scatterplot of the given location coordinates with a map rendered in the background of the plot.

Location data is specified via the `locations` parameter.

You can attach plots generated by this method to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected points in the plot. To enable this functionality, you must pass `samples` to this method.

You can use the `labels` parameters to define a coloring for the points, and you can use the `sizes` parameter to scale the sizes of the points.

Parameters:
    

  * **locations** (_None_) â 

the location data to plot. Can be any of the following:

    * None, in which case `samples` must have a single [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field whose `point` attribute contains location data

    * a `num_locations x 2` array of `(longitude, latitude)` coordinates

    * the name of a [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field of `samples` with `(longitude, latitude)` coordinates in its `point` attribute

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose data is being visualized

  * **ids** (_None_) â an array-like of IDs corresponding to the locations. If not provided but `samples` are provided, the appropriate IDs will be extracted from the samples

  * **labels** (_None_) â 

data to use to color the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric or string values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric or string values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric or string values

  * **sizes** (_None_) â 

data to use to scale the sizes of the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric values

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings

  * **backend** (_"plotly"_) â the plotting backend to use. Supported values are `("plotly", "matplotlib")`

  * ****kwargs** â 

keyword arguments for the backend plotting method:

    * âplotlyâ backend: [`fiftyone.core.plots.plotly.location_scatterplot()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.location_scatterplot "fiftyone.core.plots.plotly.location_scatterplot")

    * âmatplotlibâ backend: [`fiftyone.core.plots.matplotlib.location_scatterplot()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.location_scatterplot "fiftyone.core.plots.matplotlib.location_scatterplot")



Returns:
    

one of the following

  * an `InteractivePlot`, if IDs are available

  * a [`fiftyone.core.plots.plotly.PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot "fiftyone.core.plots.plotly.PlotlyNotebookPlot"), if IDs are not available but you are working with the plotly backend in a Jupyter notebook

  * a plotly or matplotlib figure, otherwise




class fiftyone.core.plots.base.Plot#
    

Bases: `object`

Base class for all plots.

**Attributes:**

`is_frozen` | Whether this plot is currently frozen.  
---|---  
  
**Methods:**

`show`(**kwargs) | Shows the plot.  
---|---  
`save`(path,Â **kwargs) | Saves the plot.  
`freeze`() | Freezes the plot, replacing it with a static image.  
  
property is_frozen#
    

Whether this plot is currently frozen.

show(_** kwargs_)#
    

Shows the plot.

Parameters:
    

****kwargs** â subclass-specific keyword arguments

save(_path_ , _** kwargs_)#
    

Saves the plot.

Parameters:
    

  * **path** â the path to write the plot

  * ****kwargs** â subclass-specific keyword arguments




freeze()#
    

Freezes the plot, replacing it with a static image.

Only applicable in notebook contexts.

class fiftyone.core.plots.base.ResponsivePlot(_link_type_)#
    

Bases: `Plot`

Base class for all responsive plots that can push/pull updates to a linked object.

Parameters:
    

**link_type** â the link type of the plot

**Attributes:**

`link_type` | The link type between this plot and a connected session.  
---|---  
`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
`is_connected` | Whether this plot is currently connected.  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
  
**Methods:**

`connect`() | Connects this plot, if necessary.  
---|---  
`show`(**kwargs) | Shows the plot.  
`reset`() | Resets the plot to its default state.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`disconnect`() | Disconnects the plot, if necessary.  
`save`(path,Â **kwargs) | Saves the plot.  
  
property link_type#
    

The link type between this plot and a connected session.

property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

property is_connected#
    

Whether this plot is currently connected.

property is_disconnected#
    

Whether this plot is currently disconnected.

property is_frozen#
    

Whether this plot is currently frozen.

connect()#
    

Connects this plot, if necessary.

show(_** kwargs_)#
    

Shows the plot.

The plot will be connected if necessary.

Parameters:
    

****kwargs** â subclass-specific keyword arguments

reset()#
    

Resets the plot to its default state.

freeze()#
    

Freezes the plot, replacing it with a static image.

The plot will also be disconnected.

Only applicable in notebook contexts.

disconnect()#
    

Disconnects the plot, if necessary.

save(_path_ , _** kwargs_)#
    

Saves the plot.

Parameters:
    

  * **path** â the path to write the plot

  * ****kwargs** â subclass-specific keyword arguments




class fiftyone.core.plots.base.ViewPlot(_init_view =None_)#
    

Bases: `ResponsivePlot`

Base class for plots that can be automatically populated given a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instance.

The state of `ViewPlot` instances can also be updated by external parties by calling its `update_view()` method.

Parameters:
    

**init_view** (_None_) â an initial [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to load

**Attributes:**

`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
---|---  
`is_connected` | Whether this plot is currently connected.  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
  
**Methods:**

`update_view`(view[,Â agg_results]) | Updates the plot based on the provided view.  
---|---  
`reset`() | Resets the plot to its default state.  
`connect`() | Connects this plot, if necessary.  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`save`(path,Â **kwargs) | Saves the plot.  
`show`(**kwargs) | Shows the plot.  
  
property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

update_view(_view_ , _agg_results =None_)#
    

Updates the plot based on the provided view.

Parameters:
    

  * **view** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **agg_results** (_None_) â a list of pre-computed aggregation results




reset()#
    

Resets the plot to its default state.

connect()#
    

Connects this plot, if necessary.

disconnect()#
    

Disconnects the plot, if necessary.

freeze()#
    

Freezes the plot, replacing it with a static image.

The plot will also be disconnected.

Only applicable in notebook contexts.

property is_connected#
    

Whether this plot is currently connected.

property is_disconnected#
    

Whether this plot is currently disconnected.

property is_frozen#
    

Whether this plot is currently frozen.

property link_type#
    

The link type between this plot and a connected session.

save(_path_ , _** kwargs_)#
    

Saves the plot.

Parameters:
    

  * **path** â the path to write the plot

  * ****kwargs** â subclass-specific keyword arguments




show(_** kwargs_)#
    

Shows the plot.

The plot will be connected if necessary.

Parameters:
    

****kwargs** â subclass-specific keyword arguments

class fiftyone.core.plots.base.InteractivePlot(_link_type ='samples'_, _init_view =None_, _label_fields =None_, _selection_mode =None_, _init_fcn =None_)#
    

Bases: `ResponsivePlot`

Base class for plots that support selection of their points.

Whenever a selection is made in an `InteractivePlot`, the plot will invoke any selection callback(s) registered on it, reporting to its listeners the IDs of its selected points.

Conversely, the state of an `InteractivePlot` can be updated by external parties by calling its `select_ids()` method.

Parameters:
    

  * **link_type** (_"samples"_) â whether this plot is linked to `"samples"`, `"frames"`, or `"labels"`

  * **init_view** (_None_) â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining an initial view from which to derive selection views when points are selected in the plot. This view will also be shown when the plot is in its default state (no selection)

  * **label_fields** (_None_) â a label field or list of label fields to which points in this plot correspond. Only applicable when `link_type == "labels"`

  * **selection_mode** (_None_) â the initial selection mode to use when updating connected sessions in response to selections in this plot. See `selection_mode()` for details

  * **init_fcn** (_None_) â a function that can be called with `init_view` as its argument that returns a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining an initial view from which to derive certain types of selection views. See `selection_mode()` for details




**Attributes:**

`selection_mode` | The current selection mode of the plot.  
---|---  
`init_view` | A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.  
`selected_ids` | A list of IDs of the currently selected points.  
`is_connected` | Whether this plot is currently connected.  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
  
**Methods:**

`recommend_link_type`([label_field,Â samples]) | Recommends a link type for the given info.  
---|---  
`register_selection_callback`(callback) | Registers a selection callback for this plot.  
`register_sync_callback`(callback) | Registers a callback that can sync this plot with a `SessionPlot` connected to it.  
`register_disconnect_callback`(callback) | Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.  
`select_ids`(ids[,Â view]) | Selects the points with the given IDs in this plot.  
`connect`() | Connects this plot, if necessary.  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`save`(path,Â **kwargs) | Saves the plot.  
`show`(**kwargs) | Shows the plot.  
`reset`() | Resets the plot to its default state.  
  
property selection_mode#
    

The current selection mode of the plot.

This property controls how the current view is updated in response to updates from `InteractivePlot` instances that are linked to labels or frames.

When `link_type` is `"frames"`, the supported values are:

  * `"select"`: show video samples with labels only for the selected frames

  * `"match"`: show unfiltered video samples containing at least one selected frame

  * `"frames"`: show only the selected frames in a frames view




When `link_type` is `"labels"`, the supported values are:

  * `"select"`: show only the selected labels

  * `"match"`: show unfiltered samples containing at least one selected label

  * `"patches"`: show the selected labels in a patches view




Note

In order to use `"patches"` selection mode, you must have provided an `init_fcn` when constructing this plot that defines how to create the base patches view. This usually involves [`to_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_patches "fiftyone.core.collections.SampleCollection.to_patches") or [`to_evaluation_patches()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_evaluation_patches "fiftyone.core.collections.SampleCollection.to_evaluation_patches")

Note

In order to use `"frames"` selection mode, you must have provided an `init_fcn` when constructing this plot that defines how to create the base frames view. This usually involves [`to_frames()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.to_frames "fiftyone.core.collections.SampleCollection.to_frames")

property init_view#
    

A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.

This view will also be shown when the plot is in its default state (no selection).

property selected_ids#
    

A list of IDs of the currently selected points.

An empty list means all points are deselected, and None means default state (nothing selected or unselected).

If the plot is not connected, returns None.

static recommend_link_type(_label_field =None_, _samples =None_)#
    

Recommends a link type for the given info.

Parameters:
    

  * **label_field** (_None_) â the label field, if any

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection"), if known



Returns:
    

a `(link_type, label_fields, selection_mode, init_fcn)` tuple

register_selection_callback(_callback_)#
    

Registers a selection callback for this plot.

Selection callbacks are functions that take a single argument containing the list of currently selected IDs.

If a selection callback is registered, this plot should invoke it each time their selection is updated.

Parameters:
    

**callback** â a selection callback

register_sync_callback(_callback_)#
    

Registers a callback that can sync this plot with a `SessionPlot` connected to it.

The typical use case for this function is to serve as the callback for a `sync` button on the plot.

Parameters:
    

**callback** â a function with no arguments

register_disconnect_callback(_callback_)#
    

Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.

The typical use case for this function is to serve as the callback for a `disconnect` button on the plot.

Parameters:
    

**callback** â a function with no arguments

select_ids(_ids_ , _view =None_)#
    

Selects the points with the given IDs in this plot.

Parameters:
    

  * **ids** â a list of IDs, or None to reset the plot to its default state

  * **view** (_None_) â the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") corresponding to the given IDs, if available




connect()#
    

Connects this plot, if necessary.

disconnect()#
    

Disconnects the plot, if necessary.

freeze()#
    

Freezes the plot, replacing it with a static image.

The plot will also be disconnected.

Only applicable in notebook contexts.

property is_connected#
    

Whether this plot is currently connected.

property is_disconnected#
    

Whether this plot is currently disconnected.

property is_frozen#
    

Whether this plot is currently frozen.

property link_type#
    

The link type between this plot and a connected session.

save(_path_ , _** kwargs_)#
    

Saves the plot.

Parameters:
    

  * **path** â the path to write the plot

  * ****kwargs** â subclass-specific keyword arguments




show(_** kwargs_)#
    

Shows the plot.

The plot will be connected if necessary.

Parameters:
    

****kwargs** â subclass-specific keyword arguments

property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

reset()#
    

Resets the plot to its default state.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
