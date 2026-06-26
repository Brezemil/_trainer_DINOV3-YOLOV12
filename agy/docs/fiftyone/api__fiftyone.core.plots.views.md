---
source_url: https://docs.voxel51.com/api/fiftyone.core.plots.views.html
---

# fiftyone.core.plots.views#

Plotly-powered view plots.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PlotlyViewPlot`(widget[,Â init_view]) | Base class for `ViewPlot` instances with Plotly backends.  
---|---  
`ViewGrid`(plots[,Â shape,Â hgap,Â vgap,Â init_view]) | A grid of `PlotlyViewPlot` instances.  
`CategoricalHistogram`(field_or_expr[,Â expr,Â ...]) | A histogram of a categorial field.  
`NumericalHistogram`(field_or_expr[,Â expr,Â ...]) | A histogram of a numerical field.  
  
class fiftyone.core.plots.views.PlotlyViewPlot(_widget_ , _init_view =None_)#
    

Bases: [`PlotlyWidgetMixin`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyWidgetMixin "fiftyone.core.plots.plotly.PlotlyWidgetMixin"), [`ViewPlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot "fiftyone.core.plots.base.ViewPlot")

Base class for `ViewPlot` instances with Plotly backends.

Parameters:
    

  * **widget** â a [`plotly.graph_objects.FigureWidget`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.FigureWidget "\(in \)")

  * **init_view** (_None_) â an optional initial [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to load




**Methods:**

`show`(**kwargs) | Shows this plot.  
---|---  
`connect`() | Connects this plot, if necessary.  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`reset`() | Resets the plot to its default state.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
`update_view`(view[,Â agg_results]) | Updates the plot based on the provided view.  
  
**Attributes:**

`is_connected` | Whether this plot is currently connected.  
---|---  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
  
show(_** kwargs_)#
    

Shows this plot.

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

property is_connected#
    

Whether this plot is currently connected.

property is_disconnected#
    

Whether this plot is currently disconnected.

property is_frozen#
    

Whether this plot is currently frozen.

property link_type#
    

The link type between this plot and a connected session.

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




property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

update_view(_view_ , _agg_results =None_)#
    

Updates the plot based on the provided view.

Parameters:
    

  * **view** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **agg_results** (_None_) â a list of pre-computed aggregation results




class fiftyone.core.plots.views.ViewGrid(_plots_ , _shape =None_, _hgap =None_, _vgap =None_, _init_view =None_, _** kwargs_)#
    

Bases: `PlotlyViewPlot`

A grid of `PlotlyViewPlot` instances.

Parameters:
    

  * **plots** â a `PlotlyViewPlot` or iterable of `PlotlyViewPlot` instances

  * **shape** (_None_) â the `(rows, cols)` shape to use for the grid

  * **hgap** (_None_) â a horizontal spacing between the subplots, in `[0, 1]`

  * **vgap** (_None_) â a vertical spacing between the subplots, in `[0, 1]`

  * **init_view** (_None_) â an optional initial [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to load

  * ****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")




**Methods:**

`connect`() | Connects this plot, if necessary.  
---|---  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`reset`() | Resets the plot to its default state.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
`show`(**kwargs) | Shows this plot.  
`update_view`(view[,Â agg_results]) | Updates the plot based on the provided view.  
  
**Attributes:**

`is_connected` | Whether this plot is currently connected.  
---|---  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
  
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




show(_** kwargs_)#
    

Shows this plot.

Parameters:
    

****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

update_view(_view_ , _agg_results =None_)#
    

Updates the plot based on the provided view.

Parameters:
    

  * **view** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **agg_results** (_None_) â a list of pre-computed aggregation results




class fiftyone.core.plots.views.CategoricalHistogram(_field_or_expr_ , _expr =None_, _order ='alphabetical'_, _xlabel =None_, _log =None_, _bargap =None_, _color =None_, _opacity =None_, _init_view =None_, _** kwargs_)#
    

Bases: `PlotlyViewPlot`

A histogram of a categorial field.

Parameters:
    

  * **field_or_expr** â a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to plot

  * **expr** (_None_) â 

an optional [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before plotting

  * **order** (_"alphabetical"_) â the x-axis ordering strategy to use. Can be âalphabeticalâ to sort by field value, or âfrequencyâ to sort in descending order of frequency, or a function suitable for `sorted(items, key=order)`, where `items` is a list of `(value, count)` tuples

  * **xlabel** (_None_) â an optional x-label for the plot

  * **log** (_False_) â whether to use a log scale y-axis

  * **bargap** (_None_) â relative spacing between bars in `[0, 1]`

  * **color** (_None_) â a color for the bars. Can be any color supported by `plotly:plotly.graph_objects.bar.Marker.color()`

  * **opacity** (_None_) â an optional opacity for the bars in `[0, 1]`

  * **init_view** (_None_) â an optional initial [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to load

  * ****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")




**Methods:**

`connect`() | Connects this plot, if necessary.  
---|---  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`reset`() | Resets the plot to its default state.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
`show`(**kwargs) | Shows this plot.  
`update_view`(view[,Â agg_results]) | Updates the plot based on the provided view.  
  
**Attributes:**

`is_connected` | Whether this plot is currently connected.  
---|---  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
  
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




show(_** kwargs_)#
    

Shows this plot.

Parameters:
    

****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

update_view(_view_ , _agg_results =None_)#
    

Updates the plot based on the provided view.

Parameters:
    

  * **view** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **agg_results** (_None_) â a list of pre-computed aggregation results




class fiftyone.core.plots.views.NumericalHistogram(_field_or_expr_ , _expr =None_, _bins =None_, _range =None_, _xlabel =None_, _log =None_, _color =None_, _opacity =None_, _init_view =None_, _** kwargs_)#
    

Bases: `PlotlyViewPlot`

A histogram of a numerical field.

Parameters:
    

  * **field_or_expr** â 

a field name, `embedded.field.name`, [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression"), or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) defining the field or expression to plot

  * **expr** (_None_) â 

an optional [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) to apply to `field_or_expr` (which must be a field) before plotting

  * **bins** (_None_) â can be either an integer number of bins to generate or a monotonically increasing sequence specifying the bin edges to use. By default, 10 bins are created. If `bins` is an integer and no `range` is specified, bin edges are automatically computed from the bounds of the field

  * **range** (_None_) â a `(lower, upper)` tuple specifying a range in which to generate equal-width bins. Only applicable when `bins` is an integer or `None`

  * **xlabel** (_None_) â an optional x-label for the plot

  * **log** (_False_) â whether to use a log scale y-axis

  * **color** (_None_) â a color for the bars. Can be any color supported by `plotly:plotly.graph_objects.bar.Marker.color()`

  * **opacity** (_None_) â an optional opacity for the bars in `[0, 1]`

  * **init_view** (_None_) â an optional initial [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to load

  * ****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")




**Methods:**

`connect`() | Connects this plot, if necessary.  
---|---  
`disconnect`() | Disconnects the plot, if necessary.  
`freeze`() | Freezes the plot, replacing it with a static image.  
`reset`() | Resets the plot to its default state.  
`save`(path[,Â width,Â height,Â scale]) | Saves the plot as an image or HTML.  
`show`(**kwargs) | Shows this plot.  
`update_view`(view[,Â agg_results]) | Updates the plot based on the provided view.  
  
**Attributes:**

`is_connected` | Whether this plot is currently connected.  
---|---  
`is_disconnected` | Whether this plot is currently disconnected.  
`is_frozen` | Whether this plot is currently frozen.  
`link_type` | The link type between this plot and a connected session.  
`supports_session_updates` | Whether this plot supports automatic updates in response to session changes.  
  
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




show(_** kwargs_)#
    

Shows this plot.

Parameters:
    

****kwargs** â optional parameters for [`plotly.graph_objects.Figure.update_layout()`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.Figure.update_layout "\(in \)")

property supports_session_updates#
    

Whether this plot supports automatic updates in response to session changes.

update_view(_view_ , _agg_results =None_)#
    

Updates the plot based on the provided view.

Parameters:
    

  * **view** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **agg_results** (_None_) â a list of pre-computed aggregation results




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
