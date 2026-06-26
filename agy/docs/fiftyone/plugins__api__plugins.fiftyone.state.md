---
source_url: https://docs.voxel51.com/plugins/api/plugins.fiftyone.state.html
---

# @fiftyone/state#

## State#

### activeFieldsConfig#

Name | Type | Description  
---|---|---  
activeFieldsConfig.exclude | `boolean` |   
activeFieldsConfig.paths | `readonly` |   
      
    
    const activeFieldsConfig = useRecoilValue(fos.activeFieldsConfig);
    

### activeIndex#

Name | Type | Description  
---|---|---  
activeIndex | `string` |   
      
    
    const activeIndex = useRecoilValue(fos.activeIndex);
    

### activeModalSample#

Name | Type | Description  
---|---|---  
activeModalSample | `plugins.fiftyone.state.Sample` |   
      
    
    const activeModalSample = useRecoilValue(fos.activeModalSample);
    

### activeModalSidebarSample#

Name | Type | Description  
---|---|---  
activeModalSidebarSample | `plugins.fiftyone.state.Sample` |   
      
    
    const activeModalSidebarSample = useRecoilValue(fos.activeModalSidebarSample);
    

### activePlot#

Name | Type | Description  
---|---|---  
activePlot | `string` |   
      
    
    const [activePlot, setActivePlot] = useRecoilState(fos.activePlot);
    

### activeSliceDescriptorLabel#

Name | Type | Description  
---|---|---  
activeSliceDescriptorLabel | `string` |   
      
    
    const activeSliceDescriptorLabel = useRecoilValue(fos.activeSliceDescriptorLabel);
    

### allFieldsCheckedState#

Name | Type | Description  
---|---|---  
allFieldsCheckedState | `boolean` |   
      
    
    const [allFieldsCheckedState, setAllFieldsCheckedState] = useRecoilState(fos.allFieldsCheckedState);
    

### anyTagging#

Name | Type | Description  
---|---|---  
anyTagging | `boolean` |   
      
    
    const [anyTagging, setAnyTagging] = useRecoilState(fos.anyTagging);
    

### attributeVisibility#

Name | Type | Description  
---|---|---  
attributeVisibility | `plugins.fiftyone.state.Filters` |   
      
    
    const [attributeVisibility, setAttributeVisibility] = useRecoilState(fos.attributeVisibility);
    

### canAnnotate#

Name | Type | Description  
---|---|---  
canAnnotate.enabled | `boolean` |   
canAnnotate.message | `string` |   
      
    
    const [canAnnotate, setCanAnnotate] = useRecoilState(fos.canAnnotate);
    

### canCreateNewField#

Name | Type | Description  
---|---|---  
canCreateNewField.enabled | `boolean` |   
canCreateNewField.message | `string` |   
      
    
    const [canCreateNewField, setCanCreateNewField] = useRecoilState(fos.canCreateNewField);
    

### canEditCustomColors#

Name | Type | Description  
---|---|---  
canEditCustomColors.enabled | `boolean` |   
canEditCustomColors.message | `string` |   
      
    
    const [canEditCustomColors, setCanEditCustomColors] = useRecoilState(fos.canEditCustomColors);
    

### canEditLabels#

Name | Type | Description  
---|---|---  
canEditLabels.enabled | `boolean` |   
canEditLabels.message | `string` |   
      
    
    const [canEditLabels, setCanEditLabels] = useRecoilState(fos.canEditLabels);
    

### canEditSavedViews#

Name | Type | Description  
---|---|---  
canEditSavedViews.enabled | `boolean` |   
canEditSavedViews.message | `string` |   
      
    
    const [canEditSavedViews, setCanEditSavedViews] = useRecoilState(fos.canEditSavedViews);
    

### canEditWorkspaces#

Name | Type | Description  
---|---|---  
canEditWorkspaces.enabled | `boolean` |   
canEditWorkspaces.message | `string` |   
      
    
    const [canEditWorkspaces, setCanEditWorkspaces] = useRecoilState(fos.canEditWorkspaces);
    

### canManageSchema#

Name | Type | Description  
---|---|---  
canManageSchema.enabled | `boolean` |   
canManageSchema.message | `string` |   
      
    
    const [canManageSchema, setCanManageSchema] = useRecoilState(fos.canManageSchema);
    

### canModifySidebarGroup#

Name | Type | Description  
---|---|---  
canModifySidebarGroup.enabled | `boolean` |   
canModifySidebarGroup.message | `string` |   
      
    
    const [canModifySidebarGroup, setCanModifySidebarGroup] = useRecoilState(fos.canModifySidebarGroup);
    

### canTagSamplesOrLabels#

Name | Type | Description  
---|---|---  
canTagSamplesOrLabels.enabled | `boolean` |   
canTagSamplesOrLabels.message | `string` |   
      
    
    const [canTagSamplesOrLabels, setCanTagSamplesOrLabels] = useRecoilState(fos.canTagSamplesOrLabels);
    

### collapsedPaths#

Name | Type | Description  
---|---|---  
collapsedPaths | `Set < string >` `<` `string` `>` |   
      
    
    const collapsedPaths = useRecoilValue(fos.collapsedPaths);
    

### colorMap#
    
    
    const colorMap = useRecoilValue(fos.colorMap);
    

### colorMapRGB#
    
    
    const colorMapRGB = useRecoilValue(fos.colorMapRGB);
    

### colorScheme#

Name | Type | Description  
---|---|---  
colorScheme | `plugins.fiftyone.state.ColorSchemeInput` |   
      
    
    const [colorScheme, setColorScheme] = useRecoilState(fos.colorScheme);
    

### colorSeed#

Name | Type | Description  
---|---|---  
colorSeed | `number` |   
      
    
    const [colorSeed, setColorSeed] = useRecoilState(fos.colorSeed);
    

### coloring#

Name | Type | Description  
---|---|---  
coloring | `plugins.fiftyone.state.Coloring` |   
      
    
    const [coloring, setColoring] = useRecoilState(fos.coloring);
    

### config#

Name | Type | Description  
---|---|---  
config.colorBy | `plugins.fiftyone.state.ColorBy` |   
config.colorPool | `readonly` |   
config.colorscale | `string` |   
config.defaultQueryPerformance | `boolean` |   
config.disableFrameFiltering | `boolean` |   
config.enableQueryPerformance | `boolean` |   
config.gridZoom | `number` |   
config.loopVideos | `boolean` |   
config.maxQueryTime | `number` |   
config.mediaFallback | `boolean` |   
config.multicolorKeypoints | `boolean` |   
config.notebookHeight | `number` |   
config.plugins | `object` |   
config.showConfidence | `boolean` |   
config.showIndex | `boolean` |   
config.showLabel | `boolean` |   
config.showSkeletons | `boolean` |   
config.showTooltip | `boolean` |   
config.theme | `plugins.fiftyone.state.Theme` |   
config.timezone | `string` |   
config.useFrameNumber | `boolean` |   
      
    
    const config = useRecoilValue(fos.config);
    

### configData#

Name | Type | Description  
---|---|---  
configData | `plugins.fiftyone.state.configFragment$data` |   
      
    
    const [configData, setConfigData] = useRecoilState(fos.configData);
    

### currentGroupSliceNames#

Slice names that actually exist for the currently opened modal group.

This differs from `groupSlices`, which describes dataset-level slice definitions. Sparse groups may omit some slices entirely, and annotate-mode selectors should only offer slices that are present for the active group.
    
    
    const currentGroupSliceNames = useRecoilValue(fos.currentGroupSliceNames);
    

### currentSampleId#

Name | Type | Description  
---|---|---  
currentSampleId | `string` |   
      
    
    const currentSampleId = useRecoilValue(fos.currentSampleId);
    

### currentViewSlug#

Name | Type | Description  
---|---|---  
currentViewSlug | `string` |   
      
    
    const currentViewSlug = useRecoilValue(fos.currentViewSlug);
    

### dataset#

Name | Type | Description  
---|---|---  
dataset | `plugins.fiftyone.state.Dataset` |   
      
    
    const [dataset, setDataset] = useRecoilState(fos.dataset);
    

### datasetAppConfig#

Name | Type | Description  
---|---|---  
datasetAppConfig | `plugins.fiftyone.state.datasetAppConfigFragment$data` |   
      
    
    const [datasetAppConfig, setDatasetAppConfig] = useRecoilState(fos.datasetAppConfig);
    

### datasetColorScheme#

Name | Type | Description  
---|---|---  
datasetColorScheme | `plugins.fiftyone.state.colorSchemeFragment$data` |   
      
    
    const [datasetColorScheme, setDatasetColorScheme] = useRecoilState(fos.datasetColorScheme);
    

### datasetFrameCount#

Name | Type | Description  
---|---|---  
datasetFrameCount | `number` |   
      
    
    const datasetFrameCount = useRecoilValue(fos.datasetFrameCount);
    

### datasetId#

Name | Type | Description  
---|---|---  
datasetId | `string` |   
      
    
    const [datasetId, setDatasetId] = useRecoilState(fos.datasetId);
    

### datasetName#

Name | Type | Description  
---|---|---  
datasetName | `string` |   
      
    
    const [datasetName, setDatasetName] = useRecoilState(fos.datasetName);
    

### datasetSampleCount#

Name | Type | Description  
---|---|---  
datasetSampleCount | `number` |   
      
    
    const datasetSampleCount = useRecoilValue(fos.datasetSampleCount);
    

### defaultActiveFields#
    
    
    const defaultActiveFields = useRecoilValue(fos.defaultActiveFields);
    

### defaultGroupSlice#

Name | Type | Description  
---|---|---  
defaultGroupSlice | `string` |   
      
    
    const [defaultGroupSlice, setDefaultGroupSlice] = useRecoilState(fos.defaultGroupSlice);
    

### defaultQueryPerformanceConfig#

Name | Type | Description  
---|---|---  
defaultQueryPerformanceConfig | `boolean` |   
      
    
    const defaultQueryPerformanceConfig = useRecoilValue(fos.defaultQueryPerformanceConfig);
    

### defaultTargets#

Name | Type | Description  
---|---|---  
defaultTargets | `plugins.fiftyone.state.Targets` |   
      
    
    const defaultTargets = useRecoilValue(fos.defaultTargets);
    

### disableFrameFiltering#

Name | Type | Description  
---|---|---  
disableFrameFiltering | `boolean` |   
      
    
    const disableFrameFiltering = useRecoilValue(fos.disableFrameFiltering);
    

### disabledCheckboxPaths#

Returns a set of paths that have their checkbox disabled in the sidebar

Name | Type | Description  
---|---|---  
disabledCheckboxPaths | `Set < string >` `<` `string` `>` |   
      
    
    const disabledCheckboxPaths = useRecoilValue(fos.disabledCheckboxPaths);
    

### disabledFilterPaths#

Returns a set of paths that have their filter dropdown disabled in the sidebar

Name | Type | Description  
---|---|---  
disabledFilterPaths | `Set < string >` `<` `string` `>` |   
      
    
    const disabledFilterPaths = useRecoilValue(fos.disabledFilterPaths);
    

### disabledFrameFilterPaths#

Name | Type | Description  
---|---|---  
disabledFrameFilterPaths | `Set < string >` `<` `string` `>` |   
      
    
    const disabledFrameFilterPaths = useRecoilValue(fos.disabledFrameFilterPaths);
    

### distributionPaths#
    
    
    const distributionPaths = useRecoilValue(fos.distributionPaths);
    

### dynamicGroupCurrentElementIndex#

Name | Type | Description  
---|---|---  
dynamicGroupCurrentElementIndex | `number` |   
      
    
    const [dynamicGroupCurrentElementIndex, setDynamicGroupCurrentElementIndex] = useRecoilState(fos.dynamicGroupCurrentElementIndex);
    

### dynamicGroupFields#
    
    
    const dynamicGroupFields = useRecoilValue(fos.dynamicGroupFields);
    

### dynamicGroupIndex#

Name | Type | Description  
---|---|---  
dynamicGroupIndex | `number` |   
      
    
    const [dynamicGroupIndex, setDynamicGroupIndex] = useRecoilState(fos.dynamicGroupIndex);
    

### dynamicGroupParameters#

Name | Type | Description  
---|---|---  
dynamicGroupParameters | `plugins.fiftyone.state.DynamicGroupParameters` |   
      
    
    const [dynamicGroupParameters, setDynamicGroupParameters] = useRecoilState(fos.dynamicGroupParameters);
    

### dynamicGroupsTargetFrameRate#

Name | Type | Description  
---|---|---  
dynamicGroupsTargetFrameRate | `number` |   
      
    
    const dynamicGroupsTargetFrameRate = useRecoilValue(fos.dynamicGroupsTargetFrameRate);
    

### editingFieldAtom#

Name | Type | Description  
---|---|---  
editingFieldAtom | `boolean` |   
      
    
    const [editingFieldAtom, setEditingFieldAtom] = useRecoilState(fos.editingFieldAtom);
    

### elementNames#

Name | Type | Description  
---|---|---  
elementNames.plural | `string` |   
elementNames.singular | `string` |   
      
    
    const elementNames = useRecoilValue(fos.elementNames);
    

### eligibleFieldsToCustomizeColor#
    
    
    const eligibleFieldsToCustomizeColor = useRecoilValue(fos.eligibleFieldsToCustomizeColor);
    

### enableQueryPerformanceConfig#

Name | Type | Description  
---|---|---  
enableQueryPerformanceConfig | `boolean` |   
      
    
    const enableQueryPerformanceConfig = useRecoilValue(fos.enableQueryPerformanceConfig);
    

### escapeKeyHandlerIdsAtom#

Name | Type | Description  
---|---|---  
escapeKeyHandlerIdsAtom | `Set < string >` `<` `string` `>` |   
      
    
    const [escapeKeyHandlerIdsAtom, setEscapeKeyHandlerIdsAtom] = useRecoilState(fos.escapeKeyHandlerIdsAtom);
    

### excludedPathsStrippedState#
    
    
    const excludedPathsStrippedState = useRecoilValue(fos.excludedPathsStrippedState);
    

### expandedPathsState#
    
    
    const [expandedPathsState, setExpandedPathsState] = useRecoilState(fos.expandedPathsState);
    

### extendedSelection#

Name | Type | Description  
---|---|---  
extendedSelection.scope | `string` |   
extendedSelection.selection | `Array<` `string` `>` |   
extendedSelection.spatialSelection | `Object` |   
      
    
    const [extendedSelection, setExtendedSelection] = useRecoilState(fos.extendedSelection);
    

### extendedSelectionOverrideStage#

Name | Type | Description  
---|---|---  
extendedSelectionOverrideStage | `any` |   
      
    
    const [extendedSelectionOverrideStage, setExtendedSelectionOverrideStage] = useRecoilState(fos.extendedSelectionOverrideStage);
    

### extendedStages#

Name | Type | Description  
---|---|---  
extendedStages | `any` |   
      
    
    const extendedStages = useRecoilValue(fos.extendedStages);
    

### extendedStagesNoSort#

Name | Type | Description  
---|---|---  
extendedStagesNoSort | `any` |   
      
    
    const extendedStagesNoSort = useRecoilValue(fos.extendedStagesNoSort);
    

### extendedStagesUnsorted#

Name | Type | Description  
---|---|---  
extendedStagesUnsorted | `any` |   
      
    
    const extendedStagesUnsorted = useRecoilValue(fos.extendedStagesUnsorted);
    

### fieldSchemaState#

Name | Type | Description  
---|---|---  
fieldSchemaState | `any` |   
      
    
    const [fieldSchemaState, setFieldSchemaState] = useRecoilState(fos.fieldSchemaState);
    

### fieldVisibilityStage#

Name | Type | Description  
---|---|---  
fieldVisibilityStage | `plugins.fiftyone.state.FieldVisibilityStage` |   
      
    
    const [fieldVisibilityStage, setFieldVisibilityStage] = useRecoilState(fos.fieldVisibilityStage);
    

### filters#

Name | Type | Description  
---|---|---  
filters | `plugins.fiftyone.state.Filters` |   
      
    
    const [filters, setFilters] = useRecoilState(fos.filters);
    

### flatFrameFields#
    
    
    const flatFrameFields = useRecoilValue(fos.flatFrameFields);
    

### flatSampleFields#
    
    
    const flatSampleFields = useRecoilValue(fos.flatSampleFields);
    

### frameFields#
    
    
    const frameFields = useRecoilValue(fos.frameFields);
    

### frameFieldsList#
    
    
    const frameFieldsList = useRecoilValue(fos.frameFieldsList);
    

### fullSchema#

Name | Type | Description  
---|---|---  
fullSchema | `plugins.fiftyone.state.Schema` |   
      
    
    const fullSchema = useRecoilValue(fos.fullSchema);
    

### fullscreen#

Name | Type | Description  
---|---|---  
fullscreen | `boolean` |   
      
    
    const [fullscreen, setFullscreen] = useRecoilState(fos.fullscreen);
    

### fullyDisabledPaths#

