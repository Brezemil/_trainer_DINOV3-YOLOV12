---
source_url: https://docs.voxel51.com/plugins/api/plugins.fiftyone.relay.html
---

# @fiftyone/relay#

## Hooks#

### useRelayEnvironment#

@fiftyone/relay.useRelayEnvironment()#
    

Return type:
    

`Environment`

## Functions#

### Writer#

@fiftyone/relay.Writer(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`WriterProps`)



Return type:
    

`Element`

A Recoil/Relay atomic syncing interface between a current page query and atom and atom families

### getPageQuery#

@fiftyone/relay.getPageQuery()#
    

Return type:
    

`Object`

### graphQLSyncFragmentAtom#

@fiftyone/relay.graphQLSyncFragmentAtom(_fragmentOptions_ , _options_)#
    

Arguments:
    

  * **fragmentOptions** (`GraphQLSyncFragmentSyncAtomOptions`)

  * **options** (`GraphQLSyncFragmentAtomOptions`)



Return type:
    

`RecoilState < K >` `<` `plugins.fiftyone.relay.K` `>`

Creates a recoil atom synced with a relay fragment via its path in a query. If the fragment path cannot be read from given the parent fragment keys and the optional final read function, the atomâs default value will be used

### graphQLSyncFragmentAtomFamily#

@fiftyone/relay.graphQLSyncFragmentAtomFamily(_fragmentOptions_ , _options_)#
    

Arguments:
    

  * **fragmentOptions** (`GraphQLSyncFragmentSyncAtomFamilyOptions`)

  * **options** (`GraphQLSyncFragmentAtomFamilyOptions`)




Creates a recoil atom family synced with a relay fragment via its path in a query. If the fragment path cannot be read from given the parent fragment keys. Includes the optional `sync` parameter to conditionally opt-in to fragment syncing given an atom instanceâs parameters `P`.

> @fiftyone/relay.graphQLSyncFragmentAtomFamily(_fragmentOptions_ , _options_)#
>     
> 
> Arguments:
>     
> 
>   * **params** (`P`)
> 
> 

> Return type:
>     
> 
> `RecoilState < K >` `<` `plugins.fiftyone.relay.K` `>`

### isPaginateSamplesConnection#

@fiftyone/relay.isPaginateSamplesConnection(_samples_)#
    

Arguments:
    

  * **samples** (`Union`)



Return type:
    

Type guard for `PaginateSamplesConnection`. Returns `true` when `samples` is the successful connection variant and `edges` / `pageInfo` are safe to access.

### readFragment#

@fiftyone/relay.readFragment(_fragmentInput_ , _fragmentRef_)#
    

Arguments:
    

  * **fragmentInput** (`GraphQLTaggedNode`)

  * **fragmentRef** (`TKey`)



Return type:
    

`KeyTypeData < TKey >` `<` `plugins.fiftyone.relay.TKey` `>`

### resetEffect#

@fiftyone/relay.resetEffect(_viewChange_)#
    

Arguments:
    

  * **viewChange** (`boolean`)



Return type:
    

`AtomEffect < T >` `<` `plugins.fiftyone.relay.T` `>`

Effect for restting an atomâs value when the view or dataset changes. Can be limited to only dataset changes when viewChange is false

### selectorWithEffect#

@fiftyone/relay.selectorWithEffect(___namedParameters_ , _itemKey_)#
    

Arguments:
    

  * **__namedParameters**

  * **itemKey** (`string`)



Return type:
    

`RecoilState < T >` `<` `plugins.fiftyone.relay.T` `>`

Wraps a Recoil selector so writes can be routed through the setter registry provided by `SelectorEffectContext`.

This is useful when a piece of state is primarily derived from another atom or selector, but writes must still flow through an external sync layer such as the Relay writer/session bridge. The returned selector:

  * reads exactly like a normal selector via `options.get`

  * looks up a matching setter from the effect store using `itemKey` or `options.key`

  * optionally transforms the write payload via `options.set`

  * optionally mirrors the final value into `state` for local Recoil updates




### subscribe#

@fiftyone/relay.subscribe(_subscription_)#
    

Arguments:
    

  * **subscription** ()




### subscribeBefore#

@fiftyone/relay.subscribeBefore(_subscription_)#
    

Arguments:
    

  * **subscription** ()




## Types#

### PageQuery#

class @fiftyone/relay.PageQuery()#
    

#### Properties#

Name | Type | Description  
---|---|---  
concreteRequest | `ConcreteRequest` |   
data |  |   
event | `Union<` `'fieldVisibility'` `,` `'modal'` `>` |   
preloadedQuery | `PreloadedQuery < T , Record >` `<` `plugins.fiftyone.relay.T` `,` `Record < string , unknown >` `>` |   
  
class @fiftyone/relay.Aggregate()#
    

### Aggregate#

Name | Type | Description  
---|---|---  
Aggregate.count | `Union<` `plugins.fiftyone.relay.Count` `,` `null` `>` |   
Aggregate.countValues | `Union<` `plugins.fiftyone.relay.CountValues` `,` `null` `>` |   
Aggregate.histogramValues | `Union<` `plugins.fiftyone.relay.HistogramValues` `,` `null` `>` |   
  
class @fiftyone/relay.AggregationForm()#
    

### AggregationForm#

Name | Type | Description  
---|---|---  
AggregationForm.dataset | `string` |   
AggregationForm.dynamicGroup | `Union<` `object` `,` `null` `>` |   
AggregationForm.extendedStages | `Array<` `any` `>` |   
AggregationForm.filters | `Union<` `object` `,` `null` `>` |   
AggregationForm.groupId | `Union<` `string` `,` `null` `>` |   
AggregationForm.hiddenLabels | `ReadonlyArray < SelectedLabel >` `<` `plugins.fiftyone.relay.SelectedLabel` `>` |   
AggregationForm.hint | `Union<` `string` `,` `null` `>` |   
AggregationForm.index | `Union<` `number` `,` `null` `>` |   
AggregationForm.maxQueryTime | `Union<` `number` `,` `null` `>` |   
AggregationForm.mixed | `boolean` |   
AggregationForm.paths | `ReadonlyArray < string >` `<` `string` `>` |   
AggregationForm.queryPerformance | `Union<` `boolean` `,` `null` `>` |   
AggregationForm.sampleIds | `ReadonlyArray < string >` `<` `string` `>` |   
AggregationForm.slice | `Union<` `string` `,` `null` `>` |   
AggregationForm.slices | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
AggregationForm.view | `Array<` `any` `>` |   
AggregationForm.viewName | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.BrainRunType()#
    

### BrainRunType#

Union of `'similarity'`, `'visualization'`, `'%future added value'`

class @fiftyone/relay.ColorBy()#
    

### ColorBy#

Union of `'field'`, `'instance'`, `'value'`, `'%future added value'`

class @fiftyone/relay.ColorSchemeInput()#
    

### ColorSchemeInput#

Name | Type | Description  
---|---|---  
ColorSchemeInput.colorBy | `Union<` `string` `,` `null` `>` |   
ColorSchemeInput.colorPool | `ReadonlyArray < string >` `<` `string` `>` |   
ColorSchemeInput.colorscales | `Union<` `ReadonlyArray < ColorscaleInput >` `,` `null` `>` |   
ColorSchemeInput.defaultColorscale | `Union<` `plugins.fiftyone.relay.DefaultColorscaleInput` `,` `null` `>` |   
ColorSchemeInput.defaultMaskTargetsColors | `Union<` `ReadonlyArray < MaskColorInput >` `,` `null` `>` |   
ColorSchemeInput.fields | `Union<` `ReadonlyArray < CustomizeColorInput >` `,` `null` `>` |   
ColorSchemeInput.id | `Union<` `string` `,` `null` `>` |   
ColorSchemeInput.labelTags | `Union<` `plugins.fiftyone.relay.LabelTagColorInput` `,` `null` `>` |   
ColorSchemeInput.multicolorKeypoints | `Union<` `boolean` `,` `null` `>` |   
ColorSchemeInput.opacity | `Union<` `number` `,` `null` `>` |   
ColorSchemeInput.showSkeletons | `Union<` `boolean` `,` `null` `>` |   
  
