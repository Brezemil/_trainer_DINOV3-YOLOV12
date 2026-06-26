---
source_url: https://docs.voxel51.com/plugins/api/plugins.fiftyone.operators.html
---

# @fiftyone/operators#

## Hooks#

### useFirstExistingUri#

@fiftyone/operators.useFirstExistingUri(_uris_)#
    

Arguments:
    

  * **uris** (`Array`)



Return type:
    

`Object`

### useGlobalExecutionContext#

@fiftyone/operators.useGlobalExecutionContext()#
    

Return type:
    

`plugins.fiftyone.operators.ExecutionContext`

### useOperatorBrowser#

@fiftyone/operators.useOperatorBrowser()#
    

Return type:
    

`Object`

### useOperatorExecutor#

@fiftyone/operators.useOperatorExecutor(_uri_ , _handlers_)#
    

Arguments:
    

  * **uri** (`any`)

  * **handlers** (`any`)



Return type:
    

`Object`

**Returns**

An object containing the state of the operator execution.

Example:
    
    
    const defaultParams = {
      // default parameters of the operator
      param1: "value1",
      param2: "value2",
    };
    const paramOverrides = {
      // override the parameters of the operator
      param1: "value1-override",
    };
    const handlers = {
      onSuccess: (result: OperatorResult, opts: OperatorExecutorOptions) => {
        // do something with the success
      },
      onError: (error: OperatorResult, opts: OperatorExecutorOptions) => {
        // do something with the error
      }
    };
    const executor = useOperatorExecutor("my-operator", handlers);
    const myBtnCb = useCallback(() => {
      const opts: OperatorExecutorOptions = {
        skipErrorNotification: true,
        callback: (result: OperatorResult, opts: OperatorExecutorOptions) => {
          if (result.error) {
            // do something with the error
          }
        }
      };
      executor.execute(paramOverrides, opts);
    }, [executor]);
    

### useOperatorPlacements#

@fiftyone/operators.useOperatorPlacements(_place_)#
    

Arguments:
    

  * **place** (`Places`)



Return type:
    

`Object`

### useOperators#

@fiftyone/operators.useOperators(_datasetLess_)#
    

Arguments:
    

  * **datasetLess** (`boolean`)



Return type:
    

`Object`

Load built-in and installed JavaScript and Python operators and queue all
    

start-up operators for execution.

### usePanelEvent#

@fiftyone/operators.usePanelEvent()#
    

Return type:
    

`plugins.fiftyone.operators.TriggerEventFn`

A hook that can be used to trigger an operator on a panel.

**Returns**

A function that can be used to trigger an operator on a panel.

Example:
    
    
    const panelId = usePanelId();
    const triggerEvent = usePanelEvent();
    triggerEvent(panelId, {
      operator: "@voxel51/plugin/operator#event",
      params: { param1: "value1" },
    });
    

### usePromptOperatorInput#

@fiftyone/operators.usePromptOperatorInput()#
    

@fiftyone/operators.promptOperatorInput()#
    

Arguments:
    

  * **operatorName** (`any`)

  * **params** (`Any`)

  * **options** (`Any`)



Return type:
    

`void`

### useTriggerPanelEvent#

@fiftyone/operators.useTriggerPanelEvent()#
    

@fiftyone/operators.triggerPanelEvent()#
    

Arguments:
    

  * **event** (`string`)

  * **params** (`ParamsType`)

  * **prompt** (`boolean`)

  * **callback** (`ExecutionCallback`)



Return type:
    

`void`

## Functions#

### OperatorBrowser#

@fiftyone/operators.OperatorBrowser()#
    

Return type:
    

`ReactPortal`

### OperatorCore#

@fiftyone/operators.OperatorCore()#
    

Return type:
    

`Element`

### OperatorExecutionButton#

