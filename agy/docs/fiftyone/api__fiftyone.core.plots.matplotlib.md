---
source_url: https://docs.voxel51.com/api/fiftyone.core.plots.matplotlib.html
---

# fiftyone.core.plots.matplotlib#

Matplotlib plots.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`plot_confusion_matrix`(confusion_matrix,Â labels) | Plots a confusion matrix.  
---|---  
`plot_regressions`(ytrue,Â ypred[,Â samples,Â ...]) | Plots the given regression results.  
`plot_pr_curve`(precision,Â recall[,Â label,Â ...]) | Plots a precision-recall (PR) curve.  
`plot_pr_curves`(precisions,Â recall,Â classes) | Plots a set of per-class precision-recall (PR) curves.  
`plot_roc_curve`(fpr,Â tpr[,Â roc_auc,Â title,Â ...]) | Plots a receiver operating characteristic (ROC) curve.  
`lines`([x,Â y,Â samples,Â ids,Â link_field,Â ...]) | Plots the given lines(s) data.  
`scatterplot`(points[,Â samples,Â ids,Â ...]) | Generates an interactive scatterplot of the given points.  
`location_scatterplot`([locations,Â samples,Â ...]) | Generates an interactive scatterplot of the given location coordinates with a map rendered in the background of the plot.  
  
**Classes:**

`InteractiveMatplotlibPlot`(figure,Â **kwargs) | Base class for interactive matplotlib plots.  
---|---  
`InteractiveCollection`(collection[,Â ids,Â ...]) | Interactive wrapper for a matplotlib collection.  
  
fiftyone.core.plots.matplotlib.plot_confusion_matrix(_confusion_matrix_ , _labels_ , _show_values =True_, _show_colorbar =True_, _cmap =None_, _title =None_, _xticks_rotation =45.0_, _values_format =None_, _ax =None_, _figsize =None_)#
    

Plots a confusion matrix.

Parameters:
    

  * **confusion_matrix** â a `num_true x num_preds` confusion matrix

  * **labels** â a `max(num_true, num_preds)` array-like of class labels

  * **show_values** (_True_) â whether to show counts in the confusion matrix cells

  * **show_colorbar** (_True_) â whether to show a colorbar

  * **cmap** (_None_) â a colormap recognized by `matplotlib`

  * **title** (_None_) â a title for the plot

  * **xticks_rotation** (_45.0_) â a rotation for the x-tick labels. Can be numeric degrees, âverticalâ, âhorizontalâ, or None

  * **values_format** (_None_) â a format string like `".2g"` or `"d"` to use to format the cell counts

  * **ax** (_None_) â a matplotlib axis to plot in

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches



Returns:
    

a matplotlib figure

fiftyone.core.plots.matplotlib.plot_regressions(_ytrue_ , _ypred_ , _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _classes =None_, _gt_field =None_, _pred_field =None_, _best_fit_label =None_, _marker_size =None_, _cmap =None_, _title =None_, _ax =None_, _figsize =None_, _style =None_, _** kwargs_)#
    

Plots the given regression results.

Parameters:
    

  * **ytrue** â an array-like of ground truth values

  * **ypred** â an array-like of predicted values

  * **samples** (_None_) â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose data is being visualized

  * **ids** (_None_) â an array-like of sample or frame IDs corresponding to the regressions. If not provided but `samples` are provided, the appropriate IDs will be extracted from the samples

  * **labels** (_None_) â 

data to use to color the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric or string values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric or string values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric or string values

    * a list of array-lies of numeric or string values, if `link_field` refers to frames

  * **sizes** (_None_) â 

data to use to scale the sizes of the points. Can be any of the following:

    * the name of a sample field or `embedded.field.name` of `samples` from which to extract numeric values

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") defining numeric values to compute from `samples` via [`fiftyone.core.collections.SampleCollection.values()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.values "fiftyone.core.collections.SampleCollection.values")

    * an array-like of numeric values

    * a list of array-likes of numeric or string values, if `link_field` refers to frames

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings

  * **gt_field** (_None_) â the name of the ground truth field

  * **pred_field** (_None_) â the name of the predictions field

  * **best_fit_label** (_None_) â a custom legend label for the best fit line

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **cmap** (_None_) â a colormap recognized by `matplotlib`

  * **title** (_None_) â a title for the plot

  * **ax** (_None_) â a matplotlib axis to plot in

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches

  * **style** (_None_) â a style to use for the plot

  * ****kwargs** â optional keyword arguments for matplotlibâs `scatter()`



Returns:
    

a matplotlib figure