class @fiftyone/relay.ColorscaleInput()#
    

### ColorscaleInput#

Name | Type | Description  
---|---|---  
ColorscaleInput.list | `Union<` `ReadonlyArray < ColorscaleListInput >` `,` `null` `>` |   
ColorscaleInput.name | `Union<` `string` `,` `null` `>` |   
ColorscaleInput.path | `string` |   
  
class @fiftyone/relay.ColorscaleListInput()#
    

### ColorscaleListInput#

Name | Type | Description  
---|---|---  
ColorscaleListInput.color | `string` |   
ColorscaleListInput.value | `Union<` `number` `,` `null` `>` |   
  
class @fiftyone/relay.Count()#
    

### Count#

Name | Type | Description  
---|---|---  
Count.field | `string` |   
  
class @fiftyone/relay.CountValues()#
    

### CountValues#

Name | Type | Description  
---|---|---  
CountValues.field | `string` |   
  
class @fiftyone/relay.CustomizeColorInput()#
    

### CustomizeColorInput#

Name | Type | Description  
---|---|---  
CustomizeColorInput.colorByAttribute | `Union<` `string` `,` `null` `>` |   
CustomizeColorInput.fieldColor | `Union<` `string` `,` `null` `>` |   
CustomizeColorInput.maskTargetsColors | `Union<` `ReadonlyArray < MaskColorInput >` `,` `null` `>` |   
CustomizeColorInput.path | `string` |   
CustomizeColorInput.valueColors | `Union<` `ReadonlyArray < ValueColorInput >` `,` `null` `>` |   
  
class @fiftyone/relay.DefaultColorscaleInput()#
    

### DefaultColorscaleInput#

Name | Type | Description  
---|---|---  
DefaultColorscaleInput.list | `Union<` `ReadonlyArray < ColorscaleListInput >` `,` `null` `>` |   
DefaultColorscaleInput.name | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.ExtendedViewForm()#
    

### ExtendedViewForm#

Name | Type | Description  
---|---|---  
ExtendedViewForm.filters | `Union<` `object` `,` `null` `>` |   
ExtendedViewForm.mixed | `Union<` `boolean` `,` `null` `>` |   
ExtendedViewForm.sampleIds | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
ExtendedViewForm.slice | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.GraphQLSyncFragmentAtomFamilyOptions()#
    

### GraphQLSyncFragmentAtomFamilyOptions#

Name | Type | Description  
---|---|---  
GraphQLSyncFragmentAtomFamilyOptions | `Omit < AtomFamilyOptions , >` `<` `AtomFamilyOptions < K , P >` `,` `'default'` `>` |   
  
class @fiftyone/relay.GraphQLSyncFragmentAtomOptions()#
    

### GraphQLSyncFragmentAtomOptions#

Name | Type | Description  
---|---|---  
GraphQLSyncFragmentAtomOptions | `Omit < AtomOptions , >` `<` `AtomOptions < K >` `,` `'default'` `>` |   
  
class @fiftyone/relay.GraphQLSyncFragmentSyncAtomFamilyOptions()#
    

### GraphQLSyncFragmentSyncAtomFamilyOptions#

Name | Type | Description  
---|---|---  
GraphQLSyncFragmentSyncAtomFamilyOptions.default | `plugins.fiftyone.relay.K` |   
GraphQLSyncFragmentSyncAtomFamilyOptions.fragments | `Array<` `GraphQLTaggedNode` `>` |   
GraphQLSyncFragmentSyncAtomFamilyOptions.keys | `Array<` `string` `>` |   
GraphQLSyncFragmentSyncAtomFamilyOptions.read | `(` `data` `:` `KeyTypeData < T >` `, `` ``previous` `:` `Union< KeyTypeData , >` `, `` ``params` `:` `plugins.fiftyone.relay.P` `)` |   
GraphQLSyncFragmentSyncAtomFamilyOptions.sync | `(` `params` `:` `plugins.fiftyone.relay.P` `)` |   
  
class @fiftyone/relay.GraphQLSyncFragmentSyncAtomOptions()#
    

### GraphQLSyncFragmentSyncAtomOptions#

Name | Type | Description  
---|---|---  
GraphQLSyncFragmentSyncAtomOptions.default | `plugins.fiftyone.relay.K` |   
GraphQLSyncFragmentSyncAtomOptions.fragments | `Array<` `GraphQLTaggedNode` `>` |   
GraphQLSyncFragmentSyncAtomOptions.keys | `Array<` `string` `>` |   
GraphQLSyncFragmentSyncAtomOptions.read | `(` `data` `:` `KeyTypeData < T >` `, `` ``previous` `:` `Union< KeyTypeData , >` `)` |   
GraphQLSyncFragmentSyncAtomOptions.selectorEffect | `Union<` `'write'` `,` `boolean` `,` `( params : Parameters )` `>` |   
  
class @fiftyone/relay.GroupElementFilter()#
    

### GroupElementFilter#

Name | Type | Description  
---|---|---  
GroupElementFilter.id | `Union<` `string` `,` `null` `>` |   
GroupElementFilter.slice | `Union<` `string` `,` `null` `>` |   
GroupElementFilter.slices | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
  
class @fiftyone/relay.HistogramValues()#
    

### HistogramValues#

Name | Type | Description  
---|---|---  
HistogramValues.field | `string` |   
  
class @fiftyone/relay.IndexType()#
    

### IndexType#

Union of `'asc'`, `'desc'`, `'%future added value'`

class @fiftyone/relay.LabelTagColorInput()#
    

### LabelTagColorInput#

Name | Type | Description  
---|---|---  
LabelTagColorInput.fieldColor | `Union<` `string` `,` `null` `>` |   
LabelTagColorInput.valueColors | `Union<` `ReadonlyArray < ValueColorInput >` `,` `null` `>` |   
  
class @fiftyone/relay.LightningInput()#
    

### LightningInput#

Name | Type | Description  
---|---|---  
LightningInput.dataset | `string` |   
LightningInput.match | `Union<` `object` `,` `null` `>` |   
LightningInput.paths | `ReadonlyArray < LightningPathInput >` `<` `plugins.fiftyone.relay.LightningPathInput` `>` |   
LightningInput.slice | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.LightningPathInput()#
    

### LightningPathInput#

Name | Type | Description  
---|---|---  
LightningPathInput.exclude | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
LightningPathInput.filters | `Union<` `object` `,` `null` `>` |   
LightningPathInput.first | `Union<` `number` `,` `null` `>` |   
LightningPathInput.index | `Union<` `string` `,` `null` `>` |   
LightningPathInput.maxDocumentsSearch | `Union<` `number` `,` `null` `>` |   
LightningPathInput.path | `string` |   
LightningPathInput.search | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.MaskColorInput()#
    

### MaskColorInput#

Name | Type | Description  
---|---|---  
MaskColorInput.color | `string` |   
MaskColorInput.intTarget | `number` |   
  
class @fiftyone/relay.PageSubscription()#
    

### PageSubscription#

class @fiftyone/relay.PaginateSamplesConnection()#
    

### PaginateSamplesConnection#

The successful `SampleItemStrConnection` branch of `samples`, with the `QueryTimeout` and `%other` union members removed. Use this when narrowing `paginateSamplesQuery` results before accessing `edges` / `pageInfo`.

