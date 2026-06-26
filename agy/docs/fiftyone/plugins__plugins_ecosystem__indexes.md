---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/indexes.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/indexes)

# Indexes Plugin#

A plugin that contains utilities for working with FiftyOne database indexes.

## Installation#
    
    
    fiftyone plugins download \
        https://github.com/voxel51/fiftyone-plugins \
        --plugin-names @voxel51/indexes
    

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

### manage_indexes#

You can use this operator to view, create, and delete database indexes, which are useful for speeding up queries on large datasets in [Lightning Mode](https://docs.voxel51.com/user_guide/app.html#lightning-mode).

Note that, for large datasets, creating indexes can slow down write operations during the process and create overhead in MongoDB, so you should only create indexes for fields that you frequently query on.

For more information on indexes, see the [MongoDB documentation](https://docs.mongodb.com/manual/indexes).

This operator is a wrapper around the [list_indexes()](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.list_indexes), [get_index_information()](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.get_index_information), [create_index()](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.create_index), and [drop_index()](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.drop_index) methods:
    
    
    dataset.create_index("uniqueness")
    dataset.create_index("ground_truth.detections.label")
    
    print(dataset.list_indexes())
    
    dataset.drop_index("uniqueness")
    dataset.drop_index("ground_truth.detections.label")
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
