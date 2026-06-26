---
source_url: https://docs.voxel51.com/plugins/api/plugins.fiftyone.utilities.html
---

# @fiftyone/utilities#

## Hooks#

### useExternalLink#

@fiftyone/utilities.useExternalLink(_href_)#
    

Arguments:
    

  * **href** ()




### useItemsWithOrderPersistence#

@fiftyone/utilities.useItemsWithOrderPersistence(_items_ , _key_)#
    

Arguments:
    

  * **items** (`Array`)

  * **key** (`string`)



Return type:
    

`Object`

## Functions#

### applyAlpha#

@fiftyone/utilities.applyAlpha(_color_ , _alpha_)#
    

Arguments:
    

  * **color** (`string`)

  * **alpha** (`number`)



Return type:
    

`string`

### buildSimilarityRunName#

@fiftyone/utilities.buildSimilarityRunName(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`Object`)

  * **__namedParameters.hasUploadedImage** (`boolean`)

  * **__namedParameters.isImageSearch** (`boolean`)

  * **__namedParameters.isUpload** (`boolean`)

  * **__namedParameters.negativeQueryIds** (`Array`)

  * **__namedParameters.patchesField** (`string`)

  * **__namedParameters.queryIds** (`Union`)

  * **__namedParameters.textQuery** (`string`)



Return type:
    

`string`

Build a default display name for a similarity search run.

  * Text queries: return the raw query string

  * Upload queries: â1 imageâ / â0 imagesâ

  * Image queries: âN samplesâ / âN patchesâ with optional negative counts




### canPerformAction#

@fiftyone/utilities.canPerformAction(_allowed_ , _readOnly_ , _action_)#
    

Arguments:
    

  * **allowed** (`boolean`)

  * **readOnly** (`boolean`)

  * **action** (`string`)



Return type:
    

`plugins.fiftyone.utilities.CanPerformActionReturnType`

### clearFetchCache#

@fiftyone/utilities.clearFetchCache()#
    

Return type:
    

`void`

Clears cached fetch responses.

### clone#

@fiftyone/utilities.clone(_data_)#
    

Arguments:
    

  * **data** (`T`)



Return type:
    

`plugins.fiftyone.utilities.Mutable` `<` `plugins.fiftyone.utilities.T` `>`

### createColorGenerator#

@fiftyone/utilities.createColorGenerator(_colorPool_ , _seed_)#
    

Arguments:
    

  * **colorPool** (`readonly`)

  * **seed** ()




### createResourceGroup#

@fiftyone/utilities.createResourceGroup()#
    

@fiftyone/utilities.createResourceGroup()#
    

Arguments:
    

  * **key** (`string`)

  * **loader** (`( )`)



Return type:
    

`plugins.fiftyone.utilities.Resource` `<` `plugins.fiftyone.utilities.T` `>`

### dateFromDateString#

@fiftyone/utilities.dateFromDateString(_v_)#
    

Arguments:
    

  * **v** (`string`)



Return type:
    

`number`

### dateFromDateTimeString#

@fiftyone/utilities.dateFromDateTimeString(_timeZone_ , _v_)#
    

Arguments:
    

  * **timeZone** (`string`)

  * **v** (`string`)



Return type:
    

`number`

### determinePathType#

