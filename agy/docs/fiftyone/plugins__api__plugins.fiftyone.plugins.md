---
source_url: https://docs.voxel51.com/plugins/api/plugins.fiftyone.plugins.html
---

# @fiftyone/plugins#

## State#

### pluginsLoaderAtom#

Name | Type | Description  
---|---|---  
pluginsLoaderAtom | `Union<` `'loading'` `,` `'error'` `,` `'ready'` `>` |   
      
    
    const [pluginsLoaderAtom, setPluginsLoaderAtom] = useRecoilState(fos.pluginsLoaderAtom);
    

## Hooks#

### useActivePlugins#

@fiftyone/plugins.useActivePlugins(_type_ , _ctx_)#
    

Arguments:
    

  * **type** (`TType`)

  * **ctx** (`Record`)



Return type:
    

`Array<` `>`

### usePlugin#

@fiftyone/plugins.usePlugin(_type_)#
    

Arguments:
    

  * **type** (`TType`)



Return type:
    

`Array<` `>`

### usePluginComponent#

@fiftyone/plugins.usePluginComponent(_name_ , _ctx_)#
    

Arguments:
    

  * **name** (`string`)

  * **ctx** (`Record`)



Return type:
    

`plugins.fiftyone.plugins.ComponentRegistration` `<` `Any` `>`

Returns a component plugin by name if itâs available for the given `ctx`.

**Returns**

The plugin component or
    
    
    `undefined`
    

### usePluginDefinition#

@fiftyone/plugins.usePluginDefinition(_name_)#
    

Arguments:
    

  * **name** (`string`)



Return type:
    

`plugins.fiftyone.plugins.PluginDefinition`

Get a plugin definition by name.

**Returns**

The plugin definition

### usePluginSettings#

@fiftyone/plugins.usePluginSettings(_pluginName_ , _defaults_)#
    

Arguments:
    

  * **pluginName** (`string`)

  * **defaults** (`Partial`)



Return type:
    

`plugins.fiftyone.plugins.T`

### usePlugins#

@fiftyone/plugins.usePlugins()#
    

Return type:
    

`Object`

A react hook for loading the plugin system.

## Functions#

### createSampleRendererRenderContext#

@fiftyone/plugins.createSampleRendererRenderContext(_sample_ , _selectedMediaField_ , _dataset_ , _schema_ , _surface_)#
    

Arguments:
    

  * **sample** (`TSample`)

  * **selectedMediaField** (`string`)

  * **dataset** (`Dataset`)

  * **schema** (`Schema`)

  * **surface** (`SampleRendererSurface`)



Return type:
    

`plugins.fiftyone.plugins.SampleRendererRenderContext` `<` `plugins.fiftyone.plugins.TSample` `>`

Creates the full render context passed to sample renderer components.

### getAbsolutePluginPath#

@fiftyone/plugins.getAbsolutePluginPath(_name_ , _path_)#
    

Arguments:
    

  * **name** (`string`)

  * **path** (`string`)



Return type:
    

`string`

Get the absolute path to a file within a plugin directory.

**Returns**

An absolute path to the file

### getByType#

@fiftyone/plugins.getByType(_type_)#
    

Arguments:
    

  * **type** (`TType`)



Return type:
    

`Array<` `>`

Get a list of plugins match the given `type`.

**Returns**

A list of plugins

### getCategoryForPanel#

@fiftyone/plugins.getCategoryForPanel(_panel_)#
    

Arguments:
    

  * **panel** (`Union`)



Return type:
    

`plugins.fiftyone.plugins.CategoryID`

### getCategoryLabel#

@fiftyone/plugins.getCategoryLabel(_category_)#
    

Arguments:
    

  * **category** (`CategoryID`)



Return type:
    

`string`

### getComponent#

@fiftyone/plugins.getComponent(_name_)#
    

Arguments:
    

  * **name** (`string`)



Return type:
    

`FunctionComponent < T >` `<` `plugins.fiftyone.plugins.T` `>`

Returns the component registered under the given name.

### getMatchingSampleRenderer#

@fiftyone/plugins.getMatchingSampleRenderer(_registrations_ , _ctx_)#
    

Arguments:
    

  * **registrations** (`Array`)

  * **ctx** (`SampleRendererMatchContext`)



Return type:
    

`plugins.fiftyone.plugins.TRegistration`

Returns the highest-priority renderer registration that supports the given context.

