---
source_url: https://docs.voxel51.com/plugins/api/plugins.operators.model_evaluation.html
---

# plugins.operators.model_evaluation#

  * [plugins.operators.model_evaluation.utils](plugins__api__plugins.operators.model_evaluation.utils.md)
    * [`CustomCodeViewReason`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason)
      * [`CustomCodeViewReason.TOO_MANY_CATEGORIES`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.TOO_MANY_CATEGORIES)
      * [`CustomCodeViewReason.TOO_MANY_INT_CATEGORIES`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.TOO_MANY_INT_CATEGORIES)
      * [`CustomCodeViewReason.FLOAT_TYPE`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.FLOAT_TYPE)
      * [`CustomCodeViewReason.SLOW`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.SLOW)
      * [`CustomCodeViewReason.encode()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.encode)
      * [`CustomCodeViewReason.replace()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.replace)
      * [`CustomCodeViewReason.split()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.split)
      * [`CustomCodeViewReason.rsplit()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.rsplit)
      * [`CustomCodeViewReason.join()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.join)
      * [`CustomCodeViewReason.capitalize()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.capitalize)
      * [`CustomCodeViewReason.casefold()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.casefold)
      * [`CustomCodeViewReason.title()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.title)
      * [`CustomCodeViewReason.center()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.center)
      * [`CustomCodeViewReason.count()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.count)
      * [`CustomCodeViewReason.expandtabs()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.expandtabs)
      * [`CustomCodeViewReason.find()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.find)
      * [`CustomCodeViewReason.partition()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.partition)
      * [`CustomCodeViewReason.index()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.index)
      * [`CustomCodeViewReason.ljust()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.ljust)
      * [`CustomCodeViewReason.lower()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.lower)
      * [`CustomCodeViewReason.lstrip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.lstrip)
      * [`CustomCodeViewReason.rfind()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.rfind)
      * [`CustomCodeViewReason.rindex()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.rindex)
      * [`CustomCodeViewReason.rjust()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.rjust)
      * [`CustomCodeViewReason.rstrip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.rstrip)
      * [`CustomCodeViewReason.rpartition()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.rpartition)
      * [`CustomCodeViewReason.splitlines()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.splitlines)
      * [`CustomCodeViewReason.strip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.strip)
      * [`CustomCodeViewReason.swapcase()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.swapcase)
      * [`CustomCodeViewReason.translate()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.translate)
      * [`CustomCodeViewReason.upper()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.upper)
      * [`CustomCodeViewReason.startswith()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.startswith)
      * [`CustomCodeViewReason.endswith()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.endswith)
      * [`CustomCodeViewReason.removeprefix()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.removeprefix)
      * [`CustomCodeViewReason.removesuffix()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.removesuffix)
      * [`CustomCodeViewReason.isascii()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isascii)
      * [`CustomCodeViewReason.islower()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.islower)
      * [`CustomCodeViewReason.isupper()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isupper)
      * [`CustomCodeViewReason.istitle()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.istitle)
      * [`CustomCodeViewReason.isspace()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isspace)
      * [`CustomCodeViewReason.isdecimal()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isdecimal)
      * [`CustomCodeViewReason.isdigit()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isdigit)
      * [`CustomCodeViewReason.isnumeric()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isnumeric)
      * [`CustomCodeViewReason.isalpha()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isalpha)
      * [`CustomCodeViewReason.isalnum()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isalnum)
      * [`CustomCodeViewReason.isidentifier()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isidentifier)
      * [`CustomCodeViewReason.isprintable()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.isprintable)
      * [`CustomCodeViewReason.zfill()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.zfill)
      * [`CustomCodeViewReason.format()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.format)
      * [`CustomCodeViewReason.format_map()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.format_map)
      * [`CustomCodeViewReason.maketrans()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.CustomCodeViewReason.maketrans)
    * [`ShowOptionsMethod`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod)
      * [`ShowOptionsMethod.CODE`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.CODE)
      * [`ShowOptionsMethod.CHECKBOX`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.CHECKBOX)
      * [`ShowOptionsMethod.EMPTY`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.EMPTY)
      * [`ShowOptionsMethod.AUTOCOMPLETE`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.AUTOCOMPLETE)
      * [`ShowOptionsMethod.encode()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.encode)
      * [`ShowOptionsMethod.replace()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.replace)
      * [`ShowOptionsMethod.split()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.split)
      * [`ShowOptionsMethod.rsplit()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.rsplit)
      * [`ShowOptionsMethod.join()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.join)
      * [`ShowOptionsMethod.capitalize()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.capitalize)
      * [`ShowOptionsMethod.casefold()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.casefold)
      * [`ShowOptionsMethod.title()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.title)
      * [`ShowOptionsMethod.center()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.center)
      * [`ShowOptionsMethod.count()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.count)
      * [`ShowOptionsMethod.expandtabs()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.expandtabs)
      * [`ShowOptionsMethod.find()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.find)
      * [`ShowOptionsMethod.partition()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.partition)
      * [`ShowOptionsMethod.index()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.index)
      * [`ShowOptionsMethod.ljust()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.ljust)
      * [`ShowOptionsMethod.lower()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.lower)
      * [`ShowOptionsMethod.lstrip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.lstrip)
      * [`ShowOptionsMethod.rfind()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.rfind)
      * [`ShowOptionsMethod.rindex()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.rindex)
      * [`ShowOptionsMethod.rjust()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.rjust)
      * [`ShowOptionsMethod.rstrip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.rstrip)
      * [`ShowOptionsMethod.rpartition()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.rpartition)
      * [`ShowOptionsMethod.splitlines()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.splitlines)
      * [`ShowOptionsMethod.strip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.strip)
      * [`ShowOptionsMethod.swapcase()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.swapcase)
      * [`ShowOptionsMethod.translate()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.translate)
      * [`ShowOptionsMethod.upper()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.upper)
      * [`ShowOptionsMethod.startswith()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.startswith)
      * [`ShowOptionsMethod.endswith()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.endswith)
      * [`ShowOptionsMethod.removeprefix()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.removeprefix)
      * [`ShowOptionsMethod.removesuffix()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.removesuffix)
      * [`ShowOptionsMethod.isascii()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isascii)
      * [`ShowOptionsMethod.islower()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.islower)
      * [`ShowOptionsMethod.isupper()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isupper)
      * [`ShowOptionsMethod.istitle()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.istitle)
      * [`ShowOptionsMethod.isspace()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isspace)
      * [`ShowOptionsMethod.isdecimal()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isdecimal)
      * [`ShowOptionsMethod.isdigit()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isdigit)
      * [`ShowOptionsMethod.isnumeric()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isnumeric)
      * [`ShowOptionsMethod.isalpha()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isalpha)
      * [`ShowOptionsMethod.isalnum()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isalnum)
      * [`ShowOptionsMethod.isidentifier()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isidentifier)
      * [`ShowOptionsMethod.isprintable()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.isprintable)
      * [`ShowOptionsMethod.zfill()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.zfill)
      * [`ShowOptionsMethod.format()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.format)
      * [`ShowOptionsMethod.format_map()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.format_map)
      * [`ShowOptionsMethod.maketrans()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ShowOptionsMethod.maketrans)
    * [`ScenarioType`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType)
      * [`ScenarioType.VIEW`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.VIEW)
      * [`ScenarioType.CUSTOM_CODE`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.CUSTOM_CODE)
      * [`ScenarioType.LABEL_ATTRIBUTE`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.LABEL_ATTRIBUTE)
      * [`ScenarioType.SAMPLE_FIELD`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.SAMPLE_FIELD)
      * [`ScenarioType.encode()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.encode)
      * [`ScenarioType.replace()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.replace)
      * [`ScenarioType.split()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.split)
      * [`ScenarioType.rsplit()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.rsplit)
      * [`ScenarioType.join()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.join)
      * [`ScenarioType.capitalize()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.capitalize)
      * [`ScenarioType.casefold()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.casefold)
      * [`ScenarioType.title()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.title)
      * [`ScenarioType.center()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.center)
      * [`ScenarioType.count()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.count)
      * [`ScenarioType.expandtabs()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.expandtabs)
      * [`ScenarioType.find()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.find)
      * [`ScenarioType.partition()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.partition)
      * [`ScenarioType.index()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.index)
      * [`ScenarioType.ljust()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.ljust)
      * [`ScenarioType.lower()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.lower)
      * [`ScenarioType.lstrip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.lstrip)
      * [`ScenarioType.rfind()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.rfind)
      * [`ScenarioType.rindex()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.rindex)
      * [`ScenarioType.rjust()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.rjust)
      * [`ScenarioType.rstrip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.rstrip)
      * [`ScenarioType.rpartition()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.rpartition)
      * [`ScenarioType.splitlines()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.splitlines)
      * [`ScenarioType.strip()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.strip)
      * [`ScenarioType.swapcase()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.swapcase)
      * [`ScenarioType.translate()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.translate)
      * [`ScenarioType.upper()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.upper)
      * [`ScenarioType.startswith()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.startswith)
      * [`ScenarioType.endswith()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.endswith)
      * [`ScenarioType.removeprefix()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.removeprefix)
      * [`ScenarioType.removesuffix()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.removesuffix)
      * [`ScenarioType.isascii()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isascii)
      * [`ScenarioType.islower()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.islower)
      * [`ScenarioType.isupper()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isupper)
      * [`ScenarioType.istitle()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.istitle)
      * [`ScenarioType.isspace()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isspace)
      * [`ScenarioType.isdecimal()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isdecimal)
      * [`ScenarioType.isdigit()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isdigit)
      * [`ScenarioType.isnumeric()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isnumeric)
      * [`ScenarioType.isalpha()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isalpha)
      * [`ScenarioType.isalnum()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isalnum)
      * [`ScenarioType.isidentifier()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isidentifier)
      * [`ScenarioType.isprintable()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.isprintable)
      * [`ScenarioType.zfill()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.zfill)
      * [`ScenarioType.format()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.format)
      * [`ScenarioType.format_map()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.format_map)
      * [`ScenarioType.maketrans()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.ScenarioType.maketrans)
    * [`get_scenario_example()`](plugins__api__plugins.operators.model_evaluation.utils.md#plugins.operators.model_evaluation.utils.get_scenario_example)



## Module contents#

Scenario plugin.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ConfigureScenario`([_builtin]) |   
---|---  
`ConfigureScenarioPlotResolver`([_builtin]) |   
`ListScenarios`([_builtin]) |   
  
**Functions:**

`get_dataset`(ctx) | Returns the dataset for the current context.  
---|---  
`extract_evaluation_keys`(ctx) |   
`get_evaluations_results`(ctx) | Returns the evaluation results for the current context.  
`get_label_attribute_path`(params) | Returns the last part of the label attribute path to use in use_subset(type="attribute", ...)  
`get_scenario_type`(params) |   
`resolve_subsets`(scenario_type,Â params,Â values) |   
  
class plugins.operators.model_evaluation.ConfigureScenario(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

**Attributes:**

`last_view_type_used` |   
---|---  
`config` | The `OperatorConfig` for the operator.  
`builtin` | Whether the operator is builtin.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
**Methods:**

`get_samples_count`(ctx) | Returns the number of samples in the dataset for the current context.  
---|---  
`get_default_for_distribution_preview`(ctx) | Returns the default value for the sample distribution preview.  
`render_name_input`(ctx,Â inputs) |   
`render_scenario_types`(inputs,Â selected_type) |   
`extract_evaluation_id`(ctx) |   
`convert_to_plotly_data`(preview_data) |   
`render_empty_sample_distribution`(ctx,Â ...[,Â ...]) |   
`get_label_attribute_path`(params) | Returns the last part of the label attribute path to use in use_subset(type="attribute", ...)  
`render_sample_distribution`(ctx,Â inputs,Â ...) |   
`render_plot_preview_toggle`(ctx,Â inputs) |   
`render_sample_distribution_graph`(ctx,Â ...) |   
`get_custom_code_key`(params) |   
`extract_custom_code`(ctx[,Â example_type]) |   
`render_custom_code`(ctx,Â inputs[,Â example_type]) |   
`render_no_values_warning`(inputs,Â field_name) |   
`render_use_custom_code_warning`(inputs[,Â reason]) |   
`render_use_custom_code_instead`(ctx,Â inputs) |   
`get_saved_view_scenarios_picker_type`(ctx) | Returns the view mode for saved views based on the number of available saved views.  
`render_saved_views`(ctx,Â inputs) | Renders sample distribution for subsets using saved views.  
`get_scenario_values_key`(params) | returns a unique key that holds the latest selected values for a - certain scenario type.  
`get_selected_values`(params) |   
`render_checkbox_view`(ctx,Â values,Â inputs[,Â ...]) |   
`get_scenarios_picker_type`(ctx,Â field_name) | Determines the scenario picker type for a given field based on its type and distinct values.  
`render_auto_complete_view`(ctx,Â values,Â inputs) | Renders an auto-complete view as a more compact/efficient input option when, - There are too many distinct values to display and The field is of type string.  
`render_scenario_picker_view`(ctx,Â field_name,Â ...) | Renders the appropriate UI component based on the picker type.  
`get_valid_label_attribute_path_options`(...) | Returns all the paths in the dataset schema that are valid label attributes types.  
`render_label_attribute`(ctx,Â inputs,Â gt_field) |   
`get_valid_sample_field_path_options`(...) | Get valid sample field path options based on the schema. - Filters out - fields having roots with type as List of documents - non-primitives - non-list of primitives.  
`render_sample_fields`(ctx,Â inputs[,Â field_name]) |   
`get_modal_title`(ctx) |   
`get_scenario_names`(ctx) |   
`resolve_input`(ctx) | Returns the resolved input property.  
`render_custom_code_content`(inputs,Â ...) |   
`execute`(ctx) | Executes the operator.  
`add_secrets`(secrets) | Adds secrets to the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
last_view_type_used = None#
    

property config#
    

The `OperatorConfig` for the operator.

get_samples_count(_ctx_)#
    

Returns the number of samples in the dataset for the current context.

get_default_for_distribution_preview(_ctx_)#
    

Returns the default value for the sample distribution preview.

render_name_input(_ctx_ , _inputs_)#
    

render_scenario_types(_inputs_ , _selected_type_)#
    

extract_evaluation_id(_ctx_)#
    

convert_to_plotly_data(_preview_data_)#
    

render_empty_sample_distribution(_ctx_ , _inputs_ , _params_ , _description =None_, _is_invalid =True_)#
    

get_label_attribute_path(_params_)#
    

Returns the last part of the label attribute path to use in use_subset(type=âattributeâ, â¦)

render_sample_distribution(_ctx_ , _inputs_ , _scenario_type_ , _values_)#
    

render_plot_preview_toggle(_ctx_ , _inputs_)#
    

render_sample_distribution_graph(_ctx_ , _inputs_ , _subset_expressions_ , _scenario_type_)#
    

get_custom_code_key(_params_)#
    

extract_custom_code(_ctx_ , _example_type =ScenarioType.CUSTOM_CODE_)#
    

render_custom_code(_ctx_ , _inputs_ , _example_type =ScenarioType.CUSTOM_CODE_)#
    

render_no_values_warning(_inputs_ , _field_name_ , _link =''_)#
    

render_use_custom_code_warning(_inputs_ , _reason =CustomCodeViewReason.TOO_MANY_CATEGORIES_)#
    

render_use_custom_code_instead(_ctx_ , _inputs_ , _reason =CustomCodeViewReason.TOO_MANY_CATEGORIES_)#
    

get_saved_view_scenarios_picker_type(_ctx_)#
    

Returns the view mode for saved views based on the number of available saved views.

render_saved_views(_ctx_ , _inputs_)#
    

Renders sample distribution for subsets using saved views.

get_scenario_values_key(_params_)#
    

returns a unique key that holds the latest selected values for a \- certain scenario type. has to be one of type ScenarioType \- certain scenario field (ex: âtagsâ, âlabelsâ)

get_selected_values(_params_)#
    

render_checkbox_view(_ctx_ , _values_ , _inputs_ , _with_description =None_)#
    

get_scenarios_picker_type(_ctx_ , _field_name_)#
    

Determines the scenario picker type for a given field based on its type and distinct values. \- if the field is of type float, shows custom code mode \- if the field is boolean, shows checkbox mode \- if the field has no distinct values, shows empty mode \- if the field has too many distinct values, shows auto-complete or custom code mode \- if the field has a manageable number of distinct values, shows checkbox mode

Returns:
    

Picker type and corresponding values.

Return type:
    

[Tuple](api__fiftyone.operators.types.md#fiftyone.operators.types.Tuple "fiftyone.operators.types.Tuple")[str, Any]

render_auto_complete_view(_ctx_ , _values_ , _inputs_)#
    

Renders an auto-complete view as a more compact/efficient input option when, \- There are too many distinct values to display and The field is of type string. \- There are too many distinct saved views to display as checkbox.

Eventually, if there are selected values, it attempts to render the sample distribution preview graph

render_scenario_picker_view(_ctx_ , _field_name_ , _inputs_)#
    

Renders the appropriate UI component based on the picker type.

get_valid_label_attribute_path_options(_schema_ , _gt_field_)#
    

Returns all the paths in the dataset schema that are valid label attributes types. \- primitives \- OR list of primitives \- AND path starts with gt_field

render_label_attribute(_ctx_ , _inputs_ , _gt_field_ , _label_attr =None_)#
    

get_valid_sample_field_path_options(_flat_field_schema_)#
    

Get valid sample field path options based on the schema. \- Filters out

>   * fields having roots with type as List of documents
> 
>   * non-primitives
> 
>   * non-list of primitives
> 
> 


render_sample_fields(_ctx_ , _inputs_ , _field_name =None_)#
    

get_modal_title(_ctx_)#
    

get_scenario_names(_ctx_)#
    

resolve_input(_ctx_)#
    

Returns the resolved input property.

Subclasses can implement this method to define the inputs to the operator. This method should never be called directly. Instead use `resolve_type()`.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called each time the input changes.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

render_custom_code_content(_inputs_ , _custom_code_ , _code_key_)#
    

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

resolve_delegation(_ctx_)#
    

Returns the resolved _forced_ delegation flag.

Subclasses can implement this method to decide if delegated execution should be _forced_ for the given operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

whether the operation should be delegated (True), run immediately (False), or None to defer to `resolve_execution_options()` to specify the available options

resolve_execution_options(_ctx_)#
    

Returns the resolved execution options.

Subclasses can implement this method to define the execution options available for the operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.executor.ExecutionOptions`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions "fiftyone.operators.executor.ExecutionOptions") instance

resolve_output(_ctx_)#
    

Returns the resolved output property.

Subclasses can implement this method to define the outputs of the operator.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called after the operator is executed.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_placement(_ctx_)#
    

Returns the resolved placement of the operator.

Subclasses can implement this method to define the placement of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement "fiftyone.operators.types.Placement"), or None

resolve_run_name(_ctx_)#
    

Returns the resolved run name of the operator.

Subclasses can implement this method to define the run name of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a string, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

class plugins.operators.model_evaluation.ConfigureScenarioPlotResolver(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

**Attributes:**

`config` | The `OperatorConfig` for the operator.  
---|---  
`builtin` | Whether the operator is builtin.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
**Methods:**

`execute`(ctx) | Executes the operator.  
---|---  
`get_subset_def_data_for_eval_key`(ctx,Â ...) | Builds and returns an execution cache key for each type of scenario.  
`get_subset_def_data_for_eval`(ctx,Â _,Â ...) |   
`get_sample_distribution`(ctx,Â subset_expressions) |   
`add_secrets`(secrets) | Adds secrets to the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
property config#
    

The `OperatorConfig` for the operator.

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

get_subset_def_data_for_eval_key(_ctx_ , _eval_key_ , ___ , _name_ , _subset_def_)#
    

Builds and returns an execution cache key for each type of scenario. \- eval key + name + type + subset definition

get_subset_def_data_for_eval(_ctx_ , ___ , _eval_result_ , _name_ , _subset_def_)#
    

get_sample_distribution(_ctx_ , _subset_expressions_)#
    

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

resolve_delegation(_ctx_)#
    

Returns the resolved _forced_ delegation flag.

Subclasses can implement this method to decide if delegated execution should be _forced_ for the given operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

whether the operation should be delegated (True), run immediately (False), or None to defer to `resolve_execution_options()` to specify the available options

resolve_execution_options(_ctx_)#
    

Returns the resolved execution options.

Subclasses can implement this method to define the execution options available for the operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.executor.ExecutionOptions`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions "fiftyone.operators.executor.ExecutionOptions") instance

resolve_input(_ctx_)#
    

Returns the resolved input property.

Subclasses can implement this method to define the inputs to the operator. This method should never be called directly. Instead use `resolve_type()`.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called each time the input changes.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_output(_ctx_)#
    

Returns the resolved output property.

Subclasses can implement this method to define the outputs of the operator.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called after the operator is executed.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_placement(_ctx_)#
    

Returns the resolved placement of the operator.

Subclasses can implement this method to define the placement of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement "fiftyone.operators.types.Placement"), or None

resolve_run_name(_ctx_)#
    

Returns the resolved run name of the operator.

Subclasses can implement this method to define the run name of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a string, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

class plugins.operators.model_evaluation.ListScenarios(__builtin =False_)#
    

Bases: [`Operator`](api__fiftyone.operators.operator.md#fiftyone.operators.operator.Operator "fiftyone.operators.operator.Operator")

**Attributes:**

`config` | The `OperatorConfig` for the operator.  
---|---  
`builtin` | Whether the operator is builtin.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
**Methods:**

`execute`(ctx) | Executes the operator.  
---|---  
`add_secrets`(secrets) | Adds secrets to the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
property config#
    

The `OperatorConfig` for the operator.

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

resolve_delegation(_ctx_)#
    

Returns the resolved _forced_ delegation flag.

Subclasses can implement this method to decide if delegated execution should be _forced_ for the given operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

whether the operation should be delegated (True), run immediately (False), or None to defer to `resolve_execution_options()` to specify the available options

resolve_execution_options(_ctx_)#
    

Returns the resolved execution options.

Subclasses can implement this method to define the execution options available for the operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.executor.ExecutionOptions`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions "fiftyone.operators.executor.ExecutionOptions") instance

resolve_input(_ctx_)#
    

Returns the resolved input property.

Subclasses can implement this method to define the inputs to the operator. This method should never be called directly. Instead use `resolve_type()`.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called each time the input changes.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_output(_ctx_)#
    

Returns the resolved output property.

Subclasses can implement this method to define the outputs of the operator.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called after the operator is executed.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_placement(_ctx_)#
    

Returns the resolved placement of the operator.

Subclasses can implement this method to define the placement of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement "fiftyone.operators.types.Placement"), or None

resolve_run_name(_ctx_)#
    

Returns the resolved run name of the operator.

Subclasses can implement this method to define the run name of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a string, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

plugins.operators.model_evaluation.get_dataset(_ctx_)#
    

Returns the dataset for the current context.

plugins.operators.model_evaluation.extract_evaluation_keys(_ctx_)#
    

plugins.operators.model_evaluation.get_evaluations_results(_ctx_)#
    

Returns the evaluation results for the current context.

plugins.operators.model_evaluation.get_label_attribute_path(_params_)#
    

Returns the last part of the label attribute path to use in use_subset(type=âattributeâ, â¦)

plugins.operators.model_evaluation.get_scenario_type(_params_)#
    

plugins.operators.model_evaluation.resolve_subsets(_scenario_type_ , _params_ , _values_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
