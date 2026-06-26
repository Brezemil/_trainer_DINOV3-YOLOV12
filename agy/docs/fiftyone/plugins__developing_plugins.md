---
source_url: https://docs.voxel51.com/plugins/developing_plugins.html
---

# Developing Plugins#

This page describes how to write your own FiftyOne plugins.

Note

Check out the [Plugins Ecosystem](https://docs.voxel51.com/plugins/index.html#plugins-ecosystem) for a growing collection of plugins that you can use as examples when developing your own.

## Design overview#

Plugins are composed of one or more panels, operators, skills, and components.

Together these building blocks enable you to build full-featured interactive data applications that tailor FiftyOne to your specific use case and workflow. Whether youâre working with images, videos, or other data types, a plugin can help you streamline your machine learning workflows and co-develop your data and models.

![https://cdn.voxel51.com/develop_plugins/plugin-design.png](https://cdn.voxel51.com/develop_plugins/plugin-design.png)

### Plugin types#

FiftyOne plugins can be written in Python or JavaScript (JS), or a combination of both.

Python plugins are built using the `fiftyone` package, pip packages, and your own Python. They can consist of panels, operators, and skills.

JS plugins are built using the `@fiftyone` TypeScript packages, npm packages, and your own TypeScript. They can consist of panels, operators, skills, and custom components.

### Panels#

Panels are miniature full-featured data applications that you can open in [App spaces](user_guide__app.md#app-spaces) and interactively manipulate to explore your dataset and update/respond to updates from other spaces that are currently open in the App.

FiftyOne natively includes the following Panels:

  * [Samples panel](user_guide__app.md#app-samples-panel): the media grid that loads by default when you launch the App

  * [Histograms panel](user_guide__app.md#app-histograms-panel): a dashboard of histograms for the fields of your dataset

  * [Embeddings panel](user_guide__app.md#app-embeddings-panel): a canvas for working with [embeddings visualizations](brain.md#brain-embeddings-visualization)

  * [Map panel](user_guide__app.md#app-map-panel): visualizes the geolocation data of datasets that have a [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field


![../_images/app-map-panel.gif](../_images/app-map-panel.gif)

Note

Jump to this section for more information about developing panels.

### Operators#

Operators are user-facing operations that allow you to interact with the data in your dataset. They can range from simple actions like checking a checkbox to more complex workflows such as requesting annotation of samples from a configurable backend. Operators can even be composed of other operators or be used to add functionality to custom panels.

FiftyOne comes with a number of builtin [`Python`](plugins__api__plugins.operators.md#module-plugins.operators "plugins.operators") and [JavaScript](https://github.com/voxel51/fiftyone/blob/develop/app/packages/operators/src/built-in-operators.ts) operators for common tasks that are intended for either user-facing or internal plugin use.

![../_images/operator-browser.gif](../_images/operator-browser.gif)

Note

Jump to this section for more information about developing operators.

### Skills#

Skills are Markdown files that teach AI agents how to perform complex FiftyOne workflows using natural language. Each skill describes a task that an agent can be asked to perform, providing step-by-step guidance that the agent follows to complete the workflow autonomously.

Note

Jump to this section for more information about developing skills.

### Components#

Components are responsible for rendering and event handling in plugins. They provide the necessary functionality to display and interact with your plugin in the FiftyOne App. Components also implement form inputs and output rendering for operators, making it possible to customize the way an operator is rendered in the FiftyOne App.

For example, FiftyOne comes with a wide variety of [`builtin types`](api__fiftyone.operators.types.md#module-fiftyone.operators.types "fiftyone.operators.types") that you can leverage to build complex input and output forms for your operators.

![../_images/file-explorer.gif](../_images/file-explorer.gif)

Note

Jump to this section for more information about developing components.

## Development setup#

In order to develop Python plugins, you can use either a release or source install of FiftyOne:
    
    
    pip install fiftyone
    

In order to develop JS plugins, you will need a [source install](https://github.com/voxel51/fiftyone#installing-from-source) of FiftyOne and a vite config that links modules to your `fiftyone/app` directory.

Note

For JS plugins we recommend forking the [FiftyOne Hello World JS Example](https://github.com/voxel51/hello-world-plugin-js) repository and following the conventions there to build your JS plugin.

### Testing plugins locally#

Added in version 1.13.0.

The easiest way to test a plugin during development is the `fiftyone app debug` command, which launches the App with server logs printed directly to your shell:
    
    
    fiftyone app debug
    

You can also load a specific dataset immediately on launch:
    
    
    fiftyone app debug <name>
    

Note

Make sure your plugin is installed in your [plugins directory](plugins__using_plugins.md#plugins-directory) before launching. If you add or modify a plugin while the App is running, restart the debug session to pick up the changes.

## Anatomy of a plugin#

FiftyOne recognizes plugins by searching for `fiftyone.yml` or `fiftyone.yaml` files within your [plugins directory](plugins__using_plugins.md#plugins-directory).

Below is an example of a plugin directory with a typical Python plugin and JS plugin:
    
    
    /path/to/your/plugins/dir/
        my-js-plugin/
            fiftyone.yml
            package.json
            dist/
                index.umd.js
        my-py-plugin/
            fiftyone.yml
            __init__.py
            requirements.txt
    

Note

If the source code for a plugin already exists on disk, you can make it into a plugin using [`create_plugin()`](api__fiftyone.plugins.core.md#fiftyone.plugins.core.create_plugin "fiftyone.plugins.core.create_plugin") or the [fiftyone plugins create](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-create) CLI command.

This will copy the source code to the plugins directory and create a `fiftyone.yml` file for you if one does not already exist. Alternatively, you can manually copy the code into your plugins directory.

If your FiftyOne App is already running, you may need to restart the server and refresh your browser to see new plugins.

Note

When writing Python plugins with multiple files, see importing modules for how to import code between files in your plugin.

### fiftyone.yml#

All plugins must contain a `fiftyone.yml` or `fiftyone.yaml` file, which is used to define the pluginâs metadata, declare any operators and panels that it exposes, and declare any [secrets](plugins__using_plugins.md#plugins-secrets) that it may require. The following fields are available:

For example, the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/annotation/fiftyone.yml) pluginâs `fiftyone.yml` looks like this:
    
    
     1name: "@voxel51/annotation"
     2type: plugin
     3author: Voxel51
     4version: 1.0.0
     5url: https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation
     6license: Apache 2.0
     7description: Utilities for integrating FiftyOne with annotation tools
     8fiftyone:
     9  version: ">=0.22"
    10operators:
    11  - request_annotations
    12  - load_annotations
    13  - get_annotation_info
    14  - load_annotation_view
    15  - rename_annotation_run
    16  - delete_annotation_run
    17secrets:
    18  - FIFTYONE_CVAT_URL
    19  - FIFTYONE_CVAT_USERNAME
    20  - FIFTYONE_CVAT_PASSWORD
    21  - FIFTYONE_CVAT_EMAIL
    22  - FIFTYONE_LABELBOX_URL
    23  - FIFTYONE_LABELBOX_API_KEY
    24  - FIFTYONE_LABELSTUDIO_URL
    25  - FIFTYONE_LABELSTUDIO_API_KEY
    

Note

Although it is not strictly required, we highly recommend using the `@user-or-org-name/plugin-name` naming convention when writing plugins.

### Python plugins#

Python plugins should define the following files:

  * `__init__.py` **(required)** : entrypoint that defines the Python operators and panels that the plugin defines

  * `requirements.txt`: specifies the Python package requirements to run the plugin




### JS plugins#

JS plugins should define the following files:

  * `package.json`: a JSON file containing additional information about the plugin, including the JS bundle file path

  * `dist/index.umd.js`: a JS bundle file for the plugin




## Publishing plugins#

You can publish your FiftyOne plugins either privately or publicly by simply uploading the source directory or a ZIP of it to GitHub or another file hosting service.

Note

Want to share your plugin with the FiftyOne community? Make a pull request into the [FiftyOne Plugins](https://github.com/voxel51/fiftyone-plugins) repository to add it to the [Community Plugins list](https://github.com/voxel51/fiftyone-plugins#community-plugins)!

Any users with access to the pluginâs hosted location can easily [download it](plugins__using_plugins.md#plugins-download) via the [fiftyone plugins download](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-download) CLI command:
    
    
    # Download plugin(s) from a GitHub repository
    fiftyone plugins download https://github.com/<user>/<repo>[/tree/branch]
    
    # Download plugin(s) by specifying the GitHub repository details
    fiftyone plugins download <user>/<repo>[/<ref>]
    
    # Download specific plugins from a GitHub repository
    fiftyone plugins download \\
        https://github.com/<user>/<repo>[/tree/branch] \\
        --plugin-names <name1> <name2> <name3>
    

Note

GitHub repositories may contain multiple plugins. By default, all plugins that are found within the first three directory levels are installed, but you can select specific ones if desired as shown above.

## Quick examples#

This section contains a few quick examples of plugins before we dive into the full details of the plugin system.

Note

The best way to learn how to write plugins is to use and inspect existing ones. Check out the [FiftyOne plugins](https://github.com/voxel51/fiftyone-plugins) repository for a growing collection of plugins that you can use as examples when developing your own.

### Example plugin#

The [Hello World plugin](https://github.com/voxel51/hello-world-plugin-js) defines both a JS Panel and a Python operator:
    
    
     1name: "@voxel51/hello-world"
     2type: plugin
     3author: Voxel51
     4version: 1.0.0
     5url: https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/hello-world/README.md
     6license: Apache 2.0
     7description: An example of JS and Python components in a single plugin
     8fiftyone:
     9  version: "*"
    10operators:
    11  - count_samples
    12  - show_alert
    
    
    
     1import fiftyone.operators as foo
     2import fiftyone.operators.types as types
     3
     4class CountSamples(foo.Operator):
     5    @property
     6    def config(self):
     7        return foo.OperatorConfig(
     8            name="count_samples",
     9            label="Count samples",
    10            dynamic=True,
    11        )
    12
    13    def resolve_input(self, ctx):
    14        inputs = types.Object()
    15
    16        if ctx.view != ctx.dataset.view():
    17            choices = types.RadioGroup()
    18            choices.add_choice(
    19                "DATASET",
    20                label="Dataset",
    21                description="Count the number of samples in the dataset",
    22            )
    23
    24            choices.add_choice(
    25                "VIEW",
    26                label="Current view",
    27                description="Count the number of samples in the current view",
    28            )
    29
    30            inputs.enum(
    31                "target",
    32                choices.values(),
    33                required=True,
    34                default="VIEW",
    35                view=choices,
    36            )
    37
    38        return types.Property(inputs, view=types.View(label="Count samples"))
    39
    40    def execute(self, ctx):
    41        target = ctx.params.get("target", "DATASET")
    42        sample_collection = ctx.view if target == "VIEW" else ctx.dataset
    43        return {"count": sample_collection.count()}
    44
    45    def resolve_output(self, ctx):
    46        target = ctx.params.get("target", "DATASET")
    47        outputs = types.Object()
    48        outputs.int(
    49            "count",
    50            label=f"Number of samples in the current {target.lower()}",
    51        )
    52        return types.Property(outputs)
    53
    54def register(p):
    55    p.register(CountSamples)
    
    
    
     1import * as fos from "@fiftyone/state";
     2import { useRecoilValue } from "recoil";
     3import { useCallback } from "react";
     4import { Button } from "@fiftyone/components";
     5import {
     6  types,
     7  useOperatorExecutor,
     8  Operator,
     9  OperatorConfig,
    10  registerOperator,
    11  executeOperator,
    12} from "@fiftyone/operators";
    13
    14export function HelloWorld() {
    15  const executor = useOperatorExecutor("@voxel51/hello-world/count_samples");
    16  const onClickAlert = useCallback(() =>
    17    executeOperator("@voxel51/hello-world/show_alert")
    18  );
    19  const dataset = useRecoilValue(fos.dataset);
    20
    21  if (executor.isLoading) return <h3>Loading...</h3>;
    22  if (executor.result) return <h3>Dataset size: {executor.result.count}</h3>;
    23
    24  return (
    25    <>
    26      <h1>Hello, world!</h1>
    27      <h2>
    28        You are viewing the <strong>{dataset.name}</strong> dataset
    29      </h2>
    30      <Button onClick={() => executor.execute()}>Count samples</Button>
    31      <Button onClick={onClickAlert}>Show alert</Button>
    32    </>
    33  );
    34}
    35
    36class AlertOperator extends Operator {
    37  get config() {
    38    return new OperatorConfig({
    39      name: "show_alert",
    40      label: "Show alert",
    41      unlisted: true,
    42    });
    43  }
    44  async execute() {
    45    alert(`Hello from plugin ${this.pluginName}`);
    46  }
    47}
    48
    49registerOperator(AlertOperator, "@voxel51/hello-world");
    
    
    
     1import { registerComponent, PluginComponentType } from "@fiftyone/plugins";
     2import { HelloWorld } from "./HelloWorld";
     3
     4registerComponent({
     5  name: "HelloWorld",
     6  label: "Hello world",
     7  component: HelloWorld,
     8  type: PluginComponentType.Panel,
     9  activator: myActivator,
    10});
    11
    12function myActivator({ dataset }) {
    13  // Example of activating the plugin in a particular context
    14  // return dataset.name === 'quickstart'
    15
    16  return true;
    17}
    

Hereâs the plugin in action! The `Hello world` panel is available under the `+` icon next to the Samples tab and the `count_samples` operator is available in the operator browser:

![../_images/hello-world.gif](../_images/hello-world.gif)

### Example Python operator#

Hereâs a simple Python operator that accepts a string input and then displays it to the user in the operatorâs output modal.
    
    
     1class SimpleInputExample(foo.Operator):
     2    @property
     3    def config(self):
     4        return foo.OperatorConfig(
     5            name="simple_input_example",
     6            label="Simple input example",
     7        )
     8
     9    def resolve_input(self, ctx):
    10        inputs = types.Object()
    11        inputs.str("message", label="Message", required=True)
    12        header = "Simple input example"
    13        return types.Property(inputs, view=types.View(label=header))
    14
    15    def execute(self, ctx):
    16        return {"message": ctx.params["message"]}
    17
    18    def resolve_output(self, ctx):
    19        outputs = types.Object()
    20        outputs.str("message", label="Message")
    21        header = "Simple input example: Success!"
    22        return types.Property(outputs, view=types.View(label=header))
    23
    24def register(p):
    25    p.register(SimpleInputExample)
    

In practice, operators would use the inputs to perform some operation on the current dataset.

Note

Remember that you must also include the operatorâs name in the pluginâs fiftyone.yml:
    
    
    operators:
      - simple_input_example
    

### Example Python panel#

Hereâs a simple Python panel that renders a button that shows a âHello world!â notification when clicked:
    
    
     1import fiftyone.operators as foo
     2import fiftyone.operators.types as types
     3
     4class HelloWorldPanel(foo.Panel):
     5    @property
     6    def config(self):
     7        return foo.PanelConfig(
     8            name="hello_world_panel",
     9            label="Hello World Panel"
    10        )
    11
    12    def on_load(self, ctx):
    13        ctx.panel.state.hello_message = "Hello world!"
    14
    15    def say_hello(self, ctx):
    16        ctx.ops.notify(ctx.panel.state.hello_message)
    17
    18    def render(self, ctx):
    19        panel = types.Object()
    20        panel.btn(
    21            "hello_btn",
    22            label="Say Hello",
    23            icon="emoji_people",
    24            on_click=self.say_hello,
    25            variant="contained",
    26        )
    27
    28        panel_view = types.GridView(
    29            width=100, height=100, align_x="center", align_y="center"
    30        )
    31        return types.Property(panel, view=panel_view)
    32
    33def register(p):
    34    p.register(HelloWorldPanel)
    

Note

Remember that you must also include the panelâs name in the pluginâs fiftyone.yml:
    
    
    panels:
      - hello_world_panel
    

![../_images/hello-world-panel-inline.gif](../_images/hello-world-panel-inline.gif)

### Example JS operator#

Hereâs how to define a JS operator that sets the currently selected samples in the App based on a list of sample IDs provided via a `samples` parameter.
    
    
     1import {Operator, OperatorConfig, types, registerOperator} from "@fiftyone/operators";
     2const PLUGIN_NAME = "@my/plugin";
     3
     4class SetSelectedSamples extends Operator {
     5    get config(): OperatorConfig {
     6        return new OperatorConfig({
     7            name: "set_selected_samples",
     8            label: "Set selected samples",
     9            unlisted: true,
    10        });
    11    }
    12    useHooks(): {} {
    13        return {
    14            setSelected: fos.useSetSelected(),
    15        };
    16    }
    17    async execute({ hooks, params }: ExecutionContext) {
    18        hooks.setSelected(params.samples);
    19    }
    20}
    21
    22registerOperator(SetSelectedSamples, PLUGIN_NAME);
    

Unlike Python operators, JS operators can use React hooks and the `@fiftyone/*` packages by defining a `useHook()` method. Any values return in this method will be available to the operatorâs `execute()` method via `ctx.hooks`.

Note

Marking the operator as `unlisted` omits it from the [operator browser](plugins__using_plugins.md#using-operators), which is useful when the operator is intended only for internal use by other plugin components.

## Developing operators#

Operators allow you to define custom operations that accept parameters via input properties, execute some actions based on them, and optionally return outputs. They can be [executed](plugins__using_plugins.md#using-operators) by users in the App or triggered internally by other operators.

Operators can be defined in either Python or JS, and FiftyOne comes with a number of builtin [`Python`](plugins__api__plugins.operators.md#module-plugins.operators "plugins.operators") and [JS](https://github.com/voxel51/fiftyone/blob/develop/app/packages/operators/src/built-in-operators.ts) operators for common tasks.

The [`fiftyone.operators.types`](api__fiftyone.operators.types.md#module-fiftyone.operators.types "fiftyone.operators.types") module and [`@fiftyone/operators`](plugins__api__plugins.fiftyone.operators.md#module-fiftyone-operators "@fiftyone/operators") package define a rich builtin type system that operator developers can use to define the input and output properties of their operators without the need to build custom user interfaces from scratch. These types handle all aspects of input collection, validation, and component rendering for you.

Operators can be composed for coordination between Python and the FiftyOne App, such as triggering a reload of samples/view to update the app with the changes made by the operator. Operators can also be scheduled to run by an orchestrator or triggered by other operators.

### Operator interface#

The code block below describes the Python interface for defining operators. Weâll dive into each component of the interface in more detail in the subsequent sections.

Note

The JS interface for defining operators is analogous. See this example JS operator for details.
    
    
      1import fiftyone.operators as foo
      2import fiftyone.operators.types as types
      3
      4class ExampleOperator(foo.Operator):
      5    @property
      6    def config(self):
      7        return foo.OperatorConfig(
      8            # The operator's URI: f"{plugin_name}/{name}"
      9            name="example_operator",  # required
     10
     11            # The display name of the operator
     12            label="Example operator",  # required
     13
     14            # A description for the operator
     15            description="An example description"
     16
     17            # Whether to re-execute resolve_input() after each user input
     18            dynamic=True/False,  # default False
     19
     20            # Whether the operator's execute() method returns a generator
     21            # that should be iterated over until exhausted
     22            execute_as_generator=True/False,  # default False
     23
     24            # Whether to hide this operator from the App's operator browser
     25            # Set this to True if the operator is only for internal use
     26            unlisted=True/False,  # default False
     27
     28            # Whether the operator should be executed every time a new App
     29            # session starts
     30            on_startup=True/False,  # default False
     31
     32            # Whether the operator should be executed every time a new
     33            # dataset is opened in the App
     34            on_dataset_open=True/False,  # default False
     35
     36            # Custom icons to use
     37            # Can be a URL, a local path in the plugin directory, or the
     38            # name of a MUI icon: https://marella.me/material-icons/demo
     39            icon="/assets/icon.svg",
     40            light_icon="/assets/icon-light.svg",  # light theme only
     41            dark_icon="/assets/icon-dark.svg",  # dark theme only
     42
     43            # Whether the operator supports immediate and/or delegated execution
     44            allow_immediate_execution=True/False,    # default True
     45            allow_delegated_execution=True/False,    # default False
     46            default_choice_to_delegated=True/False,  # default False
     47            resolve_execution_options_on_change=None,
     48
     49            # Whether the operator supports distributed execution
     50            allow_distributed_execution=True/False,  # default False
     51        )
     52
     53    def resolve_placement(self, ctx):
     54        """You can optionally implement this method to configure a button
     55        or icon in the App that triggers this operator.
     56
     57        By default the operator only appears in the operator browser
     58        (unless it is unlisted).
     59
     60        Returns:
     61            a `types.Placement`
     62        """
     63        return types.Placement(
     64            # Make operator appear in the actions row above the sample grid
     65            types.Places.SAMPLES_GRID_SECONDARY_ACTIONS,
     66
     67            # Use a button as the operator's placement
     68            types.Button(
     69                # A label for placement button visible on hover
     70                label="Open Histograms Panel",
     71
     72                # An icon for the button
     73                # The default is a button with the `label` displayed
     74                icon="/assets/icon.svg",
     75
     76                # If False, don't show the operator's input prompt when we
     77                # do not require user input
     78                prompt=True/False  # False
     79            )
     80        )
     81
     82    def resolve_input(self, ctx):
     83        """Implement this method to collect user inputs as parameters
     84        that are stored in `ctx.params`.
     85
     86        Returns:
     87            a `types.Property` defining the form's components
     88        """
     89        inputs = types.Object()
     90
     91        # Use the builtin `types` and the current `ctx.params` to define
     92        # the necessary user input data
     93        inputs.str("key", ...)
     94
     95        # When `dynamic=True`, you'll often use the current `ctx` to
     96        # conditionally render different components
     97        if ctx.params["key"] == "value" and len(ctx.view) < 100:
     98            # do something
     99        else:
    100            # do something else
    101
    102        return types.Property(inputs, view=types.View(label="Example operator"))
    103
    104    def resolve_delegation(self, ctx):
    105        """Implement this method if you want to programmatically *force*
    106        this operation to be delegated or executed immediately.
    107
    108        Returns:
    109            whether the operation should be delegated (True), run
    110            immediately (False), or None to defer to
    111            `resolve_execution_options()` to specify the available options
    112        """
    113        return len(ctx.view) > 1000  # delegate for larger views
    114
    115    def resolve_execution_options(self, ctx):
    116        """Implement this method if you want to dynamically configure the
    117        execution options available to this operator based on the current
    118        `ctx`.
    119
    120        Returns:
    121            an `ExecutionOptions` instance
    122        """
    123        should_delegate = len(ctx.view) > 1000  # delegate for larger views
    124        return foo.ExecutionOptions(
    125            allow_immediate_execution=True,
    126            allow_delegated_execution=True,
    127            default_choice_to_delegated=should_delegate,
    128        )
    129
    130    def execute(self, ctx):
    131        """Executes the actual operation based on the hydrated `ctx`.
    132        All operators must implement this method.
    133
    134        This method can optionally be implemented as `async`.
    135
    136        Returns:
    137            an optional dict of results values
    138        """
    139        # Use ctx.params, ctx.dataset, ctx.view, etc to perform the
    140        # necessary computation
    141        value = ctx.params["key"]
    142        view = ctx.view
    143        n = len(view)
    144
    145        # Use ctx.ops to trigger builtin operations
    146        ctx.ops.clear_selected_samples()
    147        ctx.ops.set_view(view=view)
    148
    149        # Use ctx.trigger to call other operators as necessary
    150        ctx.trigger("operator_uri", params={"key": value})
    151
    152        # If `execute_as_generator=True`, this method may yield multiple
    153        # messages
    154        for i, sample in enumerate(current_view, 1):
    155            # do some computation
    156            yield ctx.ops.set_progress(progress=i/n)
    157
    158        yield ctx.ops.reload_dataset()
    159
    160        return {"value": value, ...}
    161
    162    def resolve_output(self, ctx):
    163        """Implement this method if your operator renders an output form
    164        to the user.
    165
    166        Returns:
    167            a `types.Property` defining the components of the output form
    168        """
    169        outputs = types.Object()
    170
    171        # Use the builtin `types` and the current `ctx.params` and
    172        # `ctx.results` as necessary to define the necessary output form
    173        outputs.define_property("value", ...)
    174
    175        return types.Property(outputs, view=types.View(label="Example operator"))
    176
    177def register(p):
    178    """Always implement this method and register() each operator that your
    179    plugin defines.
    180    """
    181    p.register(ExampleOperator)
    

Note

Remember that you must also include the operatorâs name in the pluginâs fiftyone.yml:
    
    
    operators:
      - example_operator
    

### Operator config#

Every operator must define a [`config`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.config "fiftyone.operators.operator.Operator.config") property that defines its name, display name, and other optional metadata about its execution:
    
    
     1@property
     2def config(self):
     3    return foo.OperatorConfig(
     4        # The operator's URI: f"{plugin_name}/{name}"
     5        name="example_operator",  # required
     6
     7        # The display name of the operator
     8        label="Example operator",  # required
     9
    10        # A description for the operator
    11        description="An example description"
    12
    13        # Whether to re-execute resolve_input() after each user input
    14        dynamic=True/False,  # default False
    15
    16        # Whether the operator's execute() method returns a generator
    17        # that should be iterated over until exhausted
    18        execute_as_generator=True/False,  # default False
    19
    20        # Whether to hide this operator from the App's operator browser
    21        # Set this to True if the operator is only for internal use
    22        unlisted=True/False,  # default False
    23
    24        # Whether the operator should be executed every time a new App
    25        # session starts
    26        on_startup=True/False,  # default False
    27
    28        # Whether the operator should be executed every time a new dataset
    29        # is opened in the App
    30        on_dataset_open=True/False,  # default False
    31
    32        # Custom icons to use
    33        # Can be a URL, a local path in the plugin directory, or the
    34        # name of a MUI icon: https://marella.me/material-icons/demo
    35        icon="/assets/icon.svg",
    36        light_icon="/assets/icon-light.svg",  # light theme only
    37        dark_icon="/assets/icon-dark.svg",  # dark theme only
    38
    39        # Whether the operator supports immediate and/or delegated execution
    40        allow_immediate_execution=True/False,    # default True
    41        allow_delegated_execution=True/False,    # default False
    42        default_choice_to_delegated=True/False,  # default False
    43        resolve_execution_options_on_change=None,
    44
    45        # Whether the operator supports distributed execution
    46        allow_distributed_execution=True/False,  # default False
    47    )
    

### Execution context#

An [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") is passed to each of the operatorâs methods at runtime. This `ctx` contains static information about the current state of the App (dataset, view, panel, selection, etc) as well as dynamic information about the current parameters and results.

An [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") contains the following properties:

  * `ctx.params`: a dict containing the operatorâs current input parameter values

  * `ctx.dataset_name`: the name of the current dataset

  * `ctx.dataset` \- the current [`Dataset`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset "fiftyone.core.dataset.Dataset") instance

  * `ctx.view` \- the current [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") instance

  * `ctx.spaces` \- the current [Spaces layout](user_guide__app.md#app-spaces) in the App

  * `ctx.current_sample` \- the ID of the active sample in the App modal, if any

  * `ctx.selected` \- the list of currently selected samples in the App, if any

  * `ctx.selected_labels` \- the list of currently selected labels in the App, if any

  * `ctx.extended_selection` \- the extended selection of the view, if any

  * `ctx.active_fields` \- the list of currently active fields in the App sidebar, if any

  * `ctx.group_slice` \- the active group slice in the App, if any

  * `ctx.user_id` \- the ID of the user that invoked the operator, if known

  * `ctx.user` \- an object of information about the user that invoked the operator, if known, including the userâs `id`, `name`, `email`, `role`, and `dataset_permission`

  * `ctx.user_request_token` \- the request token authenticating the user executing the operation, if known

  * `ctx.prompt_id` \- a unique identifier for each instance of a user opening an operator prompt in the App

  * `ctx.operator_uri` \- the URI of the target operator

  * `ctx.panel_id` \- the ID of the panel that invoked the operator, if any

  * `ctx.panel` \- a [`PanelRef`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.PanelRef "fiftyone.operators.panel.PanelRef") instance that you can use to read and write the state and data of the current panel, if the operator was invoked from a panel

  * `ctx.pipeline` \- information about execution state of the pipeline, if applicable. See this section

  * `ctx.delegated` \- whether the operation was delegated

  * `ctx.requesting_delegated_execution` \- whether delegated execution was requested for the operation

  * `ctx.delegation_target` \- the orchestrator to which the operation should be delegated, if applicable

  * `ctx.ops` \- an [`Operations`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations "fiftyone.operators.operations.Operations") instance that you can use to trigger builtin operations on the current context

  * `ctx.trigger` \- a method that you can use to trigger arbitrary operations on the current context

  * `ctx.secrets` \- a dict of secrets for the plugin, if any

  * `ctx.results` \- a dict containing the outputs of the `execute()` method, if it has been called

  * `ctx.hooks` **(JS only)** \- the return value of the operatorâs `useHooks()` method




### Operator inputs#

Operators can optionally implement [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") to define user input forms that are presented to the user as a modal in the App when the operator is invoked.

The basic objective of [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") is to populate the `ctx.params` dict with user-provided parameter values, which are retrieved from the various subproperties of the [`Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property") returned by the method (`inputs` in the examples below).

The [`fiftyone.operators.types`](api__fiftyone.operators.types.md#module-fiftyone.operators.types "fiftyone.operators.types") module defines a rich builtin type system that you can use to define the necessary input properties. These types handle all aspects of input collection, validation, and component rendering for you!

For example, hereâs a simple example of collecting a single string input from the user:
    
    
    1def resolve_input(self, ctx):
    2    inputs = types.Object()
    3    inputs.str("message", label="Message", required=True)
    4    return types.Property(inputs, view=types.View(label="Static example"))
    5
    6def execute(self, ctx):
    7    the_message = ctx.params["message"]
    

If the operatorâs config declares `dynamic=True`, then [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") will be called after each user input, which allows you to construct dynamic forms whose components may contextually change based on the already provided values and any other aspects of the execution context:
    
    
     1import fiftyone.brain as fob
     2
     3def resolve_input(self, ctx):
     4    inputs = types.Object()
     5    brain_keys = ctx.dataset.list_brain_runs()
     6
     7    if not brain_keys:
     8        warning = types.Warning(label="This dataset has no brain runs")
     9        prop = inputs.view("warning", warning)
    10        prop.invalid = True  # so form's `Execute` button is disabled
    11        return
    12
    13    choices = types.DropdownView()
    14    for brain_key in brain_keys:
    15        choices.add_choice(brain_key, label=brain_key)
    16
    17    inputs.str(
    18        "brain_key",
    19        required=True,
    20        label="Brain key",
    21        description="Choose a brain key to use",
    22        view=choices,
    23    )
    24
    25    brain_key = ctx.params.get("brain_key", None)
    26    if brain_key is None:
    27        return  # single `brain_key`
    28
    29    info = ctx.dataset.get_brain_info(brain_key)
    30
    31    if isinstance(info.config, fob.SimilarityConfig):
    32        # We found a similarity config; render some inputs specific to that
    33        inputs.bool(
    34            "upgrade",
    35            label="Compute visualization",
    36            description="Generate an embeddings visualization for this index?",
    37            view=types.CheckboxView(),
    38        )
    39
    40    return types.Property(inputs, view=types.View(label="Dynamic example"))
    

Remember that properties automatically handle validation for you. So if you configure a property as `required=True` but the user has not provided a value, the property will automatically be marked as `invalid=True`. The operatorâs `Execute` button will be enabled if and only if all input properties are valid (recursively searching nested objects).

Note

As the example above shows, you can manually set a property to invalid by setting its `invalid` property.

### Common input patterns#

The [`fiftyone.operators.types`](api__fiftyone.operators.types.md#module-fiftyone.operators.types "fiftyone.operators.types") module provides a wide variety of input types and views that you can use to build rich input forms for your operators. This section demonstrates the most popular patterns.

Note

These examples show Python operators. The same types are available for JS operators via the [`@fiftyone/operators`](plugins__api__plugins.fiftyone.operators.md#module-fiftyone-operators "@fiftyone/operators") package.

![https://cdn.voxel51.com/developing_plugins/operator_inputs_showcase.webp](https://cdn.voxel51.com/developing_plugins/operator_inputs_showcase.webp)

#### String inputs#

The simplest input type is a string field. Use the `description` parameter to configure placeholder text:
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    inputs.str(
     5        "name",
     6        label="Name",
     7        description="Enter a name...",
     8        required=True,
     9    )
    10
    11    inputs.str(
    12        "notes",
    13        label="Notes",
    14        description="Optional notes",
    15    )
    16
    17    return types.Property(inputs, view=types.View(label="String inputs"))
    18
    19def execute(self, ctx):
    20    name = ctx.params["name"]
    21    notes = ctx.params.get("notes", None)
    

#### Numeric inputs#

Use `inputs.int()` and `inputs.float()` to collect numeric values. You can enforce `min` and `max` constraints and optionally render the input as a slider via [`SliderView`](api__fiftyone.operators.types.md#fiftyone.operators.types.SliderView "fiftyone.operators.types.SliderView"):
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    # A simple integer input with min/max constraints
     5    inputs.int(
     6        "num_samples",
     7        label="Number of samples",
     8        description="How many samples to process",
     9        required=True,
    10        min=1,
    11        max=1000,
    12    )
    13
    14    # A float input rendered as a slider
    15    inputs.float(
    16        "confidence",
    17        label="Confidence threshold",
    18        description="Minimum confidence score",
    19        default=0.5,
    20        min=0.0,
    21        max=1.0,
    22        view=types.SliderView(),
    23    )
    24
    25    return types.Property(inputs, view=types.View(label="Numeric inputs"))
    26
    27def execute(self, ctx):
    28    num_samples = ctx.params["num_samples"]
    29    confidence = ctx.params.get("confidence", 0.5)
    

#### Boolean inputs#

Use `inputs.bool()` to collect boolean values. By default, a checkbox is rendered, but you can also use [`SwitchView`](api__fiftyone.operators.types.md#fiftyone.operators.types.SwitchView "fiftyone.operators.types.SwitchView") for a toggle switch:
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    # A standard checkbox
     5    inputs.bool(
     6        "include_labels",
     7        label="Include labels",
     8        description="Whether to include labels in the export",
     9        default=True,
    10        view=types.CheckboxView(),
    11    )
    12
    13    # A toggle switch
    14    inputs.bool(
    15        "overwrite",
    16        label="Overwrite existing",
    17        description="Whether to overwrite existing results",
    18        default=False,
    19        view=types.SwitchView(),
    20    )
    21
    22    return types.Property(inputs, view=types.View(label="Boolean inputs"))
    23
    24def execute(self, ctx):
    25    include_labels = ctx.params.get("include_labels", True)
    26    overwrite = ctx.params.get("overwrite", False)
    

#### Date and datetime inputs#

Use [`DateTimeView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DateTimeView "fiftyone.operators.types.DateTimeView") to render a calendar picker. Set `date_only=True` to collect a date without a time component. The values are returned as epoch timestamps in milliseconds and can be converted to Python datetime objects via [`timestamp_to_datetime()`](api__fiftyone.core.utils.md#fiftyone.core.utils.timestamp_to_datetime "fiftyone.core.utils.timestamp_to_datetime"):
    
    
     1import fiftyone.core.utils as fou
     2
     3def resolve_input(self, ctx):
     4    inputs = types.Object()
     5
     6    # A date-only picker
     7    inputs.int(
     8        "start_date",
     9        required=True,
    10        label="Start date",
    11        description="Choose a start date",
    12        view=types.DateTimeView(date_only=True),
    13    )
    14
    15    # A full date and time picker
    16    inputs.int(
    17        "end_datetime",
    18        label="End date/time",
    19        description="Choose an end date and time",
    20        view=types.DateTimeView(),
    21    )
    22
    23    return types.Property(inputs, view=types.View(label="Date inputs"))
    24
    25def execute(self, ctx):
    26    start_epoch = ctx.params.get("start_date", None)
    27    end_epoch = ctx.params.get("end_datetime", None)
    28
    29    if start_epoch is not None:
    30        start = fou.timestamp_to_datetime(start_epoch)
    31
    32    if end_epoch is not None:
    33        end = fou.timestamp_to_datetime(end_epoch)
    

Note

Date and datetime properties must use `inputs.int()` because the values are returned as epoch timestamps (milliseconds).

#### Dropdown and autocomplete inputs#

Use [`DropdownView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView "fiftyone.operators.types.DropdownView") to render a dropdown selector. For inputs where the user may also need to search or type a custom value, use [`AutocompleteView`](api__fiftyone.operators.types.md#fiftyone.operators.types.AutocompleteView "fiftyone.operators.types.AutocompleteView"):
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    # A standard dropdown
     5    dropdown = types.DropdownView()
     6    dropdown.add_choice("coco", label="COCO")
     7    dropdown.add_choice("voc", label="VOC")
     8    dropdown.add_choice("yolo", label="YOLO")
     9
    10    inputs.enum(
    11        "format",
    12        dropdown.values(),
    13        required=True,
    14        label="Export format",
    15        description="Choose an export format",
    16        view=dropdown,
    17    )
    18
    19    # An autocomplete input that also allows custom values
    20    field_names = ctx.dataset.get_field_schema().keys()
    21    autocomplete = types.AutocompleteView()
    22    for name in field_names:
    23        autocomplete.add_choice(name, label=name)
    24
    25    inputs.enum(
    26        "field",
    27        autocomplete.values(),
    28        required=True,
    29        label="Field",
    30        description="Choose or type a field name",
    31        view=autocomplete,
    32    )
    33
    34    return types.Property(inputs, view=types.View(label="Selection inputs"))
    35
    36def execute(self, ctx):
    37    format = ctx.params["format"]
    38    field = ctx.params["field"]
    

#### Radio group inputs#

Use [`RadioGroup`](api__fiftyone.operators.types.md#fiftyone.operators.types.RadioGroup "fiftyone.operators.types.RadioGroup") to render a set of mutually exclusive choices as radio buttons. You can control the layout via the `orientation` parameter:
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    choices = types.RadioGroup(orientation="vertical")
     5    choices.add_choice(
     6        "classification",
     7        label="Classification",
     8        description="Classify each sample into a category",
     9    )
    10    choices.add_choice(
    11        "detection",
    12        label="Detection",
    13        description="Detect objects in each sample",
    14    )
    15    choices.add_choice(
    16        "segmentation",
    17        label="Segmentation",
    18        description="Segment each sample",
    19    )
    20
    21    inputs.enum(
    22        "task",
    23        choices.values(),
    24        required=True,
    25        label="Task type",
    26        view=choices,
    27    )
    28
    29    return types.Property(inputs, view=types.View(label="Radio group inputs"))
    30
    31def execute(self, ctx):
    32    task = ctx.params["task"]
    

#### Conditional inputs#

A common pattern is to show or hide input fields based on the current value of another field. To achieve this, set `dynamic=True` in the operatorâs config and use the current `ctx.params` to conditionally define properties in [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input"):
    
    
     1import fiftyone.operators as foo
     2import fiftyone.operators.types as types
     3
     4class ConditionalInputsExample(foo.Operator):
     5    @property
     6    def config(self):
     7        return foo.OperatorConfig(
     8            name="conditional_inputs_example",
     9            label="Conditional inputs example",
    10            dynamic=True,
    11        )
    12
    13    def resolve_input(self, ctx):
    14        inputs = types.Object()
    15
    16        # First, let the user choose a task type
    17        choices = types.RadioGroup()
    18        choices.add_choice("export", label="Export")
    19        choices.add_choice("import", label="Import")
    20
    21        inputs.enum(
    22            "action",
    23            choices.values(),
    24            required=True,
    25            label="Action",
    26            view=choices,
    27        )
    28
    29        action = ctx.params.get("action", None)
    30
    31        # Then show different fields depending on the chosen action
    32        if action == "export":
    33            dropdown = types.DropdownView()
    34            dropdown.add_choice("coco", label="COCO")
    35            dropdown.add_choice("yolo", label="YOLO")
    36
    37            inputs.enum(
    38                "format",
    39                dropdown.values(),
    40                required=True,
    41                label="Export format",
    42                view=dropdown,
    43            )
    44            inputs.str(
    45                "output_dir",
    46                required=True,
    47                label="Output directory",
    48                description="Where to write the exported data",
    49            )
    50
    51        elif action == "import":
    52            inputs.file(
    53                "input_file",
    54                required=True,
    55                label="Input file",
    56                description="Choose a file to import",
    57                view=types.FileExplorerView(
    58                    button_label="Choose a file...",
    59                ),
    60            )
    61
    62        return types.Property(
    63            inputs, view=types.View(label="Conditional inputs example")
    64        )
    65
    66    def execute(self, ctx):
    67        action = ctx.params["action"]
    68
    69        if action == "export":
    70            format = ctx.params["format"]
    71            output_dir = ctx.params["output_dir"]
    72            # perform export...
    73        elif action == "import":
    74            input_file = ctx.params.get("input_file", {})
    75            filepath = input_file.get("absolute_path", None)
    76            # perform import...
    

Note

The `dynamic=True` setting causes [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") to be called after each user interaction, which is what enables the conditional rendering. Without it, the form is rendered only once.

#### File inputs#

Use `inputs.file()` with [`FileExplorerView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileExplorerView "fiftyone.operators.types.FileExplorerView") to let users browse and select files or directories. You can also use [`FileView`](api__fiftyone.operators.types.md#fiftyone.operators.types.FileView "fiftyone.operators.types.FileView") for drag-and-drop file uploads:
    
    
     1import base64
     2
     3def resolve_input(self, ctx):
     4    inputs = types.Object()
     5
     6    # A file explorer for choosing a directory
     7    inputs.file(
     8        "directory",
     9        required=True,
    10        label="Directory",
    11        description="Choose a directory",
    12        view=types.FileExplorerView(
    13            choose_dir=True,
    14            button_label="Choose a directory...",
    15        ),
    16    )
    17
    18    # A drag-and-drop file upload
    19    inputs.define_property(
    20        "uploaded",
    21        types.UploadedFile(),
    22        label="Upload a file",
    23        description="Drag and drop a file here",
    24        view=types.FileView(
    25            max_size=10 * 1024 * 1024,
    26            max_size_error_message="File must be under 10MB",
    27            types=".csv,.json",
    28        ),
    29    )
    30
    31    return types.Property(inputs, view=types.View(label="File inputs"))
    32
    33def execute(self, ctx):
    34    directory = ctx.params.get("directory", {}).get("absolute_path", None)
    35    file_obj = ctx.params["uploaded"]
    36    filename = file_obj["name"]
    37    content = base64.b64decode(file_obj["content"])
    

#### List inputs#

Use [`DropdownView`](api__fiftyone.operators.types.md#fiftyone.operators.types.DropdownView "fiftyone.operators.types.DropdownView") with `multiple=True` to let users select multiple values from a predefined set:
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    choices = types.DropdownView(multiple=True)
     5    choices.add_choice("train", label="Train")
     6    choices.add_choice("val", label="Validation")
     7    choices.add_choice("test", label="Test")
     8
     9    inputs.list(
    10        "splits",
    11        types.String(),
    12        label="Splits",
    13        description="Select one or more splits",
    14        view=choices,
    15    )
    16
    17    return types.Property(inputs, view=types.View(label="List input"))
    18
    19def execute(self, ctx):
    20    splits = ctx.params.get("splits", [])
    

Note

You can also use [`TagsView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TagsView "fiftyone.operators.types.TagsView") with `inputs.list()` to render values as chips. `TagsView` is best suited for displaying existing tags, while `DropdownView(multiple=True)` is recommended when users need to choose from a known set of options.

#### Code inputs#

Use [`CodeView`](api__fiftyone.operators.types.md#fiftyone.operators.types.CodeView "fiftyone.operators.types.CodeView") to render a code editor with syntax highlighting. Specify the `language` parameter to enable highlighting for the appropriate language:
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    inputs.str(
     5        "query",
     6        label="MongoDB query",
     7        description="Enter a MongoDB aggregation pipeline",
     8        view=types.CodeView(language="json"),
     9    )
    10
    11    return types.Property(inputs, view=types.View(label="Code input"))
    12
    13def execute(self, ctx):
    14    query = ctx.params.get("query", None)
    

#### Tabbed inputs#

Use [`TabsView`](api__fiftyone.operators.types.md#fiftyone.operators.types.TabsView "fiftyone.operators.types.TabsView") to render a set of choices as a horizontal tab bar. Combine with conditional logic to show different fields for each tab:
    
    
     1def resolve_input(self, ctx):
     2    inputs = types.Object()
     3
     4    tabs = types.TabsView()
     5    tabs.add_choice("IMAGE", label="Image")
     6    tabs.add_choice("VIDEO", label="Video")
     7    tabs.add_choice("POINT_CLOUD", label="Point cloud")
     8
     9    inputs.enum(
    10        "media_type",
    11        tabs.values(),
    12        default="IMAGE",
    13        required=True,
    14        label="Media type",
    15        view=tabs,
    16    )
    17
    18    media_type = ctx.params.get("media_type", "IMAGE")
    19
    20    if media_type == "IMAGE":
    21        inputs.str(
    22            "image_field",
    23            required=True,
    24            label="Image field",
    25            description="The field containing images",
    26        )
    27    elif media_type == "VIDEO":
    28        inputs.str(
    29            "video_field",
    30            required=True,
    31            label="Video field",
    32            description="The field containing videos",
    33        )
    34    elif media_type == "POINT_CLOUD":
    35        inputs.str(
    36            "point_cloud_field",
    37            required=True,
    38            label="Point cloud field",
    39            description="The field containing point clouds",
    40        )
    41
    42    return types.Property(inputs, view=types.View(label="Tabbed input"))
    43
    44def execute(self, ctx):
    45    media_type = ctx.params["media_type"]
    46
    47    if media_type == "IMAGE":
    48        field = ctx.params["image_field"]
    49    elif media_type == "VIDEO":
    50        field = ctx.params["video_field"]
    51    elif media_type == "POINT_CLOUD":
    52        field = ctx.params["point_cloud_field"]
    

### Caching expensive inputs#

Some operators may need to perform expensive computations in [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") to collect user inputs. In such cases, the [`execution_cache`](api__fiftyone.operators.cache.md#fiftyone.operators.cache.execution_cache "fiftyone.operators.cache.execution_cache") decorator can be used to optimize the operatorâs runtime by caching these expensive computations so that they are not re-computed unnecessarily. Input caching can be particularly important for operators that declare `dynamic=True`, as their [`resolve_input()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_input "fiftyone.operators.operator.Operator.resolve_input") is called after each user interaction in the prompt modal.

To use the [`execution_cache`](api__fiftyone.operators.cache.md#fiftyone.operators.cache.execution_cache "fiftyone.operators.cache.execution_cache") decorator, simply isolate any expensive computations in a dedicated method and configure the caching strategy according to your needs:
    
    
     1from operator import itemgetter
     2import fiftyone.operators as foo
     3
     4class ExpensiveInputsOperator(foo.Operator):
     5    @property
     6    def config(self):
     7        return foo.OperatorConfig(
     8            name="expensive_inputs_operator",
     9            label="Example view operator",
    10            dynamic=True,
    11        )
    12
    13    def resolve_input(self, ctx):
    14        inputs = types.Object()
    15
    16        inputs.str("path", ...)
    17        path = ctx.params["path"]
    18
    19        # An expensive computation that we don't want to repeat unnecessarily
    20        counts = count_values(ctx, path)
    21
    22        choices = types.DropdownView()
    23        for value, count in sorted(counts.items(), key=itemgetter(1), reverse=True):
    24            choices.add_choice(value, label=f"{value} ({count})")
    25
    26        ...
    27
    28# Option 1
    29# Cache for all dataset users for 90 seconds
    30@execution_cache(ttl=90)
    31def count_values(ctx, path):
    32    return ctx.dataset.count_values(path)
    33
    34# Option 2
    35# Cache in-memory and only for the life of the current prompt modal
    36@execution_cache(prompt_scoped=True, residency="ephemeral")
    37def count_values(ctx, path):
    38    return ctx.dataset.count_values(path)
    

Note

Refer to this section for more information about using the execution cache.

### Async data loading#

Some operators need to load data asynchronously (e.g., from an API or database) based on user input. The [`loader()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.loader "fiftyone.operators.types.Object.loader") method allows you to fetch data without blocking the form, showing a loading indicator while the data is being retrieved.

To use a loader, define an operator that returns the data and call [`inputs.loader()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.loader "fiftyone.operators.types.Object.loader") to trigger it:
    
    
     1class LoadModels(foo.Operator):
     2    @property
     3    def config(self):
     4        return foo.OperatorConfig(name="load_models", unlisted=True)
     5
     6    def execute(self, ctx):
     7        make = ctx.params.get("make")
     8        models = {"dodge": [{"id": "charger", "name": "Charger"}]}
     9        return models.get(make, [])
    10
    11
    12class CarSelector(foo.Operator):
    13    @property
    14    def config(self):
    15        return foo.OperatorConfig(name="car_selector", dynamic=True)
    16
    17    def resolve_input(self, ctx):
    18        inputs = types.Object()
    19        inputs.enum("make", values=["dodge", "jeep"], label="Make")
    20
    21        if ctx.params.get("make"):
    22            inputs.loader(
    23                "models",
    24                type=types.List(types.Object()),
    25                operator="@my-plugin/load_models",
    26                params={"make": ctx.params["make"]},
    27                label="Loading models...",
    28                dependencies=["make"],  # reload when "make" changes
    29            )
    30
    31        models = ctx.params.get("models", {})
    32        if models.get("state") == "loaded":
    33            inputs.enum("model", values=[m["id"] for m in models["data"]], label="Model")
    34
    35        return types.Property(inputs)
    

The loader property value always has the following structure:

  * `state`: one of `"idle"`, `"loading"`, `"loaded"`, or `"errored"`

  * `data`: the data returned by the operator (shaped by the `type` argument)

  * `error`: an error message if the loader failed




By default, loaders execute only once when the form mounts. To reload data when specific parameters change, use the `dependencies` argument with a list of parameter paths to watch:
    
    
    inputs.loader(
        "models",
        type=types.List(types.Object()),
        operator="@my-plugin/load_models",
        params={"make": ctx.params["make"]},
        label="Loading models...",
        dependencies=["make"],  # reload only when "make" changes
    )
    

The `dependencies` argument supports dot-notation for nested values (e.g., `"filters.category"`). The loader will re-execute whenever any of these values change, but will ignore changes to other parameters.

Note

Loaders require `dynamic=True` in the operator config so that [`resolve_input()`](api__fiftyone.operators.md#fiftyone.operators.Operator.resolve_input "fiftyone.operators.Operator.resolve_input") is re-called when the loader state changes.

### Target view **NEW**#

Added in version 1.8.0.

A common pattern when defining operators is to allow users to choose whether an operator should be applied to the entire dataset, just the current view, or some other subset of samples. FiftyOne has a builtin utility for applying this pattern to your operators.

To use this feature, call the [`inputs.view_target()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.view_target "fiftyone.operators.types.Object.view_target") function within your operatorâs [`resolve_input()`](api__fiftyone.operators.md#fiftyone.operators.Operator.resolve_input "fiftyone.operators.Operator.resolve_input") method. This will add a radio button group to your operatorâs input form that presents the set of possible view targets to the user. The resolved target view can then be accessed in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method via [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view").

Hereâs a simple example of an operator that uses the target view pattern to give the user the choice of target view to process:
    
    
     1import fiftyone.operators as foo
     2
     3class MyTargetViewOperator(foo.Operator):
     4    @property
     5    def config(self):
     6        return foo.OperatorConfig(
     7            name="target_view_operator",
     8            label="Target view operator",
     9            dynamic=True,
    10        )
    11
    12    def resolve_input(self, ctx):
    13        inputs = types.Object()
    14
    15        # Prompt user to select the target view to process
    16        inputs.view_target(ctx)
    17
    18        return types.Property(
    19            inputs, view=types.View(label="Target view operator")
    20        )
    21
    22    def execute(self, ctx):
    23        # Do something with the target view
    24        target_view = ctx.target_view()
    25        print("Sample collection size", len(target_view))
    

And hereâs a screenshot of a typical target view radio group in an operatorâs input form:

![../_images/operator-target-view.png](../_images/operator-target-view.png)

The available choices the user will have for the target view at runtime depend on the current execution context and the values of any optional parameters you pass to [`inputs.view_target()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.view_target "fiftyone.operators.types.Object.view_target").

The full set of possible view targets are:

Choice | Description  
---|---  
DATASET | The current dataset loaded in the App. Always presented as an option unless the current view is a generated view  
BASE_VIEW | The current base view in the App. Always presented as an option in place of `DATASET` when the current view is a generated view (eg [patches](https://docs.voxel51.com/user_guide/using_views.html#object-patches-views), [frames](https://docs.voxel51.com/user_guide/using_views.html#frame-views), or [clips](https://docs.voxel51.com/user_guide/using_views.html#clip-views)). Base view is the semantic equivalent of âentire datasetâ for generated views. For example, `dataset.limit(51).to_frames("ground_truth").limit(10)` has a base view of `dataset.limit(51).to_frames("ground_truth")`  
CURRENT_VIEW | The current view loaded in the App. Always presented as an option unless the full dataset is currently loaded  
DATASET_VIEW | A full view of the current dataset (ie `ctx.dataset.view()`). Only presented as an option if `allow_dataset_view=True`  
SELECTED_SAMPLES | The currently selected samples in the App. Only presented as an option if `allow_selected_samples=True` and the user has samples selected  
SELECTED_LABELS | The currently selected labels in the App, Only presented as an option if `allow_selected_labels=True` and the user has labels selected  
  
At runtime, the target view radio group is dynamically generated to only show the valid view targets given the current state of the userâs App.

For example, if the user is currently viewing the entire dataset in the App and no samples are currently selected, the `DATASET_VIEW` and `SELECTED_SAMPLES` options are automatically omitted from the radio group, since they do not apply. If there is only one valid choice, the radio group is omitted completely.

The target view descriptions in the input form can be configured by passing the optional `action_description` and various other description parameters to [`inputs.view_target()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Object.view_target "fiftyone.operators.types.Object.view_target"). If a description parameter is not `None`, it will be used as the description for the corresponding target view choice. Otherwise, a default description will be generated such as `f"{action_description} the entire dataset"`.

### Operator execution#

All operators must implement [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute"), which is where their main actions are performed.

The [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") method takes an execution context as input whose `ctx.params` dict has been hydrated with parameters provided either by the user by filling out the operatorâs input form or directly provided by the operation that triggered it. The method can optionally return a dict of results values that will be made available via `ctx.results` when the operatorâs output form is rendered.

#### Synchronous execution#

Your execution method is free to make use of the full power of the FiftyOne SDK and any external dependencies that it needs.

For example, you might perform inference on a model:
    
    
     1import fiftyone.zoo as foz
     2
     3def execute(self, ctx):
     4    name = ctx.params["name"]
     5    label_field = ctx.params["label_field"]
     6    confidence_thresh = ctx.params.get("confidence_thresh", None)
     7
     8    model = foz.load_zoo_model(name)
     9    ctx.view.apply_model(
    10        model, label_field=label_field, confidence_thresh=confidence_thresh
    11    )
    12
    13    num_predictions = ctx.view.count(f"{label_field}.detections")
    14    return {"num_predictions": num_predictions}
    

Note

When an operatorâs [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") method throws an error it will be displayed to the user in the browser.

#### Asynchronous execution#

The [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") method can also be `async`:
    
    
    1import aiohttp
    2
    3async def execute(self, ctx):
    4    # do something async
    5    async with aiohttp.ClientSession() as session:
    6        async with session.get(url) as resp:
    7            r = await resp.json()
    

#### Operator composition#

Many operators are designed to be composed with other operators to build up more complex behaviors. You can trigger other operations from within an operatorâs [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") method via [`ctx.ops`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations "fiftyone.operators.operations.Operations") and [`ctx.trigger`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.trigger "fiftyone.operators.executor.ExecutionContext.trigger").

The [`ctx.ops`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations "fiftyone.operators.operations.Operations") property of an execution context exposes all builtin [`Python`](plugins__api__plugins.operators.md#module-plugins.operators "plugins.operators") and [JavaScript](https://github.com/voxel51/fiftyone/blob/develop/app/packages/operators/src/built-in-operators.ts) operators in a conveniently documented functional interface. For example, many operations involve updating the current state of the App:
    
    
     1def execute(self, ctx):
     2    # Dataset
     3    ctx.ops.open_dataset("...")
     4    ctx.ops.reload_dataset()
     5
     6    # View/sidebar
     7    ctx.ops.set_view(name="...")  # saved view by name
     8    ctx.ops.set_view(view=view)  # arbitrary view
     9    ctx.ops.clear_view()
    10    ctx.ops.clear_sidebar_filters()
    11
    12    # Selected samples
    13    ctx.ops.set_selected_samples([...])
    14    ctx.ops.clear_selected_samples()
    15
    16    # Selected labels
    17    ctx.ops.set_selected_labels([...])
    18    ctx.ops.clear_selected_labels()
    19
    20    # Panels
    21    ctx.ops.open_panel("Embeddings")
    22    ctx.ops.close_panel("Embeddings")
    

The [`ctx.trigger`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.trigger "fiftyone.operators.executor.ExecutionContext.trigger") property is a lower-level function that allows you to invoke arbitrary operations by providing their URI and parameters, including all builtin operations as well as any operations installed via custom plugins. For example, hereâs how to trigger the same App-related operations from above:
    
    
     1def execute(self, ctx):
     2    # Dataset
     3    ctx.trigger("open_dataset", params=dict(name="..."))
     4    ctx.trigger("reload_dataset")  # refreshes the App
     5
     6    # View/sidebar
     7    ctx.trigger("set_view", params=dict(name="..."))  # saved view by name
     8    ctx.trigger("set_view", params=dict(view=view._serialize()))  # arbitrary view
     9    ctx.trigger("clear_view")
    10    ctx.trigger("clear_sidebar_filters")
    11
    12    # Selected samples
    13    ctx.trigger("set_selected_samples", params=dict(samples=[...]))
    14    ctx.trigger("clear_selected_samples")
    15
    16    # Selected labels
    17    ctx.trigger("set_selected_labels", params=dict(labels=[...]))
    18    ctx.trigger("clear_selected_labels")
    19
    20    # Panels
    21    ctx.trigger("open_panel", params=dict(name="Embeddings"))
    22    ctx.trigger("close_panel", params=dict(name="Embeddings"))
    

#### Generator execution#

If your operatorâs config declares that it is a generator via `execute_as_generator=True`, then its [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") method should `yield` calls to [`ctx.ops`](api__fiftyone.operators.operations.md#fiftyone.operators.operations.Operations "fiftyone.operators.operations.Operations") methods or [`ctx.trigger()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.trigger "fiftyone.operators.executor.ExecutionContext.trigger"), both of which trigger another operation and return a [`GeneratedMessage`](api__fiftyone.operators.message.md#fiftyone.operators.message.GeneratedMessage "fiftyone.operators.message.GeneratedMessage") instance containing the result of the invocation.

For example, a common generator pattern is to use the builtin `set_progress` operator to render a progress bar tracking the progress of an operation:
    
    
     1def execute(self, ctx):
     2    # render a progress bar tracking the execution
     3    for i in range(n):
     4        # [process a chunk here]
     5
     6        # Option 1: ctx.ops
     7        yield ctx.ops.set_progress(progress=i/n, label=f"Processed {i}/{n}")
     8
     9        # Option 2: ctx.trigger
    10        yield ctx.trigger(
    11            "set_progress",
    12            dict(progress=i/n, label=f"Processed {i}/{n}"),
    13        )
    

Note

Check out the [VoxelGPT plugin](https://github.com/voxel51/voxelgpt/blob/dfe23093485081fb889dbe18685587f4358a4438/__init__.py#L133) for a more sophisticated example of using generator execution to stream an LLMâs response to a panel.

### Delegated execution#

By default, operations are executed immediately after their inputs are provided in the App or they are triggered programmatically.

However, many interesting operations like model inference, embeddings computation, evaluation, and exports are computationally intensive and/or not suitable for immediate execution.

In such cases, [delegated operations](plugins__using_plugins.md#delegated-operations) come to the rescue by allowing users to schedule potentially long-running tasks that are executed in the background while you continue to use the App.

Note

[FiftyOne Enterprise](enterprise__plugins.md#enterprise-delegated-operations) deployments come out of the box with a connected compute cluster for executing delegated operations at scale.

In FiftyOne Open Source, you can use delegated operations at small scale by [running them locally](plugins__using_plugins.md#delegated-orchestrator-open-source).

There are a variety of options available for configuring whether a given operation should be delegated or executed immediately.

#### Execution options#

You can provide the optional properties described below in the operatorâs config to specify the available execution modes for the operator:
    
    
     1@property
     2def config(self):
     3    return foo.OperatorConfig(
     4        # Other parameters...
     5
     6        # Whether to allow immediate execution
     7        allow_immediate_execution=True/False,    # default True
     8
     9        # Whether to allow delegated execution
    10        allow_delegated_execution=True/False,    # default False
    11
    12        # Whether the default execution mode should be delegated, if both
    13        # options are available
    14        default_choice_to_delegated=True/False,  # default False
    15
    16        # Whether to resolve execution options dynamically when the
    17        # operator's inputs change. By default, this behavior will match
    18        # the operator's ``dynamic`` setting
    19        resolve_execution_options_on_change=True/False/None,  # default None
    20    )
    

When the operatorâs input form is rendered in the App, the `Execute|Schedule` button at the bottom of the modal will contextually show whether the operation will be executed immediately, scheduled for delegated execution, or allow the user to choose between the supported options if there are multiple:

![../_images/operator-execute-button.png](../_images/operator-execute-button.png)

#### Dynamic execution options#

Operators may also implement [`resolve_execution_options()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_execution_options "fiftyone.operators.operator.Operator.resolve_execution_options") to dynamically configure the available execution options based on the current execution context:
    
    
     1# Option 1: recommend delegation for larger views
     2def resolve_execution_options(self, ctx):
     3    should_delegate = len(ctx.view) > 1000
     4    return foo.ExecutionOptions(
     5        allow_immediate_execution=True,
     6        allow_delegated_execution=True,
     7        default_choice_to_delegated=should_delegate,
     8    )
     9
    10# Option 2: force delegation for larger views
    11def resolve_execution_options(self, ctx):
    12    delegate = len(ctx.view) > 1000
    13    return foo.ExecutionOptions(
    14        allow_immediate_execution=not delegate,
    15        allow_delegated_execution=delegate,
    16    )
    

If implemented, this method will override any static execution parameters included in the operatorâs config as described in the previous section.

#### Forced delegation#

Operators can implement [`resolve_delegation()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_delegation "fiftyone.operators.operator.Operator.resolve_delegation") to force a particular operation to be delegated (by returning `True`) or executed immediately (by returning `False`) based on the current execution context.

For example, you could decide whether to delegate execution based on the size of the current view:
    
    
    1def resolve_delegation(self, ctx):
    2    # Force delegation for large views and immediate execution for small views
    3    return len(ctx.view) > 1000
    

If [`resolve_delegation()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_delegation "fiftyone.operators.operator.Operator.resolve_delegation") is not implemented or returns `None`, then the choice of execution mode is deferred to the prior mechanisms described above.

#### Reporting progress#

Delegated operations can report their execution progress by calling [`set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") on their execution context from within [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute"):
    
    
     1import fiftyone as fo
     2import fiftyone.core.storage as fos
     3import fiftyone.core.utils as fou
     4
     5def execute(self, ctx):
     6    images_dir = ctx.params["images_dir"]
     7
     8    filepaths = fos.list_files(images_dir, abs_paths=True, recursive=True)
     9
    10    num_added = 0
    11    num_total = len(filepaths)
    12    for batch in fou.iter_batches(filepaths, 100):
    13        samples = [fo.Sample(filepath=f) for f in batch]
    14        ctx.dataset.add_samples(samples)
    15
    16        num_added += len(batch)
    17        ctx.set_progress(progress=num_added / num_total)
    

Note

[FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise) users can view the current progress of their delegated operations from the [Runs page](enterprise__plugins.md#enterprise-managing-delegated-operations).

For your convenience, all builtin methods of the FiftyOne SDK that support rendering progress bars provide an optional `progress` method that you can use trigger calls to [`set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") using the pattern show below:
    
    
     1import fiftyone as fo
     2
     3def execute(self, ctx):
     4    images_dir = ctx.params["images_dir"]
     5
     6    # Custom logic that controls how progress is reported
     7    def set_progress(pb):
     8        if pb.complete:
     9            ctx.set_progress(progress=1, label="Operation complete")
    10        else:
    11            ctx.set_progress(progress=pb.progress)
    12
    13    # Option 1: report progress every five seconds
    14    progress = fo.report_progress(set_progress, dt=5.0)
    15
    16    # Option 2: report progress at 10 equally-spaced increments
    17    # progress = fo.report_progress(set_progress, n=10)
    18
    19    ctx.dataset.add_images_dir(images_dir, progress=progress)
    

You can also use the builtin [`ProgressHandler`](api__fiftyone.operators.md#fiftyone.operators.ProgressHandler "fiftyone.operators.ProgressHandler") class to automatically forward logging messages to [`set_progress()`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.set_progress "fiftyone.operators.executor.ExecutionContext.set_progress") as `label` values using the pattern shown below:
    
    
     1import logging
     2import fiftyone.operators as foo
     3import fiftyone.zoo as foz
     4
     5def execute(self, ctx):
     6    name = ctx.params["name"]
     7
     8    # Automatically report all `fiftyone` logging messages
     9    with foo.ProgressHandler(ctx, logger=logging.getLogger("fiftyone")):
    10        foz.load_zoo_dataset(name, persistent=True)
    

### Distributed execution **NEW**#

Added in version 1.8.0.

In FiftyOne Enterprise, delegated operations can be [distributed across multiple workers](enterprise__plugins.md#enterprise-distributed-execution) to accelerate computation on large datasets.

Distributed execution is not available in FiftyOne Open Source, but plugin authors can still utilize the distributed execution paradigm described here so that their operators can be executed in a distributed fashion when used in FiftyOne Enterprise. When an operator that supports distributed execution is used in FiftyOne Open Source, its [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method will simply be called exactly once with the full target view on which the operator was invoked.

#### Supporting distributed execution#

To declare that an operator supports distributed execution, simply set `allow_distributed_execution=True` in the operatorâs config:
    
    
     1@property
     2def config(self):
     3    return foo.OperatorConfig(
     4        name="my_distributed_operator",
     5        label="My distributed operator",
     6        ...
     7
     8        # Declare support for distributed execution
     9        allow_delegated_execution=True,
    10        allow_distributed_execution=True,
    11    )
    

At runtime, a distributed operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method is called one or more times, each with a different `ctx.view` that encodes the specific samples that should be processed in that batch:
    
    
    1 def execute(self, ctx):
    2     # Use `ctx.view` as the basis for your computation
    3     for sample in ctx.view:
    4         ...
    

The number of batches is [chosen](enterprise__plugins.md#enterprise-distributed-execution) by the user who schedules a distributed execution. The user may also opt _not_ to use distributed execution, in which case [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") is called exactly once. Any necessary batching is automatically handled by FiftyOneâs scheduling engine.

Warning

Since distributed operators are executed multiple times, each on a subset of the data, in any order, the operator cannot perform any pre or post processing outside of the current batch. To do this you must use an operator pipeline.

#### Supporting target views#

If your operator uses the target view pattern, then you should use [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view") instead of `ctx.view` in the operatorâs [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method to ensure that non-distributed execution continues to work as expected:
    
    
    1 def execute(self, ctx):
    2     # Use `ctx.target_view()` as the basis for your computation
    3     for sample in ctx.target_view():
    4         ...
    

Why is this? When the user chooses distribution execution, [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view") and `ctx.view` are equivalent; both encode the specific samples to process in the current batch. However, if the user opts for non-distributed execution, then [`ctx.target_view()`](api__fiftyone.operators.md#fiftyone.operators.ExecutionContext.target_view "fiftyone.operators.ExecutionContext.target_view") must be used as the user may have chosen a target view other than the current `ctx.view`.

### Operator pipelines **NEW**#

Added in version 1.10.0.

In addition to developing individual operators, [FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise) allows you to define a linear composition of regular operators into a single **operator pipeline**. An operator pipeline acts as a single, higher-level operation composed of multiple discrete **stages** , where each stage is a call to another operator.

Note

Currently, **Operator Pipelines** are only supported for **delegated** **execution** within FiftyOne Enterprise. Immediate execution or use in FiftyOne Open Source is not supported for this feature.

#### Defining a pipeline operator#

To define an operator that executes a pipeline, you must subclass [`PipelineOperator`](api__fiftyone.operators.md#fiftyone.operators.PipelineOperator "fiftyone.operators.PipelineOperator") instead of the typical base [`Operator`](api__fiftyone.operators.md#fiftyone.operators.Operator "fiftyone.operators.Operator").

A `PipelineOperator` is structured similarly to a regular operator, but replaces the standard [`execute()`](api__fiftyone.operators.md#fiftyone.operators.Operator.execute "fiftyone.operators.Operator.execute") method with a required method in which you define the pipelineâs stages: [`resolve_pipeline()`](api__fiftyone.operators.md#fiftyone.operators.PipelineOperator.resolve_pipeline "fiftyone.operators.PipelineOperator.resolve_pipeline").

[`resolve_input()`](api__fiftyone.operators.md#fiftyone.operators.Operator.resolve_input "fiftyone.operators.Operator.resolve_input") can also be implemented to define user inputs for the pipeline operator. In this case, any inputs defined will be available to the `resolve_pipeline()` method via `ctx.params`, for configuring the pipelineâs stages.

Additionally, any stage can be a distributed operator to provide fan-out capability to the pipeline.

This diagram shows an example of an operator pipeline with three stages:

  1. Initialization

  2. Distributed processing of data

  3. Finalization/cleanup




Note that if Stage 1 or Stage 2 fails, Stage 3 will still run because it is marked with `always_run=True`.

![../_images/pipeline-operator.png](../_images/pipeline-operator.png)

#### Pipeline components#

The pipeline is constructed using core classes from [`fiftyone.operators.types`](api__fiftyone.operators.types.md#module-fiftyone.operators.types "fiftyone.operators.types").

##### [`fiftyone.operators.types.Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline")#

The top-level container for the stages, which `resolve_pipeline()` must return. The two ways to create a pipeline are:

  1. Instantiate an empty pipeline and add stages via [`stage()`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline.stage "fiftyone.operators.types.Pipeline.stage")

  2. Instantiate a pipeline with an initial list of stages via the [`Pipeline`](api__fiftyone.operators.types.md#fiftyone.operators.types.Pipeline "fiftyone.operators.types.Pipeline") constructor




##### [`fiftyone.operators.types.PipelineStage`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage "fiftyone.operators.types.PipelineStage")#

Represents a single step in the pipeline, which is an invocation of a regular operator.

#### Example pipeline operators#

This example code shows how to define the pipeline operator shown and described above.
    
    
    import fiftyone.operators as foo
    import fiftyone.operators.types as types
    
    class PipelineOp(foo.PipelineOperator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="my_pipeline_op",
                label="My Example Pipeline",
                # Must allow delegation, immediate is not supported for pipelines
                allow_delegated_execution=True,
                allow_immediate_execution=False,
                allow_distributed_execution=True,
            )
    
        def resolve_input(self, ctx):
            # Define inputs for the top-level pipeline operator
            inputs = types.Object()
            inputs.view_target(ctx)
            inputs.str(name="a_str", label="A string input", default="default")
            return types.Property(inputs)
    
        def resolve_pipeline(self, ctx):
            """
            Required method that defines the pipeline's stages.
            Returns:
                a `types.Pipeline` instance.
            """
            pipeline = types.Pipeline([
                # Stage 1: Initialization
                types.PipelineStage(
                    operator_uri="@my-plugin/my_stage1",
                    name="Initialization",
                    params=ctx.params,  # pass top-level inputs straight through
                )
    
                # Stage 2: Distributed work, leveraging ctx.num_distributed_tasks
                types.PipelineStage(
                    operator_uri="@my-plugin/my_stage2_distr",
                    name="Process Data",
                    num_distributed_tasks=ctx.num_distributed_tasks,
                    params={"some_param": "some_value"}, # custom params for stage 2
                )
    
                # Stage 3: Finalization/Cleanup
                types.PipelineStage(
                    operator_uri="@my-plugin/my_stage3_cleanup",
                    name="Finalization",
                    always_run=True, # Runs even if Stage 1 or 2 fails
                    # no params passed
                )
            ])
    
            return pipeline
    

We can even dynamically configure the pipelineâs stages based on user inputs or other aspects of the execution context. For example, this is a pipeline approximating the functionality of [`compute_visualization()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_visualization "fiftyone.brain.compute_visualization"). It also showcases the alternative pipeline creation syntax.
    
    
    import fiftyone.operators as foo
    import fiftyone.operators.types as types
    
    class ComputeVisualizationPipeline(foo.PipelineOperator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="compute_viz_pipeline",
                label="Compute Visualization Pipeline",
                allow_delegated_execution=True,
                allow_immediate_execution=False,
                allow_distributed_execution=True,
            )
    
        def resolve_input(self, ctx):
            # Define inputs for the top-level pipeline operator
            inputs = types.Object()
            inputs.view_target(ctx)
            inputs.bool(
                name="force_compute_embeddings",
                label="Force compute embeddings?",
                default=False
            )
    
            ... # other inputs
    
            return types.Property(inputs)
    
        def resolve_pipeline(self, ctx):
            pipeline = types.Pipeline()
            view = ctx.target_view()
    
            # Compute embeddings first if the view doesn't have them or
            #   user told us to force it
            if ctx.params.get(
                "force_compute_embeddings", False
            ) or not has_embeddings(view):
                pipeline.stage(
                    operator_uri="@my-plugin/compute_embeddings",
                    name="Compute Embeddings",
                    num_distributed_tasks=ctx.num_distributed_tasks,
                    params=_get_compute_embeddings_params(ctx.params),
                )
    
            # Perform dimensionality reduction on embeddings
            pipeline.stage(
                operator_uri="@my-plugin/dimensionality_reduction",
                name="Reduce to 2 Dimensions",
                num_distributed_tasks=ctx.num_distributed_tasks,
                params=_get_dimensionality_reduction_params(ctx.params),
            )
    
            # Create a plot from the viz field and upload to a cloud bucket
            pipeline.stage(
                operator_uri="@my-plugin/generate_plot",
                name="Generate Plot and Upload",
                params={
                    "visualization_field": ctx.params.get("visualization_field"),
                    "cloud_path": ctx.params.get("cloud_path"),
                },
            )
    
            return pipeline
    

#### Execution context for stages#

When a standard operator is executed as a stage within a pipeline, its execution context is augmented with the **`ctx.pipeline`** property.

This field is an instance of [`PipelineExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.PipelineExecutionContext "fiftyone.operators.executor.PipelineExecutionContext") which provides information about the overall pipeline execution to the current stage operator.

The stage operator can use this context for conditional logic, such as performing a cleanup action:
    
    
    def execute(self, ctx):
        if not ctx.pipeline.active:
            # This stage is running because an earlier stage failed
            print(f"Running cleanup after failure: {ctx.pipeline.error or 'unknown error'}")
    
        # ... normal stage logic
    

#### Overriding request parameters per stage#

By default, each stage in a pipeline inherits the same execution context as the top-level pipeline operator â including its `view`, `view_name`, and other request parameters.

Use `request_params_overrides` on a [`PipelineStage`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage "fiftyone.operators.types.PipelineStage") to give a specific stage a different execution context. Any key you include in `request_params_overrides` will shadow the corresponding value from the top-level request for that stage only; all other stages are unaffected.

Commonly overridden parameters include:

  * `view` â a [`DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") to apply (serialized automatically), or `None` to clear any active view

  * `view_name` â the name of a saved view to use

  * `selected` â a list of selected sample IDs

  * `group_slice` â the group slice to use




Note

Do **not** include `params` inside `request_params_overrides`. Use the `params` field of [`PipelineStage`](api__fiftyone.operators.types.md#fiftyone.operators.types.PipelineStage "fiftyone.operators.types.PipelineStage") directly for operator parameters.

Note

The following parameters cannot be overridden per stage and will be ignored if included: `dataset_id`, `dataset_name`, `delegated`, `delegation_target`, `request_delegation`, `results`.
    
    
    import fiftyone.operators as foo
    import fiftyone.operators.types as types
    
    class MultiViewPipeline(foo.PipelineOperator):
        @property
        def config(self):
            return foo.OperatorConfig(
                name="multi_view_pipeline",
                label="Multi-View Pipeline",
                allow_delegated_execution=True,
                allow_immediate_execution=False,
            )
    
        def resolve_pipeline(self, ctx):
            pipeline = types.Pipeline()
    
            # Stage 1 runs against the view the user has open
            pipeline.stage(
                operator_uri="@my-plugin/compute_stats",
                name="Stats on current view",
                params={"field": "predictions"},
            )
    
            # Stage 2 runs against a different saved view
            pipeline.stage(
                operator_uri="@my-plugin/compute_stats",
                name="Stats on val split",
                params={"field": "predictions"},
                request_params_overrides={"view_name": "val_split"},
            )
    
            # Stage 3 runs against the full dataset (no view applied)
            pipeline.stage(
                operator_uri="@my-plugin/compute_stats",
                name="Stats on full dataset",
                params={"field": "predictions"},
                request_params_overrides={"view": None, "view_name": None},
            )
    
            # Stage 4 runs against a programmatic slice of the current view,
            # useful for manual batching
            batch = ctx.view[:100]
            pipeline.stage(
                operator_uri="@my-plugin/compute_stats",
                name="Stats on first 100 samples",
                params={"field": "predictions"},
                request_params_overrides={"view": batch},
            )
    
            return pipeline
    

### Accessing secrets#

Some plugins may require sensitive information such as API tokens and login credentials in order to function. Any secrets that a plugin requires are in its fiftyone.yml.

For example, the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/annotation/fiftyone.yml) plugin declares the following secrets:
    
    
    1secrets:
    2  - FIFTYONE_CVAT_URL
    3  - FIFTYONE_CVAT_USERNAME
    4  - FIFTYONE_CVAT_PASSWORD
    5  - FIFTYONE_CVAT_EMAIL
    6  - FIFTYONE_LABELBOX_URL
    7  - FIFTYONE_LABELBOX_API_KEY
    8  - FIFTYONE_LABELSTUDIO_URL
    9  - FIFTYONE_LABELSTUDIO_API_KEY
    

As the naming convention implies, any necessary secrets are provided by users by setting environment variables with the appropriate names. For example, if you want to use the CVAT backend with the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/annotation/fiftyone.yml) plugin, you would set:
    
    
    FIFTYONE_CVAT_URL=...
    FIFTYONE_CVAT_USERNAME=...
    FIFTYONE_CVAT_PASSWORD=...
    FIFTYONE_CVAT_EMAIL=...
    

At runtime, the pluginâs execution context is automatically hydrated with any available secrets that are declared by the plugin. Operators can access these secrets via the `ctx.secrets` dict:
    
    
    1def execute(self, ctx):
    2   url = ctx.secrets["FIFTYONE_CVAT_URL"]
    3   username = ctx.secrets["FIFTYONE_CVAT_USERNAME"]
    4   password = ctx.secrets["FIFTYONE_CVAT_PASSWORD"]
    5   email = ctx.secrets["FIFTYONE_CVAT_EMAIL"]
    

### Importing modules#

When your plugin has multiple Python files, you can import between them using absolute imports based on your pluginâs name.

Plugin names map to Python module namespaces under `fiftyone.plugins.orgs`:

Plugin name | Module namespace  
---|---  
`@myorg/my-plugin` | `fiftyone.plugins.orgs.myorg.my_plugin`  
`my-plugin` | `fiftyone.plugins.orgs.external.my_plugin`  
  
Note

Plugins without an organization prefix are placed under the `external` namespace.

Names are automatically sanitized: hyphens become underscores and `PascalCase` becomes `snake_case`.

For example, if your plugin `@myorg/my-plugin` has this structure:
    
    
    my-plugin/
        fiftyone.yml
        __init__.py
        utils.py
        models/
            __init__.py
            classifier.py
    

You can import modules using absolute paths:
    
    
    1# In __init__.py
    2from fiftyone.plugins.orgs.myorg.my_plugin.utils import helper
    3from fiftyone.plugins.orgs.myorg.my_plugin.models import classifier
    4
    5# In models/classifier.py
    6from fiftyone.plugins.orgs.myorg.my_plugin.utils import helper
    

Relative imports also work:
    
    
    # In __init__.py
    from .utils import helper
    from .models import classifier
    

Warning

These module paths are for **internal plugin use only**. External code should not import plugin modules directly, as the namespace is created dynamically when FiftyOne loads the plugin. To run plugin code from external scripts, use the [operator execution API](plugins__using_plugins.md#using-operators).

### Operator outputs#

Operators can optionally implement [`resolve_output()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_output "fiftyone.operators.operator.Operator.resolve_output") to define read-only output forms that are presented to the user as a modal in the App after the operatorâs execution completes.

The basic objective of [`resolve_output()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_output "fiftyone.operators.operator.Operator.resolve_output") is to define properties that describe how to render the values in `ctx.results` for the user. As with input forms, you can use the [`fiftyone.operators.types`](api__fiftyone.operators.types.md#module-fiftyone.operators.types "fiftyone.operators.types") module to define the output properties.

For example, the output form below renders the number of samples (`count`) computed during the operatorâs execution:
    
    
     1def execute(self, ctx):
     2    # computation here...
     3
     4    return {"count": count}
     5
     6def resolve_output(self, ctx):
     7    outputs = types.Object()
     8    outputs.int(
     9        "count",
    10        label="Count",
    11        description=f"The number of samples in the current {target}",
    12    )
    13    return types.Property(outputs)
    

Note

All properties in output forms are implicitly rendered as read-only.

### Operator placement#

By default, operators are only accessible from the [operator browser](plugins__using_plugins.md#using-operators). However, you can place a custom button, icon, menu item, etc. in the App that will trigger the operator when clicked in any location supported by the [`types.Places`](api__fiftyone.operators.types.md#fiftyone.operators.types.Places "fiftyone.operators.types.Places") enum.

For example, you can use:

  * `types.Places.SAMPLES_GRID_ACTIONS`

![../_images/samples_grid_actions.png](../_images/samples_grid_actions.png)
  * `types.Places.SAMPLES_GRID_SECONDARY_ACTIONS`

![../_images/samples_grid_secondary_actions.png](../_images/samples_grid_secondary_actions.png)
  * `types.Places.SAMPLES_VIEWER_ACTIONS`

![../_images/samples_viewer_actions.png](../_images/samples_viewer_actions.png)
  * `types.Places.EMBEDDINGS_ACTIONS`

![../_images/embeddings_actions.png](../_images/embeddings_actions.png)
  * `types.Places.HISTOGRAM_ACTIONS`

![../_images/histograms_actions.png](../_images/histograms_actions.png)
  * `types.Places.MAP_ACTIONS`

![../_images/map_actions.png](../_images/map_actions.png)



  
You can add a placement for an operator by implementing the [`resolve_placement()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.resolve_placement "fiftyone.operators.operator.Operator.resolve_placement") method as demonstrated below:
    
    
     1import fiftyone.operators as foo
     2import fiftyone.operators.types as types
     3
     4class OpenHistogramsPanel(foo.Operator):
     5    @property
     6    def config(self):
     7        return foo.OperatorConfig(
     8            name="open_histograms_panel",
     9            label="Open histograms panel"
    10        )
    11
    12    def resolve_placement(self, ctx):
    13        return types.Placement(
    14            types.Places.SAMPLES_GRID_SECONDARY_ACTIONS,
    15            types.Button(
    16                label="Open Histograms Panel",
    17                icon="/assets/histograms.svg",
    18                prompt=False,
    19            )
    20        )
    21
    22    def execute(self, ctx):
    23        return ctx.ops.open_panel("Histograms", layout="horizontal", is_active=True)
    24
    25def register(p):
    26    p.register(OpenHistogramsPanel)
    
    
    
     1import {
     2    Operator,
     3    OperatorConfig,
     4    registerOperator,
     5    useOperatorExecutor,
     6    types,
     7} from "@fiftyone/operators";
     8
     9const PLUGIN_NAME = "@my/plugin";
    10
    11class OpenEmbeddingsPanel extends Operator {
    12    get config() {
    13        return new OperatorConfig({
    14            name: "open_embeddings_panel",
    15            label: "Open embeddings panel",
    16        });
    17    }
    18
    19    useHooks() {
    20        const openPanelOperator = useOperatorExecutor("open_panel");
    21        return { openPanelOperator };
    22    }
    23
    24    async resolvePlacement() {
    25        return new types.Placement(
    26            types.Places.SAMPLES_GRID_SECONDARY_ACTIONS,
    27            new types.Button({
    28                label: "Open embeddings panel",
    29                icon: "/assets/embeddings.svg",
    30            })
    31        );
    32    }
    33
    34    async execute({ hooks }) {
    35        const { openPanelOperator } = hooks;
    36        openPanelOperator.execute({
    37            name: "Embeddings",
    38            isActive: true,
    39            layout: "horizontal",
    40        });
    41    }
    42}
    43
    44registerOperator(OpenEmbeddingsPanel, PLUGIN_NAME);
    

## Developing panels#

Panels are miniature full-featured data applications that you can open in [App spaces](user_guide__app.md#app-spaces) and interactively manipulate to explore your dataset and update/respond to updates from other spaces that are currently open in the App.

Panels can be defined in either Python or JS, and FiftyOne comes with a number of builtin panels for common tasks.

Panels can be scoped to the Appâs grid view or modal view via their config. Grid panels enable extensibility at the macro level, allowing you to work with entire datasets or views, while modal panels provide extensibility at the micro level, focusing on individual samples and scenarios.

Panels, like operators, can make use of the [`fiftyone.operators.types`](api__fiftyone.operators.types.md#module-fiftyone.operators.types "fiftyone.operators.types") module and the [`@fiftyone/operators`](plugins__api__plugins.fiftyone.operators.md#module-fiftyone-operators "@fiftyone/operators") package, which define a rich builtin type system that panel developers can use to implement the layout and associated events that define the panel.

Panels can trigger both Python and JS operators, either programmatically or by interactively launching a prompt that users can fill out to provide the necessary parameters for the operatorâs execution. This powerful composability allows panels to define interactive workflows that guide the user through executing workflows on their data and then interactively exploring and analyzing the results of the computation.

Panels can also interact with other components of the App, such as responding to changes in (or programmatically updating) the current dataset, view, current selection, or active sample in the modal.

### Panel interface#

The code block below describes the Python interface for defining panels. Weâll dive into each component of the interface in more detail in the subsequent sections.

Note

See this section for more information on developing panels in JS.
    
    
      1import fiftyone.operators as foo
      2import fiftyone.operators.types as types
      3
      4class ExamplePanel(foo.Panel):
      5    @property
      6    def config(self):
      7        return foo.PanelConfig(
      8            # The panel's URI: f"{plugin_name}/{name}"
      9            name="example_panel",  # required
     10
     11            # The display name of the panel in the "+" menu
     12            label="Example panel",  # required
     13
     14            # Custom icons to use in the "+"" menu
     15            # Can be a URL, a local path in the plugin directory, or the
     16            # name of a MUI icon: https://marella.me/material-icons/demo
     17            icon="/assets/icon.svg",
     18            light_icon="developer_mode",  # light theme only
     19            dark_icon="developer_mode",  # dark theme only
     20
     21            # Whether to allow multiple instances of the panel to be opened
     22            allow_multiple=False,
     23
     24            # Whether the panel should be available in the grid, modal, or both
     25            # Possible values: "grid", "modal", "grid modal"
     26            surfaces="grid",  # default = "grid"
     27
     28            # Markdown-formatted text that describes the panel. This is
     29            # rendered in a tooltip when the help icon in the panel
     30            # title is hovered over
     31            help_markdown="A description of the panel",
     32        )
     33
     34    def render(self, ctx):
     35        """Implement this method to define your panel's layout and events.
     36
     37        This method is called after every panel event is executed (panel
     38        load, button callback, context change event, etc).
     39
     40        Returns:
     41            a `types.Property` defining the panel's components
     42        """
     43        panel = types.Object()
     44
     45        brain_keys = ctx.panel.get_state("brain_keys", [])
     46
     47        # Define a menu of actions for the panel
     48        menu = panel.menu("menu", variant="square", color="51")
     49        menu.enum(
     50            "brain_key",
     51            label="Choose a brain key",  # placeholder text
     52            values=brain_keys,
     53            on_change=self.on_change_brain_key,  # custom event callback
     54        )
     55        menu.btn(
     56            "learn_more",
     57            label="Learn more",  # tooltip text
     58            icon="help",  # material UI icon
     59            on_click=self.on_click_learn_more,  # custom event callback
     60        )
     61
     62        # Define components that appear in the panel's main body
     63        panel.str("event", label="The last event", view=types.LabelValueView())
     64        panel.obj(
     65            "event_data", label="The last event data", view=types.JSONView()
     66        )
     67
     68        # Display a checkbox to toggle between plot and compute visualization button
     69        show_compute_visualization_btn = ctx.panel.get_state(
     70            "show_start_button", True
     71        )
     72        panel.bool(
     73            "show_start_button",
     74            label="Show compute visualization button",
     75            on_change=self.on_change_show_start_button,
     76        )
     77
     78        # You can use conditional logic to dynamically change the layout
     79        # based on the current panel state
     80        if show_compute_visualization_btn:
     81            # Define a button with a custom on click event
     82            panel.btn(
     83                "start",
     84                label="Compute visualization",  # button text
     85                on_click=self.on_click_start,  # custom event callback
     86                variant="contained",  # button style
     87            )
     88        else:
     89            # Define an interactive plot with custom callbacks
     90            panel.plot(
     91                "embeddings",
     92                config={},  # plotly config
     93                layout={},  # plotly layout config
     94                on_selected=self.on_selected_embeddings,  # custom event callback
     95                height="400px",
     96            )
     97
     98        return types.Property(
     99            panel, view=types.GridView(orientation="vertical")
    100        )
    101
    102    #######################################################################
    103    # Builtin events
    104    #######################################################################
    105
    106    def on_load(self, ctx):
    107        """Implement this method to set panel state/data when the panel
    108        initially loads.
    109        """
    110        event = {
    111            "data": None,
    112            "description": "the panel is loaded",
    113        }
    114        ctx.panel.set_state("event", "on_load")
    115        ctx.panel.set_data("event_data", event)
    116
    117        # Get the list of brain keys to populate `brain_key` dropdown
    118        visualization_keys = ctx.dataset.list_brain_runs("visualization")
    119        ctx.panel.set_state("brain_keys", visualization_keys)
    120
    121        # Show compute visualization button by default
    122        ctx.panel.set_state("show_start_button", True)
    123
    124    def on_unload(self, ctx):
    125        """Implement this method to set panel state/data when the panel is
    126        being closed.
    127        """
    128        event = {
    129            "data": None,
    130            "description": "the panel is unloaded",
    131        }
    132        ctx.panel.set_state("event", "on_unload")
    133        ctx.panel.set_data("event_data", event)
    134
    135    def on_change_ctx(self, ctx):
    136        """Implement this method to set panel state/data when any aspect
    137        of the execution context (view, selected samples, filters, etc.) changes.
    138
    139        The current execution context will be available via ``ctx``.
    140        """
    141        event = {
    142            "data": {
    143                "view": ctx.view._serialize(),
    144                "selected": ctx.selected,
    145                "has_custom_view": ctx.has_custom_view,
    146            },
    147            "description": "the current ExecutionContext",
    148        }
    149        ctx.panel.set_state("event", "on_change_ctx")
    150        ctx.panel.set_data("event_data", event)
    151
    152    def on_change_dataset(self, ctx):
    153        """Implement this method to set panel state/data when the current
    154        dataset is changed.
    155
    156        The new dataset will be available via ``ctx.dataset``.
    157        """
    158        event = {
    159            "data": ctx.dataset.name,
    160            "description": "the current dataset name",
    161        }
    162        ctx.panel.set_state("event", "on_change_dataset")
    163        ctx.panel.set_data("event_data", event)
    164
    165    def on_change_view(self, ctx):
    166        """Implement this method to set panel state/data when the current
    167        view is changed.
    168
    169        The new view will be available via ``ctx.view``.
    170        """
    171        event = {
    172            "data": ctx.view._serialize(),
    173            "description": "the current view",
    174        }
    175        ctx.panel.set_state("event", "on_change_view")
    176        ctx.panel.set_data("event_data", event)
    177
    178    def on_change_spaces(self, ctx):
    179        """Implement this method to set panel state/data when the current
    180        spaces layout changes.
    181
    182        The current spaces layout will be available via ``ctx.spaces``.
    183        """
    184        event = {
    185            "data": ctx.spaces,
    186            "description": "the current spaces layout",
    187        }
    188        ctx.panel.set_state("event", "on_change_spaces")
    189        ctx.panel.set_data("event_data", event)
    190
    191    def on_change_current_sample(self, ctx):
    192        """Implement this method to set panel state/data when a new sample
    193        is loaded in the Sample modal.
    194
    195        The ID of the new sample will be available via
    196        ``ctx.current_sample``.
    197        """
    198        event = {
    199            "data": ctx.current_sample,
    200            "description": "the current sample",
    201        }
    202        ctx.panel.set_state("event", "on_change_current_sample")
    203        ctx.panel.set_data("event_data", event)
    204
    205    def on_change_selected(self, ctx):
    206        """Implement this method to set panel state/data when the current
    207        selection changes (eg in the Samples panel).
    208
    209        The IDs of the current selected samples will be available via
    210        ``ctx.selected``.
    211        """
    212        event = {
    213            "data": ctx.selected,
    214            "description": "the current selection",
    215        }
    216        ctx.panel.set_state("event", "on_change_selected")
    217        ctx.panel.set_data("event_data", event)
    218
    219    def on_change_selected_labels(self, ctx):
    220        """Implement this method to set panel state/data when the current
    221        selected labels change (eg in the Sample modal).
    222
    223        Information about the current selected labels will be available
    224        via ``ctx.selected_labels``.
    225        """
    226        event = {
    227            "data": ctx.selected_labels,
    228            "description": "the current selected labels",
    229        }
    230        ctx.panel.set_state("event", "on_change_selected_labels")
    231        ctx.panel.set_data("event_data", event)
    232
    233    def on_change_active_fields(self, ctx):
    234        """Implement this method to set panel state/data when the current
    235        active fields change in the sidebar.
    236
    237        The active fields will be available via ``ctx.active_fields``.
    238        """
    239        event = {
    240            "data": ctx.active_fields,
    241            "description": "the current active fields",
    242        }
    243        ctx.panel.set_state("event", "on_change_active_fields")
    244        ctx.panel.set_data("event_data", event)
    245
    246    def on_change_extended_selection(self, ctx):
    247        """Implement this method to set panel state/data when the current
    248        extended selection changes.
    249
    250        The IDs of the current extended selection will be available via
    251        ``ctx.extended_selection``.
    252        """
    253        event = {
    254            "data": ctx.extended_selection,
    255            "description": "the current extended selection",
    256        }
    257        ctx.panel.set_state("event", "on_change_extended_selection")
    258        ctx.panel.set_data("event_data", event)
    259
    260    def on_change_group_slice(self, ctx):
    261        """Implement this method to set panel state/data when the current
    262        group slice changes.
    263
    264        The current group slice will be available via ``ctx.group_slice``.
    265        """
    266        event = {
    267            "data": ctx.group_slice,
    268            "description": "the current group slice",
    269        }
    270        ctx.panel.set_state("event", "on_change_group_slice")
    271        ctx.panel.set_data("event_data", event)
    272
    273    #######################################################################
    274    # Custom events
    275    # These events are defined by user code above and, just like builtin
    276    # events, take `ctx` as input and are followed by a call to render()
    277    #######################################################################
    278
    279    def on_change_brain_key(self, ctx):
    280        # Load expensive content based on current `brain_key`
    281        brain_key = ctx.panel.get_state("menu.brain_key")
    282        results = ctx.dataset.load_brain_results(brain_key)
    283
    284        # Format results for plotly
    285        x, y = zip(*results.points.tolist())
    286        ids = results.sample_ids
    287
    288        plot_data = [
    289            {"x": x, "y": y, "ids": ids, "type": "scatter", "mode": "markers"}
    290        ]
    291
    292        # Store large content as panel data for efficiency
    293        ctx.panel.set_data("embeddings", plot_data)
    294
    295        # Show plot with embeddings data instead of the compute visualization button
    296        ctx.panel.set_state("show_start_button", False)
    297
    298    def on_click_start(self, ctx):
    299        # Launch an interactive prompt for user to execute an operator
    300        ctx.prompt("@voxel51/brain/compute_visualization")
    301
    302        # Lightweight state update
    303        ctx.panel.set_state("show_start_button", False)
    304
    305    def on_click_learn_more(self, ctx):
    306        # Trigger a builtin operation via `ctx.ops`
    307        url = "https://docs.voxel51.com/plugins/developing_plugins.html"
    308        ctx.ops.notify(f"Check out {url} for more information")
    309
    310    def on_selected_embeddings(self, ctx):
    311        # Get selected points from event params
    312        selected_points = ctx.params.get("data", [])
    313        selected_sample_ids = [d.get("id", None) for d in selected_points]
    314
    315        # Conditionally trigger a builtin operation via `ctx.ops`
    316        if len(selected_sample_ids) > 0:
    317            ctx.ops.set_extended_selection(selected_sample_ids)
    318
    319    def on_change_show_start_button(self, ctx):
    320        # Get current state of the checkbox on change
    321        current_state = ctx.params.get("value", None)
    322
    323def register(p):
    324    """Always implement this method and register() each panel that your
    325    plugin defines.
    326    """
    327    p.register(ExamplePanel)
    

![../_images/example-panel-inline.gif](../_images/example-panel-inline.gif)

Note

Remember that you must also include the panelâs name in the pluginâs fiftyone.yml:
    
    
    panels:
      - example_panel
    

### Panel config#

Every panel must define a [`config`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.config "fiftyone.operators.panel.Panel.config") property that defines its name, display name, surfaces, and other optional metadata about its behavior:
    
    
     1@property
     2def config(self):
     3    return foo.PanelConfig(
     4        # The panel's URI: f"{plugin_name}/{name}"
     5        name="example_panel",  # required
     6
     7        # The display name of the panel in the "+" menu
     8        label="Example panel",  # required
     9
    10        # Custom icons to use in the "+"" menu
    11        # Can be a URL, a local path in the plugin directory, or the
    12        # name of a MUI icon: https://marella.me/material-icons/demo
    13        icon="/assets/icon.svg",
    14        light_icon="/assets/icon-light.svg",  # light theme only
    15        dark_icon="/assets/icon-dark.svg",  # dark theme only
    16
    17        # Whether to allow multiple instances of the panel to be opened
    18        allow_multiple=False,
    19
    20        # Whether the panel should be available in the grid, modal, or both
    21        # Possible values: "grid", "modal", "grid modal"
    22        surfaces="grid",  # default = "grid"
    23
    24        # Markdown-formatted text that describes the panel. This is
    25        # rendered in a tooltip when the help icon in the panel
    26        # title is hovered over
    27        help_markdown="A description of the panel",
    28    )
    

The `surfaces` key defines the panelâs scope:

  * Grid panels can be accessed from the `+` button in the Appâs [grid view](user_guide__app.md#app-fields-sidebar), which allows you to build macro experiences that work with entire datasets or views

  * Modal panels can be accessed from the `+` button in the Appâs [modal view](user_guide__app.md#app-sample-view), which allows you to build interactions that focus on individual samples and scenarios




Note

For an example of a modal panel, refer to the [label count panel](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/label_count).

### Execution context#

An [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") is passed to each of the panelâs methods at runtime. This `ctx` contains static information about the current state of the App (dataset, view, panel, selection, etc) as well as dynamic information about the panelâs current state and data.

See this section for a full description of the execution context.

### Panel state and data#

Panels provide two mechanisms for persisting information: panel state and panel data.

#### Basic structure#

Panel state can be accessed and updated via `ctx.panel.state`, and panel data can be updated (but not accessed) via `ctx.panel.data`.

Under the hood, panel state and data is merged into a single nested object that maps 1-1 to the structure and naming of the properties defined by the panelâs [`render()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.render "fiftyone.operators.panel.Panel.render") method.

The example code below shows how to access and update panel state.

Note

Since panel state and panel data are merged into a single object, it is important to avoid naming conflicts between state and data keys. If a key is present in both panel state and data, the value in _panel data_ will be used.
    
    
     1class CounterPanel(foo.Panel):
     2    @property
     3    def config(self):
     4        return foo.PanelConfig(
     5            name="counter_panel", label="Counter Panel", icon="123"
     6        )
     7
     8    def on_load(self, ctx):
     9        ctx.panel.state.v_stack = {"h_stack": {"count": 3}}
    10
    11    def increment(self, ctx):
    12        count = ctx.panel.state.get("v_stack.h_stack.count", 0)
    13        ctx.panel.state.set("v_stack.h_stack.count", count + 1)
    14
    15    def decrement(self, ctx):
    16        count = ctx.panel.get_state("v_stack.h_stack.count", 0)
    17        ctx.panel.set_state("v_stack.h_stack.count", count - 1)
    18
    19    def render(self, ctx):
    20        panel = types.Object()
    21
    22        # Define a vertical stack object with the name 'v_stack'
    23        # key: 'v_stack'
    24        v_stack = panel.v_stack("v_stack", align_x="center", gap=2)
    25
    26        # Define a horizontal stack object with the name 'h_stack' on 'v_stack'
    27        # key: 'v_stack.h_stack'
    28        h_stack = v_stack.h_stack("h_stack", align_y="center")
    29
    30        # Get state
    31        v_stack_state = ctx.panel.state.v_stack
    32        h_stack_state = v_stack_state["h_stack"] if v_stack_state is not None else None
    33        count = h_stack_state["count"] if h_stack_state is not None else 0
    34
    35        # Add a message to the horizontal stack object with the name 'count'
    36        # key: 'v_stack.h_stack.count'
    37        h_stack.message("count", f"Count: {count}")
    38
    39        # Add a button to the horizontal stack object with the name 'increment'
    40        # key: 'v_stack.h_stack.increment'
    41        h_stack.btn(
    42            "increment",
    43            label="Increment",
    44            icon="add",
    45            on_click=self.increment,
    46            variant="contained",
    47        )
    48
    49        # Add a button to the horizontal stack object with the name 'decrement'
    50        # key: 'v_stack.h_stack.count'
    51        h_stack.btn(
    52            "decrement",
    53            label="Decrement",
    54            icon="remove",
    55            on_click=self.decrement,
    56            variant="contained",
    57        )
    58
    59        return types.Property(panel)
    

![../_images/counter-panel-inline.gif](../_images/counter-panel-inline.gif)

#### Panel state#

Panel state is included in every [`render()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.render "fiftyone.operators.panel.Panel.render") call and event callback and is analogous to operator parameters:

  * The values of any components defined in a panelâs [`render()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.render "fiftyone.operators.panel.Panel.render") method are available via corresponding state properties of the same name

  * The current panel state is readable during a panelâs execution



    
    
     1def render(self, ctx):
     2    panel = types.Object()
     3
     4    menu = panel.menu("menu", ...)
     5    actions = menu.btn_group("actions")
     6    actions.enum(
     7        "mode",
     8        values=["foo", "bar"],
     9        on_change=self.on_change_mode,
    10        ...
    11    )
    12
    13    panel.str("user_input", default="spam")
    14
    15def on_change_mode(self, ctx):
    16    # Object-based interface
    17    mode = ctx.panel.state.menu.actions.mode
    18    user_input = ctx.panel.state.user_input
    19
    20    # Functional interface
    21    mode = ctx.panel.get_state("menu.actions.mode")
    22    user_input = ctx.panel.get_state("user_input")
    

Panel state can be programmatically updated in panel methods via the two syntaxes shown below:
    
    
    1def on_change_view(self, ctx):
    2    # Top-level state attributes can be modified by setting properties
    3    ctx.panel.state.foo = "bar"
    4
    5    # Use set_state() to efficiently apply nested updates
    6    ctx.panel.set_state("foo.bar", {"spam": "eggs"})
    

Warning

Donât directly modify panel state in [`render()`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel.render "fiftyone.operators.panel.Panel.render"), just like how `setState()` should not be called in Reactâs [render()](https://legacy.reactjs.org/docs/react-component.html#render).

Instead set panel state in event callbacks as demonstrated above.

#### Panel data#

Panel data is designed to store larger content such as plot data that is loaded once and henceforward stored _only_ clientside to avoid unnecessary/expensive reloads and serverside serialization during the lifecycle of the panel.
    
    
     1def on_load(self, ctx):
     2    self.update_plot_data(ctx)
     3
     4def render(self, ctx):
     5    panel = types.Object()
     6
     7    menu = panel.menu("menu", ...)
     8    actions = menu.btn_group("actions")
     9    actions.enum(
    10        "brain_key",
    11        label="Brain key",
    12        values=["foo", "bar"],
    13        default=None,
    14        on_change=self.update_plot_data,
    15    )
    16
    17    panel.plot("embeddings", config=..., layout=...)
    18
    19    return types.Property(panel)
    20
    21def update_plot_data(self, ctx):
    22    brain_key = ctx.panel.state.menu.actions.brain_key
    23    if brain_key is None:
    24        return
    25
    26    # Load expensive content based on current `brain_key`
    27    results = ctx.dataset.load_brain_results(brain_key)
    28
    29    # Store large content as panel data for efficiency
    30    data = {"points": results.points, ...}
    31    ctx.panel.set_data("embeddings", data)
    

Note how the panelâs `on_load()` hook is implemented so that panel data can be hydrated when the panel is initially loaded, and then subsequently plot data is loaded only when the `brain_key` property is modified.

Note

Panel data is never readable in Python; it is only implicitly used by the types you define when they are rendered clientside.

### Execution store#

Panels can store data in the execution store, which is a key-value store that is persisted beyond the lifetime of the panel. This is useful for storing information that should persist across panel instances and App sessions, such as cached data, long-lived panel state, or user preferences.

You can create/retrieve execution stores scoped to the current `ctx.dataset` via [`ctx.store`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext.store "fiftyone.operators.executor.ExecutionContext.store"):
    
    
     1def on_load(ctx):
     2    # Retrieve a store scoped to the current `ctx.dataset`
     3    # The store is automatically created if necessary
     4    store = ctx.store("my_store")
     5
     6    # Load a pre-existing value from the store
     7    user_choice = store.get("user_choice")
     8
     9    # Store data with a TTL to ensure it is evicted after `ttl` seconds
    10    store.set("my_key", {"foo": "bar"}, ttl=60)
    11
    12    # List all keys in the store
    13    print(store.list_keys())  # ["user_choice", "my_key"]
    14
    15    # Retrieve data from the store
    16    print(store.get("my_key"))  # {"foo": "bar"}
    17
    18    # Retrieve metadata about a key
    19    print(store.get_metadata("my_key"))
    20    # {"created_at": ..., "updated_at": ..., "expires_at": ...}
    21
    22    # Delete a key from the store
    23    store.delete("my_key")
    24
    25    # Clear all data in the store
    26    store.clear()
    

Note

Did you know? Any execution stores associated with a dataset are automatically deleted when the dataset is deleted.

For advanced use cases, it is also possible to create and use global stores that are available to all datasets via the [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore") class:
    
    
     1from fiftyone.operators import ExecutionStore
     2
     3# Retrieve a global store
     4# The store is automatically created if necessary
     5store = ExecutionStore.create("my_store")
     6
     7# Store data with a TTL to ensure it is evicted after `ttl` seconds
     8store.set("my_key", {"foo": "bar"}, ttl=60)
     9
    10# List all keys in the global store
    11print(store.list_keys())  # ["my_key"]
    12
    13# Retrieve data from the global store
    14print(store.get("my_key"))  # {"foo": "bar"}
    15
    16# Retrieve metadata about a key
    17print(store.get_metadata("my_key"))
    18# {"created_at": ..., "updated_at": ..., "expires_at": ...}
    19
    20# Delete a key from the global store
    21store.delete("my_key")
    22
    23# Clear all data in the global store
    24store.clear()
    

Warning

Global stores have no automatic garbage collection, so take care when creating and using global stores whose keys do not utilize TTLs.

### Execution cache#

The [`execution cache`](api__fiftyone.operators.cache.md#module-fiftyone.operators.cache "fiftyone.operators.cache") is a decorator-based interface for caching function results in the execution store. This is useful for avoiding repeated computations in dynamic operators or persisting long-lived values across panel instances and App sessions.

Cached entries are stored in a dataset-scoped or global [`ExecutionStore`](api__fiftyone.operators.store.md#fiftyone.operators.store.ExecutionStore "fiftyone.operators.store.ExecutionStore") and can be customized with TTLs, user scoping, operator prompt modal scoping, and more.

Use the [`execution_cache`](api__fiftyone.operators.cache.md#fiftyone.operators.cache.execution_cache "fiftyone.operators.cache.execution_cache") decorator to cache a functionâs result:
    
    
     1from fiftyone.operators import execution_cache
     2
     3# Default behavior: cache for the life of a dataset
     4@execution_cache
     5def expensive_query(ctx, path):
     6    return ctx.dataset.count_values(path)
     7
     8# Cache in-memory, and only while the current operator prompt modal is open
     9@execution_cache(prompt_scoped=True, residency="ephemeral")
    10def expensive_query(ctx, path):
    11    return ctx.dataset.count_values(path)
    12
    13# Cache with a custom TTL and store name
    14class Processor:
    15    @execution_cache(ttl=60, store_name="processor_cache")
    16    def expensive_query(self, ctx, path):
    17        return ctx.dataset.count_values(path)
    18
    19#
    20# Cache at the user-level
    21#
    22
    23def custom_key_fn(ctx, path):
    24    return path, ctx.user_id
    25
    26@execution_cache(ttl=90, key_fn=custom_key_fn, jwt_scoped=True)
    27def user_specific_query(ctx, path):
    28    return ctx.dataset.match(F("creator_id") == ctx.user_id).count_values(path)
    29
    30#
    31# You can manually bypass/modify the cache if necessary
    32#
    33
    34# Bypass the cache
    35result = expensive_query.uncached(ctx, path)
    36
    37# Set the cache for the given arguments
    38expensive_query.set_cache(ctx, path, value_to_cache)
    39
    40# Clear the cache for a specific input
    41expensive_query.clear_cache(ctx, path)
    42
    43# Clear all cache entries for the function
    44expensive_query.clear_all_caches()
    45expensive_query.clear_all_caches(dataset_id=dataset._doc.id)
    

Note

See the [`execution_cache`](api__fiftyone.operators.cache.md#fiftyone.operators.cache.execution_cache "fiftyone.operators.cache.execution_cache") documentation for more information about customizing the caching behavior.

The function being cached must:

  * accept a [`ctx`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") as the first parameter

  * be idempotent, i.e., same inputs produce the same outputs

  * have serializable function arguments and return values

  * have no side effects




By default, cached entries are associated with the current dataset and will be automatically deleted when the dataset is deleted, but you can customize this behavior, including setting an explicit time-to-live in seconds for cached entries, by passing optional keyword arguments like `ttl` to [`execution_cache`](api__fiftyone.operators.cache.md#fiftyone.operators.cache.execution_cache "fiftyone.operators.cache.execution_cache").

Warning

When `residency != "ephemeral"`, cached values must be coerced to JSON safe types in order to be stored. By default, a default JSON converter is used that can handle many common types, but you can override this behavior if necessary by providing custom `serialize` and `deserialize` functions.

Hereâs an example of caching a sample using custom serialization:
    
    
     1import fiftyone as fo
     2from fiftyone.operators import execution_cache
     3
     4def serialize_sample(sample):
     5    return sample.to_dict()
     6
     7def deserialize_sample(data):
     8    return fo.Sample.from_dict(data)
     9
    10@execution_cache(
    11    ttl=60,
    12    serialize=serialize_sample,
    13    deserialize=deserialize_sample,
    14)
    15def get_first_sample(ctx):
    16    return ctx.dataset.first()
    

### Saved workspaces#

[Saved workspaces](user_guide__app.md#app-workspaces) may contain any number of Python panels!

When a workspace is saved, the current panel state of any panels in the layout is persisted as part of the workspaceâs definition. Thus when the workspace is loaded later, all panels will ârememberâ their state.

Panel data (which may be large), on the other hand, is _not_ explicitly persisted. Instead it should be hydrated when the panel is loaded using the pattern demonstrated here.

### Accessing secrets#

Panels can access secrets defined by their plugin.

At runtime, the panelâs execution context is automatically hydrated with any available secrets that are declared by the plugin. Panels can access these secrets via the `ctx.secrets` dict:
    
    
    1def on_load(self, ctx):
    2    url = ctx.secrets["FIFTYONE_CVAT_URL"]
    3    username = ctx.secrets["FIFTYONE_CVAT_USERNAME"]
    4    password = ctx.secrets["FIFTYONE_CVAT_PASSWORD"]
    5    email = ctx.secrets["FIFTYONE_CVAT_EMAIL"]
    

### Common patterns#

Most panels make use of common patterns like callbacks, menus, interactive plots, and walkthrough layouts.

Learning the patterns described below will help you build panels faster and avoid roadblocks along the way.

Note

Check out the [panel examples](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/panel-examples) plugin to see a collection of fully-functional panels that demonstrate the common patterns below.

#### Hybrid panels (Python + JavaScript/React)#

FiftyOne supports building panels that combine Python and JavaScript/React code. This allows you to leverage the full power of React and the JS ecosystem while still taking advantage of the simplicity and expressiveness of Python for defining panel logic and state.

The Python panel class handles configuration, state initialization, and event logic. The `render()` method connects to the React component via `composite_view=True`. Any event handlers passed as view kwargs become callable from JavaScript:
    
    
     1import fiftyone.operators as foo
     2import fiftyone.operators.types as types
     3
     4class HybridPanel(foo.Panel):
     5    @property
     6    def config(self):
     7        return foo.PanelConfig(
     8            name="hybrid_panel",
     9            label="Hybrid Panel",
    10            icon="adjust",
    11            surfaces="grid modal",
    12        )
    13
    14    def on_load(self, ctx):
    15        ctx.panel.set_state("count", 0)
    16
    17    def increment(self, ctx):
    18        count = ctx.panel.get_state("count") or 0
    19        ctx.panel.set_state("count", count + 1)
    20
    21    def render(self, ctx):
    22        panel = types.Object()
    23        return types.Property(
    24            panel,
    25            view=types.View(
    26                component="MyCustomView",
    27                composite_view=True,
    28                increment=self.increment,
    29            ),
    30        )
    31
    32def register(p):
    33    p.register(HybridPanel)
    

On the JavaScript side, register a component whose `name` matches the `component` argument in `render()`. Access panel state via `usePanelStatePartial` and trigger Python event handlers using `useTriggerPanelEvent`:
    
    
     1import { PluginComponentType, registerComponent } from "@fiftyone/plugins";
     2import { usePanelStatePartial } from "@fiftyone/spaces";
     3import { useTriggerPanelEvent } from "@fiftyone/operators";
     4
     5function MyCustomView({ schema }) {
     6    const [state] = usePanelStatePartial("state", {});
     7    const triggerEvent = useTriggerPanelEvent();
     8    const { increment } = schema.view;
     9
    10    return (
    11        <button onClick={() => triggerEvent(increment)}>
    12            Count: {state.count}
    13        </button>
    14    );
    15}
    16
    17registerComponent({
    18    name: "MyCustomView",
    19    label: "MyCustomView",
    20    component: MyCustomView,
    21    type: PluginComponentType.Component,
    22    activator: () => true,
    23});
    

Note

Check out the [Hybrid Panel Plugin](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/hybrid-panel) for a complete example of building a hybrid panel.

#### Callbacks#

Most panel components support callback methods like `on_click` and `on_change` that you can implement to perform operations and trigger state updates when users interact with the components.

For example, the code below shows how clicking a button or changing the state of a slider can initiate callbacks that trigger operators, open other panels, and programmatically modify the current state.

Note

All callback functions have access to the current [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") via their `ctx` argument and can use it to get/update panel state and trigger other operations.

Warning

The return value of all panel eventsâincluding builtin events (such as `on_load`, `on_unload`, `on_change_ctx`, etc.) and custom events (such as `on_change_brain_key`, `on_click_start`, etc.)âmust be JSON-serializable.

If your panel event returns a value of a custom type (for example, a NumPy array or a FiftyOne Sample or custom class), you must first convert it to a JSON-serializable format (such as a Python list or dictionary).

Returning non-serializable objects will cause errors and prevent your panel from functioning correctly.
    
    
     1def on_load(self, ctx):
     2    # Set initial slider state
     3    ctx.panel.state.slider_value = 5
     4
     5def open_compute(self, ctx):
     6    # Launch an interactive prompt for user to execute an operator
     7    ctx.prompt("@voxel51/brain/compute_visualization")
     8
     9def open_embeddings(self, ctx):
    10    # Open embeddings panel
    11    ctx.trigger("open_panel", params=dict(name="Embeddings"))
    12
    13def change_value(self, ctx):
    14    # Grab current slider value from `ctx.params`
    15    ctx.panel.state.slider_value = (
    16        ctx.params["value"] or ctx.params["panel_state"]["slider_value"]
    17    )
    18
    19def render(self, ctx):
    20    panel = types.Object()
    21
    22    # Define buttons that work with on_click callbacks
    23    panel.btn(
    24        "button_1",
    25        label="Compute visualization",
    26        on_click=self.open_compute,
    27    )
    28    panel.btn(
    29        "button_2",
    30        label="Open embeddings panel",
    31        on_click=self.open_embeddings,
    32    )
    33
    34    # Define a slider with an `on_change` callback
    35    slider = types.SliderView(
    36        data=ctx.panel.state.slider_value, label="Example Slider"
    37    )
    38    schema = {"min": 0, "max": 10, "multipleOf": 1}
    39    panel.int(
    40        "slider_value", view=slider, on_change=self.change_value, **schema
    41    )
    

Note

Did you know? You can use `ctx.params` in a callback to access the state of the property that triggered the action.

#### Dropdown menus#

Dropdown menus can be a useful tool to build panels whose layout/content dynamically changes based on the current state of the menu.

Hereâs an example of a dropdown menu with selectable options that alters the panel layout based on user input.

Note

Panels also support a `menu()` property that provides a convenient syntax for defining a group of dropdowns, buttons, etc that can be anchored to a particular position in your panel (e.g., top-left).

Check out this section for an example panel that makes use of `menu()`.
    
    
     1class DropdownMenuExample(foo.Panel):
     2    @property
     3    def config(self):
     4        return foo.PanelConfig(
     5            name="example_dropdown_menu",
     6            label="Examples: Dropdown Menu",
     7        )
     8
     9    def on_load(self, ctx):
    10        ctx.panel.state.selection = None
    11
    12    def alter_selection(self, ctx):
    13        ctx.panel.state.selection = ctx.params["value"]
    14
    15    def refresh_page(self, ctx):
    16        ctx.ops.reload_dataset()
    17
    18    def reload_samples(self, ctx):
    19        ctx.ops.reload_samples()
    20
    21    def say_hi(self, ctx):
    22        ctx.ops.notify("Hi!", variant="success")
    23
    24    def render(self, ctx):
    25        panel = types.Object()
    26
    27        panel.md(
    28            """
    29            ### Welcome to the Python Panel Dropdown Menu Example
    30            Use the menu below to select what you would like to do next!
    31
    32            ---
    33
    34        """,
    35            name="header",
    36            width=50,  # 50% of current panel width
    37            height="200px",
    38        )
    39
    40        # Define a dropdown menu and add choices
    41        dropdown = types.DropdownView()
    42        dropdown.add_choice(
    43            "refresh",
    44            label="Display Refresh Button",
    45            description="Displays button that will refresh the FiftyOne App",
    46        )
    47        dropdown.add_choice(
    48            "reload_samples",
    49            label="Display Reload Samples Button",
    50            description="Displays button that will reload the samples view",
    51        )
    52        dropdown.add_choice(
    53            "say_hi",
    54            label="Display Hi Button",
    55            description="Displays button that will say hi",
    56        )
    57
    58        # Add dropdown menu to the panel as a view and use the `on_change`
    59        # callback to trigger `alter_selection`
    60        panel.view(
    61            "dropdown",
    62            view=dropdown,
    63            label="Dropdown Menu",
    64            on_change=self.alter_selection,
    65        )
    66
    67        # Change panel visual state dependent on dropdown menu selection
    68        if ctx.panel.state.selection == "refresh":
    69            panel.btn(
    70                "refresh",
    71                label="Refresh FiftyOne",
    72                on_click=self.refresh_page,
    73                variant="contained",
    74            )
    75        elif ctx.panel.state.selection == "reload_samples":
    76            panel.btn(
    77                "reload_samples",
    78                label="Reload Samples",
    79                on_click=self.reload_samples,
    80                variant="contained",
    81            )
    82        elif ctx.panel.state.selection == "say_hi":
    83            panel.btn(
    84                "say_hi",
    85                label="Say Hi",
    86                on_click=self.say_hi,
    87                variant="contained",
    88            )
    89
    90        return types.Property(
    91            panel,
    92            view=types.GridView(
    93                height=100,
    94                width=100,
    95                align_x="center",
    96                align_y="center",
    97                orientation="vertical",
    98            ),
    99        )
    

![../_images/dropdown-example-inline.gif](../_images/dropdown-example-inline.gif)

#### Interactive plots#

Panels provide native support for defining interactive plots that can render data from the current dataset and dynamically update or trigger actions as users interact with the plots.

For example, hereâs a panel that displays a histogram of a specified field of the current dataset where clicking a bar loads the corresponding samples in the App.
    
    
     1import fiftyone.operators as foo
     2import fiftyone.operators.types as types
     3from fiftyone import ViewField as F
     4
     5class InteractivePlotExample(foo.Panel):
     6    @property
     7    def config(self):
     8        return foo.PanelConfig(
     9            name="example_interactive_plot",
    10            label="Examples: Interactive Plot",
    11            icon="bar_chart",
    12        )
    13
    14    def on_load(self, ctx):
    15        # Get target field
    16        target_field = (
    17            ctx.panel.state.target_field or "ground_truth.detections.label"
    18        )
    19        ctx.panel.state.target_field = target_field
    20
    21        # Compute target histogram for current dataset
    22        counts = ctx.dataset.count_values(target_field)
    23        keys, values = zip(*sorted(counts.items(), key=lambda x: x[0]))
    24
    25        # Store as panel data for efficiency
    26        ctx.panel.data.histogram = {"x": keys, "y": values, "type": "bar"}
    27
    28        # Launch panel in a horizontal split view
    29        ctx.ops.split_panel("example_interactive_plot", layout="horizontal")
    30
    31    def on_change_view(self, ctx):
    32        # Update histogram when current view changes
    33        self.on_load(ctx)
    34
    35    def on_histogram_click(self, ctx):
    36        # The histogram bar that the user clicked
    37        value = ctx.params.get("x")
    38
    39        # Create a view that matches the selected histogram bar
    40        field = ctx.panel.state.target_field
    41        view = _make_matching_view(ctx.dataset, field, value)
    42
    43        # Load view in App
    44        if view is not None:
    45            ctx.ops.set_view(view=view)
    46
    47    def reset(self, ctx):
    48        ctx.ops.clear_view()
    49        self.on_load(ctx)
    50
    51    def render(self, ctx):
    52        panel = types.Object()
    53
    54        panel.plot(
    55            "histogram",
    56            layout={
    57                "title": {
    58                    "text": "Interactive Histogram",
    59                    "xanchor": "center",
    60                    "yanchor": "top",
    61                    "automargin": True,
    62                },
    63                "xaxis": {"title": "Labels"},
    64                "yaxis": {"title": "Count"},
    65            },
    66            on_click=self.on_histogram_click,
    67            width=100,
    68        )
    69
    70        panel.btn(
    71            "reset",
    72            label="Reset Chart",
    73            on_click=self.reset,
    74            variant="contained",
    75        )
    76
    77        return types.Property(
    78            panel,
    79            view=types.GridView(
    80                align_x="center",
    81                align_y="center",
    82                orientation="vertical",
    83                height=100,
    84                width=100,
    85                gap=2,
    86                padding=0,
    87            ),
    88        )
    89
    90def _make_matching_view(dataset, field, value):
    91    if field.endswith(".label"):
    92        root_field = field.split(".")[0]
    93        return dataset.filter_labels(root_field, F("label") == value)
    94    elif field == "tags":
    95        return dataset.match_tags(value)
    96    else:
    97        return dataset.match(F(field) == value)
    

![../_images/interactive-plot-example-inline.gif](../_images/interactive-plot-example-inline.gif)

#### Walkthroughs#

You can use a combination of panel objects like markdown, buttons, arrow navigation, and layout containers to create guided walkthroughs similar to the ones at [try.fiftyone.ai](https://try.fiftyone.ai/datasets/example/samples).

Hereâs an example of a panel that leads the user through multiple steps of a guided workflow.
    
    
      1class WalkthroughExample(foo.Panel):
      2    @property
      3    def config(self):
      4        return foo.PanelConfig(
      5            name="example_walkthrough",
      6            label="Examples: Walkthrough",
      7        )
      8
      9    def on_load(self, ctx):
     10        ctx.panel.state.page = 1
     11        info_table = [
     12            {
     13                "Dataset Name": f"{ctx.dataset.name}",
     14                "Dataset Description": "FiftyOne Quick Start Zoo Dataset",
     15                "Number of Samples": f"{ctx.dataset.count()}",
     16            },
     17        ]
     18
     19    ctx.panel.state.info_table = info_table
     20
     21    def go_to_next_page(self, ctx):
     22        ctx.panel.state.page = ctx.panel.state.page + 1
     23
     24    def go_to_previous_page(self, ctx):
     25        ctx.panel.state.page = ctx.panel.state.page - 1
     26
     27    def reset_page(self, ctx):
     28        ctx.panel.state.page = 1
     29
     30    def open_operator_io(self, ctx):
     31        ctx.ops.open_panel("OperatorIO")
     32
     33    def render(self, ctx):
     34        panel = types.Object()
     35
     36        # Define a vertical stack to live inside your panel
     37        stack = panel.v_stack(
     38            "welcome", gap=2, width=75, align_x="center", align_y="center"
     39        )
     40        button_container = types.GridView(
     41            gap=2, align_x="left", align_y="center"
     42        )
     43
     44        page = ctx.panel.state.get("page", 1)
     45
     46        if page == 1:
     47            stack.md(
     48                """
     49                ### A Tutorial Walkthrough
     50
     51                Welcome to the FiftyOne App! Here is a great example of what it looks like to create a tutorial style walkthrough via a Python Panel.
     52            """,
     53                name="markdown_screen_1",
     54            )
     55            stack.media_player(
     56                "video",
     57                "https://youtu.be/ad79nYk2keg",
     58                align_x="center",
     59                align_y="center",
     60            )
     61        elif page == 2:
     62            stack.md(
     63                """
     64                ### Information About Your Dataset
     65
     66                Perhaps you would like to know some more information about your dataset?
     67            """,
     68                name="markdown_screen_2",
     69            )
     70            table = types.TableView()
     71            table.add_column("Dataset Name", label="Dataset Name")
     72            table.add_column("Dataset Description", label="Description")
     73            table.add_column("Number of Samples", label="Number of Samples")
     74
     75            panel.obj(
     76                name="info_table",
     77                view=table,
     78                label="Cool Info About Your Data",
     79            )
     80        elif page == 3:
     81            if ctx.panel.state.operator_status != "opened":
     82                stack.md(
     83                    """
     84                    ### One Last Trick
     85
     86                    If you want to do something cool, click the button below.
     87                """,
     88                    name="markdown_screen_3",
     89                )
     90                btns = stack.obj("top_btns", view=button_container)
     91                btns.type.btn(
     92                    "open_operator_io",
     93                    label="Do Something Cool",
     94                    on_click=self.open_operator_io,
     95                    variant="contained"
     96                )
     97        else:
     98            stack.md(
     99                """
    100                #### How did you get here?
    101                Looks like you found the end of the walkthrough. Or have you gotten a little lost in the grid? No worries, let's get you back to the walkthrough!
    102            """
    103            )
    104            btns = stack.obj("btns", view=button_container)
    105            btns.type.btn("reset", label="Go Home", on_click=self.reset_page)
    106
    107        # Arrow navigation to go to next or previous page
    108        panel.arrow_nav(
    109            "arrow_nav",
    110            forward=page != 3,  # hidden for the last page
    111            backward=page != 1,  # hidden for the first page
    112            on_forward=self.go_to_next_page,
    113            on_backward=self.go_to_previous_page,
    114        )
    115
    116        return types.Property(
    117            panel,
    118            view=types.GridView(
    119                height=100, width=100, align_x="center", align_y="center"
    120            ),
    121        )
    

![../_images/walkthrough-example-inline.gif](../_images/walkthrough-example-inline.gif)

#### Displaying multimedia#

Displaying images, videos, and other forms of multimedia is straightforward in panels. You can embed third-party resources like URLs or load multimedia stored in local directories.

Here are some examples of panels that load, render, and manipulate various forms of image and video data.
    
    
     1class ImageExample(foo.Panel):
     2    @property
     3    def config(self):
     4        return foo.PanelConfig(
     5            name="example_image",
     6            label="Examples: Image",
     7        )
     8
     9    def on_load(self, ctx):
    10        # Load image from static URL
    11        ctx.panel.state.single_image = "https://static6.depositphotos.com/1119834/620/i/450/depositphotos_6201075-stock-photo-african-elephant-smelling.jpg"
    12
    13        # Load 10 images from dataset
    14        samples = ctx.dataset.limit(10)
    15        for index, sample in enumerate(samples):
    16            image_path = (
    17                f"http://localhost:5151/media?filepath={sample.filepath}"
    18            )
    19            ctx.panel.set_state(f"image{index}", image_path)
    20
    21    def render(self, ctx):
    22        panel = types.Object()
    23
    24        panel.md(
    25            "# Image Collection\n\n_Here's a collage of images that can be loaded a few different ways_",
    26            name="intro_message",
    27        )
    28
    29        panel.md(
    30            "## Single Image\n\nThis image was loaded from a url",
    31            name="header_one",
    32        )
    33        image_holder = types.ImageView()
    34
    35        panel.view(
    36            "single_image", view=image_holder, caption="A picture of a canyon"
    37        )
    38
    39        panel.md("---", name="divider")
    40        panel.md(
    41            "## Multiple Images\n\n_All these images were loaded from our current dataset_",
    42            name="header_two",
    43        )
    44
    45        for index in range(10):
    46            image_holder = types.ImageView()
    47            panel.view(
    48                f"image{index}", view=image_holder, caption=f"Image {index}"
    49            )
    50
    51        return types.Property(
    52            panel,
    53            view=types.GridView(
    54                align_x="center", align_y="center", orientation="vertical"
    55            ),
    56        )
    
    
    
     1class MediaPlayerExample(foo.Panel):
     2    @property
     3    def config(self):
     4        return foo.PanelConfig(
     5            name="example_media_player",
     6            label="Examples: Media Player",
     7        )
     8
     9    def on_load(self, ctx):
    10        ctx.panel.state.media_player = {
    11            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    12        }
    13
    14    def render(self, ctx):
    15        panel = types.Object()
    16
    17        panel.md(
    18            "# Media View Player Example\n\nHere's a fun video to check out",
    19            name="intro_message",
    20        )
    21
    22        media_player = types.MediaPlayerView()
    23
    24        panel.obj(
    25            "media_player",
    26            view=media_player,
    27            label="Media Player Example",
    28            default={"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
    29        )
    30
    31        return types.Property(
    32            panel,
    33            view=types.GridView(
    34                align_x="center", align_y="center", orientation="vertical"
    35            ),
    36        )
    

![../_images/multimedia-example-inline.gif](../_images/multimedia-example-inline.gif)

#### Type hints#

Defining the types of your panelâs function arguments allows you to inspect the methods available to an object and will dramatically help you increase your speed of development.

With type hints, your IDE can preview helpful docstrings, trace `fiftyone` source code, and see what methods exist on your object during the development process.

For example, declaring that the `ctx` variable has type [`ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext") allows you to reveal all of its available methods during development:
    
    
     1from fiftyone.operators import ExecutionContext
     2
     3def on_load(ctx: ExecutionContext):
     4    ctx.trigger()
     5    ctx.ops()
     6    ctx.secrets()
     7
     8    # Reveals the remaining methods available to ctx
     9    ctx.
    10    ...
    

## Developing skills#

Skills are Markdown files that teach AI agents how to perform complex FiftyOne workflows using natural language. A skill describes a task that an agent can be asked to perform â such as importing a dataset, running inference, or finding duplicates â and provides step-by-step guidance that the agent follows to complete the workflow autonomously.

You can bundle skills inside any FiftyOne plugin by placing them in a `skills/` subdirectory and declaring their names in your `fiftyone.yml`:
    
    
    skills:
      - my-skill-name
    

Note

See [Developing skills](agents__developing_skills.md#developing-skills-authoring) for a full guide on authoring skills, including the required file structure, YAML frontmatter fields, and how to contribute skills to the community.

## Developing JS plugins#

This section describes how to develop JS-specific plugin components.

### Getting Started#

To start building your own JS plugin, refer to the [hello-world-plugin-js](https://github.com/voxel51/hello-world-plugin-js) repository. This repo serves as a starting point, providing examples of a build process, a JS panel, and a JS operator.

The [fiftyone-js-plugin-build](https://github.com/voxel51/fiftyone-js-plugin-build) package offers a utility for configuring [vite](https://vite.dev) to build your JS plugin bundle.

### Component types#

JS plugins may register components to add or customize functionality within the FiftyOne App. Each component is registered with an activation function. The component will only be considered for rendering when the activation function returns `true`:

  * **Panel** : JS plugins can register panel components that can be opened by clicking the `+` next to any existing panelâs tab

  * **Component** : JS plugins can register generic components that can be used to render operator input and output




### Panels and Components#

Hereâs some examples of using panels and components to add your own custom user interface and components to the FiftyOne App.

#### Hello world panel#

A simple plugin that renders âHello worldâ in a panel would look like this:
    
    
     1import { registerComponent, PluginComponentTypes } from "@fiftyone/plugins";
     2
     3function HelloWorld() {
     4    return <h1>Hello world</h1>;
     5}
     6
     7registerComponent({
     8    name: "HelloWorld",
     9    label: "Hello world",
    10    component: HelloWorld,
    11    type: PluginComponentTypes.Panel,
    12    activator: () => true
    13});
    14
    15:linenos:
    

#### Adding a custom Panel#
    
    
     1import * as fop from "@fiftyone/plugins";
     2import * as fos from "@fiftyone/state";
     3import * as foa from "@fiftyone/aggregations";
     4import AwesomeMap from "react-mapping-library";
     5
     6function CustomPanel() {
     7    const dataset = useRecoilValue(fos.dataset);
     8    const view = useRecoilValue(fos.view);
     9    const filters = useRecoilValue(fos.filters);
    10    const [aggregate, points, loading] = foa.useAggregation({
    11        dataset,
    12        filters,
    13        view,
    14    });
    15
    16    React.useEffect(() => {
    17        aggregate(
    18            [
    19                new foa.aggregations.Values({
    20                    fieldOrExpr: "id",
    21                }),
    22                new foa.aggregations.Values({
    23                    fieldOrExpr: "location.point.coordinates",
    24                }),
    25            ],
    26            dataset.name
    27        );
    28    }, [dataset, filters, view]);
    29
    30    if (loading) return <h1>Loading</h1>;
    31
    32    return <MyMap geoPoints={points} />;
    33}
    34
    35fop.registerComponent({
    36    // component to delegate to
    37    component: CustomPanel,
    38
    39    // tell FiftyOne you want to provide a custom panel
    40    type: PluginComponentTypes.Panel,
    41
    42    // used for the panel selector button
    43    label: "Map",
    44
    45    // only show the Map panel when the dataset has Geo data
    46    activator: ({ dataset }) => dataset.sampleFields.location,
    47});
    

#### Custom operator view using component plugin#

Creating and registering a custom view type:
    
    
     1import * as fop from "@fiftyone/plugins";
     2import { useState } from "react"
     3
     4function CustomOperatorView(props) {
     5    // these props are provided to the component used as the view for an
     6    // operator input/output field
     7    const { errors, data, id, onChange, path, schema } = props
     8
     9    // schema may optionally include a view property which contains
    10    // attributes such label, description, caption for
    11    // the field. Schema will also provide a type property to indicate the type
    12    // of value expected for the field (i.e. string, number, object, array, etc.)
    13    const { default: defaultValue, view, type } = schema
    14
    15    // Schema may also provide a default value for the field
    16    const [value, setValue] = useState(defaultValue)
    17
    18    return (
    19        <div>
    20            <label htmlFor={id}>{view.label}</label>
    21            <input
    22                value={value}
    23                id={id}
    24                type={type}
    25                onChange={(e) => {
    26                    // onChange function passed as a prop can be called with
    27                    // path and value to set the current value for a field
    28                    onChange(path, e.target.value)
    29                }}
    30            />
    31        </div>
    32    )
    33}
    34
    35fop.registerComponent({
    36    // unique name you can use later to refer to the component plugin
    37    name: "CustomOperatorView",
    38
    39    // component to delegate to
    40    component: CustomOperatorView,
    41
    42    // tell FiftyOne you want to provide a custom component
    43    type: PluginComponentTypes.Component,
    44
    45    // activate this plugin unconditionally
    46    activator: () => true,
    47});
    

Using the custom component as the view for a Python operator field:
    
    
     1import fiftyone.operators as foo
     2import fiftyone.operators.types as types
     3
     4class CustomViewOperator(foo.Operator):
     5    @property
     6    def config(self):
     7        return foo.OperatorConfig(
     8            name="custom_view_operator",
     9            label="Custom View Operator",
    10        )
    11
    12    def resolve_input(self, ctx):
    13        inputs = types.Object()
    14        inputs.str(
    15            "name",
    16            label="Name",
    17            default="FiftyOne",
    18            # provide the name of a registered component plugin
    19            view=types.View(component="CustomOperatorView")
    20        )
    21        return types.Property(inputs)
    22
    23    def execute(self, ctx):
    24        return {}
    

#### Custom sample renderers#

Plugins can register `SampleRenderer` components to provide custom rendering for non-native media types in the grid and modal. Native media types (`image`, `video`, `point-cloud`, `3d`) continue to use the built-in media renderers.

Each sample renderer declares `sampleRendererOptions.supports`. The simplest form is a matcher object with `extensions`, `mimeTypes`, and `mediaTypes`. All specified matcher groups must match (AND), and values in a group are matched case-insensitively (OR). `supports` can also be a predicate function that receives the sample renderer match context.

Grid rendering is opt-in. Set `sampleRendererOptions.grid.enabled` to `true` to enable a renderer in the grid. If you need a different grid-only implementation, provide `sampleRendererOptions.grid.overrideComponent`; otherwise the canonical renderer component is reused in both modal and grid.

The sample renderer component receives a single `ctx` prop containing the sample renderer render context:

  * `sample` and `media`

  * `surface` (`"modal"` or `"grid"`)

  * `dataset` and `schema`




Hereâs an example of a hypothetical plugin config that renders PDF files in both the grid and modal:
    
    
     1import {
     2  type SampleRendererProps,
     3  PluginComponentType,
     4  registerComponent,
     5} from "@fiftyone/plugins";
     6
     7function PdfRenderer({ ctx }: SampleRendererProps) {
     8  return (
     9    <iframe
    10      src={ctx.media.url ?? ""}
    11      title={ctx.sample.sample.filepath}
    12      style={{ width: "100%", height: "100%", border: 0 }}
    13    />
    14  );
    15}
    16
    17registerComponent({
    18  name: "PDFRenderer",
    19  label: "PDF renderer",
    20  component: PdfRenderer,
    21  type: PluginComponentType.SampleRenderer,
    22  activator: () => true,
    23  sampleRendererOptions: {
    24    priority: 100,
    25    supports: {
    26      extensions: [".pdf"],
    27      mimeTypes: ["application/pdf"],
    28      mediaTypes: ["unknown"],
    29    },
    30    grid: {
    31      enabled: true,
    32    },
    33  },
    34});
    

### FiftyOne App state#

There are a few ways to manage the state of your plugin. By default you should defer to existing state management in the FiftyOne App.

For example, if you want to allow users to select samples, you can use the `@fiftyone/state` package.

#### Interactivity and state#

If your plugin only has internal state, you can use existing state management to achieve your desired UX. For example, in a 3D visualizer, you might want to use [Three.js](https://threejs.org) and its object model, events, and state management. Or just use your own React hooks to maintain your plugin components internal state.

If you want to allow users to interact with other aspects of FiftyOne through your plugin, you can use the `@fiftyone/state` package:
    
    
    1// note: similar to react hooks, these must be used in the context
    2// of a React component
    3
    4// select a dataset
    5const selectLabel = fos.useOnSelectLabel();
    6
    7// in a callback
    8selectLabel({ id: "labelId", field: "fieldName" });
    

The example above shows how you can coordinate or surface existing features of FiftyOne through your plugin via the `@fiftyone/state` package. This package provides hooks to access and modify the state of the FiftyOne App.

#### Recoil, atoms, and selectors#

You can also use a combination of your own and fiftyoneâs recoil `atoms` and `selectors`.

Hereâs an example the combines both approaches in a hook that you could call from anywhere where hooks are supported (almost all plugin component types).
    
    
     1import {atom, useRecoilValue, useRecoilState} from 'recoil';
     2
     3const myPluginmyPluginFieldsState = atom({
     4    key: 'myPluginFields',
     5    default: []
     6})
     7
     8function useMyHook() {
     9    const dataset = useRecoilValue(fos.dataset);
    10    const [fields, setFields] = useRecoilState(myPluginFieldsState);
    11
    12    return {
    13        dataset,
    14        fields,
    15        addField: (field) => setFields([...fields, field])
    16    }
    17}
    

### Panel state#

Plugins that provide `PluginComponentTypes.Panel` components should use the `@fiftyone/spaces` package to manage their state. This package provides hooks to allow plugins to manage the state of individual panel instances.
    
    
     1import { usePanelStatePartial, usePanelTitle } from "@fiftyone/spaces";
     2import { Button } from '@fiftyone/components';
     3
     4// in your panel component, you can use the usePanelStatePartial hook
     5// to read and write to the panel state
     6function MyPanel() {
     7    const [state, setState] = usePanelStatePartial('choice');
     8    const setTitle = usePanelTitle();
     9
    10    React.useEffect(() => {
    11      setTitle(`My Panel: ${state}`);
    12    }, [state]);
    13
    14    return (
    15      <div>
    16        <h1>Choice: {state}</h1>
    17        <Button onClick={() => setState('A')}>A</Button>
    18        <Button onClick={() => setState('B')}>B</Button>
    19      </div>
    20    );
    21}
    

### Reading settings in your plugin#

Plugins may support two styles of configuration settings:

  * System-wide plugin settings under the `plugins` key of your [App config](user_guide__config.md#configuring-fiftyone-app)

  * Dataset-specific plugin settings for any subset of the above values on a [datasetâs App config](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config).




Plugin settings are used, for example, to allow the user to configure the default camera position of FiftyOneâs builtin [3D visualizer](user_guide__app.md#app-3d-visualizer-config).

Hereâs an example of a system-wide plugin setting:
    
    
    1// app_config.json
    2{
    3  "plugins": {
    4    "my-plugin": {
    5      "mysetting": "foo"
    6    }
    7  }
    8}
    

And hereâs how to customize that setting for a particular dataset:
    
    
    1import fiftyone as fo
    2
    3dataset = fo.load_dataset("quickstart")
    4dataset.app_config.plugins["my-plugin"] = {"mysetting": "bar"}
    5dataset.save()
    

In your plugin implementation, you can read settings with the `useSettings` hook:
    
    
    1const { mysetting } = fop.useSettings("my-plugin");
    

Note

See the [this page](user_guide__config.md#configuring-plugins) page for more information about configuring plugins.

### Querying FiftyOne#

A typical use case for a JS plugin is to provide a unique way of visualizing FiftyOne data. However some plugins may need to also fetch data in a unique way to efficiently visualize it.

For example, a `PluginComponentType.Panel` plugin rendering a map of geo points may need to fetch data relative to where the user is currently viewing. In MongoDB, such a query would look like this:
    
    
    1{
    2  $geoNear: {
    3    near: { type: "Point", coordinates: [ -73.99279 , 40.719296 ] },
    4    maxDistance: 2,
    5    query: { category: "Parks" },
    6  }
    7}
    

In a FiftyOne plugin this same query can be performed using the `useAggregation()` method of the plugin SDK:
    
    
     1import * as fop from "@fiftyone/plugins";
     2import * as fos from "@fiftyone/state";
     3import * as foa from "@fiftyone/aggregations";
     4import * as recoil from "recoil";
     5
     6function useGeoDataNear() {
     7    const dataset = useRecoilValue(fos.dataset);
     8    const view = useRecoilValue(fos.view);
     9    const filters = useRecoilValue(fos.filters);
    10    const [aggregate, points, isLoading] = foa.useAggregation({
    11        dataset,
    12        filters,
    13        view,
    14    });
    15    const availableFields = findAvailableFields(dataset.sampleFields);
    16    const [selectedField, setField] = React.useState(availableFields[0]);
    17
    18    React.useEffect(() => {
    19        aggregate([
    20            new foa.aggregations.Values({
    21                fieldOrExpr: "location.point.coordinates",
    22            }),
    23        ]);
    24    }, []);
    25
    26    return {
    27        points,
    28        isLoading,
    29        setField,
    30        availableFields,
    31        selectedField,
    32    };
    33}
    34
    35function MapPlugin() {
    36    const { points, isLoading, setField, availableFields, selectedField } =
    37        useGeoDataNear();
    38
    39    return (
    40        <Map
    41            points={points}
    42            onSelectField={(f) => setField(f)}
    43            selectedField={selectedField}
    44            locationFields={availableFields}
    45        />
    46    );
    47}
    48
    49fop.registerComponent({
    50    name: "MapPlugin",
    51    label: "Map",
    52    activator: ({ dataset }) => findAvailableFields(dataset.fields).length > 0,
    53});
    

## Plugin runtime#

### JS runtime#

In JS, plugins are loaded from your [plugins directory](plugins__using_plugins.md#plugins-directory) into the browser. The FiftyOne App server finds these plugins by looking for `package.json` files that include `fiftyone` as a property. This `fiftyone` property describes where the plugin executable (dist) is.

### Python runtime#

Python operators are executed in two ways:

#### Immediate execution#

By default, all operations are executed by the plugin server immediately after they are triggered, either programmatically or by the user in the App.

The plugin server is launched by the FiftyOne App as a subprocess that is responsible for loading plugins and executing them. The plugin server is only accessible via ipc. Its interface (similar to JSON rpc) allows for functions to be called over interprocess communication. This allows for user python code to be isolated from core code. It also allows for the operating system to manage the separate process as it exists in the same process tree as the root process (ipython, Jupyter, etc).

#### Delegated execution#

Python operations may also be delegated for execution in the background.

When an operation is delegated, the following happens:

  1. The operationâs execution context is serialized and stored in the database

  2. The [connected orchestrator](plugins__using_plugins.md#delegated-orchestrator) picks up the task and executes it when resources are available




## Advanced usage#

### Storing custom runs#

When users execute builtin methods like [annotation](integrations__annotation.md#fiftyone-annotation), [evaluation](user_guide__evaluation.md#evaluating-models), and [brain methods](brain.md#fiftyone-brain) on their datasets, certain configuration and results information is stored on the dataset that can be accessed later; for example, see [managing brain runs](brain.md#brain-managing-runs).

FiftyOne also provides the ability to store _custom runs_ on datasets, which can be used by plugin developers to persist arbitrary application-specific information that can be accessed later by users and/or plugins.

The interface for creating custom runs is simple:
    
    
     1import fiftyone as fo
     2
     3dataset = fo.Dataset("custom-runs-example")
     4dataset.persistent = True
     5
     6config = dataset.init_run()
     7config.foo = "bar"  # add as many key-value pairs as you need
     8
     9# Also possible
    10# config = fo.RunConfig(foo="bar")
    11
    12dataset.register_run("custom", config)
    13
    14results = dataset.init_run_results("custom")
    15results.spam = "eggs"  # add as many key-value pairs as you need
    16
    17# Also possible
    18# results = fo.RunResults(dataset, config, "custom", spam="eggs")
    19
    20dataset.save_run_results("custom", results)
    

Note

[`RunConfig`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunConfig "fiftyone.core.runs.RunConfig") and [`RunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults "fiftyone.core.runs.RunResults") can store any JSON serializable values.

[`RunConfig`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunConfig "fiftyone.core.runs.RunConfig") documents must be less than 16MB, although they are generally far smaller as they are intended to store only a handful of simple parameters.

[`RunResults`](api__fiftyone.core.runs.md#fiftyone.core.runs.RunResults "fiftyone.core.runs.RunResults") instances are stored in [GridFS](https://www.mongodb.com/docs/manual/core/gridfs) and may exceed 16MB. They are only loaded when specifically accessed by a user.

You can access custom runs at any time as follows:
    
    
    1import fiftyone as fo
    2
    3dataset = fo.load_dataset("custom-runs-example")
    4
    5info = dataset.get_run_info("custom")
    6print(info)
    7
    8results = dataset.load_run_results("custom")
    9print(results)
    
    
    
    {
        "key": "custom",
        "version": "0.22.3",
        "timestamp": "2023-10-26T13:29:20.837595",
        "config": {
            "type": "run",
            "method": null,
            "cls": "fiftyone.core.runs.RunConfig",
            "foo": "bar"
        }
    }
    
    
    
    {
        "cls": "fiftyone.core.runs.RunResults",
        "spam": "eggs"
    }
    

### Managing custom runs#

FiftyOne provides a variety of methods that you can use to manage custom runs stored on datasets.

Call [`list_runs()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.list_runs "fiftyone.core.collections.SampleCollection.list_runs") to see the available custom run keys on a dataset:
    
    
    1dataset.list_runs()
    

Use [`get_run_info()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_run_info "fiftyone.core.collections.SampleCollection.get_run_info") to retrieve information about the configuration of a custom run:
    
    
    1info = dataset.get_run_info(run_key)
    2print(info)
    

Use [`init_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.init_run "fiftyone.core.collections.SampleCollection.init_run") and [`register_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.register_run "fiftyone.core.collections.SampleCollection.register_run") to create a new custom run on a dataset:
    
    
    1config = dataset.init_run()
    2config.foo = "bar"  # add as many key-value pairs as you need
    3
    4dataset.register_run(run_key, config)
    

Use [`update_run_config()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.update_run_config "fiftyone.core.collections.SampleCollection.update_run_config") to update the run config associated with an existing custom run:
    
    
    1dataset.update_run_config(run_key, config)
    

Use [`init_run_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.init_run_results "fiftyone.core.collections.SampleCollection.init_run_results") and [`save_run_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.save_run_results "fiftyone.core.collections.SampleCollection.save_run_results") to store run results for a custom run:
    
    
    1results = dataset.init_run_results(run_key)
    2results.spam = "eggs"  # add as many key-value pairs as you need
    3
    4dataset.save_run_results(run_key, results)
    5
    6# update existing results
    7dataset.save_run_results(run_key, results, overwrite=True)
    

Use [`load_run_results()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_run_results "fiftyone.core.collections.SampleCollection.load_run_results") to load the results for a custom run:
    
    
    1results = dataset.load_run_results(run_key)
    

Use [`rename_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.rename_run "fiftyone.core.collections.SampleCollection.rename_run") to rename the run key associated with an existing custom run:
    
    
    1dataset.rename_run(run_key, new_run_key)
    

Use [`delete_run()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.delete_run "fiftyone.core.collections.SampleCollection.delete_run") to delete the record of a custom run from a dataset:
    
    
    1dataset.delete_run(run_key)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