fiftyone.core.plots.matplotlib.plot_pr_curve(_precision_ , _recall_ , _label =None_, _title =None_, _ax =None_, _figsize =None_, _style =None_, _** kwargs_)#
    

Plots a precision-recall (PR) curve.

Parameters:
    

  * **precision** â an array-like of precision values

  * **recall** â an array-like of recall values

  * **label** (_None_) â a label for the curve

  * **title** (_None_) â a title for the plot

  * **ax** (_None_) â a matplotlib axis to plot in

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches

  * **style** (_None_) â a style to use for the plot

  * ****kwargs** â optional keyword arguments for matplotlibâs `plot()`



Returns:
    

a matplotlib figure

fiftyone.core.plots.matplotlib.plot_pr_curves(_precisions_ , _recall_ , _classes_ , _title =None_, _ax =None_, _figsize =None_, _style =None_, _** kwargs_)#
    

Plots a set of per-class precision-recall (PR) curves.

Parameters:
    

  * **precisions** â a `num_classes x num_recalls` array-like of per-class precision values

  * **recall** â an array-like of recall values

  * **classes** â the list of classes

  * **title** (_None_) â a title for the plot

  * **ax** (_None_) â a matplotlib axis to plot in

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches

  * **style** (_None_) â a style to use for the plot

  * ****kwargs** â optional keyword arguments for matplotlibâs `plot()`



Returns:
    

a matplotlib figure

fiftyone.core.plots.matplotlib.plot_roc_curve(_fpr_ , _tpr_ , _roc_auc =None_, _title =None_, _ax =None_, _figsize =None_, _style =None_, _** kwargs_)#
    

Plots a receiver operating characteristic (ROC) curve.

Parameters:
    

  * **fpr** â an array-like of false positive rates

  * **tpr** â an array-like of true positive rates

  * **roc_auc** (_None_) â the area under the ROC curve

  * **title** (_None_) â a title for the plot

  * **ax** (_None_) â a matplotlib axis to plot in

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches

  * **style** (_None_) â a style to use for the plot

  * ****kwargs** â optional keyword arguments for matplotlibâs `plot()`



Returns:
    

a matplotlib figure

fiftyone.core.plots.matplotlib.lines(_x =None_, _y =None_, _samples =None_, _ids =None_, _link_field =None_, _sizes =None_, _labels =None_, _colors =None_, _marker_size =None_, _title =None_, _xlabel =None_, _ylabel =None_, _ax =None_, _ax_equal =False_, _figsize =None_, _style =None_, _buttons =None_, _** kwargs_)#
    

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

  * **labels** (_None_) â a label or list of labels for the line traces

  * **colors** (_None_) â a list of colors recognized by `matplotlib` to use for the line traces. See <https://matplotlib.org/stable/tutorials/colors/colormaps.html> for more information

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **title** (_None_) â a title for the plot

  * **xlabel** (_None_) â an x-axis label

  * **ylabel** (_None_) â a y-axis label

  * **ax** (_None_) â a matplotlib axis to plot in

  * **ax_equal** (_False_) â whether to set `axis("equal")`

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches

  * **style** (_None_) â a style to use for the plot

  * **buttons** (_None_) â a list of `(label, icon_image, callback)` tuples defining buttons to add to the plot

  * ****kwargs** â optional keyword arguments for matplotlibâs `plot()` and `scatter()`



Returns:
    

one of the following

  * an `InteractiveCollection`, when IDs are available

  * a matplotlib figure, otherwise




fiftyone.core.plots.matplotlib.scatterplot(_points_ , _samples =None_, _ids =None_, _link_field =None_, _labels =None_, _sizes =None_, _classes =None_, _marker_size =None_, _cmap =None_, _title =None_, _ax =None_, _ax_equal =False_, _figsize =None_, _style =None_, _buttons =None_, _** kwargs_)#
    

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

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **cmap** (_None_) â a colormap recognized by `matplotlib`

  * **title** (_None_) â a title for the plot

  * **ax** (_None_) â a matplotlib axis to plot in

  * **ax_equal** (_False_) â whether to set `axis("equal")`

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches

  * **style** (_None_) â a style to use for the plot

  * **buttons** (_None_) â a list of `(label, icon_image, callback)` tuples defining buttons to add to the plot

  * ****kwargs** â optional keyword arguments for matplotlibâs `scatter()`



Returns:
    

one of the following

  * an `InteractiveCollection`, for 2D points and when IDs are available

  * a matplotlib figure, otherwise




