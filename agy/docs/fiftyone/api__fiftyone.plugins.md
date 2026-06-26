---
source_url: https://docs.voxel51.com/api/fiftyone.plugins.html
---

# fiftyone.plugins#

  * [fiftyone.plugins.constants](api__fiftyone.plugins.constants.md)
  * [fiftyone.plugins.context](api__fiftyone.plugins.context.md)
    * [`build_plugin_contexts()`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.build_plugin_contexts)
    * [`PluginContext`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext)
      * [`PluginContext.name`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext.name)
      * [`PluginContext.secrets`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext.secrets)
      * [`PluginContext.has_errors()`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext.has_errors)
      * [`PluginContext.can_register()`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext.can_register)
      * [`PluginContext.register()`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext.register)
      * [`PluginContext.register_all()`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext.register_all)
      * [`PluginContext.dispose_all()`](api__fiftyone.plugins.context.md#fiftyone.plugins.context.PluginContext.dispose_all)
  * [fiftyone.plugins.core](api__fiftyone.plugins.core.md)
    * [`PluginPackage`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.PluginPackage)
      * [`PluginPackage.name`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.PluginPackage.name)
      * [`PluginPackage.path`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.PluginPackage.path)
      * [`PluginPackage.shadow_paths`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.PluginPackage.shadow_paths)
    * [`list_plugins()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.list_plugins)
    * [`enable_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.enable_plugin)
    * [`disable_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.disable_plugin)
    * [`delete_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.delete_plugin)
    * [`list_downloaded_plugins()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.list_downloaded_plugins)
    * [`list_enabled_plugins()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.list_enabled_plugins)
    * [`list_disabled_plugins()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.list_disabled_plugins)
    * [`get_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.get_plugin)
    * [`find_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.find_plugin)
    * [`download_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.download_plugin)
    * [`load_plugin_requirements()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.load_plugin_requirements)
    * [`install_plugin_requirements()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.install_plugin_requirements)
    * [`ensure_plugin_requirements()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.ensure_plugin_requirements)
    * [`ensure_plugin_compatibility()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.ensure_plugin_compatibility)
    * [`create_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.create_plugin)
  * [fiftyone.plugins.definitions](api__fiftyone.plugins.definitions.md)
    * [`PluginDefinition`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition)
      * [`PluginDefinition.name`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.name)
      * [`PluginDefinition.directory`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.directory)
      * [`PluginDefinition.builtin`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.builtin)
      * [`PluginDefinition.shadow_paths`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.shadow_paths)
      * [`PluginDefinition.author`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.author)
      * [`PluginDefinition.version`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.version)
      * [`PluginDefinition.url`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.url)
      * [`PluginDefinition.license`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.license)
      * [`PluginDefinition.description`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.description)
      * [`PluginDefinition.tags`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.tags)
      * [`PluginDefinition.fiftyone_compatibility`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.fiftyone_compatibility)
      * [`PluginDefinition.fiftyone_requirement`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.fiftyone_requirement)
      * [`PluginDefinition.operators`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.operators)
      * [`PluginDefinition.skills`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.skills)
      * [`PluginDefinition.package_json_path`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.package_json_path)
      * [`PluginDefinition.has_package_json`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.has_package_json)
      * [`PluginDefinition.js_bundle`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.js_bundle)
      * [`PluginDefinition.js_bundle_path`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.js_bundle_path)
      * [`PluginDefinition.py_entry`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.py_entry)
      * [`PluginDefinition.py_entry_path`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.py_entry_path)
      * [`PluginDefinition.server_path`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.server_path)
      * [`PluginDefinition.js_bundle_server_path`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.js_bundle_server_path)
      * [`PluginDefinition.js_bundle_hash`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.js_bundle_hash)
      * [`PluginDefinition.can_register_operator()`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.can_register_operator)
      * [`PluginDefinition.has_py`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.has_py)
      * [`PluginDefinition.has_js`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.has_js)
      * [`PluginDefinition.secrets`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.secrets)
      * [`PluginDefinition.to_dict()`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.to_dict)
      * [`PluginDefinition.from_disk()`](api__fiftyone.plugins.definitions.md#fiftyone.plugins.definitions.PluginDefinition.from_disk)
  * [fiftyone.plugins.secrets](api__fiftyone.plugins.secrets.md)
    * [`PluginSecretsResolver`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.PluginSecretsResolver)
      * [`PluginSecretsResolver.register_operator()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.PluginSecretsResolver.register_operator)
      * [`PluginSecretsResolver.client()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.PluginSecretsResolver.client)
      * [`PluginSecretsResolver.get_multiple()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.PluginSecretsResolver.get_multiple)
      * [`PluginSecretsResolver.get_secret()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.PluginSecretsResolver.get_secret)
      * [`PluginSecretsResolver.get_secret_sync()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.PluginSecretsResolver.get_secret_sync)
    * [`SecretsDictionary`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.SecretsDictionary)
      * [`SecretsDictionary.copy()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.SecretsDictionary.copy)
      * [`SecretsDictionary.keys()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.SecretsDictionary.keys)
      * [`SecretsDictionary.values()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.SecretsDictionary.values)
      * [`SecretsDictionary.items()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.SecretsDictionary.items)
      * [`SecretsDictionary.get()`](api__fiftyone.plugins.secrets.md#fiftyone.plugins.secrets.SecretsDictionary.get)
  * [fiftyone.plugins.skills](api__fiftyone.plugins.skills.md)
    * [`SkillDefinition`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition)
      * [`SkillDefinition.name`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition.name)
      * [`SkillDefinition.description`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition.description)
      * [`SkillDefinition.category`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition.category)
      * [`SkillDefinition.path`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition.path)
      * [`SkillDefinition.plugin_name`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition.plugin_name)
      * [`SkillDefinition.content`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition.content)
      * [`SkillDefinition.to_dict()`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.SkillDefinition.to_dict)
    * [`list_skills()`](api__fiftyone.plugins.skills.md#fiftyone.plugins.skills.list_skills)
  * [fiftyone.plugins.utils](api__fiftyone.plugins.utils.md)
    * [`list_zoo_plugins()`](api__fiftyone.plugins.utils.md#fiftyone.plugins.utils.list_zoo_plugins)
    * [`find_plugins()`](api__fiftyone.plugins.utils.md#fiftyone.plugins.utils.find_plugins)
    * [`get_plugin_info()`](api__fiftyone.plugins.utils.md#fiftyone.plugins.utils.get_plugin_info)



## Module contents#

FiftyOne plugins.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`enable_plugin`(plugin_name[,Â _allow_missing]) | Enables the given plugin.  
---|---  
`disable_plugin`(plugin_name[,Â _allow_missing]) | Disables the given plugin.  
`delete_plugin`(plugin_name) | Deletes the given plugin from local disk.  
`list_plugins`([enabled,Â builtin,Â shadowed]) | Lists available plugins.  
`list_disabled_plugins`() | Returns a list of all disabled plugin names.  
`list_downloaded_plugins`() | Returns a list of all downloaded plugin names.  
`list_enabled_plugins`() | Returns a list of all enabled plugin names.  
`get_plugin`([name,Â plugin_dir]) | Gets the definition for the given plugin.  
`find_plugin`(name) | Returns the path to the plugin on local disk.  
`download_plugin`(url_or_gh_repo[,Â ...]) | Downloads the plugin(s) from the given location to your local plugins directory (`fo.config.plugins_dir`).  
`create_plugin`(plugin_name[,Â from_files,Â ...]) | Creates a plugin with the given name.  
`load_plugin_requirements`(plugin_name) | Loads the Python package requirements associated with the given plugin, if any.  
`install_plugin_requirements`(plugin_name[,Â ...]) | Installs any Python package requirements associated with the given plugin.  
`ensure_plugin_requirements`(plugin_name[,Â ...]) | Ensures that any Python package requirements associated with the given plugin are installed.  
`ensure_plugin_compatibility`(plugin_name[,Â ...]) | Ensures that the given plugin is compatible with your current FiftyOne package version.  
`list_skills`([enabled,Â plugin,Â category]) | Lists available skills from installed plugins.  
  
**Classes:**

`PluginDefinition`(directory,Â metadata[,Â ...]) | A plugin definition.  
---|---  
`PluginContext`(plugin_definition) | Context that represents a plugin and the Python objects it creates.  
`PluginSecretsResolver`() | Injects secrets from environmental variables into the execution context.  
  
fiftyone.plugins.enable_plugin(_plugin_name_ , __allow_missing =False_)#
    

Enables the given plugin.

Parameters:
    

**plugin_name** â the plugin name

fiftyone.plugins.disable_plugin(_plugin_name_ , __allow_missing =False_)#
    

Disables the given plugin.

Parameters:
    

**plugin_name** â the plugin name

fiftyone.plugins.delete_plugin(_plugin_name_)#
    

Deletes the given plugin from local disk.

Parameters:
    

**plugin_name** â the plugin name

fiftyone.plugins.list_plugins(_enabled =True_, _builtin =False_, _shadowed =False_)#
    

Lists available plugins.

Parameters:
    

  * **enabled** (_True_) â whether to include only enabled plugins (True) or only disabled plugins (False) or all plugins (âallâ)

  * **builtin** (_False_) â whether to include only builtin plugins (True) or only non-builtin plugins (False) or all plugins (âallâ)

  * **shadowed** (_False_) â whether to include only âshadowedâ duplicate plugins (True) or only usable plugins (False) or all plugins (âallâ)



Returns:
    

a list of `PluginDefinition` instances

fiftyone.plugins.list_disabled_plugins()#
    

Returns a list of all disabled plugin names.

Returns:
    

a list of plugin names

fiftyone.plugins.list_downloaded_plugins()#
    

Returns a list of all downloaded plugin names.

Returns:
    

a list of plugin names

fiftyone.plugins.list_enabled_plugins()#
    

Returns a list of all enabled plugin names.

Returns:
    

a list of plugin names

fiftyone.plugins.get_plugin(_name =None_, _plugin_dir =None_)#
    

Gets the definition for the given plugin.

Parameters:
    

  * **name** (_None_) â the plugin name

  * **plugin_dir** (_None_) â a directory containing the plugin



Returns:
    

a `PluginDefinition`

fiftyone.plugins.find_plugin(_name_)#
    

Returns the path to the plugin on local disk.

Parameters:
    

**name** â the plugin name

Returns:
    

the path to the plugin directory

fiftyone.plugins.download_plugin(_url_or_gh_repo_ , _plugin_names =None_, _overwrite =False_)#
    

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

fiftyone.plugins.create_plugin(_plugin_name_ , _from_files =None_, _outdir =None_, _description =None_, _tags =None_, _version =None_, _overwrite =False_, _** kwargs_)#
    

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

fiftyone.plugins.load_plugin_requirements(_plugin_name_)#
    

Loads the Python package requirements associated with the given plugin, if any.

Parameters:
    

**plugin_name** â the plugin name

Returns:
    

a list of requirement strings, or `None`

fiftyone.plugins.install_plugin_requirements(_plugin_name_ , _error_level =None_)#
    

Installs any Python package requirements associated with the given plugin.

Parameters:
    

  * **plugin_name** â the plugin name

  * **error_level** (_None_) â 

the error level to use, defined as:

    * 0: raise error if the install fails

    * 1: log warning if the install fails

    * 2: ignore install fails

By default, `fiftyone.config.requirement_error_level` is used




fiftyone.plugins.ensure_plugin_requirements(_plugin_name_ , _error_level =None_, _log_success =False_)#
    

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




fiftyone.plugins.ensure_plugin_compatibility(_plugin_name_ , _error_level =None_, _log_success =False_)#
    

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




class fiftyone.plugins.PluginDefinition(_directory_ , _metadata_ , _shadow_paths =None_)#
    

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

class fiftyone.plugins.PluginContext(_plugin_definition_)#
    

Bases: `object`

Context that represents a plugin and the Python objects it creates.

Parameters:
    

**plugin_definition** â the `fiftyone.plugins.PluginDefinition` for the plugin

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

class fiftyone.plugins.PluginSecretsResolver#
    

Bases: `object`

Injects secrets from environmental variables into the execution context.

**Methods:**

`register_operator`(operator_uri,Â required_secrets) |   
---|---  
`client`() |   
`get_multiple`(keys,Â operator_uri,Â **kwargs) | Get the value of multiple secrets.  
`get_secret`(key,Â operator_uri,Â **kwargs) | Get the value of a secret.  
`get_secret_sync`(key,Â operator_uri,Â **kwargs) | Get the value of a secret.  
  
register_operator(_operator_uri : str_, _required_secrets : List[str]_) → None#
    

client() → ISecretProvider#
    

async get_multiple(_keys : List[str]_, _operator_uri : str_, _** kwargs_) → Dict[str, ISecret | None]#
    

Get the value of multiple secrets. :param keys: list of secret keys :param operator_uri: the operator URI :param kwargs: additional keyword arguments to pass to the secrets :param client for authentication if required:

Returns:
    

A dictionary of secret keys and their values

async get_secret(_key : str_, _operator_uri : str_, _** kwargs_) → ISecret | None#
    

Get the value of a secret.

Parameters:
    

  * **key** (_str_) â unique secret identifier

  * **kwargs** â additional keyword arguments to pass to the secrets

  * **required** (_client for authentication if_)




get_secret_sync(_key : str_, _operator_uri : str_, _** kwargs_) → ISecret | None#
    

Get the value of a secret.

Parameters:
    

  * **key** (_str_) â unique secret identifier

  * **kwargs** â additional keyword arguments to pass to the secrets

  * **required** (_client for authentication if_)




fiftyone.plugins.list_skills(_enabled =True_, _plugin =None_, _category =None_)#
    

Lists available skills from installed plugins.

Parameters:
    

  * **enabled** (_True_) â whether to include only enabled plugins (True), only disabled plugins (False), or all plugins (`"all"`)

  * **plugin** (_None_) â a plugin name or list of plugin names to include. By default, skills from all plugins are included

  * **category** (_None_) â a category or list of categories to filter by. By default, skills of all categories are included



Returns:
    

a list of `SkillDefinition` instances

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