@fiftyone/operators.OperatorExecutionButton(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`Object`)

  * **__namedParameters.children** (`ReactNode`)

  * **__namedParameters.disabled** (`boolean`)

  * **__namedParameters.executionParams** (`object`)

  * **__namedParameters.insideModal** (`boolean`)

  * **__namedParameters.menuAnchorOrigin** (`Object`)

  * **__namedParameters.menuTransformOrigin** (`Object`)

  * **__namedParameters.onClick** (`( )`)

  * **__namedParameters.onError** (`ExecutionErrorCallback`)

  * **__namedParameters.onOptionSelected** (`( option : OperatorExecutionOption )`)

  * **__namedParameters.onSuccess** (`ExecutionCallback`)

  * **__namedParameters.operatorUri** (`string`)



Return type:
    

`Element`

Button which acts as a trigger for opening an `OperatorExecutionMenu`.

### OperatorIO#

@fiftyone/operators.OperatorIO(_props_)#
    

Arguments:
    

  * **props** (`any`)



Return type:
    

`Element`

### OperatorInvocationRequestExecutor#

@fiftyone/operators.OperatorInvocationRequestExecutor()#
    

Return type:
    

`Element`

### OperatorPlacementWithErrorBoundary#

@fiftyone/operators.OperatorPlacementWithErrorBoundary(_props_)#
    

Arguments:
    

  * **props** (`OperatorPlacementProps`)



Return type:
    

`Element`

### OperatorPlacements#

@fiftyone/operators.OperatorPlacements(_props_)#
    

Arguments:
    

  * **props** (`OperatorPlacementsProps`)



Return type:
    

`Element`

### OperatorPrompt#

@fiftyone/operators.OperatorPrompt()#
    

Return type:
    

`Element`

### OperatorPromptArea#

@fiftyone/operators.OperatorPromptArea(_props_)#
    

Arguments:
    

  * **props** (`OperatorPromptAreaPropsType`)



Return type:
    

`Element`

### abortOperationsByExpression#

@fiftyone/operators.abortOperationsByExpression(_expression_)#
    

Arguments:
    

  * **expression** (`any`)



Return type:
    

`void`

Cancels all abortable operations that match the given expression.

### abortOperationsByURI#

@fiftyone/operators.abortOperationsByURI(_uri_)#
    

Arguments:
    

  * **uri** (`any`)



Return type:
    

`void`

Cancels all abortable operations started by the operator with the given uri.

### executeOperator#

@fiftyone/operators.executeOperator(_uri_ , _params_ , _options_)#
    

Arguments:
    

  * **uri** (`string`)

  * **params** (`unknown`)

  * **options** (`OperatorExecutorOptions`)



Return type:
    

`Promise < void >` `<` `void` `>`

### registerOperator#

@fiftyone/operators.registerOperator(_OperatorType_ , _pluginName_)#
    

Arguments:
    

  * **OperatorType**

  * **pluginName** (`string`)



Return type:
    

`void`

### validate#

@fiftyone/operators.validate(_params_ , _property_)#
    

Arguments:
    

  * **params** (`ParamsType`)

  * **property** (`Property`)



Return type:
    

`Object`

## Types#

### Places#

Places where you can have your operator placement rendered.

Name | Value  
---|---  
DISPLAY_OPTIONS |   
EMBEDDINGS_ACTIONS |   
HEADER_ACTIONS |   
HISTOGRAM_ACTIONS |   
MAP_ACTIONS |   
MAP_SECONDARY_ACTIONS |   
SAMPLES_GRID_ACTIONS |   
SAMPLES_GRID_SECONDARY_ACTIONS |   
SAMPLES_VIEWER_ACTIONS |   
  
Operator class for describing an autocomplete `View` for an operator type.

### AutocompleteView#

class @fiftyone/operators.AutocompleteView()#
    

Summary:
    

Operator class for describing an autocomplete `View` for an operator type.

@fiftyone/operators.new AutocompleteView(_options_)#
    

Arguments:
    

  * **options** (`ChoicesOptions`)



Return type:
    

`plugins.fiftyone.operators.AutocompleteView`

### BaseType#

class @fiftyone/operators.BaseType()#
    

@fiftyone/operators.new BaseType()#
    

