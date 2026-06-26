---
source_url: https://docs.voxel51.com/api/fiftyone.core.stages.html
---

# fiftyone.core.stages#

View stages.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`ViewStage`() | Abstract base class for all view stages.  
---|---  
`Concat`(samples) | Concatenates the contents of the given [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to this collection.  
`Exclude`(sample_ids) | Excludes the samples with the given IDs from a collection.  
`ExcludeBy`(field,Â values) | Excludes the samples with the given field values from a collection.  
`ExcludeFields`([field_names,Â meta_filter,Â ...]) | Excludes the fields with the given names from the samples in a collection.  
`ExcludeFrames`(frame_ids[,Â omit_empty]) | Excludes the frames with the given IDs from a video collection.  
`ExcludeGroups`(group_ids[,Â ordered]) | Excludes the groups with the given IDs from a grouped collection.  
`ExcludeLabels`([labels,Â ids,Â instance_ids,Â ...]) | Excludes the specified labels from a collection.  
`Exists`(field[,Â bool]) | Returns a view containing the samples in a collection that have (or do not have) a non-`None` value for the given field or embedded field.  
`FilterField`(field,Â filter[,Â only_matches,Â ...]) | Filters the values of a given field or embedded field of each sample in a collection.  
`FilterLabels`(field,Â filter[,Â only_matches,Â ...]) | Filters the [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field of each sample in a collection.  
`FilterKeypoints`(field[,Â filter,Â labels,Â ...]) | Filters the individual [`fiftyone.core.labels.Keypoint.points`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.points "fiftyone.core.labels.Keypoint.points") elements in the specified keypoints field of each sample in the collection.  
`GeoNear`(point[,Â location_field,Â ...]) | Sorts the samples in a collection by their proximity to a specified geolocation.  
`GeoWithin`(boundary[,Â location_field,Â ...]) | Filters the samples in a collection to only match samples whose geolocation is within a specified boundary.  
`GroupBy`(field_or_expr[,Â order_by,Â reverse,Â ...]) | Creates a view that groups the samples in a collection by a specified field or expression.  
`Flatten`([stages]) | Returns a flattened view that contains all samples in a dynamic grouped collection.  
`Limit`(limit) | Creates a view with at most the given number of samples.  
`LimitLabels`(field,Â limit) | Limits the number of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances in the specified labels list field of each sample in a collection.  
`MapLabels`(field,Â map) | Maps the `label` values of a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field to new values for each sample in a collection.  
`MapValues`(field,Â map) | Maps the values in the given field to new values for each sample in a collection.  
`SetField`(field,Â expr[,Â _allow_missing,Â ...]) | Sets a field or embedded field on each sample in a collection by evaluating the given expression.  
`Match`(filter) | Filters the samples in the collection by the given filter.  
`SelectGroupSlices`([slices,Â media_type,Â ...]) | Selects the specified group slice(s) from a grouped collection.  
`ExcludeGroupSlices`([slices,Â media_type]) | Excludes the specified group slice(s) from a grouped collection.  
`MatchFrames`(filter[,Â omit_empty]) | Filters the frames in a video collection by the given filter.  
`MatchLabels`([labels,Â ids,Â instance_ids,Â ...]) | Selects the samples from a collection that contain (or do not contain) at least one label that matches the specified criteria.  
`MatchTags`(tags[,Â bool,Â all]) | Returns a view containing the samples in the collection that have or don't have any/all of the given tag(s).  
`Mongo`(pipeline[,Â _needs_frames,Â _group_slices]) | A view stage defined by a raw MongoDB aggregation pipeline.  
`Select`(sample_ids[,Â ordered]) | Selects the samples with the given IDs from a collection.  
`SelectBy`(field,Â values[,Â ordered]) | Selects the samples with the given field values from a collection.  
`SelectFields`([field_names,Â meta_filter,Â ...]) | Selects only the fields with the given names from the samples in the collection.  
`SelectFrames`(frame_ids[,Â omit_empty]) | Selects the frames with the given IDs from a video collection.  
`SelectGroups`(group_ids[,Â ordered]) | Selects the groups with the given IDs from a grouped collection.  
`SelectLabels`([labels,Â ids,Â instance_ids,Â ...]) | Selects only the specified labels from a collection.  
`Shuffle`([seed,Â _randint]) | Randomly shuffles the samples in a collection.  
`Skip`(skip) | Omits the given number of samples from the head of a collection.  
`SortBy`(field_or_expr[,Â reverse,Â create_index]) | Sorts the samples in a collection by the given field(s) or expression(s).  
`SortBySimilarity`(query[,Â k,Â reverse,Â ...]) | Sorts a collection by similarity to a specified query.  
`Take`(size[,Â seed,Â _randint]) | Randomly samples the given number of samples from a collection.  
`ToPatches`(field[,Â config,Â _state]) | Creates a view that contains one sample per object patch in the specified field of a collection.  
`ToEvaluationPatches`(eval_key[,Â config,Â _state]) | Creates a view based on the results of the evaluation with the given key that contains one sample for each true positive, false positive, and false negative example in the collection, respectively.  
`ToClips`(field_or_expr[,Â config,Â _state]) | Creates a view that contains one sample per clip defined by the given field or expression in a video collection.  
`ToTrajectories`(field[,Â config,Â _state]) | Creates a view that contains one clip for each unique object trajectory defined by their `(label, index)` in a frame-level field of a video collection.  
`ToFrames`([config,Â _state]) | Creates a view that contains one sample per frame in a video collection.  
  
**Exceptions:**

`ViewStageError` | An error raised when a problem with a `ViewStage` is encountered.  
---|---  
  
class fiftyone.core.stages.ViewStage#
    

Bases: `object`

Abstract base class for all view stages.

`ViewStage` instances represent logical operations to apply to [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") instances, which may decide what subset of samples in the collection should pass though the stage, and also what subset of the contents of each [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") should be passed. The output of view stages are represented by a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView").

**Attributes:**

`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
---|---  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

exception fiftyone.core.stages.ViewStageError#
    

Bases: `Exception`

An error raised when a problem with a `ViewStage` is encountered.

**Methods:**

`add_note` | Exception.add_note(note) -- add a note to the exception  
---|---  
`with_traceback` | Exception.with_traceback(tb) -- set self.__traceback__ to tb and return self.  
  
**Attributes:**

`args` |   
---|---  
  
add_note()#
    

Exception.add_note(note) â add a note to the exception

args#
    

with_traceback()#
    

Exception.with_traceback(tb) â set self.__traceback__ to tb and return self.

class fiftyone.core.stages.Concat(_samples_)#
    

Bases: `ViewStage`

Concatenates the contents of the given [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to this collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Concatenate two views
    #
    
    view1 = dataset.match(F("uniqueness") < 0.2)
    view2 = dataset.match(F("uniqueness") > 0.7)
    
    stage = fo.Concat(view2)
    view = view1.add_stage(stage)
    
    print(view1)
    print(view2)
    print(view)
    
    #
    # Concatenate two patches views
    #
    
    gt_objects = dataset.to_patches("ground_truth")
    
    patches1 = gt_objects[:50]
    patches2 = gt_objects[-50:]
    
    stage = fo.Concat(patches2)
    patches = patches1.add_stage(stage)
    
    print(patches1)
    print(patches2)
    print(patches)
    

Parameters:
    

**samples** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose contents to append to this collection

**Attributes:**

`samples` | The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose contents to append to this collection.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property samples#
    

The [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose contents to append to this collection.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.Exclude(_sample_ids_)#
    

Bases: `ViewStage`

Excludes the samples with the given IDs from a collection.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="/path/to/image1.png"),
            fo.Sample(filepath="/path/to/image2.png"),
            fo.Sample(filepath="/path/to/image3.png"),
        ]
    )
    
    #
    # Exclude the first sample from the dataset
    #
    
    sample_id = dataset.first().id
    stage = fo.Exclude(sample_id)
    view = dataset.add_stage(stage)
    
    #
    # Exclude the first and last samples from the dataset
    #
    
    sample_ids = [dataset.first().id, dataset.last().id]
    stage = fo.Exclude(sample_ids)
    view = dataset.add_stage(stage)
    

Parameters:
    

**sample_ids** â 

the samples to exclude. Can be any of the following:

  * a sample ID

  * an iterable of sample IDs

  * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

  * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

  * a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")




**Attributes:**

`sample_ids` | The list of sample IDs to exclude.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property sample_ids#
    

The list of sample IDs to exclude.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.ExcludeBy(_field_ , _values_)#
    

Bases: `ViewStage`

Excludes the samples with the given field values from a collection.

This stage is typically used to work with categorical fields (strings, ints, and bools). If you want to exclude samples based on floating point fields, use `Match`.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image%d.jpg" % i, int=i, str=str(i))
            for i in range(10)
        ]
    )
    
    #
    # Create a view excluding samples whose `int` field have the given
    # values
    #
    
    stage = fo.ExcludeBy("int", [1, 9, 3, 7, 5])
    view = dataset.add_stage(stage)
    print(view.head(5))
    
    #
    # Create a view excluding samples whose `str` field have the given
    # values
    #
    
    stage = fo.ExcludeBy("str", ["1", "9", "3", "7", "5"])
    view = dataset.add_stage(stage)
    print(view.head(5))
    

Parameters:
    

  * **field** â a field or `embedded.field.name`

  * **values** â a value or iterable of values to exclude by




**Attributes:**

`field` | The field whose values to exclude by.  
---|---  
`values` | The list of values to exclude by.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property field#
    

The field whose values to exclude by.

property values#
    

The list of values to exclude by.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.ExcludeFields(_field_names =None_, _meta_filter =None_, __allow_missing =False_)#
    

Bases: `ViewStage`

Excludes the fields with the given names from the samples in a collection.

Note that default fields cannot be excluded.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                ground_truth=fo.Classification(label="cat"),
                predictions=fo.Classification(
                    label="cat",
                    confidence=0.9,
                    mood="surly",
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                ground_truth=fo.Classification(label="dog"),
                predictions=fo.Classification(
                    label="dog",
                    confidence=0.8,
                    mood="happy",
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
            ),
        ]
    )
    
    #
    # Exclude the `predictions` field from all samples
    #
    
    stage = fo.ExcludeFields("predictions")
    view = dataset.add_stage(stage)
    
    #
    # Exclude the `mood` attribute from all classifications in the
    # `predictions` field
    #
    
    stage = fo.ExcludeFields("predictions.mood")
    view = dataset.add_stage(stage)
    
    #
    # Exclude the `predictions` field from all samples
    #
    

Parameters:
    

  * **field_names** (_None_) â a field name or iterable of field names to exclude. May contain `embedded.field.name` as well

  * **meta_filter** (_None_) â 

a filter that dynamically excludes fields in the collectionâs schema according to the specified rule, which can be matched against the fieldâs `name`, `type`, `description`, and/or `info`. For example:

    * Use `meta_filter="2023"` or `meta_filter={"any": "2023"}` to exclude fields that have the string â2023â anywhere in their name, type, description, or info

    * Use `meta_filter={"type": "StringField"}` or `meta_filter={"type": "Classification"}` to exclude all string or classification fields, respectively

    * Use `meta_filter={"description": "my description"}` to exclude fields whose description contains the string âmy descriptionâ

    * Use `meta_filter={"info": "2023"}` to exclude fields that have the string â2023â anywhere in their info

    * Use `meta_filter={"info.key": "value"}}` to exclude fields that have a specific key/value pair in their info

    * Include `meta_filter={"include_nested_fields": True, ...}` in your meta filter to include all nested fields in the filter




**Attributes:**

`field_names` | A list of field names to exclude.  
---|---  
`meta_filter` | A filter that dynamically excludes fields.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
---|---  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field_names#
    

A list of field names to exclude.

property meta_filter#
    

A filter that dynamically excludes fields.

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.ExcludeFrames(_frame_ids_ , _omit_empty =True_)#
    

Bases: `ViewStage`

Excludes the frames with the given IDs from a video collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    #
    # Exclude some specific frames
    #
    
    frame_ids = [
        dataset.first().frames.first().id,
        dataset.last().frames.last().id,
    ]
    
    stage = fo.ExcludeFrames(frame_ids)
    view = dataset.add_stage(stage)
    
    print(dataset.count("frames"))
    print(view.count("frames"))
    

Parameters:
    

  * **frame_ids** â 

the frames to exclude. Can be any of the following:

    * a frame ID

    * an iterable of frame IDs

    * a [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") or [`fiftyone.core.frame.FrameView`](api__fiftyone.core.frame.md#fiftyone.core.frame.FrameView "fiftyone.core.frame.FrameView")

    * an iterable of [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") or [`fiftyone.core.frame.FrameView`](api__fiftyone.core.frame.md#fiftyone.core.frame.FrameView "fiftyone.core.frame.FrameView") instances

    * a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose frames to exclude

  * **omit_empty** (_True_) â whether to omit samples that have no frames after excluding the specified frames




**Attributes:**

`frame_ids` | The list of frame IDs to exclude.  
---|---  
`omit_empty` | Whether to omit samples that have no frames after filtering.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property frame_ids#
    

The list of frame IDs to exclude.

property omit_empty#
    

Whether to omit samples that have no frames after filtering.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.ExcludeGroups(_group_ids_ , _ordered =False_)#
    

Bases: `ViewStage`

Excludes the groups with the given IDs from a grouped collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-groups")
    
    #
    # Exclude some specific groups by ID
    #
    
    view = dataset.take(2)
    group_ids = view.values("group.id")
    
    stage = fo.ExcludeGroups(group_ids)
    other_groups = dataset.add_stage(stage)
    
    assert len(set(group_ids) & set(other_groups.values("group.id"))) == 0
    

Parameters:
    

**groups_ids** â 

the groups to select. Can be any of the following:

  * a group ID

  * an iterable of group IDs

  * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

  * a group dict returned by [`get_group()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_group "fiftyone.core.collections.SampleCollection.get_group")

  * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

  * an iterable of group dicts returned by [`get_group()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_group "fiftyone.core.collections.SampleCollection.get_group")

  * a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")




**Attributes:**

`group_ids` | The list of group IDs to exclude.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property group_ids#
    

The list of group IDs to exclude.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.ExcludeLabels(_labels =None_, _ids =None_, _instance_ids =None_, _tags =None_, _fields =None_, _omit_empty =True_)#
    

Bases: `ViewStage`

Excludes the specified labels from a collection.

The returned view will omit samples, sample fields, and individual labels that do not match the specified selection criteria.

You can perform an exclusion via one or more of the following methods:

  * Provide the `labels` argument, which should contain a list of dicts in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels"), to exclude specific labels

  * Provide the `ids` argument to exclude labels with specific IDs

  * Provide the `instance_ids` argument to exclude labels with specific instance IDs

  * Provide the `tags` argument to exclude labels with specific tags




If multiple criteria are specified, labels must match all of them in order to be excluded.

By default, the exclusion is applied to all [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields, but you can provide the `fields` argument to explicitly define the field(s) in which to exclude.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Exclude the labels currently selected in the App
    #
    
    session = fo.launch_app(dataset)
    
    # Select some labels in the App...
    
    stage = fo.ExcludeLabels(labels=session.selected_labels)
    view = dataset.add_stage(stage)
    
    #
    # Exclude labels with the specified IDs
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    stage = fo.ExcludeLabels(ids=ids)
    view = dataset.add_stage(stage)
    
    print(dataset.count("ground_truth.detections"))
    print(view.count("ground_truth.detections"))
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    
    #
    # Exclude labels with the specified tags
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    # Give the labels a "test" tag
    dataset = dataset.clone()  # create copy since we're modifying data
    dataset.select_labels(ids=ids).tag_labels("test")
    
    print(dataset.count_values("ground_truth.detections.tags"))
    print(dataset.count_values("predictions.detections.tags"))
    
    # Exclude the labels via their tag
    stage = fo.ExcludeLabels(tags="test")
    view = dataset.add_stage(stage)
    
    print(dataset.count("ground_truth.detections"))
    print(view.count("ground_truth.detections"))
    
    print(dataset.count("predictions.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

  * **labels** (_None_) â a list of dicts specifying the labels to exclude in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels")

  * **ids** (_None_) â an ID or iterable of IDs of the labels to exclude

  * **instance_ids** (_None_) â an instance ID or iterable of instance IDs of the labels to exclude

  * **tags** (_None_) â a tag or iterable of tags of labels to exclude

  * **fields** (_None_) â a field or iterable of fields from which to exclude

  * **omit_empty** (_True_) â whether to omit samples that have no labels after filtering




**Attributes:**

`labels` | A list of dicts specifying the labels to exclude.  
---|---  
`ids` | A list of IDs of labels to exclude.  
`instance_ids` | A list of instance IDs of labels to exclude.  
`tags` | A list of tags of labels to exclude.  
`fields` | A list of fields from which labels are being excluded.  
`omit_empty` | Whether to omit samples that have no labels after filtering.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property labels#
    

A list of dicts specifying the labels to exclude.

property ids#
    

A list of IDs of labels to exclude.

property instance_ids#
    

A list of instance IDs of labels to exclude.

property tags#
    

A list of tags of labels to exclude.

property fields#
    

A list of fields from which labels are being excluded.

property omit_empty#
    

Whether to omit samples that have no labels after filtering.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.Exists(_field_ , _bool =None_)#
    

Bases: `ViewStage`

Returns a view containing the samples in a collection that have (or do not have) a non-`None` value for the given field or embedded field.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                ground_truth=fo.Classification(label="cat"),
                predictions=fo.Classification(label="cat", confidence=0.9),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                ground_truth=fo.Classification(label="dog"),
                predictions=fo.Classification(label="dog", confidence=0.8),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                ground_truth=fo.Classification(label="dog"),
                predictions=fo.Classification(label="dog"),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                ground_truth=None,
                predictions=None,
            ),
            fo.Sample(filepath="/path/to/image5.png"),
        ]
    )
    
    #
    # Only include samples that have a value in their `predictions` field
    #
    
    stage = fo.Exists("predictions")
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that do NOT have a value in their `predictions`
    # field
    #
    
    stage = fo.Exists("predictions", False)
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that have prediction confidences
    #
    
    stage = fo.Exists("predictions.confidence")
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **field** â the field name or `embedded.field.name`

  * **bool** (_True_) â whether to check if the field exists (None or True) or does not exist (False)




**Attributes:**

`field` | The field to check for existence.  
---|---  
`bool` | Whether to check if the field exists (True) or does not exist (False).  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property field#
    

The field to check for existence.

property bool#
    

Whether to check if the field exists (True) or does not exist (False).

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.FilterField(_field_ , _filter_ , _only_matches =True_, __new_field =None_)#
    

Bases: `ViewStage`

Filters the values of a given field or embedded field of each sample in a collection.

Values of `field` for which `filter` returns `False` are replaced with `None`.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                ground_truth=fo.Classification(label="cat"),
                predictions=fo.Classification(label="cat", confidence=0.9),
                numeric_field=1.0,
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                ground_truth=fo.Classification(label="dog"),
                predictions=fo.Classification(label="dog", confidence=0.8),
                numeric_field=-1.0,
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                ground_truth=None,
                predictions=None,
                numeric_field=None,
            ),
        ]
    )
    
    #
    # Only include classifications in the `predictions` field
    # whose `label` is "cat"
    #
    
    stage = fo.FilterField("predictions", F("label") == "cat")
    view = dataset.add_stage(stage)
    
    #
    # Only include samples whose `numeric_field` value is positive
    #
    
    stage = fo.FilterField("numeric_field", F() > 0)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **field** â the field name or `embedded.field.name`

  * **filter** â a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

  * **only_matches** (_True_) â whether to only include samples that match the filter (True) or include all samples (False)




**Attributes:**

`field` | The field to filter.  
---|---  
`filter` | The filter expression.  
`only_matches` | Whether to only include samples that match the filter.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field#
    

The field to filter.

property filter#
    

The filter expression.

property only_matches#
    

Whether to only include samples that match the filter.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.FilterLabels(_field_ , _filter_ , _only_matches =True_, _trajectories =False_, __new_field =None_, __validate =True_)#
    

Bases: `ViewStage`

Filters the [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field of each sample in a collection.

If the specified `field` is a single [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") type, fields for which `filter` returns `False` are replaced with `None`:

  * [`fiftyone.core.labels.Classification`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classification "fiftyone.core.labels.Classification")

  * [`fiftyone.core.labels.Detection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detection "fiftyone.core.labels.Detection")

  * [`fiftyone.core.labels.Polyline`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polyline "fiftyone.core.labels.Polyline")

  * [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint")




If the specified `field` is a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") list type, the label elements for which `filter` returns `False` are omitted from the view:

  * [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications")

  * [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

  * [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

  * [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")




Classifications Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Classification(label="cat", confidence=0.9),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Classification(label="dog", confidence=0.8),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=fo.Classification(label="rabbit"),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Only include classifications in the `predictions` field whose
    # `confidence` is greater than 0.8
    #
    
    stage = fo.FilterLabels("predictions", F("confidence") > 0.8)
    view = dataset.add_stage(stage)
    
    #
    # Only include classifications in the `predictions` field whose `label`
    # is "cat" or "dog"
    #
    
    stage = fo.FilterLabels("predictions", F("label").is_in(["cat", "dog"]))
    view = dataset.add_stage(stage)
    

Detections Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.1, 0.1, 0.5, 0.5],
                            confidence=0.9,
                        ),
                        fo.Detection(
                            label="dog",
                            bounding_box=[0.2, 0.2, 0.3, 0.3],
                            confidence=0.8,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.5, 0.5, 0.4, 0.4],
                            confidence=0.95,
                        ),
                        fo.Detection(label="rabbit"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="squirrel",
                            bounding_box=[0.25, 0.25, 0.5, 0.5],
                            confidence=0.5,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Only include detections in the `predictions` field whose `confidence`
    # is greater than 0.8
    #
    
    stage = fo.FilterLabels("predictions", F("confidence") > 0.8)
    view = dataset.add_stage(stage)
    
    #
    # Only include detections in the `predictions` field whose `label` is
    # "cat" or "dog"
    #
    
    stage = fo.FilterLabels("predictions", F("label").is_in(["cat", "dog"]))
    view = dataset.add_stage(stage)
    
    #
    # Only include detections in the `predictions` field whose bounding box
    # area is smaller than 0.2
    #
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox_area = F("bounding_box")[2] * F("bounding_box")[3]
    
    stage = fo.FilterLabels("predictions", bbox_area < 0.2)
    view = dataset.add_stage(stage)
    

Polylines Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Polylines(
                    polylines=[
                        fo.Polyline(
                            label="lane",
                            points=[[(0.1, 0.1), (0.1, 0.6)]],
                            filled=False,
                        ),
                        fo.Polyline(
                            label="road",
                            points=[[(0.2, 0.2), (0.5, 0.5), (0.2, 0.5)]],
                            filled=True,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Polylines(
                    polylines=[
                        fo.Polyline(
                            label="lane",
                            points=[[(0.4, 0.4), (0.9, 0.4)]],
                            filled=False,
                        ),
                        fo.Polyline(
                            label="road",
                            points=[[(0.6, 0.6), (0.9, 0.9), (0.6, 0.9)]],
                            filled=True,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Only include polylines in the `predictions` field that are filled
    #
    
    stage = fo.FilterLabels("predictions", F("filled") == True)
    view = dataset.add_stage(stage)
    
    #
    # Only include polylines in the `predictions` field whose `label` is
    # "lane"
    #
    
    stage = fo.FilterLabels("predictions", F("label") == "lane")
    view = dataset.add_stage(stage)
    
    #
    # Only include polylines in the `predictions` field with at least
    # 3 vertices
    #
    
    num_vertices = F("points").map(F().length()).sum()
    stage = fo.FilterLabels("predictions", num_vertices >= 3)
    view = dataset.add_stage(stage)
    

Keypoints Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Keypoint(
                    label="house",
                    points=[(0.1, 0.1), (0.1, 0.9), (0.9, 0.9), (0.9, 0.1)],
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Keypoint(
                    label="window",
                    points=[(0.4, 0.4), (0.5, 0.5), (0.6, 0.6)],
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Only include keypoints in the `predictions` field whose `label` is
    # "house"
    #
    
    stage = fo.FilterLabels("predictions", F("label") == "house")
    view = dataset.add_stage(stage)
    
    #
    # Only include keypoints in the `predictions` field with less than four
    # points
    #
    
    stage = fo.FilterLabels("predictions", F("points").length() < 4)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **field** â the label field to filter

  * **filter** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

  * **only_matches** (_True_) â whether to only include samples with at least one label after filtering (True) or include all samples (False)

  * **trajectories** (_False_) â whether to match entire object trajectories for which the object matches the given filter on at least one frame. Only applicable to video datasets and frame-level label fields whose objects have their `index` attributes populated




**Attributes:**

`field` | The label field to filter.  
---|---  
`filter` | The filter expression.  
`only_matches` | Whether to only include samples that match the filter.  
`trajectories` | Whether to match entire object trajectories for which the object matches the given filter on at least one frame.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field#
    

The label field to filter.

property filter#
    

The filter expression.

property only_matches#
    

Whether to only include samples that match the filter.

property trajectories#
    

Whether to match entire object trajectories for which the object matches the given filter on at least one frame.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.FilterKeypoints(_field_ , _filter =None_, _labels =None_, _only_matches =True_, __new_field =None_)#
    

Bases: `ViewStage`

Filters the individual [`fiftyone.core.labels.Keypoint.points`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.points "fiftyone.core.labels.Keypoint.points") elements in the specified keypoints field of each sample in the collection.

Note

Use `FilterLabels` if you simply want to filter entire [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") objects in a field.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Keypoints(
                    keypoints=[
                        fo.Keypoint(
                            label="person",
                            points=[(0.1, 0.1), (0.1, 0.9), (0.9, 0.9), (0.9, 0.1)],
                            confidence=[0.7, 0.8, 0.95, 0.99],
                        )
                    ]
                )
            ),
            fo.Sample(filepath="/path/to/image2.png"),
        ]
    )
    
    dataset.default_skeleton = fo.KeypointSkeleton(
        labels=["nose", "left eye", "right eye", "left ear", "right ear"],
        edges=[[0, 1, 2, 0], [0, 3], [0, 4]],
    )
    
    #
    # Only include keypoints in the `predictions` field whose
    # `confidence` is greater than 0.9
    #
    
    stage = fo.FilterKeypoints("predictions", filter=F("confidence") > 0.9)
    view = dataset.add_stage(stage)
    
    #
    # Only include keypoints in the `predictions` field with less than
    # four points
    #
    
    stage = fo.FilterKeypoints("predictions", labels=["left eye", "right eye"])
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **field** â the [`fiftyone.core.labels.Keypoint`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint "fiftyone.core.labels.Keypoint") or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints") field to filter

  * **filter** (_None_) â a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean, like `F("confidence") > 0.5` or `F("occluded") == False`, to apply elementwise to the specified field, which must be a list of same length as [`fiftyone.core.labels.Keypoint.points`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoint.points "fiftyone.core.labels.Keypoint.points")

  * **labels** (_None_) â a label or iterable of keypoint skeleton labels to keep

  * **only_matches** (_True_) â whether to only include keypoints/samples with at least one point after filtering (True) or include all keypoints/samples (False)




**Attributes:**

`filter` | The filter expression.  
---|---  
`labels` | An iterable of keypoint skeleton labels to keep.  
`only_matches` | Whether to only include samples that match the filter.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property filter#
    

The filter expression.

property labels#
    

An iterable of keypoint skeleton labels to keep.

property only_matches#
    

Whether to only include samples that match the filter.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.GeoNear(_point_ , _location_field =None_, _min_distance =None_, _max_distance =None_, _query =None_, _create_index =False_)#
    

Bases: `_GeoStage`

Sorts the samples in a collection by their proximity to a specified geolocation.

Note

This stage must be the **first stage** in any [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") in which it appears, and it **requires** a spherical index on the specified location field.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    TIMES_SQUARE = [-73.9855, 40.7580]
    
    dataset = foz.load_zoo_dataset("quickstart-geo")
    
    #
    # Sort the samples by their proximity to Times Square
    #
    
    stage = fo.GeoNear(TIMES_SQUARE, create_index=True)
    view = dataset.add_stage(stage)
    
    #
    # Sort the samples by their proximity to Times Square, and only
    # include samples within 5km
    #
    
    stage = fo.GeoNear(
        TIMES_SQUARE,
        max_distance=5000,
        create_index=True,
    )
    view = dataset.add_stage(stage)
    
    #
    # Sort the samples by their proximity to Times Square, and only
    # include samples that are in Manhattan
    #
    
    import fiftyone.utils.geojson as foug
    
    in_manhattan = foug.geo_within(
        "location.point",
        [
            [
                [-73.949701, 40.834487],
                [-73.896611, 40.815076],
                [-73.998083, 40.696534],
                [-74.031751, 40.715273],
                [-73.949701, 40.834487],
            ]
        ]
    )
    
    stage = fo.GeoNear(
        TIMES_SQUARE,
        location_field="location",
        query=in_manhattan,
        create_index=True,
    )
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **point** â 

the reference point to compute distances to. Can be any of the following:

    * A `[longitude, latitude]` list

    * A GeoJSON dict with `Point` type

    * A [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation") instance whose `point` attribute contains the point

  * **location_field** (_None_) â 

the location data of each sample to use. Can be any of the following:

    * The name of a `fiftyone.core.fields.GeoLocation` field whose `point` attribute to use as location data

    * An `embedded.field.name` containing GeoJSON data to use as location data

    * `None`, in which case there must be a single `fiftyone.core.fields.GeoLocation` field on the samples, which is used by default

  * **min_distance** (_None_) â filter samples that are less than this distance (in meters) from `point`

  * **max_distance** (_None_) â filter samples that are greater than this distance (in meters) from `point`

  * **query** (_None_) â an optional dict defining a [MongoDB read query](https://docs.mongodb.com/manual/tutorial/query-documents/#read-operations-query-argument) that samples must match in order to be included in this view

  * **create_index** (_False_) â whether to create the required spherical index, if necessary




**Attributes:**

`point` | The point to search proximity to.  
---|---  
`min_distance` | The minimum distance for matches, in meters.  
`max_distance` | The maximum distance for matches, in meters.  
`query` | A query dict specifying a match condition.  
`create_index` | Whether to create the relevant spherical index, if necessary.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`location_field` | The location field.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_,Â **__) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property point#
    

The point to search proximity to.

property min_distance#
    

The minimum distance for matches, in meters.

property max_distance#
    

The maximum distance for matches, in meters.

property query#
    

A query dict specifying a match condition.

to_mongo(___ , _** ___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property create_index#
    

Whether to create the relevant spherical index, if necessary.

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property location_field#
    

The location field.

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.GeoWithin(_boundary_ , _location_field =None_, _strict =True_, _create_index =False_)#
    

Bases: `_GeoStage`

Filters the samples in a collection to only match samples whose geolocation is within a specified boundary.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    MANHATTAN = [
        [
            [-73.949701, 40.834487],
            [-73.896611, 40.815076],
            [-73.998083, 40.696534],
            [-74.031751, 40.715273],
            [-73.949701, 40.834487],
        ]
    ]
    
    dataset = foz.load_zoo_dataset("quickstart-geo")
    
    #
    # Create a view that only contains samples in Manhattan
    #
    
    stage = fo.GeoWithin(MANHATTAN)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **boundary** â a [`fiftyone.core.labels.GeoLocation`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocation "fiftyone.core.labels.GeoLocation"), [`fiftyone.core.labels.GeoLocations`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.GeoLocations "fiftyone.core.labels.GeoLocations"), GeoJSON dict, or list of coordinates that define a `Polygon` or `MultiPolygon` to search within

  * **location_field** (_None_) â 

the location data of each sample to use. Can be any of the following:

    * The name of a `fiftyone.core.fields.GeoLocation` field whose `point` attribute to use as location data

    * An `embedded.field.name` that directly contains the GeoJSON location data to use

    * `None`, in which case there must be a single `fiftyone.core.fields.GeoLocation` field on the samples, which is used by default

  * **strict** (_True_) â whether a sampleâs location data must strictly fall within boundary (True) in order to match, or whether any intersection suffices (False)

  * **create_index** (_False_) â whether to create a spherical index, if necessary, to optimize the query




**Attributes:**

`boundary` | A GeoJSON dict describing the boundary to match within.  
---|---  
`strict` | Whether matches must be strictly contained in the boundary.  
`create_index` | Whether to create the relevant spherical index, if necessary.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`location_field` | The location field.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_,Â **__) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property boundary#
    

A GeoJSON dict describing the boundary to match within.

property strict#
    

Whether matches must be strictly contained in the boundary.

to_mongo(___ , _** ___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property create_index#
    

Whether to create the relevant spherical index, if necessary.

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property location_field#
    

The location field.

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.GroupBy(_field_or_expr_ , _order_by =None_, _reverse =False_, _flat =False_, _match_expr =None_, _sort_expr =None_, _create_index =False_, _order_by_key =None_)#
    

Bases: `ViewStage`

Creates a view that groups the samples in a collection by a specified field or expression.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("cifar10", split="test")
    
    #
    # Take 1000 samples at random and group them by ground truth label
    #
    
    stage = fo.GroupBy("ground_truth.label")
    view = dataset.take(1000).add_stage(stage)
    
    for group in view.iter_groups():
        print("%s: %d" % (group[0].ground_truth.label, len(group)))
    
    #
    # Variation of above operation that arranges the groups in decreasing
    # order of size and immediately flattens them
    #
    
    from itertools import groupby
    
    stage = fo.GroupBy(
        "ground_truth.label",
        flat=True,
        sort_expr=F().length(),
        reverse=True,
    )
    view = dataset.take(1000).add_stage(stage)
    
    rle = lambda v: [(k, len(list(g))) for k, g in groupby(v)]
    for label, count in rle(view.values("ground_truth.label")):
        print("%s: %d" % (label, count))
    

Parameters:
    

  * **field_or_expr** â 

the field or `embedded.field.name` to group by, or a list of field names defining a compound group key, or a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines the value to group by

  * **order_by** (_None_) â an optional field by which to order the samples in each group

  * **reverse** (_False_) â whether to return the results in descending order. Applies to both `order_by` and `sort_expr`

  * **flat** (_False_) â whether to return a grouped collection (False) or a flattened collection (True)

  * **match_expr** (_None_) â 

an optional [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines which groups to include in the output view. If provided, this expression will be evaluated on the list of samples in each group. Only applicable when `flat=True`

  * **sort_expr** (_None_) â 

an optional [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines how to sort the groups in the output view. If provided, this expression will be evaluated on the list of samples in each group. Only applicable when `flat=True`

  * **create_index** (_False_) â whether to create an index, if necessary, to optimize the grouping. Only applicable when grouping by field(s), not expressions

  * **order_by_key** (_None_) â an optional fixed `order_by` value representing the first sample in a group. Required for optimized performance. See [this guide](user_guide__app.md#app-query-performant-stages) for more details




**Attributes:**

`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
---|---  
`field_or_expr` | The field or expression to group by.  
`order_by` | The field by which to order the samples in each group.  
`order_by_key` | The `order_by` value representing the first sample in a group.  
`reverse` | Whether to sort the groups in descending order.  
`flat` | Whether to generate a flattened collection.  
`match_expr` | An expression to apply to select groups in the output view.  
`sort_expr` | An expression defining how the sort the groups in the output view.  
`create_index` | Whether to create an index, if necessary, to optimize the grouping.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




property field_or_expr#
    

The field or expression to group by.

property order_by#
    

The field by which to order the samples in each group.

property order_by_key#
    

The `order_by` value representing the first sample in a group.

property reverse#
    

Whether to sort the groups in descending order.

property flat#
    

Whether to generate a flattened collection.

property match_expr#
    

An expression to apply to select groups in the output view.

property sort_expr#
    

An expression defining how the sort the groups in the output view.

property create_index#
    

Whether to create an index, if necessary, to optimize the grouping.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

class fiftyone.core.stages.Flatten(_stages =None_)#
    

Bases: `ViewStage`

Returns a flattened view that contains all samples in a dynamic grouped collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("cifar10", split="test")
    
    # Group samples by ground truth label
    grouped_view = dataset.take(1000).group_by("ground_truth.label")
    print(len(grouped_view))  # 10
    
    # Return a flat view that contains 10 samples from each class
    stage = fo.Flatten(fo.Limit(10))
    flat_view = grouped_view.add_stage(stage)
    print(len(flat_view))  # 100
    

Parameters:
    

**stages** (_None_) â a `ViewStage` or list of `ViewStage` instances to apply to each groupâs samples while flattening

**Attributes:**

`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
---|---  
`stages` | Stage(s) to apply to each group's samples while flattening.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




property stages#
    

Stage(s) to apply to each groupâs samples while flattening.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

class fiftyone.core.stages.Limit(_limit_)#
    

Bases: `ViewStage`

Creates a view with at most the given number of samples.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                ground_truth=fo.Classification(label="cat"),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                ground_truth=fo.Classification(label="dog"),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                ground_truth=None,
            ),
        ]
    )
    
    #
    # Only include the first 2 samples in the view
    #
    
    stage = fo.Limit(2)
    view = dataset.add_stage(stage)
    

Parameters:
    

**limit** â the maximum number of samples to return. If a non-positive number is provided, an empty view is returned

**Attributes:**

`limit` | The maximum number of samples to return.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property limit#
    

The maximum number of samples to return.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.LimitLabels(_field_ , _limit_)#
    

Bases: `ViewStage`

Limits the number of [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") instances in the specified labels list field of each sample in a collection.

The specified `field` must be one of the following types:

  * [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications")

  * [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

  * [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")




Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.1, 0.1, 0.5, 0.5],
                            confidence=0.9,
                        ),
                        fo.Detection(
                            label="dog",
                            bounding_box=[0.2, 0.2, 0.3, 0.3],
                            confidence=0.8,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.5, 0.5, 0.4, 0.4],
                            confidence=0.95,
                        ),
                        fo.Detection(label="rabbit"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Only include the first detection in the `predictions` field of each
    # sample
    #
    
    stage = fo.LimitLabels("predictions", 1)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **field** â the labels list field to filter

  * **limit** â the maximum number of labels to include in each labels list. If a non-positive number is provided, all lists will be empty




**Attributes:**

`field` | The labels field to limit.  
---|---  
`limit` | The maximum number of labels to allow in each labels list.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field#
    

The labels field to limit.

property limit#
    

The maximum number of labels to allow in each labels list.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.MapLabels(_field_ , _map_)#
    

Bases: `ViewStage`

Maps the `label` values of a [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") field to new values for each sample in a collection.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                weather=fo.Classification(label="sunny"),
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.1, 0.1, 0.5, 0.5],
                            confidence=0.9,
                        ),
                        fo.Detection(
                            label="dog",
                            bounding_box=[0.2, 0.2, 0.3, 0.3],
                            confidence=0.8,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                weather=fo.Classification(label="cloudy"),
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.5, 0.5, 0.4, 0.4],
                            confidence=0.95,
                        ),
                        fo.Detection(label="rabbit"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                weather=fo.Classification(label="partly cloudy"),
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="squirrel",
                            bounding_box=[0.25, 0.25, 0.5, 0.5],
                            confidence=0.5,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Map the "partly cloudy" weather label to "cloudy"
    #
    
    stage = fo.MapLabels("weather", {"partly cloudy": "cloudy"})
    view = dataset.add_stage(stage)
    
    #
    # Map "rabbit" and "squirrel" predictions to "other"
    #
    
    stage = fo.MapLabels(
        "predictions", {"rabbit": "other", "squirrel": "other"}
    )
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **field** â the labels field to map

  * **map** â a dict mapping label values to new label values




**Attributes:**

`field` | The labels field to map.  
---|---  
`map` | The labels map dict.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field#
    

The labels field to map.

property map#
    

The labels map dict.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.MapValues(_field_ , _map_)#
    

Bases: `ViewStage`

Maps the values in the given field to new values for each sample in a collection.

Examples:
    
    
    import random
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    values = [random.choice(ANIMALS) for _ in range(len(dataset))]
    dataset.set_values("str_field", values)
    dataset.set_values("list_field", [[v] for v in values])
    
    dataset.set_field("ground_truth.detections.tags", [F("label")]).save()
    
    # Map all animals to string "animal"
    mapping = {a: "animal" for a in ANIMALS}
    
    #
    # Map values in top-level fields
    #
    
    stage = fo.MapValues("str_field", mapping)
    view = dataset.add_stage(stage)
    
    print(view.count_values("str_field"))
    # {"animal": 200}
    
    stage = fo.MapValues("list_field", mapping)
    view = dataset.add_stage(stage)
    
    print(view.count_values("list_field"))
    # {"animal": 200}
    
    #
    # Map values in nested fields
    #
    
    stage = fo.MapValues("ground_truth.detections.label", mapping)
    view = dataset.add_stage(stage)
    
    print(view.count_values("ground_truth.detections.label"))
    # {"animal": 183, ...}
    
    stage = fo.MapValues("ground_truth.detections.tags", mapping)
    view = dataset.add_stage(stage)
    
    print(view.count_values("ground_truth.detections.tags"))
    # {"animal": 183, ...}
    

Parameters:
    

  * **field** â the field or `embedded.field.name` to map

  * **map** â a dict mapping values to new values




**Attributes:**

`field` | The field to map.  
---|---  
`map` | The value map dict.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property field#
    

The field to map.

property map#
    

The value map dict.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.SetField(_field_ , _expr_ , __allow_missing =False_, __allow_limit =False_)#
    

Bases: `ViewStage`

Sets a field or embedded field on each sample in a collection by evaluating the given expression.

This method can process embedded list fields. To do so, simply append `[]` to any list component(s) of the field path.

Note

There are two cases where FiftyOne will automatically unwind array fields without requiring you to explicitly specify this via the `[]` syntax:

**Top-level lists:** when you specify a `field` path that refers to a top-level list field of a dataset; i.e., `list_field` is automatically coerced to `list_field[]`, if necessary.

**List fields:** When you specify a `field` path that refers to the list field of a [`Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") class, such as the [`Detections.detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections.detections "fiftyone.core.labels.Detections.detections") attribute; i.e., `ground_truth.detections.label` is automatically coerced to `ground_truth.detections[].label`, if necessary.

See the examples below for demonstrations of this behavior.

The provided `expr` is interpreted relative to the document on which the embedded field is being set. For example, if you are setting a nested field `field="embedded.document.field"`, then the expression `expr` you provide will be applied to the `embedded.document` document. Note that you can override this behavior by defining an expression that is bound to the root document by prepending `"$"` to any field name(s) in the expression.

See the examples below for more information.

Note

Note that you cannot set a non-existing top-level field using this stage, since doing so would violate the datasetâs schema. You can, however, first declare a new field via [`fiftyone.core.dataset.Dataset.add_sample_field()`](https://docs.voxel51.com/api/fiftyone.core.dataset.html#fiftyone.core.dataset.Dataset.add_sample_field "fiftyone.core.dataset.Dataset.add_sample_field") and then populate it in a view via this stage.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Replace all values of uniqueness that are less than 0.5 with `None`
    #
    
    stage = fo.SetField(
        "uniqueness",
        (F("uniqueness") >= 0.5).if_else(F("uniqueness"), None)
    )
    view = dataset.add_stage(stage)
    print(view.bounds("uniqueness"))
    
    #
    # Lower bound all object confidences in the `predictions` field by 0.5
    #
    
    stage = fo.SetField(
        "predictions.detections.confidence", F("confidence").max(0.5)
    )
    view = dataset.add_stage(stage)
    print(view.bounds("predictions.detections.confidence"))
    
    #
    # Add a `num_predictions` property to the `predictions` field that
    # contains the number of objects in the field
    #
    
    stage = fo.SetField(
        "predictions.num_predictions",
        F("$predictions.detections").length(),
    )
    view = dataset.add_stage(stage)
    print(view.bounds("predictions.num_predictions"))
    
    #
    # Set an `is_animal` field on each object in the `predictions` field
    # that indicates whether the object is an animal
    #
    
    ANIMALS = [
        "bear", "bird", "cat", "cow", "dog", "elephant", "giraffe",
        "horse", "sheep", "zebra"
    ]
    
    stage = fo.SetField(
        "predictions.detections.is_animal", F("label").is_in(ANIMALS)
    )
    view = dataset.add_stage(stage)
    print(view.count_values("predictions.detections.is_animal"))
    

Parameters:
    

  * **field** â the field or `embedded.field.name` to set

  * **expr** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines the field value to set




**Attributes:**

`field` | The field to set.  
---|---  
`expr` | The expression to apply.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field#
    

The field to set.

property expr#
    

The expression to apply.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.Match(_filter_)#
    

Bases: `ViewStage`

Filters the samples in the collection by the given filter.

Examples:
    
    
    import fiftyone as fo
    from fiftyone import ViewField as F
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                weather=fo.Classification(label="sunny"),
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.1, 0.1, 0.5, 0.5],
                            confidence=0.9,
                        ),
                        fo.Detection(
                            label="dog",
                            bounding_box=[0.2, 0.2, 0.3, 0.3],
                            confidence=0.8,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.jpg",
                weather=fo.Classification(label="cloudy"),
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.5, 0.5, 0.4, 0.4],
                            confidence=0.95,
                        ),
                        fo.Detection(label="rabbit"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                weather=fo.Classification(label="partly cloudy"),
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="squirrel",
                            bounding_box=[0.25, 0.25, 0.5, 0.5],
                            confidence=0.5,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image4.jpg",
                predictions=None,
            ),
        ]
    )
    
    #
    # Only include samples whose `filepath` ends with ".jpg"
    #
    
    stage = fo.Match(F("filepath").ends_with(".jpg"))
    view = dataset.add_stage(stage)
    
    #
    # Only include samples whose `weather` field is "sunny"
    #
    
    stage = fo.Match(F("weather.label") == "sunny")
    view = dataset.add_stage(stage)
    
    #
    # Only include samples with at least 2 objects in their `predictions`
    # field
    #
    
    stage = fo.Match(F("predictions.detections").length() >= 2)
    view = dataset.add_stage(stage)
    
    #
    # Only include samples whose `predictions` field contains at least one
    # object with area smaller than 0.2
    #
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox = F("bounding_box")
    bbox_area = bbox[2] * bbox[3]
    
    small_boxes = F("predictions.detections").filter(bbox_area < 0.2)
    stage = fo.Match(small_boxes.length() > 0)
    view = dataset.add_stage(stage)
    

Parameters:
    

**filter** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

**Attributes:**

`filter` | The filter expression.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property filter#
    

The filter expression.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.SelectGroupSlices(_slices =None_, _media_type =None_, _flat =True_, __allow_mixed =False_, __force_mixed =False_)#
    

Bases: `ViewStage`

Selects the specified group slice(s) from a grouped collection.

When `flat==True`, the returned view is a flattened non-grouped view containing the samples from the slice(s) of interest.

When `flat=False`, the returned view is a grouped collection containing only the slice(s) of interest.

Note

When `flat=True`, this stage performs a `$lookup` that pulls the requested slice(s) for each sample in the input collection from the source dataset. As a result, the stage emits _unfiltered samples_.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_group_field("group", default="ego")
    
    group1 = fo.Group()
    group2 = fo.Group()
    
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/left-image1.jpg",
                group=group1.element("left"),
            ),
            fo.Sample(
                filepath="/path/to/video1.mp4",
                group=group1.element("ego"),
            ),
            fo.Sample(
                filepath="/path/to/right-image1.jpg",
                group=group1.element("right"),
            ),
            fo.Sample(
                filepath="/path/to/left-image2.jpg",
                group=group2.element("left"),
            ),
            fo.Sample(
                filepath="/path/to/video2.mp4",
                group=group2.element("ego"),
            ),
            fo.Sample(
                filepath="/path/to/right-image2.jpg",
                group=group2.element("right"),
            ),
        ]
    )
    
    #
    # Retrieve the samples from the "ego" group slice
    #
    
    stage = fo.SelectGroupSlices("ego")
    view = dataset.add_stage(stage)
    
    #
    # Retrieve the samples from the "left" or "right" group slices
    #
    
    stage = fo.SelectGroupSlices(["left", "right"])
    view = dataset.add_stage(stage)
    
    #
    # Select only the "left" and "right" group slices
    #
    
    stage = fo.SelectGroupSlices(["left", "right"], flat=False)
    view = dataset.add_stage(stage)
    
    #
    # Retrieve all image samples
    #
    
    stage = fo.SelectGroupSlices(media_type="image")
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **slices** (_None_) â a group slice or iterable of group slices to select. If neither argument is provided, a flattened list of all samples is returned

  * **media_type** (_None_) â a media type or iterable of media types whose slice(s) to select

  * **flat** (_True_) â whether to return a flattened collection (True) or a grouped collection (False)




**Attributes:**

`slices` | The group slice(s) to select.  
---|---  
`media_type` | The media type(s) whose slices to select.  
`flat` | Whether to generate a flattened collection.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property slices#
    

The group slice(s) to select.

property media_type#
    

The media type(s) whose slices to select.

property flat#
    

Whether to generate a flattened collection.

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.ExcludeGroupSlices(_slices =None_, _media_type =None_)#
    

Bases: `ViewStage`

Excludes the specified group slice(s) from a grouped collection.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_group_field("group", default="ego")
    
    group1 = fo.Group()
    group2 = fo.Group()
    
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/left-image1.jpg",
                group=group1.element("left"),
            ),
            fo.Sample(
                filepath="/path/to/video1.mp4",
                group=group1.element("ego"),
            ),
            fo.Sample(
                filepath="/path/to/right-image1.jpg",
                group=group1.element("right"),
            ),
            fo.Sample(
                filepath="/path/to/left-image2.jpg",
                group=group2.element("left"),
            ),
            fo.Sample(
                filepath="/path/to/video2.mp4",
                group=group2.element("ego"),
            ),
            fo.Sample(
                filepath="/path/to/right-image2.jpg",
                group=group2.element("right"),
            ),
        ]
    )
    
    #
    # Exclude the "ego" group slice
    #
    
    stage = fo.ExcludeGroupSlices("ego")
    view = dataset.add_stage(stage)
    
    #
    # Exclude the "left" and "right" group slices
    #
    
    stage = fo.ExcludeGroupSlices(["left", "right"])
    view = dataset.add_stage(stage)
    
    #
    # Exclude all image slices
    #
    
    stage = fo.ExcludeGroupSlices(media_type="image")
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **slices** (_None_) â a group slice or iterable of group slices to exclude.

  * **media_type** (_None_) â a media type or iterable of media types whose slice(s) to exclude




**Attributes:**

`slices` | The group slice(s) to exclude.  
---|---  
`media_type` | The media type(s) whose slices to exclude.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property slices#
    

The group slice(s) to exclude.

property media_type#
    

The media type(s) whose slices to exclude.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.MatchFrames(_filter_ , _omit_empty =True_)#
    

Bases: `ViewStage`

Filters the frames in a video collection by the given filter.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    #
    # Match frames with at least 10 detections
    #
    
    num_objects = F("detections.detections").length()
    stage = fo.MatchFrames(num_objects > 10)
    view = dataset.add_stage(stage)
    
    print(dataset.count())
    print(view.count())
    
    print(dataset.count("frames"))
    print(view.count("frames"))
    

Parameters:
    

  * **filter** â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing the filter to apply

  * **omit_empty** (_True_) â whether to omit samples with no frame labels after filtering




**Attributes:**

`filter` | The filter expression.  
---|---  
`omit_empty` | Whether to omit samples that have no frames after filtering.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property filter#
    

The filter expression.

property omit_empty#
    

Whether to omit samples that have no frames after filtering.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.MatchLabels(_labels =None_, _ids =None_, _instance_ids =None_, _tags =None_, _filter =None_, _fields =None_, _bool =None_)#
    

Bases: `ViewStage`

Selects the samples from a collection that contain (or do not contain) at least one label that matches the specified criteria.

Note that, unlike `SelectLabels` and `FilterLabels`, this stage will not filter the labels themselves; it only selects the corresponding samples.

You can perform a selection via one or more of the following methods:

  * Provide the `labels` argument, which should contain a list of dicts in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels"), to match specific labels

  * Provide the `ids` argument to match labels with specific IDs

  * Provide the `instance_ids` argument to match labels with specific instance IDs

  * Provide the `tags` argument to match labels with specific tags

  * Provide the `filter` argument to match labels based on a boolean [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") that is applied to each individual [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") element

  * Pass `bool=False` to negate the operation and instead match samples that _do not_ contain at least one label matching the specified criteria




If multiple criteria are specified, labels must match all of them in order to trigger a sample match.

By default, the selection is applied to all [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields, but you can provide the `fields` argument to explicitly define the field(s) in which to search.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Only show samples whose labels are currently selected in the App
    #
    
    session = fo.launch_app(dataset)
    
    # Select some labels in the App...
    
    stage = fo.MatchLabels(labels=session.selected_labels)
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that contain labels with the specified IDs
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    stage = fo.MatchLabels(ids=ids)
    view = dataset.add_stage(stage)
    
    print(len(view))
    print(view.count("ground_truth.detections"))
    print(view.count("predictions.detections"))
    
    #
    # Only include samples that contain labels with the specified tags
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    # Give the labels a "test" tag
    dataset = dataset.clone()  # create copy since we're modifying data
    dataset.select_labels(ids=ids).tag_labels("test")
    
    print(dataset.count_values("ground_truth.detections.tags"))
    print(dataset.count_values("predictions.detections.tags"))
    
    # Retrieve the labels via their tag
    stage = fo.MatchLabels(tags="test")
    view = dataset.add_stage(stage)
    
    print(len(view))
    print(view.count("ground_truth.detections"))
    print(view.count("predictions.detections"))
    
    #
    # Only include samples that contain labels matching a filter
    #
    
    filter = F("confidence") > 0.99
    stage = fo.MatchLabels(filter=filter, fields="predictions")
    view = dataset.add_stage(stage)
    
    print(len(view))
    print(view.count("ground_truth.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

  * **labels** (_None_) â a list of dicts specifying the labels to select in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels")

  * **ids** (_None_) â an ID or iterable of IDs of the labels to select

  * **instance_ids** (_None_) â an instance ID or iterable of instance IDs of the labels to select

  * **tags** (_None_) â a tag or iterable of tags of labels to select

  * **filter** (_None_) â 

a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that returns a boolean describing whether to select a given label. In the case of list fields like [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), the filter is applied to the list elements, not the root field

  * **fields** (_None_) â a field or iterable of fields from which to select

  * **bool** (_None_) â whether to match samples that have (None or True) or do not have (False) at least one label that matches the specified criteria




**Attributes:**

`labels` | A list of dicts specifying the labels to match.  
---|---  
`ids` | A list of IDs of labels to match.  
`instance_ids` | A list of instance IDs of labels to match.  
`tags` | A list of tags of labels to match.  
`filter` | A filter expression that defines the labels to match.  
`fields` | A list of fields from which labels are being matched.  
`bool` | Whether to match samples that have (None or True) or do not have (False) at least one label that matches the specified criteria.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property labels#
    

A list of dicts specifying the labels to match.

property ids#
    

A list of IDs of labels to match.

property instance_ids#
    

A list of instance IDs of labels to match.

property tags#
    

A list of tags of labels to match.

property filter#
    

A filter expression that defines the labels to match.

property fields#
    

A list of fields from which labels are being matched.

property bool#
    

Whether to match samples that have (None or True) or do not have (False) at least one label that matches the specified criteria.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.MatchTags(_tags_ , _bool =None_, _all =False_)#
    

Bases: `ViewStage`

Returns a view containing the samples in the collection that have or donât have any/all of the given tag(s).

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image1.png", tags=["train"]),
            fo.Sample(filepath="image2.png", tags=["test"]),
            fo.Sample(filepath="image3.png", tags=["train", "test"]),
            fo.Sample(filepath="image4.png"),
        ]
    )
    
    #
    # Only include samples that have the "test" tag
    #
    
    stage = fo.MatchTags("test")
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that do not have the "test" tag
    #
    
    stage = fo.MatchTags("test", bool=False)
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that have the "test" or "train" tags
    #
    
    stage = fo.MatchTags(["test", "train"])
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that have the "test" and "train" tags
    #
    
    stage = fo.MatchTags(["test", "train"], all=True)
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that do not have the "test" or "train" tags
    #
    
    stage = fo.MatchTags(["test", "train"], bool=False)
    view = dataset.add_stage(stage)
    
    #
    # Only include samples that do not have the "test" and "train" tags
    #
    
    stage = fo.MatchTags(["test", "train"], bool=False, all=True)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **tags** â the tag or iterable of tags to match

  * **bool** (_None_) â whether to match samples that have (None or True) or do not have (False) the given tags

  * **all** (_False_) â whether to match samples that have (or donât have) all (True) or any (None or False) of the given tags




**Attributes:**

`tags` | The list of tags to match.  
---|---  
`bool` | Whether to match samples that have (True) or do not have (False) any of the given tags.  
`all` | Whether to match samples that have (or don't have) all (True) or any (False) of the given tags.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property tags#
    

The list of tags to match.

property bool#
    

Whether to match samples that have (True) or do not have (False) any of the given tags.

property all#
    

Whether to match samples that have (or donât have) all (True) or any (False) of the given tags.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.Mongo(_pipeline_ , __needs_frames =None_, __group_slices =None_)#
    

Bases: `ViewStage`

A view stage defined by a raw MongoDB aggregation pipeline.

See [MongoDB aggregation pipelines](https://docs.mongodb.com/manual/core/aggregation-pipeline/) for more details.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.1, 0.1, 0.5, 0.5],
                            confidence=0.9,
                        ),
                        fo.Detection(
                            label="dog",
                            bounding_box=[0.2, 0.2, 0.3, 0.3],
                            confidence=0.8,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.5, 0.5, 0.4, 0.4],
                            confidence=0.95,
                        ),
                        fo.Detection(label="rabbit"),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                predictions=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="squirrel",
                            bounding_box=[0.25, 0.25, 0.5, 0.5],
                            confidence=0.5,
                        ),
                    ]
                ),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                predictions=None,
            ),
        ]
    )
    
    #
    # Extract a view containing the second and third samples in the dataset
    #
    
    stage = fo.Mongo([{"$skip": 1}, {"$limit": 2}])
    view = dataset.add_stage(stage)
    
    #
    # Sort by the number of objects in the `precictions` field
    #
    
    stage = fo.Mongo([
        {
            "$addFields": {
                "_sort_field": {
                    "$size": {"$ifNull": ["$predictions.detections", []]}
                }
            }
        },
        {"$sort": {"_sort_field": -1}},
        {"$project": {"_sort_field": False}},
    ])
    view = dataset.add_stage(stage)
    

