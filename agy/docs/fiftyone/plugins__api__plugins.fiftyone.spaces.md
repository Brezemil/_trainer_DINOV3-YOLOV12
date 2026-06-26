---
source_url: https://docs.voxel51.com/plugins/api/plugins.fiftyone.spaces.html
---

# @fiftyone/spaces#

## Hooks#

### useInitializePanel#

@fiftyone/spaces.useInitializePanel()#
    

@fiftyone/spaces.initializePanel()#
    

Arguments:
    

  * **args** (`[ panelId , scope , state , data ]`)



Return type:
    

`Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### usePanel#

@fiftyone/spaces.usePanel(_name_ , _predicate_)#
    

Arguments:
    

  * **name** (`SpaceNodeType`)

  * **predicate** (`( panel : SpacePanelRegistration )`)



Return type:
    

`plugins.fiftyone.spaces.SpacePanelRegistration`

### usePanelAreaRenderer#

@fiftyone/spaces.usePanelAreaRenderer(_areaId_)#
    

Arguments:
    

  * **areaId** (`string`)



Return type:
    

`Object`

### usePanelCloseEffect#

@fiftyone/spaces.usePanelCloseEffect(_panelId_)#
    

Arguments:
    

  * **panelId** ()




### usePanelContext#

@fiftyone/spaces.usePanelContext()#
    

Return type:
    

`plugins.fiftyone.spaces.PanelContextType`

### usePanelId#

@fiftyone/spaces.usePanelId()#
    

Return type:
    

`string`

### usePanelLoading#

@fiftyone/spaces.usePanelLoading(_id_)#
    

Arguments:
    

  * **id** (`string`)



Return type:
    

`[` `boolean` `,` `( loading : boolean , id : string )` `]`

Get and set loading state of a panel

Note: `id` is optional if hook is used within the component of a panel.

### usePanelState#

@fiftyone/spaces.usePanelState(_defaultState_ , _id_ , _local_ , _scope_)#
    

Arguments:
    

  * **defaultState** (`T`)

  * **id** (`string`)

  * **local** (`boolean`)

  * **scope** (`string`)



Return type:
    

`Array<` `Union<` `plugins.fiftyone.spaces.T` `,` `SetterOrUpdater < T >` `>` `>`

Get and set state of a panel

Note: `id` is optional if hook is used within the component of a panel.

### usePanelStateByIdCallback#

@fiftyone/spaces.usePanelStateByIdCallback(_callback_ , _local_ , _scope_)#
    

Arguments:
    

  * **callback** (`( panelId : string , panelState : T , args : )`)

  * **local** (`boolean`)

  * **scope** (`string`)




Get a callback function that can be used to update the panel state.

**Returns**

A callback function that can be used to update the panel state. The callback is called with the panelId, panelState, and args.

Example:
    
    
    const resolvePanelState = (panelId, panelState, args) => {
      const [countInc] = args;
      // do something with the panelState
      const count = panelState.count + countInc;
      return { ...panelState, count };
    };
    const local = true; // true = local state, false = global state
    const setPanelState = usePanelStateByIdCallback(resolvePanelState, local, scope);
    const usePanelId = usePanelId();
    const countInc = 10;
    setPanelState("panelId", panelState, [countInc]);
    
          .. js:function:: panelStateByIdCallback
    
    
             :param args:
             :type args: [ panelId ,  ]
             :rtype: ``Promise < void >`` ``<`` ``void`` ``>``
    

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### usePanelStateCallback#

@fiftyone/spaces.usePanelStateCallback(_callback_ , _local_ , _scope_)#
    

Arguments:
    

  * **callback** (`( panelState : T )`)

  * **local** (`boolean`)

  * **scope** (`string`)




Can only be used within a panel component

> @fiftyone/spaces.panelStateCallback()#
>     
> 
> Arguments:
>     
> 
>   * **args** (`[ ]`)
> 
> 

> Return type:
>     
> 
> `Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### usePanelStateLazy#

@fiftyone/spaces.usePanelStateLazy(_local_ , _scope_)#
    

Arguments:
    

  * **local** (`boolean`)

  * **scope** (`string`)




Lazily read panel state on demand

**Returns**

a state resolver function which return promise that resolves to the current state of a panel

> @fiftyone/spaces.panelStateLazy()#
>     
> 
> Return type:
>     
> 
> `Promise < any >` `<` `any` `>`

### usePanelStatePartial#

@fiftyone/spaces.usePanelStatePartial(_key_ , _defaultState_ , _local_ , _scope_)#
    

Arguments:
    

  * **key** (`string`)

  * **defaultState** (`T`)

  * **local** (`boolean`)

  * **scope** (`string`)



Return type:
    

`Array<` `any` `>`

Get partial state of current panel (i.e. property of an object state)

Should only be used within a panel component whose state is an object or
    

an array

### usePanelTabAutoPosition#