Name | Type | Description  
---|---|---  
PaginateSamplesConnection | `Exclude < Exclude , >` `<` `Exclude < , >` `,` `Object` `>` |   
  
class @fiftyone/relay.PaginateSamplesNode()#
    

### PaginateSamplesNode#

A concrete sample node from `paginateSamplesQuery`, with the `QueryTimeout`, `%other` connection variants and the `%other` node variant all narrowed away. Consumers can treat the result as one of the known sample types (`ImageSample`, `PointCloudSample`, etc.).

Name | Type | Description  
---|---|---  
PaginateSamplesNode | `Exclude < , >` `<` ```` `,` `Object` `>` |   
  
class @fiftyone/relay.SampleFilter()#
    

### SampleFilter#

Name | Type | Description  
---|---|---  
SampleFilter.group | `Union<` `plugins.fiftyone.relay.GroupElementFilter` `,` `null` `>` |   
SampleFilter.id | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.SavedViewInfo()#
    

### SavedViewInfo#

Name | Type | Description  
---|---|---  
SavedViewInfo.color | `Union<` `string` `,` `null` `>` |   
SavedViewInfo.description | `Union<` `string` `,` `null` `>` |   
SavedViewInfo.name | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.SelectedLabel()#
    

### SelectedLabel#

Name | Type | Description  
---|---|---  
SelectedLabel.field | `string` |   
SelectedLabel.frameNumber | `Union<` `number` `,` `null` `>` |   
SelectedLabel.instanceId | `Union<` `string` `,` `null` `>` |   
SelectedLabel.labelId | `string` |   
SelectedLabel.sampleId | `string` |   
SelectedLabel.type | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.Setter()#
    

### Setter#

class @fiftyone/relay.SidebarGroupInput()#
    

### SidebarGroupInput#

Name | Type | Description  
---|---|---  
SidebarGroupInput.expanded | `Union<` `boolean` `,` `null` `>` |   
SidebarGroupInput.name | `string` |   
SidebarGroupInput.paths | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
  
class @fiftyone/relay.SidebarMode()#
    

### SidebarMode#

Union of `'all'`, `'best'`, `'fast'`, `'%future added value'`

class @fiftyone/relay.StateForm()#
    

### StateForm#

Name | Type | Description  
---|---|---  
StateForm.addStages | `Union<` `Array< any >` `,` `null` `>` |   
StateForm.extended | `Union<` `object` `,` `null` `>` |   
StateForm.filters | `Union<` `object` `,` `null` `>` |   
StateForm.labels | `Union<` `ReadonlyArray < SelectedLabel >` `,` `null` `>` |   
StateForm.sampleIds | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
StateForm.slice | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.Theme()#
    

### Theme#

Union of `'browser'`, `'dark'`, `'light'`, `'%future added value'`

class @fiftyone/relay.ValueColorInput()#
    

### ValueColorInput#

Name | Type | Description  
---|---|---  
ValueColorInput.color | `string` |   
ValueColorInput.value | `string` |   
  
class @fiftyone/relay.aggregateQuery()#
    

### aggregateQuery#

Name | Type | Description  
---|---|---  
aggregateQuery.response | `plugins.fiftyone.relay.aggregateQuery$data` |   
aggregateQuery.variables | `plugins.fiftyone.relay.aggregateQuery$variables` |   
  
class @fiftyone/relay.aggregateQuery$data()#
    

### aggregateQuery$data#

Name | Type | Description  
---|---|---  
aggregateQuery$data.aggregate | `ReadonlyArray < >` `<` `Union< , >` `>` |   
  
class @fiftyone/relay.aggregateQuery$variables()#
    

### aggregateQuery$variables#

Name | Type | Description  
---|---|---  
aggregateQuery$variables.aggregations | `ReadonlyArray < Aggregate >` `<` `plugins.fiftyone.relay.Aggregate` `>` |   
aggregateQuery$variables.dataset | `string` |   
aggregateQuery$variables.view | `Array<` `any` `>` |   
  
class @fiftyone/relay.aggregationsQuery()#
    

### aggregationsQuery#

Name | Type | Description  
---|---|---  
aggregationsQuery.response | `plugins.fiftyone.relay.aggregationsQuery$data` |   
aggregationsQuery.variables | `plugins.fiftyone.relay.aggregationsQuery$variables` |   
  
class @fiftyone/relay.aggregationsQuery$data()#
    

### aggregationsQuery$data#

Name | Type | Description  
---|---|---  
aggregationsQuery$data.aggregations | `ReadonlyArray < >` `<` `Union< , , , , , , , >` `>` |   
  
class @fiftyone/relay.aggregationsQuery$variables()#
    

### aggregationsQuery$variables#

Name | Type | Description  
---|---|---  
aggregationsQuery$variables.form | `plugins.fiftyone.relay.AggregationForm` |   
  
class @fiftyone/relay.colorSchemeFragment$data()#
    

### colorSchemeFragment$data#

Name | Type | Description  
---|---|---  
colorSchemeFragment$data. $fragmentType | `'colorSchemeFragment'` |   
colorSchemeFragment$data.colorBy | `Union<` `plugins.fiftyone.relay.ColorBy` `,` `null` `>` |   
colorSchemeFragment$data.colorPool | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
colorSchemeFragment$data.colorscales | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
colorSchemeFragment$data.defaultColorscale | `Union<` `Object` `,` `null` `>` |   
colorSchemeFragment$data.defaultMaskTargetsColors | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
colorSchemeFragment$data.fields | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
colorSchemeFragment$data.id | `string` |   
colorSchemeFragment$data.labelTags | `Union<` `Object` `,` `null` `>` |   
colorSchemeFragment$data.multicolorKeypoints | `Union<` `boolean` `,` `null` `>` |   
colorSchemeFragment$data.opacity | `Union<` `number` `,` `null` `>` |   
colorSchemeFragment$data.showSkeletons | `Union<` `boolean` `,` `null` `>` |   
  
class @fiftyone/relay.colorSchemeFragment$key()#
    

### colorSchemeFragment$key#

Name | Type | Description  
---|---|---  
colorSchemeFragment$key. $data | `plugins.fiftyone.relay.colorSchemeFragment$data` |   
colorSchemeFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'colorSchemeFragment'` `>` |   
  
class @fiftyone/relay.configFragment$data()#
    

### configFragment$data#

Name | Type | Description  
---|---|---  
configFragment$data. $fragmentType | `'configFragment'` |   
configFragment$data.colorscale | `Union<` `ReadonlyArray < ReadonlyArray >` `,` `null` `>` |   
configFragment$data.config | `Object` |   
  
class @fiftyone/relay.configFragment$key()#
    

### configFragment$key#

Name | Type | Description  
---|---|---  
configFragment$key. $data | `plugins.fiftyone.relay.configFragment$data` |   
configFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'configFragment'` `>` |   
  
class @fiftyone/relay.configQuery()#
    

### configQuery#

Name | Type | Description  
---|---|---  
configQuery.response | `plugins.fiftyone.relay.configQuery$data` |   
configQuery.variables | `plugins.fiftyone.relay.configQuery$variables` |   
  
class @fiftyone/relay.configQuery$data()#
    

### configQuery$data#

Name | Type | Description  
---|---|---  
configQuery$data.colorscale | `Union<` `ReadonlyArray < ReadonlyArray >` `,` `null` `>` |   
configQuery$data.config | `Object` |   
  
class @fiftyone/relay.configQuery$variables()#
    

### configQuery$variables#

class @fiftyone/relay.countValuesQuery()#
    

### countValuesQuery#

Name | Type | Description  
---|---|---  
countValuesQuery.response | `plugins.fiftyone.relay.countValuesQuery$data` |   
countValuesQuery.variables | `plugins.fiftyone.relay.countValuesQuery$variables` |   
  