Parameters:
    

**pipeline** â a MongoDB aggregation pipeline (list of dicts)

**Attributes:**

`pipeline` | The MongoDB aggregation pipeline.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property pipeline#
    

The MongoDB aggregation pipeline.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.Select(_sample_ids_ , _ordered =False_)#
    

Bases: `ViewStage`

Selects the samples with the given IDs from a collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Create a view containing the currently selected samples in the App
    #
    
    session = fo.launch_app(dataset)
    
    # Select samples in the App...
    
    stage = fo.Select(session.selected)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **sample_ids** â 

the samples to select. Can be any of the following:

    * a sample ID

    * an iterable of sample IDs

    * an iterable of booleans of same length as the collection encoding which samples to select

    * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

    * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

    * a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **ordered** (_False_) â whether to sort the samples in the returned view to match the order of the provided IDs




**Attributes:**

`sample_ids` | The list of sample IDs to select.  
---|---  
`ordered` | Whether to sort the samples in the same order as the IDs.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property sample_ids#
    

The list of sample IDs to select.

property ordered#
    

Whether to sort the samples in the same order as the IDs.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.SelectBy(_field_ , _values_ , _ordered =False_)#
    

Bases: `ViewStage`

Selects the samples with the given field values from a collection.

This stage is typically used to work with categorical fields (strings, ints, and bools). If you want to select samples based on floating point fields, use `Match`.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(filepath="image%d.jpg" % i, int=i, str=str(i))
            for i in range(100)
        ]
    )
    
    #
    # Create a view containing samples whose `int` field have the given
    # values
    #
    
    stage = fo.SelectBy("int", [1, 51, 11, 41, 21, 31])
    view = dataset.add_stage(stage)
    print(view.head(6))
    
    #
    # Create a view containing samples whose `str` field have the given
    # values, in order
    #
    
    stage = fo.SelectBy(
        "str", ["1", "51", "11", "41", "21", "31"], ordered=True
    )
    view = dataset.add_stage(stage)
    print(view.head(6))
    

