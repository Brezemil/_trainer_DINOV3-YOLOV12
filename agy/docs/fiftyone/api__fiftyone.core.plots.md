---
source_url: https://docs.voxel51.com/api/fiftyone.core.plots.html
---

# fiftyone.core.plots#

  * [fiftyone.core.plots.base](api__fiftyone.core.plots.base.md)
    * [`plot_confusion_matrix()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.plot_confusion_matrix)
    * [`plot_regressions()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.plot_regressions)
    * [`plot_pr_curve()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.plot_pr_curve)
    * [`plot_pr_curves()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.plot_pr_curves)
    * [`plot_roc_curve()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.plot_roc_curve)
    * [`lines()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.lines)
    * [`scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.scatterplot)
    * [`location_scatterplot()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.location_scatterplot)
    * [`Plot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot)
      * [`Plot.is_frozen`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.is_frozen)
      * [`Plot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.show)
      * [`Plot.save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.save)
      * [`Plot.freeze()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot.freeze)
    * [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot)
      * [`ResponsivePlot.link_type`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.link_type)
      * [`ResponsivePlot.supports_session_updates`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.supports_session_updates)
      * [`ResponsivePlot.is_connected`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.is_connected)
      * [`ResponsivePlot.is_disconnected`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.is_disconnected)
      * [`ResponsivePlot.is_frozen`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.is_frozen)
      * [`ResponsivePlot.connect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.connect)
      * [`ResponsivePlot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.show)
      * [`ResponsivePlot.reset()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.reset)
      * [`ResponsivePlot.freeze()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.freeze)
      * [`ResponsivePlot.disconnect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.disconnect)
      * [`ResponsivePlot.save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot.save)
    * [`ViewPlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot)
      * [`ViewPlot.supports_session_updates`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.supports_session_updates)
      * [`ViewPlot.update_view()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.update_view)
      * [`ViewPlot.reset()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.reset)
      * [`ViewPlot.connect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.connect)
      * [`ViewPlot.disconnect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.disconnect)
      * [`ViewPlot.freeze()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.freeze)
      * [`ViewPlot.is_connected`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.is_connected)
      * [`ViewPlot.is_disconnected`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.is_disconnected)
      * [`ViewPlot.is_frozen`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.is_frozen)
      * [`ViewPlot.link_type`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.link_type)
      * [`ViewPlot.save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.save)
      * [`ViewPlot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ViewPlot.show)
    * [`InteractivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot)
      * [`InteractivePlot.selection_mode`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selection_mode)
      * [`InteractivePlot.init_view`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.init_view)
      * [`InteractivePlot.selected_ids`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.selected_ids)
      * [`InteractivePlot.recommend_link_type()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.recommend_link_type)
      * [`InteractivePlot.register_selection_callback()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.register_selection_callback)
      * [`InteractivePlot.register_sync_callback()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.register_sync_callback)
      * [`InteractivePlot.register_disconnect_callback()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.register_disconnect_callback)
      * [`InteractivePlot.select_ids()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.select_ids)
      * [`InteractivePlot.connect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.connect)
      * [`InteractivePlot.disconnect()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.disconnect)
      * [`InteractivePlot.freeze()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.freeze)
      * [`InteractivePlot.is_connected`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.is_connected)
      * [`InteractivePlot.is_disconnected`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.is_disconnected)
      * [`InteractivePlot.is_frozen`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.is_frozen)
      * [`InteractivePlot.link_type`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.link_type)
      * [`InteractivePlot.save()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.save)
      * [`InteractivePlot.show()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.show)
      * [`InteractivePlot.supports_session_updates`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.supports_session_updates)
      * [`InteractivePlot.reset()`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.InteractivePlot.reset)
  * [fiftyone.core.plots.manager](api__fiftyone.core.plots.manager.md)
    * [`PlotManager`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager)
      * [`PlotManager.summary()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.summary)
      * [`PlotManager.keys()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.keys)
      * [`PlotManager.items()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.items)
      * [`PlotManager.values()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.values)
      * [`PlotManager.is_connected`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.is_connected)
      * [`PlotManager.is_disconnected`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.is_disconnected)
      * [`PlotManager.has_view_links`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.has_view_links)
      * [`PlotManager.has_sample_links`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.has_sample_links)
      * [`PlotManager.has_frame_links`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.has_frame_links)
      * [`PlotManager.has_label_links`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.has_label_links)
      * [`PlotManager.attach()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.attach)
      * [`PlotManager.remove()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.remove)
      * [`PlotManager.clear()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.clear)
      * [`PlotManager.pop()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.pop)
      * [`PlotManager.connect()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.connect)
      * [`PlotManager.disconnect()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.disconnect)
      * [`PlotManager.sync()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.sync)
      * [`PlotManager.freeze()`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager.freeze)
  * [fiftyone.core.plots.matplotlib](api__fiftyone.core.plots.matplotlib.md)
    * [`plot_confusion_matrix()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_confusion_matrix)
    * [`plot_regressions()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_regressions)
    * [`plot_pr_curve()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_pr_curve)
    * [`plot_pr_curves()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_pr_curves)
    * [`plot_roc_curve()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.plot_roc_curve)
    * [`lines()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.lines)
    * [`scatterplot()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.scatterplot)
    * [`location_scatterplot()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.location_scatterplot)
    * [`InteractiveMatplotlibPlot`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot)
      * [`InteractiveMatplotlibPlot.supports_session_updates`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.supports_session_updates)
      * [`InteractiveMatplotlibPlot.show()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.show)
      * [`InteractiveMatplotlibPlot.save()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.save)
      * [`InteractiveMatplotlibPlot.connect()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.connect)
      * [`InteractiveMatplotlibPlot.disconnect()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.disconnect)
      * [`InteractiveMatplotlibPlot.freeze()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.freeze)
      * [`InteractiveMatplotlibPlot.init_view`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.init_view)
      * [`InteractiveMatplotlibPlot.is_connected`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.is_connected)
      * [`InteractiveMatplotlibPlot.is_disconnected`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.is_disconnected)
      * [`InteractiveMatplotlibPlot.is_frozen`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.is_frozen)
      * [`InteractiveMatplotlibPlot.link_type`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.link_type)
      * [`InteractiveMatplotlibPlot.recommend_link_type()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.recommend_link_type)
      * [`InteractiveMatplotlibPlot.register_disconnect_callback()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.register_disconnect_callback)
      * [`InteractiveMatplotlibPlot.register_selection_callback()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.register_selection_callback)
      * [`InteractiveMatplotlibPlot.register_sync_callback()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.register_sync_callback)
      * [`InteractiveMatplotlibPlot.reset()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.reset)
      * [`InteractiveMatplotlibPlot.select_ids()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.select_ids)
      * [`InteractiveMatplotlibPlot.selected_ids`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.selected_ids)
      * [`InteractiveMatplotlibPlot.selection_mode`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveMatplotlibPlot.selection_mode)
    * [`InteractiveCollection`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection)
      * [`InteractiveCollection.connect()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.connect)
      * [`InteractiveCollection.disconnect()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.disconnect)
      * [`InteractiveCollection.freeze()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.freeze)
      * [`InteractiveCollection.init_view`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.init_view)
      * [`InteractiveCollection.is_connected`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.is_connected)
      * [`InteractiveCollection.is_disconnected`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.is_disconnected)
      * [`InteractiveCollection.is_frozen`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.is_frozen)
      * [`InteractiveCollection.link_type`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.link_type)
      * [`InteractiveCollection.recommend_link_type()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.recommend_link_type)
      * [`InteractiveCollection.register_disconnect_callback()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.register_disconnect_callback)
      * [`InteractiveCollection.register_selection_callback()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.register_selection_callback)
      * [`InteractiveCollection.register_sync_callback()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.register_sync_callback)
      * [`InteractiveCollection.reset()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.reset)
      * [`InteractiveCollection.save()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.save)
      * [`InteractiveCollection.select_ids()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.select_ids)
      * [`InteractiveCollection.selected_ids`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.selected_ids)
      * [`InteractiveCollection.selection_mode`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.selection_mode)
      * [`InteractiveCollection.show()`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.show)
      * [`InteractiveCollection.supports_session_updates`](api__fiftyone.core.plots.matplotlib.md#fiftyone.core.plots.matplotlib.InteractiveCollection.supports_session_updates)
  * [fiftyone.core.plots.plotly](api__fiftyone.core.plots.plotly.md)
    * [`plot_confusion_matrix()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_confusion_matrix)
    * [`plot_regressions()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_regressions)
    * [`plot_pr_curve()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_pr_curve)
    * [`plot_pr_curves()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_pr_curves)
    * [`plot_roc_curve()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.plot_roc_curve)
    * [`lines()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.lines)
    * [`scatterplot()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.scatterplot)
    * [`location_scatterplot()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.location_scatterplot)
    * [`get_colormap()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.get_colormap)
    * [`PlotlyWidgetMixin`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyWidgetMixin)
      * [`PlotlyWidgetMixin.save()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyWidgetMixin.save)
    * [`PlotlyNotebookPlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot)
      * [`PlotlyNotebookPlot.is_frozen`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot.is_frozen)
      * [`PlotlyNotebookPlot.update_layout()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot.update_layout)
      * [`PlotlyNotebookPlot.show()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot.show)
      * [`PlotlyNotebookPlot.freeze()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot.freeze)
      * [`PlotlyNotebookPlot.save()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyNotebookPlot.save)
    * [`PlotlyInteractivePlot`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot)
      * [`PlotlyInteractivePlot.update_layout()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.update_layout)
      * [`PlotlyInteractivePlot.show()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.show)
      * [`PlotlyInteractivePlot.connect()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.connect)
      * [`PlotlyInteractivePlot.disconnect()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.disconnect)
      * [`PlotlyInteractivePlot.freeze()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.freeze)
      * [`PlotlyInteractivePlot.init_view`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.init_view)
      * [`PlotlyInteractivePlot.is_connected`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.is_connected)
      * [`PlotlyInteractivePlot.is_disconnected`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.is_disconnected)
      * [`PlotlyInteractivePlot.is_frozen`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.is_frozen)
      * [`PlotlyInteractivePlot.link_type`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.link_type)
      * [`PlotlyInteractivePlot.recommend_link_type()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.recommend_link_type)
      * [`PlotlyInteractivePlot.register_disconnect_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.register_disconnect_callback)
      * [`PlotlyInteractivePlot.register_selection_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.register_selection_callback)
      * [`PlotlyInteractivePlot.register_sync_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.register_sync_callback)
      * [`PlotlyInteractivePlot.reset()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.reset)
      * [`PlotlyInteractivePlot.save()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.save)
      * [`PlotlyInteractivePlot.select_ids()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.select_ids)
      * [`PlotlyInteractivePlot.selected_ids`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.selected_ids)
      * [`PlotlyInteractivePlot.selection_mode`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.selection_mode)
      * [`PlotlyInteractivePlot.supports_session_updates`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.PlotlyInteractivePlot.supports_session_updates)
    * [`InteractiveScatter`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter)
      * [`InteractiveScatter.supports_session_updates`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.supports_session_updates)
      * [`InteractiveScatter.connect()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.connect)
      * [`InteractiveScatter.disconnect()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.disconnect)
      * [`InteractiveScatter.freeze()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.freeze)
      * [`InteractiveScatter.init_view`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.init_view)
      * [`InteractiveScatter.is_connected`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.is_connected)
      * [`InteractiveScatter.is_disconnected`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.is_disconnected)
      * [`InteractiveScatter.is_frozen`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.is_frozen)
      * [`InteractiveScatter.link_type`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.link_type)
      * [`InteractiveScatter.recommend_link_type()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.recommend_link_type)
      * [`InteractiveScatter.register_disconnect_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.register_disconnect_callback)
      * [`InteractiveScatter.register_selection_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.register_selection_callback)
      * [`InteractiveScatter.register_sync_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.register_sync_callback)
      * [`InteractiveScatter.reset()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.reset)
      * [`InteractiveScatter.save()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.save)
      * [`InteractiveScatter.select_ids()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.select_ids)
      * [`InteractiveScatter.selected_ids`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.selected_ids)
      * [`InteractiveScatter.selection_mode`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.selection_mode)
      * [`InteractiveScatter.show()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.show)
      * [`InteractiveScatter.update_layout()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveScatter.update_layout)
    * [`InteractiveHeatmap`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap)
      * [`InteractiveHeatmap.supports_session_updates`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.supports_session_updates)
      * [`InteractiveHeatmap.init_view`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.init_view)
      * [`InteractiveHeatmap.connect()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.connect)
      * [`InteractiveHeatmap.disconnect()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.disconnect)
      * [`InteractiveHeatmap.freeze()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.freeze)
      * [`InteractiveHeatmap.is_connected`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.is_connected)
      * [`InteractiveHeatmap.is_disconnected`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.is_disconnected)
      * [`InteractiveHeatmap.is_frozen`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.is_frozen)
      * [`InteractiveHeatmap.link_type`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.link_type)
      * [`InteractiveHeatmap.recommend_link_type()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.recommend_link_type)
      * [`InteractiveHeatmap.register_disconnect_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.register_disconnect_callback)
      * [`InteractiveHeatmap.register_selection_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.register_selection_callback)
      * [`InteractiveHeatmap.register_sync_callback()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.register_sync_callback)
      * [`InteractiveHeatmap.reset()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.reset)
      * [`InteractiveHeatmap.save()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.save)
      * [`InteractiveHeatmap.select_ids()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.select_ids)
      * [`InteractiveHeatmap.selected_ids`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.selected_ids)
      * [`InteractiveHeatmap.selection_mode`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.selection_mode)
      * [`InteractiveHeatmap.show()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.show)
      * [`InteractiveHeatmap.update_layout()`](api__fiftyone.core.plots.plotly.md#fiftyone.core.plots.plotly.InteractiveHeatmap.update_layout)
  * [fiftyone.core.plots.utils](api__fiftyone.core.plots.utils.md)
    * [`parse_scatter_inputs()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.parse_scatter_inputs)
    * [`parse_locations()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.parse_locations)
    * [`parse_lines_inputs()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.parse_lines_inputs)
    * [`best_fit_line()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.best_fit_line)
    * [`load_button_icon()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.load_button_icon)
    * [`load_icon()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.load_icon)
    * [`serialize_icon()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.serialize_icon)
    * [`pad_icon()`](api__fiftyone.core.plots.utils.md#fiftyone.core.plots.utils.pad_icon)
  * [fiftyone.core.plots.views](api__fiftyone.core.plots.views.md)
    * [`PlotlyViewPlot`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot)
      * [`PlotlyViewPlot.show()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.show)
      * [`PlotlyViewPlot.connect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.connect)
      * [`PlotlyViewPlot.disconnect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.disconnect)
      * [`PlotlyViewPlot.freeze()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.freeze)
      * [`PlotlyViewPlot.is_connected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.is_connected)
      * [`PlotlyViewPlot.is_disconnected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.is_disconnected)
      * [`PlotlyViewPlot.is_frozen`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.is_frozen)
      * [`PlotlyViewPlot.link_type`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.link_type)
      * [`PlotlyViewPlot.reset()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.reset)
      * [`PlotlyViewPlot.save()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.save)
      * [`PlotlyViewPlot.supports_session_updates`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.supports_session_updates)
      * [`PlotlyViewPlot.update_view()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot.update_view)
    * [`ViewGrid`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid)
      * [`ViewGrid.connect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.connect)
      * [`ViewGrid.disconnect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.disconnect)
      * [`ViewGrid.freeze()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.freeze)
      * [`ViewGrid.is_connected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.is_connected)
      * [`ViewGrid.is_disconnected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.is_disconnected)
      * [`ViewGrid.is_frozen`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.is_frozen)
      * [`ViewGrid.link_type`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.link_type)
      * [`ViewGrid.reset()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.reset)
      * [`ViewGrid.save()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.save)
      * [`ViewGrid.show()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.show)
      * [`ViewGrid.supports_session_updates`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.supports_session_updates)
      * [`ViewGrid.update_view()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.ViewGrid.update_view)
    * [`CategoricalHistogram`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram)
      * [`CategoricalHistogram.connect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.connect)
      * [`CategoricalHistogram.disconnect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.disconnect)
      * [`CategoricalHistogram.freeze()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.freeze)
      * [`CategoricalHistogram.is_connected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.is_connected)
      * [`CategoricalHistogram.is_disconnected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.is_disconnected)
      * [`CategoricalHistogram.is_frozen`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.is_frozen)
      * [`CategoricalHistogram.link_type`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.link_type)
      * [`CategoricalHistogram.reset()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.reset)
      * [`CategoricalHistogram.save()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.save)
      * [`CategoricalHistogram.show()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.show)
      * [`CategoricalHistogram.supports_session_updates`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.supports_session_updates)
      * [`CategoricalHistogram.update_view()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.CategoricalHistogram.update_view)
    * [`NumericalHistogram`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram)
      * [`NumericalHistogram.connect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.connect)
      * [`NumericalHistogram.disconnect()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.disconnect)
      * [`NumericalHistogram.freeze()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.freeze)
      * [`NumericalHistogram.is_connected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.is_connected)
      * [`NumericalHistogram.is_disconnected`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.is_disconnected)
      * [`NumericalHistogram.is_frozen`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.is_frozen)
      * [`NumericalHistogram.link_type`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.link_type)
      * [`NumericalHistogram.reset()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.reset)
      * [`NumericalHistogram.save()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.save)
      * [`NumericalHistogram.show()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.show)
      * [`NumericalHistogram.supports_session_updates`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.supports_session_updates)
      * [`NumericalHistogram.update_view()`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.NumericalHistogram.update_view)



## Module contents#

Plotting framework.

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
`InteractivePlot`([link_type,Â init_view,Â ...]) | Base class for plots that support selection of their points.  
`ViewPlot`([init_view]) | Base class for plots that can be automatically populated given a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instance.  
`PlotManager`(session) | Class that manages communication between a [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") and one or more [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances.  
`ViewGrid`(plots[,Â shape,Â hgap,Â vgap,Â init_view]) | A grid of `PlotlyViewPlot` instances.  
`CategoricalHistogram`(field_or_expr[,Â expr,Â ...]) | A histogram of a categorial field.  
`NumericalHistogram`(field_or_expr[,Â expr,Â ...]) | A histogram of a numerical field.  
  
fiftyone.core.plots.plot_confusion_matrix(_confusion_matrix_ , _labels_ , _ids =None_, _samples =None_, _eval_key =None_, _gt_field =None_, _pred_field =None_, _backend ='plotly'_, _** kwargs_)#
    

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




fiftyone.core.plots.plot_regressions(_ytrue_ , _ypred_ , _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _classes =None_, _gt_field =None_, _pred_field =None_, _backend ='plotly'_, _** kwargs_)#
    

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




fiftyone.core.plots.plot_pr_curve(_precision_ , _recall_ , _thresholds =None_, _label =None_, _backend ='plotly'_, _** kwargs_)#
    

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




fiftyone.core.plots.plot_pr_curves(_precisions_ , _recall_ , _classes_ , _thresholds =None_, _backend ='plotly'_, _** kwargs_)#
    

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




fiftyone.core.plots.plot_roc_curve(_fpr_ , _tpr_ , _thresholds =None_, _roc_auc =None_, _backend ='plotly'_, _** kwargs_)#
    

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




fiftyone.core.plots.lines(_x =None_, _y =None_, _samples =None_, _ids =None_, _link_field =None_, _sizes =None_, _backend ='plotly'_, _** kwargs_)#
    

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




fiftyone.core.plots.scatterplot(_points_ , _samples =None_, _ids =None_, _link_field =None_, _labels =None_, _sizes =None_, _classes =None_, _backend ='plotly'_, _** kwargs_)#
    

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




fiftyone.core.plots.location_scatterplot(_locations =None_, _samples =None_, _ids =None_, _labels =None_, _sizes =None_, _classes =None_, _backend ='plotly'_, _** kwargs_)#
    

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




class fiftyone.core.plots.Plot#
    

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

class fiftyone.core.plots.ResponsivePlot(_link_type_)#
    

Bases: [`Plot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.Plot "fiftyone.core.plots.base.Plot")

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




class fiftyone.core.plots.InteractivePlot(_link_type ='samples'_, _init_view =None_, _label_fields =None_, _selection_mode =None_, _init_fcn =None_)#
    

Bases: [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot")

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

class fiftyone.core.plots.ViewPlot(_init_view =None_)#
    

Bases: [`ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot")

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

class fiftyone.core.plots.PlotManager(_session_)#
    

Bases: `object`

Class that manages communication between a [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session") and one or more [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances.

Each plot can be linked to either the view, samples, frames, or labels of a session:

  * **View links:** When a plot has `link_type == "view"`, then, when the sessionâs view changes, the plot is updated based on the content of the view

  * **Sample links:** When points are selected in a plot with `link_type == "samples"`, a view containing the corresponding samples is loaded in the App. Conversely, when the sessionâs view changes, the corresponding points are selected in the plot

  * **Frame links:** When points are selected in a plot with `link_type == "frames"`, a view containing the corresponding frames is loaded in the App. Conversely, when the sessionâs view changes, the corresponding points are selected in the plot

  * **Label links:** When points are selected in a plot with `link_type == "labels"`, a view containing the corresponding labels is loaded in the App. Conversely, when the sessionâs view changes, the points in the plot corresponding to all labels in the view are selected in the plot




Parameters:
    

**session** â a [`fiftyone.core.session.Session`](api__fiftyone.core.session.md#fiftyone.core.session.Session "fiftyone.core.session.Session")

**Methods:**

`summary`() | Returns a string summary of this manager.  
---|---  
`keys`() | Returns an iterator over the names of plots in this manager.  
`items`() | Returns an iterator over the `(name, plot)` pairs in this manager.  
`values`() | Returns an iterator over the plots in this manager.  
`attach`(plot[,Â name,Â connect,Â overwrite]) | Attaches a plot to this manager.  
`remove`(name) | Removes the plot from this manager.  
`clear`() | Removes all plots from this manager.  
`pop`(name) | Removes the plot from this manager and returns it.  
`connect`() | Connects this manager to its session and all plots.  
`disconnect`() | Disconnects this manager from its session and all plots.  
`sync`() | Syncs all connected plots with the session's current view.  
`freeze`() | Freezes all connected plots, replacing them with static images.  
  
**Attributes:**

`is_connected` | Whether this manager is currently connected to its plots.  
---|---  
`is_disconnected` | Whether this manager is currently disconnected from its plots.  
`has_view_links` | Whether this manager has plots linked to views.  
`has_sample_links` | Whether this manager has plots linked to samples.  
`has_frame_links` | Whether this manager has plots linked to frames.  
`has_label_links` | Whether this manager has plots linked to labels.  
  
summary()#
    

Returns a string summary of this manager.

Returns:
    

a string summary

keys()#
    

Returns an iterator over the names of plots in this manager.

Returns:
    

an iterator over plot names

items()#
    

Returns an iterator over the `(name, plot)` pairs in this manager.

Returns:
    

an iterator that emits `(name, ResponsivePlot)` tuples

values()#
    

Returns an iterator over the plots in this manager.

Returns:
    

an iterator that emits [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot") instances

property is_connected#
    

Whether this manager is currently connected to its plots.

property is_disconnected#
    

Whether this manager is currently disconnected from its plots.

property has_view_links#
    

Whether this manager has plots linked to views.

property has_sample_links#
    

Whether this manager has plots linked to samples.

property has_frame_links#
    

Whether this manager has plots linked to frames.

property has_label_links#
    

Whether this manager has plots linked to labels.

attach(_plot_ , _name =None_, _connect =True_, _overwrite =True_)#
    

Attaches a plot to this manager.

Parameters:
    

  * **plot** â a [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot")

  * **name** (_None_) â an optional name for the plot

  * **connect** (_True_) â whether to immediately connect the plot

  * **overwrite** (_True_) â whether to overwrite an existing plot of the same name




remove(_name_)#
    

Removes the plot from this manager.

Parameters:
    

**name** â the name of a plot

clear()#
    

Removes all plots from this manager.

pop(_name_)#
    

Removes the plot from this manager and returns it.

Parameters:
    

**name** â the name of a plot

Returns:
    

the [`fiftyone.core.plots.base.ResponsivePlot`](api__fiftyone.core.plots.base.md#fiftyone.core.plots.base.ResponsivePlot "fiftyone.core.plots.base.ResponsivePlot")

connect()#
    

Connects this manager to its session and all plots.

disconnect()#
    

Disconnects this manager from its session and all plots.

sync()#
    

Syncs all connected plots with the sessionâs current view.

freeze()#
    

Freezes all connected plots, replacing them with static images.

Only applicable in notebook contexts.

class fiftyone.core.plots.ViewGrid(_plots_ , _shape =None_, _hgap =None_, _vgap =None_, _init_view =None_, _** kwargs_)#
    

Bases: [`PlotlyViewPlot`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot "fiftyone.core.plots.views.PlotlyViewPlot")

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




class fiftyone.core.plots.CategoricalHistogram(_field_or_expr_ , _expr =None_, _order ='alphabetical'_, _xlabel =None_, _log =None_, _bargap =None_, _color =None_, _opacity =None_, _init_view =None_, _** kwargs_)#
    

Bases: [`PlotlyViewPlot`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot "fiftyone.core.plots.views.PlotlyViewPlot")

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




class fiftyone.core.plots.NumericalHistogram(_field_or_expr_ , _expr =None_, _bins =None_, _range =None_, _xlabel =None_, _log =None_, _color =None_, _opacity =None_, _init_view =None_, _** kwargs_)#
    

Bases: [`PlotlyViewPlot`](api__fiftyone.core.plots.views.md#fiftyone.core.plots.views.PlotlyViewPlot "fiftyone.core.plots.views.PlotlyViewPlot")

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
