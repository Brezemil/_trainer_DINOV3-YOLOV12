---
source_url: https://docs.voxel51.com/api/fiftyone.core.plots.plotly.html
---

# fiftyone.core.plots.plotly#

Plotly plots.

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
`get_colormap`(colorscale[,Â n,Â hex_strs]) | Generates a continuous colormap with the specified number of colors from the given plotly colorscale.  
  
**Classes:**

`PlotlyWidgetMixin`(widget) | Mixin for Plotly plots that use widgets to display in Jupyter notebooks.  
---|---  
`PlotlyNotebookPlot`(figure) | A wrapper around a Plotly plot for Jupyter notebook contexts that allows it to be replaced with a screenshot by calling `freeze()`.  
`PlotlyInteractivePlot`(widget,Â **kwargs) | Base class for [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") instances with Plotly backends.  
`InteractiveScatter`(figure,Â **kwargs) | Wrapper class that turns a Plotly figure containing one or more scatter-type traces into an [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot").  
`InteractiveHeatmap`(Z,Â ids[,Â xlabels,Â ...]) | An interactive Plotly heatmap.  
  
fiftyone.core.plots.plotly.plot_confusion_matrix(_confusion_matrix_ , _labels_ , _ids =None_, _samples =None_, _eval_key =None_, _gt_field =None_, _pred_field =None_, _colorscale ='oranges'_, _log_colorscale =False_, _title =None_, _** kwargs_)#
    

Plots a confusion matrix.

If `ids` are provided, this method returns a `InteractiveHeatmap` that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected cells in the confusion matrix.

Parameters:
    

  * **confusion_matrix** â a `num_true x num_preds` confusion matrix

  * **labels** â a `max(num_true, num_preds)` array-like of class labels

  * **ids** (_None_) â an array-like of same shape as `confusion_matrix` whose elements are array-likes of label IDs corresponding to each cell

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for which the confusion matrix was generated. Only used when `ids` are also provided to update an attached session

  * **eval_key** (_None_) â the evaluation key of the evaluation

  * **gt_field** (_None_) â the name of the ground truth field

  * **pred_field** (_None_) â the name of the predictions field

  * **colorscale** (_"oranges"_) â a plotly colorscale to use. See <https://plotly.com/python/colorscales> for options

  * **log_colorscale** (_False_) â whether to apply the colorscale on a log scale. This is useful to better visualize variations in smaller values when large values are also present

  * **title** (_None_) â a title for the plot

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * a `InteractiveHeatmap`, if `ids` are provided

  * a `PlotlyNotebookPlot`, if no `ids` are provided and you are working in a Jupyter notebook

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.plot_regressions(_ytrue_ , _ypred_ , _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _classes =None_, _gt_field =None_, _pred_field =None_, _figure =None_, _best_fit_label =None_, _marker_size =None_, _title =None_, _labels_title =None_, _sizes_title =None_, _show_colorbar_title =None_, _** kwargs_)#
    

Plots the given regression results.

If IDs are provided and you are working in a notebook environment with the default plotly backend, this method returns an `InteractiveScatter` plot that you can attach to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected points in the plot.

Parameters:
    

  * **ytrue** â an array-like of ground truth values

  * **ypred** â an array-like of predicted values

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") for which the results were generated. Only used by the âplotlyâ backend when IDs are provided

  * **ids** (_None_) â an array-like of IDs corresponding to the regressions

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

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings. If provided, the element order of this list also controls the z-order and legend order of multitrace plots (first class is rendered first, and thus on the bottom, and appears first in the legend)

  * **gt_field** (_None_) â the name of the ground truth field

  * **pred_field** (_None_) â the name of the predictions field

  * **figure** (_None_) â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)") to which to add the plot

  * **best_fit_label** (_None_) â a custom legend label for the best fit line

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **title** (_None_) â a title for the plot

  * **labels_title** (_None_) â a title string to use for `labels` in the tooltip and the colorbar title. By default, if `labels` is a field name, this name will be used, otherwise the colorbar will not have a title and the tooltip will use âlabelâ

  * **sizes_title** (_None_) â a title string to use for `sizes` in the tooltip. By default, if `sizes` is a field name, this name will be used, otherwise the tooltip will use âsizeâ

  * **show_colorbar_title** (_None_) â whether to show the colorbar title. By default, a title will be shown only if a value was passed to `labels_title` or an appropriate default can be inferred from the `labels` parameter

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * a `InteractiveScatter`, if IDs are provided

  * a `PlotlyNotebookPlot`, if no IDs are provided but you are working in a Jupyter notebook

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.plot_pr_curve(_precision_ , _recall_ , _thresholds =None_, _label =None_, _style ='area'_, _figure =None_, _title =None_, _** kwargs_)#
    

Plots a precision-recall (PR) curve.

Parameters:
    

  * **precision** â an array-like of precision values

  * **recall** â an array-like of recall values

  * **thresholds** (_None_) â an array-like of decision thresholds

  * **label** (_None_) â a label for the curve

  * **style** (_"area"_) â a plot style to use. Supported values are `("area", "line")`

  * **figure** (_None_) â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)") to which to add the plot

  * **title** (_None_) â a title for the plot

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * a `PlotlyNotebookPlot`, if you are working in a Jupyter notebook

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.plot_pr_curves(_precisions_ , _recall_ , _classes_ , _thresholds =None_, _figure =None_, _title =None_, _** kwargs_)#
    