Returns a set of paths that should have both their checkbox and filter dropdown disabled in the sidebar

Name | Type | Description  
---|---|---  
fullyDisabledPaths | `Set < string >` `<` `string` `>` |   
      
    
    const fullyDisabledPaths = useRecoilValue(fos.fullyDisabledPaths);
    

### generatedDatasetName#

Extracts the generated dataset name from the view stages. Generated views (patches, clips, frames) store their dataset info in the `_state` kwarg of the view stage that created them (e.g., ToPatches, ToClips).

Name | Type | Description  
---|---|---  
generatedDatasetName | `string` |   
      
    
    const generatedDatasetName = useRecoilValue(fos.generatedDatasetName);
    

### getSkeleton#
    
    
    const getSkeleton = useRecoilValue(fos.getSkeleton);
    

### getTarget#
    
    
    const getTarget = useRecoilValue(fos.getTarget);
    

### gridSortBy#

Name | Type | Description  
---|---|---  
gridSortBy.descending | `boolean` |   
gridSortBy.field | `string` |   
      
    
    const [gridSortBy, setGridSortBy] = useRecoilState(fos.gridSortBy);
    

### gridSortFields#
    
    
    const gridSortFields = useRecoilValue(fos.gridSortFields);
    

### groupByFieldValue#
    
    
    const groupByFieldValue = useRecoilValue(fos.groupByFieldValue);
    

### groupField#

Name | Type | Description  
---|---|---  
groupField | `string` |   
      
    
    const groupField = useRecoilValue(fos.groupField);
    

### groupId#

Name | Type | Description  
---|---|---  
groupId | `string` |   
      
    
    const groupId = useRecoilValue(fos.groupId);
    

### groupMediaIsCarouselVisible#

Derived selector that determines if the carousel should actually be visible. Combines user setting with contextual rules (e.g., hidden for ImaVid in nested groups).

Name | Type | Description  
---|---|---  
groupMediaIsCarouselVisible | `boolean` |   
      
    
    const groupMediaIsCarouselVisible = useRecoilValue(fos.groupMediaIsCarouselVisible);
    

### groupMediaIsCarouselVisibleSetting#

User setting controlling whether the carousel (filmstrip of group slices) is visible in the modal.

Name | Type | Description  
---|---|---  
groupMediaIsCarouselVisibleSetting | `boolean` |   
      
    
    const [groupMediaIsCarouselVisibleSetting, setGroupMediaIsCarouselVisibleSetting] = useRecoilState(fos.groupMediaIsCarouselVisibleSetting);
    

### groupMediaIsMain2DViewerVisible#

Derived selector that determines if the main viewer should actually be visible. Combines user setting with contextual rules (shown when no 3D slices or multiple media types exist).

Name | Type | Description  
---|---|---  
groupMediaIsMain2DViewerVisible | `boolean` |   
      
    
    const groupMediaIsMain2DViewerVisible = useRecoilValue(fos.groupMediaIsMain2DViewerVisible);
    

### groupMediaIsMain2DViewerVisibleSetting#

User setting controlling whether the main 2D viewer is visible in the modal for grouped datasets. Persisted to session storage.

Name | Type | Description  
---|---|---  
groupMediaIsMain2DViewerVisibleSetting | `boolean` |   
      
    
    const [groupMediaIsMain2DViewerVisibleSetting, setGroupMediaIsMain2DViewerVisibleSetting] = useRecoilState(fos.groupMediaIsMain2DViewerVisibleSetting);
    

### groupMediaTypes#
    
    
    const groupMediaTypes = useRecoilValue(fos.groupMediaTypes);
    

### groupMediaTypesMap#

Mapping of slice names to their media types for grouped datasets. E.g., { âleftâ: âimageâ, ârightâ: âimageâ, âlidarâ: âpoint_cloudâ }
    
    
    const groupMediaTypesMap = useRecoilValue(fos.groupMediaTypesMap);
    

### groupMediaTypesSet#

Name | Type | Description  
---|---|---  
groupMediaTypesSet | `Set < string >` `<` `string` `>` |   
      
    
    const groupMediaTypesSet = useRecoilValue(fos.groupMediaTypesSet);
    

### groupSampleAtMainSlice#

Same as `modalSample` but always pinned to the datasetâs main `groupSlice` for both the active slice and the requested slices. Used by `groupByFieldValue` so the dynamic group value is always read from the main sliceâs sample regardless of which slice the modal is currently displaying. Has its own Relay cache key so it can resolve independently.

Name | Type | Description  
---|---|---  
groupSampleAtMainSlice | `plugins.fiftyone.state.ModalSample` |   
      
    
    const [groupSampleAtMainSlice, setGroupSampleAtMainSlice] = useRecoilState(fos.groupSampleAtMainSlice);
    

### groupSlice#

Name | Type | Description  
---|---|---  
groupSlice | `string` |   
      
    
    const [groupSlice, setGroupSlice] = useRecoilState(fos.groupSlice);
    

### groupSlices#
    
    
    const groupSlices = useRecoilValue(fos.groupSlices);
    

### hasGroupSlices#

Name | Type | Description  
---|---|---  
hasGroupSlices | `boolean` |   
      
    
    const hasGroupSlices = useRecoilValue(fos.hasGroupSlices);
    

### hasSelectedLabels#

Name | Type | Description  
---|---|---  
hasSelectedLabels | `boolean` |   
      
    
    const hasSelectedLabels = useRecoilValue(fos.hasSelectedLabels);
    

### hasSelectedSamples#

Name | Type | Description  
---|---|---  
hasSelectedSamples | `boolean` |   
      
    
    const hasSelectedSamples = useRecoilValue(fos.hasSelectedSamples);
    

### hiddenLabelIds#

Name | Type | Description  
---|---|---  
hiddenLabelIds | `Set < string >` `<` `string` `>` |   
      
    
    const hiddenLabelIds = useRecoilValue(fos.hiddenLabelIds);
    

### hiddenLabels#

Name | Type | Description  
---|---|---  
hiddenLabels | `plugins.fiftyone.state.SelectedLabelMap` |   
      
    
    const [hiddenLabels, setHiddenLabels] = useRecoilState(fos.hiddenLabels);
    

### hiddenLabelsArray#
    
    
    const hiddenLabelsArray = useRecoilValue(fos.hiddenLabelsArray);
    

### hiddenNoneGroups#

Name | Type | Description  
---|---|---  
hiddenNoneGroups.groups | `Set < string >` `<` `string` `>` |   
hiddenNoneGroups.paths | `Set < string >` `<` `string` `>` |   
      
    
    const hiddenNoneGroups = useRecoilValue(fos.hiddenNoneGroups);
    

### hideNoneValuedFields#

Name | Type | Description  
---|---|---  
hideNoneValuedFields | `boolean` |   
      
    
    const [hideNoneValuedFields, setHideNoneValuedFields] = useRecoilState(fos.hideNoneValuedFields);
    

### hoveredSample#

Name | Type | Description  
---|---|---  
hoveredSample | `plugins.fiftyone.state.Sample` |   
      
    
    const [hoveredSample, setHoveredSample] = useRecoilState(fos.hoveredSample);
    

### includeNestedFieldsState#

Name | Type | Description  
---|---|---  
includeNestedFieldsState | `boolean` |   
      
    
    const [includeNestedFieldsState, setIncludeNestedFieldsState] = useRecoilState(fos.includeNestedFieldsState);
    

### indexInfo#

Name | Type | Description  
---|---|---  
indexInfo | `plugins.fiftyone.state.indexesFragment$data` |   
      
    
    const [indexInfo, setIndexInfo] = useRecoilState(fos.indexInfo);
    

### is3DDataset#

Name | Type | Description  
---|---|---  
is3DDataset | `boolean` |   
      
    
    const is3DDataset = useRecoilValue(fos.is3DDataset);
    

### isClipsView#

Name | Type | Description  
---|---|---  
isClipsView | `boolean` |   
      
    
    const isClipsView = useRecoilValue(fos.isClipsView);
    

### isDynamicGroup#

Name | Type | Description  
---|---|---  
isDynamicGroup | `boolean` |   
      
    
    const isDynamicGroup = useRecoilValue(fos.isDynamicGroup);
    

### isFieldVisibilityActive#

Name | Type | Description  
---|---|---  
isFieldVisibilityActive | `boolean` |   
      
    
    const isFieldVisibilityActive = useRecoilValue(fos.isFieldVisibilityActive);
    

### isFramesView#

Name | Type | Description  
---|---|---  
isFramesView | `boolean` |   
      
    
    const isFramesView = useRecoilValue(fos.isFramesView);
    

### isGeneratedView#

Name | Type | Description  
---|---|---  
isGeneratedView | `boolean` |   
      
    
    const isGeneratedView = useRecoilValue(fos.isGeneratedView);
    

### isGroup#

Name | Type | Description  
---|---|---  
isGroup | `boolean` |   
      
    
    const isGroup = useRecoilValue(fos.isGroup);
    

### isInMultiPanelViewAtom#

Name | Type | Description  
---|---|---  
isInMultiPanelViewAtom | `boolean` |   
      
    
    const [isInMultiPanelViewAtom, setIsInMultiPanelViewAtom] = useRecoilState(fos.isInMultiPanelViewAtom);
    

### isLargeVideo#

Name | Type | Description  
---|---|---  
isLargeVideo | `boolean` |   
      
    
    const isLargeVideo = useRecoilValue(fos.isLargeVideo);
    

### isModalActive#

Name | Type | Description  
---|---|---  
isModalActive | `boolean` |   
      
    
    const isModalActive = useRecoilValue(fos.isModalActive);
    

### isNestedDynamicGroup#

Name | Type | Description  
---|---|---  
isNestedDynamicGroup | `boolean` |   
      
    
    const isNestedDynamicGroup = useRecoilValue(fos.isNestedDynamicGroup);
    

### isNonNestedDynamicGroup#

Name | Type | Description  
---|---|---  
isNonNestedDynamicGroup | `boolean` |   
      
    
    const isNonNestedDynamicGroup = useRecoilValue(fos.isNonNestedDynamicGroup);
    

### isNotebook#

Name | Type | Description  
---|---|---  
isNotebook | `boolean` |   
      
    
    const isNotebook = useRecoilValue(fos.isNotebook);
    

### isOrderedDynamicGroup#

Name | Type | Description  
---|---|---  
isOrderedDynamicGroup | `boolean` |   
      
    
    const isOrderedDynamicGroup = useRecoilValue(fos.isOrderedDynamicGroup);
    

### isPatchesView#

Name | Type | Description  
---|---|---  
isPatchesView | `boolean` |   
      
    
    const isPatchesView = useRecoilValue(fos.isPatchesView);
    

### isQueryPerformantView#

Name | Type | Description  
---|---|---  
isQueryPerformantView | `boolean` |   
      
    
    const isQueryPerformantView = useRecoilValue(fos.isQueryPerformantView);
    

### isRootView#

Name | Type | Description  
---|---|---  
isRootView | `boolean` |   
      
    
    const isRootView = useRecoilValue(fos.isRootView);
    

### isSidebarFilterMode#

Name | Type | Description  
---|---|---  
isSidebarFilterMode | `boolean` |   
      
    
    const [isSidebarFilterMode, setIsSidebarFilterMode] = useRecoilState(fos.isSidebarFilterMode);
    

### isTooltipLocked#

Name | Type | Description  
---|---|---  
isTooltipLocked | `boolean` |   
      
    
    const [isTooltipLocked, setIsTooltipLocked] = useRecoilState(fos.isTooltipLocked);
    

### isVideoDataset#

Name | Type | Description  
---|---|---  
isVideoDataset | `boolean` |   
      
    
    const isVideoDataset = useRecoilValue(fos.isVideoDataset);
    

### labelPathsSet#

Name | Type | Description  
---|---|---  
labelPathsSet | `Set < string >` `<` `string` `>` |   
      
    
    const labelPathsSet = useRecoilValue(fos.labelPathsSet);
    

### labelPathsSetExpanded#

Name | Type | Description  
---|---|---  
labelPathsSetExpanded | `Set < string >` `<` `string` `>` |   
      
    
    const labelPathsSetExpanded = useRecoilValue(fos.labelPathsSetExpanded);
    

### labelSelectionStyle#

Name | Type | Description  
---|---|---  
labelSelectionStyle | `plugins.fiftyone.state.LabelSelectionStyle` |   
      
    
    const [labelSelectionStyle, setLabelSelectionStyle] = useRecoilState(fos.labelSelectionStyle);
    

### lastLoadedDatasetNameState#

Name | Type | Description  
---|---|---  
lastLoadedDatasetNameState | `string` |   
      
    
    const [lastLoadedDatasetNameState, setLastLoadedDatasetNameState] = useRecoilState(fos.lastLoadedDatasetNameState);
    

### loading#

Name | Type | Description  
---|---|---  
loading | `boolean` |   
      
    
    const [loading, setLoading] = useRecoilState(fos.loading);
    

### lookerPanels#

Name | Type | Description  
---|---|---  
lookerPanels.help | `Object` |   
lookerPanels.json | `Object` |   
      
    
    const [lookerPanels, setLookerPanels] = useRecoilState(fos.lookerPanels);
    

### mediaFields#
    
    
    const [mediaFields, setMediaFields] = useRecoilState(fos.mediaFields);
    

### mediaType#

Name | Type | Description  
---|---|---  
mediaType | `string` |   
      
    
    const [mediaType, setMediaType] = useRecoilState(fos.mediaType);
    

### mediaTypeSelector#

Name | Type | Description  
---|---|---  
mediaTypeSelector | `Union<` `'image'` `,` `'group'` `,` `'point_cloud'` `,` `'point-cloud'` `,` `'three_d'` `,` `'3d'` `,` `'video'` `,` `'unknown'` `>` |   
      
    
    const mediaTypeSelector = useRecoilValue(fos.mediaTypeSelector);
    

### modal#

Name | Type | Description  
---|---|---  
modal | `plugins.fiftyone.state.ModalSample` |   
      
    
    const [modal, setModal] = useRecoilState(fos.modal);
    

### modalAttributeVisibility#

Name | Type | Description  
---|---|---  
modalAttributeVisibility | `plugins.fiftyone.state.Filters` |   
      
    
    const [modalAttributeVisibility, setModalAttributeVisibility] = useRecoilState(fos.modalAttributeVisibility);
    

### modalFilters#

Name | Type | Description  
---|---|---  
modalFilters | `plugins.fiftyone.state.Filters` |   
      
    
    const [modalFilters, setModalFilters] = useRecoilState(fos.modalFilters);
    

### modalGroupSlice#

Name | Type | Description  
---|---|---  
modalGroupSlice | `string` |   
      
    
    const [modalGroupSlice, setModalGroupSlice] = useRecoilState(fos.modalGroupSlice);
    

### modalLooker#

Name | Type | Description  
---|---|---  
modalLooker | `plugins.fiftyone.state.Lookers` |   
      
    
    const [modalLooker, setModalLooker] = useRecoilState(fos.modalLooker);
    

### modalSample#

Name | Type | Description  
---|---|---  
modalSample | `plugins.fiftyone.state.ModalSample` |   
      
    
    const [modalSample, setModalSample] = useRecoilState(fos.modalSample);
    

### modalSampleId#

Name | Type | Description  
---|---|---  
modalSampleId | `string` |   
      
    
    const modalSampleId = useRecoilValue(fos.modalSampleId);
    

### modalSelector#

Name | Type | Description  
---|---|---  
modalSelector | `plugins.fiftyone.state.ModalSelector` |   
      
    
    const [modalSelector, setModalSelector] = useRecoilState(fos.modalSelector);
    

### modalTopBarVisible#

Name | Type | Description  
---|---|---  
modalTopBarVisible | `boolean` |   
      
    
    const [modalTopBarVisible, setModalTopBarVisible] = useRecoilState(fos.modalTopBarVisible);
    

### non3dSamples#
    
    
    const non3dSamples = useRecoilValue(fos.non3dSamples);
    

### noneValuedPaths#

Name | Type | Description  
---|---|---  
noneValuedPaths | `Record < string , Set >` `<` `string` `,` `Set < string >` `>` |   
      
    
    const [noneValuedPaths, setNoneValuedPaths] = useRecoilState(fos.noneValuedPaths);
    

### nullableModalSampleId#

Name | Type | Description  
---|---|---  
nullableModalSampleId | `string` |   
      
    
    const nullableModalSampleId = useRecoilValue(fos.nullableModalSampleId);
    

### only3d#

Name | Type | Description  
---|---|---  
only3d | `boolean` |   
      
    
    const only3d = useRecoilValue(fos.only3d);
    

### parentMediaTypeSelector#

Name | Type | Description  
---|---|---  
parentMediaTypeSelector | `Union<` `'image'` `,` `'group'` `,` `'point_cloud'` `,` `'point-cloud'` `,` `'three_d'` `,` `'3d'` `,` `'video'` `,` `'unknown'` `>` |   
      
    
    const parentMediaTypeSelector = useRecoilValue(fos.parentMediaTypeSelector);
    

