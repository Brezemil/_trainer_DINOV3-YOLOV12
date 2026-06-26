---
source_url: https://docs.voxel51.com/api/fiftyone.core.session.html
---

# fiftyone.core.session#

  * [fiftyone.core.session.client](api__fiftyone.core.session.client.md)
    * [`Client`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client)
      * [`Client.address`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.address)
      * [`Client.auto`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.auto)
      * [`Client.port`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.port)
      * [`Client.remote`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.remote)
      * [`Client.start_time`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.start_time)
      * [`Client.origin`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.origin)
      * [`Client.is_open`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.is_open)
      * [`Client.open()`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.open)
      * [`Client.close()`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.close)
      * [`Client.send_event()`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.send_event)
      * [`Client.add_event_listener()`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.add_event_listener)
      * [`Client.remove_event_listener()`](api__fiftyone.core.session.client.md#fiftyone.core.session.client.Client.remove_event_listener)
  * [fiftyone.core.session.constants](api__fiftyone.core.session.constants.md)
  * [fiftyone.core.session.events](api__fiftyone.core.session.events.md)
    * [`Event`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Event)
      * [`Event.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Event.get_event_name)
      * [`Event.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Event.from_data)
      * [`Event.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Event.from_data_async)
      * [`Event.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Event.serialize)
    * [`LabelData`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelData)
      * [`LabelData.label_id`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelData.label_id)
      * [`LabelData.field`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelData.field)
      * [`LabelData.sample_id`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelData.sample_id)
      * [`LabelData.frame_number`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelData.frame_number)
      * [`LabelData.instance_id`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelData.instance_id)
      * [`LabelData.type`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelData.type)
    * [`Screenshot`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Screenshot)
      * [`Screenshot.bytes`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Screenshot.bytes)
      * [`Screenshot.max_width`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Screenshot.max_width)
    * [`CaptureNotebookCell`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell)
      * [`CaptureNotebookCell.subscription`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell.subscription)
      * [`CaptureNotebookCell.src`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell.src)
      * [`CaptureNotebookCell.width`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell.width)
      * [`CaptureNotebookCell.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell.from_data)
      * [`CaptureNotebookCell.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell.from_data_async)
      * [`CaptureNotebookCell.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell.get_event_name)
      * [`CaptureNotebookCell.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CaptureNotebookCell.serialize)
    * [`CloseSession`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CloseSession)
      * [`CloseSession.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CloseSession.from_data)
      * [`CloseSession.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CloseSession.from_data_async)
      * [`CloseSession.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CloseSession.get_event_name)
      * [`CloseSession.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CloseSession.serialize)
    * [`DeactivateNotebookCell`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DeactivateNotebookCell)
      * [`DeactivateNotebookCell.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DeactivateNotebookCell.from_data)
      * [`DeactivateNotebookCell.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DeactivateNotebookCell.from_data_async)
      * [`DeactivateNotebookCell.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DeactivateNotebookCell.get_event_name)
      * [`DeactivateNotebookCell.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DeactivateNotebookCell.serialize)
    * [`Ping`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Ping)
      * [`Ping.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Ping.from_data)
      * [`Ping.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Ping.from_data_async)
      * [`Ping.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Ping.get_event_name)
      * [`Ping.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Ping.serialize)
    * [`ReactivateNotebookCell`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ReactivateNotebookCell)
      * [`ReactivateNotebookCell.subscription`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ReactivateNotebookCell.subscription)
      * [`ReactivateNotebookCell.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ReactivateNotebookCell.from_data)
      * [`ReactivateNotebookCell.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ReactivateNotebookCell.from_data_async)
      * [`ReactivateNotebookCell.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ReactivateNotebookCell.get_event_name)
      * [`ReactivateNotebookCell.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ReactivateNotebookCell.serialize)
    * [`Refresh`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Refresh)
      * [`Refresh.state`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Refresh.state)
      * [`Refresh.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Refresh.from_data)
      * [`Refresh.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Refresh.from_data_async)
      * [`Refresh.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Refresh.get_event_name)
      * [`Refresh.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Refresh.serialize)
    * [`SelectLabels`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectLabels)
      * [`SelectLabels.labels`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectLabels.labels)
      * [`SelectLabels.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectLabels.from_data)
      * [`SelectLabels.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectLabels.from_data_async)
      * [`SelectLabels.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectLabels.get_event_name)
      * [`SelectLabels.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectLabels.serialize)
    * [`SelectSamples`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectSamples)
      * [`SelectSamples.samples`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectSamples.samples)
      * [`SelectSamples.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectSamples.from_data)
      * [`SelectSamples.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectSamples.from_data_async)
      * [`SelectSamples.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectSamples.get_event_name)
      * [`SelectSamples.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SelectSamples.serialize)
    * [`SetSampleSelectionStyle`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSampleSelectionStyle)
      * [`SetSampleSelectionStyle.style`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSampleSelectionStyle.style)
      * [`SetSampleSelectionStyle.style`](api__fiftyone.core.session.events.md#id0)
      * [`SetSampleSelectionStyle.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSampleSelectionStyle.from_data)
      * [`SetSampleSelectionStyle.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSampleSelectionStyle.from_data_async)
      * [`SetSampleSelectionStyle.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSampleSelectionStyle.get_event_name)
      * [`SetSampleSelectionStyle.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSampleSelectionStyle.serialize)
    * [`SetLabelSelectionStyle`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetLabelSelectionStyle)
      * [`SetLabelSelectionStyle.style`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetLabelSelectionStyle.style)
      * [`SetLabelSelectionStyle.style`](api__fiftyone.core.session.events.md#id1)
      * [`SetLabelSelectionStyle.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetLabelSelectionStyle.from_data)
      * [`SetLabelSelectionStyle.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetLabelSelectionStyle.from_data_async)
      * [`SetLabelSelectionStyle.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetLabelSelectionStyle.get_event_name)
      * [`SetLabelSelectionStyle.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetLabelSelectionStyle.serialize)
    * [`ValueColor`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ValueColor)
      * [`ValueColor.color`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ValueColor.color)
      * [`ValueColor.value`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ValueColor.value)
    * [`MaskColor`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.MaskColor)
      * [`MaskColor.color`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.MaskColor.color)
      * [`MaskColor.intTarget`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.MaskColor.intTarget)
    * [`CustomizeColor`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CustomizeColor)
      * [`CustomizeColor.path`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CustomizeColor.path)
      * [`CustomizeColor.fieldColor`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CustomizeColor.fieldColor)
      * [`CustomizeColor.colorByAttribute`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CustomizeColor.colorByAttribute)
      * [`CustomizeColor.valueColors`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CustomizeColor.valueColors)
      * [`CustomizeColor.maskTargetsColors`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.CustomizeColor.maskTargetsColors)
    * [`ColorscaleList`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorscaleList)
      * [`ColorscaleList.value`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorscaleList.value)
      * [`ColorscaleList.color`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorscaleList.color)
    * [`Colorscale`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale)
      * [`Colorscale.path`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.path)
      * [`Colorscale.name`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.name)
      * [`Colorscale.list`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list)
      * [`Colorscale.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.serialize)
    * [`DefaultColorscale`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DefaultColorscale)
      * [`DefaultColorscale.name`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DefaultColorscale.name)
      * [`DefaultColorscale.list`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DefaultColorscale.list)
      * [`DefaultColorscale.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.DefaultColorscale.serialize)
    * [`LabelTagsColors`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelTagsColors)
      * [`LabelTagsColors.fieldColor`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelTagsColors.fieldColor)
      * [`LabelTagsColors.valueColors`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.LabelTagsColors.valueColors)
    * [`ColorScheme`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme)
      * [`ColorScheme.color_pool`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.color_pool)
      * [`ColorScheme.color_by`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.color_by)
      * [`ColorScheme.multicolor_keypoints`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.multicolor_keypoints)
      * [`ColorScheme.opacity`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.opacity)
      * [`ColorScheme.show_skeletons`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.show_skeletons)
      * [`ColorScheme.fields`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.fields)
      * [`ColorScheme.default_mask_targets_colors`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.default_mask_targets_colors)
      * [`ColorScheme.colorscales`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.colorscales)
      * [`ColorScheme.default_colorscale`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.default_colorscale)
      * [`ColorScheme.label_tags`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.label_tags)
      * [`ColorScheme.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ColorScheme.serialize)
    * [`SetColorScheme`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme)
      * [`SetColorScheme.color_scheme`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme.color_scheme)
      * [`SetColorScheme.from_odm()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme.from_odm)
      * [`SetColorScheme.to_odm()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme.to_odm)
      * [`SetColorScheme.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme.from_data)
      * [`SetColorScheme.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme.from_data_async)
      * [`SetColorScheme.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme.get_event_name)
      * [`SetColorScheme.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetColorScheme.serialize)
    * [`SetDatasetColorScheme`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetDatasetColorScheme)
      * [`SetDatasetColorScheme.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetDatasetColorScheme.from_data)
      * [`SetDatasetColorScheme.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetDatasetColorScheme.from_data_async)
      * [`SetDatasetColorScheme.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetDatasetColorScheme.get_event_name)
      * [`SetDatasetColorScheme.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetDatasetColorScheme.serialize)
    * [`SetSample`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample)
      * [`SetSample.group_id`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample.group_id)
      * [`SetSample.sample_id`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample.sample_id)
      * [`SetSample.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample.from_data)
      * [`SetSample.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample.from_data_async)
      * [`SetSample.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample.get_event_name)
      * [`SetSample.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSample.serialize)
    * [`SetSpaces`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSpaces)
      * [`SetSpaces.spaces`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSpaces.spaces)
      * [`SetSpaces.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSpaces.from_data)
      * [`SetSpaces.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSpaces.from_data_async)
      * [`SetSpaces.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSpaces.get_event_name)
      * [`SetSpaces.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetSpaces.serialize)
    * [`SetGroupSlice`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetGroupSlice)
      * [`SetGroupSlice.slice`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetGroupSlice.slice)
      * [`SetGroupSlice.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetGroupSlice.from_data)
      * [`SetGroupSlice.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetGroupSlice.from_data_async)
      * [`SetGroupSlice.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetGroupSlice.get_event_name)
      * [`SetGroupSlice.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetGroupSlice.serialize)
    * [`SetFieldVisibilityStage`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetFieldVisibilityStage)
      * [`SetFieldVisibilityStage.stage`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetFieldVisibilityStage.stage)
      * [`SetFieldVisibilityStage.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetFieldVisibilityStage.from_data)
      * [`SetFieldVisibilityStage.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetFieldVisibilityStage.from_data_async)
      * [`SetFieldVisibilityStage.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetFieldVisibilityStage.get_event_name)
      * [`SetFieldVisibilityStage.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.SetFieldVisibilityStage.serialize)
    * [`StateUpdate`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.StateUpdate)
      * [`StateUpdate.state`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.StateUpdate.state)
      * [`StateUpdate.from_data()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.StateUpdate.from_data)
      * [`StateUpdate.from_data_async()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.StateUpdate.from_data_async)
      * [`StateUpdate.get_event_name()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.StateUpdate.get_event_name)
      * [`StateUpdate.serialize()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.StateUpdate.serialize)
    * [`AppInitializer`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.AppInitializer)
      * [`AppInitializer.dataset`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.AppInitializer.dataset)
      * [`AppInitializer.group_id`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.AppInitializer.group_id)
      * [`AppInitializer.group_slice`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.AppInitializer.group_slice)
      * [`AppInitializer.sample_id`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.AppInitializer.sample_id)
      * [`AppInitializer.view`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.AppInitializer.view)
      * [`AppInitializer.workspace`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.AppInitializer.workspace)
    * [`ListenPayload`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ListenPayload)
      * [`ListenPayload.initializer`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ListenPayload.initializer)
      * [`ListenPayload.events`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ListenPayload.events)
      * [`ListenPayload.subscription`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ListenPayload.subscription)
      * [`ListenPayload.polling`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ListenPayload.polling)
      * [`ListenPayload.from_dict()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.ListenPayload.from_dict)
    * [`add_screenshot()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.add_screenshot)
    * [`dict_factory()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.dict_factory)
    * [`get_screenshot()`](api__fiftyone.core.session.events.md#fiftyone.core.session.events.get_screenshot)
  * [fiftyone.core.session.notebooks](api__fiftyone.core.session.notebooks.md)
    * [`NotebookCell`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.NotebookCell)
      * [`NotebookCell.address`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.NotebookCell.address)
      * [`NotebookCell.height`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.NotebookCell.height)
      * [`NotebookCell.handle`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.NotebookCell.handle)
      * [`NotebookCell.port`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.NotebookCell.port)
      * [`NotebookCell.subscription`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.NotebookCell.subscription)
    * [`capture()`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.capture)
    * [`display()`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.display)
    * [`display_ipython()`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.display_ipython)
    * [`display_colab()`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.display_colab)
    * [`display_databricks()`](api__fiftyone.core.session.notebooks.md#fiftyone.core.session.notebooks.display_databricks)
  * [fiftyone.core.session.session](api__fiftyone.core.session.session.md)
    * [`launch_app()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.launch_app)
    * [`close_app()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.close_app)
    * [`update_state()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.update_state)
    * [`Session`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session)
      * [`Session.auto`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.auto)
      * [`Session.server_port`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.server_port)
      * [`Session.server_address`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.server_address)
      * [`Session.remote`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.remote)
      * [`Session.url`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.url)
      * [`Session.config`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.config)
      * [`Session.group_id`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.group_id)
      * [`Session.sample_id`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.sample_id)
      * [`Session.spaces`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.spaces)
      * [`Session.load_workspace()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.load_workspace)
      * [`Session.color_scheme`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.color_scheme)
      * [`Session.dataset`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.dataset)
      * [`Session.clear_dataset()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.clear_dataset)
      * [`Session.view`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.view)
      * [`Session.clear_view()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.clear_view)
      * [`Session.has_plots`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.has_plots)
      * [`Session.plots`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.plots)
      * [`Session.refresh()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.refresh)
      * [`Session.selected`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.selected)
      * [`Session.selected_samples`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.selected_samples)
      * [`Session.clear_selected()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.clear_selected)
      * [`Session.select_samples()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.select_samples)
      * [`Session.sample_selection_style`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.sample_selection_style)
      * [`Session.set_sample_selection_style()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.set_sample_selection_style)
      * [`Session.clear_sample_selection_style()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.clear_sample_selection_style)
      * [`Session.label_selection_style`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.label_selection_style)
      * [`Session.set_label_selection_style()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.set_label_selection_style)
      * [`Session.clear_label_selection_style()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.clear_label_selection_style)
      * [`Session.selected_labels`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.selected_labels)
      * [`Session.select_labels()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.select_labels)
      * [`Session.clear_selected_labels()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.clear_selected_labels)
      * [`Session.tag_selected_samples()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.tag_selected_samples)
      * [`Session.untag_selected_samples()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.untag_selected_samples)
      * [`Session.tag_selected_labels()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.tag_selected_labels)
      * [`Session.untag_selected_labels()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.untag_selected_labels)
      * [`Session.selected_view`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.selected_view)
      * [`Session.summary()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.summary)
      * [`Session.open()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.open)
      * [`Session.open_tab()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.open_tab)
      * [`Session.show()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.show)
      * [`Session.no_show()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.no_show)
      * [`Session.wait()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.wait)
      * [`Session.close()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.close)
      * [`Session.freeze()`](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session.freeze)
  * [fiftyone.core.session.templates](api__fiftyone.core.session.templates.md)
  * [fiftyone.core.session.utils](api__fiftyone.core.session.utils.md)
    * [`normalize_selected_samples()`](api__fiftyone.core.session.utils.md#fiftyone.core.session.utils.normalize_selected_samples)



## Module contents#

Session definitions for interacting with the FiftyOne App.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`close_app`() | Closes the FiftyOne App, if necessary.  
---|---  
`launch_app`([dataset,Â view,Â sample_id,Â ...]) | Launches the FiftyOne App.  
  
**Classes:**

`Session`([dataset,Â view,Â sample_id,Â ...]) | Session that maintains a 1-1 shared state with the FiftyOne App.  
---|---  
  
fiftyone.core.session.close_app() → None#
    

Closes the FiftyOne App, if necessary.

If no App is currently open, this method has no effect.

fiftyone.core.session.launch_app(_dataset : [Dataset](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") = None_, _view : [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") = None_, _sample_id : str = None_, _group_id : str = None_, _spaces : [Space](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space") = None_, _color_scheme : [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme") = None_, _plots : [PlotManager](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") = None_, _port : int = None_, _address : str = None_, _remote : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _browser : str = None_, _height : int = None_, _auto : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _config : [AppConfig](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") = None_) → [Session](api__fiftyone.core.session.session.md#fiftyone.core.session.session.Session "fiftyone.core.session.session.Session")#
    

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

class fiftyone.core.session.Session(_dataset : [Dataset](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") | [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") = None_, _view : [DatasetView](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") = None_, _sample_id : str = None_, _group_id : str = None_, _spaces : [Space](api__fiftyone.core.odm.workspace.md#fiftyone.core.odm.workspace.Space "fiftyone.core.odm.workspace.Space") = None_, _color_scheme : [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme") = None_, _plots : [PlotManager](api__fiftyone.core.plots.manager.md#fiftyone.core.plots.manager.PlotManager "fiftyone.core.plots.manager.PlotManager") = None_, _port : int = None_, _address : str = None_, _remote : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _browser : str = None_, _height : int = None_, _auto : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True_, _config : [AppConfig](api__fiftyone.core.config.md#fiftyone.core.config.AppConfig "fiftyone.core.config.AppConfig") = None_, _view_name : str = None_)#
    

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