Plots a set of per-class precision-recall (PR) curves.

Parameters:
    

  * **precisions** â a `num_classes x num_recalls` array-like of per-class precision values

  * **recall** â an array-like of recall values

  * **classes** â the list of classes

  * **thresholds** (_None_) â a `num_classes x num_recalls` array-like of decision thresholds

  * **figure** (_None_) â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)") to which to add the plots

  * **title** (_None_) â a title for the plot

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * a `PlotlyNotebookPlot`, if you are working in a Jupyter notebook

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.plot_roc_curve(_fpr_ , _tpr_ , _thresholds =None_, _roc_auc =None_, _style ='area'_, _figure =None_, _title =None_, _** kwargs_)#
    

Plots a receiver operating characteristic (ROC) curve.

Parameters:
    

  * **fpr** â an array-like of false positive rates

  * **tpr** â an array-like of true positive rates

  * **thresholds** (_None_) â an array-like of decision thresholds

  * **roc_auc** (_None_) â the area under the ROC curve

  * **style** (_"area"_) â a plot style to use. Supported values are `("area", "line")`

  * **figure** (_None_) â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)") to which to add the plot

  * **title** (_None_) â a title for the plot

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * a `PlotlyNotebookPlot`, if you are working in a Jupyter notebook

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.lines(_x =None_, _y =None_, _samples =None_, _ids =None_, _link_field =None_, _sizes =None_, _labels =None_, _colors =None_, _marker_size =None_, _figure =None_, _title =None_, _xaxis_title =None_, _yaxis_title =None_, _sizes_title =None_, _axis_equal =False_, _** kwargs_)#
    

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

  * **labels** (_None_) â a name or list of names for the line traces

  * **colors** (_None_) â a list of colors to use for the line traces. See <https://plotly.com/python/colorscales> for options

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **figure** (_None_) â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)") to which to add the plot

  * **title** (_None_) â a title for the plot

  * **xaxis_title** (_None_) â an x-axis title

  * **yaxis_title** (_None_) â a y-axis title

  * **sizes_title** (_None_) â a title string to use for `sizes` in the tooltip. By default, if `sizes` is a field name, this name will be used, otherwise the tooltip will use âsizeâ

  * **axis_equal** (_False_) â whether to set the axes to equal scale

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * an `InteractiveScatter`, when IDs are available

  * a `PlotlyNotebookPlot`, if youâre working in a Jupyter notebook but the above conditions arenât met

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.scatterplot(_points_ , _samples =None_, _ids =None_, _link_field =None_, _labels =None_, _sizes =None_, _edges =None_, _classes =None_, _figure =None_, _multi_trace =None_, _marker_size =None_, _colorscale =None_, _log_colorscale =False_, _title =None_, _trace_title =None_, _labels_title =None_, _sizes_title =None_, _edges_title =None_, _show_colorbar_title =None_, _axis_equal =False_, _** kwargs_)#
    

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

    * the name of a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field, if the points correspond to the labels in this field

  * **labels** (_None_) â 