Parameters:
    

  * **field** â a field or `embedded.field.name`

  * **values** â a value or iterable of values to select by

  * **ordered** (_False_) â whether to sort the samples in the returned view to match the order of the provided values




**Attributes:**

`field` | The field whose values to select by.  
---|---  
`values` | The list of values to select by.  
`ordered` | Whether to sort the samples in the same order as the IDs.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property field#
    

The field whose values to select by.

property values#
    

The list of values to select by.

property ordered#
    

Whether to sort the samples in the same order as the IDs.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.SelectFields(_field_names =None_, _meta_filter =None_, __allow_missing =False_, __media_types =None_)#
    

Bases: `ViewStage`

Selects only the fields with the given names from the samples in the collection. All other fields are excluded.

Note that default sample fields are always selected.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                uniqueness=1.0,
                ground_truth=fo.Detections(
                    detections=[
                        fo.Detection(
                            label="cat",
                            bounding_box=[0.1, 0.1, 0.5, 0.5],
                            mood="surly",
                            age=51,
                        ),
                        fo.Detection(
                            label="dog",
                            bounding_box=[0.2, 0.2, 0.3, 0.3],
                            mood="happy",
                            age=52,
                        ),
                    ]
                )
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                uniqueness=0.0,
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
            ),
        ]
    )
    
    #
    # Include only the default fields on each sample
    #
    
    stage = fo.SelectFields()
    view = dataset.add_stage(stage)
    
    #
    # Include only the `uniqueness` field (and the default fields) on each
    # sample
    #
    
    stage = fo.SelectFields("uniqueness")
    view = dataset.add_stage(stage)
    
    #
    # Include only the `mood` attribute (and the default attributes) of
    # each `Detection` in the `ground_truth` field
    #
    
    stage = fo.SelectFields("ground_truth.detections.mood")
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **field_names** (_None_) â a field name or iterable of field names to select. May contain `embedded.field.name` as well

  * **meta_filter** (_None_) â 

