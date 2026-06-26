---
source_url: https://docs.voxel51.com/api/fiftyone.operators.types.html
---

# fiftyone.operators.types#

FiftyOne operator types.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`Pipeline`([stages]) | Dataclass representing a FiftyOne operator pipeline.  
---|---  
`PipelineRunInfo`([active,Â expected_children,Â ...]) | Dataclass with information about a pipeline run.  
`PipelineStage`(operator_uri[,Â always_run,Â ...]) | Dataclass representing a stage in a FiftyOne plugin operator pipeline  
`BaseType`() | Base class for all types.  
`Void`() | Represents a void type.  
`Object`([root_view]) | Represents a JSON object.  
`Property`(type,Â **kwargs) | Represents a property on an [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator").  
`ResolvableProperty`(resolver,Â **kwargs) | Represents a resolvable property.  
`String`([allow_empty]) | Represents a string.  
`Boolean`() | Represents a boolean.  
`Number`([min,Â max,Â int,Â float]) | Represents a number.  
`List`(element_type[,Â min_items,Â max_items]) | Represents a list.  
`SampleID`() | Represents a `fiftyone.core.samples.Sample` ID.  
`Enum`(values) | Represents an enum.  
`OneOf`(types) | Represents a one-of type.  
`Tuple`(*items) | Represents a tuple of types.  
`Tree`(*items) | Represents a tree selection type.  
`Map`(key_type,Â value_type) | Represents a map.  
`File`(**kwargs) | Represents a file and related metadata for use with `FileExplorerView`.  
`UploadedFile`(**kwargs) | Represents an object with uploaded file content and its metadata in properties.  
`View`([container]) | Represents a view of a `Property`.  
`InferredView`(**kwargs) | Represents a view of a `Property` that is inferred from the data.  
`Form`([live,Â submit_button_label,Â ...]) | A form view.  
`ReadOnlyView`(**kwargs) | A read-only `View`.  
`Choice`(value[,Â include]) | Represents a choice in a `Choices` view.  
`Choices`(**kwargs) | Represents a set of choices in a `View`.  
`RadioGroup`(**kwargs) | Represents a set of choices in a `View` that are displayed as a radio group.  
`Dropdown`(**kwargs) | Represents a set of choices in a `View` that are displayed as a dropdown.  
`Notice`(**kwargs) | Represents a notice in a `View`.  
`Header`(**kwargs) | Represents a header in a `View`.  
`Warning`(**kwargs) | Represents a warning in a `View`.  
`Error`(**kwargs) | Represents an error in a `View`.  
`Button`(**kwargs) | Represents a button in a `View`.  
`OperatorExecutionButtonView`(**kwargs) | Represents an operator execution button in a `View`.  
`OneOfView`(**kwargs) | Displays one of the given `View` instances.  
`ListView`(**kwargs) | Displays a list of `View` instances.  
`TupleView`(*itemsView,Â **options) | Displays a tuple of `View` instances.  
`TreeSelectionView`(**options) | Displays a tree selection checkbox groups.  
`CodeView`(**kwargs) | Displays a code editor.  
`ColorView`(**kwargs) | Displays a color picker.  
`TabsView`(**kwargs) | Displays a tabbed view.  
`JSONView`(**kwargs) | Displays a JSON viewer.  
`AutocompleteView`(**kwargs) | Displays an autocomplete input.  
`FileView`(**kwargs) | Displays a file input.  
`LinkView`(**kwargs) | Displays a hyperlink.  
`HiddenView`(**kwargs) | Allows properties to be hidden from the user.  
`LoadingView`(**kwargs) | Displays a loading indicator.  
`LoaderView`(operator[,Â params,Â label,Â ...]) | A view that loads data asynchronously via an operator.  
`PillBadgeView`(**kwargs) | Displays a pill shaped badge.  
`PlotlyView`(**kwargs) | Displays a Plotly chart.  
`Placement`(place[,Â view]) | Represents the placement of an operator in the FiftyOne App.  
`Places`(value) | The places available to operators in the FiftyOne App.  
`KeyValueView`(**kwargs) | Displays a key-value editor.  
`Column`(key,Â **kwargs) | A column in a `TableView`.  
`Action`(name,Â **kwargs) | An action (currently supported only in a `TableView`).  
`Tooltip`(row,Â column,Â **kwargs) | A tooltip (currently supported only in a `TableView`).  
`TableView`(**kwargs) | Displays a table.  
`MapView`(**kwargs) | Displays a key-value mapping.  
`ProgressView`(**kwargs) | Displays a progress bar.  
`ImageView`(**kwargs) | Displays an image.  
`AlertView`(**kwargs) | Displays an alert.  
`ToastView`(**kwargs) | Displays a snackbar style toast element.  
`CheckboxView`(**kwargs) | Displays a checkbox.  
`ErrorView`(**kwargs) | Displays an error.  
`HeaderView`(**kwargs) | Displays a header component.  
`ObjectView`(**kwargs) | Displays an object component.  
`RadioView`(**kwargs) | Displays a radio component for the given `RadioGroup` instance.  
`SwitchView`(**kwargs) | Displays a toggle switch.  
`TextView`(**kwargs) | Displays a text. .. note:: Must be used with `String` properties.  
`TextFieldView`([multiline,Â rows]) | Displays a text input.  
`FieldView`(**kwargs) | Displays a text input.  
`LazyFieldView`(**kwargs) | Displays a lazy text input which only apply input field changes on blur or when user clicks the save button within the field.  
`DropdownView`(**kwargs) | Displays a dropdown selector input.  
`DateTimeView`(**kwargs) | Displays a date/time input - response in epoch time  
`LabelValueView`(**kwargs) | Displays a label-value component.  
`PrimitiveView`(**kwargs) | Displays a primitive value component.  
`SliderView`(**kwargs) | Displays a slider component.  
`TagsView`(**kwargs) | Displays a list of tags component.  
`Success`(**kwargs) | Represents a success in a `View`.  
`ButtonView`(**kwargs) | Represents a button in a `Button`.  
`MarkdownView`(**kwargs) | Renders a markdown string as HTML.  
`StatusButtonView`(**kwargs) | Renders a status button.  
`MediaPlayerView`(**kwargs) | Renders a media player for audio and video files.  
`FileExplorerView`(**kwargs) | Displays a file explorer for interacting with files.  
`PromptView`(**kwargs) | Customizes how a prompt is rendered.  
`ViewTargetOptions`(choices_view[,Â ...]) | Represents the options for a `ViewTargetProperty`.  
`ViewTargetProperty`(ctx[,Â view_type,Â ...]) | Property that displays a view target selector.  
`GridView`(**kwargs) | Displays properties of an object as a grid of components in horizontal or vertical orientation.  
`DashboardView`(**kwargs) | Defines a Dashboard view.  
`DrawerView`(**kwargs) | Renders an operator prompt as a left or right side drawer.  
`IconButtonView`(**kwargs) | Represents a button in a `View`.  
`ModalView`(**kwargs) | Represents a button in a `View` that opens up an interactive modal.  
`HStackView`([orientation]) | Displays properties of an object as a horizontal stack of components.  
`VStackView`([orientation]) | Displays properties of an object as a vertical stack of components.  
`ButtonGroupView`([orientation]) | Displays a group of buttons in a horizontal stack.  
`MenuView`([orientation]) | Displays a menu of options in a vertical stack.  
`ArrowNavView`(**kwargs) | Displays a floating navigation arrows.  
`FrameLoaderView`(**kwargs) | Utility for animating panel state based on the given timeline_name.  
`TimelineView`(**kwargs) | Represents a timeline for playing animations.  
`TimerView`(**kwargs) | Supports a timer for executing operators/events after a specified duration or interval.  
`ComponentView`(name,Â **kwargs) | Represents a custom component view.  
`Container`(**kwargs) | Represents a base container for a container types.  
`PaperContainer`([elevation,Â rounded]) | Represents an elevated block for a view.  
`OutlinedContainer`([rounded]) | Represents an elevated block for a view.  
`RiskLevel`(value) | Risk levels that operators can declare.  
  
**Functions:**

`dedent`(text) | Remove any common leading whitespace from every line in text.  
---|---  
  
class fiftyone.operators.types.Pipeline(_stages : [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[PipelineStage] | None = None_, _** kwargs_)#
    

Bases: `object`

Dataclass representing a FiftyOne operator pipeline.

A pipeline consists of one or more stages, each of which is an operator.

**Attributes:**

`stages` | A list of `PipelineStage` instances  
---|---  
  
**Methods:**

`stage`(operator_uri[,Â always_run,Â name,Â ...]) | Adds a stage to the end of the pipeline.  
---|---  
`from_json`(json_dict) | Loads the pipeline from a JSON/python dict.  
`to_json`() | Converts this pipeline to JSON/python dict representation  
  
stages: [list](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")[PipelineStage]#
    

A list of `PipelineStage` instances

stage(_operator_uri_ , _always_run =False_, _name =None_, _num_distributed_tasks =None_, _params =None_, _rerunnable =None_, _request_params_overrides =None_, _** kwargs_)#
    

Adds a stage to the end of the pipeline.

Parameters:
    

  * **operator_uri** â the URI of the operator to use for the stage

  * **always_run** â if True, this stage runs even when the pipeline is inactive (e.g., after a failure), enabling cleanup/finalization stages

  * **name** â the name of the stage

  * **num_distributed_tasks** â the number of distributed tasks to use for the stage, optional

  * **params** â optional parameters to pass to the operator

  * **rerunnable** â whether the stage is rerunnable

  * **request_params_overrides** â optional dict of request parameter overrides for the execution context. Allows overriding fields like view (accepts a DatasetView or serialized stages), filters, etc.

  * ****kwargs** â reserved for future use



Returns:
    

a `PipelineStage`

classmethod from_json(_json_dict_)#
    

Loads the pipeline from a JSON/python dict.

Examples:
    
    
    {
        "stages": [
            {
                "operator_uri": "@voxel51/test/blah",
                "name": "my_stage",
                "request_params_overrides": {
                    "view_name": "filtered_view"
                }
            },
            ...,
        ]
    }
    

Parameters:
    

**json_dict** â a JSON / python dict representation of the pipeline

to_json()#
    

Converts this pipeline to JSON/python dict representation

Examples:
    
    
    {
        "stages": [
            {
                "operator_uri": "@voxel51/test/blah",
                "name": "my_stage",
                "request_params_overrides": {
                    "view_name": "filtered_view"
                }
            },
            ...,
        ]
    }
    

Returns:
    

JSON / python dict representation of the pipeline

class fiftyone.operators.types.PipelineRunInfo(_active =True_, _expected_children =None_, _stage_index =0_, _child_errors =None_, _** __)#
    

Bases: `object`

Dataclass with information about a pipeline run.

Unlike the pipeline definition, the information in this class is dynamic as it changes over time as the pipeline is executed. An instance of this class represents a snapshot of the state of execution.

**Attributes:**

`active` | Whether the pipeline is currently active, i.e., having no failures in prior stages  
---|---  
`expected_children` | List of the number of expected child operations per stage  
`stage_index` | Index of the pipeline's current execution stage  
`child_errors` | Mapping from child operation IDs to error messages  
  
**Methods:**

`from_json`(doc) |   
---|---  
`to_json`() |   
  
active: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = True#
    

Whether the pipeline is currently active, i.e., having no failures in prior stages

expected_children: List[int] | None = None#
    

List of the number of expected child operations per stage

stage_index: int = 0#
    

Index of the pipelineâs current execution stage

child_errors: dict[str, str] | None = None#
    

Mapping from child operation IDs to error messages

classmethod from_json(_doc : dict_)#
    

to_json()#
    

class fiftyone.operators.types.PipelineStage(_operator_uri : str_, _always_run : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False_, _name : str | None = None_, _num_distributed_tasks : int | None = None_, _params : Mapping[str, Any] | None = None_, _rerunnable : [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None_, _request_params_overrides : Mapping[str, Any] | None = None_, _** __)#
    

Bases: `object`

Dataclass representing a stage in a FiftyOne plugin operator pipeline

**Attributes:**

`operator_uri` | The URI of the operator to use for the stage  
---|---  
`always_run` | Whether the stage should always run regardless of failures in previous stages of the pipeline  
`name` | The optional name of the stage  
`num_distributed_tasks` | The number of distributed tasks to split the stage into  
`params` | Optional dict of parameters to pass to the operator  
`rerunnable` | Whether the stage is rerunnable, defaults to operator config  
`request_params_overrides` | Optional dict of request parameter overrides for the execution context.  
  
**Methods:**

`to_json`() | Converts the object definition to JSON / python dict.  
---|---  
  
operator_uri: str#
    

The URI of the operator to use for the stage

always_run: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") = False#
    

Whether the stage should always run regardless of failures in previous stages of the pipeline

name: str | None = None#
    

The optional name of the stage

num_distributed_tasks: int | None = None#
    

The number of distributed tasks to split the stage into

params: Mapping[str, Any] | None = None#
    

Optional dict of parameters to pass to the operator

rerunnable: [bool](api__fiftyone.core.stages.md#fiftyone.core.stages.Exists.bool "fiftyone.core.stages.Exists.bool") | None = None#
    

Whether the stage is rerunnable, defaults to operator config

request_params_overrides: Mapping[str, Any] | None = None#
    

Optional dict of request parameter overrides for the execution context.

Commonly overridden parameters include: \- view: a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") (serialized

> automatically) or `None` to clear any active view

  * view_name: name of a saved view to use

  * selected: list of selected sample IDs

  * group_slice: group slice to use




The keys `dataset_id`, `dataset_name`, `delegated`, `delegation_target`, `request_delegation`, and `results` are not allowed and will be removed with a logged error.

Note: The params field should not be included here; use the params field of `PipelineStage` directly for operator parameters.

to_json()#
    

Converts the object definition to JSON / python dict.

Returns:
    

a JSON / python dict

fiftyone.operators.types.dedent(_text_)#
    

Remove any common leading whitespace from every line in text.

This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.

Note that tabs and spaces are both treated as whitespace, but they are not equal: the lines â helloâ and âthelloâ are considered to have no common leading whitespace.

Entirely blank lines are normalized to a newline character.

class fiftyone.operators.types.BaseType#
    

Bases: `object`

Base class for all types.

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Void#
    

Bases: `BaseType`

Represents a void type.

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Object(_root_view =None_)#
    

Bases: `BaseType`

Represents a JSON object.

Parameters:
    

**root_view** (_None_) â the `View` used to display the object

**Methods:**

`add_property`(name,Â property) | Adds a property to the object.  
---|---  
`get_property`(name) | Gets a property by name.  
`define_property`(name,Â type,Â **kwargs) | Defines a property on the object.  
`str`(name[,Â allow_empty]) | Defines a property on the object that is a string.  
`bool`(name,Â **kwargs) | Defines a property on the object that is a boolean.  
`int`(name[,Â min,Â max]) | Defines a property on the object that is an integer.  
`float`(name[,Â min,Â max]) | Defines a property on the object that is a float.  
`enum`(name,Â values,Â **kwargs) | Defines a property on the object that is an enum.  
`list`(name,Â element_type[,Â min_items,Â max_items]) | Defines a property on the object that is a list.  
`obj`(name,Â **kwargs) | Defines a property on the object that is an object.  
`file`(name,Â **kwargs) | Defines a property on the object that is a file.  
`uploaded_file`(name,Â **kwargs) | Defines a property on the object that is an uploaded file.  
`view`(name,Â view,Â **kwargs) | Defines a view-only property.  
`loader`(name,Â type,Â operator[,Â params,Â ...]) | Defines a loader property that fetches data asynchronously.  
`btn`(name,Â label[,Â icon,Â variant,Â disabled,Â ...]) | Defines a button or icon button to display to the user as a `Button`.  
`img`(name[,Â href,Â on_click,Â prompt,Â params,Â ...]) | Defines an image to display to the user as a `ImageView`.  
`message`(name,Â label,Â **kwargs) | Defines a message to display to the user as a `Notice`.  
`grid`(name,Â **kwargs) | Defines a grid view as a `View`.  
`dashboard`(name,Â **kwargs) | Defines a dashboard view as a `View`.  
`plot`(name,Â **kwargs) | Defines an object property displayed as a plot.  
`h_stack`(name,Â **kwargs) | Defines a horizontal stack object.  
`v_stack`(name,Â **kwargs) | Defines a vertical stack object.  
`menu`(name,Â **kwargs) | Defined an `Object` property that is displayed as a menu.  
`btn_group`(name,Â **kwargs) | Defines a button group object.  
`md`(markdown[,Â name]) | Defines a markdown object.  
`media_player`(name,Â url,Â **kwargs) | Defines a media player object.  
`arrow_nav`(name[,Â forward,Â backward,Â position]) | Defines a floating navigation arrows as a `ArrowNavView`.  
`map`(name,Â key_type,Â value_type,Â **kwargs) | Defines a map property on the object.  
`oneof`(name,Â types,Â **kwargs) | Defines a one-of property on the object.  
`tuple`(name,Â *items,Â **kwargs) | Defines a tuple property on the object.  
`tree`(name,Â **kwargs) | Defines a tree property on the object.  
`clone`() | Clones the definition of the object.  
`view_target`(ctx[,Â name,Â view_type,Â ...]) | Defines a view target input property.  
`target_view`(ctx[,Â name,Â view_type,Â ...]) | Defines a view target input property.  
`to_json`() | Converts the object definition to JSON.  
  
add_property(_name_ , _property_)#
    

Adds a property to the object.

Parameters:
    

  * **name** â the name of the property

  * **property** â the property to add



Returns:
    

the `Property` that was added

get_property(_name_)#
    

Gets a property by name.

Parameters:
    

**name** â the name of the property

Returns:
    

the `Property`, or None

define_property(_name_ , _type_ , _** kwargs_)#
    

Defines a property on the object.

Parameters:
    

  * **name** â the name of the property

  * **type** â the type of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

the `Property` that was added

str(_name_ , _allow_empty =False_, _** kwargs_)#
    

Defines a property on the object that is a string.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

bool(_name_ , _** kwargs_)#
    

Defines a property on the object that is a boolean.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

int(_name_ , _min =None_, _max =None_, _** kwargs_)#
    

Defines a property on the object that is an integer.

Parameters:
    

  * **name** â the name of the property

  * **min** â minimum value of the property

  * **max** â maximum value of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

float(_name_ , _min =None_, _max =None_, _** kwargs_)#
    

Defines a property on the object that is a float.

Parameters:
    

  * **name** â the name of the property

  * **min** â minimum value of the property

  * **max** â maximum value of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

enum(_name_ , _values_ , _** kwargs_)#
    

Defines a property on the object that is an enum.

Parameters:
    

  * **name** â the name of the property

  * **values** â a list of values that define the enum

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property, which must be a `Choices` or a subclass of it



Returns:
    

a `Property`

list(_name_ , _element_type_ , _min_items =None_, _max_items =None_, _** kwargs_)#
    

Defines a property on the object that is a list.

Parameters:
    

  * **name** â the name of the property

  * **element_type** â the type of the elements in the list

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

obj(_name_ , _** kwargs_)#
    

Defines a property on the object that is an object.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

file(_name_ , _** kwargs_)#
    

Defines a property on the object that is a file.

Parameters:
    

  * **name** â the name of the property

  * **view** (_None_) â the `View` of the property




uploaded_file(_name_ , _** kwargs_)#
    

Defines a property on the object that is an uploaded file.

Parameters:
    

  * **name** â the name of the property

  * **view** (_None_) â the `View` of the property

  * **lite** (_False_) â whether to use the lite version of the file. When True, the content of the file in not included in resolve_input params, only the metadata is included.




view(_name_ , _view_ , _** kwargs_)#
    

Defines a view-only property.

Examples:
    
    
    import fiftyone.operators.types as types
    
    notice = types.Notice(label="a label", description="a description")
    inputs = types.Object()
    inputs.view("notice", notice)
    

Parameters:
    

  * **name** â the name of the property

  * **view** â the `View` to define



Returns:
    

a `Property`

loader(_name_ , _type_ , _operator_ , _params =None_, _label =None_, _placeholder_view =None_, _dependencies =None_, _** kwargs_)#
    

Defines a loader property that fetches data asynchronously.

The loader executes an operator and stores the result at the property path. The property value always has the following structure:
    
    
    {
        "state": "idle" | "loading" | "loaded" | "errored",
        "data": <type>,  # the loaded data, shaped by the type argument
        "error": <str>   # error message (when state is "errored")
    }
    

The `type` argument defines the shape of the `data` field, not the entire loader value. For example, if `type=types.List(types.Object())`, then `ctx.params[name]["data"]` will be a list of objects.

By default, the loader executes only once when the component mounts. Use the `dependencies` argument to specify which param paths should trigger a reload when their values change.

Examples:
    
    
    def resolve_input(self, ctx):
        inputs = types.Object()
    
        inputs.str("make", label="Car Make")
    
        chosen_make = ctx.params.get("make")
        if chosen_make:
            inputs.loader(
                "available_models",
                type=types.List(types.Object()),
                operator="@my-plugin/load_models",
                params={"make": chosen_make},
                label="Loading models...",
                dependencies=["make"],  # reload when "make" changes
            )
    
        models = ctx.params.get("available_models", {})
        if models.get("state") == "loaded":
            choices = Choices()
            for model in models.get("data", []):
                choices.add_choice(model["id"], label=model["name"])
            inputs.enum("model", values=choices)
    
        return types.Property(inputs)
    

Parameters:
    

  * **name** â the name of the property

  * **type** â the type of the `data` field within the loader value (e.g., `types.Object()`, `types.List(types.Object())`)

  * **operator** â the operator to execute (string URI or callable method)

  * **params** (_None_) â parameters to pass to the operator

  * **label** (_None_) â loading message to display

  * **placeholder_view** (_None_) â view to render while loading

  * **dependencies** (_None_) â list of param paths (dot-notation supported) that should trigger a reload when changed. If None, the loader only executes once on mount



Returns:
    

a `Property`

btn(_name_ , _label_ , _icon =None_, _variant =None_, _disabled =False_, _on_click =None_, _prompt =False_, _params =None_, _space =None_, _href =None_, _icon_position ='left'_, _** kwargs_)#
    

Defines a button or icon button to display to the user as a `Button`.

Examples:
    
    
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    inputs.btn(
        "greet",
        label="Say Hi!",
        icon="waving_hand",
        variant="round",
        on_click="print_stdout",
        params={"msg": "Hi!"},
    )
    

Parameters:
    

  * **name** â the name of the property

  * **label** â the label of the button

  * **icon** (_None_) â the name of the icon to display

  * **icon_position** (_"left"_) â the position of the icon. Can be `"left"` or `"right"`

  * **disabled** (_False_) â whether the button is disabled

  * **variant** (_None_) â the variant of the button. Can be `"contained"`, `"outlined"`, `"round"` or `"square"`

  * **on_click** (_None_) â the name of the operator to execute when the button is clicked

  * **prompt** (_False_) â whether to prompt the user before executing the operator

  * **params** (_None_) â the parameters to pass to the operator

  * **space** (_None_) â An int specifying how much vertical/horizontal space to allocate out of `12` depending on the orientation of the parent container

  * **href** (_None_) â the URL to navigate to when the button is clicked




img(_name_ , _href =None_, _on_click =None_, _prompt =False_, _params =None_, _point_on_hover =True_, _height =None_, _width =None_, _alt_text =None_, _** kwargs_)#
    

Defines an image to display to the user as a `ImageView`.

Examples:
    
    
    import fiftyone.operators.types as types
    ctx.panel.state.my_img = "/path/to/my/image.jpg"
    
    panel = types.Object()
    panel.img(
        "my_img", # uses the value in ctx.panel.state.my_img
        href="https://path/to/navigate/to",
        on_click=self.do_something,
        prompt=False,
        params={"foo": "bar"},
        point_on_hover=True,
        height="100px",
        width="100px",
        alt_text="My image alt text"
    )
    

Parameters:
    

  * **name** â the name of the state variable to use as the image source

  * **href** (_None_) â the url to navigate to when the image is clicked

  * **on_click** (_None_) â the name of the operator to execute when the button is clicked

  * **prompt** (_False_) â whether to prompt the user before executing the operator

  * **params** (_None_) â the parameters to pass to the operator

  * **point_on_hover** (_True_) â whether to show a pointer when hovering over the image

  * **height** (_None_) â the height of the image

  * **width** (_None_) â the width of the image

  * **alt_text** (_None_) â the alt text of the image




message(_name_ , _label_ , _** kwargs_)#
    

Defines a message to display to the user as a `Notice`.

Parameters:
    

  * **name** â the name of the property

  * **label** â the label of the notice

  * **description** (_None_) â the description of the notice

  * **view** (_None_) â the `View` of the notice



Returns:
    

a `Property`

grid(_name_ , _** kwargs_)#
    

Defines a grid view as a `View`.

dashboard(_name_ , _** kwargs_)#
    

Defines a dashboard view as a `View`.

See `DashboardView` for more information.

Parameters:
    

**name** â the name of the property

Returns:
    

an `Object`

See `DashboardView` for more information.

plot(_name_ , _** kwargs_)#
    

Defines an object property displayed as a plot.

Parameters:
    

  * **name** â the name of the property

  * **config** (_None_) â the chart config

  * **layout** (_None_) â the chart layout




See `PlotlyView` for more information.

h_stack(_name_ , _** kwargs_)#
    

Defines a horizontal stack object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

v_stack(_name_ , _** kwargs_)#
    

Defines a vertical stack object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

menu(_name_ , _** kwargs_)#
    

Defined an `Object` property that is displayed as a menu.

Note

Can be used for an `Button` type with properties whose views are one of `Button`, `Dropdown`, `DropdownView`, and :class;`Choices`. The variant and color of the items can be set using the variant and color parameters.

Parameters:
    

  * **name** â the name of the property

  * **variant** (_None_) â the variant for the items of the menu. Can be `"contained"`, `"outlined"`, `"round"` or `"square"`

  * **color** (_None_) â the color for the items of the menu.

  * **overlay** (_None_) â whether to display the menu as an overlay. Can be `"top-left"`,

  * **"top-center"**

  * **"top-right"**

  * **"bottom-left"**

  * **"bottom-center"`**

  * **or**

  * **of** (_"bottom-right". Overlay is useful when you want to display a floating menu on top_)

  * **content** (_another_)

  * **icon** (_None_) â when set, the icon will be displayed as the menu button instead of the label.

  * **"SettingsIcon"** (_Can be_)

  * **"MoreVertIcon".**



Returns:
    

a `Object`

btn_group(_name_ , _** kwargs_)#
    

Defines a button group object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

md(_markdown_ , _name ='markdown'_, _** kwargs_)#
    

Defines a markdown object.

Parameters:
    

  * **markdown** â the markdown to display

  * **name** â the name of the property




media_player(_name_ , _url_ , _** kwargs_)#
    

Defines a media player object.

Parameters:
    

  * **name** â the name of the property

  * **url** â the URL of the media to display

  * **on_start** (_None_) â the operator to execute when the media starts

  * **on_play** (_None_) â the operator to execute when the media is played

  * **on_pause** (_None_) â the operator to execute when the media is paused

  * **on_buffer** (_None_) â the operator to execute when the media is buffering

  * **on_buffer_end** (_None_) â the operator to execute when the media stops buffering

  * **on_ended** (_None_) â the operator to execute when the media ends

  * **on_error** (_None_) â the operator to execute when the media errors

  * **on_duration** (_None_) â the operator to execute when the media duration is loaded

  * **on_seek** (_None_) â the operator to execute when the media is seeked

  * **on_progress** (_None_) â the operator to execute when the media progresses



Returns:
    

a `Object`

arrow_nav(_name_ , _forward =None_, _backward =None_, _position =None_, _** kwargs_)#
    

Defines a floating navigation arrows as a `ArrowNavView`.

Parameters:
    

  * **forward** (_True_) â Whether to display the forward arrow

  * **backward** (_True_) â Whether to display the backward arrow

  * **on_forward** (_None_) â The operator to execute when the forward arrow is clicked

  * **on_backward** (_None_) â The operator to execute when the backward arrow is clicked

  * **position** (_"center"_) â The position of the arrows. Can be either `"top"`, `center`, `"bottom"`, `"left"`, `middle` (center horizontally), or ``"right"`



Returns:
    

a `Property`

map(_name_ , _key_type_ , _value_type_ , _** kwargs_)#
    

Defines a map property on the object.

Parameters:
    

  * **name** â the name of the property

  * **key_type** â the type of the keys in the map

  * **value_type** â the type of the values in the map



Returns:
    

a `Map`

oneof(_name_ , _types_ , _** kwargs_)#
    

Defines a one-of property on the object.

Parameters:
    

  * **name** â the name of the property

  * **types** â list of types that are instances of `BaseType`



Returns:
    

a `OneOf`

tuple(_name_ , _* items_, _** kwargs_)#
    

Defines a tuple property on the object.

Parameters:
    

  * **name** â the name of the property

  * ***items** â the types of the items in the tuple



Returns:
    

a `Tuple`

tree(_name_ , _** kwargs_)#
    

Defines a tree property on the object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Tree`

clone()#
    

Clones the definition of the object.

Parameters:
    

**name** â the name of the property

Returns:
    

an `Object`

view_target(_ctx_ , _name ='view_target'_, _view_type =None_, _action_description ='Process'_, _default_target =None_, _allow_selected_samples =True_, _allow_selected_labels =False_, _allow_dataset_view =False_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _** kwargs_)#
    

Defines a view target input property.

This property has an enum input that allows the user to select which view to process. The available choices depend on the current context and the provided flags.

The choices include:

  * Entire dataset (if the current view is not a generated view)

  * Base view (if the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), which is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

  * Dataset view (if `allow_dataset_view` is `True`)

  * Current view (if the current view is different from the dataset view)

  * Selected samples (if `allow_selected_samples` is `True` and there are selected samples)

  * Selected labels (if `allow_selected_labels` is `True` and there are selected labels)




If thereâs no view or selected items, the only option is entire dataset, so the view target selector is hidden and âDATASETâ will be returned.

The resolved target view can be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

The target view descriptions are generated based on the provided `action_description` and the various description parameters. If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

Examples:
    
    
    import fiftyone.operators as foo
    
    class MyTargetViewOperator(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="target_view_operator",
                label="Testing Target View Operator",
                dynamic=True,
            )
    
        def resolve_input(self, ctx):
            inputs = types.Object()
    
            view_target_prop = inputs.view_target(ctx)
    
            return types.Property(
                inputs, view=types.View(label="Target View Operator")
            )
    
        def execute(self, ctx):
            target_view = ctx.target_view()
            # Do something with the target view
            print("Sample collection size", len(target_view))
    
    Args:
        ctx: the operator's :class:`fiftyone.operators.ExecutionContext`
        name(view_target): the name of the view target property
        view_type (RadioGroup): the view type to use (RadioGroup, Dropdown,
            etc.)
        default_target (None): the default target view to select if
            multiple choices are available. If ``None`` or
            ``default_target`` is not an available choice, the most
            targeted / selective available choice is chosen.
        action_description (Process): a short description of the action
            being performed, used to generate default descriptions for the
            various target views
        allow_selected_samples (True): whether to allow the "selected
            samples" target view
        allow_selected_labels (False): whether to allow the "selected
            labels" target view
        allow_dataset_view (False): whether to allow the "dataset view"
            target view
        base_view_label (Base view): the label for the "base view" target
            view
        base_view_description (None): the description for the "base view"
            target view. If ``None``, a default description is generated
        current_view_label (Current view): the label for the "current
            view" target view
        current_view_description (None): the description for the "current
            view" target view. If ``None``, a default description is
            generated
        dataset_label (Entire dataset): the label for the "entire dataset"
            target view
        dataset_description (None): the description for the "entire
            dataset" target view. If ``None``, a default description is
            generated
        dataset_view_label (Dataset): the label for the "dataset view"
            target view
        dataset_view_description (None): the description for the "dataset
            view" target view. If ``None``, a default description is
            generated
        selected_samples_label (Selected samples): the label for the
            "selected samples" target view
        selected_samples_description (None): the description for the
            "selected samples" target view. If ``None``, a default
            description is generated
        selected_labels_label (Selected labels): the label for the
            "selected labels" target view
        selected_labels_description (None): the description for the
            "selected labels" target view. If ``None``, a default
            description is generated
    
    Returns:
        a :class:`ViewTargetProperty`
    

target_view(_ctx_ , _name ='view_target'_, _view_type =None_, _action_description ='Process'_, _default_target =None_, _allow_selected_samples =True_, _allow_selected_labels =False_, _allow_dataset_view =False_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _** kwargs_)#
    

Defines a view target input property.

This property has an enum input that allows the user to select which view to process. The available choices depend on the current context and the provided flags.

The choices include:

  * Entire dataset (if the current view is not a generated view)

  * Base view (if the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), which is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

  * Dataset view (if `allow_dataset_view` is `True`)

  * Current view (if the current view is different from the dataset view)

  * Selected samples (if `allow_selected_samples` is `True` and there are selected samples)

  * Selected labels (if `allow_selected_labels` is `True` and there are selected labels)




If thereâs no view or selected items, the only option is entire dataset, so the view target selector is hidden and âDATASETâ will be returned.

The resolved target view can be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

The target view descriptions are generated based on the provided `action_description` and the various description parameters. If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

Examples:
    
    
    import fiftyone.operators as foo
    
    class MyTargetViewOperator(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="target_view_operator",
                label="Testing Target View Operator",
                dynamic=True,
            )
    
        def resolve_input(self, ctx):
            inputs = types.Object()
    
            view_target_prop = inputs.view_target(ctx)
    
            return types.Property(
                inputs, view=types.View(label="Target View Operator")
            )
    
        def execute(self, ctx):
            target_view = ctx.target_view()
            # Do something with the target view
            print("Sample collection size", len(target_view))
    
    Args:
        ctx: the operator's :class:`fiftyone.operators.ExecutionContext`
        name(view_target): the name of the view target property
        view_type (RadioGroup): the view type to use (RadioGroup, Dropdown,
            etc.)
        default_target (None): the default target view to select if
            multiple choices are available. If ``None`` or
            ``default_target`` is not an available choice, the most
            targeted / selective available choice is chosen.
        action_description (Process): a short description of the action
            being performed, used to generate default descriptions for the
            various target views
        allow_selected_samples (True): whether to allow the "selected
            samples" target view
        allow_selected_labels (False): whether to allow the "selected
            labels" target view
        allow_dataset_view (False): whether to allow the "dataset view"
            target view
        base_view_label (Base view): the label for the "base view" target
            view
        base_view_description (None): the description for the "base view"
            target view. If ``None``, a default description is generated
        current_view_label (Current view): the label for the "current
            view" target view
        current_view_description (None): the description for the "current
            view" target view. If ``None``, a default description is
            generated
        dataset_label (Entire dataset): the label for the "entire dataset"
            target view
        dataset_description (None): the description for the "entire
            dataset" target view. If ``None``, a default description is
            generated
        dataset_view_label (Dataset): the label for the "dataset view"
            target view
        dataset_view_description (None): the description for the "dataset
            view" target view. If ``None``, a default description is
            generated
        selected_samples_label (Selected samples): the label for the
            "selected samples" target view
        selected_samples_description (None): the description for the
            "selected samples" target view. If ``None``, a default
            description is generated
        selected_labels_label (Selected labels): the label for the
            "selected labels" target view
        selected_labels_description (None): the description for the
            "selected labels" target view. If ``None``, a default
            description is generated
    
    Returns:
        a :class:`ViewTargetProperty`
    

to_json()#
    

Converts the object definition to JSON.

Returns:
    

a JSON dict

class fiftyone.operators.types.Property(_type_ , _** kwargs_)#
    

Bases: `BaseType`

Represents a property on an [`fiftyone.operators.Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator").

Properties are used to define the data that an operator can accept as input and return as output.

Properties may also define a `View` that can be used to customize how the property behaves in the FiftyOne App.

Examples:
    
    
    import fiftyone.operators.types as types
    
    my_object = types.Object()
    
    # Define a string property
    my_object.str("name", label="Name", description="a description")
    
    # Define an enum property with a custom view
    radio_group = types.RadioGroup()
    radio_group.add_choice("car", "A brand new car")
    radio_group.add_choice("truck", "A fancy truck")
    my_object.enum("type", radio_group.values(), view=radio_group)
    

Parameters:
    

  * **type** â the type of the property

  * **invalid** (_False_) â whether the property is invalid

  * **default** (_None_) â the default value of the property

  * **required** (_False_) â whether the property is required

  * **error_message** (_"Invalid"_) â the error message of the property

  * **view** (_None_) â the `View` of the property




**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.ResolvableProperty(_resolver : str_, _** kwargs_)#
    

Bases: `BaseType`

Represents a resolvable property.

Parameters:
    

  * **resolver** (_str_) â operator to resolve the schema for this property

  * **debounce** (_None_) â whether to debounce the resolver

  * **throttle** (_None_) â whether to throttle the resolver

  * **wait** (_None_) â wait time in milliseconds for when debounce or throttle is True

  * **auto_update** (_True_) â whether to auto-update the property when dependencies change

  * **dependencies** ([_list_](api__fiftyone.core.session.events.md#fiftyone.core.session.events.Colorscale.list "fiftyone.core.session.events.Colorscale.list")) â list of property names that this property depends on

  * **params** (_dict_) â parameters to pass to the resolver

  * **validate** (_False_) â whether the property should be validated. If True, the operator will not be allowed to execute until this property is resolved and validated.

  * **leading** (_False_) â whether to invoke the resolver on the leading edge when debouncing or throttling is enabled.

  * **trailing** (_True_) â whether to invoke the resolver on the trailing edge when debouncing or throttling is enabled.




**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.String(_allow_empty =False_)#
    

Bases: `BaseType`

Represents a string.

Parameters:
    

**allow_empty** (_False_) â allow an empty string value

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Boolean#
    

Bases: `BaseType`

Represents a boolean.

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Number(_min =None_, _max =None_, _int =False_, _float =False_)#
    

Bases: `BaseType`

Represents a number.

Parameters:
    

  * **min** (_None_) â the minimum value of the `Number`

  * **max** (_None_) â the maximum value of the `Number`

  * **int** (_False_) â whether the number is an integer

  * **float** (_False_) â whether the number is a float




**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.List(_element_type_ , _min_items =None_, _max_items =None_)#
    

Bases: `BaseType`

Represents a list.

Parameters:
    

  * **element_type** â the type of the elements in the list

  * **min_items** (_None_) â the minimum number of items in the list

  * **max_items** (_None_) â the maximum number of items in the list




**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.SampleID#
    

Bases: `String`

Represents a `fiftyone.core.samples.Sample` ID.

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Enum(_values_)#
    

Bases: `BaseType`

Represents an enum.

Parameters:
    

**values** â the values of the enum

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.OneOf(_types_)#
    

Bases: `BaseType`

Represents a one-of type.

Examples:
    
    
    import fiftyone.operators.types as types
    
    my_object = types.Object()
    my_object.define_property(
        "my_property",
        types.OneOf([types.String(), types.Number()],
    )
    

Parameters:
    

**types** â the possible types

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Tuple(_* items_)#
    

Bases: `BaseType`

Represents a tuple of types.

Examples:
    
    
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    inputs.define_property(
        "image", types.Tuple(types.String(), types.Number())
    )
    

Parameters:
    

***items** â the types

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Tree(_* items_)#
    

Bases: `BaseType`

Represents a tree selection type.

Examples:
    
    
    import fiftyone.operators.types as types
    inputs = types.Object()
    

Parameters:
    

***items** â the tree structure of items

**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Map(_key_type_ , _value_type_)#
    

Bases: `BaseType`

Represents a map.

Examples:
    
    
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    inputs.define_property(
        "image", types.Map(types.String(), types.Number())
    )
    

Parameters:
    

  * **key_type** â the type of the keys in the `Map`

  * **value_type** â the type of the values in the `Map`




**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.File(_** kwargs_)#
    

Bases: `Object`

Represents a file and related metadata for use with `FileExplorerView`.

**Methods:**

`add_property`(name,Â property) | Adds a property to the object.  
---|---  
`arrow_nav`(name[,Â forward,Â backward,Â position]) | Defines a floating navigation arrows as a `ArrowNavView`.  
`bool`(name,Â **kwargs) | Defines a property on the object that is a boolean.  
`btn`(name,Â label[,Â icon,Â variant,Â disabled,Â ...]) | Defines a button or icon button to display to the user as a `Button`.  
`btn_group`(name,Â **kwargs) | Defines a button group object.  
`clone`() | Clones the definition of the object.  
`dashboard`(name,Â **kwargs) | Defines a dashboard view as a `View`.  
`define_property`(name,Â type,Â **kwargs) | Defines a property on the object.  
`enum`(name,Â values,Â **kwargs) | Defines a property on the object that is an enum.  
`file`(name,Â **kwargs) | Defines a property on the object that is a file.  
`float`(name[,Â min,Â max]) | Defines a property on the object that is a float.  
`get_property`(name) | Gets a property by name.  
`grid`(name,Â **kwargs) | Defines a grid view as a `View`.  
`h_stack`(name,Â **kwargs) | Defines a horizontal stack object.  
`img`(name[,Â href,Â on_click,Â prompt,Â params,Â ...]) | Defines an image to display to the user as a `ImageView`.  
`int`(name[,Â min,Â max]) | Defines a property on the object that is an integer.  
`list`(name,Â element_type[,Â min_items,Â max_items]) | Defines a property on the object that is a list.  
`loader`(name,Â type,Â operator[,Â params,Â ...]) | Defines a loader property that fetches data asynchronously.  
`map`(name,Â key_type,Â value_type,Â **kwargs) | Defines a map property on the object.  
`md`(markdown[,Â name]) | Defines a markdown object.  
`media_player`(name,Â url,Â **kwargs) | Defines a media player object.  
`menu`(name,Â **kwargs) | Defined an `Object` property that is displayed as a menu.  
`message`(name,Â label,Â **kwargs) | Defines a message to display to the user as a `Notice`.  
`obj`(name,Â **kwargs) | Defines a property on the object that is an object.  
`oneof`(name,Â types,Â **kwargs) | Defines a one-of property on the object.  
`plot`(name,Â **kwargs) | Defines an object property displayed as a plot.  
`str`(name[,Â allow_empty]) | Defines a property on the object that is a string.  
`target_view`(ctx[,Â name,Â view_type,Â ...]) | Defines a view target input property.  
`to_json`() | Converts the object definition to JSON.  
`tree`(name,Â **kwargs) | Defines a tree property on the object.  
`tuple`(name,Â *items,Â **kwargs) | Defines a tuple property on the object.  
`uploaded_file`(name,Â **kwargs) | Defines a property on the object that is an uploaded file.  
`v_stack`(name,Â **kwargs) | Defines a vertical stack object.  
`view`(name,Â view,Â **kwargs) | Defines a view-only property.  
`view_target`(ctx[,Â name,Â view_type,Â ...]) | Defines a view target input property.  
  
add_property(_name_ , _property_)#
    

Adds a property to the object.

Parameters:
    

  * **name** â the name of the property

  * **property** â the property to add



Returns:
    

the `Property` that was added

arrow_nav(_name_ , _forward =None_, _backward =None_, _position =None_, _** kwargs_)#
    

Defines a floating navigation arrows as a `ArrowNavView`.

Parameters:
    

  * **forward** (_True_) â Whether to display the forward arrow

  * **backward** (_True_) â Whether to display the backward arrow

  * **on_forward** (_None_) â The operator to execute when the forward arrow is clicked

  * **on_backward** (_None_) â The operator to execute when the backward arrow is clicked

  * **position** (_"center"_) â The position of the arrows. Can be either `"top"`, `center`, `"bottom"`, `"left"`, `middle` (center horizontally), or ``"right"`



Returns:
    

a `Property`

bool(_name_ , _** kwargs_)#
    

Defines a property on the object that is a boolean.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

btn(_name_ , _label_ , _icon =None_, _variant =None_, _disabled =False_, _on_click =None_, _prompt =False_, _params =None_, _space =None_, _href =None_, _icon_position ='left'_, _** kwargs_)#
    

Defines a button or icon button to display to the user as a `Button`.

Examples:
    
    
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    inputs.btn(
        "greet",
        label="Say Hi!",
        icon="waving_hand",
        variant="round",
        on_click="print_stdout",
        params={"msg": "Hi!"},
    )
    

Parameters:
    

  * **name** â the name of the property

  * **label** â the label of the button

  * **icon** (_None_) â the name of the icon to display

  * **icon_position** (_"left"_) â the position of the icon. Can be `"left"` or `"right"`

  * **disabled** (_False_) â whether the button is disabled

  * **variant** (_None_) â the variant of the button. Can be `"contained"`, `"outlined"`, `"round"` or `"square"`

  * **on_click** (_None_) â the name of the operator to execute when the button is clicked

  * **prompt** (_False_) â whether to prompt the user before executing the operator

  * **params** (_None_) â the parameters to pass to the operator

  * **space** (_None_) â An int specifying how much vertical/horizontal space to allocate out of `12` depending on the orientation of the parent container

  * **href** (_None_) â the URL to navigate to when the button is clicked




btn_group(_name_ , _** kwargs_)#
    

Defines a button group object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

clone()#
    

Clones the definition of the object.

Parameters:
    

**name** â the name of the property

Returns:
    

an `Object`

dashboard(_name_ , _** kwargs_)#
    

Defines a dashboard view as a `View`.

See `DashboardView` for more information.

Parameters:
    

**name** â the name of the property

Returns:
    

an `Object`

See `DashboardView` for more information.

define_property(_name_ , _type_ , _** kwargs_)#
    

Defines a property on the object.

Parameters:
    

  * **name** â the name of the property

  * **type** â the type of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

the `Property` that was added

enum(_name_ , _values_ , _** kwargs_)#
    

Defines a property on the object that is an enum.

Parameters:
    

  * **name** â the name of the property

  * **values** â a list of values that define the enum

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property, which must be a `Choices` or a subclass of it



Returns:
    

a `Property`

file(_name_ , _** kwargs_)#
    

Defines a property on the object that is a file.

Parameters:
    

  * **name** â the name of the property

  * **view** (_None_) â the `View` of the property




float(_name_ , _min =None_, _max =None_, _** kwargs_)#
    

Defines a property on the object that is a float.

Parameters:
    

  * **name** â the name of the property

  * **min** â minimum value of the property

  * **max** â maximum value of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

get_property(_name_)#
    

Gets a property by name.

Parameters:
    

**name** â the name of the property

Returns:
    

the `Property`, or None

grid(_name_ , _** kwargs_)#
    

Defines a grid view as a `View`.

h_stack(_name_ , _** kwargs_)#
    

Defines a horizontal stack object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

img(_name_ , _href =None_, _on_click =None_, _prompt =False_, _params =None_, _point_on_hover =True_, _height =None_, _width =None_, _alt_text =None_, _** kwargs_)#
    

Defines an image to display to the user as a `ImageView`.

Examples:
    
    
    import fiftyone.operators.types as types
    ctx.panel.state.my_img = "/path/to/my/image.jpg"
    
    panel = types.Object()
    panel.img(
        "my_img", # uses the value in ctx.panel.state.my_img
        href="https://path/to/navigate/to",
        on_click=self.do_something,
        prompt=False,
        params={"foo": "bar"},
        point_on_hover=True,
        height="100px",
        width="100px",
        alt_text="My image alt text"
    )
    

Parameters:
    

  * **name** â the name of the state variable to use as the image source

  * **href** (_None_) â the url to navigate to when the image is clicked

  * **on_click** (_None_) â the name of the operator to execute when the button is clicked

  * **prompt** (_False_) â whether to prompt the user before executing the operator

  * **params** (_None_) â the parameters to pass to the operator

  * **point_on_hover** (_True_) â whether to show a pointer when hovering over the image

  * **height** (_None_) â the height of the image

  * **width** (_None_) â the width of the image

  * **alt_text** (_None_) â the alt text of the image




int(_name_ , _min =None_, _max =None_, _** kwargs_)#
    

Defines a property on the object that is an integer.

Parameters:
    

  * **name** â the name of the property

  * **min** â minimum value of the property

  * **max** â maximum value of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

list(_name_ , _element_type_ , _min_items =None_, _max_items =None_, _** kwargs_)#
    

Defines a property on the object that is a list.

Parameters:
    

  * **name** â the name of the property

  * **element_type** â the type of the elements in the list

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

loader(_name_ , _type_ , _operator_ , _params =None_, _label =None_, _placeholder_view =None_, _dependencies =None_, _** kwargs_)#
    

Defines a loader property that fetches data asynchronously.

The loader executes an operator and stores the result at the property path. The property value always has the following structure:
    
    
    {
        "state": "idle" | "loading" | "loaded" | "errored",
        "data": <type>,  # the loaded data, shaped by the type argument
        "error": <str>   # error message (when state is "errored")
    }
    

The `type` argument defines the shape of the `data` field, not the entire loader value. For example, if `type=types.List(types.Object())`, then `ctx.params[name]["data"]` will be a list of objects.

By default, the loader executes only once when the component mounts. Use the `dependencies` argument to specify which param paths should trigger a reload when their values change.

Examples:
    
    
    def resolve_input(self, ctx):
        inputs = types.Object()
    
        inputs.str("make", label="Car Make")
    
        chosen_make = ctx.params.get("make")
        if chosen_make:
            inputs.loader(
                "available_models",
                type=types.List(types.Object()),
                operator="@my-plugin/load_models",
                params={"make": chosen_make},
                label="Loading models...",
                dependencies=["make"],  # reload when "make" changes
            )
    
        models = ctx.params.get("available_models", {})
        if models.get("state") == "loaded":
            choices = Choices()
            for model in models.get("data", []):
                choices.add_choice(model["id"], label=model["name"])
            inputs.enum("model", values=choices)
    
        return types.Property(inputs)
    

Parameters:
    

  * **name** â the name of the property

  * **type** â the type of the `data` field within the loader value (e.g., `types.Object()`, `types.List(types.Object())`)

  * **operator** â the operator to execute (string URI or callable method)

  * **params** (_None_) â parameters to pass to the operator

  * **label** (_None_) â loading message to display

  * **placeholder_view** (_None_) â view to render while loading

  * **dependencies** (_None_) â list of param paths (dot-notation supported) that should trigger a reload when changed. If None, the loader only executes once on mount



Returns:
    

a `Property`

map(_name_ , _key_type_ , _value_type_ , _** kwargs_)#
    

Defines a map property on the object.

Parameters:
    

  * **name** â the name of the property

  * **key_type** â the type of the keys in the map

  * **value_type** â the type of the values in the map



Returns:
    

a `Map`

md(_markdown_ , _name ='markdown'_, _** kwargs_)#
    

Defines a markdown object.

Parameters:
    

  * **markdown** â the markdown to display

  * **name** â the name of the property




media_player(_name_ , _url_ , _** kwargs_)#
    

Defines a media player object.

Parameters:
    

  * **name** â the name of the property

  * **url** â the URL of the media to display

  * **on_start** (_None_) â the operator to execute when the media starts

  * **on_play** (_None_) â the operator to execute when the media is played

  * **on_pause** (_None_) â the operator to execute when the media is paused

  * **on_buffer** (_None_) â the operator to execute when the media is buffering

  * **on_buffer_end** (_None_) â the operator to execute when the media stops buffering

  * **on_ended** (_None_) â the operator to execute when the media ends

  * **on_error** (_None_) â the operator to execute when the media errors

  * **on_duration** (_None_) â the operator to execute when the media duration is loaded

  * **on_seek** (_None_) â the operator to execute when the media is seeked

  * **on_progress** (_None_) â the operator to execute when the media progresses



Returns:
    

a `Object`

menu(_name_ , _** kwargs_)#
    

Defined an `Object` property that is displayed as a menu.

Note

Can be used for an `Button` type with properties whose views are one of `Button`, `Dropdown`, `DropdownView`, and :class;`Choices`. The variant and color of the items can be set using the variant and color parameters.

Parameters:
    

  * **name** â the name of the property

  * **variant** (_None_) â the variant for the items of the menu. Can be `"contained"`, `"outlined"`, `"round"` or `"square"`

  * **color** (_None_) â the color for the items of the menu.

  * **overlay** (_None_) â whether to display the menu as an overlay. Can be `"top-left"`,

  * **"top-center"**

  * **"top-right"**

  * **"bottom-left"**

  * **"bottom-center"`**

  * **or**

  * **of** (_"bottom-right". Overlay is useful when you want to display a floating menu on top_)

  * **content** (_another_)

  * **icon** (_None_) â when set, the icon will be displayed as the menu button instead of the label.

  * **"SettingsIcon"** (_Can be_)

  * **"MoreVertIcon".**



Returns:
    

a `Object`

message(_name_ , _label_ , _** kwargs_)#
    

Defines a message to display to the user as a `Notice`.

Parameters:
    

  * **name** â the name of the property

  * **label** â the label of the notice

  * **description** (_None_) â the description of the notice

  * **view** (_None_) â the `View` of the notice



Returns:
    

a `Property`

obj(_name_ , _** kwargs_)#
    

Defines a property on the object that is an object.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

oneof(_name_ , _types_ , _** kwargs_)#
    

Defines a one-of property on the object.

Parameters:
    

  * **name** â the name of the property

  * **types** â list of types that are instances of `BaseType`



Returns:
    

a `OneOf`

plot(_name_ , _** kwargs_)#
    

Defines an object property displayed as a plot.

Parameters:
    

  * **name** â the name of the property

  * **config** (_None_) â the chart config

  * **layout** (_None_) â the chart layout




See `PlotlyView` for more information.

str(_name_ , _allow_empty =False_, _** kwargs_)#
    

Defines a property on the object that is a string.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

target_view(_ctx_ , _name ='view_target'_, _view_type =None_, _action_description ='Process'_, _default_target =None_, _allow_selected_samples =True_, _allow_selected_labels =False_, _allow_dataset_view =False_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _** kwargs_)#
    

Defines a view target input property.

This property has an enum input that allows the user to select which view to process. The available choices depend on the current context and the provided flags.

The choices include:

  * Entire dataset (if the current view is not a generated view)

  * Base view (if the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), which is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

  * Dataset view (if `allow_dataset_view` is `True`)

  * Current view (if the current view is different from the dataset view)

  * Selected samples (if `allow_selected_samples` is `True` and there are selected samples)

  * Selected labels (if `allow_selected_labels` is `True` and there are selected labels)




If thereâs no view or selected items, the only option is entire dataset, so the view target selector is hidden and âDATASETâ will be returned.

The resolved target view can be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

The target view descriptions are generated based on the provided `action_description` and the various description parameters. If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

Examples:
    
    
    import fiftyone.operators as foo
    
    class MyTargetViewOperator(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="target_view_operator",
                label="Testing Target View Operator",
                dynamic=True,
            )
    
        def resolve_input(self, ctx):
            inputs = types.Object()
    
            view_target_prop = inputs.view_target(ctx)
    
            return types.Property(
                inputs, view=types.View(label="Target View Operator")
            )
    
        def execute(self, ctx):
            target_view = ctx.target_view()
            # Do something with the target view
            print("Sample collection size", len(target_view))
    
    Args:
        ctx: the operator's :class:`fiftyone.operators.ExecutionContext`
        name(view_target): the name of the view target property
        view_type (RadioGroup): the view type to use (RadioGroup, Dropdown,
            etc.)
        default_target (None): the default target view to select if
            multiple choices are available. If ``None`` or
            ``default_target`` is not an available choice, the most
            targeted / selective available choice is chosen.
        action_description (Process): a short description of the action
            being performed, used to generate default descriptions for the
            various target views
        allow_selected_samples (True): whether to allow the "selected
            samples" target view
        allow_selected_labels (False): whether to allow the "selected
            labels" target view
        allow_dataset_view (False): whether to allow the "dataset view"
            target view
        base_view_label (Base view): the label for the "base view" target
            view
        base_view_description (None): the description for the "base view"
            target view. If ``None``, a default description is generated
        current_view_label (Current view): the label for the "current
            view" target view
        current_view_description (None): the description for the "current
            view" target view. If ``None``, a default description is
            generated
        dataset_label (Entire dataset): the label for the "entire dataset"
            target view
        dataset_description (None): the description for the "entire
            dataset" target view. If ``None``, a default description is
            generated
        dataset_view_label (Dataset): the label for the "dataset view"
            target view
        dataset_view_description (None): the description for the "dataset
            view" target view. If ``None``, a default description is
            generated
        selected_samples_label (Selected samples): the label for the
            "selected samples" target view
        selected_samples_description (None): the description for the
            "selected samples" target view. If ``None``, a default
            description is generated
        selected_labels_label (Selected labels): the label for the
            "selected labels" target view
        selected_labels_description (None): the description for the
            "selected labels" target view. If ``None``, a default
            description is generated
    
    Returns:
        a :class:`ViewTargetProperty`
    

to_json()#
    

Converts the object definition to JSON.

Returns:
    

a JSON dict

tree(_name_ , _** kwargs_)#
    

Defines a tree property on the object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Tree`

tuple(_name_ , _* items_, _** kwargs_)#
    

Defines a tuple property on the object.

Parameters:
    

  * **name** â the name of the property

  * ***items** â the types of the items in the tuple



Returns:
    

a `Tuple`

uploaded_file(_name_ , _** kwargs_)#
    

Defines a property on the object that is an uploaded file.

Parameters:
    

  * **name** â the name of the property

  * **view** (_None_) â the `View` of the property

  * **lite** (_False_) â whether to use the lite version of the file. When True, the content of the file in not included in resolve_input params, only the metadata is included.




v_stack(_name_ , _** kwargs_)#
    

Defines a vertical stack object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

view(_name_ , _view_ , _** kwargs_)#
    

Defines a view-only property.

Examples:
    
    
    import fiftyone.operators.types as types
    
    notice = types.Notice(label="a label", description="a description")
    inputs = types.Object()
    inputs.view("notice", notice)
    

Parameters:
    

  * **name** â the name of the property

  * **view** â the `View` to define



Returns:
    

a `Property`

view_target(_ctx_ , _name ='view_target'_, _view_type =None_, _action_description ='Process'_, _default_target =None_, _allow_selected_samples =True_, _allow_selected_labels =False_, _allow_dataset_view =False_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _** kwargs_)#
    

Defines a view target input property.

This property has an enum input that allows the user to select which view to process. The available choices depend on the current context and the provided flags.

The choices include:

  * Entire dataset (if the current view is not a generated view)

  * Base view (if the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), which is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

  * Dataset view (if `allow_dataset_view` is `True`)

  * Current view (if the current view is different from the dataset view)

  * Selected samples (if `allow_selected_samples` is `True` and there are selected samples)

  * Selected labels (if `allow_selected_labels` is `True` and there are selected labels)




If thereâs no view or selected items, the only option is entire dataset, so the view target selector is hidden and âDATASETâ will be returned.

The resolved target view can be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

The target view descriptions are generated based on the provided `action_description` and the various description parameters. If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

Examples:
    
    
    import fiftyone.operators as foo
    
    class MyTargetViewOperator(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="target_view_operator",
                label="Testing Target View Operator",
                dynamic=True,
            )
    
        def resolve_input(self, ctx):
            inputs = types.Object()
    
            view_target_prop = inputs.view_target(ctx)
    
            return types.Property(
                inputs, view=types.View(label="Target View Operator")
            )
    
        def execute(self, ctx):
            target_view = ctx.target_view()
            # Do something with the target view
            print("Sample collection size", len(target_view))
    
    Args:
        ctx: the operator's :class:`fiftyone.operators.ExecutionContext`
        name(view_target): the name of the view target property
        view_type (RadioGroup): the view type to use (RadioGroup, Dropdown,
            etc.)
        default_target (None): the default target view to select if
            multiple choices are available. If ``None`` or
            ``default_target`` is not an available choice, the most
            targeted / selective available choice is chosen.
        action_description (Process): a short description of the action
            being performed, used to generate default descriptions for the
            various target views
        allow_selected_samples (True): whether to allow the "selected
            samples" target view
        allow_selected_labels (False): whether to allow the "selected
            labels" target view
        allow_dataset_view (False): whether to allow the "dataset view"
            target view
        base_view_label (Base view): the label for the "base view" target
            view
        base_view_description (None): the description for the "base view"
            target view. If ``None``, a default description is generated
        current_view_label (Current view): the label for the "current
            view" target view
        current_view_description (None): the description for the "current
            view" target view. If ``None``, a default description is
            generated
        dataset_label (Entire dataset): the label for the "entire dataset"
            target view
        dataset_description (None): the description for the "entire
            dataset" target view. If ``None``, a default description is
            generated
        dataset_view_label (Dataset): the label for the "dataset view"
            target view
        dataset_view_description (None): the description for the "dataset
            view" target view. If ``None``, a default description is
            generated
        selected_samples_label (Selected samples): the label for the
            "selected samples" target view
        selected_samples_description (None): the description for the
            "selected samples" target view. If ``None``, a default
            description is generated
        selected_labels_label (Selected labels): the label for the
            "selected labels" target view
        selected_labels_description (None): the description for the
            "selected labels" target view. If ``None``, a default
            description is generated
    
    Returns:
        a :class:`ViewTargetProperty`
    

class fiftyone.operators.types.UploadedFile(_** kwargs_)#
    

Bases: `Object`

Represents an object with uploaded file content and its metadata in properties.

Properties:
    

name: the name of the file type: the mime type of the file size: the size of the file in bytes content: the base64 encoded content of the file last_modified: the last modified time of the file in ms since epoch

**Methods:**

`add_property`(name,Â property) | Adds a property to the object.  
---|---  
`arrow_nav`(name[,Â forward,Â backward,Â position]) | Defines a floating navigation arrows as a `ArrowNavView`.  
`bool`(name,Â **kwargs) | Defines a property on the object that is a boolean.  
`btn`(name,Â label[,Â icon,Â variant,Â disabled,Â ...]) | Defines a button or icon button to display to the user as a `Button`.  
`btn_group`(name,Â **kwargs) | Defines a button group object.  
`clone`() | Clones the definition of the object.  
`dashboard`(name,Â **kwargs) | Defines a dashboard view as a `View`.  
`define_property`(name,Â type,Â **kwargs) | Defines a property on the object.  
`enum`(name,Â values,Â **kwargs) | Defines a property on the object that is an enum.  
`file`(name,Â **kwargs) | Defines a property on the object that is a file.  
`float`(name[,Â min,Â max]) | Defines a property on the object that is a float.  
`get_property`(name) | Gets a property by name.  
`grid`(name,Â **kwargs) | Defines a grid view as a `View`.  
`h_stack`(name,Â **kwargs) | Defines a horizontal stack object.  
`img`(name[,Â href,Â on_click,Â prompt,Â params,Â ...]) | Defines an image to display to the user as a `ImageView`.  
`int`(name[,Â min,Â max]) | Defines a property on the object that is an integer.  
`list`(name,Â element_type[,Â min_items,Â max_items]) | Defines a property on the object that is a list.  
`loader`(name,Â type,Â operator[,Â params,Â ...]) | Defines a loader property that fetches data asynchronously.  
`map`(name,Â key_type,Â value_type,Â **kwargs) | Defines a map property on the object.  
`md`(markdown[,Â name]) | Defines a markdown object.  
`media_player`(name,Â url,Â **kwargs) | Defines a media player object.  
`menu`(name,Â **kwargs) | Defined an `Object` property that is displayed as a menu.  
`message`(name,Â label,Â **kwargs) | Defines a message to display to the user as a `Notice`.  
`obj`(name,Â **kwargs) | Defines a property on the object that is an object.  
`oneof`(name,Â types,Â **kwargs) | Defines a one-of property on the object.  
`plot`(name,Â **kwargs) | Defines an object property displayed as a plot.  
`str`(name[,Â allow_empty]) | Defines a property on the object that is a string.  
`target_view`(ctx[,Â name,Â view_type,Â ...]) | Defines a view target input property.  
`to_json`() | Converts the object definition to JSON.  
`tree`(name,Â **kwargs) | Defines a tree property on the object.  
`tuple`(name,Â *items,Â **kwargs) | Defines a tuple property on the object.  
`uploaded_file`(name,Â **kwargs) | Defines a property on the object that is an uploaded file.  
`v_stack`(name,Â **kwargs) | Defines a vertical stack object.  
`view`(name,Â view,Â **kwargs) | Defines a view-only property.  
`view_target`(ctx[,Â name,Â view_type,Â ...]) | Defines a view target input property.  
  
add_property(_name_ , _property_)#
    

Adds a property to the object.

Parameters:
    

  * **name** â the name of the property

  * **property** â the property to add



Returns:
    

the `Property` that was added

arrow_nav(_name_ , _forward =None_, _backward =None_, _position =None_, _** kwargs_)#
    

Defines a floating navigation arrows as a `ArrowNavView`.

Parameters:
    

  * **forward** (_True_) â Whether to display the forward arrow

  * **backward** (_True_) â Whether to display the backward arrow

  * **on_forward** (_None_) â The operator to execute when the forward arrow is clicked

  * **on_backward** (_None_) â The operator to execute when the backward arrow is clicked

  * **position** (_"center"_) â The position of the arrows. Can be either `"top"`, `center`, `"bottom"`, `"left"`, `middle` (center horizontally), or ``"right"`



Returns:
    

a `Property`

bool(_name_ , _** kwargs_)#
    

Defines a property on the object that is a boolean.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

btn(_name_ , _label_ , _icon =None_, _variant =None_, _disabled =False_, _on_click =None_, _prompt =False_, _params =None_, _space =None_, _href =None_, _icon_position ='left'_, _** kwargs_)#
    

Defines a button or icon button to display to the user as a `Button`.

Examples:
    
    
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    inputs.btn(
        "greet",
        label="Say Hi!",
        icon="waving_hand",
        variant="round",
        on_click="print_stdout",
        params={"msg": "Hi!"},
    )
    

Parameters:
    

  * **name** â the name of the property

  * **label** â the label of the button

  * **icon** (_None_) â the name of the icon to display

  * **icon_position** (_"left"_) â the position of the icon. Can be `"left"` or `"right"`

  * **disabled** (_False_) â whether the button is disabled

  * **variant** (_None_) â the variant of the button. Can be `"contained"`, `"outlined"`, `"round"` or `"square"`

  * **on_click** (_None_) â the name of the operator to execute when the button is clicked

  * **prompt** (_False_) â whether to prompt the user before executing the operator

  * **params** (_None_) â the parameters to pass to the operator

  * **space** (_None_) â An int specifying how much vertical/horizontal space to allocate out of `12` depending on the orientation of the parent container

  * **href** (_None_) â the URL to navigate to when the button is clicked




btn_group(_name_ , _** kwargs_)#
    

Defines a button group object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

clone()#
    

Clones the definition of the object.

Parameters:
    

**name** â the name of the property

Returns:
    

an `Object`

dashboard(_name_ , _** kwargs_)#
    

Defines a dashboard view as a `View`.

See `DashboardView` for more information.

Parameters:
    

**name** â the name of the property

Returns:
    

an `Object`

See `DashboardView` for more information.

define_property(_name_ , _type_ , _** kwargs_)#
    

Defines a property on the object.

Parameters:
    

  * **name** â the name of the property

  * **type** â the type of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

the `Property` that was added

enum(_name_ , _values_ , _** kwargs_)#
    

Defines a property on the object that is an enum.

Parameters:
    

  * **name** â the name of the property

  * **values** â a list of values that define the enum

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property, which must be a `Choices` or a subclass of it



Returns:
    

a `Property`

file(_name_ , _** kwargs_)#
    

Defines a property on the object that is a file.

Parameters:
    

  * **name** â the name of the property

  * **view** (_None_) â the `View` of the property




float(_name_ , _min =None_, _max =None_, _** kwargs_)#
    

Defines a property on the object that is a float.

Parameters:
    

  * **name** â the name of the property

  * **min** â minimum value of the property

  * **max** â maximum value of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

get_property(_name_)#
    

Gets a property by name.

Parameters:
    

**name** â the name of the property

Returns:
    

the `Property`, or None

grid(_name_ , _** kwargs_)#
    

Defines a grid view as a `View`.

h_stack(_name_ , _** kwargs_)#
    

Defines a horizontal stack object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

img(_name_ , _href =None_, _on_click =None_, _prompt =False_, _params =None_, _point_on_hover =True_, _height =None_, _width =None_, _alt_text =None_, _** kwargs_)#
    

Defines an image to display to the user as a `ImageView`.

Examples:
    
    
    import fiftyone.operators.types as types
    ctx.panel.state.my_img = "/path/to/my/image.jpg"
    
    panel = types.Object()
    panel.img(
        "my_img", # uses the value in ctx.panel.state.my_img
        href="https://path/to/navigate/to",
        on_click=self.do_something,
        prompt=False,
        params={"foo": "bar"},
        point_on_hover=True,
        height="100px",
        width="100px",
        alt_text="My image alt text"
    )
    

Parameters:
    

  * **name** â the name of the state variable to use as the image source

  * **href** (_None_) â the url to navigate to when the image is clicked

  * **on_click** (_None_) â the name of the operator to execute when the button is clicked

  * **prompt** (_False_) â whether to prompt the user before executing the operator

  * **params** (_None_) â the parameters to pass to the operator

  * **point_on_hover** (_True_) â whether to show a pointer when hovering over the image

  * **height** (_None_) â the height of the image

  * **width** (_None_) â the width of the image

  * **alt_text** (_None_) â the alt text of the image




int(_name_ , _min =None_, _max =None_, _** kwargs_)#
    

Defines a property on the object that is an integer.

Parameters:
    

  * **name** â the name of the property

  * **min** â minimum value of the property

  * **max** â maximum value of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

list(_name_ , _element_type_ , _min_items =None_, _max_items =None_, _** kwargs_)#
    

Defines a property on the object that is a list.

Parameters:
    

  * **name** â the name of the property

  * **element_type** â the type of the elements in the list

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

loader(_name_ , _type_ , _operator_ , _params =None_, _label =None_, _placeholder_view =None_, _dependencies =None_, _** kwargs_)#
    

Defines a loader property that fetches data asynchronously.

The loader executes an operator and stores the result at the property path. The property value always has the following structure:
    
    
    {
        "state": "idle" | "loading" | "loaded" | "errored",
        "data": <type>,  # the loaded data, shaped by the type argument
        "error": <str>   # error message (when state is "errored")
    }
    

The `type` argument defines the shape of the `data` field, not the entire loader value. For example, if `type=types.List(types.Object())`, then `ctx.params[name]["data"]` will be a list of objects.

By default, the loader executes only once when the component mounts. Use the `dependencies` argument to specify which param paths should trigger a reload when their values change.

Examples:
    
    
    def resolve_input(self, ctx):
        inputs = types.Object()
    
        inputs.str("make", label="Car Make")
    
        chosen_make = ctx.params.get("make")
        if chosen_make:
            inputs.loader(
                "available_models",
                type=types.List(types.Object()),
                operator="@my-plugin/load_models",
                params={"make": chosen_make},
                label="Loading models...",
                dependencies=["make"],  # reload when "make" changes
            )
    
        models = ctx.params.get("available_models", {})
        if models.get("state") == "loaded":
            choices = Choices()
            for model in models.get("data", []):
                choices.add_choice(model["id"], label=model["name"])
            inputs.enum("model", values=choices)
    
        return types.Property(inputs)
    

Parameters:
    

  * **name** â the name of the property

  * **type** â the type of the `data` field within the loader value (e.g., `types.Object()`, `types.List(types.Object())`)

  * **operator** â the operator to execute (string URI or callable method)

  * **params** (_None_) â parameters to pass to the operator

  * **label** (_None_) â loading message to display

  * **placeholder_view** (_None_) â view to render while loading

  * **dependencies** (_None_) â list of param paths (dot-notation supported) that should trigger a reload when changed. If None, the loader only executes once on mount



Returns:
    

a `Property`

map(_name_ , _key_type_ , _value_type_ , _** kwargs_)#
    

Defines a map property on the object.

Parameters:
    

  * **name** â the name of the property

  * **key_type** â the type of the keys in the map

  * **value_type** â the type of the values in the map



Returns:
    

a `Map`

md(_markdown_ , _name ='markdown'_, _** kwargs_)#
    

Defines a markdown object.

Parameters:
    

  * **markdown** â the markdown to display

  * **name** â the name of the property




media_player(_name_ , _url_ , _** kwargs_)#
    

Defines a media player object.

Parameters:
    

  * **name** â the name of the property

  * **url** â the URL of the media to display

  * **on_start** (_None_) â the operator to execute when the media starts

  * **on_play** (_None_) â the operator to execute when the media is played

  * **on_pause** (_None_) â the operator to execute when the media is paused

  * **on_buffer** (_None_) â the operator to execute when the media is buffering

  * **on_buffer_end** (_None_) â the operator to execute when the media stops buffering

  * **on_ended** (_None_) â the operator to execute when the media ends

  * **on_error** (_None_) â the operator to execute when the media errors

  * **on_duration** (_None_) â the operator to execute when the media duration is loaded

  * **on_seek** (_None_) â the operator to execute when the media is seeked

  * **on_progress** (_None_) â the operator to execute when the media progresses



Returns:
    

a `Object`

menu(_name_ , _** kwargs_)#
    

Defined an `Object` property that is displayed as a menu.

Note

Can be used for an `Button` type with properties whose views are one of `Button`, `Dropdown`, `DropdownView`, and :class;`Choices`. The variant and color of the items can be set using the variant and color parameters.

Parameters:
    

  * **name** â the name of the property

  * **variant** (_None_) â the variant for the items of the menu. Can be `"contained"`, `"outlined"`, `"round"` or `"square"`

  * **color** (_None_) â the color for the items of the menu.

  * **overlay** (_None_) â whether to display the menu as an overlay. Can be `"top-left"`,

  * **"top-center"**

  * **"top-right"**

  * **"bottom-left"**

  * **"bottom-center"`**

  * **or**

  * **of** (_"bottom-right". Overlay is useful when you want to display a floating menu on top_)

  * **content** (_another_)

  * **icon** (_None_) â when set, the icon will be displayed as the menu button instead of the label.

  * **"SettingsIcon"** (_Can be_)

  * **"MoreVertIcon".**



Returns:
    

a `Object`

message(_name_ , _label_ , _** kwargs_)#
    

Defines a message to display to the user as a `Notice`.

Parameters:
    

  * **name** â the name of the property

  * **label** â the label of the notice

  * **description** (_None_) â the description of the notice

  * **view** (_None_) â the `View` of the notice



Returns:
    

a `Property`

obj(_name_ , _** kwargs_)#
    

Defines a property on the object that is an object.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

oneof(_name_ , _types_ , _** kwargs_)#
    

Defines a one-of property on the object.

Parameters:
    

  * **name** â the name of the property

  * **types** â list of types that are instances of `BaseType`



Returns:
    

a `OneOf`

plot(_name_ , _** kwargs_)#
    

Defines an object property displayed as a plot.

Parameters:
    

  * **name** â the name of the property

  * **config** (_None_) â the chart config

  * **layout** (_None_) â the chart layout




See `PlotlyView` for more information.

str(_name_ , _allow_empty =False_, _** kwargs_)#
    

Defines a property on the object that is a string.

Parameters:
    

  * **name** â the name of the property

  * **label** (_None_) â the label of the property

  * **description** (_None_) â the description of the property

  * **view** (_None_) â the `View` of the property



Returns:
    

a `Property`

target_view(_ctx_ , _name ='view_target'_, _view_type =None_, _action_description ='Process'_, _default_target =None_, _allow_selected_samples =True_, _allow_selected_labels =False_, _allow_dataset_view =False_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _** kwargs_)#
    

Defines a view target input property.

This property has an enum input that allows the user to select which view to process. The available choices depend on the current context and the provided flags.

The choices include:

  * Entire dataset (if the current view is not a generated view)

  * Base view (if the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), which is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

  * Dataset view (if `allow_dataset_view` is `True`)

  * Current view (if the current view is different from the dataset view)

  * Selected samples (if `allow_selected_samples` is `True` and there are selected samples)

  * Selected labels (if `allow_selected_labels` is `True` and there are selected labels)




If thereâs no view or selected items, the only option is entire dataset, so the view target selector is hidden and âDATASETâ will be returned.

The resolved target view can be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

The target view descriptions are generated based on the provided `action_description` and the various description parameters. If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

Examples:
    
    
    import fiftyone.operators as foo
    
    class MyTargetViewOperator(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="target_view_operator",
                label="Testing Target View Operator",
                dynamic=True,
            )
    
        def resolve_input(self, ctx):
            inputs = types.Object()
    
            view_target_prop = inputs.view_target(ctx)
    
            return types.Property(
                inputs, view=types.View(label="Target View Operator")
            )
    
        def execute(self, ctx):
            target_view = ctx.target_view()
            # Do something with the target view
            print("Sample collection size", len(target_view))
    
    Args:
        ctx: the operator's :class:`fiftyone.operators.ExecutionContext`
        name(view_target): the name of the view target property
        view_type (RadioGroup): the view type to use (RadioGroup, Dropdown,
            etc.)
        default_target (None): the default target view to select if
            multiple choices are available. If ``None`` or
            ``default_target`` is not an available choice, the most
            targeted / selective available choice is chosen.
        action_description (Process): a short description of the action
            being performed, used to generate default descriptions for the
            various target views
        allow_selected_samples (True): whether to allow the "selected
            samples" target view
        allow_selected_labels (False): whether to allow the "selected
            labels" target view
        allow_dataset_view (False): whether to allow the "dataset view"
            target view
        base_view_label (Base view): the label for the "base view" target
            view
        base_view_description (None): the description for the "base view"
            target view. If ``None``, a default description is generated
        current_view_label (Current view): the label for the "current
            view" target view
        current_view_description (None): the description for the "current
            view" target view. If ``None``, a default description is
            generated
        dataset_label (Entire dataset): the label for the "entire dataset"
            target view
        dataset_description (None): the description for the "entire
            dataset" target view. If ``None``, a default description is
            generated
        dataset_view_label (Dataset): the label for the "dataset view"
            target view
        dataset_view_description (None): the description for the "dataset
            view" target view. If ``None``, a default description is
            generated
        selected_samples_label (Selected samples): the label for the
            "selected samples" target view
        selected_samples_description (None): the description for the
            "selected samples" target view. If ``None``, a default
            description is generated
        selected_labels_label (Selected labels): the label for the
            "selected labels" target view
        selected_labels_description (None): the description for the
            "selected labels" target view. If ``None``, a default
            description is generated
    
    Returns:
        a :class:`ViewTargetProperty`
    

to_json()#
    

Converts the object definition to JSON.

Returns:
    

a JSON dict

tree(_name_ , _** kwargs_)#
    

Defines a tree property on the object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Tree`

tuple(_name_ , _* items_, _** kwargs_)#
    

Defines a tuple property on the object.

Parameters:
    

  * **name** â the name of the property

  * ***items** â the types of the items in the tuple



Returns:
    

a `Tuple`

uploaded_file(_name_ , _** kwargs_)#
    

Defines a property on the object that is an uploaded file.

Parameters:
    

  * **name** â the name of the property

  * **view** (_None_) â the `View` of the property

  * **lite** (_False_) â whether to use the lite version of the file. When True, the content of the file in not included in resolve_input params, only the metadata is included.




v_stack(_name_ , _** kwargs_)#
    

Defines a vertical stack object.

Parameters:
    

**name** â the name of the property

Returns:
    

a `Object`

view(_name_ , _view_ , _** kwargs_)#
    

Defines a view-only property.

Examples:
    
    
    import fiftyone.operators.types as types
    
    notice = types.Notice(label="a label", description="a description")
    inputs = types.Object()
    inputs.view("notice", notice)
    

Parameters:
    

  * **name** â the name of the property

  * **view** â the `View` to define



Returns:
    

a `Property`

view_target(_ctx_ , _name ='view_target'_, _view_type =None_, _action_description ='Process'_, _default_target =None_, _allow_selected_samples =True_, _allow_selected_labels =False_, _allow_dataset_view =False_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _** kwargs_)#
    

Defines a view target input property.

This property has an enum input that allows the user to select which view to process. The available choices depend on the current context and the provided flags.

The choices include:

  * Entire dataset (if the current view is not a generated view)

  * Base view (if the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), which is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

  * Dataset view (if `allow_dataset_view` is `True`)

  * Current view (if the current view is different from the dataset view)

  * Selected samples (if `allow_selected_samples` is `True` and there are selected samples)

  * Selected labels (if `allow_selected_labels` is `True` and there are selected labels)




If thereâs no view or selected items, the only option is entire dataset, so the view target selector is hidden and âDATASETâ will be returned.

The resolved target view can be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

The target view descriptions are generated based on the provided `action_description` and the various description parameters. If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

Examples:
    
    
    import fiftyone.operators as foo
    
    class MyTargetViewOperator(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="target_view_operator",
                label="Testing Target View Operator",
                dynamic=True,
            )
    
        def resolve_input(self, ctx):
            inputs = types.Object()
    
            view_target_prop = inputs.view_target(ctx)
    
            return types.Property(
                inputs, view=types.View(label="Target View Operator")
            )
    
        def execute(self, ctx):
            target_view = ctx.target_view()
            # Do something with the target view
            print("Sample collection size", len(target_view))
    
    Args:
        ctx: the operator's :class:`fiftyone.operators.ExecutionContext`
        name(view_target): the name of the view target property
        view_type (RadioGroup): the view type to use (RadioGroup, Dropdown,
            etc.)
        default_target (None): the default target view to select if
            multiple choices are available. If ``None`` or
            ``default_target`` is not an available choice, the most
            targeted / selective available choice is chosen.
        action_description (Process): a short description of the action
            being performed, used to generate default descriptions for the
            various target views
        allow_selected_samples (True): whether to allow the "selected
            samples" target view
        allow_selected_labels (False): whether to allow the "selected
            labels" target view
        allow_dataset_view (False): whether to allow the "dataset view"
            target view
        base_view_label (Base view): the label for the "base view" target
            view
        base_view_description (None): the description for the "base view"
            target view. If ``None``, a default description is generated
        current_view_label (Current view): the label for the "current
            view" target view
        current_view_description (None): the description for the "current
            view" target view. If ``None``, a default description is
            generated
        dataset_label (Entire dataset): the label for the "entire dataset"
            target view
        dataset_description (None): the description for the "entire
            dataset" target view. If ``None``, a default description is
            generated
        dataset_view_label (Dataset): the label for the "dataset view"
            target view
        dataset_view_description (None): the description for the "dataset
            view" target view. If ``None``, a default description is
            generated
        selected_samples_label (Selected samples): the label for the
            "selected samples" target view
        selected_samples_description (None): the description for the
            "selected samples" target view. If ``None``, a default
            description is generated
        selected_labels_label (Selected labels): the label for the
            "selected labels" target view
        selected_labels_description (None): the description for the
            "selected labels" target view. If ``None``, a default
            description is generated
    
    Returns:
        a :class:`ViewTargetProperty`
    

class fiftyone.operators.types.View(_container =None_, _** kwargs_)#
    

Bases: `object`

Represents a view of a `Property`.

Views are used to define how properties are displayed in the FiftyOne App.

Parameters:
    

  * **label** (_None_) â a label for the view

  * **description** (_None_) â a description for the view

  * **caption** (_None_) â a caption for the view

  * **space** (_12_) â An int specifying how much vertical/horizontal space to allocate out of `12` depending on the orientation of the parent container

  * **placeholder** (_None_) â string to display placeholder text

  * **read_only** (_False_) â whether the view is read-only

  * **component** (_None_) â specifying custom component to use as the view

  * **componentsProps** (_None_) â dict for providing props to components rendered by a view

  * **container** (_None_) â the container (instance of `BaseType`) of the view




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.InferredView(_** kwargs_)#
    

Bases: `View`

Represents a view of a `Property` that is inferred from the data.

Note

You can only use inferred views for input properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Form(_live =False_, _submit_button_label ='Execute'_, _cancel_button_label ='Close'_, _** kwargs_)#
    

Bases: `View`

A form view.

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ReadOnlyView(_** kwargs_)#
    

Bases: `View`

A read-only `View`.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Choice(_value_ , _include =True_, _** kwargs_)#
    

Bases: `View`

Represents a choice in a `Choices` view.

Parameters:
    

  * **value** â the value of the choice

  * **label** (_None_) â a label for the `Choice`

  * **description** (_None_) â a description for the `Choice`

  * **caption** (_None_) â a caption for the `Choice`




**Methods:**

`clone`() | Clones the `Choice`.  
---|---  
`to_json`() |   
`kwargs_to_json`() |   
  
clone()#
    

Clones the `Choice`.

Returns:
    

a `Choice`

to_json()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.Choices(_** kwargs_)#
    

Bases: `View`

Represents a set of choices in a `View`.

Use this view to define a set of choices for a `Property` that can be selected by the user and require labels and optional descriptions.

Examples:
    
    
    import fiftyone.operators.types as types
    
    choices = types.Choices()
    choices.add_choice("cat", label="Cat", description="A cat")
    choices.add_choice("dog", label="Dog", description="A dog")
    
    inputs = types.Object()
    inputs.enum("animal", choices.values(), view=choices)
    

Parameters:
    

**choices** (_None_) â a list of `Choice` instances

**Attributes:**

`choices` |   
---|---  
  
**Methods:**

`values`() | Returns the choice values for this instance.  
---|---  
`add_choice`(value,Â **kwargs) | Adds a choice value to this instance.  
`append`(choice) | Appends a `Choice` to the list of choices.  
`clone`() |   
`to_json`() |   
`kwargs_to_json`() |   
  
property choices#
    

values()#
    

Returns the choice values for this instance.

Returns:
    

a list of values

add_choice(_value_ , _** kwargs_)#
    

Adds a choice value to this instance.

Parameters:
    

**value** â a choice value

Returns:
    

the `Choice` that was added

append(_choice_)#
    

Appends a `Choice` to the list of choices.

Parameters:
    

**choice** â a `Choice` instance

clone()#
    

to_json()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.RadioGroup(_** kwargs_)#
    

Bases: `Choices`

Represents a set of choices in a `View` that are displayed as a radio group.

Examples:
    
    
    import fiftyone.operators.types as types
    
    choices = types.RadioGroup()
    choices.add_choice("cat", label="Cat", description="A cat")
    choices.add_choice("dog", label="Dog", description="A dog")
    
    inputs = types.Object()
    inputs.enum("animal", choices.values(), view=choices)
    

Parameters:
    

  * **orientation** (_"horizontal"_) â the orientation of the radio group Can be `"horizontal"` or `"vertical"`

  * **label** (_None_) â a label for the radio group

  * **description** (_None_) â a description for the radio group

  * **caption** (_None_) â a caption for the radio group




**Methods:**

`to_json`() |   
---|---  
`add_choice`(value,Â **kwargs) | Adds a choice value to this instance.  
`append`(choice) | Appends a `Choice` to the list of choices.  
`clone`() |   
`kwargs_to_json`() |   
`values`() | Returns the choice values for this instance.  
  
**Attributes:**

`choices` |   
---|---  
  
to_json()#
    

add_choice(_value_ , _** kwargs_)#
    

Adds a choice value to this instance.

Parameters:
    

**value** â a choice value

Returns:
    

the `Choice` that was added

append(_choice_)#
    

Appends a `Choice` to the list of choices.

Parameters:
    

**choice** â a `Choice` instance

property choices#
    

clone()#
    

kwargs_to_json()#
    

values()#
    

Returns the choice values for this instance.

Returns:
    

a list of values

class fiftyone.operators.types.Dropdown(_** kwargs_)#
    

Bases: `Choices`

Represents a set of choices in a `View` that are displayed as a dropdown.

Examples:
    
    
    import fiftyone.operators.types as types
    
    choices = types.Dropdown()
    choices.add_choice("cat", label="Cat", description="A cat")
    choices.add_choice("dog", label="Dog", description="A dog")
    
    inputs = types.Object()
    inputs.enum("animal", choices.values(), view=choices)
    

Parameters:
    

  * **label** (_None_) â a label for the dropdown

  * **description** (_None_) â a description for the dropdown

  * **caption** (_None_) â a caption for the dropdown




**Methods:**

`add_choice`(value,Â **kwargs) | Adds a choice value to this instance.  
---|---  
`append`(choice) | Appends a `Choice` to the list of choices.  
`clone`() |   
`kwargs_to_json`() |   
`to_json`() |   
`values`() | Returns the choice values for this instance.  
  
**Attributes:**

`choices` |   
---|---  
  
add_choice(_value_ , _** kwargs_)#
    

Adds a choice value to this instance.

Parameters:
    

**value** â a choice value

Returns:
    

the `Choice` that was added

append(_choice_)#
    

Appends a `Choice` to the list of choices.

Parameters:
    

**choice** â a `Choice` instance

property choices#
    

clone()#
    

kwargs_to_json()#
    

to_json()#
    

values()#
    

Returns the choice values for this instance.

Returns:
    

a list of values

class fiftyone.operators.types.Notice(_** kwargs_)#
    

Bases: `View`

Represents a notice in a `View`.

You can use this view to display notices to the user.

Examples:
    
    
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    inputs.notice("This is a notice")
    

Parameters:
    

  * **label** (_None_) â a label for the notice

  * **description** (_None_) â a description for the notice

  * **caption** (_None_) â a caption for the notice




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Header(_** kwargs_)#
    

Bases: `View`

Represents a header in a `View`.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Warning(_** kwargs_)#
    

Bases: `View`

Represents a warning in a `View`.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Error(_** kwargs_)#
    

Bases: `View`

Represents an error in a `View`.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Button(_** kwargs_)#
    

Bases: `View`

Represents a button in a `View`.

Examples:
    
    
    import fiftyone.operators.types as types
    
    button = types.Button(
        label="Click me",
        operator="print_stdout",
        params={"msg": "Hello World"},
    )
    
    inputs = types.Object()
    inputs.view("btn", button)
    

Parameters:
    

  * **label** (_None_) â a label for the button

  * **description** (_None_) â a description for the button

  * **caption** (_None_) â a caption for the button

  * **operator** (_None_) â the name of the operator to execute when the button is clicked

  * **params** (_None_) â the parameters to pass to the operator

  * **href** (_None_) â the URL to navigate to when the button is clicked




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.OperatorExecutionButtonView(_** kwargs_)#
    

Bases: `Button`

Represents an operator execution button in a `View`.

Examples:
    
    
    import fiftyone.operators.types as types
    
    exec_button = types.OperatorExecutionButtonView(
        label="Execute Simple Op",
        variant="contained",
        operator="@voxel51/panel-examples/simple_op",
        on_success=self.on_success,
        on_error=self.on_error,
        on_option_selected=self.on_select,
        params={"msg": "Hello World!"},
    )
    
    inputs = types.Object()
    inputs.view("operator_btn", view=exec_button)
    

Parameters:
    

  * **icon** â an icon for the button. Defaults to âexpand_moreâ if not provided.

  * **label** â a label for the button.

  * **variant** â the variant of the button. Can be âcontainedâ or âoutlinedâ.

  * **description** â a description for the button.

  * **title** â a tooltip title for the button.

  * **operator** â the URI of the operator to execute when the button is clicked.

  * **on_success** â the URI of the operator to execute when the operator execution is successful.

  * **on_error** â the URI of the operator to execute when the operator execution fails.

  * **on_option_selected** â the URI of the operator to execute when an option is selected.

  * **params** â the parameters dict to pass to the operator.

  * **disabled** â whether the button is disabled.




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.OneOfView(_** kwargs_)#
    

Bases: `View`

Displays one of the given `View` instances.

Examples:
    
    
    import fiftyone.operators.types as types
    
    choices = types.RadioGroup()
    choices.add_choice("cat", label="Cat", description="A cat")
    choices.add_choice("dog", label="Dog", description="A dog")
    view = types.OneOfView(
        oneof=[types.Enum(choices.values()), types.String()]
    )
    
    inputs = types.Object()
    inputs.define_property(types.OneOfView(oneof=[choices]), view=view)
    

Parameters:
    

**oneof** (_None_) â a list of `View` instances

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ListView(_** kwargs_)#
    

Bases: `View`

Displays a list of `View` instances.

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.TupleView(_* itemsView_, _** options_)#
    

Bases: `View`

Displays a tuple of `View` instances.

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.TreeSelectionView(_** options_)#
    

Bases: `View`

Displays a tree selection checkbox groups.

Examples:
    
    
    import fiftyone.operators.types as types
    
    structure = [
        ["group_id_1", ["sample_id_1", "sample_id_2"]],
        ["group_id_2", ["sample_id_3", "sample_id_4", "sample_id_5"], ["group_id_8", ["sample_id_6"]]],
    ]
    
    tree_view = types.TreeSelectionView(
        data=structure # this data represents the basic group structure;
    )
    
    panel.view('exact_duplicate_selections', view=tree_view, on_change=self.toggle_select)
    
    def toggle_select(self, ctx):
        selected = ctx.params['value']
        print('selected samples:', selected)
    

Parameters:
    

  * **data** (_None_) â a list of lists representing the tree structure of groups and its children

  * **on_change** (_None_) â the operator to execute when the tree selection changes




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.CodeView(_** kwargs_)#
    

Bases: `View`

Displays a code editor.

Examples:
    
    
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    inputs.str("src", types.CodeView(language="python"))
    

Parameters:
    

**language** (_None_) â the language to use for syntax highlighting

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ColorView(_** kwargs_)#
    

Bases: `View`

Displays a color picker.

Parameters:
    

  * **compact** (_None_) â whether to display the color picker in compact mode

  * **variant** (_None_) â the variant of the color picker. See <https://casesandberg.github.io/react-color>




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.TabsView(_** kwargs_)#
    

Bases: `Choices`

Displays a tabbed view.

Parameters:
    

**variant** (_None_) â the variant of the tabs. See <https://material-ui.com/components/tabs>

**Methods:**

`to_json`() |   
---|---  
`add_choice`(value,Â **kwargs) | Adds a choice value to this instance.  
`append`(choice) | Appends a `Choice` to the list of choices.  
`clone`() |   
`kwargs_to_json`() |   
`values`() | Returns the choice values for this instance.  
  
**Attributes:**

`choices` |   
---|---  
  
to_json()#
    

add_choice(_value_ , _** kwargs_)#
    

Adds a choice value to this instance.

Parameters:
    

**value** â a choice value

Returns:
    

the `Choice` that was added

append(_choice_)#
    

Appends a `Choice` to the list of choices.

Parameters:
    

**choice** â a `Choice` instance

property choices#
    

clone()#
    

kwargs_to_json()#
    

values()#
    

Returns the choice values for this instance.

Returns:
    

a list of values

class fiftyone.operators.types.JSONView(_** kwargs_)#
    

Bases: `View`

Displays a JSON viewer.

Examples:
    
    
    # Show an object/dictionary in a JSON viewer
    outputs.obj("my_property", label="My Object", view=types.JSONView())
    

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.AutocompleteView(_** kwargs_)#
    

Bases: `Choices`

Displays an autocomplete input.

Note

This view can be used in place of `Choices`.

Parameters:
    

  * **choices** (_None_) â a list of `Choice` instances

  * **read_only** (_False_) â whether the view is read-only

  * **allow_user_input** (_True_) â when True the user can input a value that is not in the choices

  * **allow_duplicates** (_True_) â when True the user can select the same choice multiple times




**Methods:**

`add_choice`(value,Â **kwargs) | Adds a choice value to this instance.  
---|---  
`append`(choice) | Appends a `Choice` to the list of choices.  
`clone`() |   
`kwargs_to_json`() |   
`to_json`() |   
`values`() | Returns the choice values for this instance.  
  
**Attributes:**

`choices` |   
---|---  
  
add_choice(_value_ , _** kwargs_)#
    

Adds a choice value to this instance.

Parameters:
    

**value** â a choice value

Returns:
    

the `Choice` that was added

append(_choice_)#
    

Appends a `Choice` to the list of choices.

Parameters:
    

**choice** â a `Choice` instance

property choices#
    

clone()#
    

kwargs_to_json()#
    

to_json()#
    

values()#
    

Returns the choice values for this instance.

Returns:
    

a list of values

class fiftyone.operators.types.FileView(_** kwargs_)#
    

Bases: `View`

Displays a file input.

Note

This view can be used on `String` or `UploadedFile` properties. If used on a `String` property, the value will be the base64-encoded contents. If used on a `UploadedFile`, the value will be a `UploadedFile` object.

Parameters:
    

  * **max_size** (_None_) â a maximum allowed size of the file, in bytes

  * **max_size_error_message** (_None_) â an error message to display if the file exceeds the max size

  * **types** (_None_) â a string containing the comma-separated file types to accept

  * **lite** (_False_) â whether to use the lite version of the file. When True, the content of the file in not included, only the metadata is included in resolve_input params. Must be used in conjunction with a property of type `UploadedFile` .




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.LinkView(_** kwargs_)#
    

Bases: `View`

Displays a hyperlink.

Parameters:
    

**href** (_None_) â the URL to link to. Defaults to the property `value.href`

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.HiddenView(_** kwargs_)#
    

Bases: `View`

Allows properties to be hidden from the user.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.LoadingView(_** kwargs_)#
    

Bases: `ReadOnlyView`

Displays a loading indicator.

Parameters:
    

  * **text** (_"Loading"_) â a label for the loading indicator

  * **variant** (_"spinner"_) â the variant of the loading indicator

  * **color** (_"primary"_) â the color of the loading indicator

  * **size** (_"medium"_) â the size of the loading indicator




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.LoaderView(_operator_ , _params =None_, _label =None_, _placeholder_view =None_, _dependencies =None_, _** kwargs_)#
    

Bases: `View`

A view that loads data asynchronously via an operator.

The view executes the specified operator and stores the result. The loader property value always has the following structure:
    
    
    {
        "state": "idle" | "loading" | "loaded" | "errored",
        "data": <type>,  # shaped by the type argument passed to loader()
        "error": <str>   # error message (when state is "errored")
    }
    

The `type` argument passed to `Object.loader()` defines the shape of the `data` field, not the entire loader value.

By default, the loader executes only once when the component mounts. Use the `dependencies` argument to specify which param paths should trigger a reload when their values change.

Parameters:
    

  * **operator** â the operator to execute (string URI or callable method)

  * **params** (_None_) â parameters to pass to the operator

  * **label** (_None_) â loading message to display

  * **placeholder_view** (_None_) â view to render while loading

  * **dependencies** (_None_) â list of param paths (dot-notation supported) that should trigger a reload when changed. If None, the loader only executes once on mount




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.PillBadgeView(_** kwargs_)#
    

Bases: `View`

Displays a pill shaped badge.

Parameters:
    

  * **text** (_"Reviewed"__|__[__"Reviewed"__,__"Not Reviewed"__]__|__[__[__"Not Started"__,__"primary"__]__,__[__"Reviewed"__,__"success"__]__,__[__"In Review"__,__"warning"__]_) â a label or set of label options with or without a color for the pill badge

  * **color** (_"primary"_) â the color of the pill

  * **variant** (_"outlined"_) â the variant of the pill

  * **show_icon** (_False_ _|__True_) â whether to display indicator icon




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.PlotlyView(_** kwargs_)#
    

Bases: `View`

Displays a Plotly chart.

Note

See [plotly/react-plotly.js](https://github.com/plotly/react-plotly.js/#basic-props) for documentation.

All event handlers have the following default params:

  * `id`: the corresponding data.ids[idx]

  * `path`: the path of the property

  * `relative_path`: the relative path of the property

  * `schema`: the schema of the property

  * `view`: the value of the PlotlyView

  * `event`: the event name (eg. onClick, onSelected, onDoubleClick)

  * `value`: the value of the clicked point (only pie chart-like plots)

  * `label`: the label of the clicked point (only pie chart-like plots)

  * `shift_pressed`: whether the shift key was pressed




Examples:
    
    
    def render(self, ctx):
        panel.plot("my_plot", on_click=self.on_click, on_selected=self.on_selected)
    
    def print_params(self, ctx, params):
        for key, value in params.items():
            ctx.print(f"{key}: {value}")
    
    def on_click(self, ctx):
        # available params
        self.print_prams(ctx, {
            "id": "id", # the corresponding data.ids[idx]
            "idx": 1, # the index of the clicked point
            "label": "label", # label (eg. on pie charts)
            "shift_pressed": false, # whether the shift key was pressed
            "trace": "my_trace", # data[trace_idx].name
            "trace_idx": 0,
            "value": "my_value", # data[trace_idx].values[idx] (eg. on a pie chart)
            "x": 2, # data[trace_idx].x[idx] (the x value on most plot types)
            "y": 3, # data[trace_idx].y[idx] (the y value on most plot types)
            "z": 4, # data[trace_idx].z[idx] (the z value on 3d plots eg. heatmap)
        })
    
    def on_selected(self, ctx):
        prin(ctx.params['data'])
        # [
        #     {
        #       "trace": "trace 0", # data[trace_idx].name
        #       "trace_idx": 0, # the index of the trace
        #       "idx": 1, # the index of the selected point
        #       "id": "one", # the corresponding data.ids[idx]
        #       "x": 2, # the x value of the selected point
        #       "y": 15, # the y value of the selected point
        #       "z": 22 # the z value of the selected point
        #     }
        # ]
    

Parameters:
    

  * **data** (_None_) â the chart data

  * **config** (_None_) â the chart config

  * **layout** (_None_) â the chart layout

  * **on_click** (_None_) â event handler for click events

  * **on_selected** (_None_) â event handler for selected events

  * **on_double_click** (_None_) â event handler for double click events




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.Placement(_place_ , _view =None_)#
    

Bases: `object`

Represents the placement of an operator in the FiftyOne App.

Parameters:
    

  * **place** â the `Places` value

  * **view** (_None_) â a `View` to render




**Methods:**

`to_json`() |   
---|---  
  
to_json()#
    

class fiftyone.operators.types.Places(_value_)#
    

Bases: `Enum`

The places available to operators in the FiftyOne App.

**Attributes:**

`SAMPLES_GRID_ACTIONS` |   
---|---  
`SAMPLES_GRID_SECONDARY_ACTIONS` |   
`SAMPLES_VIEWER_ACTIONS` |   
`EMBEDDINGS_ACTIONS` |   
`HISTOGRAM_ACTIONS` |   
`MAP_ACTIONS` |   
`MAP_SECONDARY_ACTIONS` |   
`DISPLAY_OPTIONS` |   
`HEADER_ACTIONS` |   
  
**Methods:**

`to_json`() |   
---|---  
  
SAMPLES_GRID_ACTIONS = 'samples-grid-actions'#
    

SAMPLES_GRID_SECONDARY_ACTIONS = 'samples-grid-secondary-actions'#
    

SAMPLES_VIEWER_ACTIONS = 'samples-viewer-actions'#
    

EMBEDDINGS_ACTIONS = 'embeddings-actions'#
    

HISTOGRAM_ACTIONS = 'histograms-actions'#
    

MAP_ACTIONS = 'map-actions'#
    

MAP_SECONDARY_ACTIONS = 'map-secondary-actions'#
    

DISPLAY_OPTIONS = 'display-options'#
    

HEADER_ACTIONS = 'header-actions'#
    

to_json()#
    

class fiftyone.operators.types.KeyValueView(_** kwargs_)#
    

Bases: `View`

Displays a key-value editor.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Column(_key_ , _** kwargs_)#
    

Bases: `View`

A column in a `TableView`.

Parameters:
    

**key** â the name of the property to use for data

**Methods:**

`clone`() |   
---|---  
`to_json`() |   
`kwargs_to_json`() |   
  
clone()#
    

to_json()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.Action(_name_ , _** kwargs_)#
    

Bases: `View`

An action (currently supported only in a `TableView`).

Parameters:
    

  * **name** â the name of the action

  * **label** (_None_) â the label of the action

  * **icon** (_None_) â the icon of the action

  * **tooltip** (_None_) â the tooltip of the action

  * **on_click** â the operator to execute when the action is clicked




**Methods:**

`clone`() |   
---|---  
`to_json`() |   
`kwargs_to_json`() |   
  
clone()#
    

to_json()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.Tooltip(_row_ , _column_ , _** kwargs_)#
    

Bases: `View`

A tooltip (currently supported only in a `TableView`).

Parameters:
    

  * **value** â the value of the tooltip

  * **row** â the row of the tooltip

  * **column** â the column of the tooltip




**Methods:**

`clone`() |   
---|---  
`to_json`() |   
`kwargs_to_json`() |   
  
clone()#
    

to_json()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.TableView(_** kwargs_)#
    

Bases: `View`

Displays a table.

Parameters:
    

  * **columns** (_None_) â a list of `Column` objects to display

  * **row_actions** (_None_) â a list of `Action` objects to display




**Methods:**

`keys`() |   
---|---  
`add_column`(key,Â **kwargs) |   
`add_row_action`(name,Â on_click[,Â label,Â ...]) |   
`add_tooltip`(row,Â column,Â value,Â **kwargs) |   
`clone`() |   
`to_json`() |   
`kwargs_to_json`() |   
  
keys()#
    

add_column(_key_ , _** kwargs_)#
    

add_row_action(_name_ , _on_click_ , _label =None_, _icon =None_, _tooltip =None_, _** kwargs_)#
    

add_tooltip(_row_ , _column_ , _value_ , _** kwargs_)#
    

clone()#
    

to_json()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.MapView(_** kwargs_)#
    

Bases: `View`

Displays a key-value mapping.

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ProgressView(_** kwargs_)#
    

Bases: `View`

Displays a progress bar.

Examples:
    
    
    import fiftyone.operators as foo
    import fiftyone.operators.types as types
    
    class ExampleProgress(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="example_progress",
                label="Examples: Progress",
                execute_as_generator=True,
            )
    
        async def execute(self, ctx):
            outputs = types.Object()
            schema = types.Property(outputs)
            n = 100
            for i in range(n):
                label = f"Loading {i} of {n}"
                progress_view = types.ProgressView(label=label)
                loading_schema = types.Object()
                loading_schema.int("percent_complete", view=progress_view)
                show_output_params = {
                    "outputs": types.Property(loading_schema).to_json(),
                    "results": {"percent_complete": i / n}
                }
                yield ctx.trigger("show_output", show_output_params)
    
                # Simulate computation
                await asyncio.sleep(0.5)
    

Parameters:
    

  * **label** (_None_) â the label to display under the progress bar

  * **variant** (_None_) â bar variant. Supported values are `"linear"` and `"circular"`




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ImageView(_** kwargs_)#
    

Bases: `View`

Displays an image.

Examples:
    
    
    def execute():
        return {"image": "https://voxel51.com/your/image.png"}
    
    def resolve_output(self, ctx):
        schema = {
            "height": "100px",
            "width": "100px",
            "alt": "My image alt text",
            "href": "https://voxel51.com",
            "operator": "@my/plugin/my_operator" | self.my_operator (in Python Panels),
            "prompt": False,
            "params": {"foo": "bar"},
        }
        outputs = types.Object()
        outputs.define_property(
            "image",
            types.String(),
            label="Image",
            view=types.ImageView(),
        )
        return types.Property(outputs)
    

Parameters:
    

  * **height** (_None_) â the height of the image

  * **width** (_None_) â the width of the image

  * **alt** (_None_) â the alt text of the image

  * **href** (_None_) â the url to navigate to when the image is clicked

  * **operator** (_None_) â the name of the callable operator to execute when the image is clicked

  * **prompt** (_False_) â whether to prompt the user before executing the operator

  * **params** (_None_) â the parameters to pass to the operator




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.AlertView(_** kwargs_)#
    

Bases: `View`

Displays an alert.

Parameters:
    

  * **severity** (_None_) â the severity of the alert displayed, one of `("info", "success", "warning", "error")`

  * **componentsProps** (_None_) â 

an optional dict with the following keys:

    * `'label'` (None): props to pass to the label subcomponents

    * `'description'` (None): props to pass to the description subcomponents

    * `'caption'` (None): props to pass to the caption subcomponents




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ToastView(_** kwargs_)#
    

Bases: `View`

Displays a snackbar style toast element.

Examples:

schema = {
    

> âmessageâ: âTestâ, âdurationâ: 30000, âlayoutâ: {
>
>> âverticalâ: âtopâ, âhorizontalâ: âcenterâ, âtopâ: â200pxâ
> 
> },

} snackbar = types.ToastView(**schema) panel.obj(âtoastâ, view=snackbar)

Parameters:
    

  * **message** â the message to display

  * **duration** (_None_) â the duration to stay on screen in milliseconds

  * **layout** (_None_) â the layout of the toast




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.CheckboxView(_** kwargs_)#
    

Bases: `View`

Displays a checkbox.

Examples:
    
    
    inputs.bool(
        "my_property_name",
        default=True,
        label="My Checkbox",
        description="A checkbox description.",
        view=types.CheckboxView(),
    )
    

Note

Must be used with `Boolean` properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.ErrorView(_** kwargs_)#
    

Bases: `View`

Displays an error.

Parameters:
    

  * **detailed** (_False_) â whether to display a detailed error message

  * **popout** (_None_) â if provided, displays a popout button with the given dictionary of props

  * **left** (_False_) â whether to display on the left side of the popout button




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.HeaderView(_** kwargs_)#
    

Bases: `View`

Displays a header component.

Headers can have a `label`, `description`, and `caption`, each of which are displayed in a separate line.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.ObjectView(_** kwargs_)#
    

Bases: `View`

Displays an object component.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.RadioView(_** kwargs_)#
    

Bases: `RadioGroup`

Displays a radio component for the given `RadioGroup` instance.

**Methods:**

`add_choice`(value,Â **kwargs) | Adds a choice value to this instance.  
---|---  
`append`(choice) | Appends a `Choice` to the list of choices.  
`clone`() |   
`kwargs_to_json`() |   
`to_json`() |   
`values`() | Returns the choice values for this instance.  
  
**Attributes:**

`choices` |   
---|---  
  
add_choice(_value_ , _** kwargs_)#
    

Adds a choice value to this instance.

Parameters:
    

**value** â a choice value

Returns:
    

the `Choice` that was added

append(_choice_)#
    

Appends a `Choice` to the list of choices.

Parameters:
    

**choice** â a `Choice` instance

property choices#
    

clone()#
    

kwargs_to_json()#
    

to_json()#
    

values()#
    

Returns the choice values for this instance.

Returns:
    

a list of values

class fiftyone.operators.types.SwitchView(_** kwargs_)#
    

Bases: `View`

Displays a toggle switch.

Note

Must be used with `Boolean` properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.TextView(_** kwargs_)#
    

Bases: `View`

Displays a text. .. note:
    
    
    Must be used with :class:`String` properties.
    

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.TextFieldView(_multiline =False_, _rows =None_, _** kwargs_)#
    

Bases: `View`

Displays a text input.

Note

Must be used with `String` or `Number` properties.

Parameters:
    

  * **multiline** (_False_) â whether to render a multiline text area

  * **rows** (_None_) â optional number of visible text rows when `multiline` is enabled




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.FieldView(_** kwargs_)#
    

Bases: `View`

Displays a text input.

Note

Must be used with `String` or `Number` properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.LazyFieldView(_** kwargs_)#
    

Bases: `View`

Displays a lazy text input which only apply input field changes on blur or when user clicks the save button within the field.

Note

Must be used with `String` or `Number` properties.

Parameters:
    

**save_on_blur** (_True_) â when set to False, changes in input field will not be automatically applied when user moves mouse out of the changed field. To apply changes, user must click the save button.

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.DropdownView(_** kwargs_)#
    

Bases: `Dropdown`

Displays a dropdown selector input.

**Methods:**

`add_choice`(value,Â **kwargs) | Adds a choice value to this instance.  
---|---  
`append`(choice) | Appends a `Choice` to the list of choices.  
`clone`() |   
`kwargs_to_json`() |   
`to_json`() |   
`values`() | Returns the choice values for this instance.  
  
**Attributes:**

`choices` |   
---|---  
  
add_choice(_value_ , _** kwargs_)#
    

Adds a choice value to this instance.

Parameters:
    

**value** â a choice value

Returns:
    

the `Choice` that was added

append(_choice_)#
    

Appends a `Choice` to the list of choices.

Parameters:
    

**choice** â a `Choice` instance

property choices#
    

clone()#
    

kwargs_to_json()#
    

to_json()#
    

values()#
    

Returns the choice values for this instance.

Returns:
    

a list of values

class fiftyone.operators.types.DateTimeView(_** kwargs_)#
    

Bases: `View`

Displays a date/time input - response in epoch time

Examples::
    

start_datetime_selector = types.DateTimeView(date_only=True) inputs.int(

> âstart_datetimeâ, required=True, label=âStart Date/timeâ, description=âStart date/timeâ¦â, view=start_datetime_selector,

)

end_datetime_selector = types.DateTimeView() inputs.int(

> âend_datetimeâ, required=False, label=âEnd Date/timeâ, description=âEnd date/timeâ¦â, view=end_datetime_selector,

)

â¦

start_datetime = ctx.params.get(âstart_datetimeâ, None) end_datetime = ctx.params.get(âend_datetimeâ, None)

if start_datetime:
    

start = fou.timestamp_to_datetime(start_datetime) print(fâstart: {start}â)

if end_datetime:
    

end = fou.timestamp_to_datetime(end_datetime) print(fâend: {end}â)

Parameters:
    

**date_only** (_False_) â whether to display a date only input and not require HH:MM:SS

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.LabelValueView(_** kwargs_)#
    

Bases: `View`

Displays a label-value component. Used for displaying a label and a corresponding value.

Note

Must be used with `String`, `Number`, or `Boolean` properties, or lists of such properties. Also this view is not supported for input properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.PrimitiveView(_** kwargs_)#
    

Bases: `View`

Displays a primitive value component.

Note

Must be used with `String`, `Number`, or `Boolean` properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.SliderView(_** kwargs_)#
    

Bases: `View`

Displays a slider component.

Note

This view must be used with `Number` properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.TagsView(_** kwargs_)#
    

Bases: `View`

Displays a list of tags component.

Note

Must be used with `List` properties whose items are `String`, `Number:, or :class:`Boolean` instances

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Success(_** kwargs_)#
    

Bases: `View`

Represents a success in a `View`.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.ButtonView(_** kwargs_)#
    

Bases: `Button`

Represents a button in a `Button`.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.MarkdownView(_** kwargs_)#
    

Bases: `View`

Renders a markdown string as HTML.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.StatusButtonView(_** kwargs_)#
    

Bases: `View`

Renders a status button.

Parameters:
    

  * **severity** (_None_) â the severity of the alert displayed, one of `("info", "success", "warning", "error", "enabled", "disabled")`

  * **on_click** (_None_) â an operator to execute when the button is clicked

  * **params** (_None_) â the parameters to pass to the operator

  * **disabled** â whether the button is disabled

  * **title** â tooltip title for the button




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.MediaPlayerView(_** kwargs_)#
    

Bases: `View`

Renders a media player for audio and video files.

Parameters:
    

  * **name** â the name of the property

  * **url** â the URL of the media to display

  * **on_start** (_None_) â the operator to execute when the media starts

  * **on_play** (_None_) â the operator to execute when the media is played

  * **on_pause** (_None_) â the operator to execute when the media is paused

  * **on_buffer** (_None_) â the operator to execute when the media is buffering

  * **on_buffer_end** (_None_) â the operator to execute when the media stops buffering

  * **on_ended** (_None_) â the operator to execute when the media ends

  * **on_error** (_None_) â the operator to execute when the media errors

  * **on_duration** (_None_) â the operator to execute when the media duration is loaded

  * **on_seek** (_None_) â the operator to execute when the media is seeked

  * **on_progress** (_None_) â the operator to execute when the media progresses




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.FileExplorerView(_** kwargs_)#
    

Bases: `View`

Displays a file explorer for interacting with files.

Examples:
    
    
    import os
    import fiftyone.operators.types as types
    
    inputs = types.Object()
    
    # Create an explorer that allows the user to choose a directory
    file_explorer = types.FileExplorerView(
        choose_dir=True,
        button_label="Choose a directory...",
        choose_button_label="Accept"
    )
    
    # Define a types.File property
    file_prop = inputs.file(
        "directory",
        required=True,
        label="Directory",
        description="Choose a directory",
        view=file_explorer,
    )
    
    directory = ctx.params.get("directory", {}).get("absolute_path", None)
    

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.PromptView(_** kwargs_)#
    

Bases: `View`

Customizes how a prompt is rendered.

Examples:
    
    
    import fiftyone.operators.types as types
    
    # in resolve_input
    prompt = types.PromptView(
        label="This is the title",
        submit_button_label="Click me",
        cancel_button_label="Abort"
    )
    inputs = types.Object()
    inputs.md("Hello world!")
    return types.Property(inputs, view=prompt)
    

Parameters:
    

  * **label** (_None_) â the title for the prompt

  * **submit_button_label** (_None_) â the label for the submit button

  * **cancel_button_label** (_None_) â the label for the cancel button




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.ViewTargetOptions(_choices_view_ , _action_description ='Process'_, _include_base_view =False_, _include_current_view =False_, _include_dataset =True_, _include_dataset_view =False_, _include_selected_labels =False_, _include_selected_samples =False_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _** __)#
    

Bases: `object`

Represents the options for a `ViewTargetProperty`.

choices_view#
    

a `Choices` for the view target choices

**Methods:**

`values`() |   
---|---  
  
values()#
    

class fiftyone.operators.types.ViewTargetProperty(_ctx_ , _view_type =<class 'fiftyone.operators._types.types.RadioGroup'>_, _action_description ='Process'_, _allow_selected_samples =True_, _allow_selected_labels =False_, _allow_dataset_view =False_, _default_target =None_, _dataset_label ='Entire dataset'_, _dataset_description =None_, _base_view_label ='Base view'_, _base_view_description =None_, _current_view_label ='Current view'_, _current_view_description =None_, _dataset_view_label ='Dataset'_, _dataset_view_description =None_, _selected_samples_label ='Selected samples'_, _selected_samples_description =None_, _selected_labels_label ='Selected labels'_, _selected_labels_description =None_, _**kwargs_)#
    

Bases: `Property`

Property that displays a view target selector.

This property has an enum input that allows the user to select which view to process. The available choices depend on the current context and the provided flags.

The choices include:

  * Entire dataset (if the current view is not a generated view)

  * Base view (if the current view is a generated view such as [`fiftyone.core.clips.ClipsView`](api__fiftyone.core.clips.md#fiftyone.core.clips.ClipsView "fiftyone.core.clips.ClipsView"), [`fiftyone.core.video.FramesView`](api__fiftyone.core.video.md#fiftyone.core.video.FramesView "fiftyone.core.video.FramesView"), or [`fiftyone.core.patches.PatchesView`](api__fiftyone.core.patches.md#fiftyone.core.patches.PatchesView "fiftyone.core.patches.PatchesView")), which is the semantic equivalent of âentire datasetâ for these views. The base view is the view from which the generated view was created. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`

  * Dataset view (if `allow_dataset_view` is `True`)

  * Current view (if the current view is different from the dataset view)

  * Selected samples (if `allow_selected_samples` is `True` and there are selected samples)

  * Selected labels (if `allow_selected_labels` is `True` and there are selected labels)




If thereâs no view or selected items, the only option is entire dataset, so the view target selector is hidden and âDATASETâ will be returned.

The resolved target view can be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

The target view descriptions are generated based on the provided `action_description` and the various description parameters. If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

Examples:
    
    
    import fiftyone.operators as foo
    
    class MyTargetViewOperator(foo.Operator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="target_view_operator",
                label="Testing Target View Operator",
                dynamic=True,
            )
    
        def resolve_input(self, ctx):
            inputs = types.Object()
    
            view_target_prop = inputs.view_target(ctx)
    
            return types.Property(
                inputs, view=types.View(label="Target View Operator")
            )
    
        def execute(self, ctx):
            target_view = ctx.target_view()
            # Do something with the target view
            print("Sample collection size", len(target_view))
    

options#
    

a `ViewTargetOptions` instance

**Attributes:**

`options` |   
---|---  
  
**Methods:**

`to_json`() |   
---|---  
  
property options#
    

to_json()#
    

class fiftyone.operators.types.GridView(_** kwargs_)#
    

Bases: `View`

Displays properties of an object as a grid of components in horizontal or vertical orientation.

Note

Must be used with `Object` properties.

Parameters:
    

  * **orientation** (_"2d"_) â the orientation of the stack. Can be either `"2d"`, `"horizontal"` or `"vertical"`

  * **gap** (_1_) â the gap between the components

  * **align_x** (_"left"_) â the alignment of the components. Can be either `"left"`, `"center"`, or `"right"`

  * **align_y** (_"top"_) â the alignment of the components. Can be either `"top"`, `"center"`, or `"bottom"`

  * **variant** (_None_) â the variant of the grid. Can be either `"paper"` or `"outline"`

  * **elevation** (_None_) â the elevation of the grid. Only applicable when `variant="paper"`




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.DashboardView(_** kwargs_)#
    

Bases: `View`

Defines a Dashboard view.

Parameters:
    

  * **layout** (_None_) â the layout of the dashboard.

  * **on_save_layout** (_None_) â event triggered when the layout changes

  * **on_add_item** (_None_) â event triggered when an item is added

  * **on_remove_item** (_None_) â event triggered when an item is closed

  * **on_edit_item** (_None_) â event triggered when an item is edited

  * **allow_addition** (_True_) â whether to allow adding items

  * **allow_deletion** (_True_) â whether to allow deleting items

  * **allow_edit** (_True_) â whether to allow editing items

  * **cta_title** (_None_) â the title of the call to action

  * **cta_body** (_None_) â the body of the call to action

  * **cta_button_label** (_None_) â the label of the call to action button

  * **rows** (_None_) â the number of rows in the dashboard

  * **cols** (_None_) â the number of columns in the dashboard

  * **items** (_None_) â the custom layout of the dashboard

  * **auto_layout** (_True_) â whether to automatically layout the dashboard




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.DrawerView(_** kwargs_)#
    

Bases: `View`

Renders an operator prompt as a left or right side drawer.

Examples:
    
    
    import fiftyone.operators.types as types
    
    # in resolve_input
    inputs = types.Object()
    inputs.str("message", label="Message")
    prompt = types.DrawerView(placement="left")
    return types.Property(inputs, view=prompt)
    

Parameters:
    

**placement** (_None_) â 

the placement of the drawer. Can be one of the following

  * `'left'`: display to the left of the main or expanded view

  * `'right'`: display to the right of the main or expanded view




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.IconButtonView(_** kwargs_)#
    

Bases: `Button`

Represents a button in a `View`.

Examples:
    
    
    import fiftyone.operators.types as types
    
    iconButtonView = types.IconButtonView(
        icon="waving_hand",
        operator="print_stdout",
        params={"msg": "Hi!"},
    )
    
    inputs = types.Object()
    inputs.view("icon_btn", iconButtonView)
    

Parameters:
    

  * **icon** (_None_) â a icon for the button. See [marella/material-icons](https://github.com/marella/material-icons?tab=readme-ov-file#available-icons)

  * **variant** (_None_) â the optional variant of the icon button. Can be `"round"`, `"square"`, `"outlined"`, or `"contained"`.

  * **label** (_None_) â a label for the button

  * **description** (_None_) â a description for the button

  * **caption** (_None_) â a caption for the button

  * **operator** (_None_) â the name of the operator to execute when the button is clicked

  * **params** (_None_) â the parameters to pass to the operator

  * **href** (_None_) â the URL to navigate to when the button is clicked




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.ModalView(_** kwargs_)#
    

Bases: `Button`

Represents a button in a `View` that opens up an interactive modal.

Examples:
    
    
    import fiftyone.operators.types as types
    
    schema = {
        "modal": {"icon": "local_offer", "iconVariant": "outlined", "title": "Modal Title", "subtitle": "Modal Subtitle", "body": "Modal Body", textAlign: {title: "center", subtitle: "left", body: "right"}},
        "primaryButton": {"primaryText": "This is the primary button", "primaryColor": "primary", "params": {"foo": "bar", "multiple": True}},
        "secondaryButton": {"secondaryText": "This is the secondary button", "secondaryColor": "secondary"},
        "primaryCallback": self.do_something(),
        "secondaryCallback": self.do_nothing(),
        "functionality": "tagging",
    }
    modal = types.ModalView(**schema, label="This is a modal", variant="outlined", icon="local_offer")
    
    .. note::
        The primary callback is called when the primary button is clicked and the secondary callback is called when the secondary button is clicked.
        Secondary callback defaults to a closure of the modal unless defined.
        Buttons of ModalView inherit all functionality of ButtonView.
    
    inputs = types.Object()
    inputs.view("modal_btn", modal)
    

Parameters:
    

  * **modal** â the textual content of the modal

  * **primaryButton** (_None_) â the properties of the primary button

  * **secondaryButton** (_None_) â the properties of the secondary button

  * **primaryCallback** (_None_) â the function to execute when the primary button is clicked

  * **secondaryCallback** (_None_) â the function to execute when the secondary button is clicked

  * **functionality** (_None_) â the name of the functionality to execute when the primary button is clicked. Available options are âtaggingâ




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.HStackView(_orientation ='horizontal'_, _** kwargs_)#
    

Bases: `GridView`

Displays properties of an object as a horizontal stack of components.

Note

Must be used with `Object` properties.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.VStackView(_orientation ='vertical'_, _** kwargs_)#
    

Bases: `GridView`

Displays properties of an object as a vertical stack of components.

Note

Must be used with `Object` properties.

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ButtonGroupView(_orientation ='horizontal'_, _** kwargs_)#
    

Bases: `GridView`

Displays a group of buttons in a horizontal stack.

Note

Must be used with `Button` properties.

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.MenuView(_orientation ='horizontal'_, _** kwargs_)#
    

Bases: `GridView`

Displays a menu of options in a vertical stack.

Note

Can be used for an `Button` type with properties whose views are one of `Button`, `Dropdown`, `DropdownView`, and :class;`Choices`. The variant and color of the items can be set using the variant and color parameters.

Parameters:
    

  * **name** â the name of the property

  * **variant** (_None_) â the variant for the items of the menu. Can be `"contained"`, `"outlined"`, `"round"` or `"square"`

  * **color** (_None_) â the color for the items of the menu.

  * **overlay** (_None_) â whether to display the menu as an overlay. Can be `"top-left"`,

  * **"top-center"**

  * **"top-right"**

  * **"bottom-left"**

  * **"bottom-center"`**

  * **or**

  * **of** (_"bottom-right". Overlay is useful when you want to display a floating menu on top_)

  * **content** (_another_)

  * **icon** (_None_) â when set, the icon button will be displayed as the menu trigger,

  * **"MoreVertIcon"** (_instead_ _of_ _the selected value. Can be "SettingsIcon" or_)



Returns:
    

a `Object`

**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.ArrowNavView(_** kwargs_)#
    

Bases: `View`

Displays a floating navigation arrows.

Parameters:
    

  * **forward** (_True_) â Whether to display the forward arrow

  * **backward** (_True_) â Whether to display the backward arrow

  * **on_forward** (_None_) â The operator to execute when the forward arrow is clicked

  * **on_backward** (_None_) â The operator to execute when the backward arrow is clicked

  * **position** (_"center"_) â The position of the arrows. Can be either `"top"`, `center`, `"bottom"`, `"left"`, `middle` (center horizontally), or ``"right"`




**Methods:**

`to_json`() |   
---|---  
`clone`() |   
`kwargs_to_json`() |   
  
to_json()#
    

clone()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.FrameLoaderView(_** kwargs_)#
    

Bases: `View`

Utility for animating panel state based on the given timeline_name.

Examples:
    
    
    def on_load(self, ctx):
        panel.state.plot = {
            "type": "scatter",
            "x": [1, 2, 3],
            "y": [1, 2, 3],
        }
    
    def render(self, ctx):
        panel.obj(
            "frame_data",
            view=types.FrameLoaderView(
                on_load_range=self.on_load_range,
                target="plot.selectedpoints",
            ),
        )
        panel.plot("plot")
    
    def load_range(self, ctx, range_to_load):
        r = ctx.params.get("range")
    
        chunk = {}
        for i in range(r[0], r[1]):
            rendered_frame = [i]
            chunk[f"frame_data.frames[{i}]"] = rendered_frame
    
        ctx.panel.set_data(chunk)
        current_field = ctx.panel.state.selected_field or "default_field"
        ctx.panel.set_state("frame_data.signature", current_field + str(r))
    

Parameters:
    

  * **timeline_name** (_None_) â the name of the timeline to load if provided, otherwise the default timeline

  * **on_load_range** (_None_) â the operator to execute when the frame is loading

  * **target** â the path to the property to animate




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.TimelineView(_** kwargs_)#
    

Bases: `View`

Represents a timeline for playing animations.

Parameters:
    

  * **timeline_name** (_None_) â the name of the timeline

  * **total_frames** (_None_) â the total number of frames in the timeline

  * **loop** (_False_) â whether to loop the timeline




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.TimerView(_** kwargs_)#
    

Bases: `View`

Supports a timer for executing operators/events after a specified duration or interval.

Parameters:
    

  * **timeout** (_None_) â the duration in milliseconds to wait before executing the operator

  * **interval** (_None_) â the interval in milliseconds to wait before executing the operator

  * **on_timeout** (_None_) â the operator to execute when the timeout is reached

  * **on_interval** (_None_) â the operator to execute at the interval

  * **params** (_None_) â the params passed to the on_interval or on_timeout operator




**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.ComponentView(_name_ , _** kwargs_)#
    

Bases: `View`

Represents a custom component view.

Parameters:
    

**name** â the name of the component to render. This should correspond to a registered custom plugin component.

**Methods:**

`clone`() |   
---|---  
`kwargs_to_json`() |   
`to_json`() |   
  
clone()#
    

kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.Container(_** kwargs_)#
    

Bases: `BaseType`

Represents a base container for a container types.

**Methods:**

`kwargs_to_json`() |   
---|---  
`to_json`() |   
  
kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.PaperContainer(_elevation =1_, _rounded =True_, _** kwargs_)#
    

Bases: `Container`

Represents an elevated block for a view.

Parameters:
    

  * **elevation** (_1_) â the elevation of the container. Can be a value between 0 and 24

  * **rounded** (_True_) â whether to display the paper container with rounded corners




**Methods:**

`to_json`() |   
---|---  
`kwargs_to_json`() |   
  
to_json()#
    

kwargs_to_json()#
    

class fiftyone.operators.types.OutlinedContainer(_rounded =True_, _** kwargs_)#
    

Bases: `Container`

Represents an elevated block for a view.

Parameters:
    

**rounded** (_True_) â whether to display the outlined container with rounded corners

**Methods:**

`kwargs_to_json`() |   
---|---  
`to_json`() |   
  
kwargs_to_json()#
    

to_json()#
    

class fiftyone.operators.types.RiskLevel(_value_)#
    

Bases: `Enum`

Risk levels that operators can declare.

**Attributes:**

`LOW` |   
---|---  
`MEDIUM` |   
`HIGH` |   
`DANGEROUS` |   
  
LOW = 'low'#
    

MEDIUM = 'medium'#
    

HIGH = 'high'#
    

DANGEROUS = 'dangerous'#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
