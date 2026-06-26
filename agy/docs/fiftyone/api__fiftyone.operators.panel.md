---
source_url: https://docs.voxel51.com/api/fiftyone.operators.panel.html
---

# fiftyone.operators.panel#

FiftyOne panels.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PanelConfig`(name,Â label[,Â help_markdown,Â ...]) | Configuration for a panel.  
---|---  
`Panel`([_builtin]) | A panel.  
`PanelRefBase`(ctx) | Base class for panel state and data.  
`PanelRefState`(ctx) | Class representing the state of a panel.  
`PanelRefData`(ctx) | Class representing the data of a panel.  
`PanelRef`(ctx) | Class representing a panel.  
  
**Exceptions:**

`WriteOnlyError` | Error raised when trying to read a write-only property.  
---|---  
  
class fiftyone.operators.panel.PanelConfig(_name_ , _label_ , _help_markdown =None_, _alpha =False_, _beta =False_, _is_new =False_, _category =None_, _icon =None_, _light_icon =None_, _dark_icon =None_, _allow_multiple =False_, _surfaces : Literal['grid', 'modal', 'grid modal'] = 'grid'_, _priority =None_, _** kwargs_)#
    

Bases: [`OperatorConfig`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.OperatorConfig "fiftyone.operators.operator.OperatorConfig")

Configuration for a panel.

Parameters:
    

  * **name** â the name of the panel

  * **label** â the display name for the panel

  * **icon** (_None_) â the icon to show in the panelâs tab

  * **light_icon** (_None_) â the icon to show in the panelâs tab when the App is in light mode

  * **dark_icon** (_None_) â the icon to show in the panelâs tab when the App is in dark mode

  * **allow_multiple** (_False_) â whether to allow multiple instances of the panel to be opened

  * **surfaces** (_"grid"_) â the surfaces on which the panel can be displayed

  * **help_markdown** (_None_) â a markdown string to display in the panelâs help tooltip

  * **category** (_Category_) â the category id of the panel

  * **priority** (_None_) â the priority of the panel for sorting in the UI




**Methods:**

`to_json`() |   
---|---  
  
**Attributes:**

`risk_level` | The declared `RiskLevel` for this operator.  
---|---  
  
to_json()#
    

property risk_level#
    

The declared `RiskLevel` for this operator.

class fiftyone.operators.panel.Panel(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

A panel.

**Methods:**

`render`(ctx) | Defines the panel's layout and events.  
---|---  
`resolve_input`(ctx) | Returns the resolved input property.  
`on_startup`(ctx) |   
`on_load`(ctx) |   
`execute`(ctx) | Executes the operator.  
`add_secrets`(secrets) | Adds secrets to the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
**Attributes:**

`builtin` | Whether the operator is builtin.  
---|---  
`config` | The `OperatorConfig` for the operator.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
render(_ctx_)#
    

Defines the panelâs layout and events.

This method is called after every panel event is called (on load, button callback, context change event, etc).

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

resolve_input(_ctx_)#
    

Returns the resolved input property.

Subclasses can implement this method to define the inputs to the operator. This method should never be called directly. Instead use `resolve_type()`.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called each time the input changes.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

on_startup(_ctx_)#
    

on_load(_ctx_)#
    

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

property config#
    

The `OperatorConfig` for the operator.

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

resolve_delegation(_ctx_)#
    

Returns the resolved _forced_ delegation flag.

Subclasses can implement this method to decide if delegated execution should be _forced_ for the given operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

whether the operation should be delegated (True), run immediately (False), or None to defer to `resolve_execution_options()` to specify the available options

resolve_execution_options(_ctx_)#
    

Returns the resolved execution options.

Subclasses can implement this method to define the execution options available for the operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.executor.ExecutionOptions`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions "fiftyone.operators.executor.ExecutionOptions") instance

resolve_output(_ctx_)#
    

Returns the resolved output property.

Subclasses can implement this method to define the outputs of the operator.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called after the operator is executed.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_placement(_ctx_)#
    

Returns the resolved placement of the operator.

Subclasses can implement this method to define the placement of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement "fiftyone.operators.types.Placement"), or None

resolve_run_name(_ctx_)#
    

Returns the resolved run name of the operator.

Subclasses can implement this method to define the run name of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a string, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

exception fiftyone.operators.panel.WriteOnlyError#
    

Bases: `Exception`

