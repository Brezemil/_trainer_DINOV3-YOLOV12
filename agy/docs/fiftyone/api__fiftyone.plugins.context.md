---
source_url: https://docs.voxel51.com/api/fiftyone.plugins.context.html
---

# fiftyone.plugins.context#

FiftyOne plugin context.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`build_plugin_contexts`([enabled]) | Returns contexts for all available plugins.  
---|---  
  
**Classes:**

`PluginContext`(plugin_definition) | Context that represents a plugin and the Python objects it creates.  
---|---  
  
fiftyone.plugins.context.build_plugin_contexts(_enabled =True_)#
    

Returns contexts for all available plugins.

Parameters:
    

**enabled** (_True_) â whether to include only enabled plugins (True) or only disabled plugins (False) or all plugins (âallâ)

Returns:
    

a list of `PluginContext` instances

class fiftyone.plugins.context.PluginContext(_plugin_definition_)#
    

Bases: `object`

Context that represents a plugin and the Python objects it creates.

Parameters:
    

**plugin_definition** â the [`fiftyone.plugins.PluginDefinition`](api__fiftyone.plugins.md#fiftyone.plugins.PluginDefinition "fiftyone.plugins.PluginDefinition") for the plugin

**Attributes:**

`name` | The plugin name.  
---|---  
`secrets` | List of keys for required secrets as specified in the plugin definition.  
  
**Methods:**

`has_errors`() | Determines whether the plugin has errors.  
---|---  
`can_register`(instance) | Determines whether the given operator can be registered.  
`register`(cls) | Registers the given operator on the plugin.  
`register_all`() | Registers all operators defined by the plugin on this context.  
`dispose_all`() | Disposes all operators from this context.  
  
property name#
    

The plugin name.

property secrets#
    

List of keys for required secrets as specified in the plugin definition.

has_errors()#
    

Determines whether the plugin has errors.

Returns:
    

True/False

can_register(_instance_)#
    

Determines whether the given operator can be registered.

Parameters:
    

**instance** â an [`fiftyone.operators.operator.Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

Returns:
    

True/False

register(_cls_)#
    

Registers the given operator on the plugin.

Note

Any errors are logged rather than being raised.

Parameters:
    

**cls** â an [`fiftyone.operators.operator.Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator") or [`fiftyone.operators.panel.Panel`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel "fiftyone.operators.panel.Panel") class

register_all()#
    

Registers all operators defined by the plugin on this context.

Note

Any errors are logged rather than being raised.

dispose_all()#
    

Disposes all operators from this context.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