a filter that dynamically selects fields in the collectionâs schema according to the specified rule, which can be matched against the fieldâs `name`, `type`, `description`, and/or `info`. For example:

    * Use `meta_filter="2023"` or `meta_filter={"any": "2023"}` to select fields that have the string â2023â anywhere in their name, type, description, or info

    * Use `meta_filter={"type": "StringField"}` or `meta_filter={"type": "Classification"}` to select all string or classification fields, respectively

    * Use `meta_filter={"description": "my description"}` to select fields whose description contains the string âmy descriptionâ

    * Use `meta_filter={"info": "2023"}` to select fields that have the string â2023â anywhere in their info

    * Use `meta_filter={"info.key": "value"}}` to select fields that have a specific key/value pair in their info

    * Include `meta_filter={"include_nested_fields": True, ...}` in your meta filter to include all nested fields in the filter




**Attributes:**

`field_names` | A list of field names to select.  
---|---  
`meta_filter` | A filter that dynamically selects fields.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
---|---  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field_names#
    

A list of field names to select.

property meta_filter#
    

A filter that dynamically selects fields.

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.SelectFrames(_frame_ids_ , _omit_empty =True_)#
    

Bases: `ViewStage`

Selects the frames with the given IDs from a video collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    #
    # Select some specific frames
    #
    
    frame_ids = [
        dataset.first().frames.first().id,
        dataset.last().frames.last().id,
    ]
    
    stage = fo.SelectFrames(frame_ids)
    view = dataset.add_stage(stage)
    
    print(dataset.count())
    print(view.count())
    
    print(dataset.count("frames"))
    print(view.count("frames"))
    