class @fiftyone/relay.countValuesQuery$data()#
    

### countValuesQuery$data#

Name | Type | Description  
---|---|---  
countValuesQuery$data.aggregate | `ReadonlyArray < >` `<` `Union< , , >` `>` |   
  
class @fiftyone/relay.countValuesQuery$variables()#
    

### countValuesQuery$variables#

Name | Type | Description  
---|---|---  
countValuesQuery$variables.dataset | `string` |   
countValuesQuery$variables.form | `Union<` `plugins.fiftyone.relay.ExtendedViewForm` `,` `null` `>` |   
countValuesQuery$variables.path | `string` |   
countValuesQuery$variables.view | `Array<` `any` `>` |   
  
class @fiftyone/relay.createSavedViewMutation()#
    

### createSavedViewMutation#

Name | Type | Description  
---|---|---  
createSavedViewMutation.response | `plugins.fiftyone.relay.createSavedViewMutation$data` |   
createSavedViewMutation.variables | `plugins.fiftyone.relay.createSavedViewMutation$variables` |   
  
class @fiftyone/relay.createSavedViewMutation$data()#
    

### createSavedViewMutation$data#

Name | Type | Description  
---|---|---  
createSavedViewMutation$data.createSavedView | `Union<` `Object` `,` `null` `>` |   
  
class @fiftyone/relay.createSavedViewMutation$variables()#
    

### createSavedViewMutation$variables#

Name | Type | Description  
---|---|---  
createSavedViewMutation$variables.color | `Union<` `string` `,` `null` `>` |   
createSavedViewMutation$variables.datasetName | `Union<` `string` `,` `null` `>` |   
createSavedViewMutation$variables.description | `Union<` `string` `,` `null` `>` |   
createSavedViewMutation$variables.form | `Union<` `plugins.fiftyone.relay.StateForm` `,` `null` `>` |   
createSavedViewMutation$variables.session | `Union<` `string` `,` `null` `>` |   
createSavedViewMutation$variables.subscription | `string` |   
createSavedViewMutation$variables.viewName | `string` |   
createSavedViewMutation$variables.viewStages | `Union<` `Array< any >` `,` `null` `>` |   
  
class @fiftyone/relay.datasetAppConfigFragment$data()#
    

### datasetAppConfigFragment$data#

Name | Type | Description  
---|---|---  
datasetAppConfigFragment$data. $fragmentType | `'datasetAppConfigFragment'` |   
datasetAppConfigFragment$data.activeFields | `Union<` `Object` `,` `null` `>` |   
datasetAppConfigFragment$data.colorScheme | `Union<` `Object` `,` `null` `>` |   
datasetAppConfigFragment$data.disableFrameFiltering | `Union<` `boolean` `,` `null` `>` |   
datasetAppConfigFragment$data.dynamicGroupsTargetFrameRate | `number` |   
datasetAppConfigFragment$data.gridMediaField | `string` |   
datasetAppConfigFragment$data.mediaFallback | `boolean` |   
datasetAppConfigFragment$data.mediaFields | `Union<` `ReadonlyArray < string >` `,` `null` `>` |   
datasetAppConfigFragment$data.modalMediaField | `string` |   
datasetAppConfigFragment$data.plugins | `Union<` `object` `,` `null` `>` |   
  
class @fiftyone/relay.datasetAppConfigFragment$key()#
    

### datasetAppConfigFragment$key#

Name | Type | Description  
---|---|---  
datasetAppConfigFragment$key. $data | `plugins.fiftyone.relay.datasetAppConfigFragment$data` |   
datasetAppConfigFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'datasetAppConfigFragment'` `>` |   
  
class @fiftyone/relay.datasetFragment$data()#
    

### datasetFragment$data#

Name | Type | Description  
---|---|---  
datasetFragment$data. $fragmentSpreads | `FragmentRefs < >` `<` `Union< , , , , , , , , >` `>` |   
datasetFragment$data. $fragmentType | `'datasetFragment'` |   
datasetFragment$data.appConfig | `Union<` `Object` `,` `null` `>` |   
datasetFragment$data.brainMethods | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
datasetFragment$data.createdAt | `Union<` `number` `,` `null` `>` |   
datasetFragment$data.datasetId | `string` |   
datasetFragment$data.defaultMaskTargets | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
datasetFragment$data.defaultSkeleton | `Union<` `Object` `,` `null` `>` |   
datasetFragment$data.evaluations | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
datasetFragment$data.groupField | `Union<` `string` `,` `null` `>` |   
datasetFragment$data.groupMediaTypes | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
datasetFragment$data.id | `string` |   
datasetFragment$data.info | `Union<` `object` `,` `null` `>` |   
datasetFragment$data.lastLoadedAt | `Union<` `number` `,` `null` `>` |   
datasetFragment$data.maskTargets | `ReadonlyArray < >` `<` `Object` `>` |   
datasetFragment$data.mediaType | `Union<` `string` `,` `null` `>` |   
datasetFragment$data.name | `string` |   
datasetFragment$data.parentMediaType | `Union<` `string` `,` `null` `>` |   
datasetFragment$data.skeletons | `ReadonlyArray < >` `<` `Object` `>` |   
datasetFragment$data.version | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.datasetFragment$key()#
    

### datasetFragment$key#

Name | Type | Description  
---|---|---  
datasetFragment$key. $data | `plugins.fiftyone.relay.datasetFragment$data` |   
datasetFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'datasetFragment'` `>` |   
  
class @fiftyone/relay.datasetQuery()#
    

### datasetQuery#

Name | Type | Description  
---|---|---  
datasetQuery.response | `plugins.fiftyone.relay.datasetQuery$data` |   
datasetQuery.variables | `plugins.fiftyone.relay.datasetQuery$variables` |   
  
class @fiftyone/relay.datasetQuery$data()#
    

### datasetQuery$data#

Name | Type | Description  
---|---|---  
datasetQuery$data. $fragmentSpreads | `FragmentRefs < >` `<` `Union< , , , >` `>` |   
datasetQuery$data.config | `Object` |   
datasetQuery$data.dataset | `Union<` `Object` `,` `null` `>` |   
  
class @fiftyone/relay.datasetQuery$variables()#
    

### datasetQuery$variables#

Name | Type | Description  
---|---|---  
datasetQuery$variables.extendedView | `Array<` `any` `>` |   
datasetQuery$variables.name | `string` |   
datasetQuery$variables.savedViewSlug | `Union<` `string` `,` `null` `>` |   
datasetQuery$variables.view | `Array<` `any` `>` |   
datasetQuery$variables.workspaceSlug | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.deleteSavedViewMutation()#
    

### deleteSavedViewMutation#

Name | Type | Description  
---|---|---  
deleteSavedViewMutation.response | `plugins.fiftyone.relay.deleteSavedViewMutation$data` |   
deleteSavedViewMutation.variables | `plugins.fiftyone.relay.deleteSavedViewMutation$variables` |   
  
class @fiftyone/relay.deleteSavedViewMutation$data()#
    

### deleteSavedViewMutation$data#

Name | Type | Description  
---|---|---  
deleteSavedViewMutation$data.deleteSavedView | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.deleteSavedViewMutation$variables()#
    

### deleteSavedViewMutation$variables#

Name | Type | Description  
---|---|---  
deleteSavedViewMutation$variables.datasetName | `Union<` `string` `,` `null` `>` |   
deleteSavedViewMutation$variables.session | `Union<` `string` `,` `null` `>` |   
deleteSavedViewMutation$variables.subscription | `string` |   
deleteSavedViewMutation$variables.viewName | `string` |   
  
class @fiftyone/relay.estimatedCountsFragment$data()#
    