### getPluginDefinition#

@fiftyone/plugins.getPluginDefinition(_name_)#
    

Arguments:
    

  * **name** (`string`)



Return type:
    

`plugins.fiftyone.plugins.PluginDefinition`

Get a plugin definition by name.

**Returns**

The plugin definition

### getSampleRendererComponent#

@fiftyone/plugins.getSampleRendererComponent(_registration_ , _surface_ , _canonicalComponent_)#
    

Arguments:
    

  * **registration** (`SampleRendererRegistrationLike`)

  * **surface** (`SampleRendererSurface`)

  * **canonicalComponent** (`FunctionComponent`)



Return type:
    

`FunctionComponent < SampleRendererProps >` `<` `plugins.fiftyone.plugins.SampleRendererProps` `>`

Selects the renderer component to use for the current surface.

### loadPlugins#

@fiftyone/plugins.loadPlugins()#
    

Return type:
    

`Promise < void >` `<` `void` `>`

### registerComponent#

@fiftyone/plugins.registerComponent(_registration_)#
    

Arguments:
    

  * **registration**



Return type:
    

`void`

Adds a plugin to the registry. This is called by the plugin itself.

### safePluginActivator#

@fiftyone/plugins.safePluginActivator(_plugin_ , _ctx_)#
    

Arguments:
    

  * **plugin** (`PluginComponentRegistration`)

  * **ctx** (`any`)



Return type:
    

`boolean`

a utility for safely calling plugin defined activator functions

### subscribeToRegistry#

@fiftyone/plugins.subscribeToRegistry(_handler_)#
    

Arguments:
    

  * **handler** (`RegistryEventHandler`)




Subscribe to plugin registryâs âsubscribeâ and âunsubscribeâ event.

**Returns**

A function to unsubscribe

> @fiftyone/plugins.subscribeToRegistry(_handler_)#
>     
> 
> Return type:
>     
> 
> `void`

### unregisterComponent#

@fiftyone/plugins.unregisterComponent(_name_)#
    

Arguments:
    

  * **name** (`string`)



Return type:
    

`void`

Remove a plugin from the registry.

### usingRegistry#

@fiftyone/plugins.usingRegistry()#
    

Return type:
    

`plugins.fiftyone.plugins.PluginComponentRegistry`

## Types#

### PluginComponentRegistrationByType#

class @fiftyone/plugins.PluginComponentRegistrationByType()#
    

#### Properties#

Name | Type | Description  
---|---|---  
1 | `plugins.fiftyone.plugins.PlotRegistration` `<` `Any` `>` |   
2 | `plugins.fiftyone.plugins.PanelRegistration` `<` `Any` `>` |   
3 | `plugins.fiftyone.plugins.ComponentRegistration` `<` `Any` `>` |   
4 | `plugins.fiftyone.plugins.SampleRendererRegistration` `<` `unknown` `>` |   
  
class @fiftyone/plugins.ComponentRegistration()#
    

### ComponentRegistration#

class @fiftyone/plugins.GridConfig()#
    

### GridConfig#

Grid-specific renderer behavior, including enablement and optional override.

Name | Type | Description  
---|---|---  
GridConfig.enabled | `boolean` |   
GridConfig.overrideComponent | `React.FunctionComponent < SampleRendererProps >` `<` `plugins.fiftyone.plugins.SampleRendererProps` `>` |   
  
class @fiftyone/plugins.MatchMedia()#
    

### MatchMedia#

Declarative media matchers used to determine renderer compatibility.

Name | Type | Description  
---|---|---  
MatchMedia.extensions | `Array<` `string` `>` |   
MatchMedia.mediaTypes | `Array<` `string` `>` |   
MatchMedia.mimeTypes | `Array<` `string` `>` |   
  
class @fiftyone/plugins.PanelOptions()#
    

### PanelOptions#

Defaults to `false`.â
    

âPanelOptions.alphaâ,â`boolean`â,âWhether the plugin is in alpha.

This is used to highlight alpha plugins.

Defaults to `false`.â
    

âPanelOptions.betaâ,â`boolean`â,âWhether the plugin is in beta.

This is used to highlight beta plugins.

Defaults to `false`.â
    

âPanelOptions.categoryâ,â`plugins.fiftyone.plugins.CategoryID`â,âThe category of the plugin.

Defaults to `custom`.â
    

