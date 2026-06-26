---
source_url: https://docs.voxel51.com/api/fiftyone.operators.operations.html
---

# fiftyone.operators.operations#

FiftyOne operator execution.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Operations`(ctx) | Interface to trigger builtin operations on an execution context.  
---|---  
  
class fiftyone.operators.operations.Operations(_ctx_)#
    

Bases: `object`

Interface to trigger builtin operations on an execution context.

Parameters:
    

**ctx** â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

**Methods:**

`clone_selected_samples`() | Clone the selected samples in the App.  
---|---  
`clone_sample_field`(field_name,Â new_field_name) | Clone a sample field to a new field name.  
`rename_sample_field`(field_name,Â new_field_name) | Rename a sample field to a new field name.  
`clear_sample_field`(field_name) | Clear the contents of a sample field.  
`delete_selected_samples`() | Delete the selected samples in the App.  
`delete_selected_labels`() | Delete the selected labels in the App.  
`delete_sample_field`(field_name) | Delete a sample field.  
`print_stdout`(message) | Print a message to the standard output.  
`list_files`([path,Â list_filesystems]) | List files in a directory or list filesystems.  
`reload_samples`() | Reload the sample grid in the App.  
`reload_dataset`() | Reload the dataset in the App.  
`clear_selected_samples`() | Clear selected samples in the App.  
`copy_view_as_json`() | Copy the current view in the App as JSON.  
`view_from_json`() | Set the view in the App from JSON present in clipboard.  
`clear_panel_state`([panel_id]) | Clear the state of the specified panel in the App.  
`clear_panel_data`([panel_id]) | Clear the data of the specified panel in the App.  
`set_panel_state`(state[,Â panel_id]) | Set the entire state of the specified panel in the App.  
`set_panel_data`(data[,Â panel_id]) | Set the entire data of the specified panel in the App.  
`patch_panel_state`(state[,Â panel_id]) | Patch the state of the specified panel in the App.  
`patch_panel_data`(data[,Â panel_id]) | Patch the state of the specified panel in the App.  
`reduce_panel_state`(reducer[,Â panel_id]) | Reduce the state of the specified panel in the App.  
`apply_panel_state_path`(path[,Â panel_id]) | Force update the state for path in the specified panel in the App.  
`show_panel_output`(output[,Â panel_id]) | Show output in the specified panel in the App.  
`open_panel`(name[,Â is_active,Â layout,Â force,Â ...]) | Open a panel with the given name and layout options in the App.  
`register_panel`(name,Â label[,Â help_markdown,Â ...]) | Registers a panel with the given name and lifecycle callbacks.  
`open_all_panels`() | Open all available panels in the App.  
`close_panel`([name,Â id]) | Close the given panel in the App.  
`close_all_panels`() | Close all open panels in the App.  
`split_panel`(name,Â layout) | Split the panel with the given layout in the App.  
`open_dataset`(dataset_name) | Open the specified dataset in the App.  
`clear_view`() | Clear the view bar in the App.  
`clear_sidebar_filters`() | Clear all filters in the App's sidebar.  
`clear_all_stages`() | Clear all selections, filters, and view stages from the App.  
`refresh_colors`() | Refresh the colors used in the App's UI.  
`show_selected_samples`() | Show the samples that are currently selected in the App.  
`convert_extended_selection_to_selected_samples`() | Convert the extended selection to selected samples in the App.  
`set_selected_samples`(samples) | Select the specified samples in the App.  
`set_sample_selection_style`([default,Â alt]) | Set the sample grid selection style in the App.  
`clear_sample_selection_style`() | Clear the sample grid selection style in the App, reverting to default.  
`set_label_selection_style`([default,Â alt]) | Set the label selection style in the App.  
`clear_label_selection_style`() | Clear the label selection style in the App, reverting to default.  
`set_view`([view,Â name]) | Set the current view in the App.  
`show_samples`(samples[,Â use_extended_selection]) | Show specific samples, optionally using extended selection in the App.  
`console_log`(message) | Log a message to the console.  
`show_output`(outputs,Â results) | Show output in the App's UI.  
`set_progress`([label,Â progress,Â variant]) | Set the progress indicator in the App's UI.  
`test_operator`(operator,Â raw_params) | Test the operator with given parameters.  
`set_selected_labels`(labels) | Set the selected labels in the App.  
`clear_selected_labels`() | Clear the selected labels in the App.  
`notify`(message[,Â variant]) | Show a notification in the App.  
`set_extended_selection`([selection,Â scope,Â ...]) | Sets the extended selection in the App.  
`set_spaces`([spaces,Â name]) | Sets the current spaces in the App.  
`set_active_fields`([fields]) | Set the active fields in the App.  
`clear_active_fields`() | Clear the active fields in the App.  
`track_event`(event[,Â properties]) | Track an event in the App.  
`set_panel_title`([id,Â title]) | Set the title of the specified panel in the App.  
`set_group_slice`(slice) | Set the active group slice in the App.  
`open_sample`([id,Â group_id]) | Opens the specified sample or group in the App's sample modal.  
`close_sample`() | Closes the App's sample modal.  
`show_sidebar`() | Show the App's sidebar.  
`hide_sidebar`() | Hide the App's sidebar.  
`toggle_sidebar`() | Toggle the visibility of the App's sidebar.  
`browser_download`(url[,Â filename]) | Download a file from a URL using the browser's download functionality.  
  
clone_selected_samples()#
    

Clone the selected samples in the App.

clone_sample_field(_field_name_ , _new_field_name_)#
    

Clone a sample field to a new field name.

Parameters:
    

  * **field_name** â the name of the field to clone

  * **new_field_name** â the name for the new field




rename_sample_field(_field_name_ , _new_field_name_)#
    

Rename a sample field to a new field name.

Parameters:
    

  * **field_name** â the name of the field to rename

  * **new_field_name** â the new name for the field




clear_sample_field(_field_name_)#
    

Clear the contents of a sample field.

Parameters:
    

**field_name** â the name of the field to clear

delete_selected_samples()#
    

Delete the selected samples in the App.

delete_selected_labels()#
    

Delete the selected labels in the App.

delete_sample_field(_field_name_)#
    

Delete a sample field.

Parameters:
    

**field_name** â the name of the field to delete

print_stdout(_message_)#
    

Print a message to the standard output.

Parameters:
    

**message** â the message to print

list_files(_path =None_, _list_filesystems =False_)#
    

List files in a directory or list filesystems.

Parameters:
    

  * **path** (_None_) â the path to list files from, or None to list filesystems

  * **list_filesystems** (_False_) â whether to list filesystems instead of files




reload_samples()#
    

Reload the sample grid in the App.

reload_dataset()#
    

Reload the dataset in the App.

clear_selected_samples()#
    

Clear selected samples in the App.

copy_view_as_json()#
    

Copy the current view in the App as JSON.

view_from_json()#
    

Set the view in the App from JSON present in clipboard.

clear_panel_state(_panel_id =None_)#
    

Clear the state of the specified panel in the App.

Parameters:
    

**panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used

clear_panel_data(_panel_id =None_)#
    

Clear the data of the specified panel in the App.

Parameters:
    

**panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used

set_panel_state(_state_ , _panel_id =None_)#
    

Set the entire state of the specified panel in the App.

Parameters:
    

  * **state** â the state to set

  * **panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used




set_panel_data(_data_ , _panel_id =None_)#
    

Set the entire data of the specified panel in the App.

Parameters:
    

  * **data** â the data to set

  * **panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used




patch_panel_state(_state_ , _panel_id =None_)#
    

Patch the state of the specified panel in the App.

Parameters:
    

  * **state** â the state to set

  * **panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used




patch_panel_data(_data_ , _panel_id =None_)#
    

Patch the state of the specified panel in the App.

Parameters:
    

  * **data** â the data to set

  * **panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used




reduce_panel_state(_reducer_ , _panel_id =None_)#
    

Reduce the state of the specified panel in the App.

Parameters:
    

  * **reducer** â the reducer to apply

  * **panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used




apply_panel_state_path(_path_ , _panel_id =None_)#
    

Force update the state for path in the specified panel in the App.

Parameters:
    

**path** (_str_) â the path to force update

show_panel_output(_output_ , _panel_id =None_)#
    

Show output in the specified panel in the App.

Parameters:
    

  * **output** â the output to show

  * **panel_id** (_None_) â the optional ID of the panel to clear. If not provided, the `ctx.panel_id` will be used




open_panel(_name_ , _is_active =True_, _layout =None_, _force =False_, _force_duplicate =False_, _state =None_, _data =None_)#
    

Open a panel with the given name and layout options in the App.

Parameters:
    

  * **name** â the name of the panel to open

  * **is_active** (_True_) â whether to activate the panel immediately

  * **layout** (_None_) â the layout orientation `("horizontal", "vertical")`, if applicable

  * **force** (_False_) â whether to force open the panel. Skips the check to see if a panel with the same name exists or whether the panel declares `allow_multiple=False`

  * **force_duplicate** (_False_) â whether to force open the panel even if it is already open. Only applicable if force is `True`

  * **state** (_None_) â optional initial state to set for the panel

  * **data** (_None_) â optional initial data to set for the panel




register_panel(_name_ , _label_ , _help_markdown =None_, _category =Categories.CUSTOM_, _alpha =False_, _beta =False_, _is_new =False_, _icon =None_, _light_icon =None_, _dark_icon =None_, _surfaces ='grid'_, _on_load =None_, _on_unload =None_, _on_change =None_, _on_change_ctx =None_, _on_change_dataset =None_, _on_change_view =None_, _on_change_spaces =None_, _on_change_current_sample =None_, _on_change_selected =None_, _on_change_selected_labels =None_, _on_change_extended_selection =None_, _on_change_group_slice =None_, _on_change_query_performance =None_, _on_change_active_fields =None_, _allow_duplicates =False_, _priority =None_, __builtin =False_)#
    

Registers a panel with the given name and lifecycle callbacks.

Parameters:
    

  * **name** â the name of the panel

  * **help_markdown** (_None_) â help text associated with the panel in markdown format

  * **label** â the display name of the panel

  * **icon** (_None_) â the icon to show in the panelâs tab

  * **light_icon** (_None_) â the icon to show in the panelâs tab when the App is in light mode

  * **dark_icon** (_None_) â the icon to show in the panelâs tab when the App is in dark mode

  * **surfaces** (_'grid'_) â surfaces in which to show the panel. Must be one of âgridâ, âmodalâ, or âgrid modalâ

  * **alpha** (_False_) â whether the panel is in alpha

  * **beta** (_False_) â whether the panel is in beta

  * **is_new** (_False_) â whether the panel is new

  * **category** ([_Categories.CUSTOM_](api__fiftyone.operators.md#fiftyone.operators.Categories.CUSTOM "fiftyone.operators.Categories.CUSTOM")) â the category of the panel

  * **on_load** (_None_) â an operator to invoke when the panel is loaded

  * **on_unload** (_None_) â an operator to invoke when the panel is unloaded

  * **on_change** (_None_) â an operator to invoke when the panel state changes

  * **on_change_ctx** (_None_) â an operator to invoke when the panel execution context changes

  * **on_change_dataset** (_None_) â an operator to invoke when the current dataset changes

  * **on_change_view** (_None_) â an operator to invoke when the current view changes

  * **on_change_spaces** (_None_) â an operator to invoke when the current spaces layout changes

  * **on_change_current_sample** (_None_) â an operator to invoke when the current sample changes

  * **on_change_selected** (_None_) â an operator to invoke when the current selected samples changes

  * **on_change_selected_labels** (_None_) â an operator to invoke when the current selected labels changes

  * **on_change_extended_selection** (_None_) â an operator to invoke when the current extended selection changes

  * **on_change_group_slice** (_None_) â an operator to invoke when the group slice changes

  * **on_change_query_performance** (_None_) â an operator to invoke when the query performance changes

  * **on_change_active_fields** (_None_) â an operator to invoke when the active fields change

  * **allow_duplicates** (_False_) â whether to allow multiple instances of the panel to the opened

  * **priority** (_None_) â the priority of the panel, used for sort order

  * **_builtin** (_False_) â whether the panel is a builtin panel




open_all_panels()#
    

Open all available panels in the App.

close_panel(_name =None_, _id =None_)#
    

Close the given panel in the App.

Parameters:
    

  * **name** (_None_) â the name of the panel to close

  * **id** (_None_) â the ID of the panel to close




close_all_panels()#
    

Close all open panels in the App.

split_panel(_name_ , _layout_)#
    

Split the panel with the given layout in the App.

Parameters:
    

  * **name** â the name of the panel to split

  * **layout** â the layout orientation `("horizontal", "vertical")`




open_dataset(_dataset_name_)#
    

Open the specified dataset in the App.

Parameters:
    

**dataset_name** â the name of the dataset to open

clear_view()#
    

Clear the view bar in the App.

clear_sidebar_filters()#
    

Clear all filters in the Appâs sidebar.

clear_all_stages()#
    

Clear all selections, filters, and view stages from the App.

refresh_colors()#
    

Refresh the colors used in the Appâs UI.

show_selected_samples()#
    

Show the samples that are currently selected in the App.

convert_extended_selection_to_selected_samples()#
    

Convert the extended selection to selected samples in the App.

set_selected_samples(_samples_)#
    

Select the specified samples in the App.

Despite its name, `selected_samples` represents whatever sample grid items are in the current view: samples, patches, clips, or frames.

Parameters:
    

**samples** â a list of IDs (strings) or dicts of the form `{"id": "...", "type": "default"|"alt"}`, where type corresponds to a key in `sample_selection_style`

set_sample_selection_style(_default ='checkmark'_, _alt ='checkmark'_)#
    

Set the sample grid selection style in the App.

Parameters:
    

  * **default** (_"checkmark"_) â the default selection icon style. Supported values are `"checkmark"`, `"green-checkmark"`, `"red-checkmark"`, `"thumbsup"`, `"thumbsdown"`, `"pin"`, `"star"`, `"x"`, `"bookmark"`

  * **alt** (_"checkmark"_) â the alt selection icon style




clear_sample_selection_style()#
    

Clear the sample grid selection style in the App, reverting to default.

set_label_selection_style(_default ='dashed'_, _alt ='dashed'_)#
    

Set the label selection style in the App.

Parameters:
    

  * **default** (_"dashed"_) â the default label selection style. Supported values are `"dashed"`, `"dashed-green"`, `"dashed-red"`

  * **alt** (_"dashed"_) â the alt label selection style




clear_label_selection_style()#
    

Clear the label selection style in the App, reverting to default.

set_view(_view =None_, _name =None_)#
    

Set the current view in the App.

Parameters:
    

  * **view** (_None_) â a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to load

  * **name** (_None_) â the name of a saved view to load




show_samples(_samples_ , _use_extended_selection =False_)#
    

Show specific samples, optionally using extended selection in the App.

Parameters:
    

  * **samples** â a list of sample IDs to show

  * **use_extended_selection** (_False_) â whether to use the extended selection feature




console_log(_message_)#
    

Log a message to the console.

Parameters:
    

**message** â the message to log

show_output(_outputs_ , _results_)#
    

Show output in the Appâs UI.

Parameters:
    

  * **outputs** â outputs to show

  * **results** â results to display




set_progress(_label =None_, _progress =None_, _variant =None_)#
    

Set the progress indicator in the Appâs UI.

Parameters:
    

  * **label** (_None_) â a label for the progress indicator

  * **progress** (_None_) â a progress value to set

  * **variant** (_None_) â the type of indicator `("linear", "circular")`




test_operator(_operator_ , _raw_params_)#
    

Test the operator with given parameters.

Parameters:
    

  * **operator** â the operator to test

  * **raw_params** â raw parameters for the operator




set_selected_labels(_labels_)#
    

Set the selected labels in the App.

Parameters:
    

**labels** â the labels to select

clear_selected_labels()#
    

Clear the selected labels in the App.

notify(_message_ , _variant ='info'_)#
    

Show a notification in the App.

Variants are âinfoâ, âsuccessâ, âwarningâ, and âerrorâ.

Parameters:
    

  * **message** â the message to show

  * **variant** (_"info"_) â the type of notification




set_extended_selection(_selection =None_, _scope =None_, _clear =False_, _reset =False_)#
    

Sets the extended selection in the App.

Parameters:
    

  * **selection** (_None_) â the selection to set

  * **scope** (_None_) â the scope of the selection

  * **clear** (_None_) â whether to clear the selection

  * **reset** (_None_) â whether to reset the selection




set_spaces(_spaces =None_, _name =None_)#
    

Sets the current spaces in the App.

Parameters:
    

  * **spaces** (_None_) â a [`fiftyone.core.odm.workspace.Space`](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space") to load

  * **name** (_None_) â the name of the workspace to load




set_active_fields(_fields =None_)#
    

Set the active fields in the App.

Parameters:
    

**fields** (_None_) â the possibly-empty list of fields or `embedded.fields` to set

clear_active_fields()#
    

Clear the active fields in the App.

track_event(_event_ , _properties =None_)#
    

Track an event in the App.

Parameters:
    

  * **event** â the event to track

  * **properties** (_None_) â the properties to track




set_panel_title(_id =None_, _title =None_)#
    

Set the title of the specified panel in the App.

Parameters:
    

  * **id** (_None_) â the ID of the panel to set the title

  * **title** (_None_) â the title to set




set_group_slice(_slice_)#
    

Set the active group slice in the App.

Parameters:
    

**slice** â the group slice to activate

open_sample(_id =None_, _group_id =None_)#
    

Opens the specified sample or group in the Appâs sample modal.

Parameters:
    

  * **id** (_None_) â a sample ID to open in the modal

  * **group_id** (_None_) â a group ID to open in the modal




close_sample()#
    

Closes the Appâs sample modal.

show_sidebar()#
    

Show the Appâs sidebar.

hide_sidebar()#
    

Hide the Appâs sidebar.

toggle_sidebar()#
    

Toggle the visibility of the Appâs sidebar.

browser_download(_url_ , _filename =None_)#
    

Download a file from a URL using the browserâs download functionality.

Parameters:
    

  * **url** â the URL of the file to download

  * **filename** â optional filename for the download (will use URL filename if not provided)




IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