data to use to color the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric or string values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric or string values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric or string values

    * a list of array-likes of numeric or string values, if `link_field` refers to frames and/or a label list field like [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

  * **sizes** (_None_) â 

data to use to scale the sizes of the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric values

    * a list of array-likes of numeric or string values, if `link_field` refers to frames and/or a label list field like [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

  * **edges** (_None_) â a `num_edges x 2` array of row indices into `points` defining undirected edges between points to render as a separate trace on the scatterplot

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings. If provided, the element order of this list also controls the z-order and legend order of multitrace plots (first class is rendered first, and thus on the bottom, and appears first in the legend)

  * **figure** (_None_) â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)") to which to add the plot

  * **multi_trace** (_None_) â whether to render each class as a separate trace. Only applicable when `labels` contains strings. By default, this will be true if there are up to 25 classes

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **colorscale** (_None_) â a plotly colorscale to use. Only applicable when `labels` contains numeric data. See <https://plotly.com/python/colorscales> for options

  * **log_colorscale** (_False_) â whether to apply the colorscale on a log scale. This is useful to better visualize variations in smaller values when large values are also present

  * **title** (_None_) â a title for the plot

  * **trace_title** (_None_) â a name for the scatter trace. Only applicable when plotting a single trace

  * **labels_title** (_None_) â a title string to use for `labels` in the tooltip and the colorbar title. By default, if `labels` is a field name, this name will be used, otherwise the colorbar will not have a title and the tooltip will use âlabelâ

  * **sizes_title** (_None_) â a title string to use for `sizes` in the tooltip. By default, if `sizes` is a field name, this name will be used, otherwise the tooltip will use âsizeâ

  * **edges_title** (_None_) â a title string to use for `edges` in the legend. If none is provided, edges are not included in the legend

  * **show_colorbar_title** (_None_) â whether to show the colorbar title. By default, a title will be shown only if a value was passed to `labels_title` or an appropriate default can be inferred from the `labels` parameter

  * **axis_equal** (_False_) â whether to set the axes to equal scale

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * an `InteractiveScatter`, for 2D points and when IDs are available

  * a `PlotlyNotebookPlot`, if youâre working in a Jupyter notebook but the above conditions arenât met

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.location_scatterplot(_locations =None_, _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _edges =None_, _classes =None_, _style =None_, _radius =None_, _figure =None_, _multi_trace =None_, _marker_size =None_, _colorscale =None_, _log_colorscale =False_, _title =None_, _trace_title =None_, _labels_title =None_, _sizes_title =None_, _edges_title =None_, _show_colorbar_title =None_, _map_type ='roadmap'_, _** kwargs_)#
    

Generates an interactive scatterplot of the given location coordinates with a map rendered in the background of the plot.

Location data is specified via the `locations` parameter.

You can attach plots generated by this method to an App session via its [`fiftyone.core.session.Session.plots`](api__fiftyone.core.session.md#fiftyone.core.session.Session.plots "fiftyone.core.session.Session.plots") attribute, which will automatically sync the sessionâs view with the currently selected points in the plot. To enable this functionality, you must pass `samples` to this method.

You can use the `labels` parameters to define a coloring for the points, and you can use the `sizes` parameter to scale the sizes of the points.

Parameters:
    

  * **locations** (_None_) â 

the location data to plot. Can be any of the following:

    * None, in which case `samples` must have a single [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field whose `point` attribute contains location data

    * a `num_locations x 2` array-like of `(longitude, latitude)` coordinates

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

  * **edges** (_None_) â a `num_edges x 2` array-like of row indices into `locations` defining undirected edges between points to render as a separate trace on the scatterplot

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings. If provided, the element order of this list also controls the z-order and legend order of multitrace plots (first class is rendered first, and thus on the bottom, and appears first in the legend)

  * **style** (_None_) â the plot style to use. Only applicable when the color data is numeric. Supported values are `("scatter", "density")`

  * **radius** (_None_) â the radius of influence of each lat/lon point. Only applicable when `style` is âdensityâ. Larger values will make density plots smoother and less detailed

  * **figure** (_None_) â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)") to which to add the plot

  * **multi_trace** (_None_) â whether to render each class as a separate trace. Only applicable when `labels` contains strings. By default, this will be true if there are up to 25 classes

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **colorscale** (_None_) â a plotly colorscale to use. Only applicable when `labels` contains numeric data. See <https://plotly.com/python/colorscales> for options

  * **log_colorscale** (_False_) â whether to apply the colorscale on a log scale. This is useful to better visualize variations in smaller values when large values are also present

  * **title** (_None_) â a title for the plot

  * **trace_title** (_None_) â a name for the scatter trace. Only applicable when plotting a single trace

  * **labels_title** (_None_) â a title string to use for `labels` in the tooltip and the colorbar title. By default, if `labels` is a field name, this name will be used, otherwise the colorbar will not have a title and the tooltip will use âlabelâ

  * **sizes_title** (_None_) â a title string to use for `sizes` in the tooltip. By default, if `sizes` is a field name, this name will be used, otherwise the tooltip will use âsizeâ

  * **edges_title** (_None_) â a title string to use for `edges` in the legend. If none is provided, edges are not included in the legend

  * **show_colorbar_title** (_None_) â whether to show the colorbar title. By default, a title will be shown only if a value was passed to `labels_title` or an appropriate default can be inferred from the `labels` parameter

  * **map_type** (_"satellite"_) â the map type to render. Supported values are `("roadmap", "satellite")`

  * ****kwargs** â optional keyword arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")



Returns:
    

one of the following

  * an `InteractiveScatter`, if IDs are available

  * a `PlotlyNotebookPlot`, if IDs are not available but youâre working in a Jupyter notebook

  * a plotly figure, otherwise




fiftyone.core.plots.plotly.get_colormap(_colorscale_ , _n =256_, _hex_strs =False_)#
    

Generates a continuous colormap with the specified number of colors from the given plotly colorscale.

The provided `colorscale` can be any of the following:

  * The string name of any colorscale recognized by plotly. See <https://plotly.com/python/colorscales> for possible options

  * A manually-defined colorscale like the following:
        
        [
            [0.000, "rgb(165,0,38)"],
            [0.111, "rgb(215,48,39)"],
            [0.222, "rgb(244,109,67)"],
            [0.333, "rgb(253,174,97)"],
            [0.444, "rgb(254,224,144)"],
            [0.555, "rgb(224,243,248)"],
            [0.666, "rgb(171,217,233)"],
            [0.777, "rgb(116,173,209)"],
            [0.888, "rgb(69,117,180)"],
            [1.000, "rgb(49,54,149)"],
        ]
        




The colorscale will be sampled evenly at the required resolution in order to generate the colormap.

Parameters:
    

  * **colorscale** â a valid colorscale. See above for possible options

  * **n** (_256_) â the desired number of colors

  * **hex_strs** (_False_) â whether to return `#RRGGBB` hex strings rather than `(R, G, B)` tuples



Returns:
    

a list of `(R, G, B)` tuples in [0, 255], or, if `hex_strs` is True, a list of #RRGGBB strings

class fiftyone.core.plots.plotly.PlotlyWidgetMixin(_widget_)#
    

Bases: `object`

Mixin for Plotly plots that use widgets to display in Jupyter notebooks.

This class can still be used in non-Jupyter notebook environments, but the resulting figures will not be interactive.

Parameters:
    

**widget** â a [`plotly.graph_objects.FigureWidget`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.FigureWidget "\(in \)")

**Methods:**

`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
---|---  
  
save(_path_ , _width =None_, _height =None_, _scale =None_, _** kwargs_)#
    

Saves the plot as an image or HTML.

Parameters:
    

  * **path** â the path to write the image or HTML

  * **width** (_None_) â a desired width in pixels when saving as an image. By default, the layout width is used

  * **height** (_None_) â a desired height in pixels when saving as an image. By default, the layout height is used

  * **scale** (_None_) â a scale factor to apply to the layout dimensions. By default, this is 1.0

  * ****kwargs** â keyword arguments for `plotly:plotly.graph_objects.Figure.to_image()` or `plotly:plotly.graph_objects.Figure.write_html()`




class fiftyone.core.plots.plotly.PlotlyNotebookPlot(_figure_)#
    

Bases: `PlotlyWidgetMixin`, [`Plot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot "fiftyone.core.plots.base.Plot")

A wrapper around a Plotly plot for Jupyter notebook contexts that allows it to be replaced with a screenshot by calling `freeze()`.

Parameters:
    

**figure** â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)")