### estimatedCountsFragment$data#

Name | Type | Description  
---|---|---  
estimatedCountsFragment$data. $fragmentType | `'estimatedCountsFragment'` |   
estimatedCountsFragment$data.estimatedFrameCount | `Union<` `number` `,` `null` `>` |   
estimatedCountsFragment$data.estimatedSampleCount | `number` |   
  
class @fiftyone/relay.estimatedCountsFragment$key()#
    

### estimatedCountsFragment$key#

Name | Type | Description  
---|---|---  
estimatedCountsFragment$key. $data | `plugins.fiftyone.relay.estimatedCountsFragment$data` |   
estimatedCountsFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'estimatedCountsFragment'` `>` |   
  
class @fiftyone/relay.frameFieldsFragment$data()#
    

### frameFieldsFragment$data#

Name | Type | Description  
---|---|---  
frameFieldsFragment$data. $fragmentType | `'frameFieldsFragment'` |   
frameFieldsFragment$data.frameFields | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
  
class @fiftyone/relay.frameFieldsFragment$key()#
    

### frameFieldsFragment$key#

Name | Type | Description  
---|---|---  
frameFieldsFragment$key. $data | `plugins.fiftyone.relay.frameFieldsFragment$data` |   
frameFieldsFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'frameFieldsFragment'` `>` |   
  
class @fiftyone/relay.groupSliceFragment$data()#
    

### groupSliceFragment$data#

Name | Type | Description  
---|---|---  
groupSliceFragment$data. $fragmentType | `'groupSliceFragment'` |   
groupSliceFragment$data.defaultGroupSlice | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.groupSliceFragment$key()#
    

### groupSliceFragment$key#

Name | Type | Description  
---|---|---  
groupSliceFragment$key. $data | `plugins.fiftyone.relay.groupSliceFragment$data` |   
groupSliceFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'groupSliceFragment'` `>` |   
  
class @fiftyone/relay.histogramValuesQuery()#
    

### histogramValuesQuery#

Name | Type | Description  
---|---|---  
histogramValuesQuery.response | `plugins.fiftyone.relay.histogramValuesQuery$data` |   
histogramValuesQuery.variables | `plugins.fiftyone.relay.histogramValuesQuery$variables` |   
  
class @fiftyone/relay.histogramValuesQuery$data()#
    

### histogramValuesQuery$data#

Name | Type | Description  
---|---|---  
histogramValuesQuery$data.aggregate | `ReadonlyArray < >` `<` `Union< , , , >` `>` |   
  
class @fiftyone/relay.histogramValuesQuery$variables()#
    

### histogramValuesQuery$variables#

Name | Type | Description  
---|---|---  
histogramValuesQuery$variables.dataset | `string` |   
histogramValuesQuery$variables.form | `Union<` `plugins.fiftyone.relay.ExtendedViewForm` `,` `null` `>` |   
histogramValuesQuery$variables.path | `string` |   
histogramValuesQuery$variables.view | `Array<` `any` `>` |   
  
class @fiftyone/relay.indexesFragment$data()#
    

### indexesFragment$data#

Name | Type | Description  
---|---|---  
indexesFragment$data. $fragmentType | `'indexesFragment'` |   
indexesFragment$data.frameIndexes | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
indexesFragment$data.sampleIndexes | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
  
class @fiftyone/relay.indexesFragment$key()#
    

### indexesFragment$key#

Name | Type | Description  
---|---|---  
indexesFragment$key. $data | `plugins.fiftyone.relay.indexesFragment$data` |   
indexesFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'indexesFragment'` `>` |   
  
class @fiftyone/relay.lightningQuery()#
    

### lightningQuery#

Name | Type | Description  
---|---|---  
lightningQuery.response | `plugins.fiftyone.relay.lightningQuery$data` |   
lightningQuery.variables | `plugins.fiftyone.relay.lightningQuery$variables` |   
  
class @fiftyone/relay.lightningQuery$data()#
    

### lightningQuery$data#

Name | Type | Description  
---|---|---  
lightningQuery$data.lightning | `ReadonlyArray < >` `<` `Union< , , , , , , , >` `>` |   
  
class @fiftyone/relay.lightningQuery$variables()#
    

### lightningQuery$variables#

Name | Type | Description  
---|---|---  
lightningQuery$variables.input | `plugins.fiftyone.relay.LightningInput` |   
  
class @fiftyone/relay.mainSampleQuery()#
    

### mainSampleQuery#

Name | Type | Description  
---|---|---  
mainSampleQuery.response | `plugins.fiftyone.relay.mainSampleQuery$data` |   
mainSampleQuery.variables | `plugins.fiftyone.relay.mainSampleQuery$variables` |   
  
class @fiftyone/relay.mainSampleQuery$data()#
    

### mainSampleQuery$data#

Name | Type | Description  
---|---|---  
mainSampleQuery$data.sample | `Union<` `Object` `,` `Object` `,` `Object` `,` `Object` `,` `Object` `,` `Object` `,` `null` `>` |   
  
class @fiftyone/relay.mainSampleQuery$variables()#
    

### mainSampleQuery$variables#

Name | Type | Description  
---|---|---  
mainSampleQuery$variables.dataset | `string` |   
mainSampleQuery$variables.filter | `plugins.fiftyone.relay.SampleFilter` |   
mainSampleQuery$variables.filters | `Union<` `object` `,` `null` `>` |   
mainSampleQuery$variables.view | `Array<` `any` `>` |   
  
class @fiftyone/relay.mediaFieldsFragment$data()#
    

### mediaFieldsFragment$data#

Name | Type | Description  
---|---|---  
mediaFieldsFragment$data. $fragmentType | `'mediaFieldsFragment'` |   
mediaFieldsFragment$data.appConfig | `Union<` `Object` `,` `null` `>` |   
mediaFieldsFragment$data.name | `string` |   
mediaFieldsFragment$data.sampleFields | `ReadonlyArray < >` `<` `Object` `>` |   
  
class @fiftyone/relay.mediaFieldsFragment$key()#
    

### mediaFieldsFragment$key#

Name | Type | Description  
---|---|---  
mediaFieldsFragment$key. $data | `plugins.fiftyone.relay.mediaFieldsFragment$data` |   
mediaFieldsFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'mediaFieldsFragment'` `>` |   
  
class @fiftyone/relay.mediaTypeFragment$data()#
    

### mediaTypeFragment$data#

Name | Type | Description  
---|---|---  
mediaTypeFragment$data. $fragmentType | `'mediaTypeFragment'` |   
mediaTypeFragment$data.mediaType | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.mediaTypeFragment$key()#
    

### mediaTypeFragment$key#

Name | Type | Description  
---|---|---  
mediaTypeFragment$key. $data | `plugins.fiftyone.relay.mediaTypeFragment$data` |   
mediaTypeFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'mediaTypeFragment'` `>` |   
  
class @fiftyone/relay.paginateSamplesQuery()#
    

### paginateSamplesQuery#

Name | Type | Description  
---|---|---  
paginateSamplesQuery.response | `plugins.fiftyone.relay.paginateSamplesQuery$data` |   
paginateSamplesQuery.variables | `plugins.fiftyone.relay.paginateSamplesQuery$variables` |   
  
class @fiftyone/relay.paginateSamplesQuery$data()#
    

### paginateSamplesQuery$data#

Name | Type | Description  
---|---|---  
paginateSamplesQuery$data.samples | `Union<` `Object` `,` `Object` `,` `Object` `>` |   
  
class @fiftyone/relay.paginateSamplesQuery$variables()#
    

### paginateSamplesQuery$variables#