âPanelOptions.helpMarkdownâ,â`string`â,âMarkdown help text for the plugin.â âPanelOptions.isNewâ,â`boolean`â,âWhether the plugin is new.

This is used to highlight new plugins.

Defaults to `false`.â
    

âPanelOptions.priorityâ,â`number`â,âPriority of the panel as it shows up in panel selector dropdown.

Panels are sorted by priority in ascending order.â
    

âPanelOptions.surfacesâ,â`Union<` `'grid'` `,` `'modal'` `,` `'portal'` `,` `'grid modal'` `,` `'grid portal'` `,` `'modal portal'` `,` `'grid modal portal'` `>`â,âSurfaces where plugin is made available.

If this is not provided, the plugin will be available in grid only.â

class @fiftyone/plugins.PanelRegistration()#
    

### PanelRegistration#

class @fiftyone/plugins.PlotRegistration()#
    

### PlotRegistration#

class @fiftyone/plugins.PluginActivator()#
    

### PluginActivator#

class @fiftyone/plugins.PluginComponentRegistration()#
    

### PluginComponentRegistration#

class @fiftyone/plugins.SampleRendererMatchContext()#
    

### SampleRendererMatchContext#

Context used to evaluate whether a sample renderer supports a sample.

Name | Type | Description  
---|---|---  
SampleRendererMatchContext.media | `plugins.fiftyone.plugins.SampleRendererMediaContext` |   
SampleRendererMatchContext.sample | `plugins.fiftyone.plugins.TSample` |   
SampleRendererMatchContext.surface | `plugins.fiftyone.plugins.SampleRendererSurface` |   
  
class @fiftyone/plugins.SampleRendererMediaContext()#
    

### SampleRendererMediaContext#

Normalized media attributes derived from a sample and selected media field.

Name | Type | Description  
---|---|---  
SampleRendererMediaContext.extension | `Union<` `string` `,` `null` `>` |   
SampleRendererMediaContext.field | `string` |   
SampleRendererMediaContext.isNative | `boolean` |   
SampleRendererMediaContext.mediaType | `Union<` `string` `,` `null` `>` |   
SampleRendererMediaContext.mimeType | `Union<` `string` `,` `null` `>` |   
SampleRendererMediaContext.path | `Union<` `string` `,` `null` `>` |   
SampleRendererMediaContext.url | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/plugins.SampleRendererOptions()#
    

### SampleRendererOptions#

Configuration for registering and selecting a sample renderer.

Name | Type | Description  
---|---|---  
SampleRendererOptions.grid | `plugins.fiftyone.plugins.GridConfig` |   
SampleRendererOptions.priority | `number` |   
SampleRendererOptions.supports | `Union<` `plugins.fiftyone.plugins.MatchMedia` `,` `( ctx : SampleRendererMatchContext )` `>` |   
  
class @fiftyone/plugins.SampleRendererProps()#
    

### SampleRendererProps#

Props shape received by sample renderer React components.

Name | Type | Description  
---|---|---  
SampleRendererProps.ctx | `plugins.fiftyone.plugins.SampleRendererRenderContext` `<` `plugins.fiftyone.plugins.SampleRendererSampleLike` `>` |   
  
class @fiftyone/plugins.SampleRendererRegistration()#
    

### SampleRendererRegistration#

Name | Type | Description  
---|---|---  
SampleRendererRegistration | `plugins.fiftyone.plugins.BaseSampleRendererRegistration` `<` `plugins.fiftyone.plugins.TSample` `>` |   
  
class @fiftyone/plugins.SampleRendererRenderContext()#
    

### SampleRendererRenderContext#

Full context passed to sample renderer components at render time.

class @fiftyone/plugins.SampleRendererSampleLike()#
    

### SampleRendererSampleLike#

Name | Type | Description  
---|---|---  
SampleRendererSampleLike.sample | `Object` |   
SampleRendererSampleLike.urls | `Union<` `Any` `,` `readonly` `>` |   
  
## Enums#

### Categories#

Name | Value  
---|---  
Analyze |   
Curate |   
Custom |   
Import |   
  
### PluginComponentType#

The type of plugin component.

  * `Panel` \- A panel that can be added to `@fiftyone/spaces`

  * `Plot` \- **deprecated** \- A plot that can be added as a panel

  * `SampleRenderer` \- A custom renderer for non-native sample media




Name | Value  
---|---  
Component |   
Panel |   
Plot |   
SampleRenderer |   
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
