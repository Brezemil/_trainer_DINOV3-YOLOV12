---
source_url: https://docs.voxel51.com/plugins/plugins_ecosystem/annotation.html
---

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/voxel51/fiftyone-plugins/tree/main/plugins/annotation)

# Annotation Plugin#

A plugin that contains utilities for integrating FiftyOne with annotation tools.

In order to use this plugin, you must have at least one annotation backend configured as [described here](https://docs.voxel51.com/user_guide/annotation.html).

## Installation#
    
    
    fiftyone plugins download \
        https://github.com/voxel51/fiftyone-plugins \
        --plugin-names @voxel51/annotation
    

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

### request_annotations#

You can use this operator to create annotation tasks for the current dataset or view.

This operator is essentially a wrapper around the [request annotations Python workflow](https://docs.voxel51.com/user_guide/annotation.html#requesting-annotations):
    
    
    dataset_or_view.annotate(
        anno_key,
        backend=...,
        label_schema=...,
        ...
    )
    

where the operatorâs form allows you to configure the annotation key, annotation backend, label schema, and any other applicable fields for your annotation backend.

### load_annotations#

You can use this operator to load annotations for existing runs back onto your dataset.

This operator is essentially a wrapper around the [load annotations Python workflow](https://docs.voxel51.com/user_guide/annotation.html#loading-annotations):
    
    
    dataset_or_view.load_annotations(anno_key, ...)
    

where the operatorâs form allows you to configure the annotation key and related options.

### get_annotation_info#

You can use this operator to get information about annotation runs.

This operator is essentially a wrapper around [get_annotation_info()](https://docs.voxel51.com/api/fiftyone.core.collections.html#fiftyone.core.collections.SampleCollection.get_annotation_info):
    
    
    info = dataset_or_view.get_annotation_info(anno_key)
    print(info)
    

### load_annotation_view#

You can use this operator to load the view on which an annotation run was performed.

This operator is essentially a wrapper around [load_annotation_view()](https://docs.voxel51.com/api/fiftyone.core.collections.html#fiftyone.core.collections.SampleCollection.load_annotation_view):
    
    
    view = dataset.load_annotation_view(anno_key)
    

### rename_annotation_run#

You can use this operator to rename annotation runs.

This operator is essentially a wrapper around [rename_annotation_run()](https://docs.voxel51.com/api/fiftyone.core.collections.html#fiftyone.core.collections.SampleCollection.rename_annotation_run):
    
    
    dataset_or_view.rename_annotation_run(anno_key, new_anno_key)
    

### delete_annotation_run#

You can use this operator to delete annotation runs.

This operator is essentially a wrapper around [delete_annotation_run()](https://docs.voxel51.com/api/fiftyone.core.collections.html#fiftyone.core.collections.SampleCollection.delete_annotation_run):
    
    
    dataset_or_view.delete_annotation_run(anno_key)
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