Return type:
    

`plugins.fiftyone.operators.BaseType`

Operator type for representing a boolean value for operator input/output.

### Boolean#

class @fiftyone/operators.Boolean()#
    

Summary:
    

Operator type for representing a boolean value for operator input/output.

@fiftyone/operators.new Boolean()#
    

Return type:
    

`plugins.fiftyone.operators.OperatorBoolean`

Operator class for describing a button `View` for an operator type.

### Button#

class @fiftyone/operators.Button()#
    

Summary:
    

Operator class for describing a button `View` for an operator type.

@fiftyone/operators.new Button(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.Button`

Operator class for describing a choice `View` for an operator type. Must be used in conjunction with `Choices`

### Choice#

class @fiftyone/operators.Choice()#
    

Summary:
    

Operator class for describing a choice `View` for an operator type. Must be used in conjunction with `Choices`

@fiftyone/operators.new Choice(_value_ , _options_)#
    

Arguments:
    

  * **value** (`string`)

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.Choice`

Operator class for describing choices `View` for an operator type.

### Choices#

class @fiftyone/operators.Choices()#
    

Summary:
    

Operator class for describing choices `View` for an operator type.

@fiftyone/operators.new Choices(_options_)#
    

Arguments:
    

  * **options** (`ChoicesOptions`)



Return type:
    

`plugins.fiftyone.operators.Choices`

Operator class for describing a code block `View` for an operator type.

### CodeView#

class @fiftyone/operators.CodeView()#
    

Summary:
    

Operator class for describing a code block `View` for an operator type.

@fiftyone/operators.new CodeView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.CodeView`

Operator class for describing a color picker `View` for an operator type.

### ColorView#

class @fiftyone/operators.ColorView()#
    

Summary:
    

Operator class for describing a color picker `View` for an operator type.

@fiftyone/operators.new ColorView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.ColorView`

Operator class for describing a column `View` for an operator type. Must be used in conjunction with `TableView`

### Column#

class @fiftyone/operators.Column()#
    

Summary:
    

Operator class for describing a column `View` for an operator type. Must be used in conjunction with `TableView`

@fiftyone/operators.new Column(_key_ , _options_)#
    

Arguments:
    

  * **key** (`string`)

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.Column`

Operator class for describing a ComponentView `View` for an operator type. When using ComponentView, you can render a registered custom plugin component.

### ComponentView#

class @fiftyone/operators.ComponentView()#
    

Summary:
    

Operator class for describing a ComponentView `View` for an operator type. When using ComponentView, you can render a registered custom plugin component.

@fiftyone/operators.new ComponentView(_component_ , _options_)#
    

Arguments:
    

  * **component** (`string`)

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.ComponentView`

Operator class for describing a dropdown `View` for an operator type.

### Dropdown#

class @fiftyone/operators.Dropdown()#
    

Summary:
    

Operator class for describing a dropdown `View` for an operator type.

@fiftyone/operators.new Dropdown(_options_)#
    

Arguments:
    

  * **options** (`ChoicesOptions`)



Return type:
    

`plugins.fiftyone.operators.Dropdown`

Operator type for representing an enum value for operator input/output. Enum
    

is similar to a string, but can define specific values

### Enum#

class @fiftyone/operators.Enum()#
    

Summary:
    

Operator type for representing an enum value for operator input/output. Enum is similar to a string, but can define specific values

@fiftyone/operators.new Enum(_values_)#
    

Arguments:
    

  * **values** (`Array`)



Return type:
    

`plugins.fiftyone.operators.Enum`

Operator class for describing a error notice `View` for an operator type.

### Error#

class @fiftyone/operators.Error()#
    

Summary:
    

Operator class for describing a error notice `View` for an operator type.

@fiftyone/operators.new Error(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.ErrorView`

Operator class for describing a FieldView `View` for an operator type.

### FieldView#

class @fiftyone/operators.FieldView()#
    

Summary:
    

Operator class for describing a FieldView `View` for an operator type.

@fiftyone/operators.new FieldView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.FieldView`

Operator type for defining a file and its metadata.

### File#

class @fiftyone/operators.File()#
    

Summary:
    

Operator type for defining a file and its metadata.

@fiftyone/operators.new File(_properties_)#
    

Arguments:
    

  * **properties** (`Map`)



Return type:
    

`plugins.fiftyone.operators.File`

initial properties on the object

Operator class for interacting with files.

### FileExplorerView#

class @fiftyone/operators.FileExplorerView()#
    

Summary:
    

Operator class for interacting with files.

@fiftyone/operators.new FileExplorerView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.FileExplorerView`

Operator class for describing a file upload `View` for an operator type.

### FileView#

class @fiftyone/operators.FileView()#
    

Summary:
    

Operator class for describing a file upload `View` for an operator type.

@fiftyone/operators.new FileView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.FileView`

Operator class for describing a view (rendering details in the app) for an operator type.

### Form#

class @fiftyone/operators.Form()#
    

Summary:
    

Operator class for describing a view (rendering details in the app) for an operator type.

@fiftyone/operators.new Form(_live_ , _submitButtonLabel_ , _cancelButtonLabel_ , _options_)#
    

Arguments:
    

  * **live** (`boolean`)

  * **submitButtonLabel** (`string`)

  * **cancelButtonLabel** (`string`)

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.Form`

Operator class for describing a header `View` for an operator type.

### Header#

class @fiftyone/operators.Header()#
    

Summary:
    

Operator class for describing a header `View` for an operator type.

@fiftyone/operators.new Header(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.Header`

Operator class for describing a hidden `View` for an operator type.

### HiddenView#

class @fiftyone/operators.HiddenView()#
    

Summary:
    

Operator class for describing a hidden `View` for an operator type.

@fiftyone/operators.new HiddenView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.HiddenView`

Operator class for describing a IconButtonView `Button` for an operator type.

### IconButtonView#

class @fiftyone/operators.IconButtonView()#
    

Summary:
    

Operator class for describing a IconButtonView `Button` for an operator type.

@fiftyone/operators.new IconButtonView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.IconButtonView`

Operator class for describing an inferred `View` for an operator type. Inferred view is useful for rendering an operator type without the need to describe views for each type and sub-type explicitly

### InferredView#

class @fiftyone/operators.InferredView()#
    

Summary:
    

Operator class for describing an inferred `View` for an operator type. Inferred view is useful for rendering an operator type without the need to describe views for each type and sub-type explicitly

@fiftyone/operators.new InferredView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.InferredView`

Operator class for describing a json `View` for an operator type.

### JSONView#

class @fiftyone/operators.JSONView()#
    

Summary:
    

Operator class for describing a json `View` for an operator type.

@fiftyone/operators.new JSONView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.JSONView`

Operator class for describing a key-value `View` for an operator type.

### KeyValueView#

class @fiftyone/operators.KeyValueView()#
    

Summary:
    

Operator class for describing a key-value `View` for an operator type.

@fiftyone/operators.new KeyValueView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.KeyValueView`

Operator class for describing a LazyFieldView `View` for an operator type. When using LazyFieldView, only apply input field changes on blur or when user clicks the save button within the field.

### LazyFieldView#

class @fiftyone/operators.LazyFieldView()#
    

Summary:
    

Operator class for describing a LazyFieldView `View` for an operator type. When using LazyFieldView, only apply input field changes on blur or when user clicks the save button within the field.

@fiftyone/operators.new LazyFieldView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.LazyFieldView`

Operator class for describing a link `View` for an operator type.

### LinkView#

class @fiftyone/operators.LinkView()#
    

Summary:
    

Operator class for describing a link `View` for an operator type.

@fiftyone/operators.new LinkView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.LinkView`

Operator type for representing a list value for operator input/output.

### List#

class @fiftyone/operators.List()#
    

Summary:
    

Operator type for representing a list value for operator input/output.

@fiftyone/operators.new List(_elementType_ , _minItems_ , _maxItems_)#
    

Arguments:
    

  * **elementType** (`ANY_TYPE`)

  * **minItems** (`number`)

  * **maxItems** (`number`)



Return type:
    

`plugins.fiftyone.operators.List`

Operator class for describing a list `View` for an operator type.

### ListView#

class @fiftyone/operators.ListView()#
    

Summary:
    

Operator class for describing a list `View` for an operator type.

@fiftyone/operators.new ListView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.ListView`

Operator class for describing a loader `View` for an operator type.

### LoadingView#

class @fiftyone/operators.LoadingView()#
    

Summary:
    

Operator class for describing a loader `View` for an operator type.

@fiftyone/operators.new LoadingView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.LoadingView`

Operator type for representing a map value for operator input/output. `Map` can be useful for accepting arbitrary key-value pair where key is of type `String` and value can be any one of operator type.

### Map#

class @fiftyone/operators.Map()#
    

Summary:
    

Operator type for representing a map value for operator input/output. `Map` can be useful for accepting arbitrary key-value pair where key is of type `String` and value can be any one of operator type.

@fiftyone/operators.new Map(_keyType_ , _valueType_)#
    

Arguments:
    

  * **keyType** (`ANY_TYPE`)

  * **valueType** (`ANY_TYPE`)



Return type:
    

`plugins.fiftyone.operators.OperatorMap`

Operator class for describing a map `View` for an operator type.

### MapView#

class @fiftyone/operators.MapView()#
    

Summary:
    

Operator class for describing a map `View` for an operator type.

@fiftyone/operators.new MapView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.MapView`

Operator class for rendering a string as markdown.

### MarkdownView#

class @fiftyone/operators.MarkdownView()#
    

Summary:
    

Operator class for rendering a string as markdown.

@fiftyone/operators.new MarkdownView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.MarkdownView`

Operator class for describing a view (rendering details in the app) for an operator type.

### MediaPlayerView#

class @fiftyone/operators.MediaPlayerView()#
    

Summary:
    

Operator class for describing a view (rendering details in the app) for an operator type.

@fiftyone/operators.new MediaPlayerView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.MediaPlayerView`

Operator class for describing a ModalView `Button` for an operator type.

### ModalView#

class @fiftyone/operators.ModalView()#
    

Summary:
    

Operator class for describing a ModalView `Button` for an operator type.

@fiftyone/operators.new ModalView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.ModalView`

Operator class for describing a informational notice `View` for an operator type.

### Notice#

class @fiftyone/operators.Notice()#
    

Summary:
    

Operator class for describing a informational notice `View` for an operator type.

@fiftyone/operators.new Notice(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.Notice`

Operator type for representing a number value for operator input/output.

### Number#

class @fiftyone/operators.Number()#
    

Summary:
    

Operator type for representing a number value for operator input/output.

@fiftyone/operators.new Number(_options_)#
    

Arguments:
    

  * **options** (`Object`)

  * **options.float** (`boolean`)

  * **options.int** (`boolean`)

  * **options.max** (`number`) â maximum number a value can be

  * **options.min** (`number`) â minimum number a value can be



Return type:
    

`plugins.fiftyone.operators.OperatorNumber`

Construct operator type for number-like values

Operator type for representing an object value for operator input/output.

### Object#

class @fiftyone/operators.Object()#
    

Summary:
    

Operator type for representing an object value for operator input/output.

@fiftyone/operators.new Object(_properties_)#
    

Arguments:
    

  * **properties** (`ObjectProperties`)



Return type:
    

`plugins.fiftyone.operators.OperatorObject`

You can construct operator object type optionally providing a JS `Map` with
    

key representing the name of a property and the value representing the property it self. (default: `new Map()`)

initial properties on the object

Operator type for representing an oneof value for operator input/output.
    

`OneOf` can be used when a value can be of multiple types.

### OneOf#

class @fiftyone/operators.OneOf()#
    

Summary:
    

Operator type for representing an oneof value for operator input/output. `OneOf` can be used when a value can be of multiple types.

@fiftyone/operators.new OneOf(_types_)#
    

Arguments:
    

  * **types** (`Array`)



Return type:
    

`plugins.fiftyone.operators.OneOf`

Operator class for describing a oneof `View` for an operator type.

### OneOfView#

class @fiftyone/operators.OneOfView()#
    

Summary:
    

Operator class for describing a oneof `View` for an operator type.

@fiftyone/operators.new OneOfView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.OneOfView`

Operator class for rendering a execution button.

### OperatorExecutionButtonView#

class @fiftyone/operators.OperatorExecutionButtonView()#
    

Summary:
    

Operator class for rendering a execution button.

@fiftyone/operators.new OperatorExecutionButtonView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.OperatorExecutionButtonView`

Operator class for describing a PillBadgeView `View` for an operator type.

### PillBadgeView#

class @fiftyone/operators.PillBadgeView()#
    

Summary:
    

Operator class for describing a PillBadgeView `View` for an operator type.

@fiftyone/operators.new PillBadgeView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.PillBadgeView`

Operator type for defining a placement for an operator. Placement is a button
    

that can be rendered at various places in the app

### Placement#

class @fiftyone/operators.Placement()#
    

Summary:
    

Operator type for defining a placement for an operator. Placement is a button that can be rendered at various places in the app

@fiftyone/operators.new Placement(_place_ , _view_)#
    

Arguments:
    

  * **place** (`Places`)

  * **view** (`View`)



Return type:
    

`plugins.fiftyone.operators.Placement`

Operator class for describing a plotly.js `View` for an operator type.

### PlotlyView#

class @fiftyone/operators.PlotlyView()#
    

Summary:
    

Operator class for describing a plotly.js `View` for an operator type.

@fiftyone/operators.new PlotlyView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.PlotlyView`

Operator class for describing a progress `View` for an operator type.

### ProgressView#

class @fiftyone/operators.ProgressView()#
    

Summary:
    

Operator class for describing a progress `View` for an operator type.

@fiftyone/operators.new ProgressView(_options_)#
    

Arguments:
    

  * **options** (`ProgressViewProps`)



Return type:
    

`plugins.fiftyone.operators.ProgressView`

Operator class for rendering a prompt.

### PromptView#

class @fiftyone/operators.PromptView()#
    

Summary:
    

Operator class for rendering a prompt.

@fiftyone/operators.new PromptView(_label_ , _submitButtonLabel_ , _cancelButtonLabel_)#
    

Arguments:
    

  * **label** (`string`)

  * **submitButtonLabel** (`string`)

  * **cancelButtonLabel** (`string`)



Return type:
    

`plugins.fiftyone.operators.PromptView`

Operator type for representing a property of operator
    

`Object` type.

### Property#

class @fiftyone/operators.Property()#
    

Summary:
    

Operator type for representing a property of operator `Object` type.

@fiftyone/operators.new Property(_type_ , _options_)#
    

Arguments:
    

  * **type** (`ANY_TYPE`)

  * **options** (`PropertyOptions`)



Return type:
    

`plugins.fiftyone.operators.Property`

Operator class for describing a radio-group `View` for an operator type.

### RadioGroup#

class @fiftyone/operators.RadioGroup()#
    

Summary:
    

Operator class for describing a radio-group `View` for an operator type.

@fiftyone/operators.new RadioGroup(_options_)#
    

Arguments:
    

  * **options** (`ChoicesOptions`)



Return type:
    

`plugins.fiftyone.operators.RadioGroup`

Operator class for describing a read-only `View` for an operator type.

### ReadOnlyView#

class @fiftyone/operators.ReadOnlyView()#
    

Summary:
    

Operator class for describing a read-only `View` for an operator type.

@fiftyone/operators.new ReadOnlyView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.ReadOnlyView`

### ResolvableProperty#

class @fiftyone/operators.ResolvableProperty()#
    

@fiftyone/operators.new ResolvableProperty(_options_)#
    

Arguments:
    

  * **options** (`ResolvablePropertyOptions`)



Return type:
    

`plugins.fiftyone.operators.ResolvableProperty`

Construct operator type for resolvable property

Operator type for representing a sampled id value for operator input/output.

### SampleID#

class @fiftyone/operators.SampleID()#
    

Summary:
    

Operator type for representing a sampled id value for operator input/output.

@fiftyone/operators.new SampleID(_options_)#
    

Arguments:
    

  * **options**

  * **options.allowEmpty** â allow an empty string value




number
    

type options:
    

Object

type options.allowEmpty:
    

boolean

rtype:
    

`plugins.fiftyone.operators.SampleID`

Construct operator type for string values

Operator class for rendering a status button.

### StatusButtonView#

class @fiftyone/operators.StatusButtonView()#
    

Summary:
    

Operator class for rendering a status button.

@fiftyone/operators.new StatusButtonView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.StatusButtonView`

Operator type for representing a string value for operator input/output.

### String#

class @fiftyone/operators.String()#
    

Summary:
    

Operator type for representing a string value for operator input/output.

@fiftyone/operators.new String(_options_)#
    

Arguments:
    

  * **options**

  * **options.allowEmpty** â allow an empty string value




number
    

type options:
    

Object

type options.allowEmpty:
    

boolean

rtype:
    

`plugins.fiftyone.operators.OperatorString`

Construct operator type for string values

Operator class for describing a table `View` for an operator type.

### TableView#

class @fiftyone/operators.TableView()#
    

Summary:
    

Operator class for describing a table `View` for an operator type.

@fiftyone/operators.new TableView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.TableView`

Operator class for describing a tabs `View` for an operator type.

### TabsView#

class @fiftyone/operators.TabsView()#
    

Summary:
    

Operator class for describing a tabs `View` for an operator type.

@fiftyone/operators.new TabsView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.TabsView`

Operator class for describing a TextFieldView `View` for an operator type.

### TextFieldView#

class @fiftyone/operators.TextFieldView()#
    

Summary:
    

Operator class for describing a TextFieldView `View` for an operator type.

@fiftyone/operators.new TextFieldView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.TextFieldView`

Operator class for describing a TextView `View` for an operator type.

### TextView#

class @fiftyone/operators.TextView()#
    

Summary:
    

Operator class for describing a TextView `View` for an operator type.

@fiftyone/operators.new TextView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.TextView`

Operator class for describing a ToastView `View` for an operator type.

### ToastView#

class @fiftyone/operators.ToastView()#
    

Summary:
    

Operator class for describing a ToastView `View` for an operator type.

@fiftyone/operators.new ToastView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.ToastView`

Operator class for describing a tree node selection `View` for an operator type.

### TreeSelectionView#

class @fiftyone/operators.TreeSelectionView()#
    

Summary:
    

Operator class for describing a tree node selection `View` for an operator type.

@fiftyone/operators.new TreeSelectionView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.TreeSelectionView`

Operator type for defining a trigger for an operator.

### Trigger#

class @fiftyone/operators.Trigger()#
    

Summary:
    

Operator type for defining a trigger for an operator.

@fiftyone/operators.new Trigger(_operator_ , _params_)#
    

Arguments:
    

  * **operator** (`string`)

  * **params** (`object`)



Return type:
    

`plugins.fiftyone.operators.Trigger`

Operator type for representing a tuple value for operator input/output.
    

`Tuple` can be useful for defining list of values of mixed types

### Tuple#

class @fiftyone/operators.Tuple()#
    

Summary:
    

Operator type for representing a tuple value for operator input/output. `Tuple` can be useful for defining list of values of mixed types

@fiftyone/operators.new Tuple(_items_)#
    

Arguments:
    

  * **items** (`Array`)



Return type:
    

`plugins.fiftyone.operators.Tuple`

Operator class for describing a tuple `View` for an operator type.

### TupleView#

class @fiftyone/operators.TupleView()#
    

Summary:
    

Operator class for describing a tuple `View` for an operator type.

@fiftyone/operators.new TupleView(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.TupleView`

Operator type for defining an uploaded file and its metadata.

### UploadedFile#

class @fiftyone/operators.UploadedFile()#
    

Summary:
    

Operator type for defining an uploaded file and its metadata.

@fiftyone/operators.new UploadedFile(_properties_)#
    

Arguments:
    

  * **properties** (`Map`)



Return type:
    

`plugins.fiftyone.operators.UploadedFile`

initial properties on the object

Operator class for describing a view (rendering details in the app) for an operator type.

### View#

class @fiftyone/operators.View()#
    

Summary:
    

Operator class for describing a view (rendering details in the app) for an operator type.

@fiftyone/operators.new View(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.View`

Operator type for representing void value for operator input/output. Void
    

type can be useful for displaying a informational-only views.

### Void#

class @fiftyone/operators.Void()#
    

Summary:
    

Operator type for representing void value for operator input/output. Void type can be useful for displaying a informational-only views.

@fiftyone/operators.new Void()#
    

Return type:
    

`plugins.fiftyone.operators.Void`

Operator class for describing a warning notice `View` for an operator type.

### Warning#

class @fiftyone/operators.Warning()#
    

Summary:
    

Operator class for describing a warning notice `View` for an operator type.

@fiftyone/operators.new Warning(_options_)#
    

Arguments:
    

  * **options** (`ViewProps`)



Return type:
    

`plugins.fiftyone.operators.Warning`

class @fiftyone/operators.ANY_TYPE()#
    

### ANY_TYPE#

  * `OperatorObject` is exported as `Object`

  * `OperatorString` is exported as `String`

  * `OperatorBoolean` is exported as `Boolean`

  * `OperatorNumber` is exported as `Number`

  * `OperatorMap` is exported as `Map`




Union of `Void`, `OperatorObject`, `OperatorString`, `OperatorBoolean`, `OperatorNumber`, `List`, `Enum`, `OneOf`, `Tuple`, `OperatorMap`, `File`, `UploadedFile`, `ResolvableProperty`

class @fiftyone/operators.OperatorPromptPropsType()#
    

### OperatorPromptPropsType#

Name | Type | Description  
---|---|---  
OperatorPromptPropsType.prompt | `plugins.fiftyone.operators.OperatorPromptType` |   
  
class @fiftyone/operators.OperatorPromptType()#
    

### OperatorPromptType#

Name | Type | Description  
---|---|---  
OperatorPromptType | `ReturnType < >` `<` ```` `>` |   
  
class @fiftyone/operators.OperatorResponse()#
    

### OperatorResponse#

Response type returned from operator execution.

Name | Type | Description  
---|---|---  
OperatorResponse.delegated | `boolean` |   
OperatorResponse.error | `string` |   
OperatorResponse.error_message | `string` |   
OperatorResponse.executor | `Object` |   
OperatorResponse.result | `Object` |   
  
class @fiftyone/operators.ValidationErrorsType()#
    

### ValidationErrorsType#

class @fiftyone/operators.ViewOrientation()#
    

### ViewOrientation#

Union of `'horizontal'`, `'vertical'`

class @fiftyone/operators.ViewPropertyTypes()#
    

### ViewPropertyTypes#

Union of `string`, `boolean`, `number`, `Array`, `View`, `object`, `ViewOrientation`

### typeFromJSON#

@fiftyone/operators.typeFromJSON(___namedParameters_)#
    

Arguments:
    

  * **__namedParameters** (`Object`)



Return type:
    

`plugins.fiftyone.operators.ANY_TYPE`

### viewFromJSON#

@fiftyone/operators.viewFromJSON(_json_)#
    

Arguments:
    

  * **json** (`any`)



Return type:
    

`any`

## Enums#

### OPERATOR_PROMPT_AREAS#

Name | Value  
---|---  
DRAWER_LEFT |   
DRAWER_RIGHT |   
  
### RiskLevel#

Name | Value  
---|---  
DANGEROUS |   
HIGH |   
LOW |   
MEDIUM |   
  
IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