Name | Type | Description  
---|---|---  
paginateSamplesQuery$variables.after | `Union<` `string` `,` `null` `>` |   
paginateSamplesQuery$variables.count | `Union<` `number` `,` `null` `>` |   
paginateSamplesQuery$variables.dataset | `string` |   
paginateSamplesQuery$variables.desc | `Union<` `boolean` `,` `null` `>` |   
paginateSamplesQuery$variables.dynamicGroup | `Union<` `object` `,` `null` `>` |   
paginateSamplesQuery$variables.extendedStages | `Union<` `object` `,` `null` `>` |   
paginateSamplesQuery$variables.filter | `plugins.fiftyone.relay.SampleFilter` |   
paginateSamplesQuery$variables.filters | `Union<` `object` `,` `null` `>` |   
paginateSamplesQuery$variables.hint | `Union<` `string` `,` `null` `>` |   
paginateSamplesQuery$variables.maxQueryTime | `Union<` `number` `,` `null` `>` |   
paginateSamplesQuery$variables.paginationData | `Union<` `boolean` `,` `null` `>` |   
paginateSamplesQuery$variables.sortBy | `Union<` `string` `,` `null` `>` |   
paginateSamplesQuery$variables.view | `Array<` `any` `>` |   
  
class @fiftyone/relay.sampleFieldsFragment$data()#
    

### sampleFieldsFragment$data#

Name | Type | Description  
---|---|---  
sampleFieldsFragment$data. $fragmentType | `'sampleFieldsFragment'` |   
sampleFieldsFragment$data.sampleFields | `ReadonlyArray < >` `<` `Object` `>` |   
  
class @fiftyone/relay.sampleFieldsFragment$key()#
    

### sampleFieldsFragment$key#

Name | Type | Description  
---|---|---  
sampleFieldsFragment$key. $data | `plugins.fiftyone.relay.sampleFieldsFragment$data` |   
sampleFieldsFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'sampleFieldsFragment'` `>` |   
  
class @fiftyone/relay.savedViewsFragment$data()#
    

### savedViewsFragment$data#

Name | Type | Description  
---|---|---  
savedViewsFragment$data. $fragmentType | `'savedViewsFragment'` |   
savedViewsFragment$data.savedViews | `Union<` `ReadonlyArray < >` `,` `null` `>` |   
  
class @fiftyone/relay.savedViewsFragment$key()#
    

### savedViewsFragment$key#

Name | Type | Description  
---|---|---  
savedViewsFragment$key. $data | `plugins.fiftyone.relay.savedViewsFragment$data` |   
savedViewsFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'savedViewsFragment'` `>` |   
  
class @fiftyone/relay.savedViewsFragmentQuery()#
    

### savedViewsFragmentQuery#

Name | Type | Description  
---|---|---  
savedViewsFragmentQuery.response | `plugins.fiftyone.relay.savedViewsFragmentQuery$data` |   
savedViewsFragmentQuery.variables | `plugins.fiftyone.relay.savedViewsFragmentQuery$variables` |   
  
class @fiftyone/relay.savedViewsFragmentQuery$data()#
    

### savedViewsFragmentQuery$data#

Name | Type | Description  
---|---|---  
savedViewsFragmentQuery$data. $fragmentSpreads | `FragmentRefs < >` `<` `'savedViewsFragment'` `>` |   
  
class @fiftyone/relay.savedViewsFragmentQuery$variables()#
    

### savedViewsFragmentQuery$variables#

Name | Type | Description  
---|---|---  
savedViewsFragmentQuery$variables.name | `string` |   
  
class @fiftyone/relay.searchSelectFieldsMutation()#
    

### searchSelectFieldsMutation#

Name | Type | Description  
---|---|---  
searchSelectFieldsMutation.response | `plugins.fiftyone.relay.searchSelectFieldsMutation$data` |   
searchSelectFieldsMutation.variables | `plugins.fiftyone.relay.searchSelectFieldsMutation$variables` |   
  
class @fiftyone/relay.searchSelectFieldsMutation$data()#
    

### searchSelectFieldsMutation$data#

Name | Type | Description  
---|---|---  
searchSelectFieldsMutation$data.searchSelectFields | `ReadonlyArray < string >` `<` `string` `>` |   
  
class @fiftyone/relay.searchSelectFieldsMutation$variables()#
    

### searchSelectFieldsMutation$variables#

Name | Type | Description  
---|---|---  
searchSelectFieldsMutation$variables.datasetName | `string` |   
searchSelectFieldsMutation$variables.metaFilter | `Union<` `object` `,` `null` `>` |   
  
class @fiftyone/relay.setColorSchemeMutation()#
    

### setColorSchemeMutation#

Name | Type | Description  
---|---|---  
setColorSchemeMutation.response | `plugins.fiftyone.relay.setColorSchemeMutation$data` |   
setColorSchemeMutation.variables | `plugins.fiftyone.relay.setColorSchemeMutation$variables` |   
  
class @fiftyone/relay.setColorSchemeMutation$data()#
    

### setColorSchemeMutation$data#

Name | Type | Description  
---|---|---  
setColorSchemeMutation$data.setColorScheme | `Object` |   
  
class @fiftyone/relay.setColorSchemeMutation$variables()#
    

### setColorSchemeMutation$variables#

Name | Type | Description  
---|---|---  
setColorSchemeMutation$variables.colorScheme | `plugins.fiftyone.relay.ColorSchemeInput` |   
setColorSchemeMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setDatasetColorSchemeMutation()#
    

### setDatasetColorSchemeMutation#

Name | Type | Description  
---|---|---  
setDatasetColorSchemeMutation.response | `plugins.fiftyone.relay.setDatasetColorSchemeMutation$data` |   
setDatasetColorSchemeMutation.variables | `plugins.fiftyone.relay.setDatasetColorSchemeMutation$variables` |   
  
class @fiftyone/relay.setDatasetColorSchemeMutation$data()#
    

### setDatasetColorSchemeMutation$data#

Name | Type | Description  
---|---|---  
setDatasetColorSchemeMutation$data.setDatasetColorScheme | `Union<` `Object` `,` `null` `>` |   
  
class @fiftyone/relay.setDatasetColorSchemeMutation$variables()#
    

### setDatasetColorSchemeMutation$variables#

Name | Type | Description  
---|---|---  
setDatasetColorSchemeMutation$variables.colorScheme | `Union<` `plugins.fiftyone.relay.ColorSchemeInput` `,` `null` `>` |   
setDatasetColorSchemeMutation$variables.datasetName | `string` |   
setDatasetColorSchemeMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setDatasetMutation()#
    

### setDatasetMutation#

Name | Type | Description  
---|---|---  
setDatasetMutation.response | `plugins.fiftyone.relay.setDatasetMutation$data` |   
setDatasetMutation.variables | `plugins.fiftyone.relay.setDatasetMutation$variables` |   
  
class @fiftyone/relay.setDatasetMutation$data()#
    

### setDatasetMutation$data#

Name | Type | Description  
---|---|---  
setDatasetMutation$data.setDataset | `boolean` |   
  
class @fiftyone/relay.setDatasetMutation$variables()#
    

### setDatasetMutation$variables#

Name | Type | Description  
---|---|---  
setDatasetMutation$variables.name | `Union<` `string` `,` `null` `>` |   
setDatasetMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setDatasetMutation$variables.subscription | `string` |   
setDatasetMutation$variables.viewName | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.setFieldVisibilityStageMutation()#
    

### setFieldVisibilityStageMutation#

Name | Type | Description  
---|---|---  
setFieldVisibilityStageMutation.response | `plugins.fiftyone.relay.setFieldVisibilityStageMutation$data` |   
setFieldVisibilityStageMutation.variables | `plugins.fiftyone.relay.setFieldVisibilityStageMutation$variables` |   
  
class @fiftyone/relay.setFieldVisibilityStageMutation$data()#
    