Parameters:
    

  * **frame_ids** â 

the frames to select. Can be any of the following:

    * a frame ID

    * an iterable of frame IDs

    * a [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") or [`fiftyone.core.frame.FrameView`](api__fiftyone.core.frame.md#fiftyone.core.frame.FrameView "fiftyone.core.frame.FrameView")

    * an iterable of [`fiftyone.core.frame.Frame`](api__fiftyone.core.frame.md#fiftyone.core.frame.Frame "fiftyone.core.frame.Frame") or [`fiftyone.core.frame.FrameView`](api__fiftyone.core.frame.md#fiftyone.core.frame.FrameView "fiftyone.core.frame.FrameView") instances

    * a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") whose frames to select

  * **omit_empty** (_True_) â whether to omit samples that have no frames after selecting the specified frames




**Attributes:**

`frame_ids` | The list of frame IDs to select.  
---|---  
`omit_empty` | Whether to omit samples that have no labels after filtering.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property frame_ids#
    

The list of frame IDs to select.

property omit_empty#
    

Whether to omit samples that have no labels after filtering.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.SelectGroups(_group_ids_ , _ordered =False_)#
    

Bases: `ViewStage`

Selects the groups with the given IDs from a grouped collection.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart-groups")
    
    #
    # Select some specific groups by ID
    #
    
    group_ids = dataset.take(10).values("group.id")
    
    stage = fo.SelectGroups(group_ids)
    view = dataset.add_stage(stage)
    
    assert set(view.values("group.id")) == set(group_ids)
    
    stage = fo.SelectGroups(group_ids, ordered=True)
    view = dataset.add_stage(stage)
    
    assert view.values("group.id") == group_ids
    

Parameters:
    

  * **groups_ids** â 

the groups to select. Can be any of the following:

    * a group ID

    * an iterable of group IDs

    * a [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView")

    * a group dict returned by [`get_group()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_group "fiftyone.core.collections.SampleCollection.get_group")

    * an iterable of [`fiftyone.core.sample.Sample`](api__fiftyone.utils.data.md#fiftyone.utils.data.Sample "fiftyone.core.sample.Sample") or [`fiftyone.core.sample.SampleView`](api__fiftyone.core.sample.md#fiftyone.core.sample.SampleView "fiftyone.core.sample.SampleView") instances

    * an iterable of group dicts returned by [`get_group()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.get_group "fiftyone.core.collections.SampleCollection.get_group")

    * a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

  * **ordered** (_False_) â whether to sort the groups in the returned view to match the order of the provided IDs




**Attributes:**

`group_ids` | The list of group IDs to select.  
---|---  
`ordered` | Whether to sort the groups in the same order as the IDs.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property group_ids#
    

The list of group IDs to select.

property ordered#
    

Whether to sort the groups in the same order as the IDs.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.SelectLabels(_labels =None_, _ids =None_, _instance_ids =None_, _tags =None_, _fields =None_, _omit_empty =True_)#
    

Bases: `ViewStage`

Selects only the specified labels from a collection.

The returned view will omit samples, sample fields, and individual labels that do not match the specified selection criteria.

You can perform a selection via one or more of the following methods:

  * Provide the `labels` argument, which should contain a list of dicts in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels"), to select specific labels

  * Provide the `ids` argument to select labels with specific IDs

  * Provide the `instance_ids` argument to select labels with specific instance IDs

  * Provide the `tags` argument to select labels with specific tags




If multiple criteria are specified, labels must match all of them in order to be selected.

By default, the selection is applied to all [`fiftyone.core.labels.Label`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Label "fiftyone.core.labels.Label") fields, but you can provide the `fields` argument to explicitly define the field(s) in which to select.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Only include the labels currently selected in the App
    #
    
    session = fo.launch_app(dataset)
    
    # Select some labels in the App...
    
    stage = fo.SelectLabels(labels=session.selected_labels)
    view = dataset.add_stage(stage)
    
    #
    # Only include labels with the specified IDs
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    stage = fo.SelectLabels(ids=ids)
    view = dataset.add_stage(stage)
    
    print(view.count("ground_truth.detections"))
    print(view.count("predictions.detections"))
    
    #
    # Only include labels with the specified tags
    #
    
    # Grab some label IDs
    ids = [
        dataset.first().ground_truth.detections[0].id,
        dataset.last().predictions.detections[0].id,
    ]
    
    # Give the labels a "test" tag
    dataset = dataset.clone()  # create copy since we're modifying data
    dataset.select_labels(ids=ids).tag_labels("test")
    
    print(dataset.count_values("ground_truth.detections.tags"))
    print(dataset.count_values("predictions.detections.tags"))
    
    # Retrieve the labels via their tag
    stage = fo.SelectLabels(tags="test")
    view = dataset.add_stage(stage)
    
    print(view.count("ground_truth.detections"))
    print(view.count("predictions.detections"))
    

Parameters:
    

  * **labels** (_None_) â a list of dicts specifying the labels to select in the format returned by [`fiftyone.core.session.Session.selected_labels`](api__fiftyone.core.session.md#fiftyone.core.session.Session.selected_labels "fiftyone.core.session.Session.selected_labels")

  * **ids** (_None_) â an ID or iterable of IDs of the labels to select

  * **instance_ids** (_None_) â an instance ID or iterable of instance IDs of the labels to select

  * **tags** (_None_) â a tag or iterable of tags of labels to select

  * **fields** (_None_) â a field or iterable of fields from which to select

  * **omit_empty** (_True_) â whether to omit samples that have no labels after filtering




**Attributes:**

`labels` | A list of dicts specifying the labels to select.  
---|---  
`ids` | A list of IDs of labels to select.  
`instance_ids` | A list of instance IDs of labels to select.  
`tags` | A list of tags of labels to select.  
`fields` | A list of fields from which labels are being selected.  
`omit_empty` | Whether to omit samples that have no labels after filtering.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
---|---  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property labels#
    

A list of dicts specifying the labels to select.

property ids#
    

A list of IDs of labels to select.

property instance_ids#
    

A list of instance IDs of labels to select.

property tags#
    

A list of tags of labels to select.

property fields#
    

A list of fields from which labels are being selected.

property omit_empty#
    

Whether to omit samples that have no labels after filtering.

get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.Shuffle(_seed =None_, __randint =None_)#
    

Bases: `ViewStage`

Randomly shuffles the samples in a collection.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                ground_truth=fo.Classification(label="cat"),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                ground_truth=fo.Classification(label="dog"),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                ground_truth=None,
            ),
        ]
    )
    
    #
    # Return a view that contains a randomly shuffled version of the
    # samples in the dataset
    #
    
    stage = fo.Shuffle()
    view = dataset.add_stage(stage)
    
    #
    # Shuffle the samples with a fixed random seed
    #
    
    stage = fo.Shuffle(seed=51)
    view = dataset.add_stage(stage)
    

Parameters:
    

**seed** (_None_) â an optional random seed to use when shuffling the samples

**Attributes:**

`seed` | The random seed to use, or `None`.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property seed#
    

The random seed to use, or `None`.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.Skip(_skip_)#
    

Bases: `ViewStage`

Omits the given number of samples from the head of a collection.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                ground_truth=fo.Classification(label="cat"),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                ground_truth=fo.Classification(label="dog"),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                ground_truth=fo.Classification(label="rabbit"),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                ground_truth=None,
            ),
        ]
    )
    
    #
    # Omit the first two samples from the dataset
    #
    
    stage = fo.Skip(2)
    view = dataset.add_stage(stage)
    