### patching#

Name | Type | Description  
---|---|---  
patching | `boolean` |   
      
    
    const [patching, setPatching] = useRecoilState(fos.patching);
    

### pathHiddenLabelsMap#
    
    
    const [pathHiddenLabelsMap, setPathHiddenLabelsMap] = useRecoilState(fos.pathHiddenLabelsMap);
    

### queryPerformance#

Name | Type | Description  
---|---|---  
queryPerformance | `boolean` |   
      
    
    const [queryPerformance, setQueryPerformance] = useRecoilState(fos.queryPerformance);
    

### queryPerformanceMaxSearch#

Name | Type | Description  
---|---|---  
queryPerformanceMaxSearch | `number` |   
      
    
    const [queryPerformanceMaxSearch, setQueryPerformanceMaxSearch] = useRecoilState(fos.queryPerformanceMaxSearch);
    

### queryPerformanceSetting#

Name | Type | Description  
---|---|---  
queryPerformanceSetting | `boolean` |   
      
    
    const [queryPerformanceSetting, setQueryPerformanceSetting] = useRecoilState(fos.queryPerformanceSetting);
    

### readOnly#

Name | Type | Description  
---|---|---  
readOnly | `boolean` |   
      
    
    const [readOnly, setReadOnly] = useRecoilState(fos.readOnly);
    

### refreshGroupQuery#

Name | Type | Description  
---|---|---  
refreshGroupQuery | `number` |   
      
    
    const [refreshGroupQuery, setRefreshGroupQuery] = useRecoilState(fos.refreshGroupQuery);
    

### refresher#

Name | Type | Description  
---|---|---  
refresher | `number` |   
      
    
    const [refresher, setRefresher] = useRecoilState(fos.refresher);
    

### rootElementName#

Name | Type | Description  
---|---|---  
rootElementName | `string` |   
      
    
    const rootElementName = useRecoilValue(fos.rootElementName);
    

### rootElementNamePlural#

Name | Type | Description  
---|---|---  
rootElementNamePlural | `string` |   
      
    
    const rootElementNamePlural = useRecoilValue(fos.rootElementNamePlural);
    

### sampleFields#
    
    
    const sampleFields = useRecoilValue(fos.sampleFields);
    

### sampleSelectionStyle#

Name | Type | Description  
---|---|---  
sampleSelectionStyle | `plugins.fiftyone.state.SelectionStyle` |   
      
    
    const [sampleSelectionStyle, setSampleSelectionStyle] = useRecoilState(fos.sampleSelectionStyle);
    

### savedLookerOptions#
    
    
    const [savedLookerOptions, setSavedLookerOptions] = useRecoilState(fos.savedLookerOptions);
    

### savingFilters#

Name | Type | Description  
---|---|---  
savingFilters | `boolean` |   
      
    
    const [savingFilters, setSavingFilters] = useRecoilState(fos.savingFilters);
    

### schemaSearchResultList#
    
    
    const [schemaSearchResultList, setSchemaSearchResultList] = useRecoilState(fos.schemaSearchResultList);
    

### schemaSearchResults#
    
    
    const [schemaSearchResults, setSchemaSearchResults] = useRecoilState(fos.schemaSearchResults);
    

### schemaSearchTerm#

Name | Type | Description  
---|---|---  
schemaSearchTerm | `string` |   
      
    
    const [schemaSearchTerm, setSchemaSearchTerm] = useRecoilState(fos.schemaSearchTerm);
    

### schemaSelectedSettingsTab#

Name | Type | Description  
---|---|---  
schemaSelectedSettingsTab | `string` |   
      
    
    const [schemaSelectedSettingsTab, setSchemaSelectedSettingsTab] = useRecoilState(fos.schemaSelectedSettingsTab);
    

### searchMetaFilterState#
    
    
    const [searchMetaFilterState, setSearchMetaFilterState] = useRecoilState(fos.searchMetaFilterState);
    

### selectedLabelIds#

Name | Type | Description  
---|---|---  
selectedLabelIds | `Set < string >` `<` `string` `>` |   
      
    
    const selectedLabelIds = useRecoilValue(fos.selectedLabelIds);
    

### selectedLabelMap#

Name | Type | Description  
---|---|---  
selectedLabelMap | `plugins.fiftyone.state.SelectedLabelMap` |   
      
    
    const [selectedLabelMap, setSelectedLabelMap] = useRecoilState(fos.selectedLabelMap);
    

### selectedLabelTypes#

Name | Type | Description  
---|---|---  
selectedLabelTypes | `Record < string , SelectionType >` `<` `string` `,` `plugins.fiftyone.state.SelectionType` `>` |   
      
    
    const selectedLabelTypes = useRecoilValue(fos.selectedLabelTypes);
    

### selectedLabels#
    
    
    const [selectedLabels, setSelectedLabels] = useRecoilState(fos.selectedLabels);
    

### selectedPatchSamples#

Name | Type | Description  
---|---|---  
selectedPatchSamples | `Set < unknown >` `<` `unknown` `>` |   
      
    
    const selectedPatchSamples = useRecoilValue(fos.selectedPatchSamples);
    

### selectedSampleObjects#

Name | Type | Description  
---|---|---  
selectedSampleObjects | `Map < string , Sample >` `<` `string` `,` `plugins.fiftyone.state.Sample` `>` |   
      
    
    const [selectedSampleObjects, setSelectedSampleObjects] = useRecoilState(fos.selectedSampleObjects);
    

### selectedSamples#

Name | Type | Description  
---|---|---  
selectedSamples | `Map < string , SelectionType >` `<` `string` `,` `plugins.fiftyone.state.SelectionType` `>` |   
      
    
    const [selectedSamples, setSelectedSamples] = useRecoilState(fos.selectedSamples);
    

### selectedSavedViewState#

Name | Type | Description  
---|---|---  
selectedSavedViewState | `plugins.fiftyone.state.DatasetViewOption` |   
      
    
    const [selectedSavedViewState, setSelectedSavedViewState] = useRecoilState(fos.selectedSavedViewState);
    

### selectedViewName#

Name | Type | Description  
---|---|---  
selectedViewName | `string` |   
      
    
    const [selectedViewName, setSelectedViewName] = useRecoilState(fos.selectedViewName);
    

### sessionGroupSlice#

Name | Type | Description  
---|---|---  
sessionGroupSlice | `string` |   
      
    
    const [sessionGroupSlice, setSessionGroupSlice] = useRecoilState(fos.sessionGroupSlice);
    

### sessionSpaces#

Name | Type | Description  
---|---|---  
sessionSpaces | `plugins.fiftyone.state.SpaceNodeJSON` |   
      
    
    const [sessionSpaces, setSessionSpaces] = useRecoilState(fos.sessionSpaces);
    

### settingsModal#

Name | Type | Description  
---|---|---  
settingsModal.open | `boolean` |   
      
    
    const [settingsModal, setSettingsModal] = useRecoilState(fos.settingsModal);
    

### showMetadataState#

Name | Type | Description  
---|---|---  
showMetadataState | `boolean` |   
      
    
    const [showMetadataState, setShowMetadataState] = useRecoilState(fos.showMetadataState);
    

### showModalNavigationControls#

Name | Type | Description  
---|---|---  
showModalNavigationControls | `boolean` |   
      
    
    const [showModalNavigationControls, setShowModalNavigationControls] = useRecoilState(fos.showModalNavigationControls);
    

### showNestedFieldsState#

Name | Type | Description  
---|---|---  
showNestedFieldsState | `boolean` |   
      
    
    const [showNestedFieldsState, setShowNestedFieldsState] = useRecoilState(fos.showNestedFieldsState);
    

### showOverlays#

Name | Type | Description  
---|---|---  
showOverlays | `boolean` |   
      
    
    const [showOverlays, setShowOverlays] = useRecoilState(fos.showOverlays);
    

### sidebarPaths#
    
    
    const sidebarPaths = useRecoilValue(fos.sidebarPaths);
    

### sidebarSampleId#

Name | Type | Description  
---|---|---  
sidebarSampleId | `string` |   
      
    
    const sidebarSampleId = useRecoilValue(fos.sidebarSampleId);
    

### similarityMethods#

Name | Type | Description  
---|---|---  
similarityMethods.patches | `Array<` `[` `plugins.fiftyone.state.Method` `,` `string` `]` `>` |   
similarityMethods.samples | `Array<` `plugins.fiftyone.state.Method` `>` |   
      
    
    const similarityMethods = useRecoilValue(fos.similarityMethods);
    

### similarityParameters#

Name | Type | Description  
---|---|---  
similarityParameters | `plugins.fiftyone.state.SortBySimilarityParameters` |   
      
    
    const [similarityParameters, setSimilarityParameters] = useRecoilState(fos.similarityParameters);
    

### similaritySorting#

Name | Type | Description  
---|---|---  
similaritySorting | `boolean` |   
      
    
    const [similaritySorting, setSimilaritySorting] = useRecoilState(fos.similaritySorting);
    

### snackbarErrors#
    
    
    const [snackbarErrors, setSnackbarErrors] = useRecoilState(fos.snackbarErrors);
    

### snackbarLink#

Name | Type | Description  
---|---|---  
snackbarLink.link | `string` |   
snackbarLink.message | `string` |   
      
    
    const [snackbarLink, setSnackbarLink] = useRecoilState(fos.snackbarLink);
    

### snackbarMessage#

Name | Type | Description  
---|---|---  
snackbarMessage | `string` |   
      
    
    const [snackbarMessage, setSnackbarMessage] = useRecoilState(fos.snackbarMessage);
    

### stageDefinitions#
    
    
    const stageDefinitions = useRecoilValue(fos.stageDefinitions);
    

### stageInfo#

Name | Type | Description  
---|---|---  
stageInfo | `any` |   
      
    
    const [stageInfo, setStageInfo] = useRecoilState(fos.stageInfo);
    

### stateSubscription#

Name | Type | Description  
---|---|---  
stateSubscription | `string` |   
      
    
    const stateSubscription = useRecoilValue(fos.stateSubscription);
    

### targets#

Name | Type | Description  
---|---|---  
targets.defaults | `plugins.fiftyone.state.Targets` |   
targets.fields | `Any` |   
      
    
    const targets = useRecoilValue(fos.targets);
    

### theme#

Name | Type | Description  
---|---|---  
theme | `Union<` `'dark'` `,` `'light'` `>` |   
      
    
    const [theme, setTheme] = useRecoilState(fos.theme);
    

### themeConfig#

Name | Type | Description  
---|---|---  
themeConfig | `Union<` `'dark'` `,` `'light'` `,` `'browser'` `>` |   
      
    
    const themeConfig = useRecoilValue(fos.themeConfig);
    

### timeZone#

Name | Type | Description  
---|---|---  
timeZone | `string` |   
      
    
    const timeZone = useRecoilValue(fos.timeZone);
    

### tooltipCoordinates#

Name | Type | Description  
---|---|---  
tooltipCoordinates.bottom | `plugins.fiftyone.state.placement` |   
tooltipCoordinates.left | `plugins.fiftyone.state.placement` |   
tooltipCoordinates.right | `plugins.fiftyone.state.placement` |   
tooltipCoordinates.top | `plugins.fiftyone.state.placement` |   
      
    
    const [tooltipCoordinates, setTooltipCoordinates] = useRecoilState(fos.tooltipCoordinates);
    

### tooltipDetail#

Name | Type | Description  
---|---|---  
tooltipDetail | `plugins.fiftyone.state.PointInfo` `<` `plugins.fiftyone.state.BaseLabel` `>` |   
      
    
    const [tooltipDetail, setTooltipDetail] = useRecoilState(fos.tooltipDetail);
    

### view#
    
    
    const [view, setView] = useRecoilState(fos.view);
    

### viewCls#

Name | Type | Description  
---|---|---  
viewCls | `string` |   
      
    
    const [viewCls, setViewCls] = useRecoilState(fos.viewCls);
    

### viewCounter#

Name | Type | Description  
---|---|---  
viewCounter | `number` |   
      
    
    const [viewCounter, setViewCounter] = useRecoilState(fos.viewCounter);
    

### viewName#

Name | Type | Description  
---|---|---  
viewName | `string` |   
      
    
    const [viewName, setViewName] = useRecoilState(fos.viewName);
    

### viewSchemaState#

Name | Type | Description  
---|---|---  
viewSchemaState | `any` |   
      
    
    const [viewSchemaState, setViewSchemaState] = useRecoilState(fos.viewSchemaState);
    

### viewStateForm_INTERNAL#

This atom can be set to parameterize view changes

**See**

> for example usage

Name | Type | Description  
---|---|---  
viewStateForm_INTERNAL | `plugins.fiftyone.state.StateForm` |   
      
    
    const [viewStateForm_INTERNAL, setViewStateForm_INTERNAL] = useRecoilState(fos.viewStateForm_INTERNAL);
    

## Hooks#

### useActive3dSamplesMap#

fos.useActive3dSamplesMap()#
    

Return type:
    

`Record < string , ModalSample >` `<` `string` `,` `plugins.fiftyone.state.ModalSample` `>`

Resolved samples for the currently active 3D slices.

### useActive3dSlices#

fos.useActive3dSlices()#
    

Return type:
    

`Array<` `string` `>`

The 3D slice names currently included in the rendered scene.

### useActiveDirectSlices#

fos.useActiveDirectSlices()#
    

Return type:
    

`Array<` `string` `>`

Active non-FO3D 3D slices rendered alongside the scene.

### useActiveFo3dSlice#

fos.useActiveFo3dSlice()#
    

Return type:
    

`string`

Active FO3D slice currently driving the scene, if one is selected.

### useActiveModalFields#

fos.useActiveModalFields()#
    

Return type:
    

`[` `Array< string >` `,` `SetterOrUpdater < >` `]`

Hook which provides the modalâs current active paths, and a setter to update the paths.

### useActiveModalSampleValue#

