---
source_url: https://docs.voxel51.com/api/fiftyone.plugins.definitions.html
---

# fiftyone.plugins.definitions#

Plugin definitions.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PluginDefinition`(directory,Â metadata[,Â ...]) | A plugin definition.  
---|---  
  
class fiftyone.plugins.definitions.PluginDefinition(_directory_ , _metadata_ , _shadow_paths =None_)#
    

Bases: `object`

A plugin definition.

Parameters:
    

  * **directory** â the directory containing the plugin

  * **metadata** â a plugin metadata dict

  * **shadow_paths** (_None_) â a list of plugin directories that this plugin shadows




**Attributes:**

`name` | The name of the plugin.  
---|---  
`directory` | The directory containing the plugin.  
`builtin` | Whether the plugin is a builtin plugin.  
`shadow_paths` | A list of plugin directories that this plugin shadows.  
`author` | The author of the plugin.  
`version` | The version of the plugin.  
`url` | The URL of the plugin.  
`license` | The license of the plugin.  
`description` | The description of the plugin.  
`tags` | The tags of the plugin.  
`fiftyone_compatibility` | The FiftyOne compatibility version.  
`fiftyone_requirement` | The FiftyOne requirement as a string like `fiftyone>=0.21`.  
`operators` | The operators of the plugin.  
`skills` | The skills of the plugin.  
`package_json_path` | The absolute path to the package.json file.  
`has_package_json` | Whether the plugin has a package.json file.  
`js_bundle` | The relative path to the JS bundle file.  
`js_bundle_path` |   
`py_entry` |   
`py_entry_path` | The absolute path to the Python entry file.  
`server_path` | The default server path to the plugin.  
`js_bundle_server_path` | The default server path to the JS bundle.  
`js_bundle_hash` | A hash of the plugin's JS bundle file.  
`has_py` | Whether the plugin has a Python entry file.  
`has_js` | Whether the plugin has a JS bundle file.  
`secrets` | A list of required secrets for the plugin.  
  
**Methods:**

`can_register_operator`(name) | Whether the plugin can register the given operator.  
---|---  
`to_dict`() | Returns a JSON dict representation of the plugin metadata.  
`from_disk`(metadata_path[,Â shadow_paths]) | Creates a `PluginDefinition` for the given metadata file.  
  
property name#
    

The name of the plugin.

property directory#
    

The directory containing the plugin.

property builtin#
    

Whether the plugin is a builtin plugin.

property shadow_paths#
    

A list of plugin directories that this plugin shadows.

property author#
    

The author of the plugin.

property version#
    

The version of the plugin.

property url#
    

The URL of the plugin.

property license#
    

The license of the plugin.

property description#
    

The description of the plugin.

property tags#
    

The tags of the plugin.

property fiftyone_compatibility#
    

The FiftyOne compatibility version.

property fiftyone_requirement#
    

The FiftyOne requirement as a string like `fiftyone>=0.21`.

property operators#
    

The operators of the plugin.

property skills#
    

The skills of the plugin.

property package_json_path#
    

The absolute path to the package.json file.

property has_package_json#
    

Whether the plugin has a package.json file.

property js_bundle#
    

The relative path to the JS bundle file.

property js_bundle_path#
    

property py_entry#
    

property py_entry_path#
    

The absolute path to the Python entry file.

property server_path#
    

The default server path to the plugin.

property js_bundle_server_path#
    

The default server path to the JS bundle.

property js_bundle_hash#
    

A hash of the pluginâs JS bundle file.

can_register_operator(_name_)#
    

Whether the plugin can register the given operator.

Parameters:
    

**name** â the operator name

Returns:
    

True/False

property has_py#
    

Whether the plugin has a Python entry file.

property has_js#
    

Whether the plugin has a JS bundle file.

property secrets#
    

A list of required secrets for the plugin.

to_dict()#
    

Returns a JSON dict representation of the plugin metadata.

Returns:
    

a JSON dict

classmethod from_disk(_metadata_path_ , _shadow_paths =None_)#
    

Creates a `PluginDefinition` for the given metadata file.

Parameters:
    

  * **metadata_path** â the path to a plugin `.yaml` file

  * **shadow_paths** (_None_) â a list of plugin directories that this plugin shadows



Returns:
    

a `PluginDefinition`

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
