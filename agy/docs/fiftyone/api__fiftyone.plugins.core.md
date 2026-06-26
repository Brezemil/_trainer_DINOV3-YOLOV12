---
source_url: https://docs.voxel51.com/api/fiftyone.plugins.core.html
---

# fiftyone.plugins.core#

Core plugin methods.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`PluginPackage`(name,Â path[,Â shadow_paths]) | Plugin package.  
---|---  
  
**Functions:**

`list_plugins`([enabled,Â builtin,Â shadowed]) | Lists available plugins.  
---|---  
`enable_plugin`(plugin_name[,Â _allow_missing]) | Enables the given plugin.  
`disable_plugin`(plugin_name[,Â _allow_missing]) | Disables the given plugin.  
`delete_plugin`(plugin_name) | Deletes the given plugin from local disk.  
`list_downloaded_plugins`() | Returns a list of all downloaded plugin names.  
`list_enabled_plugins`() | Returns a list of all enabled plugin names.  
`list_disabled_plugins`() | Returns a list of all disabled plugin names.  
`get_plugin`([name,Â plugin_dir]) | Gets the definition for the given plugin.  
`find_plugin`(name) | Returns the path to the plugin on local disk.  
`download_plugin`(url_or_gh_repo[,Â ...]) | Downloads the plugin(s) from the given location to your local plugins directory (`fo.config.plugins_dir`).  
`load_plugin_requirements`(plugin_name) | Loads the Python package requirements associated with the given plugin, if any.  
`install_plugin_requirements`(plugin_name[,Â ...]) | Installs any Python package requirements associated with the given plugin.  
`ensure_plugin_requirements`(plugin_name[,Â ...]) | Ensures that any Python package requirements associated with the given plugin are installed.  
`ensure_plugin_compatibility`(plugin_name[,Â ...]) | Ensures that the given plugin is compatible with your current FiftyOne package version.  
`create_plugin`(plugin_name[,Â from_files,Â ...]) | Creates a plugin with the given name.  
  
class fiftyone.plugins.core.PluginPackage(_name : str_, _path : str_, _shadow_paths : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str] | None = None_)#
    

Bases: `object`

Plugin package.

Parameters:
    

  * **name** â the name of the plugin

  * **path** â the path to the pluginâs root directory




**Attributes:**

`name` |   
---|---  
`path` |   
`shadow_paths` |   
  
name: str#
    

path: str#
    