### setFieldVisibilityStageMutation$data#

Name | Type | Description  
---|---|---  
setFieldVisibilityStageMutation$data.setFieldVisibilityStage | `boolean` |   
  
class @fiftyone/relay.setFieldVisibilityStageMutation$variables()#
    

### setFieldVisibilityStageMutation$variables#

Name | Type | Description  
---|---|---  
setFieldVisibilityStageMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setFieldVisibilityStageMutation$variables.stage | `Union<` `object` `,` `null` `>` |   
setFieldVisibilityStageMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setGroupSliceMutation()#
    

### setGroupSliceMutation#

Name | Type | Description  
---|---|---  
setGroupSliceMutation.response | `plugins.fiftyone.relay.setGroupSliceMutation$data` |   
setGroupSliceMutation.variables | `plugins.fiftyone.relay.setGroupSliceMutation$variables` |   
  
class @fiftyone/relay.setGroupSliceMutation$data()#
    

### setGroupSliceMutation$data#

Name | Type | Description  
---|---|---  
setGroupSliceMutation$data.setGroupSlice | `boolean` |   
  
class @fiftyone/relay.setGroupSliceMutation$variables()#
    

### setGroupSliceMutation$variables#

Name | Type | Description  
---|---|---  
setGroupSliceMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setGroupSliceMutation$variables.slice | `Union<` `string` `,` `null` `>` |   
setGroupSliceMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setLabelSelectionStyleMutation()#
    

### setLabelSelectionStyleMutation#

Name | Type | Description  
---|---|---  
setLabelSelectionStyleMutation.response | `plugins.fiftyone.relay.setLabelSelectionStyleMutation$data` |   
setLabelSelectionStyleMutation.variables | `plugins.fiftyone.relay.setLabelSelectionStyleMutation$variables` |   
  
class @fiftyone/relay.setLabelSelectionStyleMutation$data()#
    

### setLabelSelectionStyleMutation$data#

Name | Type | Description  
---|---|---  
setLabelSelectionStyleMutation$data.setLabelSelectionStyle | `boolean` |   
  
class @fiftyone/relay.setLabelSelectionStyleMutation$variables()#
    

### setLabelSelectionStyleMutation$variables#

Name | Type | Description  
---|---|---  
setLabelSelectionStyleMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setLabelSelectionStyleMutation$variables.style | `object` |   
setLabelSelectionStyleMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setSampleMutation()#
    

### setSampleMutation#

Name | Type | Description  
---|---|---  
setSampleMutation.response | `plugins.fiftyone.relay.setSampleMutation$data` |   
setSampleMutation.variables | `plugins.fiftyone.relay.setSampleMutation$variables` |   
  
class @fiftyone/relay.setSampleMutation$data()#
    

### setSampleMutation$data#

Name | Type | Description  
---|---|---  
setSampleMutation$data.setSample | `boolean` |   
  
class @fiftyone/relay.setSampleMutation$variables()#
    

### setSampleMutation$variables#

Name | Type | Description  
---|---|---  
setSampleMutation$variables.groupId | `Union<` `string` `,` `null` `>` |   
setSampleMutation$variables.id | `Union<` `string` `,` `null` `>` |   
setSampleMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setSampleMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setSampleSelectionStyleMutation()#
    

### setSampleSelectionStyleMutation#

Name | Type | Description  
---|---|---  
setSampleSelectionStyleMutation.response | `plugins.fiftyone.relay.setSampleSelectionStyleMutation$data` |   
setSampleSelectionStyleMutation.variables | `plugins.fiftyone.relay.setSampleSelectionStyleMutation$variables` |   
  
class @fiftyone/relay.setSampleSelectionStyleMutation$data()#
    

### setSampleSelectionStyleMutation$data#

Name | Type | Description  
---|---|---  
setSampleSelectionStyleMutation$data.setSampleSelectionStyle | `boolean` |   
  
class @fiftyone/relay.setSampleSelectionStyleMutation$variables()#
    

### setSampleSelectionStyleMutation$variables#

Name | Type | Description  
---|---|---  
setSampleSelectionStyleMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setSampleSelectionStyleMutation$variables.style | `object` |   
setSampleSelectionStyleMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setSelectedLabelsMutation()#
    

### setSelectedLabelsMutation#

Name | Type | Description  
---|---|---  
setSelectedLabelsMutation.response | `plugins.fiftyone.relay.setSelectedLabelsMutation$data` |   
setSelectedLabelsMutation.variables | `plugins.fiftyone.relay.setSelectedLabelsMutation$variables` |   
  
class @fiftyone/relay.setSelectedLabelsMutation$data()#
    

### setSelectedLabelsMutation$data#

Name | Type | Description  
---|---|---  
setSelectedLabelsMutation$data.setSelectedLabels | `boolean` |   
  
class @fiftyone/relay.setSelectedLabelsMutation$variables()#
    

### setSelectedLabelsMutation$variables#

Name | Type | Description  
---|---|---  
setSelectedLabelsMutation$variables.selectedLabels | `ReadonlyArray < SelectedLabel >` `<` `plugins.fiftyone.relay.SelectedLabel` `>` |   
setSelectedLabelsMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setSelectedLabelsMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setSelectedMutation()#
    

### setSelectedMutation#

Name | Type | Description  
---|---|---  
setSelectedMutation.response | `plugins.fiftyone.relay.setSelectedMutation$data` |   
setSelectedMutation.variables | `plugins.fiftyone.relay.setSelectedMutation$variables` |   
  
class @fiftyone/relay.setSelectedMutation$data()#
    

### setSelectedMutation$data#

Name | Type | Description  
---|---|---  
setSelectedMutation$data.setSelected | `boolean` |   
  
class @fiftyone/relay.setSelectedMutation$variables()#
    

### setSelectedMutation$variables#

Name | Type | Description  
---|---|---  
setSelectedMutation$variables.selected | `ReadonlyArray < string >` `<` `string` `>` |   
setSelectedMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setSelectedMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setSelectedSamplesMutation()#
    

### setSelectedSamplesMutation#

Name | Type | Description  
---|---|---  
setSelectedSamplesMutation.response | `plugins.fiftyone.relay.setSelectedSamplesMutation$data` |   
setSelectedSamplesMutation.variables | `plugins.fiftyone.relay.setSelectedSamplesMutation$variables` |   
  
class @fiftyone/relay.setSelectedSamplesMutation$data()#
    

### setSelectedSamplesMutation$data#

Name | Type | Description  
---|---|---  
setSelectedSamplesMutation$data.setSelectedSamples | `boolean` |   
  
class @fiftyone/relay.setSelectedSamplesMutation$variables()#
    

### setSelectedSamplesMutation$variables#

Name | Type | Description  
---|---|---  
setSelectedSamplesMutation$variables.selectedSamples | `object` |   
setSelectedSamplesMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setSelectedSamplesMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setSidebarGroupsMutation()#
    

### setSidebarGroupsMutation#

Name | Type | Description  
---|---|---  
setSidebarGroupsMutation.response | `plugins.fiftyone.relay.setSidebarGroupsMutation$data` |   
setSidebarGroupsMutation.variables | `plugins.fiftyone.relay.setSidebarGroupsMutation$variables` |   
  
class @fiftyone/relay.setSidebarGroupsMutation$data()#
    

### setSidebarGroupsMutation$data#

Name | Type | Description  
---|---|---  
setSidebarGroupsMutation$data.setSidebarGroups | `boolean` |   
  
class @fiftyone/relay.setSidebarGroupsMutation$variables()#
    

### setSidebarGroupsMutation$variables#