fiftyone.core.plots.matplotlib.location_scatterplot(_locations =None_, _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _classes =None_, _map_type ='satellite'_, _show_scale_bar =False_, _api_key =None_, _marker_size =None_, _cmap =None_, _title =None_, _ax =None_, _ax_equal =False_, _figsize =None_, _style =None_, _buttons =None_, _** kwargs_)#
    

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

  * **classes** (_None_) â a list of classes whose points to plot. Only applicable when `labels` contains strings

  * **map_type** (_"satellite"_) â the map type to render. Supported values are `("roadmap", "satellite", "hybrid", "terrain")`

  * **show_scale_bar** (_False_) â whether to render a scale bar on the plot

  * **api_key** (_None_) â a Google Maps API key to use

  * **marker_size** (_None_) â the marker size to use. If `sizes` are provided, this value is used as a reference to scale the sizes of all points

  * **cmap** (_None_) â a colormap recognized by `matplotlib`

  * **title** (_None_) â a title for the plot

  * **ax** (_None_) â a matplotlib axis to plot in

  * **ax_equal** (_False_) â whether to set `axis("equal")`

  * **figsize** (_None_) â a `(width, height)` for the figure, in inches

  * **style** (_None_) â a style to use for the plot

  * **buttons** (_None_) â a list of `(label, icon_image, callback)` tuples defining buttons to add to the plot

  * ****kwargs** â optional keyword arguments for matplotlibâs `scatter()`



Returns:
    

one of the following

  * an `InteractiveCollection`, if IDs are available

  * a matplotlib figure, otherwise




class fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot(_figure_ , _** kwargs_)#
    

Bases: [`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot")

Base class for interactive matplotlib plots.

Parameters:
    

  * **figure** â a `matplotlib.figure.Figure`

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

`show`() | Shows this plot.  
---|---  
`save`(path[,Â dpi]) | Saves the plot as an image.  
`connect`() | Connects this plot, if necessary.  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`recommend_link_type`([label_field,Â samples]) | Recommends a link type for the given info.  
`register_disconnect_callback`(callback) | Registers a callback that can disconnect this plot from a `SessionPlot` connected to it.  
`register_selection_callback`(callback) | Registers a selection callback for this plot.  
`register_sync_callback`(callback) | Registers a callback that can sync this plot with a `SessionPlot` connected to it.  
`reset`() | Resets the plot to its default state.  
`select_ids`(ids[,Â view]) | Selects the points with the given IDs in this plot.  
  
property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

show()#
    

Shows this plot.

save(_path_ , _dpi =None_, _** kwargs_)#
    

Saves the plot as an image.

Parameters:
    

  * **path** â the path to write the image

  * **dpi** (_None_) â a resolution in dots per inch

  * ****kwargs** â keyword arguments for `matplotlib.pyplot.savefig`




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

class fiftyone.core.plots.matplotlib.InteractiveCollection(_collection_ , _ids =None_, _buttons =None_, _alpha_other =0.25_, _expand_selected =3.0_, _click_tolerance =0.02_, _** kwargs_)#
    

Bases: `InteractiveMatplotlibPlot`

Interactive wrapper for a matplotlib collection.

This class enables collection points to be lasso-ed and click selected.

The currently selected points are given a visually distinctive style, and you can modify your selection by either clicking on individual points or drawing a lasso around new points.

When the shift key is pressed, new selections are added to the selected set, or subtracted if the new selection is a subset of the current selection.

Parameters:
    

  * **collection** â a `matplotlib.collections.Collection` to select points from

  * **ids** (_None_) â an array-like of IDs corresponding to the points in `collection`

  * **buttons** (_None_) â a list of `(label, icon_image, callback)` tuples defining buttons to add to the plot

  * **alpha_other** (_0.25_) â a transparency value for unselected points

  * **expand_selected** (_3.0_) â expand the size of selected points by this multiple

  * **click_tolerance** (_0.02_) â a click distance tolerance in `[0, 1]` when clicking individual points

  * ****kwargs** â keyword arguments for the [`fiftyone.core.plots.base.InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot "fiftyone.core.plots.base.InteractivePlot") constructor




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
`save`(path[,Â dpi]) | Saves the plot as an image.  
`select_ids`(ids[,Â view]) | Selects the points with the given IDs in this plot.  
`show`() | Shows this plot.  
  
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

save(_path_ , _dpi =None_, _** kwargs_)#
    

Saves the plot as an image.

Parameters:
    

  * **path** â the path to write the image

  * **dpi** (_None_) â a resolution in dots per inch

  * ****kwargs** â keyword arguments for `matplotlib.pyplot.savefig`




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

show()#
    

Shows this plot.

property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
