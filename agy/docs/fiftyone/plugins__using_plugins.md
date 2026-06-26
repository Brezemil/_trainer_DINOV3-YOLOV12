---
source_url: https://docs.voxel51.com/plugins/using_plugins.html
---

# Using Plugins#

Every plugin that you download exposes one or more Panels and/or Operators that you can access from within the App.

Note

Check out the [Plugins Ecosystem](https://docs.voxel51.com/plugins/index.html#plugins-ecosystem) for a growing collection of plugins that you can easily download and use locally.

Then, after you get comfortable using existing plugins, try your hand at [writing your own](plugins__developing_plugins.md#developing-plugins)!

## Downloading plugins#

To download and use a plugin, all you need is the pluginâs GitHub repository or a link to a ZIP archive of the pluginâs source code.

You can download plugins using any of the methods described below:
    
    
    # Download plugin(s) from a GitHub repository
    fiftyone plugins download https://github.com/<user>/<repo>[/tree/branch]
    
    # Download plugin(s) by specifying the GitHub repository details
    fiftyone plugins download <user>/<repo>[/<ref>]
    
    # Download specific plugins from a GitHub repository
    fiftyone plugins download \
        https://github.com/<user>/<repo>[/tree/branch] \
        --plugin-names <name1> <name2> <name3>
    
    
    
     1import fiftyone.plugins as fop
     2
     3# Download plugin(s) from a GitHub repository
     4fop.download_plugin("https://github.com/<user>/<repo>[/tree/branch]")
     5
     6# Download plugin(b) by specifying the GitHub repository details
     7fop.download_plugin("<user>/<repo>[/<ref>]")
     8
     9# Download specific plugins from a GitHub repository
    10fop.download_plugin(url_or_gh_repo, plugin_names=["<name1>", "<name2>"])
    

Note

A GitHub repository may contain multiple plugins. By default, all plugins that are found within the first three directory levels are installed, but you can select specific ones if desired as shown above.

Note

All plugins are downloaded to your plugins directory.

Note

You can download plugins from private GitHub repositories that you have access to by providing your GitHub personal access token via the `GITHUB_TOKEN` environment variable.

## Your plugins directory#

All plugins must be stored and are automatically downloaded to your plugins directory in order for FiftyOne to find them.

By default, plugins are downloaded to `~/fiftyone/__plugins__`, but you can customize this directory by setting the `FIFTYONE_PLUGINS_DIR` environment variable:
    
    
    export FIFTYONE_PLUGINS_DIR=/path/to/your/plugins
    

You can also permanently configure this directory by adding it to your [FiftyOne config](user_guide__config.md#configuring-fiftyone).
    
    
    {
        "plugins_dir": "/path/to/your/plugins"
    }
    

You can locate your current plugins directory by running the following command:
    
    
    fiftyone config plugins_dir
    # ~/fiftyone/__plugins__
    

Note

Your plugins directory must be readable by the FiftyOne server.

## Managing plugins#

You can use the [fiftyone plugins](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins) and [fiftyone operators](https://docs.voxel51.com/cli/index.html#cli-fiftyone-operators) CLI methods to perform a variety of plugin-related actions.

### Listing plugins#

You can use the [fiftyone plugins list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-list) command to list the plugins that youâve downloaded or created locally:
    
    
    # List all locally available plugins
    fiftyone plugins list
    
    
    
    # List enabled plugins
    fiftyone plugins list --enabled
    
    
    
    # List disabled plugins
    fiftyone plugins list --disabled
    
    
    
    plugin               version   enabled  directory
    -------------------  -------  -------  ----------------------------------------------------------
    @voxel51/annotation  1.0.0    â        ~/fiftyone/__plugins__/fiftyone-plugins/plugins/annotation
    @voxel51/brain       1.0.0    â        ~/fiftyone/__plugins__/fiftyone-plugins/plugins/brain
    @voxel51/evaluation  1.0.0    â        ~/fiftyone/__plugins__/fiftyone-plugins/plugins/evaluation
    @voxel51/indexes     1.0.0    â        ~/fiftyone/__plugins__/fiftyone-plugins/plugins/indexes
    @voxel51/io          1.0.0    â        ~/fiftyone/__plugins__/fiftyone-plugins/plugins/io
    @voxel51/utils       1.0.0    â        ~/fiftyone/__plugins__/fiftyone-plugins/plugins/utils
    @voxel51/voxelgpt    1.0.0    â        ~/fiftyone/__plugins__/voxelgpt
    @voxel51/zoo         1.0.0    â        ~/fiftyone/__plugins__/fiftyone-plugins/plugins/zoo
    

### Listing operators#

You can use the [fiftyone operators list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-operators-list) command to list the individual operators and panels within the plugins that youâve installed locally:
    
    
    # List all available operators and panels
    fiftyone operators list
    
    
    
    # List enabled operators and panels
    fiftyone operators list --enabled
    
    
    
    # List disabled operators and panels
    fiftyone operators list --disabled
    
    
    
    # Only list panels
    fiftyone operators list --panels-only
    
    
    
    uri                                          enabled   builtin   panel   unlisted
    -------------------------------------------  --------  --------  ------  ---------
    @voxel51/annotation/request_annotations      â
    @voxel51/annotation/load_annotations         â
    @voxel51/annotation/get_annotation_info      â
    @voxel51/annotation/load_annotation_view     â
    @voxel51/annotation/rename_annotation_run    â
    @voxel51/annotation/delete_annotation_run    â
    @voxel51/brain/compute_visualization         â
    @voxel51/brain/compute_similarity            â
    @voxel51/brain/compute_uniqueness            â
    @voxel51/brain/compute_mistakenness          â
    @voxel51/brain/compute_hardness              â
    @voxel51/brain/get_brain_info                â
    @voxel51/brain/load_brain_view               â
    @voxel51/brain/rename_brain_run              â
    @voxel51/brain/delete_brain_run              â
    @voxel51/evaluation/evaluate_model           â
    @voxel51/evaluation/get_evaluation_info      â
    @voxel51/evaluation/load_evaluation_view     â
    @voxel51/evaluation/rename_evaluation        â
    @voxel51/evaluation/delete_evaluation        â
    @voxel51/io/import_samples                   â
    @voxel51/io/merge_samples                    â
    @voxel51/io/merge_labels                     â
    @voxel51/io/export_samples                   â
    @voxel51/io/draw_labels                      â
    @voxel51/operators/clone_selected_samples    â          â
    @voxel51/operators/clone_sample_field        â          â
    @voxel51/operators/rename_sample_field       â          â
    @voxel51/operators/delete_selected_samples   â          â
    @voxel51/operators/delete_sample_field       â          â
    @voxel51/operators/print_stdout              â          â                 â
    @voxel51/operators/list_files                â          â                 â
    @voxel51/utils/create_dataset                â
    @voxel51/utils/load_dataset                  â
    @voxel51/utils/edit_dataset_info             â
    @voxel51/utils/rename_dataset                â
    @voxel51/utils/delete_dataset                â
    @voxel51/utils/compute_metadata              â
    @voxel51/utils/generate_thumbnails           â
    @voxel51/utils/manage_plugins                â
    @voxel51/zoo/load_zoo_dataset                â
    @voxel51/zoo/apply_zoo_model                 â
    

### Downloading plugins#

You can use the [fiftyone plugins download](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-download) command to list the plugins that youâve downloaded or created locally:
    
    
    # Download plugins from a GitHub repository URL
    fiftyone plugins download <github-repo-url>
    
    
    
    # Download plugins by specifying the GitHub repository details
    fiftyone plugins download <user>/<repo>[/<ref>]
    
    
    
    # Download specific plugins from a URL with a custom search depth
    fiftyone plugins download \
        <url> \
        --plugin-names <name1> <name2> <name3> \
        --max-depth 2  # search nested directories for plugins
    

### Getting plugin info#

You can use the [fiftyone plugins info](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-info) command to view the available metadata about a plugin:
    
    
    fiftyone plugins info @voxel51/annotation
    
    
    
    key                     value
    ----------------------  --------------------------------------------------------------------
    name                    @voxel51/annotation
    author
    version                 1.0.0
    url                     https://github.com/voxel51/fiftyone-plugins/.../annotation/README.md
    license                 Apache 2.0
    description             Utilities for integrating FiftyOne with annotation tools
    fiftyone_compatibility  >=0.22
    operators               request_annotations
                            load_annotations
                            get_annotation_info
                            load_annotation_view
                            rename_annotation_run
                            delete_annotation_run
    js_bundle               dist/index.umd.js
    py_entry                __init__.py
    js_bundle_exists        False
    js_bundle_server_path
    has_py                  True
    has_js                  False
    server_path             /plugins/fiftyone-plugins/plugins/annotation
    secrets                 FIFTYONE_CVAT_URL
                            FIFTYONE_CVAT_USERNAME
                            FIFTYONE_CVAT_PASSWORD
                            FIFTYONE_CVAT_EMAIL
                            FIFTYONE_LABELBOX_URL
                            FIFTYONE_LABELBOX_API_KEY
                            FIFTYONE_LABELSTUDIO_URL
                            FIFTYONE_LABELSTUDIO_API_KEY
    directory               ~/fiftyone/__plugins__/fiftyone-plugins/plugins/annotation
    

### Getting operator info#

You can use the [fiftyone operators info](https://docs.voxel51.com/cli/index.html#cli-fiftyone-operators-info) to view the available metadata about an individual operator or panel within a plugin:
    
    
    fiftyone operators info @voxel51/io/import_samples
    
    
    
    key                                  value
    -----------------------------------  ----------------------
    name                                 import_samples
    label                                Import samples
    description
    execute_as_generator                 True
    unlisted                             False
    dynamic                              True
    on_startup                           False
    on_dataset_open                      False
    disable_schema_validation            False
    delegation_target
    icon
    dark_icon                            /assets/icon-dark.svg
    light_icon                           /assets/icon-light.svg
    allow_immediate_execution            True
    allow_delegated_execution            False
    default_choice_to_delegated          False
    resolve_execution_options_on_change  True
    

### Installing plugin requirements#

You can use the [fiftyone plugins requirements](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-requirements) command to view, install, and ensure installation of a pluginâs requirements:
    
    
    # Print requirements for a plugin
    fiftyone plugins requirements <name> --print
    
    
    
    # Install any requirements for the plugin
    fiftyone plugins requirements <name> --install
    
    
    
    # Ensures that the requirements for the plugin are satisfied
    fiftyone plugins requirements <name> --ensure
    

### Enabling and disabling plugins#

You can use the [fiftyone plugins enable](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-enable) and [fiftyone plugins disable](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-disable) commands to enable and disable plugins that youâve downloaded:
    
    
    # Enable a plugin
    fiftyone plugins enable <name>
    
    # Enable multiple plugins
    fiftyone plugins enable <name1> <name2> ...
    
    # Enable all plugins
    fiftyone plugins enable --all
    
    
    
    # Disable a plugin
    fiftyone plugins disable <name>
    
    # Disable multiple plugins
    fiftyone plugins disable <name1> <name2> ...
    
    # Disable all plugins
    fiftyone plugins disable --all
    

Note

Operators associated with disabled plugins will not appear in the Appâs operator browser.

Plugin disablement is stored as an `enabled: false` entry in the pluginâs config settings.
    
    
    fiftyone plugins disable @voxel51/zoo
    fiftyone app config plugins
    
    
    
    {
        "map": {
            "mapboxAccessToken": "XXXXXXXX"
        },
        "@voxel51/zoo": {
            "enabled": false
        },
        ...
    }
    

### Deleting plugins#

You can use the [fiftyone plugins delete](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-delete) command to delete plugins from your local machine.
    
    
    # Delete a plugin from local disk
    fiftyone plugins delete <name>
    
    
    
    # Delete multiple plugins from local disk
    fiftyone plugins delete <name1> <name2> ...
    
    
    
    # Delete all plugins from local disk
    fiftyone plugins delete --all
    

## Configuring plugins#

Certain plugins support configuration. For those plugins, you can store:

  * System-wide plugin settings under the `plugins` key of your [App config](user_guide__config.md#configuring-fiftyone-app)

  * Dataset-specific plugin settings for any subset of the above values on a [datasetâs App config](https://docs.voxel51.com/user_guide/using_datasets.html#dataset-app-config).




See the [configuring plugins](user_guide__config.md#configuring-plugins) page for more information.

## Plugin secrets#

Some plugins may require sensitive information such as API tokens and login credentials in order to function. Any secrets that a plugin requires are documented under the `secrets` key of its `fiftyone.yml` file.

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
    

Note

You can use the [fiftyone plugins info](https://docs.voxel51.com/cli/index.html#cli-fiftyone-plugins-info) CLI command to print information about a plugin, including its required secrets.

As the naming convention implies, any necessary secrets are provided by setting environment variables with the appropriate names. For example, if you want to use the CVAT backend with the [@voxel51/annotation](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/annotation/fiftyone.yml) plugin, you would set:
    
    
    FIFTYONE_CVAT_URL=...
    FIFTYONE_CVAT_USERNAME=...
    FIFTYONE_CVAT_PASSWORD=...
    FIFTYONE_CVAT_EMAIL=...
    

At runtime, the pluginâs execution context will automatically be hydrated with any available secrets that are declared by the plugin. Operators access these secrets via the `ctx.secrets` dict:
    
    
    1def execute(self, ctx):
    2    url = ctx.secrets["FIFTYONE_CVAT_URL"]
    3    username = ctx.secrets["FIFTYONE_CVAT_USERNAME"]
    4    password = ctx.secrets["FIFTYONE_CVAT_PASSWORD"]
    5    email = ctx.secrets["FIFTYONE_CVAT_EMAIL"]
    

## Using panels#

Panels are miniature full-featured data applications that you can open in [App Spaces](user_guide__app.md#app-spaces) and interactively manipulate to explore your dataset and update/respond to updates from other spaces that are currently open in the App.

FiftyOne natively includes the following Panels:

  * [Samples panel](user_guide__app.md#app-samples-panel): the media grid that loads by default when you launch the App

  * [Histograms panel](user_guide__app.md#app-histograms-panel): a dashboard of histograms for the fields of your dataset

  * [Embeddings panel](user_guide__app.md#app-embeddings-panel): a canvas for working with [embeddings visualizations](brain.md#brain-embeddings-visualization)

  * [Map panel](user_guide__app.md#app-map-panel): visualizes the geolocation data of datasets that have a [`GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") field




Any plugins that youâve installed may expose additional panels too.

Click the `+` icon next to the âSamplesâ tab to open a new panel:

![../_images/app-map-panel.gif](../_images/app-map-panel.gif)

Note

Did you know? You can also programmatically configure spaces [in Python](user_guide__app.md#app-spaces-python).

## Using operators#

Operators are a powerful feature in FiftyOne that allow plugin developers to define custom operations that can be executed from within the App.

Some operators may expose themselves as custom buttons, icons, or menu items throughout the App. However, the Operator Browser allows users to search through all available (enabled) operators.

You can open the Operator Browser by clicking on the Operator Browser icon above the sample grid or by typing backtick (```):

![../_images/operator-browser.gif](../_images/operator-browser.gif)

Operators provide dynamic input forms that collect the necessary user inputs. The actual operation is then performed by pressing the `Execute`/`Schedule` button at the bottom of the form.

Some Operators perform an immediate action when executed, while other Operators delegate their execution to another process.

## Executing operators via SDK#

Many operators are intended to be executed programmatically via the SDK rather than (or in addition to) executing them by filling out their input form in the App.

### Calling operators#

By convention, operators that are intended to be executed programmatically should implement `__call__()` so that users have a well-documented interface for invoking the operator as a function.

For example, the [@voxel51/utils/compute_metadata](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/utils) operator can be invoked like so:
    
    
    1import fiftyone as fo
    2import fiftyone.operators as foo
    3import fiftyone.zoo as foz
    4
    5dataset = foz.load_zoo_dataset("quickstart")
    6compute_metadata = foo.get_operator("@voxel51/utils/compute_metadata")
    7
    8# (Re)compute the dataset's metadata
    9compute_metadata(dataset, overwrite=True)
    

Note

Notice that [`get_operator()`](api__fiftyone.operators.md#fiftyone.operators.get_operator "fiftyone.operators.get_operator") is used to retrieve the operator by its URI.

Behind the scenes, the operatorâs `__call__()` method is implemented as follows:
    
    
     1class ComputeMetadata(foo.Operator):
     2    def __call__(
     3        self,
     4        sample_collection,
     5        overwrite=False,
     6        num_workers=None,
     7    ):
     8        ctx = dict(view=sample_collection.view())
     9        params = dict(
    10            overwrite=overwrite,
    11            num_workers=num_workers,
    12        )
    13        return foo.execute_operator(self.uri, ctx, params=params)
    

which simply packages up the provided keyword arguments into the correct format for the operatorâs `ctx.params` and then passes them to [`execute_operator()`](api__fiftyone.operators.md#fiftyone.operators.execute_operator "fiftyone.operators.execute_operator"), which performs the execution.

For operators whose [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") method returns data, you can access it via the `result` property of the returned [`ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") object:
    
    
    1op = foo.get_operator("@an-operator/with-results")
    2
    3result = op(...)
    4print(result.result) # {...}
    

Note

When working in notebook contexts, executing operators returns an `asyncio.Task` that you can `await` to retrieve the [`ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult"):
    
    
    op = foo.get_operator("@an-operator/with-results")
    
    result = await op(...)
    print(result.result) # {...}
    

#### Requesting delegation#

Operators that support delegated execution can support this via the `__call__()` syntax by passing the `request_delegation=True` flag to [`execute_operator()`](api__fiftyone.operators.md#fiftyone.operators.execute_operator "fiftyone.operators.execute_operator").

In fact, the [@voxel51/utils/compute_metadata](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/utils) operator does just that:
    
    
     1class ComputeMetadata(foo.Operator):
     2    return foo.OperatorConfig(
     3        ...
     4        allow_immediate_execution=True,
     5        allow_delegated_execution=True,
     6    )
     7
     8    def __call__(
     9        self,
    10        sample_collection,
    11        overwrite=False,
    12        num_workers=None,
    13        delegate=False,
    14    ):
    15        ctx = dict(view=sample_collection.view())
    16        params = dict(
    17            overwrite=overwrite,
    18            num_workers=num_workers,
    19        )
    20        return foo.execute_operator(
    21            self.uri,
    22            ctx,
    23            params=params,
    24            request_delegation=delegate,
    25        )
    

which means that it can be invoked like so:
    
    
    1compute_metadata = foo.get_operator("@voxel51/utils/compute_metadata")
    2
    3# Schedule a delegated operation to (re)compute metadata
    4compute_metadata(dataset, overwrite=True, delegate=True)
    

### Direct execution#

You can programmatically execute any operator by directly calling [`execute_operator()`](api__fiftyone.operators.md#fiftyone.operators.execute_operator "fiftyone.operators.execute_operator"):
    
    
     1import fiftyone as fo
     2import fiftyone.operators as foo
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6
     7ctx = {
     8    "view": dataset.take(10),
     9    "params": dict(
    10        export_type="LABELS_ONLY",
    11        dataset_type="COCO",
    12        labels_path=dict(absolute_path="/tmp/coco/labels.json"),
    13        label_field="ground_truth",
    14    )
    15}
    16
    17foo.execute_operator("@voxel51/io/export_samples", ctx)
    

Note

In general, to use [`execute_operator()`](api__fiftyone.operators.md#fiftyone.operators.execute_operator "fiftyone.operators.execute_operator") you must inspect the operatorâs [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") implementation to understand what parameters are required.

For operators whose [`execute()`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator.execute "fiftyone.operators.operator.Operator.execute") method returns data, you can access it via the `result` property of the returned [`ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult") object:
    
    
    1result = foo.execute_operator("@an-operator/with-results", ctx)
    2print(result.result)  # {...}
    

Note

When working in notebook contexts, executing operators returns an `asyncio.Task` that you can `await` to retrieve the [`ExecutionResult`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionResult "fiftyone.operators.executor.ExecutionResult"):
    
    
    result = await foo.execute_operator("@an-operator/with-results", ctx)
    print(result.result)  # {...}
    

#### Requesting delegation#

If an operation supports both immediate and delegated execution as specified by its [execution options](plugins__developing_plugins.md#operator-execution-options), you can request delegated execution by passing the `request_delegation=True` flag to [`execute_operator()`](api__fiftyone.operators.md#fiftyone.operators.execute_operator "fiftyone.operators.execute_operator"):
    
    
    1foo.execute_operator(operator_uri, ctx=ctx, request_delegation=True)
    

This has the same effect as choosing `Schedule` from the dropdown in the operatorâs input modal when executing it from within the App:

![../_images/operator-execute-button.png](../_images/operator-execute-button.png)

Note

[FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise) users can also specify an optional delegation target for their delegated operations:
    
    
    foo.execute_operator(
        operator_uri,
        ctx=ctx,
        request_delegation=True,
        delegation_target="overnight",
    )
    

### Delegating function calls#

The [@voxel51/utils/delegate](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/utils) operator provides a general purpose utility for delegating execution of an arbitrary function call that can be expressed in any of the following forms:

  * Execute an arbitrary function: `fcn(*args, **kwargs)`

  * Apply a function to a dataset or view: `fcn(dataset_or_view, *args, **kwargs)`

  * Call an instance method of a dataset or view: `dataset_or_view.fcn(*args, **kwargs)`




Hereâs some examples of delegating common tasks that can be expressed in the above forms:
    
    
     1import fiftyone as fo
     2import fiftyone.operators as foo
     3import fiftyone.zoo as foz
     4
     5dataset = foz.load_zoo_dataset("quickstart")
     6delegate = foo.get_operator("@voxel51/utils/delegate")
     7
     8# Compute metadata
     9delegate("compute_metadata", dataset=dataset)
    10
    11# Compute visualization
    12delegate(
    13    "fiftyone.brain.compute_visualization",
    14    dataset=dataset,
    15    brain_key="img_viz",
    16)
    17
    18# Export a view
    19delegate(
    20    "export",
    21    view=dataset.to_patches("ground_truth"),
    22    export_dir="/tmp/patches",
    23    dataset_type="fiftyone.types.ImageClassificationDirectoryTree",
    24    label_field="ground_truth",
    25)
    26
    27# Load the exported patches into a new dataset
    28delegate(
    29    "fiftyone.Dataset.from_dir",
    30    dataset_dir="/tmp/patches",
    31    dataset_type="fiftyone.types.ImageClassificationDirectoryTree",
    32    label_field="ground_truth",
    33    name="patches",
    34    persistent=True,
    35)
    

## Delegated operations#

Delegated operations are a powerful feature of FiftyOneâs plugin framework that allows you to schedule potentially long-running tasks from within the App that are executed in the background while you continue to work.

Note

[FiftyOne Enterprise](enterprise__plugins.md#enterprise-delegated-operations) deployments come out of the box with a connected compute cluster for executing delegated operations at scale.

In FiftyOne Open Source, you can use delegated operations at small scale by running them locally.

For example, have model predictions on your dataset that you want to evaluate? The [@voxel51/evaluation](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/evaluation/README.md) plugin makes it easy:

![../_images/evaluation.gif](../_images/evaluation.gif)

Need to compute embedding for your dataset so you can visualize them in the [Embeddings panel](user_guide__app.md#app-embeddings-panel)? Kick off the task with the [@voxel51/brain](https://github.com/voxel51/fiftyone-plugins/blob/main/plugins/brain/README.md) plugin and proceed with other work while the execution happens in the background:

![../_images/embeddings.gif](../_images/embeddings.gif)

Why is this awesome? Your AI stack needs a flexible data-centric component that enables you to organize and compute on your data. With delegated operations, FiftyOne becomes both a dataset management/visualization tool and a workflow automation tool that defines how your data-centric workflows like ingestion, curation, and evaluation are performed.

Note

Want to run delegated operations at scale? [Contact us](https://voxel51.com/talk-to-sales) about [FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise), an open source-compatible enterprise deployment of FiftyOne with multiuser collaboration features, native cloud dataset support, and much more!

Think of FiftyOne Enterprise as the single source of truth on which you co-develop your data and models together ð

## Setting up an orchestrator#

### FiftyOne Open Source#

FiftyOne Open Source users can run delegated operations via the [fiftyone delegated launch](https://docs.voxel51.com/cli/index.html#cli-fiftyone-delegated-launch) CLI command:
    
    
    fiftyone delegated launch
    

This command starts a service that will continuously check for any queued delegated operations and execute them serially in its process.

You must also ensure that the [allow_legacy_orchestrators](user_guide__config.md#configuring-fiftyone) config flag is set in the environment where you run the App/SDK, e.g. by setting:
    
    
    export FIFTYONE_ALLOW_LEGACY_ORCHESTRATORS=true
    

### FiftyOne Enterprise#

[FiftyOne Enterprise](enterprise__plugins.md#enterprise-delegated-operations) deployments come out of the box with a connected compute cluster for executing delegated operations at scale. They can also be connected to your own compute solution, such as Databricks or Anyscale.

This powerful feature allows users to install/build plugins that execute potentially long-running tasks in the background while users continue with other work in the App.

Note

Want to take advantage of this functionality? [Contact us](https://voxel51.com/talk-to-sales) about [FiftyOne Enterprise](https://docs.voxel51.com/enterprise/index.html#fiftyone-enterprise), an open source-compatible enterprise deployment of FiftyOne with multiuser collaboration features, native cloud dataset support, and much more!

Think of FiftyOne Enterprise as the single source of truth on which you co-develop your data and models together ð

## Managing delegated operations#

The [fiftyone delegated](https://docs.voxel51.com/cli/index.html#cli-fiftyone-delegated) CLI command contains a number of useful utilities for viewing the status of your delegated operations.

### Listing delegated operations#

You can use the [fiftyone delegated list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-delegated-list) command to list the delegated operations that youâve run:
    
    
    # List all delegated operations
    fiftyone delegated list
    
    
    
    # List some specific delegated operations
    fiftyone delegated list \
        --dataset quickstart \
        --operator @voxel51/io/export_samples \
        --state COMPLETED \
        --sort-by COMPLETED_AT \
        --limit 10
    

### Getting delegated operation info#

You can use the [fiftyone delegated info](https://docs.voxel51.com/cli/index.html#cli-fiftyone-delegated-info) command to view the available metadata about a delegated operation, including its inputs, execution status, and error stack trace, if applicable.
    
    
    # Print information about a delegated operation
    fiftyone delegated info <id>
    

### Cleaning up delegated operations#

You can use the [fiftyone delegated cleanup](https://docs.voxel51.com/cli/index.html#cli-fiftyone-delegated-cleanup) command to cleanup delegated operations:
    
    
    # Delete all failed operations associated with a given dataset
    fiftyone delegated cleanup --dataset quickstart --state FAILED
    
    
    
    # Delete all delegated operations associated with non-existent datasets
    fiftyone delegated cleanup --orphan
    
    
    
    # Print information about operations rather than actually deleting them
    fiftyone delegated cleanup --orphan --dry-run
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
