---
source_url: https://docs.voxel51.com/api/fiftyone.core.session.session.html
---

# fiftyone.core.session.session#

Session class for interacting with the FiftyOne App.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`launch_app`([dataset,Â view,Â sample_id,Â ...]) | Launches the FiftyOne App.  
---|---  
`close_app`() | Closes the FiftyOne App, if necessary.  
`update_state`([auto_show]) | `Session` method decorator for triggering state update events  
  
**Classes:**

`Session`([dataset,Â view,Â sample_id,Â ...]) | Session that maintains a 1-1 shared state with the FiftyOne App.  
---|---  
  
fiftyone.core.session.session.launch_app(_dataset : [Dataset](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") = None_, _view : [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") = None_, _sample_id : str = None_, _group_id : str = None_, _spaces : [Space](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space") = None_, _color_scheme : [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme") = None_, _plots : [PlotManager](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") = None_, _port : int = None_, _address : str = None_, _remote : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _browser : str = None_, _height : int = None_, _auto : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _config : [AppConfig](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") = None_) → Session#
    

Launches the FiftyOne App.

Note that only one App instance can be opened at a time. If this method is called when another App exists, the existing App will be closed.

Parameters:
    

  * **dataset** (_None_) â an optional [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to load

  * **view** (_None_) â an optional [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to load

  * **sample_id** (_None_) â an optional [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") ID to load in the modal

  * **group_id** (_None_) â an optional [`fiftyone.core.groups.Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") ID to load in the modal

  * **spaces** (_None_) â an optional [`fiftyone.core.odm.workspace.Space`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space") instance defining a space configuration to load

  * **color_scheme** (_None_) â an optional [`fiftyone.core.odm.dataset.ColorScheme`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme") defining a custom color scheme to use

  * **plots** (_None_) â an optional [`fiftyone.core.plots.manager.PlotManager`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") to connect to this session

  * **port** (_None_) â the port number to serve the App. If None, `fiftyone.config.default_app_port` is used

  * **address** (_None_) â the address to serve the App. If None, `fiftyone.config.default_app_address` is used

  * **remote** (_False_) â whether this is a remote session, and opening the App should not be attempted

  * **browser** (_None_) â an optional browser to use to open the App. If None, the default browser will be used. Refer to list of supported browsers at <https://docs.python.org/3/library/webbrowser.html>

  * **height** (_None_) â an optional height, in pixels, at which to render App instances in notebook cells. Only applicable in notebook contexts

  * **auto** (_True_) â whether to automatically show a new App window whenever the state of the session is updated. Only applicable in notebook contexts

  * **config** (_None_) â an optional [`fiftyone.core.config.AppConfig`](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") to control fine-grained default App settings



Returns:
    

a `Session`

fiftyone.core.session.session.close_app() → None#
    

Closes the FiftyOne App, if necessary.

If no App is currently open, this method has no effect.

fiftyone.core.session.session.update_state(_auto_show : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_) → Callable#
    

`Session` method decorator for triggering state update events

Parameters:
    

**auto_show** (_False_) â whether the method should show a new notebook App cell as well, if `auto` is `True`

Returns:
    

the decorated method

class fiftyone.core.session.session.Session(_dataset : [Dataset](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") | [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") = None_, _view : [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") = None_, _sample_id : str = None_, _group_id : str = None_, _spaces : [Space](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space") = None_, _color_scheme : [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme") = None_, _plots : [PlotManager](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") = None_, _port : int = None_, _address : str = None_, _remote : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _browser : str = None_, _height : int = None_, _auto : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _config : [AppConfig](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") = None_, _view_name : str = None_)#
    

Bases: `object`

Session that maintains a 1-1 shared state with the FiftyOne App.

**Basic Usage**

  * Use `launch_app()` to launch the App and retrieve its corresponding `Session` instance.

  * To open a dataset in the App, simply set the `Session.dataset` property of the session to your [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset").

  * To load a specific view into your dataset, simply set the `Session.view` property of the session to your [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView").

  * To load a specific sample in the modal, simply set the `Session.sample_id` property of the session to the ID of the [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample").

  * To load a specific group in the modal, simply set the `Session.group_id` property of the session to the ID of the [`fiftyone.core.groups.Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group").

  * To attach/remove interactive plots, use the methods exposed on the `Session.plots` property of the session.

  * Use `Session.refresh()` to refresh the App if you update a dataset outside of the App

  * Use `Session.selected` to retrieve the IDs of the currently selected samples in the App.

  * Use `Session.selected_labels` to retrieve the IDs of the currently selected labels in the App.

  * In notebook contexts, use `Session.freeze()` to replace the App and any attached plots with static images.

  * Use `Session.close()` and `Session.open()` to temporarily close and reopen the App without creating a new `Session` instance.

  * Use `close_app()` to programmatically close the App and terminate the session.




Parameters:
    

  * **dataset** (_None_) â an optional [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") or [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to load

  * **view** (_None_) â an optional [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to load

  * **sample_id** (_None_) â an optional [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") ID to load in the modal

  * **group_id** (_None_) â an optional [`fiftyone.core.groups.Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") ID to load in the modal

  * **spaces** (_None_) â an optional [`fiftyone.core.odm.workspace.Space`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space") instance defining a space configuration to load

  * **color_scheme** (_None_) â an optional [`fiftyone.core.odm.dataset.ColorScheme`](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme") defining a custom color scheme to use

  * **plots** (_None_) â an optional [`fiftyone.core.plots.manager.PlotManager`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") to connect to this session

  * **port** (_None_) â the port number to serve the App. If None, `fiftyone.config.default_app_port` is used

  * **address** (_None_) â the address to serve the App. If None, `fiftyone.config.default_app_address` is used

  * **remote** (_False_) â whether this is a remote session, and opening the App should not be attempted

  * **browser** (_None_) â an optional browser to use to open the App. If None, the default browser will be used. Refer to list of supported browsers at <https://docs.python.org/3/library/webbrowser.html>

  * **height** (_None_) â an optional height, in pixels, at which to render App instances in notebook cells. Only applicable in notebook contexts

  * **auto** (_True_) â whether to automatically show a new App window whenever the state of the session is updated. Only applicable in notebook contexts

  * **config** (_None_) â an optional [`fiftyone.core.config.AppConfig`](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") to control fine-grained default App settings




**Attributes:**

`auto` | The auto setting for the session.  
---|---  
`server_port` | The server port for the session.  
`server_address` | The server address for the session, or None if not specified.  
`remote` | Whether the session is remote.  
`url` | The URL of the session.  
`config` | The current [`fiftyone.core.config.AppConfig`](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig").  
`group_id` | The current [`fiftyone.core.groups.Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") ID in the modal, if any.  
`sample_id` | The current [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") ID in the modal, if any.  
`spaces` | The layout state for the session.  
`color_scheme` | The color scheme for the session.  
`dataset` | The [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") connected to the session.  
`view` | The [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") connected to the session, or `None` if no view is connected.  
`has_plots` | Whether this session has any attached plots.  
`plots` | The [`fiftyone.core.plots.manager.PlotManager`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") instance that manages plots attached to this session.  
`selected` | A list of IDs of the currently selected samples in the App, if any.  
`selected_samples` | A list of selected sample dicts, each with `id` and `type` (`"default"` or `"alt"`), where type corresponds to a key in `sample_selection_style`.  
`sample_selection_style` | The current sample grid selection style config.  
`label_selection_style` | The current label selection style config.  
`selected_labels` | A list of labels currently selected in the App.  
`selected_view` | A [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the currently selected content in the App.  
  
**Methods:**

`load_workspace`(workspace) | Loads the given saved workspace.  
---|---  
`clear_dataset`() | Clears the current [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") from the session, if any.  
`clear_view`() | Clears the current [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") from the session, if any.  
`refresh`() | Refreshes the current App window.  
`clear_selected`() | Clears the currently selected samples, if any.  
`select_samples`([ids,Â tags]) | Selects the specified samples in the current view in the App.  
`set_sample_selection_style`([default,Â alt]) | Sets the sample grid selection style in the App.  
`clear_sample_selection_style`() | Clears the sample grid selection style, reverting to default checkmark.  
`set_label_selection_style`([default,Â alt]) | Sets the label selection style in the App.  
`clear_label_selection_style`() | Clears the label selection style, reverting to default dashed.  
`select_labels`([labels,Â ids,Â instance_ids,Â ...]) | Selects the specified labels in the current view in the App.  
`clear_selected_labels`() | Clears the currently selected labels, if any.  
`tag_selected_samples`(tag) | Adds the tag to the currently selected samples, if necessary.  
`untag_selected_samples`(tag) | Removes the tag from the currently selected samples, if necessary.  
`tag_selected_labels`(tag) | Adds the tag to the currently selected labels, if necessary.  
`untag_selected_labels`(tag) | Removes the tag from the currently selected labels, if necessary.  
`summary`() | Returns a string summary of the session.  
`open`() | Opens the App, if necessary.  
`open_tab`() | Opens the App in a new tab of your browser.  
`show`([height]) | Opens the App in the output of the current notebook cell.  
`no_show`() | Returns a context manager that temporarily prevents new App instances from being opened in the current notebook cell when methods are run that normally would show new App windows.  
`wait`([wait]) | Blocks execution until the App is closed by the user.  
`close`() | Closes the session and terminates the App, if necessary.  
`freeze`() | Screenshots the active App cell, replacing it with a static image.  
  
property auto: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

The auto setting for the session.

property server_port: int#
    

The server port for the session.

property server_address: str#
    

The server address for the session, or None if not specified.

property remote: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Whether the session is remote.

property url: str#
    

The URL of the session.

property config: [AppConfig](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig")#
    

The current [`fiftyone.core.config.AppConfig`](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig").

For changes to a sessionâs config to take effect in the App, a call to `Session.refresh()` or another state-updating action such as session.view = my_view must occur.

Example usage:
    
    
    import fiftyone as fo
    
    dataset, session = fo.quickstart()
    
    # change the show confidence setting and push the change to the App
    session.config.show_confidence = False
    session.refresh()
    

property group_id: str | None#
    

The current [`fiftyone.core.groups.Group`](api__fiftyone.core.groups.md#fiftyone.core.groups.Group "fiftyone.core.groups.Group") ID in the modal, if any.

property sample_id: str | None#
    

The current [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") ID in the modal, if any.

property spaces: [Space](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space")#
    

The layout state for the session.

load_workspace(_workspace : str_) → None#
    

Loads the given saved workspace.

Parameters:
    

**workspace** â the name of a saved workspace

property color_scheme: [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme")#
    

The color scheme for the session.

property dataset: [Dataset](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") | None#
    

The [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") connected to the session.

clear_dataset() → None#
    

Clears the current [`fiftyone.core.dataset.Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") from the session, if any.

property view: [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") | None#
    

The [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") connected to the session, or `None` if no view is connected.

clear_view() → None#
    

Clears the current [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") from the session, if any.

property has_plots: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool")#
    

Whether this session has any attached plots.

property plots: [PlotManager](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") | None#
    

The [`fiftyone.core.plots.manager.PlotManager`](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") instance that manages plots attached to this session.

refresh() → None#
    

Refreshes the current App window.

property selected: List[str]#
    

A list of IDs of the currently selected samples in the App, if any.

property selected_samples: List[Dict]#
    

A list of selected sample dicts, each with `id` and `type` (`"default"` or `"alt"`), where type corresponds to a key in `sample_selection_style`.

Despite its name, `selected_samples` represents whatever sample grid items are in the current view: samples in a standard dataset view, patches in a patches view, clips in a clips view, or frames in a frames view.

clear_selected() → None#
    

Clears the currently selected samples, if any.

select_samples(_ids : str | Iterable | None = None_, _tags : str | Iterable[str] | None = None_) → None#
    

Selects the specified samples in the current view in the App.

Despite its name, this applies to whatever sample grid items are in the current view: samples, patches, clips, or frames.

Parameters:
    

  * **ids** (_None_) â an ID or iterable of IDs to select. Items can be plain strings (all `"default"` type) or dicts of the form `{"id": "...", "type": "default"|"alt"}`, where type corresponds to a key in `sample_selection_style`.

  * **tags** (_None_) â a tag or iterable of tags to select




property sample_selection_style: Dict#
    

The current sample grid selection style config.

A dict with a `default` key and optional `alt` key specifying icon styles.

set_sample_selection_style(_default : str = 'checkmark'_, _alt : str = 'checkmark'_) → None#
    

Sets the sample grid selection style in the App.

Parameters:
    

  * **default** (_"checkmark"_) â the default selection icon style. Supported values are `"checkmark"`, `"green-checkmark"`, `"red-checkmark"`, `"thumbsup"`, `"thumbsdown"`, `"pin"`, `"star"`, `"x"`, `"bookmark"`

  * **alt** (_"checkmark"_) â the alt selection icon style




clear_sample_selection_style() → None#
    

Clears the sample grid selection style, reverting to default checkmark.

property label_selection_style: Dict#
    

The current label selection style config.

A dict with a `default` key and optional `alt` key specifying label selection visual styles.

set_label_selection_style(_default : str = 'dashed'_, _alt : str = 'dashed'_) → None#
    

Sets the label selection style in the App.

Parameters:
    

  * **default** (_"dashed"_) â the default label selection style. Supported values are `"dashed"`, `"dashed-green"`, `"dashed-red"`

  * **alt** (_"dashed"_) â the alt label selection style




clear_label_selection_style() → None#
    

Clears the label selection style, reverting to default dashed.

property selected_labels: List[dict]#
    

A list of labels currently selected in the App.

Items are dictionaries with the following keys:

  * `label_id`: the ID of the label

  * `sample_id`: the ID of the sample containing the label

  * `instance_id`: the instance ID of the label (optional)

  * `field`: the field name containing the label

  * `frame_number`: the frame number containing the label (only applicable to video samples)

  * `type`: the selection type (`"default"` or `"alt"`), which determines the visual style applied via `label_selection_style`




select_labels(_labels : List[dict] | None = None_, _ids : str | Iterable[str] | None = None_, _instance_ids : str | Iterable[str] | None = None_, _tags : str | Iterable[str] | None = None_, _fields : str | Iterable[str] | None = None_) → None#
    

Selects the specified labels in the current view in the App.

This method uses the same interface as [`fiftyone.core.collections.SampleCollection.select_labels()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.select_labels "fiftyone.core.collections.SampleCollection.select_labels") to specify the labels to select.

Parameters:
    

  * **labels** (_None_) â a list of dicts specifying the labels to select

  * **ids** (_None_) â an ID or iterable of IDs of the labels to select

  * **instance_ids** (_None_) â an instance ID or iterable of instance IDs of the labels to select

  * **tags** (_None_) â a tag or iterable of tags of labels to select

  * **fields** (_None_) â a field or iterable of fields from which to select




clear_selected_labels() → None#
    

Clears the currently selected labels, if any.

tag_selected_samples(_tag : str_) → None#
    

Adds the tag to the currently selected samples, if necessary.

The currently selected labels are `Session.selected`.

Parameters:
    

**tag** â a tag

untag_selected_samples(_tag : str_) → None#
    

Removes the tag from the currently selected samples, if necessary.

The currently selected labels are `Session.selected`.

Parameters:
    

**tag** â a tag

tag_selected_labels(_tag : str_) → None#
    

Adds the tag to the currently selected labels, if necessary.

The currently selected labels are `Session.selected_labels`.

Parameters:
    

**tag** â a tag

untag_selected_labels(_tag : str_) → None#
    

Removes the tag from the currently selected labels, if necessary.

The currently selected labels are `Session.selected_labels`.

Parameters:
    

**tag** â a tag

property selected_view: [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") | None#
    

A [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the currently selected content in the App.

The selected view is defined as follows:

  * If both samples and labels are selected, the view will contain only the `selected_labels` from within the `selected` samples

  * If samples are selected, the view will only contain the `selected` samples

  * If labels are selected, the view will only contain the `selected_labels`

  * If no samples or labels are selected, the view will be `None`




summary() → str#
    

Returns a string summary of the session.

Returns:
    

a string summary

open() → None#
    

Opens the App, if necessary.

The behavior of this method depends on your context:

  * Notebooks: calls `Session.show()` to open a new App window in the output of your current cell

  * Other (non-remote): opens the App in a new browser tab




open_tab() → None#
    

Opens the App in a new tab of your browser.

This method can be called from Jupyter notebooks to override the default location of the App.

show(_height : int = None_) → None#
    

Opens the App in the output of the current notebook cell.

This method has no effect in non-notebook contexts.

Parameters:
    

**height** (_None_) â a height, in pixels, for the App

no_show() → [SetAttributes](api__fiftyone.core.utils.md#fiftyone.core.utils.SetAttributes "fiftyone.core.utils.SetAttributes")#
    

Returns a context manager that temporarily prevents new App instances from being opened in the current notebook cell when methods are run that normally would show new App windows.

This method has no effect in non-notebook contexts.

Examples:
    
    
    import fiftyone as fo
    
    dataset = foz.load_zoo_dataset("quickstart")
    session = fo.launch_app(dataset)
    
    # (new cell)
    
    # Opens a new App instance
    session.view = dataset.take(100)
    
    # (new cell)
    
    # Does not open a new App instance
    with session.no_show():
        session.view = dataset.take(100)
    

Returns:
    

a context manager

wait(_wait : float = 3_) → None#
    

Blocks execution until the App is closed by the user.

All connected windows (tabs) must be closed before this method will unblock.

Parameters:
    

**wait** (_3_) â the number of seconds to wait for a new App connection before returning if all connections are lost. If negative, the process will wait forever, regardless of connections

close() → None#
    

Closes the session and terminates the App, if necessary.

freeze() → None#
    

Screenshots the active App cell, replacing it with a static image.

Only applicable to notebook contexts.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