Parameters:
    

**skip** â the number of samples to skip. If a non-positive number is provided, no samples are omitted

**Attributes:**

`skip` | The number of samples to skip.  
---|---  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property skip#
    

The number of samples to skip.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.SortBy(_field_or_expr_ , _reverse =False_, _create_index =False_)#
    

Bases: `ViewStage`

Sorts the samples in a collection by the given field(s) or expression(s).

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    #
    # Sort the samples by their `uniqueness` field in ascending order
    #
    
    stage = fo.SortBy("uniqueness", reverse=False)
    view = dataset.add_stage(stage)
    
    #
    # Sorts the samples in descending order by the number of detections in
    # their `predictions` field whose bounding box area is less than 0.2
    #
    
    # Bboxes are in [top-left-x, top-left-y, width, height] format
    bbox = F("bounding_box")
    bbox_area = bbox[2] * bbox[3]
    
    small_boxes = F("predictions.detections").filter(bbox_area < 0.2)
    stage = fo.SortBy(small_boxes.length(), reverse=True)
    view = dataset.add_stage(stage)
    
    #
    # Performs a compound sort where samples are first sorted in descending
    # order by number of detections and then in ascending order of
    # uniqueness for samples with the same number of predictions
    #
    
    stage = fo.SortBy(
        [
            (F("predictions.detections").length(), -1),
            ("uniqueness", 1),
        ]
    )
    view = dataset.add_stage(stage)
    
    num_objects, uniqueness = view[:5].values(
        [F("predictions.detections").length(), "uniqueness"]
    )
    print(list(zip(num_objects, uniqueness)))
    