**Attributes:**

`is_frozen` | Whether this plot is currently frozen.  
---|---  
  
**Methods:**

`update_layout`(**kwargs) | Updates the layout of the plot.  
---|---  
`show`(**kwargs) | Shows the plot.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
  
property is_frozen#
    

Whether this plot is currently frozen.

update_layout(_** kwargs_)#
    

Updates the layout of the plot.

Parameters:
    

****kwargs** â valid arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

show(_** kwargs_)#
    

Shows the plot.

Parameters:
    

****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

freeze()#
    

Freezes the plot, replacing it with a static image.

save(_path_ , _width =None_, _height =None_, _scale =None_, _** kwargs_)#
    

Saves the plot as an image or HTML.

Parameters:
    

  * **path** â the path to write the image or HTML

  * **width** (_None_) â a desired width in pixels when saving as an image. By default, the layout width is used

  * **height** (_None_) â a desired height in pixels when saving as an image. By default, the layout height is used

  * **scale** (_None_) â a scale factor to apply to the layout dimensions. By default, this is 1.0

  * ****kwargs** â keyword arguments for `plotly:plotly.graph_objects.Figure.to_image()` or `plotly:plotly.graph_objects.Figure.write_html()`




class fiftyone.core.plots.plotly.PlotlyInteractivePlot(_widget_ , _** kwargs_)#
    

