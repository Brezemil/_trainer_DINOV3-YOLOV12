---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/delegated.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/delegated)

# Delegated Operations Plugin#

A plugin that contains utilities for managing your [delegated operations](https://docs.voxel51.com/plugins/using_plugins.html#delegated-operations).

## Installation#
    
    
    fiftyone plugins download \
        https://github.com/voxel51/fiftyone-plugins \
        --plugin-names @voxel51/delegated
    

Refer to the [main README](https://github.com/voxel51/fiftyone-plugins) for more information about managing downloaded plugins and developing plugins locally.

## Usage#

  1. Launch the App:



    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    session = fo.launch_app(dataset)
    

  2. Press ``` or click the `Browse operations` action to open the Operators list

  3. Select any of the operators listed below!




## Operators#

### manage_delegated_operations#

You can use this operator to list delegated operations for your current dataset or other dataset(s) and optionally take actions on them.

This operator is essentially a wrapper around the following [fiftyone delegated](https://docs.voxel51.com/cli/index.html#fiftyone-delegated-operations) CLI methods:
    
    
    # List some specific delegated operations
    fiftyone delegated list \
        --dataset quickstart \
        --operator @voxel51/io/export_samples \
        --state COMPLETED \
        --sort-by COMPLETED_AT \
        --limit 10
    
    # Get info about the specified operation
    fiftyone delegated info <id>
    
    # Rerun the specified operation
    fiftyone delegated rerun <id>
    
    # Manually mark the specified operation(s) as FAILED
    fiftyone delegated fail <id1> <id2> ...
    
    # Delete the specified operation(s)
    fiftyone delegated delete <id1> <id2> ...
    

where the operatorâs form allows you to configure what operations to show and what actions to take on them, if any.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