@fiftyone/spaces.usePanelTabAutoPosition()#
    

@fiftyone/spaces.panelTabAutoPosition()#
    

Arguments:
    

  * **e** (`SortableEvent`)



Return type:
    

`Promise < void >` `<` `void` `>`

### usePanelTitle#

@fiftyone/spaces.usePanelTitle(_id_)#
    

Arguments:
    

  * **id** (`string`)



Return type:
    

`readonly`

Get and set title of a panel

Note: `id` is optional if hook is used within the component of a panel.

### usePanels#

@fiftyone/spaces.usePanels(_predicate_)#
    

Arguments:
    

  * **predicate** (`( panel : SpacePanelRegistration )`)



Return type:
    

`Array<` `plugins.fiftyone.spaces.SpacePanelRegistration` `>`

Hook to get all panels registered in the app, optionally filtered by a predicate.

### usePanelsState#

@fiftyone/spaces.usePanelsState(_local_)#
    

Arguments:
    

  * **local** (`boolean`)



Return type:
    

`[` `plugins.fiftyone.spaces.PanelsStateObject` `,` `( newPanelsState : PanelsStateObject )` `]`

Get and set multiple panels session or local state

### useReactivePanel#

@fiftyone/spaces.useReactivePanel(_name_)#
    

Arguments:
    

  * **name** (`SpaceNodeType`)



Return type:
    

`plugins.fiftyone.spaces.SpacePanelRegistration`

### useSetCustomPanelState#

@fiftyone/spaces.useSetCustomPanelState(_local_)#
    

Arguments:
    

  * **local** ()




### useSetPanelCloseEffect#

@fiftyone/spaces.useSetPanelCloseEffect(_panelId_)#
    

Arguments:
    

  * **panelId** ()




### useSetPanelStateById#

@fiftyone/spaces.useSetPanelStateById(_local_ , _scope_)#
    

Arguments:
    

  * **local** (`boolean`)

  * **scope** ()




Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useSpaceNodes#

@fiftyone/spaces.useSpaceNodes(_spaceId_)#
    

Arguments:
    

  * **spaceId** (`string`)



Return type:
    

`Array<` `plugins.fiftyone.spaces.default` `>`

### useSpaces#

@fiftyone/spaces.useSpaces(_id_ , _defaultState_)#
    

Arguments:
    

  * **id** (`string`)

  * **defaultState** (`SpaceNodeJSON`)



Return type:
    

`Object`

## Functions#

### PanelArea#

@fiftyone/spaces.PanelArea(_props_)#
    

Arguments:
    

  * **props** (`PanelAreaProps`)



Return type:
    

`Union<` `string` `,` `number` `,` `boolean` `,` `Element` `,` `ReactFragment` `>`

### PanelRenderer#

@fiftyone/spaces.PanelRenderer(_props_)#
    

Arguments:
    

  * **props** (`PanelRendererProps`)



Return type:
    

`Element`

### PanelSkeleton#

@fiftyone/spaces.PanelSkeleton()#
    

Return type:
    

`Element`

### SpacesRoot#

@fiftyone/spaces.SpacesRoot(_props_)#
    

Arguments:
    

  * **props** (`SpacesRootProps`)



Return type:
    

`Element`

### getNodes#

@fiftyone/spaces.getNodes(_node_)#
    

Arguments:
    

  * **node** (`default`)



Return type:
    

`Array<` `plugins.fiftyone.spaces.SpaceNode` `>`

### getPanelAreaRenderer#

@fiftyone/spaces.getPanelAreaRenderer(_areaId_)#
    

Arguments:
    

  * **areaId** (`string`)



Return type:
    

`ReactNode`

### registerPanelAreaRenderer#

@fiftyone/spaces.registerPanelAreaRenderer(_areaId_ , _renderer_)#
    

Arguments:
    

  * **areaId** (`string`)

  * **renderer** (`ReactNode`)



Return type:
    

`void`

### spaceNodeFromJSON#

@fiftyone/spaces.spaceNodeFromJSON(_json_ , _parent_)#
    

Arguments:
    

  * **json** (`SpaceNodeJSON`)

  * **parent** (`default`)



Return type:
    

`plugins.fiftyone.spaces.default`

### unregisterPanelAreaRenderer#

@fiftyone/spaces.unregisterPanelAreaRenderer(_areaId_)#
    

Arguments:
    

  * **areaId** (`string`)



Return type:
    

`void`

### warnPanelNotFound#

@fiftyone/spaces.warnPanelNotFound(_name_)#
    

Arguments:
    

  * **name** (`SpaceNodeType`)



Return type:
    

`any`

## Types#

class @fiftyone/spaces.AddPanelButtonProps()#
    

### AddPanelButtonProps#

Name | Type | Description  
---|---|---  
AddPanelButtonProps.node | `plugins.fiftyone.spaces.SpaceNode` |   
AddPanelButtonProps.spaceId | `string` |   
  