Bases: `PlotlyWidgetMixin`, [`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot")

Base class for [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") instances with Plotly backends.

Parameters:
    

  * **widget** â a [`plotly.graph_objects.FigureWidget`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.FigureWidget "\(in \)")

  * ****kwargs** â keyword arguments for the [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") constructor




**Methods:**

`update_layout`(**kwargs) | Updates the layout of the plot.  
---|---  
`show`(**kwargs) | Shows the plot.  
`connect`() | Connects this plot, if necessary.  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`recommend_link_type`([label_field,Â samples]) | Recommends a link type for the given info.  
`register_disconnect_callback`(callback) | Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.  
`register_selection_callback`(callback) | Registers a selection callback for this plot.  
`register_sync_callback`(callback) | Registers a callback that can sync this plot with a `SessionPlot` connected to it.  
`reset`() | Resets the plot to its default state.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
`select_ids`(ids[,Â view]) | Selects the points with the given IDs in this plot.  
  
**Attributes:**

`init_view` | A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.  
---|---  
`is_connected` | Whether this plot is currently connected.  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`selected_ids` | A list of IDs of the currently selected points.  
`selection_mode` | The current selection mode of the plot.  
`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
  
update_layout(_** kwargs_)#
    

Updates the layout of the plot.

Parameters:
    

****kwargs** â valid arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

show(_** kwargs_)#
    

Shows the plot.

Parameters:
    

****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

connect()#
    

Connects this plot, if necessary.

disconnect()#
    

Disconnects the plot, if necessary.

freeze()#
    

Freezes the plot, replacing it with a static image.

The plot will also be disconnected.

Only applicable in notebook contexts.

property init_view#
    

A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.

This view will also be shown when the plot is in its default state (no selection).

property is_connected#
    

Whether this plot is currently connected.

property is_disconnected#
    

Whether this plot is currently disconnected.

property is_frozen#
    

Whether this plot is currently frozen.

property link_type#
    

The link type between this plot and a connected session.

static recommend_link_type(_label_field =None_, _samples =None_)#
    

Recommends a link type for the given info.

Parameters:
    

  * **label_field** (_None_) â the label field, if any

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection"), if known



Returns:
    

a `(link_type, label_fields, selection_mode, init_fcn)` tuple

register_disconnect_callback(_callback_)#
    

Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.

The typical use case for this function is to serve as the callback for a `disconnect` button on the plot.

Parameters:
    

**callback** â a function with no arguments

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

reset()#
    

Resets the plot to its default state.

save(_path_ , _width =None_, _height =None_, _scale =None_, _** kwargs_)#
    

Saves the plot as an image or HTML.

Parameters:
    

  * **path** â the path to write the image or HTML

  * **width** (_None_) â a desired width in pixels when saving as an image. By default, the layout width is used

  * **height** (_None_) â a desired height in pixels when saving as an image. By default, the layout height is used

  * **scale** (_None_) â a scale factor to apply to the layout dimensions. By default, this is 1.0

  * ****kwargs** â keyword arguments for `plotly:plotly.graph_objects.Figure.to_image()` or `plotly:plotly.graph_objects.Figure.write_html()`




select_ids(_ids_ , _view =None_)#
    

Selects the points with the given IDs in this plot.

Parameters:
    

  * **ids** â a list of IDs, or None to reset the plot to its default state

  * **view** (_None_) â the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") corresponding to the given IDs, if available




property selected_ids#
    

A list of IDs of the currently selected points.

An empty list means all points are deselected, and None means default state (nothing selected or unselected).

If the plot is not connected, returns None.

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

property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

class fiftyone.core.plots.plotly.InteractiveScatter(_figure_ , _** kwargs_)#
    

Bases: `PlotlyInteractivePlot`

Wrapper class that turns a Plotly figure containing one or more scatter-type traces into an [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot").

This wrapper responds to selection and deselection events (if available) triggered on the figureâs traces via Plotlyâs lasso and box selector tools.

Traces whose `customdata` attribute contain lists/arrays are assumed to contain the IDs of the points in the trace. Traces with no `customdata` are allowed, but will not have any selection events.

Parameters:
    

  * **figure** â a [`plotly.graph_objects.Figure`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure "\(in \)")

  * ****kwargs** â keyword arguments for the [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") constructor




**Attributes:**

`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
---|---  
`init_view` | A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.  
`is_connected` | Whether this plot is currently connected.  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`selected_ids` | A list of IDs of the currently selected points.  
`selection_mode` | The current selection mode of the plot.  
  
**Methods:**

`connect`() | Connects this plot, if necessary.  
---|---  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`recommend_link_type`([label_field,Â samples]) | Recommends a link type for the given info.  
`register_disconnect_callback`(callback) | Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.  
`register_selection_callback`(callback) | Registers a selection callback for this plot.  
`register_sync_callback`(callback) | Registers a callback that can sync this plot with a `SessionPlot` connected to it.  
`reset`() | Resets the plot to its default state.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
`select_ids`(ids[,Â view]) | Selects the points with the given IDs in this plot.  
`show`(**kwargs) | Shows the plot.  
`update_layout`(**kwargs) | Updates the layout of the plot.  
  
property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

connect()#
    

Connects this plot, if necessary.

disconnect()#
    

Disconnects the plot, if necessary.

freeze()#
    

Freezes the plot, replacing it with a static image.

The plot will also be disconnected.

Only applicable in notebook contexts.

property init_view#
    

A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.

This view will also be shown when the plot is in its default state (no selection).

property is_connected#
    

Whether this plot is currently connected.

property is_disconnected#
    

Whether this plot is currently disconnected.

property is_frozen#
    

Whether this plot is currently frozen.

property link_type#
    

The link type between this plot and a connected session.

static recommend_link_type(_label_field =None_, _samples =None_)#
    

Recommends a link type for the given info.

Parameters:
    

  * **label_field** (_None_) â the label field, if any

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection"), if known



Returns:
    

a `(link_type, label_fields, selection_mode, init_fcn)` tuple

register_disconnect_callback(_callback_)#
    

Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.

The typical use case for this function is to serve as the callback for a `disconnect` button on the plot.

Parameters:
    

**callback** â a function with no arguments

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

reset()#
    

Resets the plot to its default state.

save(_path_ , _width =None_, _height =None_, _scale =None_, _** kwargs_)#
    

Saves the plot as an image or HTML.

Parameters:
    

  * **path** â the path to write the image or HTML

  * **width** (_None_) â a desired width in pixels when saving as an image. By default, the layout width is used

  * **height** (_None_) â a desired height in pixels when saving as an image. By default, the layout height is used

  * **scale** (_None_) â a scale factor to apply to the layout dimensions. By default, this is 1.0

  * ****kwargs** â keyword arguments for `plotly:plotly.graph_objects.Figure.to_image()` or `plotly:plotly.graph_objects.Figure.write_html()`




select_ids(_ids_ , _view =None_)#
    

Selects the points with the given IDs in this plot.

Parameters:
    

  * **ids** â a list of IDs, or None to reset the plot to its default state

  * **view** (_None_) â the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") corresponding to the given IDs, if available




property selected_ids#
    

A list of IDs of the currently selected points.

An empty list means all points are deselected, and None means default state (nothing selected or unselected).

If the plot is not connected, returns None.

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

show(_** kwargs_)#
    

Shows the plot.

Parameters:
    

****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

update_layout(_** kwargs_)#
    

Updates the layout of the plot.

Parameters:
    

****kwargs** â valid arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

class fiftyone.core.plots.plotly.InteractiveHeatmap(_Z_ , _ids_ , _xlabels =None_, _ylabels =None_, _zlim =None_, _values_title ='count'_, _gt_field =None_, _pred_field =None_, _colorscale =None_, _grid_opacity =0.1_, _bg_opacity =0.25_, _** kwargs_)#
    

Bases: `PlotlyInteractivePlot`

An interactive Plotly heatmap.

Unfortunately, the Plotly team has not gotten around to adding native selection utilities to plot types such as heatmaps: [plotly/plotly.js#170](https://github.com/plotly/plotly.js/issues/170).

In lieu of this feature, we provide a homebrewed heatmap that supports two types of interactivity:

  * Individual cells can be selected by clicking on them

  * Groups of cells can be lasso- or box-selected by including their cell centers in a selection




The following events will cause the selection to be cleared:

  * Clicking any cell, if there are currently multiple cells selected

  * Clicking the selected cell, if there is only one cell selected




When heatmap contents are selected via `InteractiveHeatmap.select_ids()`, the heatmap is updated to reflect the proportions of each cell included in the selection.

Parameters:
    

  * **Z** â a `num_cols x num_rows` array-like of heatmap values

  * **ids** â an array-like of same shape as `Z` whose elements contain lists of IDs for the heatmap cells

  * **xlabels** (_None_) â a `num_rows` array of x labels

  * **ylabels** (_None_) â a `num_cols` array of y labels

  * **zlim** (_None_) â a `[zmin, zmax]` limit to use for the colorbar

  * **values_title** (_"count"_) â the semantic meaning of the heatmap values. Used for tooltips

  * **gt_field** (_None_) â the name of the ground truth field, if known. Used for tooltips

  * **pred_field** (_None_) â the name of the predictions field, if known. Used for tooltips

  * **colorscale** (_None_) â a plotly colorscale to use

  * **grid_opacity** (_0.1_) â an opacity value for the grid points

  * **bg_opacity** (_0.25_) â an opacity value for background (unselected) cells

  * ****kwargs** â keyword arguments for the [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") constructor




**Attributes:**

`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
---|---  
`init_view` | A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.  
`is_connected` | Whether this plot is currently connected.  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`selected_ids` | A list of IDs of the currently selected points.  
`selection_mode` | The current selection mode of the plot.  
  
**Methods:**

`connect`() | Connects this plot, if necessary.  
---|---  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`recommend_link_type`([label_field,Â samples]) | Recommends a link type for the given info.  
`register_disconnect_callback`(callback) | Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.  
`register_selection_callback`(callback) | Registers a selection callback for this plot.  
`register_sync_callback`(callback) | Registers a callback that can sync this plot with a `SessionPlot` connected to it.  
`reset`() | Resets the plot to its default state.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
`select_ids`(ids[,Â view]) | Selects the points with the given IDs in this plot.  
`show`(**kwargs) | Shows the plot.  
`update_layout`(**kwargs) | Updates the layout of the plot.  
  
property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

property init_view#
    

A [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") defining the initial view from which to derive selection views when points are selected in the plot.

This view will also be shown when the plot is in its default state (no selection).

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

static recommend_link_type(_label_field =None_, _samples =None_)#
    

Recommends a link type for the given info.

Parameters:
    

  * **label_field** (_None_) â the label field, if any

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection"), if known



Returns:
    

a `(link_type, label_fields, selection_mode, init_fcn)` tuple

register_disconnect_callback(_callback_)#
    

Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.

The typical use case for this function is to serve as the callback for a `disconnect` button on the plot.

Parameters:
    

**callback** â a function with no arguments

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

reset()#
    

Resets the plot to its default state.

save(_path_ , _width =None_, _height =None_, _scale =None_, _** kwargs_)#
    

Saves the plot as an image or HTML.

Parameters:
    

  * **path** â the path to write the image or HTML

  * **width** (_None_) â a desired width in pixels when saving as an image. By default, the layout width is used

  * **height** (_None_) â a desired height in pixels when saving as an image. By default, the layout height is used

  * **scale** (_None_) â a scale factor to apply to the layout dimensions. By default, this is 1.0

  * ****kwargs** â keyword arguments for `plotly:plotly.graph_objects.Figure.to_image()` or `plotly:plotly.graph_objects.Figure.write_html()`




select_ids(_ids_ , _view =None_)#
    

Selects the points with the given IDs in this plot.

Parameters:
    

  * **ids** â a list of IDs, or None to reset the plot to its default state

  * **view** (_None_) â the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") corresponding to the given IDs, if available




property selected_ids#
    

A list of IDs of the currently selected points.

An empty list means all points are deselected, and None means default state (nothing selected or unselected).

If the plot is not connected, returns None.

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

show(_** kwargs_)#
    

Shows the plot.

Parameters:
    

****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

update_layout(_** kwargs_)#
    

Updates the layout of the plot.

Parameters:
    

****kwargs** â valid arguments for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