Parameters:
    

  * **field_or_expr** â 

the field(s) or expression(s) to sort by. This can be any of the following:

    * a field to sort by

    * an `embedded.field.name` to sort by

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") or a [MongoDB aggregation expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#aggregation-expressions) that defines the quantity to sort by

    * a list of `(field_or_expr, order)` tuples defining a compound sort criteria, where `field_or_expr` is a field or expression as defined above, and `order` can be 1 or any string starting with âaâ for ascending order, or -1 or any string starting with âdâ for descending order

  * **reverse** (_False_) â whether to return the results in descending order

  * **create_index** (_False_) â whether to create an index, if necessary, to optimize the sort. Only applicable when sorting by field(s), not expressions




**Attributes:**

`field_or_expr` | The field or expression to sort by.  
---|---  
`reverse` | Whether to return the results in descending order.  
`create_index` | Whether to create an index, if necessary, to optimize the sort.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property field_or_expr#
    

The field or expression to sort by.

property reverse#
    

Whether to return the results in descending order.

property create_index#
    

Whether to create an index, if necessary, to optimize the sort.

to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.SortBySimilarity(_query_ , _k =None_, _reverse =False_, _dist_field =None_, _brain_key =None_, __state =None_)#
    

Bases: `ViewStage`

Sorts a collection by similarity to a specified query.