class @fiftyone/spaces.AddPanelItemProps()#
    

### AddPanelItemProps#

Name | Type | Description  
---|---|---  
AddPanelItemProps.Icon | `React.ComponentType` |   
AddPanelItemProps.label | `string` |   
AddPanelItemProps.name | `plugins.fiftyone.spaces.SpaceNodeType` |   
AddPanelItemProps.node | `plugins.fiftyone.spaces.SpaceNode` |   
AddPanelItemProps.onClick | `(` `)` |   
AddPanelItemProps.showAlpha | `boolean` |   
AddPanelItemProps.showBeta | `boolean` |   
AddPanelItemProps.showNew | `boolean` |   
AddPanelItemProps.spaceId | `string` |   
  
class @fiftyone/spaces.PanelAreaProps()#
    

### PanelAreaProps#

Name | Type | Description  
---|---|---  
PanelAreaProps.id | `plugins.fiftyone.spaces.PANEL_AREA` |   
PanelAreaProps.resize | `Object` |   
  
class @fiftyone/spaces.PanelIconProps()#
    

### PanelIconProps#

Name | Type | Description  
---|---|---  
PanelIconProps.name | `plugins.fiftyone.spaces.SpaceNodeType` |   
  
class @fiftyone/spaces.PanelIdToScopeType()#
    

### PanelIdToScopeType#

class @fiftyone/spaces.PanelProps()#
    

### PanelProps#

Name | Type | Description  
---|---|---  
PanelProps.isModalPanel | `boolean` |   
PanelProps.node | `plugins.fiftyone.spaces.SpaceNode` |   
PanelProps.style | `React.CSSProperties` |   
  
class @fiftyone/spaces.PanelRendererProps()#
    

### PanelRendererProps#

Name | Type | Description  
---|---|---  
PanelRendererProps.id | `string` |   
PanelRendererProps.name | `string` |   
  
class @fiftyone/spaces.PanelStateParameter()#
    

### PanelStateParameter#

Name | Type | Description  
---|---|---  
PanelStateParameter.local | `boolean` |   
PanelStateParameter.panelId | `string` |   
PanelStateParameter.scope | `string` |   
  
class @fiftyone/spaces.PanelStatePartialParameter()#
    

### PanelStatePartialParameter#

class @fiftyone/spaces.PanelTabProps()#
    

### PanelTabProps#

Name | Type | Description  
---|---|---  
PanelTabProps.active | `boolean` |   
PanelTabProps.node | `plugins.fiftyone.spaces.SpaceNode` |   
PanelTabProps.spaceId | `string` |   
  
class @fiftyone/spaces.PanelsCloseEffect()#
    

### PanelsCloseEffect#

class @fiftyone/spaces.PanelsStateObject()#
    

### PanelsStateObject#

class @fiftyone/spaces.SpaceNodeJSON()#
    

### SpaceNodeJSON#

Name | Type | Description  
---|---|---  
SpaceNodeJSON.activeChild |  |   
SpaceNodeJSON.children | `Array<` `plugins.fiftyone.spaces.SpaceNodeJSON` `>` |   
SpaceNodeJSON.id |  |   
SpaceNodeJSON.layout |  |   
SpaceNodeJSON.pinned |  |   
SpaceNodeJSON.sizes | `Array<` `number` `>` |   
SpaceNodeJSON.type |  |   
  
class @fiftyone/spaces.SpaceNodeType()#
    

### SpaceNodeType#

Union of `EnumType`, `string`

class @fiftyone/spaces.SpaceProps()#
    

### SpaceProps#

Name | Type | Description  
---|---|---  
SpaceProps.archetype | `Union<` `'grid'` `,` `'modal'` `>` |   
SpaceProps.id | `string` |   
SpaceProps.node | `plugins.fiftyone.spaces.SpaceNode` |   
  
class @fiftyone/spaces.SpacesRootProps()#
    

### SpacesRootProps#

Name | Type | Description  
---|---|---  
SpacesRootProps.defaultState | `plugins.fiftyone.spaces.SpaceNodeJSON` |   
SpacesRootProps.id | `string` |   
  
class @fiftyone/spaces.SplitPanelButtonProps()#
    

### SplitPanelButtonProps#

Name | Type | Description  
---|---|---  
SplitPanelButtonProps.layout | `plugins.fiftyone.spaces.Layout` |   
SplitPanelButtonProps.node | `plugins.fiftyone.spaces.SpaceNode` |   
SplitPanelButtonProps.spaceId | `string` |   
  
## Enums#

### Layout#

Name | Value  
---|---  
Horizontal |   
Vertical |   
  
### PANEL_AREA#

Name | Value  
---|---  
GRID_SIDEBAR_RIGHT |   
  
### SPACE_TYPES#

Name | Value  
---|---  
EMPTY |   
PANEL_CONTAINER |   
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