shadow_paths: [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[str] | None = None#
    

fiftyone.plugins.core.list_plugins(_enabled =True_, _builtin =False_, _shadowed =False_)#
    

Lists available plugins.

Parameters:
    

  * **enabled** (_True_) â whether to include only enabled plugins (True) or only disabled plugins (False) or all plugins (âallâ)

  * **builtin** (_False_) â whether to include only builtin plugins (True) or only non-builtin plugins (False) or all plugins (âallâ)

  * **shadowed** (_False_) â whether to include only âshadowedâ duplicate plugins (True) or only usable plugins (False) or all plugins (âallâ)



Returns:
    

a list of `PluginDefinition` instances

fiftyone.plugins.core.enable_plugin(_plugin_name_ , __allow_missing =False_)#
    

Enables the given plugin.

Parameters:
    

**plugin_name** â the plugin name

fiftyone.plugins.core.disable_plugin(_plugin_name_ , __allow_missing =False_)#
    

Disables the given plugin.

Parameters:
    

**plugin_name** â the plugin name

fiftyone.plugins.core.delete_plugin(_plugin_name_)#
    

Deletes the given plugin from local disk.

Parameters:
    

**plugin_name** â the plugin name

fiftyone.plugins.core.list_downloaded_plugins()#
    

Returns a list of all downloaded plugin names.

Returns:
    

a list of plugin names

fiftyone.plugins.core.list_enabled_plugins()#
    

Returns a list of all enabled plugin names.

Returns:
    

a list of plugin names

fiftyone.plugins.core.list_disabled_plugins()#
    

Returns a list of all disabled plugin names.

Returns:
    

a list of plugin names

fiftyone.plugins.core.get_plugin(_name =None_, _plugin_dir =None_)#
    

Gets the definition for the given plugin.

Parameters:
    

  * **name** (_None_) â the plugin name

  * **plugin_dir** (_None_) â a directory containing the plugin



Returns:
    

a `PluginDefinition`

fiftyone.plugins.core.find_plugin(_name_)#
    

Returns the path to the plugin on local disk.

Parameters:
    

**name** â the plugin name

Returns:
    

the path to the plugin directory

fiftyone.plugins.core.download_plugin(_url_or_gh_repo_ , _plugin_names =None_, _overwrite =False_)#
    

Downloads the plugin(s) from the given location to your local plugins directory (`fo.config.plugins_dir`).

Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Parameters:
    

  * **url_or_gh_repo** â 

the location to download from, which can be:

    * a GitHub repo URL like `https://github.com/<user>/<repo>`

    * a GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

    * a GitHub ref string like `<user>/<repo>[/<ref>]`

    * a GitHub tree path like `https://github.com/<user>/<repo>/tree/<branch>/<path>`

    * a publicly accessible URL of an archive (eg zip or tar) file

  * **plugin_names** (_None_) â a plugin name or iterable of plugin names to download. By default, all found plugins are downloaded

  * **overwrite** (_False_) â whether to overwrite an existing plugin with the same name if it already exists



Returns:
    

a dict mapping plugin names to plugin directories on disk

fiftyone.plugins.core.load_plugin_requirements(_plugin_name_)#
    

Loads the Python package requirements associated with the given plugin, if any.

Parameters:
    

**plugin_name** â the plugin name

Returns:
    

a list of requirement strings, or `None`

fiftyone.plugins.core.install_plugin_requirements(_plugin_name_ , _error_level =None_)#
    

Installs any Python package requirements associated with the given plugin.

Parameters:
    

  * **plugin_name** â the plugin name

  * **error_level** (_None_) â 

the error level to use, defined as:

    * 0: raise error if the install fails

    * 1: log warning if the install fails

    * 2: ignore install fails

By default, `fiftyone.config.requirement_error_level` is used




fiftyone.plugins.core.ensure_plugin_requirements(_plugin_name_ , _error_level =None_, _log_success =False_)#
    

Ensures that any Python package requirements associated with the given plugin are installed.

Parameters:
    

  * **plugin_name** â the plugin name

  * **error_level** (_None_) â 

the error level to use, defined as:

    * 0: raise error if requirement is not satisfied

    * 1: log warning if requirement is not satisfied

    * 2: ignore unsatisifed requirements

By default, `fiftyone.config.requirement_error_level` is used

  * **log_success** (_False_) â whether to generate a log message if a requirement is satisfied




fiftyone.plugins.core.ensure_plugin_compatibility(_plugin_name_ , _error_level =None_, _log_success =False_)#
    

Ensures that the given plugin is compatible with your current FiftyOne package version.

Parameters:
    

  * **plugin_name** â the plugin name

  * **error_level** (_None_) â 

the error level to use, defined as:

    * 0: raise error if plugin is not compatible

    * 1: log warning if plugin is not satisfied

    * 2: ignore fiftyone compatibility requirements

By default, `fiftyone.config.requirement_error_level` is used

  * **log_success** (_False_) â whether to generate a log message if the plugin is compatible




fiftyone.plugins.core.create_plugin(_plugin_name_ , _from_files =None_, _outdir =None_, _description =None_, _tags =None_, _version =None_, _overwrite =False_, _** kwargs_)#
    

Creates a plugin with the given name.

If no `from_files` are provided, a directory containing only the pluginâs metadata file will be created.

If no `outdir` is specified, the plugin is created within your local plugins directory (`fo.config.plugins_dir`).

Parameters:
    

  * **plugin_name** â the name of the plugin

  * **from_files** (_None_) â a directory or list of explicit filepaths to include in the plugin

  * **outdir** (_None_) â the path at which to create the plugin directory. If not provided, the plugin is created within your `fo_config.plugins_dir`

  * **description** (_None_) â a description for the plugin

  * **tags** (_None_) â a tag or list of tags for the plugin

  * **version** (_None_) â an optional FiftyOne version requirement string

  * **overwrite** (_False_) â whether to overwrite a local plugin with the same name if one exists

  * ****kwargs** â additional keyword arguments to include in the plugin definition



Returns:
    

the directory containing the created plugin

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