In order to use this stage, you must first use [`fiftyone.brain.compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") to index your dataset by similarity.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.brain as fob
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    fob.compute_similarity(
        dataset, model="clip-vit-base32-torch", brain_key="clip"
    )
    
    #
    # Sort samples by their similarity to a sample by its ID
    #
    
    query_id = dataset.first().id
    
    stage = fo.SortBySimilarity(query_id, k=5)
    view = dataset.add_stage(stage)
    
    #
    # Sort samples by their similarity to a manually computed vector
    #
    
    model = foz.load_zoo_model("clip-vit-base32-torch")
    embeddings = dataset.take(2, seed=51).compute_embeddings(model)
    query = embeddings.mean(axis=0)
    
    stage = fo.SortBySimilarity(query, k=5)
    view = dataset.add_stage(stage)
    
    #
    # Sort samples by their similarity to a text prompt
    #
    
    query = "kites high in the air"
    
    stage = fo.SortBySimilarity(query, k=5)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **query** â 

the query, which can be any of the following:

    * an ID or iterable of IDs

    * a `num_dims` vector or `num_queries x num_dims` array of vectors

    * a prompt or iterable of prompts (if supported by the index)

  * **k** (_None_) â the number of matches to return. By default, the entire collection is sorted

  * **reverse** (_False_) â whether to sort by least similarity (True) or greatest similarity (False). Some backends may not support least similarity

  * **dist_field** (_None_) â the name of a float field in which to store the distance of each example to the specified query. The field is created if necessary

  * **brain_key** (_None_) â the brain key of an existing [`fiftyone.brain.compute_similarity()`](https://docs.voxel51.com/api/fiftyone.brain.html#fiftyone.brain.compute_similarity "fiftyone.brain.compute_similarity") run on the dataset. If not specified, the dataset must have an applicable run, which will be used by default




**Attributes:**

`query` | The query.  
---|---  
`k` | The number of matches to return.  
`reverse` | Whether to sort by least similarity.  
`dist_field` | The field to store similarity distances, if any.  
`brain_key` | The brain key of the similarity index to use.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
  
property query#
    

The query.

property k#
    

The number of matches to return.

property reverse#
    

Whether to sort by least similarity.

property dist_field#
    

The field to store similarity distances, if any.

property brain_key#
    

The brain key of the similarity index to use.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




class fiftyone.core.stages.Take(_size_ , _seed =None_, __randint =None_)#
    

Bases: `ViewStage`

Randomly samples the given number of samples from a collection.

Examples:
    
    
    import fiftyone as fo
    
    dataset = fo.Dataset()
    dataset.add_samples(
        [
            fo.Sample(
                filepath="/path/to/image1.png",
                ground_truth=fo.Classification(label="cat"),
            ),
            fo.Sample(
                filepath="/path/to/image2.png",
                ground_truth=fo.Classification(label="dog"),
            ),
            fo.Sample(
                filepath="/path/to/image3.png",
                ground_truth=fo.Classification(label="rabbit"),
            ),
            fo.Sample(
                filepath="/path/to/image4.png",
                ground_truth=None,
            ),
        ]
    )
    
    #
    # Take two random samples from the dataset
    #
    
    stage = fo.Take(2)
    view = dataset.add_stage(stage)
    
    #
    # Take two random samples from the dataset with a fixed seed
    #
    
    stage = fo.Take(2, seed=51)
    view = dataset.add_stage(stage)
    

Parameters:
    

  * **size** â the number of samples to return. If a non-positive number is provided, an empty view is returned

  * **seed** (_None_) â an optional random seed to use when selecting the samples




**Attributes:**

`size` | The number of samples to return.  
---|---  
`seed` | The random seed to use, or `None`.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`to_mongo`(_) | Returns the MongoDB aggregation pipeline for the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property size#
    

The number of samples to return.

property seed#
    

The random seed to use, or `None`.

to_mongo(___)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.ToPatches(_field_ , _config =None_, __state =None_, _** kwargs_)#
    

Bases: `ViewStage`

Creates a view that contains one sample per object patch in the specified field of a collection.

A `sample_id` field will be added that records the sample ID from which each patch was taken.

By default, fields other than `field` and the default sample fields will not be included in the returned view.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    
    session = fo.launch_app(dataset)
    
    #
    # Create a view containing the ground truth patches
    #
    
    stage = fo.ToPatches("ground_truth")
    view = dataset.add_stage(stage)
    print(view)
    
    session.view = view
    

Parameters:
    

  * **field** â the patches field, which must be of type [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines"), or [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **config** (_None_) â an optional dict of keyword arguments for [`fiftyone.core.patches.make_patches_dataset()`](api__fiftyone.core.patches.md#fiftyone.core.patches.make_patches_dataset "fiftyone.core.patches.make_patches_dataset") specifying how to perform the conversion

  * ****kwargs** â optional keyword arguments for [`fiftyone.core.patches.make_patches_dataset()`](api__fiftyone.core.patches.md#fiftyone.core.patches.make_patches_dataset "fiftyone.core.patches.make_patches_dataset") specifying how to perform the conversion




**Attributes:**

`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
---|---  
`field` | The patches field.  
`config` | Parameters specifying how to perform the conversion.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

property field#
    

The patches field.

property config#
    

Parameters specifying how to perform the conversion.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.ToEvaluationPatches(_eval_key_ , _config =None_, __state =None_, _** kwargs_)#
    

Bases: `ViewStage`

Creates a view based on the results of the evaluation with the given key that contains one sample for each true positive, false positive, and false negative example in the collection, respectively.

True positive examples will result in samples with both their ground truth and predicted fields populated, while false positive/negative examples wilL only have one of their corresponding predicted/ground truth fields populated, respectively.

If multiple predictions are matched to a ground truth object (e.g., if the evaluation protocol includes a crowd attribute), then all matched predictions will be stored in the single sample along with the ground truth object.

The returned dataset will also have top-level `type` and `iou` fields populated based on the evaluation results for that example, as well as a `sample_id` field recording the sample ID of the example, and a `crowd` field if the evaluation protocol defines a crowd attribute.

Note

The returned view will contain patches for the contents of this collection, which may differ from the view on which the `eval_key` evaluation was performed. This may exclude some labels that were evaluated and/or include labels that were not evaluated.

If you would like to see patches for the exact view on which an evaluation was performed, first call [`load_evaluation_view()`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection.load_evaluation_view "fiftyone.core.collections.SampleCollection.load_evaluation_view") to load the view and then convert to patches.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    
    dataset = foz.load_zoo_dataset("quickstart")
    dataset.evaluate_detections("predictions", eval_key="eval")
    
    session = fo.launch_app(dataset)
    
    #
    # Create a patches view for the evaluation results
    #
    
    stage = fo.ToEvaluationPatches("eval")
    view = dataset.add_stage(stage)
    print(view)
    
    session.view = view
    

Parameters:
    

  * **eval_key** â an evaluation key that corresponds to the evaluation of ground truth/predicted fields that are of type [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections"), `fiftyone.core.labels.Polylines, or :class:`fiftyone.core.labels.Keypoints`

  * **config** (_None_) â an optional dict of keyword arguments for [`fiftyone.core.patches.make_evaluation_patches_dataset()`](api__fiftyone.core.patches.md#fiftyone.core.patches.make_evaluation_patches_dataset "fiftyone.core.patches.make_evaluation_patches_dataset") specifying how to perform the conversion

  * ****kwargs** â optional keyword arguments for [`fiftyone.core.patches.make_evaluation_patches_dataset()`](api__fiftyone.core.patches.md#fiftyone.core.patches.make_evaluation_patches_dataset "fiftyone.core.patches.make_evaluation_patches_dataset") specifying how to perform the conversion




**Attributes:**

`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
---|---  
`eval_key` | The evaluation key to extract patches for.  
`config` | Parameters specifying how to perform the conversion.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

property eval_key#
    

The evaluation key to extract patches for.

property config#
    

Parameters specifying how to perform the conversion.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.ToClips(_field_or_expr_ , _config =None_, __state =None_, _** kwargs_)#
    

Bases: `ViewStage`

Creates a view that contains one sample per clip defined by the given field or expression in a video collection.

The returned view will contain:

  * A `sample_id` field that records the sample ID from which each clip was taken

  * A `support` field that records the `[first, last]` frame support of each clip

  * All frame-level information from the underlying dataset of the input collection




Refer to [`fiftyone.core.clips.make_clips_dataset()`](api__fiftyone.core.clips.md#fiftyone.core.clips.make_clips_dataset "fiftyone.core.clips.make_clips_dataset") to see the available configuration options for generating clips.

Note

The clip generation logic will respect any frame-level modifications defined in the input collection, but the output clips will always contain all frame-level labels.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    #
    # Create a clips view that contains one clip for each contiguous
    # segment that contains at least one road sign in every frame
    #
    
    stage1 = fo.FilterLabels("frames.detections", F("label") == "road sign")
    stage2 = fo.ToClips("frames.detections")
    clips = dataset.add_stage(stage1).add_stage(stage2)
    print(clips)
    
    #
    # Create a clips view that contains one clip for each contiguous
    # segment that contains at least two road signs in every frame
    #
    
    signs = F("detections.detections").filter(F("label") == "road sign")
    stage = fo.ToClips(signs.length() >= 2)
    clips = dataset.add_stage(stage)
    print(clips)
    

Parameters:
    

  * **field_or_expr** â 

can be any of the following:

    * a [`fiftyone.core.labels.TemporalDetection`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetection "fiftyone.core.labels.TemporalDetection"), [`fiftyone.core.labels.TemporalDetections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.TemporalDetections "fiftyone.core.labels.TemporalDetections"), [`fiftyone.core.fields.FrameSupportField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FrameSupportField "fiftyone.core.fields.FrameSupportField"), or list of [`fiftyone.core.fields.FrameSupportField`](api__fiftyone.core.fields.md#fiftyone.core.fields.FrameSupportField "fiftyone.core.fields.FrameSupportField") field

    * a frame-level label list field of any of the following types:

      * [`fiftyone.core.labels.Classifications`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Classifications "fiftyone.core.labels.Classifications")

      * [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

      * [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

      * [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

    * a [`fiftyone.core.expressions.ViewExpression`](api__fiftyone.core.expressions.md#fiftyone.core.expressions.ViewExpression "fiftyone.core.expressions.ViewExpression") that returns a boolean to apply to each frame of the input collection to determine if the frame should be clipped

    * a list of `[(first1, last1), (first2, last2), ...]` lists defining the frame numbers of the clips to extract from each sample

  * **config** (_None_) â an optional dict of keyword arguments for [`fiftyone.core.clips.make_clips_dataset()`](api__fiftyone.core.clips.md#fiftyone.core.clips.make_clips_dataset "fiftyone.core.clips.make_clips_dataset") specifying how to perform the conversion

  * ****kwargs** â optional keyword arguments for [`fiftyone.core.clips.make_clips_dataset()`](api__fiftyone.core.clips.md#fiftyone.core.clips.make_clips_dataset "fiftyone.core.clips.make_clips_dataset") specifying how to perform the conversion




**Attributes:**

`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
---|---  
`field_or_expr` | The field or expression defining how to extract the clips.  
`config` | Parameters specifying how to perform the conversion.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

property field_or_expr#
    

The field or expression defining how to extract the clips.

property config#
    

Parameters specifying how to perform the conversion.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.ToTrajectories(_field_ , _config =None_, __state =None_, _** kwargs_)#
    

Bases: `ViewStage`

Creates a view that contains one clip for each unique object trajectory defined by their `(label, index)` in a frame-level field of a video collection.

The returned view will contain:

  * A `sample_id` field that records the sample ID from which each clip was taken

  * A `support` field that records the `[first, last]` frame support of each clip

  * A sample-level label field that records the `label` and `index` of each trajectory




Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    #
    # Create a trajectories view for the vehicles in the dataset
    #
    
    stage1 = fo.FilterLabels("frames.detections", F("label") == "vehicle")
    stage2 = fo.ToTrajectories("frames.detections")
    trajectories = dataset.add_stage(stage1).add_stage(stage2)
    
    print(trajectories)
    

Parameters:
    

  * **field** â 

a frame-level label list field of any of the following types:

    * [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections")

    * [`fiftyone.core.labels.Polylines`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Polylines "fiftyone.core.labels.Polylines")

    * [`fiftyone.core.labels.Keypoints`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Keypoints "fiftyone.core.labels.Keypoints")

  * **config** (_None_) â an optional dict of keyword arguments for [`fiftyone.core.clips.make_clips_dataset()`](api__fiftyone.core.clips.md#fiftyone.core.clips.make_clips_dataset "fiftyone.core.clips.make_clips_dataset") specifying how to perform the conversion

  * ****kwargs** â optional keyword arguments for [`fiftyone.core.clips.make_clips_dataset()`](api__fiftyone.core.clips.md#fiftyone.core.clips.make_clips_dataset "fiftyone.core.clips.make_clips_dataset") specifying how to perform the conversion




**Attributes:**

`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
---|---  
`field` | The label field for which to extract trajectories.  
`config` | Parameters specifying how to perform the conversion.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

property field#
    

The label field for which to extract trajectories.

property config#
    

Parameters specifying how to perform the conversion.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

class fiftyone.core.stages.ToFrames(_config =None_, __state =None_, _** kwargs_)#
    

Bases: `ViewStage`

Creates a view that contains one sample per frame in a video collection.

The returned view will contain all frame-level fields and the `tags` of each video as sample-level fields, as well as a `sample_id` field that records the IDs of the parent sample for each frame.

By default, `sample_frames` is False and this method assumes that the frames of the input collection have `filepath` fields populated pointing to each frame image. Any frames without a `filepath` populated will be omitted from the returned view.

When `sample_frames` is True, this method samples each video in the collection into a directory of per-frame images and stores the filepaths in the `filepath` frame field of the source dataset. By default, each folder of images is written using the same basename as the input video. For example, if `frames_patt = "%%06d.jpg"`, then videos with the following paths:
    
    
    /path/to/video1.mp4
    /path/to/video2.mp4
    ...
    

would be sampled as follows:
    
    
    /path/to/video1/
        000001.jpg
        000002.jpg
        ...
    /path/to/video2/
        000001.jpg
        000002.jpg
        ...
    

However, you can use the optional `output_dir` and `rel_dir` parameters to customize the location and shape of the sampled frame folders. For example, if `output_dir = "/tmp"` and `rel_dir = "/path/to"`, then videos with the following paths:
    
    
    /path/to/folderA/video1.mp4
    /path/to/folderA/video2.mp4
    /path/to/folderB/video3.mp4
    ...
    

would be sampled as follows:
    
    
    /tmp/folderA/
        video1/
            000001.jpg
            000002.jpg
            ...
        video2/
            000001.jpg
            000002.jpg
            ...
    /tmp/folderB/
        video3/
            000001.jpg
            000002.jpg
            ...
    

By default, samples will be generated for every video frame at full resolution, but this method provides a variety of parameters that can be used to customize the sampling behavior.

Note

If this method is run multiple times with `sample_frames` set to True, existing frames will not be resampled unless you set `force_sample` to True.

Examples:
    
    
    import fiftyone as fo
    import fiftyone.zoo as foz
    from fiftyone import ViewField as F
    
    dataset = foz.load_zoo_dataset("quickstart-video")
    
    session = fo.launch_app(dataset)
    
    #
    # Create a frames view for an entire video dataset
    #
    
    stage = fo.ToFrames(sample_frames=True)
    frames = dataset.add_stage(stage)
    print(frames)
    
    session.view = frames
    
    #
    # Create a frames view that only contains frames with at least 10
    # objects, sampled at a maximum frame rate of 1fps
    #
    
    num_objects = F("detections.detections").length()
    view = dataset.match_frames(num_objects > 10)
    
    stage = fo.ToFrames(max_fps=1)
    frames = view.add_stage(stage)
    print(frames)
    
    session.view = frames
    

Parameters:
    

  * **config** (_None_) â an optional dict of keyword arguments for [`fiftyone.core.video.make_frames_dataset()`](api__fiftyone.core.video.md#fiftyone.core.video.make_frames_dataset "fiftyone.core.video.make_frames_dataset") specifying how to perform the conversion

  * ****kwargs** â optional keyword arguments for [`fiftyone.core.video.make_frames_dataset()`](api__fiftyone.core.video.md#fiftyone.core.video.make_frames_dataset "fiftyone.core.video.make_frames_dataset") specifying how to perform the conversion




**Attributes:**

`has_view` | Whether this stage's output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.  
---|---  
`config` | Parameters specifying how to perform the conversion.  
`flattens_groups` | Whether this stage flattens groups into a non-grouped collection.  
`outputs_dynamic_groups` | Whether this stage outputs or flattens dynamic groups.  
  
**Methods:**

`load_view`(sample_collection[,Â saved_view,Â ...]) | Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.  
---|---  
`get_edited_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.  
`get_excluded_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been excluded by the stage, if any.  
`get_filtered_fields`(sample_collection[,Â frames]) | Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.  
`get_group_expr`(sample_collection) | Returns the dynamic group expression for the given stage, if any.  
`get_group_media_types`(sample_collection) | Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.  
`get_media_type`(sample_collection) | Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.  
`get_selected_fields`(sample_collection[,Â frames]) | Returns a list of fields that have been selected by the stage, if any.  
`to_mongo`(sample_collection) | Returns the MongoDB aggregation pipeline for the stage.  
`validate`(sample_collection) | Validates that the stage can be applied to the given collection.  
  
property has_view#
    

Whether this stageâs output view should be loaded via `load_view()` rather than appending stages to an aggregation pipeline via `to_mongo()`.

property config#
    

Parameters specifying how to perform the conversion.

load_view(_sample_collection_ , _saved_view =False_, _reload =False_)#
    

Loads the [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView") containing the output of the stage.

Only usable if `has_view()` is `True`.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **saved_view** (_False_) â whether this view stage is being loaded in the context of loading a saved view

  * **reload** (_False_) â whether to force reload generated collections, if necessary



Returns:
    

a [`fiftyone.core.view.DatasetView`](api__fiftyone.core.view.md#fiftyone.core.view.DatasetView "fiftyone.core.view.DatasetView")

property flattens_groups#
    

Whether this stage flattens groups into a non-grouped collection.

The possible return values are:

  * `True`: this stage _flattens_ groups

  * `False`: this stage _does not flatten_ groups

  * `None`: this stage does not change group status




get_edited_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that may have been edited by the stage, if any.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been edited

get_excluded_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been excluded by the stage, if any.

View stages only need to report excluded fields if they insist that excluded fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

get_filtered_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of names of fields or embedded fields that contain **arrays** have been filtered by the stage, if any.

For example, if a stage filters a [`fiftyone.core.labels.Detections`](https://docs.voxel51.com/api/fiftyone.core.labels.html#fiftyone.core.labels.Detections "fiftyone.core.labels.Detections") field called `"predictions"`, it should include `"predictions.detections"` in the returned list.

The `"frames."` prefix should be omitted when `frames` is True.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been filtered

get_group_expr(_sample_collection_)#
    

Returns the dynamic group expression for the given stage, if any.

Only usable if `outputs_dynamic_groups()` is `True`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a tuple of

  * the group expression, or `None` if the stage does not generate dynamic groups

  * whether the group expression is an ObjectId field, or `None`




get_group_media_types(_sample_collection_)#
    

Returns the group media types outputted by this stage, if any, when applied to the given collection, if and only if they are different from the input collection.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a dict mapping slice names to media types, or `None` if the stage does not change the types

get_media_type(_sample_collection_)#
    

Returns the media type outputted by this stage when applied to the given collection, if and only if it is different from the input type.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

the media type, or `None` if the stage does not change the type

get_selected_fields(_sample_collection_ , _frames =False_)#
    

Returns a list of fields that have been selected by the stage, if any.

View stages only need to report selected fields if they insist that non-selected fields not appear in the schema of the returned view.

Parameters:
    

  * **sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

  * **frames** (_False_) â whether to return sample-level (False) or frame-level (True) fields



Returns:
    

a list of fields, or `None` if no fields have been selected

property outputs_dynamic_groups#
    

Whether this stage outputs or flattens dynamic groups.

The possible return values are:

  * `True`: this stage _dynamically groups_ the input collection

  * `False`: this stage _flattens_ dynamic groups

  * `None`: this stage does not change group status




to_mongo(_sample_collection_)#
    

Returns the MongoDB aggregation pipeline for the stage.

Only usable if `has_view()` is `False`.

Parameters:
    

**sample_collection** â the [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection") to which the stage is being applied

Returns:
    

a MongoDB aggregation pipeline (list of dicts)

validate(_sample_collection_)#
    

Validates that the stage can be applied to the given collection.

Parameters:
    

**sample_collection** â a [`fiftyone.core.collections.SampleCollection`](api__fiftyone.core.collections.md#fiftyone.core.collections.SampleCollection "fiftyone.core.collections.SampleCollection")

Raises:
    

**ViewStageError** â if the stage cannot be applied to the collection

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