Error raised when trying to read a write-only property.

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.operators.panel.PanelRefBase(_ctx_)#
    

Bases: `object`

Base class for panel state and data.

Parameters:
    

**ctx** â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

**Methods:**

`set`(key[,Â value]) | Sets some value(s) in the dictionary.  
---|---  
`get`(key[,Â default]) | Gets a value from the dictionary.  
`clear`() | Clears the dictionary.  
  
set(_key_ , _value =None_)#
    

Sets some value(s) in the dictionary.

Parameters:
    

  * **key** â a key, `"nested.key.path"`, or dict mapping multiple possibly-nested keys to values

  * **value** (_None_) â the value, if key is a string




get(_key_ , _default =None_)#
    

Gets a value from the dictionary.

Parameters:
    

  * **key** â a key or `"nested.key.path"`

  * **default** (_None_) â a default value if the key is not found



Returns:
    

the value

clear()#
    

Clears the dictionary.

class fiftyone.operators.panel.PanelRefState(_ctx_)#
    

Bases: `PanelRefBase`

Class representing the state of a panel.

Parameters:
    

**ctx** â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

**Methods:**

`set`(key[,Â value]) | Sets some panel state.  
---|---  
`clear`() | Clears the panel state.  
`apply`(path) | Applies the state to the panel.  
`get`(key[,Â default]) | Gets a value from the dictionary.  
  
set(_key_ , _value =None_)#
    

Sets some panel state.

Parameters:
    

  * **key** â a key, `"nested.key.path"`, or dict mapping multiple possibly-nested keys to values

  * **value** (_None_) â the value, if key is a string




clear()#
    

Clears the panel state.

apply(_path_)#
    

Applies the state to the panel.

Parameters:
    

**path** (_str_) â The path to the state.

get(_key_ , _default =None_)#
    

Gets a value from the dictionary.

Parameters:
    

  * **key** â a key or `"nested.key.path"`

  * **default** (_None_) â a default value if the key is not found



Returns:
    

the value

class fiftyone.operators.panel.PanelRefData(_ctx_)#
    

Bases: `PanelRefBase`

Class representing the data of a panel.

Parameters:
    

**ctx** â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

**Methods:**

`set`(key[,Â value]) | Sets some panel data.  
---|---  
`get`(key[,Â default]) | Gets a value from the dictionary.  
`clear`() | Clears the panel data.  
  
set(_key_ , _value =None_)#
    

Sets some panel data.

Parameters:
    

  * **key** â a key, `"nested.key.path"`, or dict mapping multiple possibly-nested keys to values

  * **value** (_None_) â the value, if key is a string




get(_key_ , _default =None_)#
    

Gets a value from the dictionary.

Parameters:
    

  * **key** â a key or `"nested.key.path"`

  * **default** (_None_) â a default value if the key is not found



Returns:
    

the value

clear()#
    

Clears the panel data.

class fiftyone.operators.panel.PanelRef(_ctx_)#
    

Bases: `object`

Class representing a panel.

Parameters:
    

**ctx** â an [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

**Attributes:**

`data` | Panel data.  
---|---  
`state` | Panel state.  
`id` | Panel ID.  
  
**Methods:**

`close`() | Closes the panel.  
---|---  
`set_state`(key[,Â value]) | Sets some panel state.  
`get_state`(key[,Â default]) | Gets some panel state.  
`set_data`(key[,Â value]) | Sets some panel data.  
`set_title`(title) | Sets the title of the panel.  
  
property data#
    

Panel data.

property state#
    

Panel state.

property id#
    

Panel ID.

close()#
    

Closes the panel.

set_state(_key_ , _value =None_)#
    

Sets some panel state.

Parameters:
    

  * **key** â a key, `"nested.key.path"`, or dict mapping multiple possibly-nested keys to values

  * **value** (_None_) â the value, if key is a string




get_state(_key_ , _default =None_)#
    

Gets some panel state.

Parameters:
    

  * **key** â the key or `"nested.key.path"`

  * **default** (_None_) â a default value if the key is not found



Returns:
    

the state value

set_data(_key_ , _value =None_)#
    

Sets some panel data.

Parameters:
    

  * **key** â a key, `"nested.key.path"`, or dict mapping multiple possibly-nested keys to values

  * **value** (_None_) â the value, if key is a string




set_title(_title_)#
    

Sets the title of the panel.

Parameters:
    

**title** â a title string

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
