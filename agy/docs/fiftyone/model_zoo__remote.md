---
source_url: https://docs.voxel51.com/model_zoo/remote.html
---

# Remotely-Sourced Zoo Models#

This page describes how to work with and create zoo models whose definitions are hosted via GitHub repositories or public URLs.

Note

To download from a private GitHub repository that you have access to, provide your GitHub personal access token by setting the `GITHUB_TOKEN` environment variable.

Note

Check out [voxel51/openai-clip](https://github.com/voxel51/openai-clip) and [voxel51/ultralytics-models](https://github.com/voxel51/ultralytics-models) for examples of remote model sources.

## Working with remotely-sourced models#

Working with remotely-sourced zoo models is just like [built-in zoo models](https://docs.voxel51.com/model_zoo/index.html#model-zoo), as both varieties support the [full zoo API](model_zoo__api.md#model-zoo-api).

When specifying remote sources, you can provide any of the following:

  * A GitHub repo URL like `https://github.com/<user>/<repo>`

  * A GitHub ref like `https://github.com/<user>/<repo>/tree/<branch>` or `https://github.com/<user>/<repo>/commit/<commit>`

  * A GitHub ref string like `<user>/<repo>[/<ref>]`

  * A publicly accessible URL of an archive (eg zip or tar) file




Hereâs the basic recipe for working with remotely-sourced zoo models:

Use [`register_zoo_model_source()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.register_zoo_model_source "fiftyone.zoo.models.register_zoo_model_source") to register a remote source of zoo models:
    
    
    1import fiftyone as fo
    2import fiftyone.zoo as foz
    3
    4foz.register_zoo_model_source("https://github.com/voxel51/openai-clip")
    

Use [`list_zoo_model_sources()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.list_zoo_model_sources "fiftyone.zoo.models.list_zoo_model_sources") to list all remote sources that have been registered locally:
    
    
    1remote_sources = foz.list_zoo_model_sources()
    2
    3print(remote_sources)
    4# [..., "https://github.com/voxel51/openai-clip", ...]
    

Once youâve registered a remote source, any models that it declares will subsequently appear as available zoo models when you call [`list_zoo_models()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.list_zoo_models "fiftyone.zoo.models.list_zoo_models"):
    
    
    1available_models = foz.list_zoo_models()
    2
    3print(available_models)
    4# [..., "voxel51/clip-vit-base32-torch", ...]
    

You can download a remote zoo model by calling [`download_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.download_zoo_model "fiftyone.zoo.models.download_zoo_model"):
    
    
    1foz.download_zoo_model("voxel51/clip-vit-base32-torch")
    

You can also directly download a remote zoo model and implicitly register its source via the following syntax:
    
    
    1foz.download_zoo_model(
    2    "https://github.com/voxel51/openai-clip",
    3    model_name="voxel51/clip-vit-base32-torch",
    4)
    

You can load a remote zoo model and apply it to a dataset or view via [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model") and [`apply_model()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.apply_model "fiftyone.core.collections.SampleCollection.apply_model"):
    
    
    1dataset = foz.load_zoo_dataset("quickstart")
    2model = foz.load_zoo_model("voxel51/clip-vit-base32-torch")
    3
    4dataset.apply_model(model, label_field="clip")
    

You can delete the local copy of a remotely-sourced zoo model via [`delete_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.delete_zoo_model "fiftyone.zoo.models.delete_zoo_model"):
    
    
    1foz.delete_zoo_model("voxel51/clip-vit-base32-torch")
    

You can unregister a remote source of zoo models and delete any local copies of models that it declares via [`delete_zoo_model_source()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.delete_zoo_model_source "fiftyone.zoo.models.delete_zoo_model_source"):
    
    
    1foz.delete_zoo_model_source("https://github.com/voxel51/openai-clip")
    

Use [fiftyone zoo models register-source](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-register-source) to register a remote source of zoo models:
    
    
    fiftyone zoo models register-source \
        https://github.com/voxel51/openai-clip
    

Use [fiftyone zoo models list-sources](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-list-sources) to list all remote sources that have been registered locally:
    
    
    fiftyone zoo models list-sources
    
    # contains a row for 'https://github.com/voxel51/openai-clip'
    

Once youâve registered a remote source, any models that it declares will subsequently appear as available zoo models when you call [fiftyone zoo models list](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-list):
    
    
    fiftyone zoo models list
    
    # contains a row for 'voxel51/clip-vit-base32-torch'
    

You can download a remote zoo model by calling [fiftyone zoo models download](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-download):
    
    
    fiftyone zoo models download voxel51/clip-vit-base32-torch
    

You can also directly download a remote zoo model and implicitly register its source via the following syntax:
    
    
    fiftyone zoo models \
        download https://github.com/voxel51/openai-clip \
        --model-name voxel51/clip-vit-base32-torch
    

You can load a remote zoo model and apply it to a dataset via [fiftyone zoo models apply](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-apply):
    
    
    MODEL_NAME=voxel51/clip-vit-base32-torch
    DATASET_NAME=quickstart
    LABEL_FIELD=clip
    
    fiftyone zoo models apply $MODEL_NAME $DATASET_NAME $LABEL_FIELD
    

You can delete the local copy of a remotely-sourced zoo model via [fiftyone zoo models delete](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-delete):
    
    
    fiftyone zoo models delete voxel51/clip-vit-base32-torch
    

You can unregister a remote source of zoo models and delete any local copies of models that it declares via [fiftyone zoo models delete-source](https://docs.voxel51.com/cli/index.html#cli-fiftyone-zoo-models-delete-source):
    
    
    fiftyone zoo models delete-source https://github.com/voxel51/openai-clip
    

## Creating remotely-sourced models#

A remote source of models is defined by a directory with the following contents:
    
    
    manifest.json
    __init__.py
        def download_model(model_name, model_path):
            pass
    
        def load_model(model_name, model_path, **kwargs):
            pass
    
        def resolve_input(model_name, ctx):
            pass
    
        def parse_parameters(model_name, ctx, params):
            pass
    

Each component is described in detail below.

Note

By convention, model sources also contain an optional `README.md` file that provides additional information about the models that it contains and example syntaxes for downloading and working with them.

### manifest.json#

The remote sourceâs `manifest.json` file defines relevant metadata about the model(s) that it contains:

Field | Required? | Description  
---|---|---  
`base_name` | **yes** | The base name of the model (no version info)  
`base_filename` |  | The base filename or directory of the model (no version info), if applicable. This is required in order for [`list_downloaded_zoo_models()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.list_downloaded_zoo_models "fiftyone.zoo.models.list_downloaded_zoo_models") to detect the model and [`delete_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.delete_zoo_model "fiftyone.zoo.models.delete_zoo_model") to delete the local copy if it is downloaded  
`author` |  | The author of the model  
`version` |  | The version of the model (if applicable). If a version is provided, then users can refer to a specific version of the model by appending `@<ver>` to its name when using methods like [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model"), otherwise the latest version of the model is loaded by default  
`url` |  | The URL at which the model is hosted  
`license` |  | The license under which the model is distributed  
`source` |  | The original source of the model  
`description` |  | A brief description of the model  
`tags` |  | A list of tags for the model. Useful in conjunction with [`list_zoo_models()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.list_zoo_models "fiftyone.zoo.models.list_zoo_models")  
`size_bytes` |  | The size of the model on disk  
`date_added` |  | The time that the model was added to the source  
`requirements` |  | JSON description of the modelâs package/runtime requirements  
`manager` |  | A [`fiftyone.core.models.ModelManagerConfig`](api__fiftyone.core.models.md#fiftyone.core.models.ModelManagerConfig "fiftyone.core.models.ModelManagerConfig") dict that describes the remote location of the model and how to download it. If this is not provided, then a download_model() function must be provided  
`default_deployment_config_dict` |  | A [`fiftyone.core.models.ModelConfig`](api__fiftyone.core.models.md#fiftyone.core.models.ModelConfig "fiftyone.core.models.ModelConfig") dict describing how to load the model. If this is not provided, then a load_model() function must be provided  
  
It can also provide optional metadata about the remote source itself:

Field | Required? | Description  
---|---|---  
`name` |  | A name for the remote model source  
`url` |  | The URL of the remote model source  
  
Hereâs an example model manifest file that declares a single model:
    
    
    {
        "name": "voxel51/openai-clip",
        "url": "https://github.com/voxel51/openai-clip",
        "models": [
            {
                "base_name": "voxel51/clip-vit-base32-torch",
                "base_filename": "CLIP-ViT-B-32.pt",
                "author": "OpenAI",
                "license": "MIT",
                "source": "https://github.com/openai/CLIP",
                "description": "CLIP text/image encoder from Learning Transferable Visual Models From Natural Language Supervision (https://arxiv.org/abs/2103.00020) trained on 400M text-image pairs",
                "tags": [
                    "classification",
                    "logits",
                    "embeddings",
                    "torch",
                    "clip",
                    "zero-shot"
                ],
                "size_bytes": 353976522,
                "date_added": "2022-04-12 17:49:51",
                "requirements": {
                    "packages": ["torch", "torchvision"],
                    "cpu": {
                        "support": true
                    },
                    "gpu": {
                        "support": true
                    }
                }
            }
        ]
    }
    

### Download model#

If a remote source contains model(s) that donât use the `manager` key in its manifest, then it must contain an `__init__.py` file that defines a `download_model()` method with the signature below:
    
    
     1def download_model(model_name, model_path):
     2    """Downloads the model.
     3
     4    Args:
     5        model_name: the name of the model to download, as declared by the
     6            ``base_name`` and optional ``version`` fields of the manifest
     7        model_path: the absolute filename or directory to which to download the
     8            model, as declared by the ``base_filename`` field of the manifest
     9    """
    10
    11    # Determine where to download `model_name` from
    12    url = ...
    13
    14    # Download `url` to `model_path`
    15    ...
    

This method is called under-the-hood when a user calls [`download_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.download_zoo_model "fiftyone.zoo.models.download_zoo_model") or [`load_zoo_model()`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model"), and its job is to download any relevant files from the web and organize and/or prepare them as necessary at the provided path.

### Load model#

If a remote source contains model(s) that donât use the `default_deployment_config_dict` key in its manifest, then it must contain an `__init__.py` file that defines a `load_model()` method with the signature below:
    
    
     1def load_model(model_name, model_path, **kwargs):
     2    """Loads the model.
     3
     4    Args:
     5        model_name: the name of the model to load, as declared by the
     6            ``base_name`` and optional ``version`` fields of the manifest
     7        model_path: the absolute filename or directory to which the model was
     8            downloaded, as declared by the ``base_filename`` field of the
     9            manifest
    10        **kwargs: optional keyword arguments that configure how the model
    11            is loaded
    12
    13    Returns:
    14        a :class:`fiftyone.core.models.Model`
    15    """
    16
    17    # The directory containing this file
    18    model_dir = os.path.dirname(model_path)
    19
    20    # Construct the specified `Model` instance, generally by importing
    21    # other modules in `model_dir`
    22    model = ...
    23
    24    return model
    

This methodâs job is to load the [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") instance for the specified model whose associated weights are stored at the provided path.

Note

Refer to [this page](model_zoo__design.md#model-zoo-design-overview) for more information about wrapping models in the [`Model`](api__fiftyone.core.models.md#fiftyone.core.models.Model "fiftyone.core.models.Model") interface.

Remotely-sourced models can optionally support customized loading by accepting optional keyword arguments to their `load_model()` method.

When [`load_zoo_model(name_or_url, ..., **kwargs)`](api__fiftyone.zoo.models.md#fiftyone.zoo.models.load_zoo_model "fiftyone.zoo.models.load_zoo_model") is called, any `kwargs` are passed through to `load_model(..., **kwargs)`.

### Resolve input#

If a remote source contains model(s) that support custom parameters, then the `__init__.py` file can define a `resolve_input()` method with the signature below that defines any necessary properties to collect the modelâs custom parameters from a user when the model is invoked [via an operator](plugins__using_plugins.md#using-operators):
    
    
     1from fiftyone.operators import types
     2
     3def resolve_input(model_name, ctx):
     4    """Defines any necessary properties to collect the model's custom
     5    parameters from a user during prompting.
     6
     7    Args:
     8        model_name: the name of the model, as declared by the ``base_name`` and
     9            optional ``version`` fields of the manifest
    10        ctx: an :class:`fiftyone.operators.ExecutionContext`
    11
    12    Returns:
    13        a :class:`fiftyone.operators.types.Property`, or None
    14    """
    15    inputs = types.Object()
    16    inputs.list(
    17        "classes",
    18        types.String(),
    19        required=False,
    20        default=None,
    21        label="Zero shot classes",
    22        description=(
    23            "An optional list of custom classes for zero-shot prediction"
    24        ),
    25        view=types.AutocompleteView(),
    26    )
    27    return types.Property(inputs)
    

Note

Refer to [this section](plugins__developing_plugins.md#operator-inputs) for more information about collecting user inputs for operators.

### Parse parameters#

If a remote source contains model(s) that support custom parameters, then the `__init__.py` file can define a `parse_parameters()` method with the signature below that performs any execution-time formatting to the modelâs custom parameters when the model is invoked [via an operator](plugins__using_plugins.md#using-operators):
    
    
     1def parse_parameters(model_name, ctx, params):
     2    """Performs any execution-time formatting to the model's custom parameters.
     3
     4    Args:
     5        model_name: the name of the model, as declared by the ``base_name`` and
     6            optional ``version`` fields of the manifest
     7        ctx: an :class:`fiftyone.operators.ExecutionContext`
     8        params: a params dict
     9    """
    10    classes = params.get("classes", None)
    11    if isinstance(classes, str):
    12        params["classes"] = classes.split(",")
    

Note

Refer to [this section](plugins__developing_plugins.md#operator-inputs) for more information about collecting user inputs for operators.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