@fiftyone/utilities.determinePathType(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`plugins.fiftyone.utilities.PathType`

### doesSchemaContainEmbeddedDocType#

@fiftyone/utilities.doesSchemaContainEmbeddedDocType(_schema_ , _embeddedDocType_)#
    

Arguments:
    

  * **schema** (`Schema`)

  * **embeddedDocType** (`string`)



Return type:
    

`boolean`

### env#

@fiftyone/utilities.env()#
    

Return type:
    

`ImportMetaEnv`

### formatDate#

@fiftyone/utilities.formatDate(_timeStamp_)#
    

Arguments:
    

  * **timeStamp** (`number`)



Return type:
    

`string`

### formatDatePicker#

@fiftyone/utilities.formatDatePicker(_v_)#
    

Arguments:
    

  * **v** (`number`)



Return type:
    

`string`

### formatDateTime#

@fiftyone/utilities.formatDateTime(_timeStamp_ , _timeZone_)#
    

Arguments:
    

  * **timeStamp** (`number`)

  * **timeZone** (`string`)



Return type:
    

`string`

### formatDateTimePicker#

@fiftyone/utilities.formatDateTimePicker(_timeZone_ , _v_)#
    

Arguments:
    

  * **timeZone** (`string`)

  * **v** (`number`)



Return type:
    

`string`

### formatLongDateTime#

@fiftyone/utilities.formatLongDateTime(_timeStamp_ , _timeZone_)#
    

Arguments:
    

  * **timeStamp** (`number`)

  * **timeZone** (`string`)



Return type:
    

`string`

### formatPrimitive#

@fiftyone/utilities.formatPrimitive(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`Object`)

  * **__namedParameters.ftype** (`string`)

  * **__namedParameters.timeZone** (`string`)

  * **__namedParameters.value** (`Primitive`)



Return type:
    

`Union<` `string` `,` `URL` `>`

### formatValueAsNumber#

@fiftyone/utilities.formatValueAsNumber(_value_ , _fractionDigits_)#
    

Arguments:
    

  * **value** (`Union`)

  * **fractionDigits** (`number`)



Return type:
    

`Union<` `string` `,` `number` `>`

### get32BitColor#

@fiftyone/utilities.get32BitColor(_color_ , _alpha_)#
    

Arguments:
    

  * **color** (`Union`)

  * **alpha** (`number`)



Return type:
    

`number`

### getAPI#

@fiftyone/utilities.getAPI()#
    

Return type:
    

`any`

### getBasename#

@fiftyone/utilities.getBasename(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`any`

### getClickModifiers#

@fiftyone/utilities.getClickModifiers(_event_)#
    

Arguments:
    

  * **event** (`PointerEvent`)



Return type:
    

`plugins.fiftyone.utilities.ClickEventModifiers`

Extract the `ClickEventModifiers` from a `PointerEvent`.

### getCls#

@fiftyone/utilities.getCls(_fieldPath_ , _schema_)#
    

Arguments:
    

  * **fieldPath** (`string`)

  * **schema** (`Schema`)



Return type:
    

`Union<` `string` `,` `undefined` `>`

### getColor#

@fiftyone/utilities.getColor(_pool_ , _seed_ , _fieldOrValue_)#
    

Arguments:
    

  * **pool** (`readonly`)

  * **seed** (`number`)

  * **fieldOrValue** (`Union`)



Return type:
    

`string`

### getColorscaleArray#

@fiftyone/utilities.getColorscaleArray(_colorscale_ , _alpha_)#
    

Arguments:
    

  * **colorscale** (`Array`)

  * **alpha** (`number`)



Return type:
    

`Readonly < Uint32Array >` `<` `Uint32Array` `>`

### getDenseLabelNames#

@fiftyone/utilities.getDenseLabelNames(_schema_)#
    

Arguments:
    

  * **schema** (`Schema`)



Return type:
    

`Array<` `string` `>`

### getEventSource#

@fiftyone/utilities.getEventSource(_path_ , _events_ , _signal_ , _body_)#
    

Arguments:
    

  * **path** (`string`)

  * **events** (`Object`)

  * **events.onclose** (`( )`)

  * **events.onerror** (`( error : Error )`)

  * **events.onmessage** (`( event : EventSourceMessage )`)

  * **events.onopen** (`( )`)

  * **signal** (`AbortSignal`)

  * **body** (`Any`)



Return type:
    

`void`

### getFetchFunction#

@fiftyone/utilities.getFetchFunction(_options_)#
    

Arguments:
    

  * **options** (`GetFetchFunctionOptions`)



Return type:
    

`plugins.fiftyone.utilities.FetchFunction`

Returns the configured fetch function singleton.

### getFetchFunctionExtended#

@fiftyone/utilities.getFetchFunctionExtended()#
    

Wrapper for `getFetchFunction` which provides response headers and configuration via `FetchFunctionConfig`.

> @fiftyone/utilities.getFetchFunctionExtended()#
>     
> 
> Arguments:
>     
> 
>   * **config** (`FetchFunctionConfig`)
> 
> 

> Return type:
>     
> 
> `Promise < FetchFunctionResult >` `<` `plugins.fiftyone.utilities.FetchFunctionResult` `>`

### getFetchHeaders#

@fiftyone/utilities.getFetchHeaders()#
    

Return type:
    

`HeadersInit`

### getFetchOrigin#

@fiftyone/utilities.getFetchOrigin()#
    

Return type:
    

`any`

### getFetchParameters#

@fiftyone/utilities.getFetchParameters()#
    

Return type:
    

`Object`

### getFetchPathPrefix#

@fiftyone/utilities.getFetchPathPrefix()#
    

Return type:
    

`string`

### getFieldInfo#

@fiftyone/utilities.getFieldInfo(_fieldPath_ , _schema_)#
    

Arguments:
    

  * **fieldPath** (`string`)

  * **schema** (`Schema`)



Return type:
    

`Union<` `plugins.fiftyone.utilities.Field` `,` `undefined` `>`

### getFieldsWithEmbeddedDocType#

@fiftyone/utilities.getFieldsWithEmbeddedDocType(_schema_ , _embeddedDocType_ , _shouldRecurse_)#
    

Arguments:
    

  * **schema** (`Schema`)

  * **embeddedDocType** (`Union`)

  * **shouldRecurse** (`boolean`)



Return type:
    

`Array<` `plugins.fiftyone.utilities.Field` `>`

### getMimeType#

@fiftyone/utilities.getMimeType(_sample_)#
    

Arguments:
    

  * **sample** (`Sample`)



Return type:
    

`string`

### getProtocol#

@fiftyone/utilities.getProtocol(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`string`

### getRGB#

@fiftyone/utilities.getRGB(_color_)#
    

Arguments:
    

  * **color** (`string`)



Return type:
    

`plugins.fiftyone.utilities.RGB`

### getRGBA#

@fiftyone/utilities.getRGBA(_value_)#
    

Arguments:
    

  * **value** (`number`)



Return type:
    

`plugins.fiftyone.utilities.RGBA`

### getRGBAColor#

@fiftyone/utilities.getRGBAColor(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`RGBA`)



Return type:
    

`string`

### getRootOrProtocol#

@fiftyone/utilities.getRootOrProtocol(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`any`

### getSamplePathExtension#

@fiftyone/utilities.getSamplePathExtension(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`string`

Returns the normalized file extension for a sample path or media URL.

Supports raw filepaths as well as direct asset URLs

### getSeparator#

@fiftyone/utilities.getSeparator(_pathType_)#
    

Arguments:
    

  * **pathType** (`PathType`)



Return type:
    

`string`

### hasValidBounds#

@fiftyone/utilities.hasValidBounds(_boundingBox_)#
    

Arguments:
    

  * **boundingBox** (`[ number , number , number , number ]`)



Return type:
    

`boolean`

Checks whether a bounding box has finite bounds with a positive width and height.

### hexToRgb#

@fiftyone/utilities.hexToRgb(_hex_)#
    

Arguments:
    

  * **hex** (`string`)



Return type:
    

`plugins.fiftyone.utilities.RGB`

### humanReadableBytes#

@fiftyone/utilities.humanReadableBytes(_bytes_)#
    

Arguments:
    

  * **bytes** (`number`)



Return type:
    

`string`

### interpolateColorsHex#

@fiftyone/utilities.interpolateColorsHex(_color1_ , _color2_ , _factor_)#
    

Arguments:
    

  * **color1** (`string`)

  * **color2** (`string`)

  * **factor** (`number`)



Return type:
    

`string`

### interpolateColorsRgb#

@fiftyone/utilities.interpolateColorsRgb(_rgb1_ , _rgb2_ , _factor_)#
    

Arguments:
    

  * **rgb1** (`RGB`)

  * **rgb2** (`RGB`)

  * **factor** (`number`)



Return type:
    

`plugins.fiftyone.utilities.RGB`

### is3d#

@fiftyone/utilities.is3d(_mediaType_)#
    

Arguments:
    

  * **mediaType** (`string`)



Return type:
    

`boolean`

Returns true if the provided media type is FO3D or point cloud.

### isAnnotationSupported#

@fiftyone/utilities.isAnnotationSupported(_mediaType_)#
    

Arguments:
    

  * **mediaType** (`string`)



Return type:
    

`boolean`

Returns true if annotation is supported for the provided media type.

### isDirect3dSamplePath#

@fiftyone/utilities.isDirect3dSamplePath(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`boolean`

Returns true when the provided sample path points to a supported direct 3D asset.

### isFo3d#

@fiftyone/utilities.isFo3d(_mediaType_)#
    

Arguments:
    

  * **mediaType** (`string`)



Return type:
    

`boolean`

Returns true if the provided media type is associated with FO3D.

### isFo3dSamplePath#

@fiftyone/utilities.isFo3dSamplePath(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`boolean`

Returns true when the provided sample path points to a real FO3D scene file.

### isFunctionalComponent#

@fiftyone/utilities.isFunctionalComponent(_value_)#
    

Arguments:
    

  * **value** (`unknown`)



Return type:
    

### isHex#

@fiftyone/utilities.isHex(_value_)#
    

Arguments:
    

  * **value** (`string`)



Return type:
    

`boolean`

### isNotebook#

@fiftyone/utilities.isNotebook()#
    

Return type:
    

`boolean`

### isNullish#

@fiftyone/utilities.isNullish(_value_)#
    

Arguments:
    

  * **value** (`any`)



Return type:
    

`boolean`

### isObject#

@fiftyone/utilities.isObject(_data_)#
    

Arguments:
    

  * **data** (`unknown`)



Return type:
    

Return true if the provided data is an object.

### isObjectIdString#

@fiftyone/utilities.isObjectIdString(_value_ , _strict_)#
    

Arguments:
    

  * **value** (`string`)

  * **strict** (`boolean`)



Return type:
    

`boolean`

### isPointCloud#

@fiftyone/utilities.isPointCloud(_mediaType_)#
    

Arguments:
    

  * **mediaType** (`string`)



Return type:
    

`boolean`

Returns true if the provided media type is associated with point clouds.

### isPrimitiveString#

@fiftyone/utilities.isPrimitiveString(_value_)#
    

Arguments:
    

  * **value** (`unknown`)



Return type:
    

`boolean`

### isPrimitiveType#

@fiftyone/utilities.isPrimitiveType(_type_)#
    

Arguments:
    

  * **type** (`string`)



Return type:
    

`boolean`

### isWrappableDirect3dSamplePath#

@fiftyone/utilities.isWrappableDirect3dSamplePath(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`boolean`

Returns true when the provided sample path points to a direct 3D asset that can be wrapped into a synthetic FO3D scene.

### joinPaths#

@fiftyone/utilities.joinPaths(_paths_)#
    

Arguments:
    

  * **paths** (`Array`)



Return type:
    

`string`

### makePseudoField#

@fiftyone/utilities.makePseudoField(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`plugins.fiftyone.utilities.Field`

### meetsFieldType#

@fiftyone/utilities.meetsFieldType(_field_ , ___namedParameters_)#
    

Arguments:
    

  * **field** (`Field`)

  * **__namedParameters** (`Object`)

  * **__namedParameters.acceptLists** (`boolean`)

  * **__namedParameters.embeddedDocType** (`Union`)

  * **__namedParameters.ftype** (`Union`)



Return type:
    

`boolean`

### mergeHeaders#

@fiftyone/utilities.mergeHeaders(_headers_)#
    

Arguments:
    

  * **headers** (`Array`)



Return type:
    

`Record < string , string >` `<` `string` `,` `string` `>`

### move#

@fiftyone/utilities.move(_array_ , _moveIndex_ , _toIndex_)#
    

Arguments:
    

  * **array** (`Array`)

  * **moveIndex** (`number`)

  * **toIndex** (`number`)



Return type:
    

`Array<` `plugins.fiftyone.utilities.T` `>`

### objectId#

@fiftyone/utilities.objectId()#
    

Return type:
    

`string`

Utility to generate mongo-like ObjectId

### pluralize#

@fiftyone/utilities.pluralize(_number_ , _singular_ , _plural_)#
    

Arguments:
    

  * **number** (`number`)

  * **singular** (`Union`)

  * **plural** (`Union`)



Return type:
    

`Union<` `string` `,` `Element` `>`

### pluralizeUnit#

@fiftyone/utilities.pluralizeUnit(_count_ , _unit_)#
    

Arguments:
    

  * **count** (`number`)

  * **unit** (`string`)



Return type:
    

`string`

Pluralize a unit string: adds âsâ for most words, âesâ for âpatchâ.

### prettify#

@fiftyone/utilities.prettify(_v_)#
    

Arguments:
    

  * **v** (`Union`)



Return type:
    

`Union<` `string` `,` `URL` `>`

### removeKeys#

@fiftyone/utilities.removeKeys(_obj_ , _keys_ , _startsWith_)#
    

Arguments:
    

  * **obj** (`KeyValue`)

  * **keys** (`Iterable`)

  * **startsWith** (`boolean`)



Return type:
    

`plugins.fiftyone.utilities.KeyValue` `<` `plugins.fiftyone.utilities.T` `>`

### resolveAncestors#

@fiftyone/utilities.resolveAncestors(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`Array<` `string` `>`

### resolveParent#

@fiftyone/utilities.resolveParent(_path_)#
    

Arguments:
    

  * **path** (`string`)



Return type:
    

`string`

### rgbStringToHex#

@fiftyone/utilities.rgbStringToHex(_rgb_)#
    

Arguments:
    

  * **rgb** (`string`)



Return type:
    

`string`

Convert RGB string to hex

**Returns**

hex string (e.g. â#ffffffâ)

**Throws**

if the RGB string is invalid

### rgbToHexCached#

@fiftyone/utilities.rgbToHexCached(_color_)#
    

Arguments:
    

  * **color** (`RGB`)



Return type:
    

`any`

### sendEvent#

@fiftyone/utilities.sendEvent(_data_)#
    

Arguments:
    

  * **data** (`Any`)



Return type:
    

`Promise < unknown >` `<` `unknown` `>`

### setContains3d#

@fiftyone/utilities.setContains3d(_mediaTypes_)#
    

Arguments:
    

  * **mediaTypes** (`Set`)



Return type:
    

`boolean`

Returns true if the provided set contains any media types which are associated with FO3D or point clouds.

### setContainsFo3d#

@fiftyone/utilities.setContainsFo3d(_mediaTypes_)#
    

Arguments:
    

  * **mediaTypes** (`Set`)



Return type:
    

`boolean`

Returns true if the provided set contains any media types which are associated with FO3D.

### setContainsPointCloud#

@fiftyone/utilities.setContainsPointCloud(_mediaTypes_)#
    

Arguments:
    

  * **mediaTypes** (`Set`)



Return type:
    

`boolean`

Returns true if the provided set contains any media types which are associated with point clouds.

### setFetchFunction#

@fiftyone/utilities.setFetchFunction(_origin_ , _defaultHeaders_ , _pathPrefix_)#
    

Arguments:
    

  * **origin** (`string`)

  * **defaultHeaders** (`HeadersInit`)

  * **pathPrefix** (`string`)



Return type:
    

`void`

### setFetchParameters#

@fiftyone/utilities.setFetchParameters(_origin_ , _headers_ , _pathPrefix_)#
    

Arguments:
    

  * **origin** (`string`)

  * **headers** (`HeadersInit`)

  * **pathPrefix** (`string`)



Return type:
    

`void`

### sizeBytesEstimate#

@fiftyone/utilities.sizeBytesEstimate(_object_)#
    

Arguments:
    

  * **object** (`SizeTypes`)



Return type:
    

`number`

### toCamelCase#

@fiftyone/utilities.toCamelCase(_obj_)#
    

Arguments:
    

  * **obj** (`O`)



Return type:
    

`plugins.fiftyone.utilities.O`

### toSlug#

@fiftyone/utilities.toSlug(_name_)#
    

Arguments:
    

  * **name** (`string`)



Return type:
    

`string`

### toSnakeCase#

@fiftyone/utilities.toSnakeCase(_obj_)#
    

Arguments:
    

  * **obj** (`O`)



Return type:
    

`plugins.fiftyone.utilities.O`

### withPath#

@fiftyone/utilities.withPath(_path_ , _types_)#
    

Arguments:
    

  * **path** (`string`)

  * **types** (`string`)



Return type:
    

`string`

@fiftyone/utilities.withPath(_path_ , _types_)#
    

Arguments:
    

  * **path** (`string`)

  * **types** (`Array`)



Return type:
    

`Array<` `string` `>`

## Types#

### APP_MODE#

Name | Type | Description  
---|---|---  
`'fiftyone'` |  |   
  
### ARRAY_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.ArrayField'` |  |   
  
### BOOK_A_DEMO_LINK#

Name | Type | Description  
---|---|---  
`'https://voxel51.com/book-a-demo/?utm_medium=referral&utm_source=opensource'` |  |   
  
### BOOLEAN_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.BooleanField'` |  |   
  
### CLASSIFICATIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Classifications'` |  |   
  
### CLASSIFICATION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Classification'` |  |   
  
### DATE_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DateField'` |  |   
  
### DATE_TIME_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DateTimeField'` |  |   
  
### DETECTIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detections'` |  |   
  
### DETECTION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detection'` |  |   
  
### DETECTION_FILED#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detection'` |  |   
  
### DICT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DictField'` |  |   
  
### DYNAMIC_EMBEDDED_DOCUMENT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DynamicEmbeddedDocumentField'` |  |   
  
### DYNAMIC_EMBEDDED_DOCUMENT_PATH#

Name | Type | Description  
---|---|---  
`'fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument'` |  |   
  
### EMBEDDED_DOCUMENT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.EmbeddedDocumentField'` |  |   
  
### FLOAT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.FloatField'` |  |   
  
### FRAME_NUMBER_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.FrameNumberField'` |  |   
  
### FRAME_SUPPORT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.FrameSupportField'` |  |   
  
### GEO_LOCATIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.GeoLocations'` |  |   
  
### GEO_LOCATION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.GeoLocation'` |  |   
  
### GROUP#

Name | Type | Description  
---|---|---  
`'fiftyone.core.groups.Group'` |  |   
  
### HEATMAP_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Heatmap'` |  |   
  
### INT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.IntField'` |  |   
  
### IS_APP_MODE_FIFTYONE#

Name | Type | Description  
---|---|---  
`boolean` |  |   
  
### JUST_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.Field'` |  |   
  
### KEYPOINTS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Keypoints'` |  |   
  
### KEYPOINTS_POINTS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.KeypointsField'` |  |   
  
### KEYPOINT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Keypoint'` |  |   
  
### LIST_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.ListField'` |  |   
  
### OBJECT_ID_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.ObjectIdField'` |  |   
  
### POLYLINES_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Polylines'` |  |   
  
### POLYLINE_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Polyline'` |  |   
  
### REGRESSION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Regression'` |  |   
  
### SEGMENTATION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Segmentation'` |  |   
  
### STRING_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.StringField'` |  |   
  
### TEMPORAL_DETECTIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.TemporalDetections'` |  |   
  
### TEMPORAL_DETECTION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.TemporalDetection'` |  |   
  
### TRY_IN_BROWSER_LINK#

Name | Type | Description  
---|---|---  
`'https://voxel51.com/try-fiftyone/'` |  |   
  
### UUID_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.UUIDField'` |  |   
  
### VECTOR_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.VectorField'` |  |   
  
### scrollbarStyles#

Name | Type | Description  
---|---|---  
`'\n--scrollbar-color: var(--fo-palette-text-tertiary);\n\n@-moz-document url-prefix() {\n & {\n scrollbar-color: var(--scrollbar-color) transparent;\n scrollbar-width: thin;\n }\n}\n\n&::-webkit-scrollbar {\n height: 14px;\n width: 14px;\n}\n\n&::-webkit-scrollbar-corner {\n background: transparent;\n}\n\n&::-webkit-scrollbar-track {\n box-shadow: inset 0 0 14px 14px transparent;\n height: 14px;\n width: 14px;\n}\n\n&::-webkit-scrollbar-thumb {\n border: solid 3px transparent;\n border-radius: 0;\n box-shadow: inset 0 0 8px 8px var(--scrollbar-color);\n}\n'` |  |   
  
### DateTimeInput#

@fiftyone/utilities.DateTimeInput(_props_)#
    

Arguments:
    

  * **props** (`PolymorphicComponentProps`)



Return type:
    

`Element`

@fiftyone/utilities.DateTimeInput(_props_)#
    

Arguments:
    

  * **props** (`FastOmit`)



Return type:
    

`ReactElement < any , >` `<` `any` `,` `Union< string , JSXElementConstructor >` `>`

**NOTE** : Exotic components are not callable.

### DateTimeInputContainer#

@fiftyone/utilities.DateTimeInputContainer(_props_)#
    

Arguments:
    

  * **props** (`PolymorphicComponentProps`)



Return type:
    

`Element`

@fiftyone/utilities.DateTimeInputContainer(_props_)#
    

Arguments:
    

  * **props** (`FastOmit`)



Return type:
    

`ReactElement < any , >` `<` `any` `,` `Union< string , JSXElementConstructor >` `>`

**NOTE** : Exotic components are not callable.

### FetchFunction#

class @fiftyone/utilities.FetchFunction()#
    

### FetchFunctionExtended#

class @fiftyone/utilities.FetchFunctionExtended()#
    

### Field#

class @fiftyone/utilities.Field()#
    

#### Properties#

Name | Type | Description  
---|---|---  
dbField | `string` |   
description | `string` |   
embeddedDocType | `string` |   
fields | `plugins.fiftyone.utilities.Schema` |   
ftype | `string` |   
info | `object` |   
name | `string` |   
path | `string` |   
pathWithDbField | `string` |   
readOnly | `boolean` |   
subfield | `string` |   
  
### GQLError#

class @fiftyone/utilities.GQLError()#
    

#### Properties#

Name | Type | Description  
---|---|---  
extensions | `Object` |   
message | `string` |   
paths | `Array<` `string` `>` |   
  
### Schema#

class @fiftyone/utilities.Schema()#
    

Name | Type | Description  
---|---|---  
[key] | `string` |   
  
### Stage#

class @fiftyone/utilities.Stage()#
    

#### Properties#

Name | Type | Description  
---|---|---  
kwargs | `Array<` `[` `string` `,` `object` `]` `>` |   
  
### StrictField#

class @fiftyone/utilities.StrictField()#
    

#### Properties#

Name | Type | Description  
---|---|---  
dbField | `string` |   
description | `string` |   
embeddedDocType | `string` |   
fields | `Array<` `plugins.fiftyone.utilities.StrictField` `>` |   
ftype | `string` |   
info | `object` |   
name | `string` |   
path | `string` |   
pathWithDbField | `string` |   
readOnly | `boolean` |   
subfield | `string` |   
  
class @fiftyone/utilities.BufferRange()#
    

### BufferRange#

Name | Type | Description  
---|---|---  
BufferRange | `Readonly < >` `<` `[ number , number ]` `>` |   
  
class @fiftyone/utilities.Buffers()#
    

### Buffers#

class @fiftyone/utilities.ClickEventModifiers()#
    

### ClickEventModifiers#

Modifier flags associated with a `PointerEvent`.

Name | Type | Description  
---|---|---  
ClickEventModifiers.altKey | `boolean` |   
ClickEventModifiers.ctrlKey | `boolean` |   
ClickEventModifiers.metaKey | `boolean` |   
ClickEventModifiers.shiftKey | `boolean` |   
  
class @fiftyone/utilities.FetchFunctionConfig()#
    

### FetchFunctionConfig#

Configuration for a `fetch` call.

derived from the request method, path, and body.â
    

âFetchFunctionConfig.errorHandlerâ,â`(` `response` `:` `Response` `)`â âFetchFunctionConfig.headersâ,â`Record < string , string >` `<` `string` `,` `string` `>`â âFetchFunctionConfig.methodâ,â`string`â âFetchFunctionConfig.pathâ,â`string`â âFetchFunctionConfig.resultâ,â`plugins.fiftyone.utilities.FetchResultType`â âFetchFunctionConfig.retriesâ,â`number`â âFetchFunctionConfig.retryCodesâ,â`Array<` `number` `>`â

class @fiftyone/utilities.FetchFunctionResult()#
    

### FetchFunctionResult#

Parsed fetch response with response headers.

Name | Type | Description  
---|---|---  
FetchFunctionResult.headers | `Headers` |   
FetchFunctionResult.response | `plugins.fiftyone.utilities.T` |   
  
class @fiftyone/utilities.FetchResultType()#
    

### FetchResultType#

Supported methods for accessing response data.

Union of `'json'`, `'blob'`, `'text'`, `'arrayBuffer'`, `'json-stream'`

class @fiftyone/utilities.GetFetchFunctionOptions()#
    

### GetFetchFunctionOptions#

Options for `getFetchFunction`.

derived from the request method, path, and body.â

class @fiftyone/utilities.NumberKeyObjectType()#
    

### NumberKeyObjectType#

class @fiftyone/utilities.Primitive()#
    

### Primitive#

Union of `number`, `null`, `string`, `undefined`, `Object`

class @fiftyone/utilities.RGB()#
    

### RGB#

Copyright 2017-2026, Voxel51, Inc.

Name | Type | Description  
---|---|---  
RGB | `[` `number` `,` `number` `,` `number` `]` |   
  
class @fiftyone/utilities.RGBA()#
    

### RGBA#

Name | Type | Description  
---|---|---  
RGBA | `[` `number` `,` `number` `,` `number` `,` `number` `]` |   
  
class @fiftyone/utilities.SerializedMask()#
    

### SerializedMask#

Segmentation mask â base64-encoded compressed numpy array, or MongoDB binary wrapper.

Union of `string`, `Object`

## Enums#

### COLOR_BY#

Name | Value  
---|---  
FIELD |   
INSTANCE |   
VALUE |   
  
### PathType#

Name | Value  
---|---  
LINUX |   
URL |   
WINDOWS |   
  
## Variables#

### AGGS#

Name | Type | Description  
---|---|---  
BOUNDS | `string` |   
COUNT | `string` |   
COUNT_VALUES | `string` |   
DISTINCT | `string` |   
  
### ARRAY_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.ArrayField'` |  |   
  
### BIG_ENDIAN#

Name | Type | Description  
---|---|---  
`boolean` |  |   
  
### BOOLEAN_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.BooleanField'` |  |   
  
### BUILT_IN_PANEL_PRIORITY_CONST#

Name | Type | Description  
---|---|---  
`51000` |  |   
  
### CLASSIFICATION#

Name | Type | Description  
---|---|---  
`'Classification'` |  |   
  
### CLASSIFICATIONS#

Name | Type | Description  
---|---|---  
`'Classifications'` |  |   
  
### CLASSIFICATIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Classifications'` |  |   
  
### CLASSIFICATION_DISABLED_SUB_PATHS#

### CLASSIFICATION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Classification'` |  |   
  
### CLIPS_FRAME_FIELDS#

### CLIPS_SAMPLE_FIELDS#

### DATE_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DateField'` |  |   
  
### DATE_TIME_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DateTimeField'` |  |   
  
### DENSE_LABELS#

Name | Type | Description  
---|---|---  
Set < string > | `Set < string >` `<` `string` `>` |   
  
### DENSE_LABEL_EMBEDDED_DOC_TYPES#

### DETECTION#

Name | Type | Description  
---|---|---  
`'Detection'` |  |   
  
### DETECTIONS#

Name | Type | Description  
---|---|---  
`'Detections'` |  |   
  
### DETECTIONS_EMBEDDED_DOC_TYPE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detections'` |  |   
  
### DETECTIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detections'` |  |   
  
### DETECTION_DISABLED_SUB_PATHS#

### DETECTION_EMBEDDED_DOC_TYPE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detection'` |  |   
  
### DETECTION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detection'` |  |   
  
### DETECTION_FILED#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Detection'` |  |   
  
### DICT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DictField'` |  |   
  
### DISABLED_LABEL_FIELDS_VISIBILITY#

### DISABLED_PATHS#

### DYNAMIC_EMBEDDED_DOCUMENT#

Name | Type | Description  
---|---|---  
`'DynamicEmbeddedDocument'` |  |   
  
### DYNAMIC_EMBEDDED_DOCUMENT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.DynamicEmbeddedDocumentField'` |  |   
  
### DYNAMIC_EMBEDDED_DOCUMENT_PATH#

Name | Type | Description  
---|---|---  
`'fiftyone.core.odm.embedded_document.DynamicEmbeddedDocument'` |  |   
  
### DYNAMIC_GROUP_FIELDS#

### EMBEDDED_DOCUMENT#

Name | Type | Description  
---|---|---  
`'EmbeddedDocument'` |  |   
  
### EMBEDDED_DOCUMENT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.EmbeddedDocumentField'` |  |   
  
### FLOAT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.FloatField'` |  |   
  
### FRAME_NUMBER_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.FrameNumberField'` |  |   
  
### FRAME_SUPPORT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.FrameSupportField'` |  |   
  
### GEOLOCATION#

Name | Type | Description  
---|---|---  
`'GeoLocation'` |  |   
  
### GEOLOCATIONS#

Name | Type | Description  
---|---|---  
`'GeoLocations'` |  |   
  
### GEOLOCATIONS_DISABLED_SUB_PATHS#

### GEOLOCATION_DISABLED_SUB_PATHS#

### GEO_LOCATIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.GeoLocations'` |  |   
  
### GEO_LOCATION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.GeoLocation'` |  |   
  
### GROUP#

Name | Type | Description  
---|---|---  
`'fiftyone.core.groups.Group'` |  |   
  
### HEATMAP#

Name | Type | Description  
---|---|---  
`'Heatmap'` |  |   
  
### HEATMAP_DISABLED_SUB_PATHS#

### HEATMAP_EMBEDDED_DOC_TYPE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Heatmap'` |  |   
  
### HEATMAP_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Heatmap'` |  |   
  
### INPUT_TYPE_DATE#

Name | Type | Description  
---|---|---  
`'date'` |  |   
  
### INPUT_TYPE_DATE_TIME#

Name | Type | Description  
---|---|---  
`'datetime-local'` |  |   
  
### INT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.IntField'` |  |   
  
### JUST_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.Field'` |  |   
  
### KEYPOINT#

Name | Type | Description  
---|---|---  
`'Keypoint'` |  |   
  
### KEYPOINTS#

Name | Type | Description  
---|---|---  
`'Keypoints'` |  |   
  
### KEYPOINTS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Keypoints'` |  |   
  
### KEYPOINTS_POINTS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.KeypointsField'` |  |   
  
### KEYPOINT_DISABLED_SUB_PATHS#

### KEYPOINT_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Keypoint'` |  |   
  
### LABELS#

### LABELS_MAP#

Name | Type | Description  
---|---|---  
Classification | `string` |   
Classifications | `string` |   
Detection | `string` |   
Detections | `string` |   
GeoLocation | `string` |   
GeoLocations | `string` |   
Heatmap | `string` |   
Keypoint | `string` |   
Keypoints | `string` |   
Polyline | `string` |   
Polylines | `string` |   
Regression | `string` |   
Segmentation | `string` |   
TemporalDetection | `string` |   
TemporalDetections | `string` |   
  
### LABELS_PATH#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels'` |  |   
  
### LABEL_DOC_TYPES#

### LABEL_LIST#

Name | Type | Description  
---|---|---  
Classifications | `string` |   
Detections | `string` |   
Keypoints | `string` |   
Polylines | `string` |   
TemporalDetections | `string` |   
  
### LABEL_LISTS#

### LABEL_LISTS_MAP#

Name | Type | Description  
---|---|---  
Classifications | `string` |   
Detections | `string` |   
Keypoints | `string` |   
Polylines | `string` |   
TemporalDetections | `string` |   
  
### LABEL_LIST_PATH#

### LIST_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.ListField'` |  |   
  
### MASK_LABELS#

Name | Type | Description  
---|---|---  
Set < string > | `Set < string >` `<` `string` `>` |   
  
### NONFINITES#

Name | Type | Description  
---|---|---  
Set < string > | `Set < string >` `<` `string` `>` |   
  
### NOT_VISIBLE_LIST#

### OBJECT_ID_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.ObjectIdField'` |  |   
  
### PATCHES_FIELDS#

### POLYLINE#

Name | Type | Description  
---|---|---  
`'Polyline'` |  |   
  
### POLYLINES#

Name | Type | Description  
---|---|---  
`'Polylines'` |  |   
  
### POLYLINES_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Polylines'` |  |   
  
### POLYLINE_DISABLED_SUB_PATHS#

### POLYLINE_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Polyline'` |  |   
  
### PRIMITIVE#

Name | Type | Description  
---|---|---  
`'Primitive'` |  |   
  
### PRIMITIVES#

Name | Type | Description  
---|---|---  
`'Primitives'` |  |   
  
### REGRESSION#

Name | Type | Description  
---|---|---  
`'Regression'` |  |   
  
### REGRESSION_DISABLED_SUB_PATHS#

### REGRESSION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Regression'` |  |   
  
### RESERVED_FIELD_KEYS#

### SEGMENTATION#

Name | Type | Description  
---|---|---  
`'Segmentation'` |  |   
  
### SEGMENTATION_DISABLED_SUB_PATHS#

### SEGMENTATION_EMBEDDED_DOC_TYPE#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Segmentation'` |  |   
  
### SEGMENTATION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.Segmentation'` |  |   
  
### SKIP_FIELD_TYPES#

### STRING_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.StringField'` |  |   
  
### TEMPORAL_DETECTION#

Name | Type | Description  
---|---|---  
`'TemporalDetection'` |  |   
  
### TEMPORAL_DETECTIONS#

Name | Type | Description  
---|---|---  
`'TemporalDetections'` |  |   
  
### TEMPORAL_DETECTIONS_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.TemporalDetections'` |  |   
  
### TEMPORAL_DETECTION_DISABLED_SUB_PATHS#

### TEMPORAL_DETECTION_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.labels.TemporalDetection'` |  |   
  
### UNSUPPORTED_FILTER_TYPES#

### UUID_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.UUIDField'` |  |   
  
### VALID_CLASS_TYPES#

### VALID_DISTRIBUTION_TYPES#

### VALID_KEYPOINTS#

### VALID_LABEL_TYPES#

### VALID_LIST_FIELDS#

### VALID_LIST_LABEL_FIELDS#

### VALID_LIST_TYPES#

### VALID_MASK_TYPES#

### VALID_NON_LIST_LABEL_TYPES#

### VALID_NUMERIC_TYPES#

### VALID_OBJECT_TYPES#

### VALID_PRIMITIVE_TYPES#

### VECTOR_FIELD#

Name | Type | Description  
---|---|---  
`'fiftyone.core.fields.VectorField'` |  |   
  
### default_app_color#

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