fos.useActiveModalSampleValue(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`Union<` ```` `,` `plugins.fiftyone.state.T` `>`

Reads a single field value at `path` from the active modal sidebar sample.

**Returns**

The resolved value, or

> when the sample is
>     
> 
> unresolved or transiently absent for the active slice.

**Throws**

Any non-

> error from the underlying
>     
> 
> loadable (e.g. plain
    
    
      `SampleNotFound`
    
    or a thrown selector error).
    

### useActivityToast#

fos.useActivityToast()#
    

Return type:
    

`plugins.fiftyone.state.IActivityToast`

Hook which provides read and write access to the applicationâs ActivityToast through the `IActivityToast` interface.

### useAll3dSamplesMap#

fos.useAll3dSamplesMap()#
    

Return type:
    

`Record < string , ModalSample >` `<` `string` `,` `plugins.fiftyone.state.ModalSample` `>`

Resolved samples for every available 3D slice in the current modal context.

### useAll3dSlices#

fos.useAll3dSlices()#
    

Return type:
    

`Array<` `string` `>`

All available 3D slice names.

### useAssertedRecoilValue#

fos.useAssertedRecoilValue(_recoilValue_)#
    

Arguments:
    

  * **recoilValue** (`RecoilValue`)



Return type:
    

`plugins.fiftyone.state.T`

### useBeforeScreenshot#

fos.useBeforeScreenshot(_cb_)#
    

Arguments:
    

  * **cb** (`( )`)



Return type:
    

`void`

### useBrowserStorage#

fos.useBrowserStorage(_key_ , _initialValue_ , _useSessionStorage_ , _parseFn_)#
    

Arguments:
    

  * **key** (`string`)

  * **initialValue** (`Union`)

  * **useSessionStorage** (`boolean`)

  * **parseFn** (`Object`)

  * **parseFn.parse** (`( value : string )`)

  * **parseFn.stringify** (`( value : T )`)



Return type:
    

`readonly`

### useClearModal#

fos.useClearModal()#
    

A react hook that allows clearing the modal state.

**Example**
    
    
    function MyComponent() {
      const clearModal = useClearModal();
      return (
       <button onClick={clearModal}>Close Modal</button>
      )
    }
    

**Returns**

A function that clears the modal state.

> fos.clearModal()#
>     
> 
> Return type:
>     
> 
> `void`

### useCreateLooker#

fos.useCreateLooker(_isModal_ , _thumbnail_ , _options_ , _highlight_ , _enableTimeline_)#
    

Arguments:
    

  * **isModal** (`boolean`)

  * **thumbnail** (`boolean`)

  * **options** (`Omit`)

  * **highlight** (`( sample : Sample )`)

  * **enableTimeline** (`boolean`)



Return type:
    

`MutableRefObject < >` `<` `( args : )` `>`

### useCurrentDataset#

fos.useCurrentDataset()#
    

Return type:
    

`plugins.fiftyone.state.Dataset`

Get the current dataset.

**Returns**

The current dataset state

### useCurrentDatasetId#

fos.useCurrentDatasetId()#
    

Return type:
    

`string`

Get the current dataset ID.

**Returns**

The current dataset ID, or null if no dataset is selected

### useCurrentDatasetName#

fos.useCurrentDatasetName()#
    

Return type:
    

`string`

Get the current dataset name.

**Returns**

The current dataset name

### useCurrentSampleId#

fos.useCurrentSampleId()#
    

Return type:
    

`string`

Gets the current sample ID.

### useDebounceCallback#

fos.useDebounceCallback(_func_ , _delay_ , _options_)#
    

Arguments:
    

  * **func** (`T`)

  * **delay** (`number`)

  * **options** (`DebounceSettings`)



Return type:
    

`plugins.fiftyone.state.DebouncedState` `<` `plugins.fiftyone.state.T` `>`

### useDeferrer#

fos.useDeferrer()#
    

Return type:
    

`Object`

### useDimensions#

fos.useDimensions()#
    

Return type:
    

`Object`

### useDisabledCheckboxPaths#

fos.useDisabledCheckboxPaths()#
    

Return type:
    

`Set < string >` `<` `string` `>`

Returns the set of field paths that are disabled in the sidebar checkbox list. Includes unsupported field types (DictField, VectorField, etc.) and frame fields that are not labels.

### useElementsCount#

fos.useElementsCount(_modal_)#
    

Arguments:
    

  * **modal** (`boolean`)



Return type:
    

`number`

Returns the last settled element count for the current dynamic group without suspending. Uses the stable groupByFieldValue so the count stays frozen while modalSample is transitioning between pages.

### useEventHandler#

fos.useEventHandler(_target_ , _eventType_ , _handler_ , _options_)#
    

Arguments:
    

  * **target** (`EventTarget`)

  * **eventType** (`string`)

  * **handler** (`( event : any )`)

  * **options** (`Union`)



Return type:
    

`void`

### useExpandSample#

fos.useExpandSample(_store_)#
    

Arguments:
    

  * **store** ()




Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useFo3dContent#

fos.useFo3dContent()#
    

Return type:
    

`unknown`

Parsed FO3D scene content cached for the active scene sample.

### useFollow#

fos.useFollow(_leaderRef_ , _followerRef_ , _api_)#
    

Arguments:
    

  * **leaderRef** (`any`)

  * **followerRef** (`any`)

  * **api** (`any`)



Return type:
    

`void`

### useGetKeypointSkeleton#

fos.useGetKeypointSkeleton()#
    

Hook which provides a function to get the default keypoint skeleton for a given field.

> fos.getKeypointSkeleton()#
>     
> 
> Arguments:
>     
> 
>   * **args** (`[ field ]`)
> 
> 

> Return type:
>     
> 
> `plugins.fiftyone.state.KeypointSkeleton`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useGridCustomRendererFailover#

fos.useGridCustomRendererFailover(_datasetName_)#
    

Arguments:
    

  * **datasetName** (`string`)



Return type:
    

`Object`

React view onto the external fail-open store.

`useSyncExternalStore` bridges React to this module-level source of truth, while selectors and other non-React code can still read it synchronously.

When a dataset name is provided, the disable/banner state is scoped to that dataset. The forced subscription remains shared because the sync repair path still applies to the entire tab.

### useGridEntries#

fos.useGridEntries()#
    

Return type:
    

`[` `Array< SidebarEntry >` `,` `( entries : )` `]`

### useGroupByFieldValue#

fos.useGroupByFieldValue()#
    

Return type:
    

`string`

Returns the last settled groupByFieldValue without ever suspending.

groupByFieldValue derives from modalSample (a graphQLSelector) and suspends during sample transitions. This hook holds the previous value steady while the next one loads, preventing Suspense boundaries from triggering on every sample navigation. Returns undefined until the first value has settled.

### useGroupSlices#

fos.useGroupSlices(_mediaTypes_)#
    

Arguments:
    

  * **mediaTypes** (`Array`)



Return type:
    

`Array<` `string` `>`

Returns the names of dataset-level group slices whose media type matches any of the provided types.

**Returns**

Slice names matching the requested media types, in dataset order.

### useHas3dSlice#

fos.useHas3dSlice()#
    

Return type:
    

`boolean`

Whether the current modal context exposes any 3D slice.

### useHasMultiple3dSlices#

fos.useHasMultiple3dSlices()#
    

Return type:
    

`boolean`

Whether more than one 3D slice is available.

### useHashChangeHandler#

fos.useHashChangeHandler(_handler_)#
    

Arguments:
    

  * **handler** (`any`)



Return type:
    

`void`

### useHelpPanel#

fos.useHelpPanel()#
    

Return type:
    

`Object`

### useHover#

fos.useHover()#
    

Return type:
    

`[` `MutableRefObject < any >` `,` `boolean` `]`

### useHoveredSample#

fos.useHoveredSample(_sample_ , _args_)#
    

Arguments:
    

  * **sample** (`Sample`)

  * **args** (`Object`)

  * **args.clear** (`( )`)

  * **args.update** (`( )`)



Return type:
    

`Object`

### useInteraction3dSample#

fos.useInteraction3dSample()#
    

Return type:
    

`plugins.fiftyone.state.ModalSample`

Representative sample used for 3D interaction-driven behavior.

### useIs3dPinned#

fos.useIs3dPinned()#
    

Return type:
    

`boolean`

Whether the 3D slice selection is pinned to a specific slice.

### useIs3dVisible#

fos.useIs3dVisible()#
    

Return type:
    

`boolean`

Whether the 3D viewer is currently visible.

### useIs3dVisibleSetting#

fos.useIs3dVisibleSetting()#
    

Return type:
    

`boolean`

Persisted user preference for showing the 3D viewer.

### useIsGroupCarouselVisible#

fos.useIsGroupCarouselVisible()#
    

Return type:
    

`boolean`

Whether the carousel is visible. Always false in annotate mode.

### useIsGroupDataset#

fos.useIsGroupDataset()#
    

Return type:
    

`boolean`

Whether the current dataset is a grouped dataset.

**Returns**

True if the current dataset is a group dataset

### useIsGroupMain2dViewerVisible#

fos.useIsGroupMain2dViewerVisible()#
    

Return type:
    

`boolean`

Whether the 2D viewer is visible. In annotate mode, suppressed when the 3D viewer is also visible so only one viewer shows at a time.

### useJSONPanel#

fos.useJSONPanel()#
    

Return type:
    

`Object`

Manage the JSON panel state and events.

**Example**
    
    
    function MyComponent() {
      const jsonPanel = useJSONPanel();
    
      return jsonPanel.isOpen && (
         <JSONPanel
           containerRef={jsonPanel.containerRef}
           onClose={() => jsonPanel.close()}
           onCopy={() => jsonPanel.copy()}
         />
       )
    }
    

### useKeyDown#

fos.useKeyDown(_key_ , _handler_ , _deps_)#
    

Arguments:
    

  * **key** (`string`)

  * **handler** (`( down : boolean , e : KeyboardEvent )`)

  * **deps** (`DependencyList`)



Return type:
    

`void`

a react hook that calls the handler when a given key is down

### useKeydownHandler#

fos.useKeydownHandler(_handler_)#
    

Arguments:
    

  * **handler** (`( e : KeyboardEvent )`)



Return type:
    

`void`

### useLookerOptions#

fos.useLookerOptions(_modal_)#
    

Arguments:
    

  * **modal** (`boolean`)



Return type:
    

`Partial < Omit >` `<` `Omit < , >` `>`

### useLookerStore#

fos.useLookerStore()#
    

Return type:
    

`plugins.fiftyone.state.LookerStore` `<` `plugins.fiftyone.state.Lookers` `>`

### useModalExplorEntries#

fos.useModalExplorEntries()#
    

Return type:
    

`[` `Array< SidebarEntry >` `,` `( entries : )` `]`

### useModalLookerOptions#

fos.useModalLookerOptions(_withFilter_)#
    

Arguments:
    

  * **withFilter** (`boolean`)



Return type:
    

`Partial < Omit >` `<` `Omit < , >` `>`

Gets the looker options for the modal.

### useModalMediaPath#

fos.useModalMediaPath()#
    

Return type:
    

`string`

Returns the current media path in the modal.

### useModalMode#

fos.useModalMode()#
    

Return type:
    

`plugins.fiftyone.state.ModalMode`

Get the current modal mode.

### useModalModeController#

fos.useModalModeController()#
    

Return type:
    

`plugins.fiftyone.state.ModalModeController`

Hook which provides a `ModalModeController`.

### useModalSample#

fos.useModalSample()#
    

Return type:
    

`plugins.fiftyone.state.ModalSample`

Get the current modal sample data.

If the modal is not open, or the sample is being loaded, this hook will return `undefined`.

### useModalSampleSchema#

fos.useModalSampleSchema()#
    

Return type:
    

`plugins.fiftyone.state.Schema`

Get the current modal sample schema.

### useModalViewport#

fos.useModalViewport()#
    

Return type:
    

`plugins.fiftyone.state.ModalViewportState`

Gets the saved modal viewport (zoom/pan) state.

### useMutation#

fos.useMutation(_hasPermission_ , _mutation_)#
    

Arguments:
    

  * **hasPermission** (`boolean`)

  * **mutation** (`string`)



Return type:
    

`plugins.fiftyone.state.CanPerformActionReturnType`

### useNon3dSlices#

fos.useNon3dSlices()#
    

Return type:
    

`Array<` `string` `>`

All available non-3D slice names.

### useNotification#

fos.useNotification()#
    

fos.notification()#
    

Arguments:
    

  * **options** (`NotificationOption`)



Return type:
    

`void`

### useObserve#

fos.useObserve(_target_ , _handler_)#
    

Arguments:
    

  * **target** (`any`)

  * **handler** (`any`)



Return type:
    

`void`

### useOnSelectLabel#

fos.useOnSelectLabel()#
    

fos.onSelectLabel()#
    

Arguments:
    

  * **args** (`[ SelectEvent ]`)



Return type:
    

`Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useOutsideClick#

fos.useOutsideClick(_ref_ , _handler_ , _eventName_)#
    

Arguments:
    

  * **ref** (`MutableRefObject`)

  * **handler** (`MouseEventHandler`)

  * **eventName** (`string`)



Return type:
    

`void`

### usePanel#

fos.usePanel(_name_ , _atom_)#
    

Arguments:
    

  * **name** (`any`)

  * **atom** (`any`)



Return type:
    

`Object`

### usePinned3dSlice#

fos.usePinned3dSlice()#
    

Return type:
    

`string`

Slice name currently pinned for 3D rendering, if any.

### usePreferredGroupAnnotationSlice#

fos.usePreferredGroupAnnotationSlice()#
    

Return type:
    

`[` `string` `,` `SetAtom < , void >` `]`

Get and set the preferred annotation slice for grouped datasets. Returns [preferredSlice, setPreferredSlice].

### useQueryPerformance#

fos.useQueryPerformance()#
    

Return type:
    

`Object`

### useQueryPerformanceSampleLimit#

fos.useQueryPerformanceSampleLimit()#
    

Return type:
    

`number`

Hook which returns the sample limit for dataset query performance.

### useRealFo3dSlices#

fos.useRealFo3dSlices()#
    

Return type:
    

`Array<` `string` `>`

Available 3D slices whose media resolves to FO3D files.

### useRefresh#

fos.useRefresh()#
    

fos.refresh()#
    

Arguments:
    

  * **args** (`[ ]`)



Return type:
    

`void`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useRefreshSample#

fos.useRefreshSample()#
    

Refresh a sample in both the modal and the grid.

> fos.refreshSample()#
>     
> 
> Arguments:
>     
> 
>   * **sample** (`Sample`)
> 
> 

> Return type:
>     
> 
> `void`

### useRenderConfig3dActions#

fos.useRenderConfig3dActions()#
    

Return type:
    

`plugins.fiftyone.state.RenderConfig3dActions`

3D render config mutation actions.

### useRenderConfig3dImperativeState#

fos.useRenderConfig3dImperativeState()#
    

Return type:
    

`plugins.fiftyone.state.RenderConfig3dImperativeState`

Imperative 3D render state queries for event handlers and callbacks.

### useRenderConfig3dState#

fos.useRenderConfig3dState()#
    

Return type:
    

`plugins.fiftyone.state.RenderConfig3dState`

Suspense-compatible 3D render state for React rendering.

### useReset#

fos.useReset()#
    

Return type:
    

`SetterOrUpdater < >` `<` `Array< Stage >` `>`

**Deprecated**

use

> instead

### useResetExtendedSelection#

fos.useResetExtendedSelection()#
    

fos.resetExtendedSelection()#
    

Arguments:
    

  * **args** (`[ ]`)



Return type:
    

`void`

Returns a function that executes an atomic transaction for updating Recoil state.

### useResizeHandler#

fos.useResizeHandler(_handler_)#
    

Arguments:
    

  * **handler** (`any`)



Return type:
    

`void`

### useRetryController#

fos.useRetryController(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`RetryConfig`)



Return type:
    

`plugins.fiftyone.state.RetryController`

Hook which returns a `RetryController` to support retryable flows.

### useSampleSchema#

fos.useSampleSchema()#
    

Return type:
    

`plugins.fiftyone.state.Schema`

Get the current sample schema.

**Returns**

The field schema for the sample space

### useSaveModalViewport#

fos.useSaveModalViewport()#
    

Return type:
    

`SetAtom < , unknown >` `<` `Array< unknown >` `,` `unknown` `>`

Setter for persisting the modal viewport (zoom/pan) state.

### useSavedViews#

fos.useSavedViews()#
    

Return type:
    

`Object`

### useSceneSample3d#

fos.useSceneSample3d()#
    

Return type:
    

`plugins.fiftyone.state.ModalSample`

Sample currently used to render the visible 3D scene.

### useSchemaSettings#

fos.useSchemaSettings()#
    

Return type:
    

`Object`

### useScreenshot#

fos.useScreenshot(_context_)#
    

Arguments:
    

  * **context** ()




### useScrollHandler#

fos.useScrollHandler(_handler_)#
    

Arguments:
    

  * **handler** (`any`)



Return type:
    

`void`

### useSearchSchemaFields#

fos.useSearchSchemaFields(_mergedSchema_)#
    

Arguments:
    

  * **mergedSchema** (`Any`)



Return type:
    

`Object`

### useSelectSample#

fos.useSelectSample()#
    

fos.selectSample()#
    

Arguments:
    

  * **args** (`[ sampleId , altKey ]`)



Return type:
    

`Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useSelectedMediaFieldGrid#

fos.useSelectedMediaFieldGrid()#
    

Return type:
    

`string`

Hook to retrieve the selected media field for the grid view.

**Returns**

The selected media field state for the grid

### useSelectedMediaFieldModal#

fos.useSelectedMediaFieldModal()#
    

Return type:
    

`string`

Hook to retrieve the selected media field for the modal view.

**Returns**

The selected media field state for the modal

### useSession#

fos.useSession(_setter_ , _ref_)#
    

Arguments:
    

  * **setter** (`Setter`)

  * **ref** (`Session`)



Return type:
    

`void`

### useSessionRef#

fos.useSessionRef()#
    

Return type:
    

`plugins.fiftyone.state.Session`

### useSessionSetter#

fos.useSessionSetter()#
    

fos.sessionSetter()#
    

Arguments:
    

  * **key** (`K`)

  * **value**



Return type:
    

`void`

### useSessionSpaces#

fos.useSessionSpaces()#
    

Return type:
    

`Array<` `any` `>`

### useSetDataset#

fos.useSetDataset()#
    

Return type:
    

`SetterOrUpdater < string >` `<` `string` `>`

### useSetExpandedSample#

fos.useSetExpandedSample()#
    

fos.setExpandedSample()#
    

Arguments:
    

  * **selector** (`ModalSelector`)



Return type:
    

`Promise < void >` `<` `void` `>`

### useSetGroupSlice#

fos.useSetGroupSlice()#
    

Return type:
    

`SetterOrUpdater < string >` `<` `string` `>`

### useSetModalState#

fos.useSetModalState()#
    

Initializer that applys relevant grid settings to the modal, e.g. sidebar checkboxes. If no navigation is provided, next/previous in the modal is disabled

> fos.setModalState()#
>     
> 
> Arguments:
>     
> 
>   * **args** (`[ navigation ]`)
> 
> 

> Return type:
>     
> 
> `Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useSetSelected#

fos.useSetSelected()#
    

Return type:
    

`SetterOrUpdater < Map >` `<` `Map < string , SelectionType >` `>`

### useSetSelectedFieldsStage#

fos.useSetSelectedFieldsStage()#
    

Return type:
    

`Object`

**Returns**

a callback to set the selectedFields stage

### useSetSelectedLabels#

fos.useSetSelectedLabels()#
    

Return type:
    

`SetterOrUpdater < >` `<` `Array< SelectedLabel >` `>`

### useSetSessionColorScheme#

fos.useSetSessionColorScheme()#
    

Return type:
    

`SetterOrUpdater < ColorSchemeInput >` `<` `plugins.fiftyone.state.ColorSchemeInput` `>`

### useSetSidebarExpanded#

fos.useSetSidebarExpanded(_params_)#
    

Arguments:
    

  * **params** (`SidebarExpandedParams`)



Return type:
    

`SetterOrUpdater < boolean >` `<` `boolean` `>`

Returns a setter for the expanded state of the given sidebar path. Use this when the component only needs to write, not read.

**Example**
    
    
    const setExpanded = useSetSidebarExpanded({ path: "ground_truth", modal: false });
    setExpanded(true);
    

### useSetSpaces#

fos.useSetSpaces()#
    

Return type:
    

`SetterOrUpdater < SpaceNodeJSON >` `<` `plugins.fiftyone.state.SpaceNodeJSON` `>`

### useSetView#

fos.useSetView()#
    

Return type:
    

`SetterOrUpdater < >` `<` `Array< Stage >` `>`

### useSidebarExpanded#

fos.useSidebarExpanded(_params_)#
    

Arguments:
    

  * **params** (`SidebarExpandedParams`)



Return type:
    

`boolean`

Returns whether the given sidebar path is currently expanded.

Prefer this over reading `fos.sidebarExpanded` directly so that call sites remain decoupled from the underlying recoil atom.

### useSidebarExpandedState#

fos.useSidebarExpandedState(_params_)#
    

Arguments:
    

  * **params** (`SidebarExpandedParams`)



Return type:
    

`[` `boolean` `,` `( value : )` `]`

Returns `[expanded, setExpanded]` for the given sidebar path â the standard read/write accessor for toggling field expansion.

**Example**
    
    
    const [expanded, setExpanded] = useSidebarExpandedState({ path, modal });
    setExpanded((v) => !v);
    

### useSimilarityType#

fos.useSimilarityType(_props_)#
    

Arguments:
    

  * **props** (`SimilarityTypeProp`)



Return type:
    

`Object`

### useStableActive3dSamplesMap#

fos.useStableActive3dSamplesMap()#
    

Return type:
    

`Record < string , ModalSample >` `<` `string` `,` `plugins.fiftyone.state.ModalSample` `>`

Like useActive3dSamplesMap but holds the last settled value while loading. Returns {} before the first value settles.

### useStableActiveFo3dSlice#

fos.useStableActiveFo3dSlice()#
    

Return type:
    

`string`

Like useActiveFo3dSlice but holds the last settled value while loading. Returns null before the first value settles (same as selector default).

### useStableAll3dSamplesMap#

fos.useStableAll3dSamplesMap()#
    

Return type:
    

`Record < string , ModalSample >` `<` `string` `,` `plugins.fiftyone.state.ModalSample` `>`

Like useAll3dSamplesMap but holds the last settled value while loading. Returns {} before the first value settles.

### useStableInteraction3dSample#

fos.useStableInteraction3dSample()#
    

Return type:
    

`plugins.fiftyone.state.ModalSample`

Like useInteraction3dSample but holds the last settled value while loading. Returns undefined before the first value settles â callers must guard.

### useStableModalSample#

fos.useStableModalSample()#
    

Return type:
    

`plugins.fiftyone.state.ModalSample`

Like `useModalSample` but holds the last settled value across loading transitions so consumers donât lose the sample mid-navigation. Returns `undefined` before the first value settles. Treats `GroupSampleNotFound` as a non-error (sparse groups legitimately lack a sample on the active slice); all other errors still bubble.

### useStableRealFo3dSlices#

fos.useStableRealFo3dSlices()#
    

Return type:
    

`Array<` `string` `>`

Like useRealFo3dSlices but holds the last settled value while loading. Returns [] before the first value settles.

### useStableSceneSample3d#

fos.useStableSceneSample3d()#
    

Return type:
    

`plugins.fiftyone.state.ModalSample`

Like useSceneSample3d but holds the last settled value while the selector is re-fetching (e.g. during group-sample navigation). The 3D scene stays visible instead of flickering to âPixelatingâ¦â. Returns undefined before the first value settles â callers must guard (return null when undefined).

### useTimeout#

fos.useTimeout(_time_)#
    

Arguments:
    

  * **time** (`number`)



Return type:
    

`boolean`

### useToClips#

fos.useToClips()#
    

fos.toClips()#
    

Arguments:
    

  * **args** (`[ field ]`)



Return type:
    

`Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useToEvaluationPatches#

fos.useToEvaluationPatches()#
    

fos.toEvaluationPatches()#
    

Arguments:
    

  * **args** (`[ evaluation ]`)



Return type:
    

`Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useToPatches#

fos.useToPatches()#
    

fos.toPatches()#
    

Arguments:
    

  * **args** (`[ field ]`)



Return type:
    

`Promise < void >` `<` `void` `>`

Returns a function that will run the callback that was passed when calling this hook. Useful for accessing Recoil state in response to events.

### useTooltip#

fos.useTooltip()#
    

Return type:
    

`Object`

### useUnboundState#

fos.useUnboundState(_value_)#
    

Arguments:
    

  * **value** (`State`)



Return type:
    

`plugins.fiftyone.state.State`

The hook can be used to get the latest value of the state without re-rendering the component.

### useUnboundStateRef#

fos.useUnboundStateRef(_value_)#
    

Arguments:
    

  * **value** (`State`)



Return type:
    

`MutableRefObject < State >` `<` `plugins.fiftyone.state.State` `>`

### useUpdateSamples#

fos.useUpdateSamples()#
    

fos.updateSamples()#
    

Arguments:
    

  * **samples** (`Array`)



Return type:
    

`void`

### useWindowSize#

fos.useWindowSize()#
    

Return type:
    

`Object`

## Functions#

### activeField#

fos.activeField(_params_)#
    

Arguments:
    

  * **params** (`Object`)

  * **params.modal** (`boolean`) â Whether the field is in a modal or not

  * **params.path** (`string`) â The path of the field



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Get or set the active state of a field.

### activeFields#

fos.activeFields(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.expanded** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### activeLabelFields#

fos.activeLabelFields(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.space** (`SPACE`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### activeLabelPaths#

fos.activeLabelPaths(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.space** (`SPACE`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### activeLabels#

fos.activeLabels(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.expanded** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< LabelData >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### aggregation#

fos.aggregation(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.isQueryPerformance** (`boolean`)

  * **param.mixed** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , , , , , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### aggregationQuery#

fos.aggregationQuery(_parameter_)#
    

Arguments:
    

  * **parameter** (`Object`)

  * **parameter.dynamicGroup** (`SerializableParam`)

  * **parameter.extended** (`boolean`)

  * **parameter.isQueryPerformance** (`boolean`)

  * **parameter.mixed** (`boolean`)

  * **parameter.modal** (`boolean`)

  * **parameter.paths** (`Array`)

  * **parameter.root** (`boolean`)

  * **parameter.useSelection** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Array< Aggregation >` `>`

GraphQL Selector Family for Aggregations.

### aggregations#

fos.aggregations(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.isQueryPerformance** (`boolean`)

  * **param.mixed** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.paths** (`Array`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< Aggregation >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### appConfigOption#

fos.appConfigOption(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.key** (`string`)

  * **param.modal** (`boolean`)



Return type:
    

`RecoilState < any >` `<` `any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### boolExcludeAtom#

fos.boolExcludeAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### boolIsMatchingAtom#

fos.boolIsMatchingAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### boolean#

fos.boolean(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `( value : boolean )` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### booleanCountResults#

fos.booleanCountResults(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Object` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### booleanResults#

fos.booleanResults(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Object` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### booleanSelectedValuesAtom#

fos.booleanSelectedValuesAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### boundedCount#

fos.boundedCount(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### bounds#

fos.bounds(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `[ number , number ]` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### boundsAtom#

fos.boundsAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < Range >` `<` `plugins.fiftyone.state.Range` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### buildSchema#

fos.buildSchema(_sampleFields_ , _frameFields_)#
    

Arguments:
    

  * **sampleFields** (`Array`)

  * **frameFields** (`Array`)



Return type:
    

`plugins.fiftyone.state.Schema`

### collapseFields#

fos.collapseFields(_paths_)#
    

Arguments:
    

  * **paths** (`any`)



Return type:
    

`Array<` `plugins.fiftyone.state.StrictField` `>`

### computeCoordinates#

fos.computeCoordinates(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`[ number , number ]`)



Return type:
    

`Object`

### convertTargets#

fos.convertTargets(_targets_)#
    

Arguments:
    

  * **targets** (`Array`)



Return type:
    

`Any`

### count#

fos.count(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.lightning** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)

  * **param.value** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### countValues#

fos.countValues(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### counts#

fos.counts(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### cropToContent#

fos.cropToContent(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### cumulativeCounts#

fos.cumulativeCounts(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.embeddedDocType** (`Union`)

  * **param.extended** (`boolean`)

  * **param.ftype** (`Union`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### cumulativeValues#

fos.cumulativeValues(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.embeddedDocType** (`Union`)

  * **param.extended** (`boolean`)

  * **param.ftype** (`Union`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### currentSlice#

fos.currentSlice(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### currentSlices#

fos.currentSlices(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### dbPath#

fos.dbPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### deferrer#

fos.deferrer(_initialized_)#
    

Arguments:
    

  * **initialized** ()




### dismissGridCustomRendererFailoverBanner#

fos.dismissGridCustomRendererFailoverBanner(_datasetName_)#
    

Arguments:
    

  * **datasetName** (`string`)



Return type:
    

`void`

Hides the warning banner for a dataset without clearing fail-open mode. Dismissing the banner is purely a UI choice and should not re-enable the crashing renderer for that dataset.

### distribution#

fos.distribution(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , , , , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### dynamicGroupPageSelector#

fos.dynamicGroupPageSelector(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.value** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `( cursor : number , pageSize : number )` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### dynamicGroupsElementCount#

fos.dynamicGroupsElementCount(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.value** (`SerializableParam`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < any >` `<` `any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### dynamicGroupsViewMode#

fos.dynamicGroupsViewMode(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Union< , , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### dynamicGroupsViewModeStore#

fos.dynamicGroupsViewModeStore(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Union< , , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### ensureColorScheme#

fos.ensureColorScheme(_colorScheme_ , _appConfig_)#
    

Arguments:
    

  * **colorScheme** (`any`)

  * **appConfig** (`Object`)

  * **appConfig.colorBy** (`ColorBy`)

  * **appConfig.colorPool** (`readonly`)

  * **appConfig.colorscale** (`string`)

  * **appConfig.multicolorKeypoints** (`boolean`)

  * **appConfig.showSkeletons** (`boolean`)



Return type:
    

`plugins.fiftyone.state.ColorSchemeInput`

### excludedPathsState#

fos.excludedPathsState(_param_)#
    

Arguments:
    

  * **param** (`SerializableParam`)



Return type:
    

`RecoilState < unknown >` `<` `unknown` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### expandPath#

fos.expandPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### falseAtom#

fos.falseAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.isFiltering** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### field#

fos.field(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < Field >` `<` `plugins.fiftyone.state.Field` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fieldHasVisibilitySetting#

fos.fieldHasVisibilitySetting(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fieldIsFiltered#

fos.fieldIsFiltered(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fieldPath#

fos.fieldPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fieldPaths#

fos.fieldPaths(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.embeddedDocType** (`Union`)

  * **param.ftype** (`Union`)

  * **param.path** (`string`)

  * **param.space** (`SPACE`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fieldSchema#

fos.fieldSchema(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.space** (`SPACE`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < Schema >` `<` `plugins.fiftyone.state.Schema` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fieldType#

fos.fieldType(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.path** (`string`)

  * **param.useListSubfield** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fields#

fos.fields(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.embeddedDocType** (`Union`)

  * **param.ftype** (`Union`)

  * **param.path** (`string`)

  * **param.space** (`SPACE`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< Field >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### fieldsMatcher#

fos.fieldsMatcher(_fields_ , _matcher_ , _present_ , _prefix_)#
    

Arguments:
    

  * **fields** (`Array`)

  * **matcher** (`( field : StrictField )`)

  * **present** (`Set`)

  * **prefix** (`string`)



Return type:
    

`Array<` `string` `>`

### filter#

fos.filter(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < Filter >` `<` `plugins.fiftyone.state.Filter` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### filterFields#

fos.filterFields(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### filterPaths#

fos.filterPaths(_paths_ , _schema_)#
    

Arguments:
    

  * **paths** (`Array`)

  * **schema** (`Schema`)



Return type:
    

`Array<` `string` `>`

### filterSearch#

fos.filterSearch(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Object` `>`

Given a field path, return a set a field filters and index name that would result in a optimized IXSCAN, if possible

### filterView#

fos.filterView(_stages_)#
    

Arguments:
    

  * **stages** (`Array`)



Return type:
    

`string`

### gatheredPaths#

fos.gatheredPaths(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.embeddedDocType** (`Union`)

  * **param.ftype** (`Union`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< any >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### generateBooleanSelectorFamily#

fos.generateBooleanSelectorFamily(_key_)#
    

Arguments:
    

  * **key** ()




Returns a function which returns a memoized atom for each unique parameter value.

### generateSelectorFamily#

fos.generateSelectorFamily(_key_)#
    

Arguments:
    

  * **key** ()




Returns a function which returns a memoized atom for each unique parameter value.

### getBrowserStorageEffectForKey#

fos.getBrowserStorageEffectForKey(_key_ , _props_)#
    

> param key:
>     
> 
> param props:
>     
> 
> param props.map:
>     
> 
> param props.prependDatasetNameInKey:
>     
> 
> If true, prepends the dataset name to the storage key.

This allows per-dataset storage isolation. Defaults to false
    

param props.sessionStorage:
    

If true, uses sessionStorage instead of localStorage. Defaults to false

param props.useJsonSerialization:
    

If true, uses JSON.stringify/parse for serialization.

Otherwise uses simple string conversion. Defaults to false
    

param props.valueClass:
    

The type of value being stored. Affects how the value is serialized/deserialized.

Options: âstringâ, âstringArrayâ, ânumberâ, âbooleanâ. Defaults to âstringâ
    

type key:
    

string

type props:
    

Object

type props.map:
    

( value : unknown )

type props.prependDatasetNameInKey:
    

boolean

type props.sessionStorage:
    

boolean

type props.useJsonSerialization:
    

boolean

type props.valueClass:
    

Union< , , , >

rtype:
    

`AtomEffect < T >` `<` `plugins.fiftyone.state.T` `>`

Recoil effect that syncs atom state with browser storage (localStorage or sessionStorage). Automatically loads the value from storage on initialization and saves it on every set.

**Returns**

A Recoil atom effect that syncs the atom with browser storage

### getCurrentEnvironment#

fos.getCurrentEnvironment()#
    

Return type:
    

`default`

### getEmbeddedLabelFields#

fos.getEmbeddedLabelFields(_fields_ , _prefix_)#
    

Arguments:
    

  * **fields** (`Array`)

  * **prefix** (`string`)



Return type:
    

`Array<` `string` `>`

### getEnvironment#

fos.getEnvironment()#
    

Return type:
    

`default`

### getGridCustomRendererFailover#

fos.getGridCustomRendererFailover(_datasetName_)#
    

Arguments:
    

  * **datasetName** (`string`)



Return type:
    

`plugins.fiftyone.state.GridCustomRendererFailure`

Returns the recorded failure for a dataset in the current browser session.

### getGridCustomRendererFailoverForcedSubscription#

fos.getGridCustomRendererFailoverForcedSubscription()#
    

Return type:
    

`string`

Returns the replacement synced subscription used after a renderer crash. The disable state is dataset-scoped, but subscription repair still happens at the tab level because the poisoned sync channel is shared by the whole app.

### getGridCustomRendererFailoverSnapshot#

fos.getGridCustomRendererFailoverSnapshot()#
    

Return type:
    

`plugins.fiftyone.state.GridCustomRendererFailoverSnapshot`

Returns the current fail-open snapshot for this browser session.

### getLabelFields#

fos.getLabelFields(_fields_ , _prefix_)#
    

Arguments:
    

  * **fields** (`Array`)

  * **prefix** (`string`)



Return type:
    

`Array<` `string` `>`

### getNormalizedUrls#

fos.getNormalizedUrls(_urls_)#
    

Arguments:
    

  * **urls** (`Union`)



Return type:
    

`Any`

### getQueryPerformancePath#

fos.getQueryPerformancePath()#
    

Return type:
    

`Object`

### getSampleSrc#

fos.getSampleSrc(_url_)#
    

Arguments:
    

  * **url** (`string`)



Return type:
    

`string`

### getSessionRef#

fos.getSessionRef()#
    

Return type:
    

`plugins.fiftyone.state.Session`

### getStageKwarg#

fos.getStageKwarg(_stage_ , _key_)#
    

Arguments:
    

  * **stage** (`Stage`)

  * **key** (`string`)



Return type:
    

`plugins.fiftyone.state.T`

Helper to extract a kwarg value from a view stageâs kwargs array. kwargs are stored as arrays of [key, value] tuples.

### gridSortByStore#

fos.gridSortByStore(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`RecoilState < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### gridSortDescendingStore#

fos.gridSortDescendingStore(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### groupFilter#

fos.groupFilter(_field_)#
    

Arguments:
    

  * **field** (`StrictField`)



Return type:
    

`boolean`

### groupHasSampleOnSlice#

fos.groupHasSampleOnSlice(_parameter_)#
    

Arguments:
    

  * **parameter** (`Object`)

  * **parameter.groupId** (`string`)

  * **parameter.slice** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

### groupIsEmpty#

fos.groupIsEmpty(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.group** (`string`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### groupLength#

fos.groupLength(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.group** (`string`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### groupSamples#

fos.groupSamples(_parameter_)#
    

Arguments:
    

  * **parameter** (`Object`)

  * **parameter.count** (`number`)

  * **parameter.paginationData** (`boolean`)

  * **parameter.slices** (`Array`)



Return type:
    

`RecoilState < >` `<` `Array< ModalSample >` `>`

### groupShown#

fos.groupShown(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.group** (`string`)

  * **param.loading** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### groupStatistics#

fos.groupStatistics(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Union< , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### hasFilters#

fos.hasFilters(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### hasVisibility#

fos.hasVisibility(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### helperFunction#

fos.helperFunction(_value_ , _exclude_ , _start_ , _end_ , _none_ , _inf_ , _ninf_ , _nan_)#
    

Arguments:
    

  * **value** (`Union`)

  * **exclude** (`boolean`)

  * **start** (`number`)

  * **end** (`number`)

  * **none** (`boolean`)

  * **inf** (`boolean`)

  * **ninf** (`boolean`)

  * **nan** (`boolean`)



Return type:
    

`boolean`

### hiddenFieldLabels#

fos.hiddenFieldLabels(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### histogramValues#

fos.histogramValues(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### imaVidLookerState#

fos.imaVidLookerState(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`RecoilState < any >` `<` `any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### imaVidStoreKey#

fos.imaVidStoreKey(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.groupByFieldValue** (`string`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### indexedPaths#

fos.indexedPaths(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.path** (`string`)

  * **param.withFilters** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### indexesByPath#

fos.indexesByPath(_param_)#
    

Arguments:
    

  * **param** (`Array`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isCompoundIndexed#

fos.isCompoundIndexed(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isDisabledCheckboxPath#

fos.isDisabledCheckboxPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isDisabledFilterPath#

fos.isDisabledFilterPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isDisabledFrameFilterPath#

fos.isDisabledFrameFilterPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isFilterDefault#

fos.isFilterDefault(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isFrameField#

fos.isFrameField(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isGridCustomRendererFailOpen#

fos.isGridCustomRendererFailOpen(_datasetName_)#
    

Arguments:
    

  * **datasetName** (`string`)



Return type:
    

`boolean`

Whether custom grid renderers are disabled for the given dataset.

### isHoveringAnyLabelWithInstanceConfig#

fos.isHoveringAnyLabelWithInstanceConfig()#
    

Return type:
    

`boolean`

Whether there are hovered instances

### isHoveringParticularLabelWithInstanceConfig#

fos.isHoveringParticularLabelWithInstanceConfig(_instanceId_)#
    

Arguments:
    

  * **instanceId** (`string`)



Return type:
    

`boolean`

Whether there are hovered instances of a particular instance

### isInListField#

fos.isInListField(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isLabelPath#

fos.isLabelPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isListField#

fos.isListField(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isMatchingAtom#

fos.isMatchingAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isNumericField#

fos.isNumericField(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isObjectIdField#

fos.isObjectIdField(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isOfDocumentFieldList#

fos.isOfDocumentFieldList(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### isStringField#

fos.isStringField(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### keypointFilter#

fos.keypointFilter(_name_ , _embeddedDocType_ , _filter_)#
    

Arguments:
    

  * **name** (`string`)

  * **embeddedDocType** (`string`)

  * **filter** ()




### labelCount#

fos.labelCount(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### labelFields#

fos.labelFields(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.space** (`SPACE`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### labelPath#

fos.labelPath(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### labelPaths#

fos.labelPaths(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.expanded** (`boolean`)

  * **param.space** (`SPACE`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### labelTagCounts#

fos.labelTagCounts(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### labelsMatcher#

fos.labelsMatcher(_parent_)#
    

Arguments:
    

  * **parent** ()




### lightningBooleanResults#

fos.lightningBooleanResults(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Object` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### lightningBounds#

fos.lightningBounds(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `[ number , number ]` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### lightningNonfinites#

fos.lightningNonfinites(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### lightningNumericResults#

fos.lightningNumericResults(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### lightningQuery#

fos.lightningQuery(_parameter_)#
    

Arguments:
    

  * **parameter** (`readonly`)



Return type:
    

`readonly` `readonly RecoilState < >` `<` `readonly` `>`

### lightningStringResults#

fos.lightningStringResults(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.exclude** (`Array`)

  * **param.filters** (`SerializableParam`)

  * **param.index** (`string`)

  * **param.maxDocumentsSearch** (`number`)

  * **param.path** (`string`)

  * **param.search** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### listBoolean#

fos.listBoolean(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `( value : boolean )` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### listNumber#

fos.listNumber(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `( value : number )` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### listString#

fos.listString(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `( value : string )` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### logOnSetEffect#

fos.logOnSetEffect(_options_)#
    

Arguments:
    

  * **options** (`Object`)

  * **options.logPrefix** (`string`) â Custom prefix for log messages. Defaults to â[Recoil Set]â



Return type:
    

`AtomEffect < T >` `<` `plugins.fiftyone.state.T` `>`

Debug effect that logs when atom value is set.

**Returns**

A Recoil atom effect that logs set operations

### lookerOptions#

fos.lookerOptions(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.withFilter** (`boolean`)



Return type:
    

`RecoilState < Partial >` `<` `Partial < Omit >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### mapSampleResponse#

fos.mapSampleResponse(_data_)#
    

Arguments:
    

  * **data** (`T`)



Return type:
    

`plugins.fiftyone.state.T`

### markGridCustomRendererFailed#

fos.markGridCustomRendererFailed(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`MarkGridCustomRendererFailedOptions`)



Return type:
    

`plugins.fiftyone.state.GridCustomRendererFailure`

Records the first renderer failure for a dataset in the current browser session.

Repeated failures on the same dataset are ignored, but a later first failure on a different dataset will mint a fresh forced subscription so the app can reload away from any newly poisoned sync channel.

### maxAtom#

fos.maxAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)

  * **param.withBounds** (`boolean`)



Return type:
    

`RecoilState < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### meetsType#

fos.meetsType(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.acceptLists** (`boolean`)

  * **param.embeddedDocType** (`Union`)

  * **param.ftype** (`Union`)

  * **param.path** (`string`)

  * **param.under** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### minAtom#

fos.minAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)

  * **param.withBounds** (`boolean`)



Return type:
    

`RecoilState < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### modalAggregationPaths#

fos.modalAggregationPaths(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.mixed** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### modalFilterFields#

fos.modalFilterFields(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### noneAtom#

fos.noneAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.isFiltering** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### noneCount#

fos.noneCount(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### nonfiniteAtom#

fos.nonfiniteAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.key** (`Union`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### nonfiniteCount#

fos.nonfiniteCount(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.key** (`Nonfinite`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### nonfiniteData#

fos.nonfiniteData(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , , , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### numGroupFieldsActive#

fos.numGroupFieldsActive(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.group** (`string`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### numGroupFieldsFiltered#

fos.numGroupFieldsFiltered(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.group** (`string`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### numGroupFieldsVisible#

fos.numGroupFieldsVisible(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.group** (`string`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### numeric#

fos.numeric(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `( value : number )` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### numericExcludeAtom#

fos.numericExcludeAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### numericFields#

fos.numericFields(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### numericIsMatchingAtom#

fos.numericIsMatchingAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### parentField#

fos.parentField(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < Field >` `<` `plugins.fiftyone.state.Field` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### pathCanBeOptimized#

fos.pathCanBeOptimized(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Union< , >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### pathColor#

fos.pathColor(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### pathFilter#

fos.pathFilter(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < PathFilterSelector >` `<` `plugins.fiftyone.state.PathFilterSelector` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### pathHasActiveIndex#

fos.pathHasActiveIndex(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### pathHasIndexes#

fos.pathHasIndexes(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.path** (`string`)

  * **param.withFilters** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### pathIndex#

fos.pathIndex(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.path** (`string`)

  * **param.withFilters** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### pathIsShown#

fos.pathIsShown(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### persistSidebarGroups#

fos.persistSidebarGroups(_variables_)#
    

Arguments:
    

  * **variables** (`setSidebarGroupsMutation$variables`)



Return type:
    

`void`

### primitivesMatcher#

fos.primitivesMatcher(_field_)#
    

Arguments:
    

  * **field** (`StrictField`)



Return type:
    

`boolean`

### pullSidebarValue#

fos.pullSidebarValue(_inputField_ , _keys_ , _input_ , _isList_)#
    

Arguments:
    

  * **inputField** (`Pick`)

  * **keys** (`Array`)

  * **input** (`object`)

  * **isList** (`boolean`)



Return type:
    

`object`

### rangeAtom#

fos.rangeAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)

  * **param.withBounds** (`boolean`)



Return type:
    

`RecoilState < Range >` `<` `plugins.fiftyone.state.Range` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### readableTags#

fos.readableTags(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.group** (`Union`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### removeRgbProperty#

fos.removeRgbProperty(_input_)#
    

Arguments:
    

  * **input** (`any`)



Return type:
    

`any`

### resolveGroups#

fos.resolveGroups(_sampleFields_ , _frameFields_ , _currentGroups_ , _configGroups_)#
    

Arguments:
    

  * **sampleFields** (`Array`)

  * **frameFields** (`Array`)

  * **currentGroups** (`Array`)

  * **configGroups** (`Array`)



Return type:
    

`Array<` `plugins.fiftyone.state.SidebarGroup` `>`

### resolveSelectionIcon#

fos.resolveSelectionIcon(_selectedSamples_ , _style_ , _sampleId_ , _isSelected_)#
    

Arguments:
    

  * **selectedSamples** (`Map`)

  * **style** (`SelectionStyle`)

  * **sampleId** (`string`)

  * **isSelected** (`boolean`)



Return type:
    

`Object`

### sampleTagCounts#

fos.sampleTagCounts(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### schemaReduce#

fos.schemaReduce(_schema_ , _field_)#
    

Arguments:
    

  * **schema** (`Schema`)

  * **field** (`StrictField`)



Return type:
    

`plugins.fiftyone.state.Schema`

### selectedMediaField#

fos.selectedMediaField(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### selectedMediaFieldAtomFamily#

fos.selectedMediaFieldAtomFamily(_params_)#
    

Arguments:
    

  * **params** (`boolean`)



Return type:
    

`RecoilState < string >` `<` `string` `>`

### selectedPatchIds#

fos.selectedPatchIds(_param_)#
    

Arguments:
    

  * **param** (`SerializableParam`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < Set >` `<` `Set < string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sessionAtom#

fos.sessionAtom(_options_)#
    

Arguments:
    

  * **options** (`SessionAtomOptions`)



Return type:
    

`RecoilState < >` `<` ```` `>`

### setCurrentEnvironment#

fos.setCurrentEnvironment(_environment_)#
    

Arguments:
    

  * **environment** (`default`)



Return type:
    

`void`

### setQueryPerformancePath#

fos.setQueryPerformancePath(_path_ , _isFrameField_)#
    

Arguments:
    

  * **path** (`string`)

  * **isFrameField** (`boolean`)



Return type:
    

`void`

### shouldRenderImaVidLooker#

fos.shouldRenderImaVidLooker(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarEntries#

fos.sidebarEntries(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.filtered** (`boolean`)

  * **param.loading** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Array< SidebarEntry >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarExpanded#

fos.sidebarExpanded(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarExpandedStore#

fos.sidebarExpandedStore(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarGroup#

fos.sidebarGroup(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.filtered** (`boolean`)

  * **param.group** (`string`)

  * **param.loading** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarGroupMapping#

fos.sidebarGroupMapping(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.filtered** (`boolean`)

  * **param.loading** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Any` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarGroupNames#

fos.sidebarGroupNames(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarGroups#

fos.sidebarGroups(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.filtered** (`boolean`)

  * **param.loading** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.persist** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Array< SidebarGroup >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarGroupsDefinition#

fos.sidebarGroupsDefinition(_params_)#
    

Arguments:
    

  * **params** (`boolean`)



Return type:
    

`RecoilState < >` `<` `Array< SidebarGroup >` `>`

### sidebarVisible#

fos.sidebarVisible(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sidebarWidth#

fos.sidebarWidth(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < number >` `<` `number` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### skeleton#

fos.skeleton(_param_)#
    

Arguments:
    

  * **param** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < KeypointSkeleton >` `<` `plugins.fiftyone.state.KeypointSkeleton` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### sortFilterResults#

fos.sortFilterResults(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < SortResults >` `<` `plugins.fiftyone.state.SortResults` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### string#

fos.string(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `( value : string )` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### stringCountResults#

fos.stringCountResults(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Object` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### stringExcludeAtom#

fos.stringExcludeAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### stringResults#

fos.stringResults(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Object` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### stringSelectedValuesAtom#

fos.stringSelectedValuesAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### stringifyObj#

fos.stringifyObj(_obj_)#
    

Arguments:
    

  * **obj** (`any`)



Return type:
    

`any`

### subscribeToGridCustomRendererFailover#

fos.subscribeToGridCustomRendererFailover(_listener_)#
    

Arguments:
    

  * **listener** (`( )`)




Subscribes React to this external fail-open store.

> fos.subscribeToGridCustomRendererFailover(_listener_)#
>     
> 
> Return type:
>     
> 
> `void`

### tagging#

fos.tagging(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.labels** (`boolean`)

  * **param.modal** (`boolean`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### textFilter#

fos.textFilter(_param_)#
    

Arguments:
    

  * **param** (`boolean`)



Return type:
    

`RecoilState < string >` `<` `string` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### transformDataset#

fos.transformDataset(_dataset_)#
    

Arguments:
    

  * **dataset** (`any`)



Return type:
    

`Readonly < Dataset >` `<` `plugins.fiftyone.state.Dataset` `>`

### trueAtom#

fos.trueAtom(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.isFiltering** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < boolean >` `<` `boolean` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### unsupportedMatcher#

fos.unsupportedMatcher(_field_)#
    

Arguments:
    

  * **field** (`StrictField`)



Return type:
    

`boolean`

### validIndexes#

fos.validIndexes(_param_)#
    

Arguments:
    

  * **param** (`Array`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Object` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### validateGroupName#

fos.validateGroupName(_current_ , _name_)#
    

Arguments:
    

  * **current** (`Array`)

  * **name** (`string`)



Return type:
    

`boolean`

### values#

fos.values(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.extended** (`boolean`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`readonly` `readonly RecoilValueReadOnly < >` `<` `Array< string >` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### viewsAreEqual#

fos.viewsAreEqual(_viewOne_ , _viewTwo_)#
    

Arguments:
    

  * **viewOne** (`Union`)

  * **viewTwo** (`Union`)



Return type:
    

`boolean`

### visibility#

fos.visibility(_param_)#
    

Arguments:
    

  * **param** (`Object`)

  * **param.modal** (`boolean`)

  * **param.path** (`string`)



Return type:
    

`RecoilState < Filter >` `<` `plugins.fiftyone.state.Filter` `>`

Returns a function which returns a memoized atom for each unique parameter value.

### withSuspense#

fos.withSuspense(_Component_ , _LoaderComponent_)#
    

Arguments:
    

  * **Component** (`ComponentType`)

  * **LoaderComponent** ()




## Types#

### SPACE#

Name | Value  
---|---  
FRAME |   
SAMPLE |   
  
### AnnotationRun#

class fos.AnnotationRun()#
    

#### Properties#

Name | Type | Description  
---|---|---  
config | `Any` |   
key | `string` |   
timestamp | `string` |   
version | `string` |   
viewStages | `readonly` |   
  
### BrainRun#

class fos.BrainRun()#
    

#### Properties#

Name | Type | Description  
---|---|---  
config | `Object` |   
key | `string` |   
timestamp | `string` |   
version | `string` |   
viewStages | `readonly` |   
  
### Config#

class fos.Config()#
    

#### Properties#

Name | Type | Description  
---|---|---  
colorPool | `Array<` `string` `>` |   
colorscale | `string` |   
customizedColors | `Array<` `plugins.fiftyone.state.CustomizeColorInput` `>` |   
gridZoom | `number` |   
loopVideos | `boolean` |   
mediaFallback | `boolean` |   
mediaFields | `Array<` `string` `>` |   
notebookHeight | `number` |   
plugins | `plugins.fiftyone.state.PluginConfig` |   
showConfidence | `boolean` |   
showIndex | `boolean` |   
showLabel | `boolean` |   
showTooltip | `boolean` |   
theme | `Union<` `'dark'` `,` `'light'` `,` `'browser'` `>` |   
timezone | `string` |   
useFrameNumber | `boolean` |   
  
### Dataset#

class fos.Dataset()#
    

The dataset object returned by the API.

#### Properties#

Name | Type | Description  
---|---|---  
appConfig | `plugins.fiftyone.state.DatasetAppConfig` |   
brainMethods | `Array<` `plugins.fiftyone.state.BrainRun` `>` |   
createdAt | `plugins.fiftyone.state.DateTime` |   
datasetId | `string` |   
defaultMaskTargets | `plugins.fiftyone.state.Targets` |   
defaultSkeleton | `plugins.fiftyone.state.KeypointSkeleton` |   
evaluations | `Array<` `plugins.fiftyone.state.EvaluationRun` `>` |   
groupField | `string` |   
groupMediaTypes | `Array<` `Object` `>` |   
groupSlice | `string` |   
id | `string` |   
info | `Any` |   
lastLoadedAt | `plugins.fiftyone.state.DateTime` |   
maskTargets | `Any` |   
mediaType | `plugins.fiftyone.state.MediaType` |   
name | `string` |   
parentMediaType | `plugins.fiftyone.state.MediaType` |   
skeletons | `Array<` `plugins.fiftyone.state.StrictKeypointSkeleton` `>` |   
version | `string` |   
  
### DatasetAppConfig#

class fos.DatasetAppConfig()#
    

#### Properties#

Name | Type | Description  
---|---|---  
activeFields | `plugins.fiftyone.state.ActiveFields` |   
dynamicGroupsTargetFrameRate | `number` |   
gridMediaField | `string` |   
mediaFields | `Array<` `string` `>` |   
modalMediaField | `string` |   
plugins | `plugins.fiftyone.state.PluginConfig` |   
  
### DateTime#

class fos.DateTime()#
    

#### Properties#

Name | Type | Description  
---|---|---  
$date | `number` |   
  
### Description#

class fos.Description()#
    

#### Properties#

Name | Type | Description  
---|---|---  
dataset | `string` |   
fieldVisibilityStage | `plugins.fiftyone.state.FieldVisibilityStage` |   
savedViewSlug | `string` |   
savedViews | `Array<` `plugins.fiftyone.state.SavedView` `>` |   
selected | `Array<` `string` `>` |   
selectedLabels | `Array<` `plugins.fiftyone.state.SelectedLabel` `>` |   
spaces | `plugins.fiftyone.state.SpaceNodeJSON` |   
view | `Array<` `plugins.fiftyone.state.Stage` `>` |   
viewCls | `string` |   
viewName | `string` |   
  
### DynamicGroupParameters#

class fos.DynamicGroupParameters()#
    

#### Properties#

Name | Type | Description  
---|---|---  
groupBy | `Union<` `object` `,` `Array< string >` `>` |   
orderBy | `string` |   
orderByKey | `unknown` |   
  
### Evaluation#

class fos.Evaluation()#
    

### EvaluationRun#

class fos.EvaluationRun()#
    

#### Properties#

Name | Type | Description  
---|---|---  
config | `Object` |   
key | `string` |   
timestamp | `string` |   
version | `string` |   
viewStages | `readonly` |   
  
### FieldVisibilityStage#

class fos.FieldVisibilityStage()#
    

#### Properties#

Name | Type | Description  
---|---|---  
cls | `string` |   
kwargs | `Object` |   
  
### Filter#

class fos.Filter()#
    

Name | Type | Description  
---|---|---  
[key] | `string` |   
  
### Filters#

class fos.Filters()#
    

Name | Type | Description  
---|---|---  
[key] | `string` |   
  
### ID#

class fos.ID()#
    

#### Properties#

Name | Type | Description  
---|---|---  
$oid | `string` |   
  
### KeypointSkeleton#

class fos.KeypointSkeleton()#
    

#### Properties#

Name | Type | Description  
---|---|---  
edges | `Array<` `Array<` `number` `>` `>` |   
labels | `Array<` `string` `>` |   
  
### Run#

class fos.Run()#
    

#### Properties#

Name | Type | Description  
---|---|---  
config | `Any` |   
key | `string` |   
timestamp | `string` |   
version | `string` |   
viewStages | `readonly` |   
  
### SavedView#

class fos.SavedView()#
    

#### Properties#

Name | Type | Description  
---|---|---  
color | `string` |   
createdAt | `plugins.fiftyone.state.DateTime` |   
datasetId | `string` |   
description | `string` |   
id | `string` |   
lastLoadedAt | `plugins.fiftyone.state.DateTime` |   
lastModifiedAt | `plugins.fiftyone.state.DateTime` |   
name | `string` |   
slug | `string` |   
viewStages | `Array<` `plugins.fiftyone.state.Stage` `>` |   
  
### SelectedLabel#

class fos.SelectedLabel()#
    

#### Properties#

Name | Type | Description  
---|---|---  
field | `string` |   
frameNumber | `number` |   
instanceId | `string` |   
labelId | `string` |   
sampleId | `string` |   
type | `plugins.fiftyone.state.SelectionType` |   
  
### SelectedLabelData#

class fos.SelectedLabelData()#
    

#### Properties#

Name | Type | Description  
---|---|---  
field | `string` |   
frameNumber | `number` |   
instanceId | `string` |   
sampleId | `string` |   
type | `plugins.fiftyone.state.SelectionType` |   
  
### SelectedLabelMap#

class fos.SelectedLabelMap()#
    

Name | Type | Description  
---|---|---  
[labelId] | `string` |   
  
### SidebarGroup#

class fos.SidebarGroup()#
    

#### Properties#

Name | Type | Description  
---|---|---  
expanded | `boolean` |   
name | `string` |   
paths | `Array<` `string` `>` |   
  
### SortBySimilarityParameters#

class fos.SortBySimilarityParameters()#
    

#### Properties#

Name | Type | Description  
---|---|---  
brainKey | `string` |   
distField | `string` |   
k | `number` |   
query | `Union<` `string` `,` `Array< string >` `>` |   
queryIds | `Array<` `string` `>` |   
reverse | `boolean` |   
  
### Stage#

class fos.Stage()#
    

#### Properties#

Name | Type | Description  
---|---|---  
kwargs | `Array<` `[` `string` `,` `unknown` `]` `>` |   
  
### StrictKeypointSkeleton#

class fos.StrictKeypointSkeleton()#
    

#### Properties#

Name | Type | Description  
---|---|---  
edges | `Array<` `Array<` `number` `>` `>` |   
labels | `Array<` `string` `>` |   
name | `string` |   
  
### Targets#

class fos.Targets()#
    

Name | Type | Description  
---|---|---  
[key] | `number` |   
  
class fos.ActiveFields()#
    

### ActiveFields#

Name | Type | Description  
---|---|---  
ActiveFields.exclude | `Union<` `boolean` `,` `null` `>` |   
ActiveFields.paths | `Array<` `string` `>` |   
  
class fos.MediaType()#
    

### MediaType#

Union of `'image'`, `'group'`, `'point_cloud'`, `'point-cloud'`, `'three_d'`, `'3d'`, `'video'`, `'unknown'`

class fos.PluginConfig()#
    

### PluginConfig#

An object containing the configuration for plugins. Each key is the name of a plugin, and the value is the configuration for that plugin.

### PANEL_SURFACE#

Name | Value  
---|---  
GRID |   
MODAL |   
  
### COLOR_BLIND_FRIENDLY_PALETTE#

### COLOR_OPTIONS#

### COLOR_OPTIONS_MAP#

Name | Type | Description  
---|---|---  
#06AED4 | `Object` |   
#16B364 | `Object` |   
#2970FF | `Object` |   
#667085 | `Object` |   
#7A5AF8 | `Object` |   
#EE46BC | `Object` |   
#EF6820 | `Object` |   
#F04438 | `Object` |   
#FAC515 | `Object` |   
  
### DEFAULT_COLOR#

Name | Type | Description  
---|---|---  
`'#667085'` |  |   
  
### DEFAULT_COLOR_OPTION#

Name | Type | Description  
---|---|---  
color | `string` |   
description | `string` |   
id | `string` |   
label | `string` |   
  
### FIFTYONE_GRID_SPACES_ID#

Name | Type | Description  
---|---|---  
`'fiftyone-spaces'` |  |   
  
### FIFTYONE_MODAL_SPACES_ID#

Name | Type | Description  
---|---|---  
`'fiftyone-modal-spaces'` |  |   
  
### BooleanFilter#

class fos.BooleanFilter()#
    

#### Properties#

Name | Type | Description  
---|---|---  
exclude | `boolean` |   
false | `boolean` |   
isMatching | `boolean` |   
none | `boolean` |   
true | `boolean` |   
  
### ClassificationAnnotationLabel#

class fos.ClassificationAnnotationLabel()#
    

#### Properties#

Name | Type | Description  
---|---|---  
data | `plugins.fiftyone.state.ClassificationLabel` |   
isNew | `boolean` |   
overlay | `plugins.fiftyone.state.ClassificationOverlay` |   
path | `string` |   
type | `'Classification'` |   
  
### ContextManager#

class fos.ContextManager()#
    

A context manager provides support for stateful transitions into and out-of some logical context.

Callbacks can be registered to be executed when entering or exiting the context.

#### Properties#

Name | Type | Description  
---|---|---  
isActive | `(` `)` |   
enter | `void` | Enter the context, triggering all registered enter callbacks.  
exit | `void` | Exit the context, triggering all registered exit callbacks.  
registerEnterCallback | `void` | Register a callback to be invoked on context `enter`.  
registerExitCallback | `void` | Register a callback to be invoked on context `exit`.  
reset | `void` | Reset the context, clearing all registered callbacks.  
  
### Detection3DAnnotationLabel#

class fos.Detection3DAnnotationLabel()#
    

#### Properties#

Name | Type | Description  
---|---|---  
data | `plugins.fiftyone.state.DetectionLabel` |   
isNew | `boolean` |   
overlay | `plugins.fiftyone.state.GenericOverlay` `<` `plugins.fiftyone.state.DetectionLabel` `>` |   
path | `string` |   
type | `'Detection'` |   
  
### DetectionAnnotationLabel#

class fos.DetectionAnnotationLabel()#
    

#### Properties#

Name | Type | Description  
---|---|---  
data | `plugins.fiftyone.state.DetectionLabel` |   
isNew | `boolean` |   
overlay | `plugins.fiftyone.state.DetectionOverlay` |   
path | `string` |   
type | `'Detection'` |   
  
### EmptyAnnotationsEntry#

class fos.EmptyAnnotationsEntry()#
    

#### Properties#

Name | Type | Description  
---|---|---  
kind | `plugins.fiftyone.state.EMPTY_ANNOTATIONS` |   
  
### EmptyEntry#

class fos.EmptyEntry()#
    

#### Properties#

Name | Type | Description  
---|---|---  
group | `string` |   
kind | `plugins.fiftyone.state.EMPTY` |   
shown | `boolean` |   
  
### GroupEntry#

class fos.GroupEntry()#
    

#### Properties#

Name | Type | Description  
---|---|---  
kind | `plugins.fiftyone.state.GROUP` |   
name | `string` |   
  
### GroupVisibilityConfigSnapshot#

class fos.GroupVisibilityConfigSnapshot()#
    

Snapshot of group visibility settings and slice captured before entering Annotate mode. Used to restore settings when returning to Explore mode.

#### Properties#

Name | Type | Description  
---|---|---  
carousel | `boolean` |   
main | `boolean` |   
slice | `string` |   
threeDViewer | `boolean` |   
  
### IActivityToast#

class fos.IActivityToast()#
    

Activity toast interface.

#### Properties#

Name | Type | Description  
---|---|---  
config | `plugins.fiftyone.state.ActivityToastConfig` | Current toast configuration.  
open | `boolean` | `true` if the toast is open, else `false`.  
setConfig | `void` | Set the toast configuration.  
setIconName | `void` | Set the icon for the toast.  
setMessage | `void` | Set the message for the toast.  
setTimeout | `void` | Set the timeout for the toast.  
setVariant | `void` | Set the toast variant.  
  
### InputEntry#

class fos.InputEntry()#
    

#### Properties#

Name | Type | Description  
---|---|---  
kind | `plugins.fiftyone.state.INPUT` |   
type | `Union<` `'filter'` `,` `'add'` `>` |   
  
### KeypointAnnotationLabel#

class fos.KeypointAnnotationLabel()#
    

#### Properties#

Name | Type | Description  
---|---|---  
data | `plugins.fiftyone.state.KeypointLabel` |   
isNew | `boolean` |   
overlay | `plugins.fiftyone.state.KeypointOverlay` |   
path | `string` |   
type | `'Keypoint'` |   
  
### Label#

class fos.Label()#
    

#### Properties#

Name | Type | Description  
---|---|---  
isNew | `boolean` |   
path | `string` |   
  
### LabelEntry#

class fos.LabelEntry()#
    

#### Properties#

Name | Type | Description  
---|---|---  
atom | `PrimitiveAtom < AnnotationLabel >` `<` `plugins.fiftyone.state.AnnotationLabel` `>` |   
id | `string` |   
kind | `plugins.fiftyone.state.LABEL` |   
  
### LoadingEntry#

class fos.LoadingEntry()#
    

#### Properties#

Name | Type | Description  
---|---|---  
id | `string` |   
kind | `plugins.fiftyone.state.LOADING` |   
  
### LookerStore#

class fos.LookerStore()#
    

#### Properties#

Name | Type | Description  
---|---|---  
indices | `Map < number , string >` `<` `number` `,` `string` `>` |   
lookers | `LRUCache < string , T , unknown >` `<` `string` `,` `plugins.fiftyone.state.T` `,` `unknown` `>` |   
reset | `(` `)` |   
samples | `Map < string , ModalSample >` `<` `string` `,` `plugins.fiftyone.state.ModalSample` `>` |   
  
### ModalModeController#

class fos.ModalModeController()#
    

Manager which supports switching modal modes.

#### Properties#

Name | Type | Description  
---|---|---  
activateAnnotateMode | `(` `)` |   
activateExploreMode | `(` `)` |   
  
### ModalViewportState#

class fos.ModalViewportState()#
    

Extends the base ViewportState with a `sampleId` so stale state from a previous sample is never mistakenly applied when switching between modes (EXPLORE vs ANNOTATE).

#### Properties#

Name | Type | Description  
---|---|---  
panX | `number` |   
panY | `number` |   
sampleId | `string` |   
scale | `number` |   
  
### NumericFilter#

class fos.NumericFilter()#
    

#### Properties#

Name | Type | Description  
---|---|---  
exclude | `boolean` |   
inf | `boolean` |   
isMatching | `boolean` |   
nan | `boolean` |   
ninf | `boolean` |   
none | `boolean` |   
range | `plugins.fiftyone.state.Range` |   
  
### PathEntry#

class fos.PathEntry()#
    

#### Properties#

Name | Type | Description  
---|---|---  
kind | `plugins.fiftyone.state.PATH` |   
path | `string` |   
shown | `boolean` |   
  
### PolylineAnnotationLabel#

class fos.PolylineAnnotationLabel()#
    

#### Properties#

Name | Type | Description  
---|---|---  
data | `plugins.fiftyone.state.PolylineLabel` |   
isNew | `boolean` |   
overlay | `Union<` `plugins.fiftyone.state.PolylineOverlay` `,` `plugins.fiftyone.state.GenericOverlay` `>` |   
path | `string` |   
type | `'Polyline'` |   
  
### PrimitiveValue#

class fos.PrimitiveValue()#
    

#### Properties#

Name | Type | Description  
---|---|---  
data | `plugins.fiftyone.state.Primitive` |   
op | `plugins.fiftyone.state.OpType` |   
path | `string` |   
type | `'Primitive'` |   
  
### RetryController#

class fos.RetryController()#
    

Utility which provides retry control flow logic.

#### Properties#

Name | Type | Description  
---|---|---  
canAttempt | `boolean` | If `true`, operation can be attempted.  
recordAttempt | `(` `)` |   
reset | `(` `)` |   
  
### SelectEvent#

class fos.SelectEvent()#
    

#### Properties#

Name | Type | Description  
---|---|---  
detail | `Object` |   
  
### Session#

class fos.Session()#
    

#### Properties#

Name | Type | Description  
---|---|---  
canAnnotate | `Object` |   
canCreateNewField | `Object` |   
canEditCustomColors | `Object` |   
canEditLabels | `Object` |   
canEditSavedViews | `Object` |   
canEditWorkspaces | `Object` |   
canManageSchema | `Object` |   
canModifySidebarGroup | `Object` |   
canTagSamplesOrLabels | `Object` |   
colorScheme | `plugins.fiftyone.state.ColorSchemeInput` |   
fieldVisibilityStage | `plugins.fiftyone.state.FieldVisibilityStage` |   
filters | `plugins.fiftyone.state.Filters` |   
labelSelectionStyle | `plugins.fiftyone.state.LabelSelectionStyle` |   
modalFilters | `plugins.fiftyone.state.Filters` |   
modalSelector | `plugins.fiftyone.state.ModalSelector` |   
readOnly | `boolean` |   
sampleSelectionStyle | `plugins.fiftyone.state.SelectionStyle` |   
selectedLabels | `Array<` `plugins.fiftyone.state.SelectedLabel` `>` |   
selectedSamples | `Map < string , SelectionType >` `<` `string` `,` `plugins.fiftyone.state.SelectionType` `>` |   
sessionGroupSlice | `string` |   
sessionSpaces | `plugins.fiftyone.state.SpaceNodeJSON` |   
  
### SortResults#

class fos.SortResults()#
    

#### Properties#

Name | Type | Description  
---|---|---  
asc | `boolean` |   
count | `boolean` |   
  
### StringFilter#

class fos.StringFilter()#
    

#### Properties#

Name | Type | Description  
---|---|---  
exclude | `boolean` |   
isMatching | `boolean` |   
values | `Array<` `string` `>` |   
  
class fos.ActivityToastConfig()#
    

### ActivityToastConfig#

Configuration data which drives ActivityToast behavior.

the toast will disappear after this time has elapsed.

This timeout is reset any time the toast configuration is modified.

A negative timeout value will disable the timeout, causing the toast to remain visible indefinitely.â

> âActivityToastConfig.variantâ,â`Variant`â,âToast variant.â

class fos.AggregationResponseFrom()#
    

### AggregationResponseFrom#

A generic type that extracts the response type from a GraphQL query.

class fos.AnnotationLabel()#
    

### AnnotationLabel#

Union of `ClassificationAnnotationLabel`, `DetectionAnnotationLabel`, `Detection3DAnnotationLabel`, `PolylineAnnotationLabel`, `KeypointAnnotationLabel`

class fos.AnnotationLabelData()#
    

### AnnotationLabelData#

class fos.ComputeCoordinatesReturnType()#
    

### ComputeCoordinatesReturnType#

Name | Type | Description  
---|---|---  
ComputeCoordinatesReturnType | `ReturnType < >` `<` ```` `>` |   
  
class fos.DatasetViewOption()#
    

### DatasetViewOption#

class fos.DebouncedState()#
    

### DebouncedState#

class fos.DimensionsType()#
    

### DimensionsType#

Name | Type | Description  
---|---|---  
DimensionsType | `ReturnType < >` `<` ```` `>` |   
  
class fos.GridCustomRendererFailure()#
    

### GridCustomRendererFailure#

Name | Type | Description  
---|---|---  
GridCustomRendererFailure.datasetName | `string` |   
GridCustomRendererFailure.errorMessage | `string` |   
GridCustomRendererFailure.failedAt | `number` |   
GridCustomRendererFailure.rendererName | `string` |   
  
class fos.GroupSliceMediaType()#
    

### GroupSliceMediaType#

Union of `'video'`, `'3d'`, `'image'`

class fos.HoveredInstancesLabelsTuple()#
    

### HoveredInstancesLabelsTuple#

Name | Type | Description  
---|---|---  
HoveredInstancesLabelsTuple | `[` `plugins.fiftyone.state.InstanceId` `,` `plugins.fiftyone.state.LabelMap` `]` |   
  
class fos.LabelMap()#
    

### LabelMap#

======= TYPES =======

Name | Type | Description  
---|---|---  
LabelMap | `Record < LabelId , LabelHoveredEventData >` `<` `plugins.fiftyone.state.LabelId` `,` `plugins.fiftyone.state.LabelHoveredEventData` `>` |   
  
class fos.LabelSelectionStyle()#
    

### LabelSelectionStyle#

Name | Type | Description  
---|---|---  
LabelSelectionStyle.alt | `plugins.fiftyone.state.LabelSelectionStyleName` |   
LabelSelectionStyle.default | `plugins.fiftyone.state.LabelSelectionStyleName` |   
  
class fos.LabelSelectionStyleName()#
    

### LabelSelectionStyleName#

Union of `'dashed'`, `'dashed-green'`, `'dashed-red'`

class fos.Loading()#
    

### Loading#

class fos.Lookers()#
    

### Lookers#

Union of `FrameLooker`, `ImageLooker`, `ImaVidLooker`, `VideoLooker`

class fos.Method()#
    

### Method#

Name | Type | Description  
---|---|---  
Method.key | `string` |   
Method.maxK | `number` |   
Method.supportsLeastSimilarity | `boolean` |   
Method.supportsPrompts | `boolean` |   
  
class fos.ModalNavigation()#
    

### ModalNavigation#

Name | Type | Description  
---|---|---  
ModalNavigation.next | `(` `offset` `:` `number` `)` |   
ModalNavigation.previous | `(` `offset` `:` `number` `)` |   
  
class fos.ModalSample()#
    

### ModalSample#

class fos.ModalSampleData()#
    

### ModalSampleData#

Name | Type | Description  
---|---|---  
ModalSampleData | `Exclude < Exclude , >` `<` `Exclude < , >` `,` `null` `>` |   
  
class fos.ModalSelector()#
    

### ModalSelector#

Name | Type | Description  
---|---|---  
ModalSelector.groupId | `string` |   
ModalSelector.hasNext | `boolean` |   
ModalSelector.hasPrevious | `boolean` |   
ModalSelector.id | `string` |   
  
class fos.Optional()#
    

### Optional#

Optional From `T` make a set of properties by key `K` become optional

class fos.PathFilterSelector()#
    

### PathFilterSelector#

class fos.Range()#
    

### Range#

Name | Type | Description  
---|---|---  
Range | `[` `Union< number , >` `,` `Union< number , >` `]` |   
  
class fos.RenderConfig3dActions()#
    

### RenderConfig3dActions#

Mutation helpers exposed by `useRenderConfig3dActions`.

Name | Type | Description  
---|---|---  
RenderConfig3dActions.focusSlice | `(` `sliceName` `:` `string` `)` |   
RenderConfig3dActions.initializeFromModalSlice | `(` `sliceName` `:` `Union< string , >` `)` |   
RenderConfig3dActions.reconcileAvailableSlices | `(` `)` |   
RenderConfig3dActions.setFo3dContent | `(` `content` `:` `Union< unknown , >` `)` |   
RenderConfig3dActions.setPinned | `(` `pinned` `:` `boolean` `)` |   
RenderConfig3dActions.setVisible | `(` `visible` `:` `boolean` `)` |   
RenderConfig3dActions.toggleSlice | `(` `sliceName` `:` `string` `, `` ``enabled` `:` `boolean` `)` |   
  
class fos.RenderConfig3dImperativeState()#
    

### RenderConfig3dImperativeState#

Imperative snapshot query helpers exposed by `useRenderConfig3dImperativeState`.

Name | Type | Description  
---|---|---  
RenderConfig3dImperativeState.getIsPinned | `(` `)` |   
  
class fos.RenderConfig3dState()#
    

### RenderConfig3dState#

Derived 3D modal state exposed by `useRenderConfig3dState`.

Name | Type | Description  
---|---|---  
RenderConfig3dState.activeDirectSlices | `Array<` `string` `>` | Active non-FO3D 3D slices rendered alongside the scene.  
RenderConfig3dState.activeFo3dSlice | `Union<` `string` `,` `null` `>` | Active FO3D slice currently driving the scene, if one is selected.  
RenderConfig3dState.activeSampleMap | `plugins.fiftyone.state.RenderConfig3dSampleMap` | Resolved samples for the currently active 3D slices.  
RenderConfig3dState.activeSlices | `Array<` `string` `>` | Slice names currently participating in 3D rendering.  
RenderConfig3dState.allSampleMap | `plugins.fiftyone.state.RenderConfig3dSampleMap` | Resolved samples for every available 3D slice in the current modal context.  
RenderConfig3dState.allSlices | `Array<` `string` `>` | All available 3D slice names.  
RenderConfig3dState.fo3dContent | `Union<` `unknown` `,` `null` `>` | Parsed FO3D scene content cached for the active scene sample.  
RenderConfig3dState.has3dSlice | `boolean` | Whether the current modal context exposes any 3D slice.  
RenderConfig3dState.hasFo3dSlice | `boolean` | Whether any available 3D slice resolves to an FO3D asset.  
RenderConfig3dState.hasMultipleSlices | `boolean` | Whether more than one 3D slice is available.  
RenderConfig3dState.interactionSample | `plugins.fiftyone.state.ModalSample` | Representative sample used for 3D interaction-driven behavior.  
RenderConfig3dState.interactionSlice | `Union<` `string` `,` `null` `>` | Slice corresponding to `RenderConfig3dState.interactionSample`.  
RenderConfig3dState.is3dVisible | `boolean` | Whether the 3D viewer should currently be shown.  
RenderConfig3dState.is3dVisibleSetting | `boolean` | Persisted user preference for showing the 3D viewer.  
RenderConfig3dState.isPinned | `boolean` | Whether the 3D selection is pinned to a specific slice.  
RenderConfig3dState.non3dSlices | `Array<` `string` `>` | All available non-3D slice names.  
RenderConfig3dState.pinnedSlice | `Union<` `string` `,` `null` `>` | Slice name currently pinned for 3D rendering, if any.  
RenderConfig3dState.realFo3dSlices | `Array<` `string` `>` | Available 3D slices whose media resolves to FO3D files.  
RenderConfig3dState.sceneSample | `plugins.fiftyone.state.ModalSample` | Sample currently used to render the visible 3D scene.  
  
class fos.ResponseFrom()#
    

### ResponseFrom#

class fos.RetryConfig()#
    

### RetryConfig#

Retry configuration.

Name | Type | Description  
---|---|---  
RetryConfig.id | `string` | Unique ID to identify this retryable instance.  
RetryConfig.maxAttempts | `number` | Maximum number of attempts.  
  
class fos.Sample()#
    

### Sample#

Name | Type | Description  
---|---|---  
Sample | `Exclude < PaginateSamplesNode , >` `<` `plugins.fiftyone.state.PaginateSamplesNode` `,` `null` `>` |   
  
class fos.SelectionIconStyle()#
    

### SelectionIconStyle#

Union of `'checkmark'`, `'green-checkmark'`, `'red-checkmark'`, `'thumbsup'`, `'thumbsdown'`, `'pin'`, `'star'`, `'x'`, `'bookmark'`

class fos.SelectionStyle()#
    

### SelectionStyle#

Name | Type | Description  
---|---|---  
SelectionStyle.alt | `plugins.fiftyone.state.SelectionIconStyle` |   
SelectionStyle.default | `plugins.fiftyone.state.SelectionIconStyle` |   
  
class fos.SelectionType()#
    

### SelectionType#

Union of `'default'`, `'alt'`

class fos.SidebarEntry()#
    

### SidebarEntry#

Union of `EmptyEntry`, `EmptyAnnotationsEntry`, `GroupEntry`, `InputEntry`, `LabelEntry`, `LoadingEntry`, `PathEntry`

## Enums#

### EntryKind#

Name | Value  
---|---  
EMPTY |   
EMPTY_ANNOTATIONS |   
GROUP |   
INPUT |   
LABEL |   
LOADING |   
PATH |   
  
### ModalMode#

Operating mode of the modal.

Name | Value  
---|---  
ANNOTATE |   
EXPLORE |   
  
## Variables#

### ANNOTATE#

Name | Type | Description  
---|---|---  
`'annotate'` |  |   
  
### BeforeScreenshotContext#

Name | Type | Description  
---|---|---  
Context < Set > | `Context < Set >` `<` `Set < >` `>` |   
  
### DEFAULT_ALPHA#

Name | Type | Description  
---|---|---  
`0.7` |  |   
  
### DEFAULT_LABEL_SELECTION_STYLE#

Name | Type | Description  
---|---|---  
LabelSelectionStyle | `plugins.fiftyone.state.LabelSelectionStyle` |   
  
### DEFAULT_SELECTED#

Name | Type | Description  
---|---|---  
DatasetViewOption | `plugins.fiftyone.state.DatasetViewOption` |   
  
### DEFAULT_SELECTION_STYLE#

Name | Type | Description  
---|---|---  
SelectionStyle | `plugins.fiftyone.state.SelectionStyle` |   
  
### EXPLORE#

Name | Type | Description  
---|---|---  
`'explore'` |  |   
  
### GRID_SPACES_DEFAULT#

Name | Type | Description  
---|---|---  
active_child | `string` |   
children | `Array<` `Object` `>` |   
component_id | `string` |   
id | `string` |   
  
### GROUP_BY_VIEW_STAGE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.stages.GroupBy'` |  |   
  
### INDEFINITE_TOAST_TIMEOUT#

Timeout value which will cause the activity toast to remain open indefinitely.

Name | Type | Description  
---|---|---  
`-1` |  |   
  
### LABEL_TAGS_FIELD#

Name | Type | Description  
---|---|---  
`'_label_tags'` |  |   
  
### LIMIT_VIEW_STAGE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.stages.Limit'` |  |   
  
### LOADING#

Sentinel returned by `useActiveModalSampleValue` when no real value is available yet. Returned in two cases:

  1. The active modal sidebar sample is still loading.

  2. The sample failed with `GroupSampleNotFound` â sparse groups can legitimately lack a sample on the active slice; consumers should render a placeholder rather than crashing.




Other errors (including plain `SampleNotFound`) still bubble â they indicate a real problem, not a transient loading state.

Compare with `=== LOADING` and typically render a loading placeholder.

### MATCH_LABEL_TAGS#

Name | Type | Description  
---|---|---  
embeddedDocType | `Array<` `string` `>` |   
ftype | `string` |   
path | `string` |   
  
### MATCH_VIEW_STAGE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.stages.Match'` |  |   
  
### OTHER_GROUP#

Name | Type | Description  
---|---|---  
`'other'` |  |   
  
### RESERVED_GROUPS#

Name | Type | Description  
---|---|---  
Set < string > | `Set < string >` `<` `string` `>` |   
  
### RelayEnvironmentKey#

Name | Type | Description  
---|---|---  
EnvironmentKey | `EnvironmentKey` |   
  
### SESSION_DEFAULT#

Name | Type | Description  
---|---|---  
Session | `plugins.fiftyone.state.Session` |   
  
### SKIP_VIEW_STAGE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.stages.Skip'` |  |   
  
### SORT_VIEW_STAGE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.stages.SortBy'` |  |   
  
### TAB_OPTIONS#

### TAB_OPTIONS_MAP#

Name | Type | Description  
---|---|---  
FILTER_RULE | `string` |   
SELECTION | `string` |   
  
### TAGS_FIELD#

Name | Type | Description  
---|---|---  
`'tags'` |  |   
  
### TAKE_VIEW_STAGE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.stages.Take'` |  |   
  
### appConfigDefault#

Name | Type | Description  
---|---|---  
`any` |  |   
  
### currentModalUniqueIdJotaiAtom#

Current modal unique id. Itâs a concatenation of the group id and the sample id.

### datasetQueryContext#

Name | Type | Description  
---|---|---  
Context < savedViewsFragment$key > | `Context < savedViewsFragment$key >` `<` `plugins.fiftyone.state.savedViewsFragment$key` `>` |   
  
### hoveredInstances#

Set of hovered instances

### jotaiStore#

Name | Type | Description  
---|---|---  
ReturnType < > | `ReturnType < >` `<` ```` `>` |   
  
### modalBridge#

Bridge for synchronous access to modal viewport state from non-React code Provides read-only access to saved viewport state (zoom/pan position).

Name | Type | Description  
---|---|---  
getModalViewport | `plugins.fiftyone.state.ModalViewportState` | Reads the current modal viewport state.  
  
### modalMode#

Name | Type | Description  
---|---|---  
WritableAtom < ModalMode , , void > | `WritableAtom < ModalMode , , void >` `<` `plugins.fiftyone.state.ModalMode` `,` `[ SetStateActionWithReset ]` `,` `void` `>` |   
  
### modalNavigation#

Name | Type | Description  
---|---|---  
get | `(` `)` |   
set | `(` `value` `:` `plugins.fiftyone.state.ModalNavigation` `)` |   
  
### numConcurrentRenderingLabels#

Number of concurrently rendering labels.

### removeAllHoveredInstances#

Remove all hovered instances

Name | Type | Description  
---|---|---  
WritableAtom < unknown , , void > | `WritableAtom < unknown , , void >` `<` `unknown` `,` `[ ]` `,` `void` `>` |   
  
### screenshotCallbacks#

Name | Type | Description  
---|---|---  
Set < > | `Set < >` `<` `( )` `>` |   
  
### stores#

Name | Type | Description  
---|---|---  
Set < > | `Set < >` `<` `Object` `>` |   
  
### updateHoveredInstances#

add a label instance to the hovered instances set

Name | Type | Description  
---|---|---  
WritableAtom < unknown , , void > | `WritableAtom < unknown , , void >` `<` `unknown` `,` `[ newValue ]` `,` `void` `>` |   
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