Name | Type | Description  
---|---|---  
setSidebarGroupsMutation$variables.dataset | `string` |   
setSidebarGroupsMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setSidebarGroupsMutation$variables.sidebarGroups | `ReadonlyArray < SidebarGroupInput >` `<` `plugins.fiftyone.relay.SidebarGroupInput` `>` |   
setSidebarGroupsMutation$variables.stages | `Array<` `any` `>` |   
setSidebarGroupsMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setSpacesMutation()#
    

### setSpacesMutation#

Name | Type | Description  
---|---|---  
setSpacesMutation.response | `plugins.fiftyone.relay.setSpacesMutation$data` |   
setSpacesMutation.variables | `plugins.fiftyone.relay.setSpacesMutation$variables` |   
  
class @fiftyone/relay.setSpacesMutation$data()#
    

### setSpacesMutation$data#

Name | Type | Description  
---|---|---  
setSpacesMutation$data.setSpaces | `boolean` |   
  
class @fiftyone/relay.setSpacesMutation$variables()#
    

### setSpacesMutation$variables#

Name | Type | Description  
---|---|---  
setSpacesMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setSpacesMutation$variables.spaces | `object` |   
setSpacesMutation$variables.subscription | `string` |   
  
class @fiftyone/relay.setViewMutation()#
    

### setViewMutation#

Name | Type | Description  
---|---|---  
setViewMutation.response | `plugins.fiftyone.relay.setViewMutation$data` |   
setViewMutation.variables | `plugins.fiftyone.relay.setViewMutation$variables` |   
  
class @fiftyone/relay.setViewMutation$data()#
    

### setViewMutation$data#

Name | Type | Description  
---|---|---  
setViewMutation$data.setView | `Union<` `Array< any >` `,` `null` `>` |   
  
class @fiftyone/relay.setViewMutation$variables()#
    

### setViewMutation$variables#

Name | Type | Description  
---|---|---  
setViewMutation$variables.datasetName | `string` |   
setViewMutation$variables.form | `plugins.fiftyone.relay.StateForm` |   
setViewMutation$variables.savedViewSlug | `Union<` `string` `,` `null` `>` |   
setViewMutation$variables.session | `Union<` `string` `,` `null` `>` |   
setViewMutation$variables.subscription | `string` |   
setViewMutation$variables.view | `Array<` `any` `>` |   
  
class @fiftyone/relay.sidebarGroupsFragment$data()#
    

### sidebarGroupsFragment$data#

Name | Type | Description  
---|---|---  
sidebarGroupsFragment$data. $fragmentSpreads | `FragmentRefs < >` `<` `Union< , >` `>` |   
sidebarGroupsFragment$data. $fragmentType | `'sidebarGroupsFragment'` |   
sidebarGroupsFragment$data.appConfig | `Union<` `Object` `,` `null` `>` |   
sidebarGroupsFragment$data.datasetId | `string` |   
  
class @fiftyone/relay.sidebarGroupsFragment$key()#
    

### sidebarGroupsFragment$key#

Name | Type | Description  
---|---|---  
sidebarGroupsFragment$key. $data | `plugins.fiftyone.relay.sidebarGroupsFragment$data` |   
sidebarGroupsFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'sidebarGroupsFragment'` `>` |   
  
class @fiftyone/relay.stageDefinitionsFragment$data()#
    

### stageDefinitionsFragment$data#

Name | Type | Description  
---|---|---  
stageDefinitionsFragment$data. $fragmentType | `'stageDefinitionsFragment'` |   
stageDefinitionsFragment$data.stageDefinitions | `ReadonlyArray < >` `<` `Object` `>` |   
  
class @fiftyone/relay.stageDefinitionsFragment$key()#
    

### stageDefinitionsFragment$key#

Name | Type | Description  
---|---|---  
stageDefinitionsFragment$key. $data | `plugins.fiftyone.relay.stageDefinitionsFragment$data` |   
stageDefinitionsFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'stageDefinitionsFragment'` `>` |   
  
class @fiftyone/relay.updateSavedViewMutation()#
    

### updateSavedViewMutation#

Name | Type | Description  
---|---|---  
updateSavedViewMutation.response | `plugins.fiftyone.relay.updateSavedViewMutation$data` |   
updateSavedViewMutation.variables | `plugins.fiftyone.relay.updateSavedViewMutation$variables` |   
  
class @fiftyone/relay.updateSavedViewMutation$data()#
    

### updateSavedViewMutation$data#

Name | Type | Description  
---|---|---  
updateSavedViewMutation$data.updateSavedView | `Union<` `Object` `,` `null` `>` |   
  
class @fiftyone/relay.updateSavedViewMutation$variables()#
    

### updateSavedViewMutation$variables#

Name | Type | Description  
---|---|---  
updateSavedViewMutation$variables.datasetName | `Union<` `string` `,` `null` `>` |   
updateSavedViewMutation$variables.session | `Union<` `string` `,` `null` `>` |   
updateSavedViewMutation$variables.subscription | `string` |   
updateSavedViewMutation$variables.updatedInfo | `plugins.fiftyone.relay.SavedViewInfo` |   
updateSavedViewMutation$variables.viewName | `string` |   
  
class @fiftyone/relay.viewFragment$data()#
    

### viewFragment$data#

Name | Type | Description  
---|---|---  
viewFragment$data. $fragmentType | `'viewFragment'` |   
viewFragment$data.stages | `Union<` `Array< any >` `,` `null` `>` |   
viewFragment$data.viewCls | `Union<` `string` `,` `null` `>` |   
viewFragment$data.viewName | `Union<` `string` `,` `null` `>` |   
  
class @fiftyone/relay.viewFragment$key()#
    

### viewFragment$key#

Name | Type | Description  
---|---|---  
viewFragment$key. $data | `plugins.fiftyone.relay.viewFragment$data` |   
viewFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'viewFragment'` `>` |   
  
class @fiftyone/relay.viewSchemaFragment$data()#
    

### viewSchemaFragment$data#

Name | Type | Description  
---|---|---  
viewSchemaFragment$data. $fragmentType | `'viewSchemaFragment'` |   
viewSchemaFragment$data.schemaForViewStages | `Object` |   
  
class @fiftyone/relay.viewSchemaFragment$key()#
    

### viewSchemaFragment$key#

Name | Type | Description  
---|---|---  
viewSchemaFragment$key. $data | `plugins.fiftyone.relay.viewSchemaFragment$data` |   
viewSchemaFragment$key. $fragmentSpreads | `FragmentRefs < >` `<` `'viewSchemaFragment'` `>` |   
  
## Variables#

### RelayEnvironmentContext#

Name | Type | Description  
---|---|---  
Context < Environment > | `Context < Environment >` `<` `Environment` `>` |   
  
### aggregate#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### aggregation#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### colorSchemeFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### configFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### countValues#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### createSavedView#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### dataset#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### datasetAppConfigFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### datasetFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### deleteSavedView#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### estimatedCounts#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### frameFieldsFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### groupSliceFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### histogramValues#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### indexesFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### lightning#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### mainSample#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### mediaFieldsFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### mediaTypeFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### paginateSamples#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### sampleFieldsFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### savedViewsFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### searchSelectFields#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setColorScheme#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setDataset#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setDatasetColorScheme#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setFieldVisibilityStage#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setGroupSlice#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setLabelSelectionStyle#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setSample#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setSampleSelectionStyle#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setSelected#

Backward-compatible mutation that accepts a flat list of sample IDs. All samples are set to âdefaultâ selection type.

Prefer setSelectedSamples for new code that needs selection type support.

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setSelectedLabels#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setSelectedSamples#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setSidebarGroups#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setSpaces#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### setView#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### sidebarGroupsFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### stageDefinitionsFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### updateSavedView#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### viewFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
### viewSchemaFragment#

Name | Type | Description  
---|---|---  
GraphQLTaggedNode | `GraphQLTaggedNode` |   
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
