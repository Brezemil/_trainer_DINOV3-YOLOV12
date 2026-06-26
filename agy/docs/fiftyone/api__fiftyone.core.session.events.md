---
source_url: https://docs.voxel51.com/api/fiftyone.core.session.events.html
---

# fiftyone.core.session.events#

Session events.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Event`() | Base server event  
---|---  
`LabelData`(label_id,Â field,Â sample_id[,Â ...]) |   
`Screenshot`(bytes,Â max_width) |   
`CaptureNotebookCell`(subscription,Â src,Â width) | Capture notebook cell screenshot event  
`CloseSession`() | Close session event  
`DeactivateNotebookCell`() | Deactivate notebook cell event  
`Ping`() | Ping (builtin) event  
`ReactivateNotebookCell`(subscription) | Reactivate notebook cell event  
`Refresh`(state) | Refresh event  
`SelectLabels`(labels) | Select labels event  
`SelectSamples`(samples) | Select samples event  
`SetSampleSelectionStyle`(style) | Set the sample selection icon style.  
`SetLabelSelectionStyle`(style) | Set the label selection visual style.  
`ValueColor`(color,Â value) |   
`MaskColor`(color,Â intTarget) |   
`CustomizeColor`(path[,Â fieldColor,Â ...]) |   
`ColorscaleList`(value,Â color) |   
`Colorscale`(path[,Â name,Â list]) |   
`DefaultColorscale`([name,Â list]) |   
`LabelTagsColors`([fieldColor,Â valueColors]) |   
`ColorScheme`([color_pool,Â color_by,Â ...]) |   
`SetColorScheme`(color_scheme) | Set color scheme event  
`SetDatasetColorScheme`() | Set dataset color scheme event  
`SetSample`([group_id,Â sample_id]) | Set sample event  
`SetSpaces`(spaces) | Set spaces event  
`SetGroupSlice`(slice) | Set group slice eventt  
`SetFieldVisibilityStage`([stage]) |   
`StateUpdate`(state) | State update event  
`AppInitializer`([dataset,Â group_id,Â ...]) |   
`ListenPayload`(initializer,Â events,Â subscription) | An initialization payload for an event listener request  
  
**Functions:**

`add_screenshot`(event) |   
---|---  
`dict_factory`(data) |   
`get_screenshot`(subscription[,Â pop]) |   
  
class fiftyone.core.session.events.Event#
    

Bases: `object`

Base server event

**Methods:**

`get_event_name`() |   
---|---  
`from_data`(event_name,Â data) |   
`from_data_async`(event_name,Â data) |   
`serialize`() |   
  
classmethod get_event_name() → str#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

serialize()#
    

class fiftyone.core.session.events.LabelData(_label_id : str_, _field : str_, _sample_id : str_, _frame_number : int | None = None_, _instance_id : str | None = None_, _type : str = 'default'_)#
    

Bases: `object`

**Attributes:**

`label_id` |   
---|---  
`field` |   
`sample_id` |   
`frame_number` |   
`instance_id` |   
`type` |   
  
label_id: str#
    

field: str#
    

sample_id: str#
    

frame_number: int | None = None#
    

instance_id: str | None = None#
    

type: str = 'default'#
    

class fiftyone.core.session.events.Screenshot(_bytes : bytes_, _max_width : int_)#
    

Bases: `object`

**Attributes:**

`bytes` |   
---|---  
`max_width` |   
  
bytes: bytes#
    

max_width: int#
    

class fiftyone.core.session.events.CaptureNotebookCell(_subscription : str_, _src : str_, _width : int_)#
    

Bases: `Event`

Capture notebook cell screenshot event

**Attributes:**

`subscription` |   
---|---  
`src` |   
`width` |   
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
subscription: str#
    

src: str#
    

width: int#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.CloseSession#
    

Bases: `Event`

Close session event

**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.DeactivateNotebookCell#
    

Bases: `Event`

Deactivate notebook cell event

**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.Ping#
    

Bases: `Event`

Ping (builtin) event

**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.ReactivateNotebookCell(_subscription : str_)#
    

Bases: `Event`

Reactivate notebook cell event

**Attributes:**

`subscription` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
subscription: str#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.Refresh(_state : [StateDescription](api__fiftyone.core.state.md#fiftyone.core.state.StateDescription "fiftyone.core.state.StateDescription")_)#
    

Bases: `Event`

Refresh event

**Attributes:**

`state` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
state: [StateDescription](api__fiftyone.core.state.md#fiftyone.core.state.StateDescription "fiftyone.core.state.StateDescription")#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SelectLabels(_labels : List[LabelData]_)#
    

Bases: `Event`

Select labels event

**Attributes:**

`labels` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
labels: List[LabelData]#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SelectSamples(_samples : List[Dict]_)#
    

Bases: `Event`

Select samples event

**Attributes:**

`samples` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
samples: List[Dict]#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SetSampleSelectionStyle(_style : Dict_)#
    

Bases: `Event`

Set the sample selection icon style.

style#
    

a dict with `"default"` and `"alt"` keys mapping to icon style names (e.g. `"checkmark"`, `"thumbsup"`, etc.)

Type:
    

Dict

**Attributes:**

`style` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
style: Dict#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SetLabelSelectionStyle(_style : Dict_)#
    

Bases: `Event`

Set the label selection visual style.

style#
    

a dict with `"default"` and `"alt"` keys mapping to label selection style names (e.g. `"dashed"`, `"dashed-red"`, etc.)

Type:
    

Dict

**Attributes:**

`style` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
style: Dict#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.ValueColor(_color : str_, _value : str_)#
    

Bases: `object`

**Attributes:**

`color` |   
---|---  
`value` |   
  
color: str#
    

value: str#
    

class fiftyone.core.session.events.MaskColor(_color : str_, _intTarget : int | None_)#
    

Bases: `object`

**Attributes:**

`color` |   
---|---  
`intTarget` |   
  
color: str#
    

intTarget: int | None#
    

class fiftyone.core.session.events.CustomizeColor(_path : str_, _fieldColor : str | None = None_, _colorByAttribute : str | None = None_, _valueColors : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.ValueColor] | None = None_, _maskTargetsColors : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.MaskColor] | None = None_)#
    

Bases: `object`

**Attributes:**

`path` |   
---|---  
`fieldColor` |   
`colorByAttribute` |   
`valueColors` |   
`maskTargetsColors` |   
  
path: str#
    

fieldColor: str | None = None#
    

colorByAttribute: str | None = None#
    

valueColors: List[ValueColor] | None = None#
    

maskTargetsColors: List[MaskColor] | None = None#
    

class fiftyone.core.session.events.ColorscaleList(_value : float_, _color : str_)#
    

Bases: `object`

**Attributes:**

`value` |   
---|---  
`color` |   
  
value: float#
    

color: str#
    

class fiftyone.core.session.events.Colorscale(_path : str_, _name : str | None = None_, _list : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.ColorscaleList] | None = None_)#
    

Bases: `object`

**Attributes:**

`path` |   
---|---  
`name` |   
`list` |   
  
**Methods:**

`serialize`() |   
---|---  
  
path: str#
    

name: str | None = None#
    

list: List[ColorscaleList] | None = None#
    

serialize()#
    

class fiftyone.core.session.events.DefaultColorscale(_name : str | None = None_, _list : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.ColorscaleList] | None = None_)#
    

Bases: `object`

**Attributes:**

`name` |   
---|---  
`list` |   
  
**Methods:**

`serialize`() |   
---|---  
  
name: str | None = None#
    

list: List[ColorscaleList] | None = None#
    

serialize()#
    

class fiftyone.core.session.events.LabelTagsColors(_fieldColor : str | None = None_, _valueColors : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.ValueColor] | None = None_)#
    

Bases: `object`

**Attributes:**

`fieldColor` |   
---|---  
`valueColors` |   
  
fieldColor: str | None = None#
    

valueColors: List[ValueColor] | None = None#
    

class fiftyone.core.session.events.ColorScheme(_color_pool : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[str] | None = None_, _color_by : str | None = None_, _multicolor_keypoints : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_, _opacity : float | None = None_, _show_skeletons : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_, _fields : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.CustomizeColor] | None = None_, _default_mask_targets_colors : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.MaskColor] | None = None_, _colorscales : [List](api__fiftyone.operators.types.md#fiftyone.operators.types.List "fiftyone.operators.types.List")[fiftyone.core.session.events.Colorscale] | None = None_, _default_colorscale : fiftyone.core.session.events.DefaultColorscale | None = None_, _label_tags : fiftyone.core.session.events.LabelTagsColors | None = None_)#
    

Bases: `object`

**Attributes:**

`color_pool` |   
---|---  
`color_by` |   
`multicolor_keypoints` |   
`opacity` |   
`show_skeletons` |   
`fields` |   
`default_mask_targets_colors` |   
`colorscales` |   
`default_colorscale` |   
`label_tags` |   
  
**Methods:**

`serialize`() |   
---|---  
  
color_pool: List[str] | None = None#
    

color_by: str | None = None#
    

multicolor_keypoints: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None#
    

opacity: float | None = None#
    

show_skeletons: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None#
    

fields: List[CustomizeColor] | None = None#
    

default_mask_targets_colors: List[MaskColor] | None = None#
    

colorscales: List[Colorscale] | None = None#
    

default_colorscale: DefaultColorscale | None = None#
    

label_tags: LabelTagsColors | None = None#
    

serialize()#
    

class fiftyone.core.session.events.SetColorScheme(_color_scheme : ColorScheme_)#
    

Bases: `Event`

Set color scheme event

**Attributes:**

`color_scheme` |   
---|---  
  
**Methods:**

`from_odm`(color_scheme) |   
---|---  
`to_odm`() |   
`from_data`(event_name,Â data) |   
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
color_scheme: ColorScheme#
    

classmethod from_odm(_color_scheme : [ColorScheme](api__fiftyone.core.odm.dataset.md#fiftyone.core.odm.dataset.ColorScheme "fiftyone.core.odm.dataset.ColorScheme")_)#
    

to_odm()#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SetDatasetColorScheme#
    

Bases: `Event`

Set dataset color scheme event

**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SetSample(_group_id : str | None = None_, _sample_id : str | None = None_)#
    

Bases: `Event`

Set sample event

**Attributes:**

`group_id` |   
---|---  
`sample_id` |   
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
group_id: str | None = None#
    

sample_id: str | None = None#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SetSpaces(_spaces : Dict_)#
    

Bases: `Event`

Set spaces event

**Attributes:**

`spaces` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
spaces: Dict#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SetGroupSlice(_slice : str_)#
    

Bases: `Event`

Set group slice eventt

**Attributes:**

`slice` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
slice: str#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.SetFieldVisibilityStage(_stage : Dict | None = None_)#
    

Bases: `Event`

**Attributes:**

`stage` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
stage: Dict | None = None#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.StateUpdate(_state : [StateDescription](api__fiftyone.core.state.md#fiftyone.core.state.StateDescription "fiftyone.core.state.StateDescription")_)#
    

Bases: `Event`

State update event

**Attributes:**

`state` |   
---|---  
  
**Methods:**

`from_data`(event_name,Â data) |   
---|---  
`from_data_async`(event_name,Â data) |   
`get_event_name`() |   
`serialize`() |   
  
state: [StateDescription](api__fiftyone.core.state.md#fiftyone.core.state.StateDescription "fiftyone.core.state.StateDescription")#
    

static from_data(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

async static from_data_async(_event_name : str_, _data : str | dict_) → CaptureNotebookCell | CloseSession | DeactivateNotebookCell | ReactivateNotebookCell | SelectSamples | SelectLabels | SetColorScheme | SetGroupSlice | SetSample | SetLabelSelectionStyle | SetSampleSelectionStyle | SetSpaces | StateUpdate | SetFieldVisibilityStage#
    

classmethod get_event_name() → str#
    

serialize()#
    

class fiftyone.core.session.events.AppInitializer(_dataset : str | None = None_, _group_id : str | None = None_, _group_slice : str | None = None_, _sample_id : str | None = None_, _view : str | None = None_, _workspace : str | None = None_)#
    

Bases: `object`

**Attributes:**

`dataset` |   
---|---  
`group_id` |   
`group_slice` |   
`sample_id` |   
`view` |   
`workspace` |   
  
dataset: str | None = None#
    

group_id: str | None = None#
    

group_slice: str | None = None#
    

sample_id: str | None = None#
    

view: str | None = None#
    

workspace: str | None = None#
    

class fiftyone.core.session.events.ListenPayload(_initializer : AppInitializer | None | [StateDescription](api__fiftyone.core.state.md#fiftyone.core.state.StateDescription "fiftyone.core.state.StateDescription")_, _events : List[str]_, _subscription : str_, _polling : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = False_)#
    

Bases: `object`

An initialization payload for an event listener request

**Attributes:**

`initializer` |   
---|---  
`events` |   
`subscription` |   
`polling` |   
  
**Methods:**

`from_dict`(d) |   
---|---  
  
initializer: AppInitializer | None | [StateDescription](api__fiftyone.core.state.md#fiftyone.core.state.StateDescription "fiftyone.core.state.StateDescription")#
    

events: List[str]#
    

subscription: str#
    

polling: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = False#
    

async classmethod from_dict(_d : dict_) → ListenPayload#
    

fiftyone.core.session.events.add_screenshot(_event : CaptureNotebookCell_) → None#
    

fiftyone.core.session.events.dict_factory(_data : List[Tuple[str, Any]]_) → Dict[str, Any]#
    

fiftyone.core.session.events.get_screenshot(_subscription : str_, _pop =False_) → Screenshot#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
